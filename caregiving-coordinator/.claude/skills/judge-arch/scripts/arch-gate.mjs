#!/usr/bin/env node
// arch-gate: a deterministic architecture check. No model involved, so it gives
// the same pass/fail every time and costs no tokens.
//
//   node arch-gate.mjs                    scan the whole project (cwd)
//   node arch-gate.mjs --root <dir>       scan another directory
//   node arch-gate.mjs --config <file> --waivers <file>
//   node arch-gate.mjs --changed          scan only files git reports as changed
//
// Exit codes: 0 = pass, 1 = violations found, 2 = could not run or could not
// read everything (fail closed: never report a pass on a scan it could not finish).
//
// Rules live in arch-gate.config.json at the project root. A rule says: files
// matching "include" (and not "exclude") must not contain any "forbid" pattern.
// Waivers live in arch-gate.waivers.json and are the only sanctioned bypass.
// Each needs rule, reason, approvedBy and an expiry date; expired ones stop working.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const args = process.argv.slice(2);
const has = (name) => args.includes(name);
const val = (name, fallback) => {
  const i = args.indexOf(name);
  return i >= 0 && args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : fallback;
};

const ROOT = path.resolve(val('--root', process.cwd()));
const CONFIG_PATH = path.resolve(ROOT, val('--config', 'arch-gate.config.json'));
const WAIVERS_PATH = path.resolve(ROOT, val('--waivers', 'arch-gate.waivers.json'));
const MAX_BYTES = 2 * 1024 * 1024;
const CODE_EXT = new Set(['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.vue', '.svelte']);
// Always skipped. Config can add to this list but never remove from it.
const DEFAULT_IGNORE = ['node_modules', 'dist', 'build', 'coverage', '.git', '.next', 'out',
  '.turbo', '.vercel', 'test', 'tests', '__tests__', 'spec', '.claude'];

function fail(message) {
  console.error(`arch-gate: ${message}`);
  process.exit(2);
}

function readJson(file, fallback) {
  let raw;
  try { raw = fs.readFileSync(file, 'utf8'); }
  catch (e) {
    if (e.code === 'ENOENT' && fallback !== undefined) return fallback;
    return fail(`cannot read ${path.relative(ROOT, file)}: ${e.message}`);
  }
  try { return JSON.parse(raw.charCodeAt(0) === 0xFEFF ? raw.slice(1) : raw); }
  catch (e) { return fail(`${path.relative(ROOT, file)} is not valid JSON: ${e.message}`); }
}

// A missing default config is allowed (built-in checks still run). A config the
// caller named explicitly must exist, so a typo cannot silently drop their rules.
const config = readJson(CONFIG_PATH, has('--config') ? undefined : {});
const waivers = readJson(WAIVERS_PATH, []);
if (!Array.isArray(waivers)) fail(`${path.basename(WAIVERS_PATH)} must be a JSON array.`);
for (const [i, w] of waivers.entries()) {
  const missing = ['rule', 'reason', 'approvedBy', 'expires'].filter((k) => !w || !w[k]);
  if (missing.length) fail(`waiver #${i} is missing: ${missing.join(', ')}. Each waiver needs rule, reason, approvedBy and expires.`);
  if (Number.isNaN(new Date(w.expires).getTime())) fail(`waiver #${i} has an unreadable expires date "${w.expires}". Use a date like 2026-12-31.`);
}

// Glob to RegExp. Supports **, *, ? and {a,b}, matched against a POSIX path.
function globToRegExp(glob) {
  let re = '^';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*') {
      if (glob[i + 1] === '*') {
        i++;
        if (glob[i + 1] === '/') { i++; re += '(?:.*/)?'; } else re += '.*';
      } else re += '[^/]*';
    } else if (c === '?') re += '[^/]';
    else if (c === '{') {
      const end = glob.indexOf('}', i);
      if (end === -1) re += '\\{';
      else {
        const alts = glob.slice(i + 1, end).split(',').map((s) => s.replace(/[.+^${}()|[\]\\]/g, '\\$&'));
        re += `(?:${alts.join('|')})`;
        i = end;
      }
    } else if ('.+^$()|[]{}\\'.includes(c)) re += `\\${c}`;
    else re += c;
  }
  return new RegExp(`${re}$`);
}

