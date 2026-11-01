# AI Development Residency

Work for the Tech Fleet AI Development Residency, by Lando.

## What is in this repo

| Folder | What it is |
|---|---|
| `caregiving-coordinator/` | The current project (Week 2 onward). Everything for the caregiving app lives here. |
| `week-1-claude-skills/` | Week 1 homework: four Claude skills (the PRD skill was removed on 2026-11-01). |
| `.claude/` (top level) | Skills used across the whole course: `wrap-up` (end-of-session routine) and `residency-context` (a local copy of the syllabus). |

## Inside `caregiving-coordinator/`

| Path | What it is |
|---|---|
| `CLAUDE.md` | The rules and skill list Claude follows in this project. |
| `.claude/skills/` | The 14 project skills (one folder each, with a `SKILL.md`). This is where the enterprise-readiness skills added in November live. |
| `.claude/hooks/` and `.claude/settings.json` | Hooks that load the skills list every session and block `git commit` when the architecture check fails. |
| `arch-gate.config.json`, `arch-gate.waivers.json` | Rules and exceptions for the architecture check (`.claude/skills/judge-arch/scripts/arch-gate.mjs`). |
| `docs/` | Research reports, the risk profile, and `skills-build-baseline.md` (what was built and all test results). |
| `research/` | Research tooling (a Reddit collector that has never been run). |
| `PLANNING-NOTES.md` | Early planning notes. |

Run the skill tests: `node --test caregiving-coordinator/.claude/skills/judge-arch/test/*.test.mjs`

## Removed on 2026-11-01

- `adhd-learning-app/`: the earlier project idea, dropped when the project changed.
- The `project-prd-brainstorm` skill, in both `caregiving-coordinator/` and `week-1-claude-skills/` (it does not fit the agile method). It can be restored from git history.
- The raw skill test outputs (`*-workspace` folders). Results are summarized in `caregiving-coordinator/docs/skills-build-baseline.md`. The raw files are in git history, for example `git show ad16c41:caregiving-coordinator/.claude/skills/judge-arch-workspace/iteration-1/benchmark.json`.
