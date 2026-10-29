#!/usr/bin/env node
// SessionStart hook: prints a short directive listing every project skill so
// the agent considers all of them every session, instead of relying only on
// description-matching (which Claude Code's own research found unreliable --
// skills only get picked up a fraction of the time when left to chance).
// This prints names + one-line purpose only, not full skill text, since the
// descriptions are already always in context -- this just makes using the
// right one mandatory instead of optional.

const SKILLS = [
  ['project-prd-brainstorm', 'turn a rough idea into a one-page PRD'],
  ['ux-ui-design-review', 'review screens/flows/forms against usability heuristics'],
  ['accessibility-check', 'check a UI against WCAG 2.2 AA'],
  ['security-review', 'review code/config for OWASP Top 10:2025 + this project\'s health-data and shared-credential risks'],
  ['writing-security-tests', 'turn a security-review finding into one real, runnable test proving the fix'],
  ['engineering-quality-check', 'gate before calling work done, ready to merge, or ready for a PR'],
];

const lines = [
  'Project skills directive (caregiving-coordinator):',
  'These are mandatory considerations for every task, not optional suggestions.',
  ...SKILLS.map(([name, purpose]) => `- ${name}: ${purpose}`),
  '',
  'Never silently fall back to base knowledge when one of these applies. Before',
  'calling any task done, state which of these skills you applied and which you',
  'deliberately judged not relevant -- never skip one silently.',
];

console.log(lines.join('\n'));
