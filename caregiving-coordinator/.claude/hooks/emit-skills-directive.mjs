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
  ['judge-arch', 'fresh-context architecture review of a change, plus the arch-gate script'],
  ['architectural-decision-records', 'write a short ADR when a decision others must follow is made'],
  ['enterprise-architecture-standards', 'decide and document layers, data ownership, and dependency rules'],
  ['skeptical-audit', 'tag every factual claim with evidence state, source, and limit'],
  ['owasp-secure-coding-bdd', 'write secure-behavior scenarios before building a feature that handles input, data, or access'],
  ['test-strategy', 'plan what to test, at what level, and which checks run as scripts'],
  ['operational-readiness', 'check monitoring, alerts, backups, and recovery before launch'],
  ['release-deployment-safety', 'check rollback, migrations, and rollout before a release'],
  ['data-lifecycle-compliance', 'inventory personal data and find gaps in how it is kept, shared, and deleted'],
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

// SessionStart reads plain stdout. SubagentStart only accepts JSON context, so
// the same directive reaches subagents (which do not inherit the session's context).
if (process.argv[2] === 'SubagentStart') {
  console.log(JSON.stringify({
    hookSpecificOutput: { hookEventName: 'SubagentStart', additionalContext: lines.join('\n') },
  }));
} else {
  console.log(lines.join('\n'));
}
