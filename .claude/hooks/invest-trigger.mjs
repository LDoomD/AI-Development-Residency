#!/usr/bin/env node
// UserPromptSubmit hook for the invest-task-scoping skill.
// Fires on specific phrases: scoping words ("INVEST", "user story", "split this task",
// "acceptance criteria") and the start of a new deliverable. Prints nothing otherwise.
// Phrases that should have fired and didn't go in
// .claude/skills/invest-task-scoping/references/misses.md.
import { readFileSync } from "node:fs";

let prompt = "";
try {
  prompt = JSON.parse(readFileSync(0, "utf8")).prompt || "";
} catch {
  process.exit(0);
}

// Skip messages the owner didn't type: helper-agent reports, other sessions, system frames.
const head = prompt.trimStart().slice(0, 300);
const NOT_USER =
  /^(Another Claude session sent a message|\[SYSTEM NOTIFICATION|<(agent-message|teammate-message|task-notification|system-reminder|side-sessions-event|ci-monitor-event|local-command|command-name)\b)/i;
if (NOT_USER.test(head)) process.exit(0);

// Skip quoted lines (start with ">").
const text = prompt
  .split("\n")
  .filter((line) => !/^\s*>/.test(line))
  .join("\n");

// "INVEST" in capitals only, so the ordinary word "invest" never fires.
const SCOPING = new RegExp(
  [
    "\\bINVEST\\b",
    "\\binvest (method|skill|audit|checklist|criteria)\\b",
    "\\buser stor(y|ies)\\b",
    "\\bsplit (this|that|the|these) (task|story|stories|feature|epic|ticket)s?\\b",
    "\\bbreak (this|that|it|these|them)( \\w+)? (down|up|into)\\b.{0,30}\\b(tasks?|stories|story|pieces)\\b",
    "\\bepics?,? (and )?features?,? (and )?tasks\\b",
    "\\bacceptance criteria\\b",
    "\\bgiven[ ,/]+when[ ,/]+then\\b",
    "\\bright-?size\\b",
  ].join("|"),
);
const SCOPING_CI = new RegExp(SCOPING.source.replace("\\bINVEST\\b|", ""), "i");

const DELIVERABLE = new RegExp(
  [
    "\\b(new|next) deliverable\\b",
    "\\b(start|begin|work on|working on|let'?s (do|work on|start|begin))( on)?( the| our| a)?( next| new)? (feature analysis|positioning|unique value proposition|release vision|vision boards?|backlog|epics?)\\b",
  ].join("|"),
  "i",
);

let mode = null;
if (DELIVERABLE.test(text)) mode = "deliverable";
else if (SCOPING.test(text) || SCOPING_CI.test(text)) mode = "scope";
if (!mode) process.exit(0);

const context =
  mode === "deliverable"
    ? "A new deliverable is starting. First check that the last deliverable's pull request is merged (`gh pr list --state open`; the project's CLAUDE.md asks for this) and say one line if it isn't. Then offer to run the invest-task-scoping skill on the new deliverable. It is an offer: the owner decides."
    : "This looks like a request to scope work or write user stories. Use the invest-task-scoping skill: grade the six INVEST letters, split what is too big, and wait for approval after each story.";

process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: "UserPromptSubmit", additionalContext: context } }));
