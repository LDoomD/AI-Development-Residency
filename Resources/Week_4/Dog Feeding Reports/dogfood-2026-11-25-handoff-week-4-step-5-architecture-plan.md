# Handoff: Week 4 step 5, the architecture plan, built from Morgan's Architecture page (2026-11-25, fourteenth report)

Replaces: `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-19-handoff-week-4-repo-setup-and-github-research.md`. What changed: the app is built, GitHub checks are set up, and the owner has read the Week 4 Figma, the Notion lecture notes and the transcripts through me. The first thirteen reports' facts still stand. Every path in this report starts at the top folder of the course repository (`AI Developer Residency `), which holds `caregiving-coordinator/`, `Resources/` and `.claude/`. Paths for the app repository are written in plain text because that repository sits outside this one.

> Paste to start: "Read this handoff report, then the Week 4 reference report and the files in section 8. Confirm in a few short, plain sentences where we are. Run `git fetch` in both repositories and tell me whether app pull request 3 is merged. Then show me sections 1 to 3 of Morgan's Architecture page, drafted from my saved specs, and wait. Short sentences. Name the file or command behind every fact. Never make anything up. Ask before Firecrawl, Chrome or the browser pane."

## 0. Start here
- **Where we are:** Week 4, Build and Launch Checklist, **step 5: plan the app before any code.** Checklist steps 1 to 4 are done on the owner's side and mine. Step 4 (the Next.js app) waits for the owner to merge app pull request 3.
- **The outcome so far, in one sentence:** the app repository Week_4_Caregiving-Coordinator (private) has its layout, a GitHub check on every pull request, and branch protection on main; pull request 3 holds a working Next.js 16.4.6 and Material UI 9.6.0 starter page at the top level, with no src/ folder.
- **Next milestone:** checklist step 5. Its text, word for word from the Notion checklist: "Architect the app. Plan the screens (tier 1), the server code (tier 2), and the database (tier 3). Ask Claude to write the plan in a document and save it in your repository before you write any code." **The guide Morgan used for this is the Notion page "WEEK 4 Example - Architecture," a 10-section document filled in one section at a time** (section 5 below).
- **Why the last session went wrong:** I started step 5 with a business-rules question taken from the lecture's 9-step method and from the project skill. The owner pointed out that the Notion checklist does not say that, and became upset at the long, confusing messages. Do not repeat it: start from the checklist text and Morgan's page.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| The app goes in the repository `LDoomD/Week_4_Caregiving-Coordinator` (renamed, private, cloned to `/Users/landodoom/Desktop/Week_4_Caregiving-Coordinator`) | **Approved** (owner, chat 2026-11-19 and 2026-11-25) | https://github.com/LDoomD/Week_4_Caregiving-Coordinator |
| The starting layout (README, app CLAUDE.md, .gitignore, .claude/ with 14 skills and hooks, 2 arch-gate files, docs/risk-profile.md, 12 spec copies in docs/specs/) | **Approved** (owner: "I think the layout of the GitHub looks fine... I already confirmed it"). Merged as pull request 1. | App repository |
| The app sits at the top level of the repository with no src/ folder | **Approved** (owner, chat 2026-11-25) | App pull request 3 |
| GitHub Actions check (checks: architecture gate and the 21 hook tests) on every pull request and every push to main | **Approved** (owner asked for How-To Part A steps 4 and 5). Merged as pull request 2. | App repository, .github/workflows/ci.yml, source: gh run list, 2026-11-25 |
| Branch protection on `main`: the check `checks` must pass before merging. Admins not forced; force pushes and deletions off | **Approved** (owner asked; GitHub accepted it 2026-11-25) | GitHub settings of the app repository |
| No deadline for Week 4 for the owner ("There's no deadline. We just have to start week four.") | **Approved** (owner, chat 2026-11-25) | This report |
| The Notion Build and Launch Checklist is the order of work, not NotebookLM | **Approved** (owner, chat 2026-11-25) | `Resources/Week_4/Build and Launch Checklist (Notion copy 2026-11-13).md` |
| **Use Morgan's 10-section Architecture page as the guide for step 5 and fill it one section at a time, starting with sections 1 to 3 drafted from the saved specs** | **Proposed** (my proposal at the end of the last session; the owner had not answered when this report was requested) | Section 5 below |

