# Week 1 Claude Skills

This folder holds five project skills in `.claude/skills/`. Use the matching
skill when the situation below comes up, and follow its SKILL.md.

## Skills to use

- `project-prd-brainstorm`: starting a new project, brainstorming an idea, or
  writing a PRD (product requirements document).
  - Ask one question at a time.
  - Save the PRD to `docs/PRD.md` only after the user approves it.
- `ux-ui-design-review`: reviewing screens, flows, forms, dashboards, or
  data tables for usability.
- `accessibility-check`: checking a UI against WCAG 2.2 level AA.
- `security-review`: checking code against the OWASP Top 10:2025.
- `engineering-quality-check`: before calling work done, ready to merge, or
  ready for a pull request.

## Rules for this folder

- The review skills report findings first. Do not edit code until the user
  asks for fixes.
- Never say code is "secure", "accessible", or "tests pass" without evidence.
  Show the command and result, or say what was not checked.
- Never write or edit the user's homework summary. They write it themselves.
