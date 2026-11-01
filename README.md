# AI Development Residency

Work for the Tech Fleet AI Development Residency, by Lando.

## What is in this repo

| Path | What it is |
|---|---|
| `caregiving-coordinator/` | The current project (Week 2 onward). Its skills live in `caregiving-coordinator/.claude/skills/`. |
| `.claude/skills/` (top level) | Two course-wide skills that Claude loads in every project: `wrap-up` (end-of-session routine) and `residency-context` (a local copy of the syllabus). |
| `README.md` | This map. |

## Inside `caregiving-coordinator/`

| Path | What it is |
|---|---|
| `CLAUDE.md` | The rules Claude follows in this project, and the skill list. |
| `.claude/skills/` | The 14 engineering skills (one folder each, with a `SKILL.md`): security, architecture, testing, release safety, data privacy and more. |
| `.claude/settings.json`, `.claude/hooks/` | Hooks that load the skills list every session and block `git commit` when the architecture check fails. |
| `arch-gate.config.json`, `arch-gate.waivers.json` | This project's rules and exceptions for the architecture check. |
| `docs/` | Research reports, the risk profile, and `skills-build-baseline.md` (what was built and every test result). |
| `research/` | Research tooling (a Reddit collector that has never been run). |
| `PLANNING-NOTES.md` | Early planning notes. |

Run the skill tests, from inside `caregiving-coordinator/`: `node --test .claude/skills/judge-arch/test/*.test.mjs`

## When a second project starts

Skills in a project's own `.claude/skills/` load only for that project. Claude also loads the `.claude/skills/` of every folder above it, up to the top of the repo. So to share the skills with a new project, move them up to the top-level `.claude/skills/`, or package them as a plugin.

## Removed on 2026-11-01

- `adhd-learning-app/`: the earlier project idea, dropped when the project changed.
- `week-1-claude-skills/`: all four skills in it already live in `caregiving-coordinator/.claude/skills/`. The original is kept at git tag `week-1-skills-as-submitted` (`git show week-1-skills-as-submitted:week-1-claude-skills/CLAUDE.md`).
- The `project-prd-brainstorm` skill (it does not fit the agile method). Restore from git history if needed.
- Raw skill test outputs (the `*-workspace` folders, including the old `residency-context-workspace`). Results are summarized in `caregiving-coordinator/docs/skills-build-baseline.md`. Raw files are in git history, for example `git show ad16c41:caregiving-coordinator/.claude/skills/judge-arch-workspace/iteration-1/benchmark.json`.