## 2. Key findings and data
| Finding | Source | Confidence |
|---|---|---|
| App pull request 3 ("Add Next.js app with Material UI") was **open, not merged**, on 2026-11-25 after the owner said both pull requests were merged. The GitHub check on it passed (17 seconds). Course repository pull requests 96, 97, 98 and 99 are merged. | `gh pr view 3`, `gh run list`, `gh pr view 99`, 2026-11-25 | Authoritative (command output) |
| App `main` is at commit 4cf79df (pull request 2 merged). The local app folder is on `main`, with an untracked `next-env.d.ts` left by the build; the file is listed in `.gitignore` on the pull request 3 branch. | `git status`, `git log`, 2026-11-25 | Authoritative |
| Course repository `main` is at c44af7c (pull request 99 merged). It still has two uncommitted changes that are not from Week 4 work: `caregiving-coordinator/docs/sources/INDEX.md` modified and an untracked folder `caregiving-coordinator/docs/sources/immigrant-data-security-2026-11-20/`. The owner did not recognize them. Never touch them. | `git status`, 2026-11-25 | Authoritative |
| Node.js v26.4.0 and npm 11.17.0 are installed. `create-next-app` and the build work on them. | `node --version`, build output, 2026-11-25 | Authoritative |
| Pull request 3 checks run on this computer: `npm ci` 0 vulnerabilities, architecture gate PASS (5 code files), hook tests 21 of 21, lint clean, build succeeded, built page returned HTTP 200 with the Material UI heading. Not run: the app in a browser. | Command output, 2026-11-25 | Authoritative |
| The teacher's example app techfleetworks/job-decoder keeps its app at the top level next to package.json, app/, src/, supabase/, docs/. | gh api repos/techfleetworks/job-decoder/contents, 2026-11-25 | Authoritative (top-level names only; no files opened) |
| **How Morgan did the architecture step (11/4 working session):** open Claude, give it the lecture notes and the requirements, say "co-create with me, I don't know what I'm doing, ask me anything." Claude "builds the architecture document skeleton in Notion, decides the foundational choices and writes the ADRs, fills the architecture document section by section, designs the database tables and the diagram, then fills the backlog." His first decision was where the data lives. He gave Claude the outcome first and decided one question at a time. | Transcript at https://docs.google.com/document/d/1LPFjae8NNiwAAlKsNmbyGXo1y17I-jHHmTJWRHdOqJk/edit , at 00:08:03, 00:16:57 and 00:24:11 | Credible secondary (machine-made transcript) |
| **How Morgan started Week 4 (11/2 lecture):** a pirate-costume welcome, a pointer to the weekly materials, a recap, a cut of CI/CD to next week, then the restaurant metaphor, the 7 idea-to-ship steps, the Language of Change, layers, patterns, ADRs, the launch steps. His closing launch summary matches the 14-step checklist. | Transcript at https://docs.google.com/document/d/1NNkM84x5j-D6_-ylhXRJtmVM6RHkLVmGaBEYXiO99M8/edit , 00:00:03 to 00:57:21 | Credible secondary |
| The saved specs already decide most of tiers 2 and 3: the stack, the foundation tables (caregiver accounts, care circles, the cared-for person, circle members and roles, consent records, an access log), later tables for Epics 3, 1, 5 and 6, and the security rules. | `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`, `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`, `caregiving-coordinator/docs/risk-profile.md` | Authoritative (the owner's approved files) |

## 3. Excluded and deferred
- **Business-logic choice (Transaction Script, Table Module or Domain Model).** Not a checklist step. It belongs inside section 5 of Morgan's page ("Software pattern"), later. The owner has not chosen. The teacher's chart ("Which approach fits your business logic rules?") points toward Domain Model for rules that keep growing; the stack and the database's Row Level Security point toward Transaction Scripts. Judgment call for the owner.
- **Vercel import and deploy:** checklist step 11, after the app and database exist. The owner reached Vercel's import screen and chose Next.js with Root Directory `./`, then stopped. I do not know if Vercel kept a half-finished project.
- **ADRs (step 6), database tables and migration (step 7), the Supabase project (step 8), features (step 9):** each happens at its numbered step. Do not start them early.
- **Optional early deploy of an empty app to Vercel:** another student's Claude suggested it. It is not in the course checklist. The owner has not asked.
- **Advanced homework (usability tests):** the owner has not asked for it.
- **NotebookLM as a source:** the owner brought one NotebookLM answer; I checked it against the files (reference report section 7). Use the Notion checklist and course page instead.
- **The unrelated course-repository changes** listed in section 2: leave alone.

## 4. Open decisions
1. **Merge app pull request 3 (owner action).** It holds the Next.js and Material UI app. Choices: merge it, or ask me to change it first. After the merge the local app folder needs `git pull --ff-only` on `main`.
2. **Start the architecture document with sections 1 to 3 of Morgan's page, drafted from the saved specs?** Why: those sections ("What we're building," "Where the app lives (the three tiers)," "Technology decisions") are already answered in the specs, so it is the fastest, least confusing start. Choices: yes, or ask me to start somewhere else. After a yes I show the draft and wait for edits.
3. **The business-logic approach (section 5 of the page).** Why it matters: it decides where the consent checks, role checks and access log are coded. Choices: A, Transaction Scripts with shared helper functions and Row Level Security as a second lock (fastest; rules can be copied and drift); or B, Domain Model (one home per rule; slower to build; the lecture says it takes months to learn). Ask this only when the owner reaches section 5, with the teacher's chart (a picture is saved by the Figma tool; see section 8) in front of them.
4. **What "the entire MVP #1" means for the Week 4 build.** The course page says the whole MVP #1 is built. The saved roadmap holds 27 tasks in 6 epics over five weeks. Morgan told another student that a very large scope still takes far more than a week. The owner has said there is no deadline. Choices: build in roadmap order (foundation, then Epic 3, and so on) until done, or narrow the first release. Do not decide alone.
5. **Which outside email service sends relative invites** (build plan, box 1 and T1.1.6). Supabase's built-in email only reaches project team members. Needed before Epic 3's first invite task.
6. **The rows marked † in the non-functional list** (for example the Supabase US region us-east-1 and Vercel iad1). The owner included them in 2026-11-15 but did not approve each one. Confirm when the Supabase project is made (step 8).
7. **Add `npm ci`, lint and build to the GitHub check?** The check today runs only the gate and the hook tests. The app now exists, so adding them is a natural next change. Owner decides.
8. **Fix line 11 of the steps page** (it names the old repository `Week-3---Caregiving-Coordinator`). Waiting for a yes.
9. **Update the build plan** line that says branch protection is not used, since the owner turned it on. Do it when the architecture document is written, with the owner's yes.

## 5. Bridge to the next milestone
Morgan's page (`Resources/Week_4/WEEK 4 Example - Architecture (Notion copy 2026-11-13).md`) has 10 sections. Fill them in order. The finished plan is saved in the app repository as docs/architecture.md, which does not exist yet (the project's `judge-arch` and `enterprise-architecture-standards` skills look for that path) after the owner approves it.

