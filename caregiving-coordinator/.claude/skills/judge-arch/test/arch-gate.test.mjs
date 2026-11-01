// Run: node --test .claude/skills/judge-arch/test/arch-gate.test.mjs
// Each test builds a throwaway project in a temp folder and runs the real gate on it.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const GATE = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'scripts', 'arch-gate.mjs');

function project(files) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'arch-gate-'));
  for (const [rel, content] of Object.entries(files)) {
    fs.mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true });
    fs.writeFileSync(path.join(dir, rel), content);
  }
  return dir;
}
const run = (dir, extra = []) =>
  spawnSync(process.execPath, [GATE, '--root', dir, ...extra], { encoding: 'utf8' });

const BOUNDARY_RULE = JSON.stringify({
  rules: [{
    name: 'ui must not call db',
    include: ['src/ui/**'],
    forbid: ['db\\.query\\('],
    message: 'Go through the service layer.',
  }],
});

test('clean project passes (exit 0)', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/ui/page.js': 'export const x = 1;\n',
  });
  const r = run(dir);
  assert.equal(r.status, 0, r.stdout + r.stderr);
  assert.match(r.stdout, /PASS/);
});

test('a forbidden pattern in a matching folder fails (exit 1) and names file and line', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/ui/page.js': 'const a = 1;\ndb.query("select 1");\n',
  });
  const r = run(dir);
  assert.equal(r.status, 1, r.stdout + r.stderr);
  assert.match(r.stdout, /ui must not call db/);
  assert.match(r.stdout, /src\/ui\/page\.js:2/);
});

test('the same pattern outside the rule folder is not flagged', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/service/repo.js': 'db.query("select 1");\n',
  });
  assert.equal(run(dir).status, 0);
});

test('built-in check flags an empty catch even with no config', () => {
  const dir = project({ 'src/a.js': 'try { f(); } catch (e) {}\n' });
  const r = run(dir);
  assert.equal(r.status, 1, r.stdout + r.stderr);
  assert.match(r.stdout, /emptyCatch/);
});

test('built-in check flags a catch that swallows the error and returns null', () => {
  const dir = project({ 'src/a.js': 'function f() { try { g(); } catch (e) { return null; } }\n' });
  const r = run(dir);
  assert.equal(r.status, 1, r.stdout + r.stderr);
  assert.match(r.stdout, /swallowReturn/);
});

test('a valid waiver lets a known violation pass', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/ui/page.js': 'db.query("x");\n',
    'arch-gate.waivers.json': JSON.stringify([{
      rule: 'ui must not call db', path: 'src/ui/page.js',
      reason: 'legacy', approvedBy: 'owner', expires: '2999-01-01',
    }]),
  });
  const r = run(dir);
  assert.equal(r.status, 0, r.stdout + r.stderr);
  assert.match(r.stdout, /1 waived/);
});

test('an expired waiver stops suppressing, so the gate fails again', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/ui/page.js': 'db.query("x");\n',
    'arch-gate.waivers.json': JSON.stringify([{
      rule: 'ui must not call db', path: 'src/ui/page.js',
      reason: 'legacy', approvedBy: 'owner', expires: '2000-01-01',
    }]),
  });
  assert.equal(run(dir).status, 1);
});

test('a waiver missing a required field fails closed (exit 2)', () => {
  const dir = project({
    'arch-gate.config.json': BOUNDARY_RULE,
    'src/ui/page.js': 'export const x = 1;\n',
    'arch-gate.waivers.json': JSON.stringify([{ rule: 'ui must not call db', reason: 'legacy' }]),
  });
  const r = run(dir);
  assert.equal(r.status, 2);
  assert.match(r.stderr, /approvedBy/);
});

test('a broken config fails closed (exit 2), never a silent pass', () => {
  const dir = project({ 'arch-gate.config.json': '{ not json', 'src/a.js': 'export {};\n' });
  assert.equal(run(dir).status, 2);
});

test('an explicitly named config that does not exist fails closed (exit 2)', () => {
  const dir = project({ 'src/a.js': 'export {};\n' });
  assert.equal(run(dir, ['--config', 'typo.json']).status, 2);
});

test('the shipped starter config flags a hardcoded credential', () => {
  const shipped = fs.readFileSync(path.join(path.dirname(GATE), '..', '..', '..', '..', 'arch-gate.config.json'), 'utf8');
  const dir = project({
    'arch-gate.config.json': shipped,
    'src/a.js': 'const apiKey = "abcd1234efgh5678ijkl";\n',
  });
  const r = run(dir);
  assert.equal(r.status, 1, r.stdout + r.stderr);
  assert.match(r.stdout, /hardcodedSecret/);
});

test('a tree with no code files says so instead of claiming real coverage', () => {
  const dir = project({ 'README.md': '# hi\n' });
  const r = run(dir);
  assert.equal(r.status, 0);
  assert.match(r.stdout, /no code files were checked/);
});
