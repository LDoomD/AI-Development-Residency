#!/usr/bin/env node
// UserPromptSubmit hook for the dogfooding-handoff skill (user level, any project).
// Fires only when the prompt sounds like writing or receiving a handoff report.
// Prints nothing otherwise, so it costs no tokens on other messages.
import { readFileSync } from "node:fs";

let prompt = "";
try {
  prompt = JSON.parse(readFileSync(0, "utf8")).prompt || "";
} catch {
  process.exit(0);
}

// Skip messages that are not typed by the user: subagent hand-backs, messages
// from other sessions, and system or app event frames. These often contain the
// word "handoff" and caused false fires (seen 2026-11-05).
const head = prompt.trimStart().slice(0, 300);
const NOT_USER =
  /^(Another Claude session sent a message|\[SYSTEM NOTIFICATION|<(agent-message|teammate-message|task-notification|system-reminder|side-sessions-event|ci-monitor-event|local-command|command-name)\b)/i;
if (NOT_USER.test(head)) process.exit(0);

const WRITE = /\b(hand-?off|dog ?f(ee|oo)d(ing)?|before (i|we) (compact|clear|close|stop|end)|new (chat|session|conversation)|start (over|fresh)|feed (you|claude|it)|(write|make|give|create) (me )?(a |the |my )?(session |progress |end[- ]of[- ]day )?(report|recap|summary)|wrap (this |it |things )?up)\b/i;
// Session-ending phrases, including the common typo "warp up".
const WRAP = /\b((wrap|warp)(ping)? (this |it |things )?up|call(ing)? it (a day|a night|for (today|tonight))|done for (today|tonight|the day))\b/i;
const RECEIVE = /\b(pick up where|where (we|i) left off|here'?s (my|the) (report|handoff|summary)|read (this|my|the) (report|handoff) first|continue from (this|my|the) (report|handoff))\b/i;

let mode = null;
if (RECEIVE.test(prompt)) mode = "receive";
else if (WRAP.test(prompt)) mode = "wrap";
else if (WRITE.test(prompt)) mode = "write";
if (!mode) process.exit(0);

const context = {
  receive:
    "This looks like a handoff report being fed in. Use the dogfooding-handoff skill (receive mode): read the report and the files it lists, say what is present or missing, confirm where we are, then follow its first steps and stop where it says to.",
  wrap:
    "The user is ending the session. If a wrap-up skill is available, run it. Make sure the work can continue later: use the dogfooding-handoff skill (write mode) for the handoff report, or update the newest one, unless nothing changed since it was written.",
  write:
    "This may be a request for a handoff report so work can continue in a new or compacted session. If so, use the dogfooding-handoff skill (write mode). If the report is for other people (a status update, release notes), it does not apply.",
}[mode];

process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: "UserPromptSubmit", additionalContext: context } }));
