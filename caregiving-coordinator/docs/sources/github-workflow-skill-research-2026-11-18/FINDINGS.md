# Has anyone built a GitHub workflow skill? Findings (2026-11-18)

**Question from the owner (2026-11-18):** Should we build a skill for GitHub, and has anyone already built one that we can learn from?

**Status of this file:** Findings only. The recommendation at the end is **Proposed**. Nothing here has been built or added to `CLAUDE.md`.

**Where the saved sources are:** `raw/` in this folder. Every source with its link, date and how much of it was read is in `urls.tsv`. Line numbers below refer to the saved files.

## 1. What I read, and what I did not

| Read in full | Read in the cited sections only | Not read |
|---|---|---|
| Anthropic's `commit-commands` plugin (README and three command files); two `obra/superpowers` skills; two `jackspace/ClaudeSkillz` skills; one `89jobrien/steve` command; the Claude Code page "Extend Claude Code" (364 lines); the Anthropic blog post "Steering Claude Code" (June 18, 2026) | Claude Code "Skills" page; Claude Code "Hooks guide"; "Skill authoring best practices" | The GitHub flow page and the git-pull page (searched earlier, summaries only); the third-party skill registries (skills.cat, skills.sh, tessl.io and others), which I used only to find names. Treat registry pages as leads, not evidence. |

## 2. Skills other people have built (all read in full)

| Skill | Who and how trusted | What it does | What it lacks for your project |
|---|---|---|---|
| **`commit-commands` plugin**: `/commit`, `/commit-push-pr`, `/clean_gone` | Anthropic. Official plugins repository, version 1.0.1, repository updated 2026-11-18. **Most trusted.** | `/commit-push-pr` makes a branch if you are on `main`, commits, pushes, and opens a pull request with `gh pr create` (README lines 47 to 88). `/clean_gone` deletes local branches whose remote copy was deleted (README lines 90 to 126), which is the clutter on your computer today. | It never pulls `main` first, never checks that the last pull request merged, and knows nothing about the course's folder names or the SUBMISSION file. `/clean_gone` uses `git branch -D`, a force delete (command file line 39), so it needs care. |
| **`finishing-a-development-branch`** in `obra/superpowers` | Popular repository (about 320,000 stars), MIT license, last pushed 2026-11-03. | Runs the tests, then offers three choices: merge locally, push and open a pull request, or keep the branch. It waits for the human to choose, and a discard needs the typed word "discard" (lines 53 to 82, 132 to 157). | It is built around tests and worktrees, and offers a local merge you do not use. The idea worth borrowing is that the human decides the merge. |
| **`using-git-worktrees`** in `obra/superpowers` | Same repository. | Sets up an isolated workspace before starting work (lines 16 to 100). | Not needed. Your Claude app already offers worktrees. |
| **`claude-git-branching`** in `jackspace/ClaudeSkillz` | Weak. 16 stars, **archived**, "harvested from your_claude_skills repository" (last lines). | Branch names like `claude/<feature>-<session-id>`, push retries, pull request scripts. | Written for one hosted setup where pushes fail unless the branch is named that way (lines 615 to 639). It also tells you to run `git config credential.helper store` (line 582), which stores credentials as plain text, and to `git rebase -i` and force-push. **Do not copy it.** |
| **`git-workflow-helper`** in the same repository | Weak. The file says "This skill was auto-generated" and still has the line "Add examples of how to use this skill here." | A bullet list of Git tips. | It recommends a `develop` branch and `feature/*` names, which is not your flow. |
| **`create-pr`** in `89jobrien/steve` | Weak. 4 stars, marked `status: unpublished`. | A pull request command built around a team's own template file. | One good idea: keep a pull request template file in the repository (lines 40 and 124 to 133). |

**What every one of them has in common:** each covers commit, branch, pull request and cleanup. **None** covers (a) checking at the start of a session that your computer matches GitHub, (b) a course's required folder names, (c) the files a course asks you to submit, or (d) working across two repositories. None enforces its rules with a hook. They all depend on someone invoking them.

## 3. What Anthropic's own guidance says about skill, CLAUDE.md or hook

All quotes are short, and the line numbers are in the saved files.

1. **Rules that must hold every time belong in a hook, not a skill or `CLAUDE.md`.** "An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee... If a rule must hold every time, make it a hook" (features overview, line 189). The blog post agrees: a "Never do this" instruction can fail "in a long session" or through "a prompt injection," and "a real guardrail needs to be deterministic" (blog, "When to use each method").
2. **Procedures belong in skills.** "A 30-line procedure in CLAUDE.md. Procedures belong in skills" (blog). The trigger table says to capture a playbook as a skill when you paste "the same playbook or multi-step procedure into chat for the third time" (features overview, line 62).
3. **A skill with side effects should only run when you ask.** `disable-model-invocation: true` is meant for workflows "with side effects or that you want to control timing, like `/commit`, `/deploy`" (skills page, line 565).
4. **Keep `CLAUDE.md` under 200 lines.** Anthropic gives this as a rule of thumb in both the features overview (line 110) and the blog. **The project's `caregiving-coordinator/CLAUDE.md` is 225 lines today**, so adding a Git section there would push it further over.
5. **A `SessionStart` hook can add text to Claude's context, but cannot block anything.** Its output is added to context on exit 0, while exit 2 only shows a message and continues (hooks guide, lines 594 and 595). Blocking is done by a `PreToolUse` hook that exits 2 (blog, "Hooks").
6. **Skill size:** keep the `SKILL.md` body under 500 lines (authoring best practices, lines 257 and 1140).

## 4. Evaluation against your project

- **Your project already has pieces of this.** `wrap-up` has the branch and pull request steps, `residency-context` has the weekly checklists, and a `protect-main` hook blocks commits and pushes on `main` (from earlier notes in memory; not re-checked today).
- **The gap is narrow.** It is the start-of-session check, the course's folder and SUBMISSION conventions, the repository map, and the "which repository does this belong in" question. No existing skill covers those, which is why I found nothing to adopt for them.
- **Adopting Anthropic's plugin is possible but not needed yet.** `/clean_gone` would clear the 41 stale local branches, but force-deleting is your call.

## 5. Recommendation (Proposed, not decided)

1. **Do not write a general "GitHub best practices" skill.** The official plugin and `wrap-up` already cover commit, push and pull request.
2. **Put the must-always rules in hooks:** a `SessionStart` hook that fetches and tells Claude when the checkout is behind `main` or on a merged branch, plus the existing `protect-main` guard. Keep the written rule in `CLAUDE.md` or a rules file to one short paragraph, since the file is already over 200 lines.
3. **Write one small skill only for the weekly submission routine**, set to run only when you invoke it (`disable-model-invocation: true`). It would hold the course's folder names, the SUBMISSION file, the tag, and the email checklist, and point to `wrap-up` and `residency-context` instead of copying them.
4. **Add a repository map file** so Claude knows which repository and folder holds each week's work.
5. **Borrow two ideas:** the human chooses the merge (from `finishing-a-development-branch`), and a pull request template file in the repository (from `create-pr`).

## 6. Limits of this research

- Four repositories were examined in depth. There are many more skills in the registries that I did not open.
- Star counts and dates are from 2026-11-18 and will change.
- Three official pages were read in the cited sections only, not end to end.
- The GitHub flow and git-pull pages have not been read in full yet. The earlier search summaries support "branch from main, open a pull request, merge," but the start-of-session sync step is my own design, not a GitHub requirement.
- I did not run or install any of these skills.
