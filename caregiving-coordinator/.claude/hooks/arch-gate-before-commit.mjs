#!/usr/bin/env node
// PreToolUse hook (matcher: Bash). Runs the architecture gate before `git commit`
// or `gh pr create` and blocks the command if the gate fails. Unlike a reminder,
// this fires whether or not Claude remembers to run the check.
//
// Exit 0 = allow. Exit 2 = block; stderr is shown to Claude as the reason.
// If the gate itself cannot run, the command is blocked too (fail closed).
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const COMMAND = /(^|[\s;&|(])(git\s+(?:-[^\s]+\s+)*commit|gh\s+pr\s+create)(\s|$)/;

let input = '';
try { input = fs.readFileSync(0, 'utf8'); } catch { /* no stdin: treated as nothing to check */ }

let payload = {};
try { payload = JSON.parse(input); } catch { process.exit(0); }

const command = payload?.tool_input?.command;
if (typeof command !== 'string' || !COMMAND.test(command)) process.exit(0);

const projectDir = process.env.CLAUDE_PROJECT_DIR || payload.cwd || process.cwd();
const gate = path.join(projectDir, '.claude', 'skills', 'judge-arch', 'scripts', 'arch-gate.mjs');

if (!fs.existsSync(gate)) {
  console.error(`arch-gate hook: ${gate} is missing, so the architecture check cannot run. Restore it or remove this hook from .claude/settings.json.`);
  process.exit(2);
}

const result = spawnSync(process.execPath, [gate, '--root', projectDir], { encoding: 'utf8' });
if (result.status === 0) process.exit(0);

console.error(`Blocked: the architecture gate did not pass (exit ${result.status}). Fix the findings below, or add an explicit, expiring waiver in arch-gate.waivers.json, then retry.\n`);
console.error((result.stdout || '') + (result.stderr || ''));
process.exit(2);
