# Caregiving Coordinator

Week 2+ project for the Tech Fleet AI Development Residency. See `README.md`
for the problem and feature scope once written.

## Skills to use

Fifteen project skills live in `.claude/skills/`. Five carried over from Week 1
(`week-1-claude-skills/`), `writing-security-tests` was added later, and nine
were added 2026-10-31 for enterprise readiness. The skills are written to be reusable across products. This
product's specific risks (health data, shared credentials, multi-user access)
live in `docs/risk-profile.md`, which the skills read.

- `project-prd-brainstorm`: starting a new project, brainstorming an idea, or
  writing a PRD. Ask one question at a time. Save the PRD to `docs/PRD.md`
  only after the user approves it.
- `ux-ui-design-review`: reviewing screens, flows, forms, dashboards, or
  data tables for usability.
- `accessibility-check`: checking a UI against WCAG 2.2 level AA.
- `security-review`: checking code against the OWASP Top 10:2025, plus the
  risks in `docs/risk-profile.md`. Use whenever the user is about to commit, push, or share code
  containing a key, token, password, or secret, even when the question looks
  simple.
- `writing-security-tests`: after a `security-review` finding, write one
  real, runnable test proving the fix for that finding, in whatever test
  framework the project already uses. Confirm what's being tested with the
  user before writing it. No Gherkin, no CI/feature-index assumption — a
  test that can't actually run isn't done.
- `engineering-quality-check`: before calling work done, ready to merge, or
  ready for a pull request. Runs the arch-gate script.
- `judge-arch`: fresh-context architecture review of a change, with the
  `arch-gate.mjs` script. Findings only.
- `architectural-decision-records`: write a short ADR in `docs/adr/` when a
  decision others must follow is made.
- `enterprise-architecture-standards`: decide and document layers, data
  ownership, and dependency rules in `docs/architecture.md`.
- `skeptical-audit`: tag each factual claim in a report with evidence state,
  source, and limit.
- `owasp-secure-coding-bdd`: write secure-behavior scenarios before building a
  feature that handles input, data, or access.
- `test-strategy`: plan what to test, at what level, and which checks run as
  scripts.
- `operational-readiness`: monitoring, alerts, backups, and recovery before
  launch.
- `release-deployment-safety`: rollback, migrations, and rollout before a
  release.
- `data-lifecycle-compliance`: inventory personal data and find gaps in how it
  is kept, shared, and deleted. Never says "compliant".

Hooks in `.claude/settings.json` force this instead of leaving it to
description-matching: `SessionStart` and `SubagentStart` load the skill list
(`.claude/hooks/emit-skills-directive.mjs`), and a `PreToolUse` hook blocks
`git commit` and `gh pr create` when `arch-gate.mjs` fails
(`.claude/hooks/arch-gate-before-commit.mjs`). Tests: `node --test
.claude/skills/judge-arch/test/*.test.mjs`.

## Rules for this folder

- The review skills report findings first. Do not edit code until the user
  asks for fixes.
- Never say code is "secure", "accessible", or "tests pass" without evidence.
  Show the command and result, or say what was not checked.
- Never silently fall back to base knowledge when a skill above applies, and
  never silently skip a relevant skill. If one is judged not relevant to a
  task, say so explicitly rather than defaulting to not using it.
- Ask before using the user's browser or the Chrome extension.
- Never write or edit the user's homework summary. They write it themselves.
- No RuFlo/claude-flow — removed from this residency's tooling; see memory.