const configIgnore = (Array.isArray(config.ignore) ? config.ignore : [])
  .map((s) => String(s).replace(/\\/g, '/').replace(/\/+$/, ''));
const ignoreNames = new Set([...DEFAULT_IGNORE, ...configIgnore.filter((s) => !s.includes('/'))]);
const ignorePaths = configIgnore.filter((s) => s.includes('/'));
const isIgnored = (rel) =>
  rel.split('/').some((seg) => ignoreNames.has(seg)) ||
  ignorePaths.some((p) => rel === p || rel.startsWith(`${p}/`));

const scanErrors = [];

function walk(dir, out) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); }
  catch (e) {
    if (e.code !== 'ENOENT') scanErrors.push(`cannot read directory ${path.relative(ROOT, dir) || '.'}: ${e.message}`);
    return out;
  }
  for (const entry of entries) {
    const rel = path.relative(ROOT, path.join(dir, entry.name)).split(path.sep).join('/');
    if (entry.isDirectory()) { if (!isIgnored(rel)) walk(path.join(dir, entry.name), out); }
    else if (entry.isFile() && !isIgnored(rel)) out.push(rel);
  }
  return out;
}

function changedFiles() {
  const git = (...a) => execFileSync('git', a, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
  const files = new Set();
  let base = null;
  for (const b of ['origin/main', 'main', 'origin/master', 'master']) {
    try { base = git('merge-base', 'HEAD', b); if (base) break; } catch { /* try the next branch name */ }
  }
  const add = (text) => text.split('\n').forEach((f) => f && files.add(f));
  if (base) { try { add(git('diff', '--name-only', `${base}...HEAD`)); } catch (e) { scanErrors.push(`git diff failed: ${e.message}`); } }
  try { add(git('diff', '--name-only', 'HEAD')); } catch (e) { scanErrors.push(`git diff failed: ${e.message}`); }
  try { add(git('ls-files', '--others', '--exclude-standard')); } catch (e) { scanErrors.push(`git ls-files failed: ${e.message}`); }
  return [...files];
}

function compile(pattern, ruleName, flags) {
  const f = (flags || 'g').includes('g') ? (flags || 'g') : `${flags || ''}g`;
  try { return new RegExp(pattern, f); }
  catch (e) { return fail(`invalid forbid pattern in rule "${ruleName}": ${pattern} (${e.message})`); }
}

const rules = (config.rules || []).map((r) => {
  if (!r.name) fail('every rule needs a "name".');
  return {
    name: r.name,
    include: (r.include || []).map(globToRegExp),
    exclude: (r.exclude || []).map(globToRegExp),
    forbid: (r.forbid || []).map((p) => compile(p, r.name, r.flags)),
    message: r.message,
  };
});

// Built-in checks run on every JS/TS file. The rule name is a short stable key so
// a waiver keeps matching even if the label wording changes.
const builtins = Object.assign({ emptyCatch: true, swallowReturn: true }, config.builtins || {});
const COMMENT_OR_SPACE = '(?:\\s|;|//[^\\n]*|/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/)*';
const BUILTIN_CHECKS = [
  ['emptyCatch', 'A catch that does nothing. Recover, retry, or report the error.',
    new RegExp(`catch\\s*(?:\\([^)]*\\))?\\s*\\{${COMMENT_OR_SPACE}\\}|\\.catch\\s*\\(\\s*(?:async\\s*)?(?:\\([^)]*\\)|[\\w$]+)\\s*=>\\s*\\{${COMMENT_OR_SPACE}\\}\\s*\\)`, 'g')],
  ['swallowReturn', 'A catch that hides the error and returns an empty value. Report or rethrow it.',
    /catch\s*(?:\([^)]*\))?\s*\{\s*return\s*(?:null|false|undefined|\[\s*\]|\{\s*\}|0|''|"")?\s*;?\s*\}/g],
];
const messages = new Map(rules.filter((r) => r.message).map((r) => [r.name, r.message]));
for (const [key, label] of BUILTIN_CHECKS) messages.set(key, label);

