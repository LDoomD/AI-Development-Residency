// Run: node --test .claude/hooks/invest-trigger.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const hook = join(dirname(fileURLToPath(import.meta.url)), "invest-trigger.mjs");

function run(prompt) {
  const r = spawnSync(process.execPath, [hook], { input: JSON.stringify({ prompt }), encoding: "utf8" });
  assert.equal(r.status, 0);
  return r.stdout ? JSON.parse(r.stdout).hookSpecificOutput.additionalContext : "";
}

const FIRES = {
  scope: [
    "let's use INVEST to audit this feature",
    "write a user story for letting a caregiver request a break",
    "split this task: build the caregiver dashboard",
    "can you break this down into tasks",
    "add acceptance criteria to the story",
    "write Given When Then scenarios for login",
    "please right-size the backlog",
    "can you break this feature down into smaller tasks I can build in a week",
    "my teacher wants the backlog in epics, features and tasks",
    "write Given/When/Then scenarios for the login story",
  ],
  deliverable: [
    "okay let's work on this new deliverable",
    "ready for the next deliverable",
    "let's start the feature analysis",
    "begin the release vision",
    "let's work on positioning",
  ],
};

const SILENT = [
  "> let's use INVEST to audit this feature",
  "I want to invest more time in the research",
  "what is a deliverable?",
  "review the feature analysis table",
  "fix the typo in the README heading",
  "summarize the market analysis in two lines",
  "open the Dog Feeding Docs folder",
  'Another Claude session sent a message:\n<agent-message from="a1">\n[Subagent hand-back] wrote a user story',
  "<task-notification> user story done",
  "[SYSTEM NOTIFICATION - NOT USER INPUT] split this task",
];

for (const [mode, list] of Object.entries(FIRES)) {
  for (const p of list) {
    test(`fires (${mode}): ${p.slice(0, 60)}`, () => {
      const ctx = run(p);
      assert.notEqual(ctx, "", "expected the hook to fire");
      const expect = { scope: "request to scope work", deliverable: "new deliverable is starting" }[mode];
      assert.ok(ctx.includes(expect), `wrong mode: ${ctx.slice(0, 50)}`);
    });
  }
}
for (const p of SILENT) {
  test(`silent: ${p.slice(0, 60).replace(/\n/g, " ")}`, () => assert.equal(run(p), ""));
}
