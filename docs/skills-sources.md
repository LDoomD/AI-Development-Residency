# Skills in this repo: sources and versions

These skills live in `.claude/skills/`. Each was copied from its original
GitHub repo at the exact commit listed below, checked file by file for
unsafe code, and lightly adjusted so every skill folder is self-contained
(see "Local changes"). Audited 2026-10-20.

| Skill | Category | Source repo | Commit | License |
|---|---|---|---|---|
| frontend-design | UX/UI design | https://github.com/anthropics/skills (`skills/frontend-design`) | dbd4588f9e1033efb41dad4bef2f7947c8993d44 | Apache-2.0 |
| frontend-ui-engineering | Accessibility and UI build quality | https://github.com/addyosmani/agent-skills (`skills/frontend-ui-engineering`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| security-and-hardening | Security | https://github.com/addyosmani/agent-skills (`skills/security-and-hardening`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| spec-driven-development | Planning and specs | https://github.com/addyosmani/agent-skills (`skills/spec-driven-development`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| code-review-and-quality | Code review | https://github.com/addyosmani/agent-skills (`skills/code-review-and-quality`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| git-workflow-and-versioning | Git workflow | https://github.com/addyosmani/agent-skills (`skills/git-workflow-and-versioning`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| documentation-and-adrs | Documentation and decisions | https://github.com/addyosmani/agent-skills (`skills/documentation-and-adrs`) | aeac41d4d005999432bb7312f7ff06383a91d59d | MIT |
| test-driven-development | Testing | https://github.com/obra/superpowers (`skills/test-driven-development`) | b739a8af570e10a95898f2bdf6cec97467fa6c12 | MIT |
| systematic-debugging | Debugging | https://github.com/obra/superpowers (`skills/systematic-debugging`) | b739a8af570e10a95898f2bdf6cec97467fa6c12 | MIT |
| verification-before-completion | Verification | https://github.com/obra/superpowers (`skills/verification-before-completion`) | b739a8af570e10a95898f2bdf6cec97467fa6c12 | MIT |

Each skill folder includes its upstream license as `LICENSE.txt`.
`frontend-design` ships its own. For the other nine, the file is copied from
the root `LICENSE` of the source repo.

## Local changes

- **Shared checklists copied in.** Addy Osmani's repo keeps checklists in a
  shared top-level `references/` folder. Copies now sit in each skill's own
  `references/` folder, and the `../../references/` links point there:
  - `frontend-ui-engineering`: `accessibility-checklist.md`
  - `security-and-hardening`: `security-checklist.md`
  - `code-review-and-quality`: `security-checklist.md`, `performance-checklist.md`
  - In `security-and-hardening/references/hardening-patterns.md`, three
    `../../../references/security-checklist.md` links now point to
    `security-checklist.md` in the same folder.
- **Links to skills that are not installed.** Some Addy Osmani skills mention
  other skills from his collection that are not installed here (for example
  `planning-and-task-breakdown` and `context-engineering`). Claude won't find
  those. This is harmless.
- **Superpowers links renamed.** `systematic-debugging` linked to
  `superpowers:test-driven-development` and
  `superpowers:verification-before-completion`. These now use the plain skill
  names. A mention of `superpowers:writing-skills` was removed from
  `test-driven-development`.
- **Files moved into the standard anatomy.**
  - `systematic-debugging`: guides moved to `references/`, the example code to
    `assets/`, and `find-polluter.sh` to `scripts/`.
  - `test-driven-development`: `writing-good-tests.md` moved to `references/`.
  - The links in both skills were updated to match.
- **Development-only files removed from `systematic-debugging`.** These were
  `CREATION-LOG.md` and four `test-*.md` scenario files, which the skill
  author used to test the skill.

## Only script included

`systematic-debugging/scripts/find-polluter.sh` runs your project's tests one
file at a time, on your machine, to find which test leaves a stray file
behind. The script itself makes no network calls and deletes nothing.

- **It runs your own tests.** It calls `npm test` for each file, so it does
  whatever your tests do.
- **The path you check must not exist yet.** If it already exists when you
  start, the script skips every test and wrongly reports "all clean".
- **No spaces in file paths.** Paths with spaces break the script.
