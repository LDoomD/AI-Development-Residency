#!/usr/bin/env node
// SessionStart hook: prints a short directive listing every project skill so
// the agent considers all of them every session, instead of relying only on
// description-matching (which Claude Code's own research found unreliable --
// skills only get picked up a fraction of the time when left to chance).
// This prints names + one-line purpose only, not full skill text, since the
// descriptions are already always in context -- this just makes using the
// right one mandatory instead of optional.

const SKILLS = [
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

// Situation cues, product-neutral. Match the situation, not the user's exact words:
// real requests are casual ("review my last commit", "is it good enough?").
const WHEN = [
  'When to use which (match the situation, not the exact words; invoke the skill with the Skill tool BEFORE answering from general knowledge):',
  '- About to call work done, commit, merge, or open a PR, or asked "is this ready", "review my commit", "good enough to merge": engineering-quality-check, plus judge-arch if code was added, moved, or restructured.',
  '- Files moved or refactored, a diff or branch to check for structure, or "is this logic in the right place": judge-arch.',
  '- Starting a product or feature, or "how should I organize this": enterprise-architecture-standards. A decision others must follow, or "why did we choose X": architectural-decision-records.',
  '- A claim stated as fact (works, secure, tested, compliant), or "how do you know that": skeptical-audit.',
  '- Planning a feature that takes input, data, or access: owasp-secure-coding-bdd. Reviewing existing code for weaknesses, or about to commit a key or password: security-review.',
  '- "What should I test", slow or flaky tests: test-strategy. Launching, or "what if it goes down": operational-readiness. Deploying or rolling back: release-deployment-safety. Storing, sharing, or deleting personal data: data-lifecycle-compliance.',
];

const lines = [
  'Project skills directive (caregiving-coordinator):',
  'These are mandatory considerations for every task, not optional suggestions.',
  ...SKILLS.map(([name, purpose]) => `- ${name}: ${purpose}`),
  '',
  ...WHEN,
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