| Section of Morgan's page | Filled from | Notes |
|---|---|---|
| 1. What we're building | `caregiving-coordinator/docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md` | Plain-language summary of the app and who it serves. |
| 2. Where the app lives (three tiers) | `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`, box 3 and the T3 group | Browser, Next.js on Vercel, Supabase. Already decided. |
| 3. Technology decisions | Same file, box 1 and the T1 group | One row per choice, with the reason. |
| 4. How the code is organized (layers) | Lecture notes, "Layers of Software Architecture" | New decisions. The project skill also wants each layer's job, what it must not do, the dependency direction, data owners, error handling, and which rules a script can check. Fold those in here and in sections 6 and 7. |
| 5. Software pattern | Lecture notes, "Enterprise Software Architecture Patterns" and "Business Logic Design" | Includes the open decision 3. |
| 6. Data architecture | Build plan box 2, T2 group, `caregiving-coordinator/docs/risk-profile.md` | One home per fact, where it is stored, who owns it. The database diagram is made later (step 7). |
| 7. The four promises | T4, T5 and T6 groups, risk profile | Reliable, scalable, maintainable, secure. |
| 8. How one request flows end to end | `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-3-2026-11-15.md` | Pick one real flow, such as signing in or recording consent. |
| 9. Decision log (ADRs) | Becomes docs/adr in the app repository (does not exist yet) at checklist step 6 | Not written in step 5. |
| 10. Open decisions | Section 4 of this report | Parked choices, so nothing is lost. |

