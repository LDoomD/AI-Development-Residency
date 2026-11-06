#!/usr/bin/env node
// UserPromptSubmit hook for the dogfooding-handoff skill (user level, any project).
// Fires only when the owner's message asks for, or feeds in, a handoff / dog feeding
// report, or says the session is ending. Prints nothing otherwise (no token cost).
//
// Narrowed 2026-11-06: fewer, specific phrases. Broad words such as "handoff" alone,
// "new chat", "start fresh" no longer fire. The skill's own description still covers
// those casual phrasings. Phrases that should have fired and didn't go in
// dogfood-handoff-misses.md, then into the lists below.
import { readFileSync } from "node:fs";

let prompt = "";
try {
  prompt = JSON.parse(readFileSync(0, "utf8")).prompt || "";
} catch {
  process.exit(0);
}

// 1. Skip messages the owner didn't type: helper-agent reports, other sessions, system frames.
const head = prompt.trimStart().slice(0, 300);
const NOT_USER =
  /^(Another Claude session sent a message|\[SYSTEM NOTIFICATION|<(agent-message|teammate-message|task-notification|system-reminder|side-sessions-event|ci-monitor-event|local-command|command-name)\b)/i;
if (NOT_USER.test(head)) process.exit(0);

// 2. Skip quoted lines (start with ">"): the owner often quotes Claude's earlier words.
let text = prompt
  .split("\n")
  .filter((line) => !/^\s*>/.test(line))
  .join("\n");

// 3. Skip talk ABOUT the wrap-up skill ("my wrap up skill", "the wrap-up routine").
text = text
  .replace(/\b(my|the|your|this|that|our)\s+(wrap|warp)[- ]?up\b(\s+(skill|routine|hook|step|process|command))?/gi, " ")
  .replace(/\b(wrap|warp)[- ]?up\s+(skill|routine|hook|step|process|command)\b/gi, " ");

// "dog feeding" as the owner says it, including speech-to-text slips seen in chat
// (dock/dark fitting). The word after it must be report/handoff/brief, so the folder name
// "Dog Feeding Docs" never fires.
const DOG = "(dog|dock|dark)[ -]?(feed|food|fitt?)(ing|er)?";

const RECEIVE = new RegExp(
  [
    "\\bpick up where\\b",
    "\\bwhere (we|i) left off\\b",
    "\\bhere'?s (my|the) (report|handoff|hand-off)\\b",
    "\\bread (this|my|the) (handoff|hand-off|report|" + DOG + " report) first\\b",
    "\\bread this (handoff|hand-off)\\b",
    "\\bcontinue from (this|my|the) (report|handoff|hand-off)\\b",
    "\\bdogfood-\\d{4}-\\d{2}-\\d{2}[\\w-]*\\.md\\b", // a dragged-in report file
  ].join("|"),
  "i",
);

// Session ending (also the typo "warp up"). Routes to the project's wrap-up skill.
const WRAP = /\b((wrap|warp)(ping)?([- ]| (this|it|things|everything) )up|call(ing)? it (a day|a night|for (today|tonight))|done for (today|tonight|the day))\b/i;

const WRITE = new RegExp(
  [
    "\\bhand-?off (report|doc|document|brief)\\b",
    "\\b" + DOG + "[ -]?(report|handoff|hand-off|brief|doc|document)\\b", // "doc" singular only: the folder is "Dog Feeding Docs"
    "\\b(write|make|give|create|need|want) (me )?(a |the |my )?hand-?off\\b",
    "\\bbefore (i|we) (compact|clear)\\b",
    "\\bfeed (you|claude) (the|this|that|a|my) (report|handoff|brief)\\b",
    "\\breport (i'?ll|i will|to) feed\\b",
  ].join("|"),
  "i",
);

let mode = null;
if (RECEIVE.test(text)) mode = "receive";
else if (WRAP.test(text)) mode = "wrap";
else if (WRITE.test(text)) mode = "write";
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
