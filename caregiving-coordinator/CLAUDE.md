# Caregiving Coordinator

Week 2+ project for the Tech Fleet AI Development Residency. See `README.md`
for the problem and feature scope once written.

## Skills to use

Five project skills live in `.claude/skills/`, carried over from Week 1
(`week-1-claude-skills/`), with `security-review` extended for this project's
health-data and shared-credential risk surfaces.

- `project-prd-brainstorm`: starting a new project, brainstorming an idea, or
  writing a PRD. Ask one question at a time. Save the PRD to `docs/PRD.md`
  only after the user approves it.
- `ux-ui-design-review`: reviewing screens, flows, forms, dashboards, or
  data tables for usability.
- `accessibility-check`: checking a UI against WCAG 2.2 level AA.
- `security-review`: checking code against the OWASP Top 10:2025, plus this
  project's extra categories (health data, shared credentials, multi-user
  access). Use whenever the user is about to commit, push, or share code
  containing a key, token, password, or secret, even when the question looks
  simple.
- `writing-security-tests`: after a `security-review` finding, write one
  real, runnable test proving the fix for that finding, in whatever test
  framework the project already uses. Confirm what's being tested with the
  user before writing it. No Gherkin, no CI/feature-index assumption — a
  test that can't actually run isn't done.
- `engineering-quality-check`: before calling work done, ready to merge, or
  ready for a pull request.

An always-on `SessionStart` hook (`.claude/hooks/emit-skills-directive.mjs`)
loads this skill list every session so it's not left to description-matching
alone.

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