## 6. First steps
1. Run `git fetch` in both repositories. Check `gh pr view 3` in the app repository. If it is still open, say one line: "App pull request 3 isn't merged yet. Merge it first, or keep going?" The owner decides.
2. Read the files in section 8. Say in a few short sentences what you have and what is missing. Do not recap this report.
3. Draft sections 1 to 3 of Morgan's Architecture page from the saved specs, as plain text in the chat, each fact with its source file. Show it and **stop and wait** for the owner's edits. Do not save docs/architecture.md (does not exist yet) yet.
4. Then go one section at a time. For each decision: say the outcome first, give two options with plain trade-offs and a recommendation, point to the source page, and wait for the owner's choice.
5. Save docs/architecture.md (does not exist yet) on a new branch and open a pull request only after the owner approves the whole plan. Then stop. ADRs are step 6.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md`, the project memory index `MEMORY.md`, the app repository's `CLAUDE.md`, and `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md` (read it first).
- **Never make anything up.** Name the file or command behind every fact. If not found, say "I did not find this" or "I am guessing."
- **Short replies, plain words.** The owner has ADHD and became upset on 2026-11-25 at long, confusing messages and at shorthand. Short sentences, one idea at a time, a small table instead of a paragraph. Say which list a step number belongs to (the 14-step checklist, the How-To's Part A and B, or the steps page).
- **Show the source before asking a decision.** If the owner asks "where is this from," show the Notion page, the Figma section or the transcript line. Do not lead with anything that is not on the checklist.
- **Morgan's method:** outcome first, co-create, one decision at a time, ask Claude to explain every unfamiliar term, demand evidence for facts.
- **One step at a time.** Do only the step asked, then stop. Questions get answers, not edits.
- **Every task gets a new branch and a pull request.** The owner merges. I never run `gh pr merge` and never commit to `main`.
- **Ask before** Firecrawl, Chrome, the browser pane, or changing GitHub settings.
- **The owner writes "What I Did" and "What I Learned."** I never write or edit them.
- **Fake data only. No secret keys in the repository.**
- **Project skills:** `enterprise-architecture-standards` applies to step 5. `architectural-decision-records` applies at step 6. Say which skills you applied or judged not relevant before calling work done.

## 8. Where things live
- **Reference report (read first):** `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md`
- **Steps page:** `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`
- **Checklist (the order of work):** `Resources/Week_4/Build and Launch Checklist (Notion copy 2026-11-13).md`, Notion https://app.notion.com/p/7b19219a469183899c040148cd01d130
- **Morgan's Architecture page (the guide for step 5):** `Resources/Week_4/WEEK 4 Example - Architecture (Notion copy 2026-11-13).md`, Notion https://app.notion.com/p/00e9219a46918328addd81a17880900c
- **Lecture notes (Notion):** `Resources/Week_4/Week 4 - Web Coding Lecture Notes (Notion copy 2026-11-13).md`, https://app.notion.com/p/7eb9219a469182888be281b0505f49c8 . Business-logic chart: heading "Business Logic Design."
- **Figma board, Week 4 section:** https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3089-14568 (the business-logic chart is node 3079:10802, the 14 launch steps node 3079:11692). Two pictures of these were sent to the owner; the files were in a temporary folder and may be gone.
- **Course page and the other helper pages:** `Resources/Week_4/Week 4 Coding Challenge - Code and Launch a Web App (Notion copy 2026-11-13).md` and the other files in `Resources/Week_4/`.
- **Transcripts (Google Docs):** the 11/2 lecture, the 11/4, 11/5 and 11/7 working sessions; document links and coverage are in section 11 of the reference report.
- **Saved specs, originals (course repository):** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`, `caregiving-coordinator/docs/risk-profile.md`, `caregiving-coordinator/docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md`, `caregiving-coordinator/docs/clean-deliverables/release-roadmap-2026-11-11.md`, `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-3-2026-11-15.md`. Copies are in the app repository under docs/specs/.
- **Git, course repository** (`LDoomD/AI-Development-Residency`): `main` at c44af7c. This report is on its own new branch with its own pull request. The two unrelated changes in section 2 stay uncommitted.
- **Git, app repository** (`LDoomD/Week_4_Caregiving-Coordinator`, private): `main` at 4cf79df. Pull request 3 (branch add-nextjs-app) is open. The local folder is on `main`.
- **Memory notes written this session** (project memory folder): reference-week-4-reference-report (new), app-repo-and-current-week (updated).

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. Owner decisions are chat replies on 2026-11-19 and 2026-11-25. Repository and pull request facts come from `gh` and `git` output on 2026-11-25. Morgan's method comes from the transcript links in section 2.
- **Checks run:** `check_handoff.py` on this report (result in the chat); `gh pr view` on app pull request 3 and course pull request 99; `git status` in both repositories.
- **Not checked:**
  - Whether app pull request 3 was merged after 2026-11-25. Check it first.
  - Whether Vercel kept a half-finished project.
  - Whether the GitHub check is free for this private repository.
  - The vision and scope boards, positioning statements, user stories, task pages and task flows were not re-read in full this session (only the five core specs named in section 5 were read, and the task flows only for their location).
  - The pictures in the lecture notes and the Figma board, and all recordings, were not viewed.
  - I did not find a transcript of the Hat Check demo, and the 11/5 working session has no transcript.
  - The step 5 approach in section 1 is my proposal; the owner has not approved it.
- **How this prevents drift:** outcomes are tagged Approved or Proposed, the business-logic choice and the scope question are listed as the owner's, and the first step shows a draft and waits for the owner.
