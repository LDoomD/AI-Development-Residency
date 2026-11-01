// Run: node --test .claude/skills/judge-arch/test/hook.test.mjs
// Feeds the PreToolUse hook the same JSON Claude Code sends and checks the exit code.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const GATE = path.join(HERE, '..', 'scripts', 'arch-gate.mjs');
const HOOK = path.join(HERE, '..', '..', '..', 'hooks', 'arch-gate-before-commit.mjs');
const DIRECTIVE = path.join(HERE, '..', '..', '..', 'hooks', 'emit-skills-directive.mjs');

function project(files, withGate = true) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'arch-hook-'));
  if (withGate) {
    const dest = path.join(dir, '.claude', 'skills', 'judge-arch', 'scripts');
    fs.mkdirSync(dest, { recursive: true });
    fs.copyFileSync(GATE, path.join(dest, 'arch-gate.mjs'));
  }
  for (const [rel, content] of Object.entries(files)) {
    fs.mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true });
    fs.writeFileSync(path.join(dir, rel), content);
  }
  return dir;
}
const hook = (dir, command) => spawnSync(process.execPath, [HOOK], {
  input: JSON.stringify({ tool_input: { command } }),
  env: { ...process.env, CLAUDE_PROJECT_DIR: dir },
  encoding: 'utf8',
});

test('commands that are not commit or PR creation are allowed without running the gate', () => {
  const dir = project({ 'src/bad.js': 'try { f(); } catch (e) {}\n' });
  assert.equal(hook(dir, 'ls -la').status, 0);
  assert.equal(hook(dir, 'git status').status, 0);
});

test('git commit is blocked (exit 2) when the gate finds a violation', () => {
  const dir = project({ 'src/bad.js': 'try { f(); } catch (e) {}\n' });
  const r = hook(dir, 'git commit -m "x"');
  assert.equal(r.status, 2, r.stderr);
  assert.match(r.stderr, /emptyCatch/);
});

test('gh pr create is blocked when the gate finds a violation', () => {
  const dir = project({ 'src/bad.js': 'try { f(); } catch (e) {}\n' });
  assert.equal(hook(dir, 'gh pr create --title x').status, 2);
});

test('git commit is allowed when the gate passes', () => {
  const dir = project({ 'src/ok.js': 'export const x = 1;\n' });
  assert.equal(hook(dir, 'git commit -m "x"').status, 0);
});

test('commit is blocked (fail closed) when the gate script is missing', () => {
  const dir = project({ 'src/ok.js': 'export const x = 1;\n' }, false);
  const r = hook(dir, 'git commit -m "x"');
  assert.equal(r.status, 2);
  assert.match(r.stderr, /missing/);
});

test('the skills directive emits valid SubagentStart JSON', () => {
  const r = spawnSync(process.execPath, [DIRECTIVE, 'SubagentStart'], { encoding: 'utf8' });
  const out = JSON.parse(r.stdout);
  assert.equal(out.hookSpecificOutput.hookEventName, 'SubagentStart');
  assert.match(out.hookSpecificOutput.additionalContext, /security-review/);
});
