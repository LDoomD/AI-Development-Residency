// Run: node --test .claude/hooks/dogfood-handoff-trigger.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const hook = join(dirname(fileURLToPath(import.meta.url)), "dogfood-handoff-trigger.mjs");

function run(prompt) {
  const r = spawnSync(process.execPath, [hook], { input: JSON.stringify({ prompt }), encoding: "utf8" });
  assert.equal(r.status, 0);
  return r.stdout ? JSON.parse(r.stdout).hookSpecificOutput.additionalContext : "";
}

const FIRES = {
  write: [
    "write the handoff report",
    "let's do a dog feeding report first",
    "before I compact the context, let's do a dog feeding report first",
    "can you do the dock fitting report please",
    "give me a handoff report",
    "I need a handoff before I clear",
    "write me the report i'll feed you tomorrow",
    "can you write up a dogfood doc for the next milestone",
  ],
  receive: [
    "read this handoff",
    'let\'s pick up where we left off',
    '@"/Users/x/Dog Feeding Docs/Week 2_3/dogfood-2026-11-05-handoff-skill-evals.md" review this',
    "here's my handoff, read it first",
  ],
  wrap: [
    "warp up Is that everybody reached my limit?",
    "wrap up, I reached my limit",
    "ok wrapping up for tonight",
    "calling it a day",
    "done for today",
    "wrap this up so i can start fresh in the morning",
    "let's wrap it up",
  ],
};

const SILENT = [
  "> ok let's wrap up for today",
  "why doesn't my wrap up skill merge?",
  "the wrap-up skill needs a change",
  "what does handoff mean in the OAuth device flow?",
  "open the Dog Feeding Docs folder and list the files",
  'Another Claude session sent a message:\n<agent-message from="a1">\n[Subagent hand-back] handoff report done',
  "<task-notification> handoff report done",
  "[SYSTEM NOTIFICATION - NOT USER INPUT] wrap up",
  "fix the login bug in auth.js",
  "can you summarize this article for my team",
  "wrap the price label in a span so I can style it",
];

for (const [mode, list] of Object.entries(FIRES)) {
  for (const p of list) {
    test(`fires (${mode}): ${p.slice(0, 60)}`, () => {
      const ctx = run(p);
      assert.notEqual(ctx, "", "expected the hook to fire");
      const expect = { write: "may be a request for a handoff", receive: "being fed in", wrap: "ending the session" }[mode];
      assert.ok(ctx.includes(expect), `wrong mode: ${ctx.slice(0, 50)}`);
    });
  }
}
for (const p of SILENT) {
  test(`silent: ${p.slice(0, 60).replace(/\n/g, " ")}`, () => assert.equal(run(p), ""));
}
