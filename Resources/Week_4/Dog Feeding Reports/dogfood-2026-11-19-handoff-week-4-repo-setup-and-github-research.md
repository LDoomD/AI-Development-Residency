# Handoff: Week 4 repository setup and GitHub research → owner approves the starting layout, then Week 4 step 4 (2026-11-19, thirteenth report)

Replaces: `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-18-handoff-security-paper-approved-owner-submits.md` as the start point for new chats. What changed: Week 2 and 3 and the security paper are finished, so everything from here is Week 4. The paper facts and the seven open decisions in the twelfth report still stand. Every path in this report starts at the top folder of the course repository (`AI Developer Residency `), which holds `caregiving-coordinator/`, `Resources/` and `.claude/`. Paths for the app repository are written in plain text because that repository sits outside this one.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Run `git fetch` in both repositories and tell me what is open. Then ask me the first open decision in section 4 and wait. Use short, plain sentences. Say real repository names, never 'the research folder'. Never make anything up: name the file or command behind every fact. Ask before Firecrawl, Chrome or the browser pane."

## 0. Start here
- **Where we are:** Week 2 and 3 were submitted on Nov 15 (the bold "Submitted on" line on the owner's Notion submission page). The security paper was submitted by the owner. We are now on **Week 4: build and launch the app**. The app repository is cloned on the owner's computer, the Week 2 and 3 specs are copied into it, and the GitHub setup research is done. Nothing in the app repository is committed yet.
- **The outcome so far, in one sentence:** the app repository exists, is private and empty on GitHub. On the owner's computer its folder now holds the smaller starting layout (CLAUDE.md, .gitignore, the .claude folder with the 14 skills and hooks, the two arch-gate files, risk-profile.md in the docs folder, and 12 more spec copies in docs/specs), built but not committed. The gate and the 21 judge-arch tests passed there on 2026-11-19 (source: command output in the chat).
- **Next milestone:** Week 4 step 4 (make the Next.js app with Material UI) from `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`. Before that, the owner makes the first commit on GitHub (decision 2: open the repository, click Add a README, commit). Then Claude pushes the layout on a branch and opens a pull request.
- **A date to be aware of:** the Week 4 course page says due date Nov 16 (`Resources/Week_4/Week 4 Coding Challenge - Code and Launch a Web App (Notion copy 2026-11-13).md`, line 20). Today is Nov 19. The steps page says "I don't know if you have extra time. Ask Morgan." (line 4). I did not find an extension in any file.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| The app goes in the repository made in Week 2, reused, not a new one. It is now named `Week_4_Caregiving-Coordinator` on GitHub (the owner renamed it; source: the Coding Challenge page, line 36) | **Approved** (owner, chat: "this is the app's new repo") | https://github.com/LDoomD/Week_4_Caregiving-Coordinator |
| The app repository is private | **Approved** (owner said they would make it private; `gh repo view` showed PRIVATE on 2026-11-19) | GitHub |
| Clone it to the Desktop, next to the course folder | **Approved** (owner: "Should we clone the repo to the computer? Yes.") | /Users/landodoom/Desktop/Week_4_Caregiving-Coordinator |
| Copy all 13 Week 2 and 3 spec files, unchanged (source: `cmp` showed 13 of 13 identical) | **Approved** (owner: "Copy all 13 files") | /Users/landodoom/Desktop/Week_4_Caregiving-Coordinator/docs/specs/ (untracked) |
| The "never make anything up" rule in `caregiving-coordinator/CLAUDE.md` and three hooks | **Approved** (merged, pull request 95) | `caregiving-coordinator/CLAUDE.md`, `caregiving-coordinator/.claude/hooks/no-invention-rule.mjs` |
| The old local branch `never-make-things-up-rule-2026-11-19` is deleted | **Approved** (owner: "we're ready to delete this") | Deleted locally with `git branch -d`; it was already merged |
| Everything from now on, including reports, is Week 4 | **Approved** (owner, chat) | This report |
| Week 4 reports are saved in `Resources/Week_4/Dog Feeding Reports/` | **Proposed** (my suggestion; the owner did not object) | This folder |
| Smaller starting layout for the app repository, built in the working folder on 2026-11-19 after the owner said "finish setting up that repo" (they never answered the layout question directly) | **Proposed** (built, not committed) | /Users/landodoom/Desktop/Week_4_Caregiving-Coordinator |

## 2. Key findings and data
The GitHub research. Each page was downloaded on 2026-11-19 and read in full. Saved copies are in `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/`, listed in `caregiving-coordinator/docs/sources/INDEX.md`.

| Finding | Source | Confidence |
|---|---|---|
| Branch protection and rulesets work on private repositories only with GitHub Pro, Team or Enterprise. On Free they work on public repositories only. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/github-protected-branches.txt`, `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/github-rulesets.txt` | Authoritative (GitHub Docs; no date on the page) |
| Secret scanning and push protection are free for public repositories. For private ones GitHub lists only organization accounts on a paid plan. Dependabot alerts can be enabled on any repository. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/github-secure-quickstart.txt` | Authoritative |
| GitHub recommends a README, a security policy file, and branches with pull requests instead of forks | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/github-best-practices.txt` | Authoritative |
| Vercel Hobby does not support collaboration on private repositories. The commit author must be the Hobby team owner, matched by email. Page last updated March 13, 2026. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/vercel-troubleshoot-collab.txt` | Authoritative |
| Claude Code reads CLAUDE.md, the settings.json file inside .claude (hooks) and the skills folder inside .claude from the repository it is opened in. Files in `~/.claude` apply to every project. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/claude-code-claude-directory.md` | Authoritative |
| Next.js has no required folder layout. Pick one and stay consistent. `.env` files stay out of git. Page lastUpdated 2026-07-21. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/nextjs-project-structure.md` | Authoritative |
| Supabase keeps migrations in `supabase/migrations`, sample data in supabase/seed.sql, settings in supabase/config.toml. Page updated Nov 2, 2026. | `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/supabase-local-migrations.txt` | Authoritative |

Facts found by commands in the chat on 2026-11-19 (source: command output, not saved as files):
- `gh auth status`: logged in as LDoomD with token scopes gist, read:org and repo. The user's plan field came back empty and the billing endpoint returned "Not Found". **The owner's GitHub plan was not found.**
- The app repository's Git author is name "Your Name" and a GitHub no-reply email. A Vercel deploy was not tested.
- The 13 spec files total 2,529 lines and 223 KB (source: `wc` output). The 8 core files are 94 KB; the 5 task-detail files are 129 KB.
- The `.claude` folder in `caregiving-coordinator/` has 54 files, about 280 KB (source: `find` and `du`).
- The GitHub MCP server failed to connect this session (source: the connection notice shown to Claude at the start of the session: "Authorization header is badly formatted"). The `gh` command in the terminal works and is what was used.
- The skills and hooks in `caregiving-coordinator/.claude/` point to these paths: docs/architecture.md (12 mentions), docs/risk-profile.md (11), docs/adr/ (6), docs/PRD.md (3), docs/test-plan.md (2), docs/security-specs/ (2) (source: `grep` count). None of architecture.md, PRD.md, test-plan.md or adr exists in the course repository yet.

## 3. Excluded and deferred
- **Foundation task pages and the Epic 2, 4, 5 and 6 task pages, and database columns and diagram:** deferred on purpose in Week 2 and 3; the columns and diagram are Week 4 work (sources: `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` lines 53 and 87, `caregiving-coordinator/docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md` lines 12 and 69, `caregiving-coordinator/docs/clean-deliverables/release-roadmap-2026-11-11.md` line 55, and the 2026-11-16 handoff, section 3). Do not call these gaps.
- **Bonus homework templates** (Usability Test Plan and Results): not used. The owner said to use only the Basic templates.
- **Folders the owner did not ask for:** architecture.md and docs/sources in the app repository. Dropped. The supabase folder, docs/adr, the database design, the src folder and Week 4 Coding Challenge/SUBMISSION.md do not exist yet and are created only by their numbered Week 4 steps (4, 6, 7, and the end).
- **Notion comparison:** the owner rejected a full Notion-versus-repository check as too costly. The repository files are the source; Notion is a copy the owner has not edited since submitting.
- **The twelfth report's decisions 1 to 7:** still open. Do not raise them unprompted.

## 4. Open decisions
1. **Check the starting layout.** It is built in the app folder but not committed. It holds: README.md (not written yet; it is made on the branch after the first commit exists), CLAUDE.md (new, short, for the app), .gitignore, the .claude folder (copied unchanged), arch-gate.config.json and arch-gate.waivers.json (copied), docs/risk-profile.md (the skills look for it there), and docs/specs (12 spec copies). Choices: keep it, or change it. The owner objected to the first, bigger layout and said to finish the repo, so Claude built this smaller one.
2. **The first commit on GitHub (the owner does this).** An empty repository needs a first commit on `main` before a branch or pull request can exist. The owner's hook `~/.claude/hooks/protect-main.mjs` (read this session) blocks Claude from committing or pushing to `main`, and Claude does not work around it. Steps for the owner: open https://github.com/LDoomD/Week_4_Caregiving-Coordinator, click **Add a README**, then **Commit changes**. After that, tell Claude. Claude then pulls `main`, makes the branch add-starting-layout, writes the real README, commits, pushes, and opens a pull request for the owner to merge.
3. **The owner's GitHub plan (Free or Pro).** The owner can see it at GitHub, Settings, Billing and plans. On Free, GitHub cannot stop pushes to `main` in a private repository. Choices: stay on Free and rely on the pull request habit plus the local hook, or upgrade. Nothing breaks either way.
4. **Skills, hooks and the gate in the app repository:** copied (all 54 files identical to the originals, checked with `diff -r`). The gate and tests work there. Open point: the gate script `arch-gate.mjs` itself was not read, and the gate checked 0 code files because the app has no code yet. Choices: leave as is, or ask Claude to read the gate later when code exists.
5. **Extra time for Week 4.** The course page says due Nov 16. The owner can ask Morgan. Claude must not decide this.
6. **The twelfth report's open decisions 1 to 7.** Listed in the twelfth report, section 4.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The 13 spec copies in the app repository (risk-profile.md sits one level up in docs) | Week 4 step 3 (list the saved Week 2 documents) and every new chat | Steps page: Claude reads these at the start of every new chat |
| Approved layout (decision 1) | The first commit and Week 4 step 4 | Step 4 says Claude shows the layout first |
| The GitHub research (section 2) | The README, .gitignore, and how branches and pull requests work | GitHub's own guidance |
| The database tables in the build plan | Week 4 step 7 (Database Design Template and migration file) | Columns and diagram are Week 4 work |

## 6. First steps
1. **Confirm where we are.** Run `git fetch` in both repositories. In the course repository run `gh pr list --state open`. Say in a few sentences what is merged and what is open (this report's pull request may be open).
2. **Ask whether the owner clicked Add a README on GitHub** (decision 2). If yes, run `git pull origin main` in the app folder, then follow decision 2.
3. **Open the pull request and hand it to the owner** (one deliverable, one branch, one pull request). The owner merges.
4. **Ask once** whether the owner made their free Vercel and Supabase accounts (Week 4 step 1; the owner never answered).
5. **Then ask the owner what to do next.** Do not start Week 4 step 4 unasked.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md`, the project memory index (`MEMORY.md`, project memory folder), and `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md` (if a task is not on that page, say so and ask first).
- **Never make anything up.** Name the file or command behind every fact. If not found, say "I did not find this" or "I am guessing."
- **Say real repository names.** "Your course repository, `AI-Development-Residency`," never "the research folder." The owner did not know that term.
- **Add only folders the Week 4 steps ask for,** and explain each in one plain sentence. Mark anything that is mine, not the course's.
- **Answer a question, then stop.** The owner said "Do not take action on anything" during discussions.
- **Every task gets a new branch and a pull request.** The owner merges; Claude does not run `gh pr merge`.
- **Use `gh` in the terminal for GitHub.** The GitHub MCP server failed to connect this session.
- **Ask before Firecrawl, Chrome and the browser pane.** Do not start more than two helper agents without telling the owner the cost.
- **The owner writes their own Submission Template "What I Did" and "What I Learned."** Claude never writes or edits them.

## 8. Where things live
- **Week 4 steps page:** `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`
- **Week 4 course page and templates:** `Resources/Week_4/Week 4 Coding Challenge - Code and Launch a Web App (Notion copy 2026-11-13).md` and the other files in `Resources/Week_4/`
- **The 13 spec originals** (in the course repository; copies are in the app repository):
  - `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`
  - `caregiving-coordinator/docs/risk-profile.md`
  - `caregiving-coordinator/docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md`
  - `caregiving-coordinator/docs/clean-deliverables/positioning-statements-2026-11-11.md`
  - `caregiving-coordinator/docs/clean-deliverables/release-roadmap-2026-11-11.md`
  - `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/epic-and-feature-user-stories-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/feature-stories-and-use-cases-epic-3-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-3-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-1-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-3-2026-11-15.md`
  - `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-1-2026-11-16.md`
  - `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`
- **GitHub research copies and index:** `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/` and `caregiving-coordinator/docs/sources/INDEX.md`
- **The owner's Notion submission page** (Week 2 and 3, closed): https://app.notion.com/p/4179219a46918157976edbc20a0a829f
- **Git, course repository** (`LDoomD/AI-Development-Residency`): branch `week-4-repo-setup-research-2026-11-19`, a new pull request opened from it. Pull requests up to 95 are merged. The old branch `never-make-things-up-rule-2026-11-19` was deleted locally.
- **Git, app repository** (`LDoomD/Week_4_Caregiving-Coordinator`, private): cloned to /Users/landodoom/Desktop/Week_4_Caregiving-Coordinator. On `main`, no commits. **Not saved anywhere but the owner's computer:** everything in the app folder (untracked): CLAUDE.md, .gitignore, .claude, the two arch-gate files, docs/risk-profile.md and 12 files in docs/specs.
- **Memory notes written this session** (project memory folder): app-repo-and-current-week (rewritten), feedback-minimal-layout-plain-repo-names (new), feedback-never-make-anything-up (from earlier).

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. Owner decisions are their chat replies on 2026-11-19. GitHub facts come from `gh repo list`, `gh repo view` and `gh auth status`. The research facts come from the eight saved pages listed in `caregiving-coordinator/docs/sources/INDEX.md`.
- **Checks run:**
  - The handoff checker `.claude/skills/dogfooding-handoff/scripts/check_handoff.py` on this report (result in the chat).
  - `cmp` on all 13 copied files: 13 identical, 0 different.
  - `node --test` on the judge-arch tests before the commit (result in the chat).
  - In the app folder: the arch gate passed (0 code files checked), the judge-arch tests passed (21 of 21), and the session-start hook printed the top rule. `diff -r` showed the copied .claude folder identical to the original.
- **Not checked:**
  - The owner's GitHub plan (the API gave nothing).
  - The arch-gate script `caregiving-coordinator/.claude/skills/judge-arch/scripts/arch-gate.mjs` was not read. The hook, `protect-main.mjs`, `arch-gate.config.json` and `arch-gate.waivers.json` were read.
  - Whether the spec copies contain private details (the owner said the repository is private, so I skipped it).
  - A Vercel deploy from the private repository (not tested).
  - The roadmap's task count (27) and whether all of MVP #1 fits in Week 4. I did not verify that.
  - The Vercel community threads, GitHub's plans page and the Claude Code skills and settings pages were seen only as search summaries and are not cited as proof.
  - The Week 4 templates other than the first 40 lines of the Database Design Template were not read in full.
- **How this prevents drift:** outcomes are tagged Approved or Proposed, the layout and first commit wait for the owner's answers, and the unsaved app repository state is named in section 8.