const waiverList = waivers.map((w) => ({ ...w, re: w.path ? globToRegExp(w.path) : null }));
const isWaived = (rule, file) => waiverList.some((w) =>
  w.rule === rule && new Date(w.expires) >= new Date() && (!w.re || w.re.test(file)));

const violations = [];
function record(rule, file, content, regex) {
  const re = new RegExp(regex.source, regex.flags.includes('g') ? regex.flags : `${regex.flags}g`);
  let m;
  while ((m = re.exec(content))) {
    const line = content.slice(0, m.index).split('\n').length;
    violations.push({ rule, file, line, snippet: m[0].replace(/\s+/g, ' ').trim().slice(0, 90), waived: isWaived(rule, file) });
    if (m.index === re.lastIndex) re.lastIndex++;
  }
}

let files = has('--changed') ? changedFiles() : walk(ROOT, []);
files = files.filter((f) => {
  if (isIgnored(f)) return false;
  try { return fs.statSync(path.join(ROOT, f)).size <= MAX_BYTES; }
  catch (e) { if (e.code !== 'ENOENT') scanErrors.push(`cannot stat ${f}: ${e.message}`); return false; }
});

let evaluated = 0;
let evaluatedCode = 0;
for (const file of files) {
  const isCode = CODE_EXT.has(path.extname(file));
  const applicable = rules.filter((r) => r.include.some((re) => re.test(file)) && !r.exclude.some((re) => re.test(file)));
  if (!applicable.length && !isCode) continue;
  let content;
  try { content = fs.readFileSync(path.join(ROOT, file), 'utf8'); }
  catch (e) { if (e.code !== 'ENOENT') scanErrors.push(`could not read ${file}: ${e.message}`); continue; }
  evaluated++;
  if (isCode) evaluatedCode++;
  for (const r of applicable) for (const re of r.forbid) record(r.name, file, content, re);
  if (isCode) for (const [key, , re] of BUILTIN_CHECKS) if (builtins[key]) record(key, file, content, re);
}

if (scanErrors.length) {
  console.error(`\narch-gate: FAIL CLOSED. ${scanErrors.length} path(s) could not be read, so the scan is incomplete and cannot report a pass:`);
  for (const s of scanErrors) console.error(`  ! ${s}`);
  process.exit(2);
}

const active = violations.filter((v) => !v.waived);
const waivedCount = violations.length - active.length;
console.log(`arch-gate: evaluated ${evaluated} of ${files.length} file(s), ${evaluatedCode} with code checks${has('--changed') ? ' (changed files only)' : ''}`);
if (evaluatedCode === 0) {
  console.log(`arch-gate: note: no code files were checked (built-in checks cover ${[...CODE_EXT].join(' ')}). A pass here says nothing about code that does not exist yet.`);
}

if (active.length === 0) {
  console.log(`PASS: no architecture violations.${waivedCount ? ` (${waivedCount} waived)` : ''}`);
  process.exit(0);
}

const byRule = new Map();
for (const v of active) {
  if (!byRule.has(v.rule)) byRule.set(v.rule, []);
  byRule.get(v.rule).push(v);
}
for (const [rule, list] of byRule) {
  console.log(`\nFAIL ${rule} (${list.length})`);
  if (messages.has(rule)) console.log(`  fix: ${messages.get(rule)}`);
  for (const v of list.slice(0, 20)) console.log(`  ${v.file}:${v.line}  ${v.snippet}`);
  if (list.length > 20) console.log(`  ...and ${list.length - 20} more`);
}
if (waivedCount) console.log(`\n(${waivedCount} waived violation(s) hidden. See ${path.basename(WAIVERS_PATH)}.)`);
console.error(`\nFAIL: ${active.length} architecture violation(s). Fix them, or add an explicit, expiring waiver.`);
process.exit(1);
