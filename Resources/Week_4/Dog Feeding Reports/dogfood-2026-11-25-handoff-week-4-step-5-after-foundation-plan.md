# Handoff: Week 4 step 5, finishing the architecture plan after the foundation draft was merged (2026-11-25, fifteenth report)

> **Replaced by:** `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-25-handoff-week-4-step-5-epic-1-screens-next.md` (2026-11-25, sixteenth report). Use that report as the start point for new chats.

Replaces: `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-25-handoff-week-4-step-5-architecture-plan.md`. What changed: the foundation part of the architecture plan was decided with the owner and is saved in the app repository as docs/architecture.md (pull request 4, merged). The owner also checked that the Week 2 and 3 basic homework is complete. Every path in this report starts at the top folder of the course repository (`AI Developer Residency `). Paths for the app repository are written in plain text because that repository sits outside this one.

> Paste to start: "Read this handoff report, then the Week 4 reference report and the files in section 8. Confirm in a few short, plain sentences where we are, using only my Build and Launch Checklist and its four groups. Run git fetch in both repositories and tell me whether app pull request 3 is merged. Then ask me the one open question about how to finish step 5, and wait. Short sentences. Name the file or command behind every fact. Never make anything up. Ask before Firecrawl, Chrome or the browser pane."

## 0. Start here
- **Where we are:** Week 4. The owner's Build and Launch Checklist has four groups: (1) Set up your accounts and tools, steps 1 to 3, finished; (2) Build the app on your computer, steps 4 to 10, in progress; (3) Launch it on the internet, steps 11 to 14, not started; (4) Move your tickets as you work, not started. We are on **step 5, "Architect the app."**
- **The outcome so far, in one sentence:** a draft architecture plan is on the app repository's `main` (pull request 4), covering the foundation (four screens, what the server does, six database tables); step 4's Next.js app is still in open pull request 3.
- **Next milestone:** finish step 5, then step 6 (ADRs). Step 5 word for word from the Notion checklist: "Architect the app. Plan the screens (tier 1), the server code (tier 2), and the database (tier 3). Ask Claude to write the plan in a document and save it in your repository before you write any code."
- **Why the owner got upset again this session:** I mixed numbering systems. I said "part 4" (a part of Morgan's 10-part page) and "step 5 of 7" (a position inside group 2) when the owner was using the 14-step checklist. Use only the owner's checklist numbers. If a part of Morgan's page is meant, say "part N of Morgan's Architecture page."

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| Use Morgan's 10-part Architecture page as the guide for step 5, and save a draft of the plan in the app repository | **Approved** (owner chose "A, save a draft now," chat 2026-11-25) | App repository, docs/architecture.md on `main` |
| The app sits at the top level with no src/ folder | **Approved** (owner, 2026-11-25) | App pull request 3 (open) |
| Sign-up asks only for an email and a password | **Approved** (owner, 2026-11-25) | docs/architecture.md, part 2 |
| Email confirmation is off in Week 4 while building with fake data. It must be turned on, with an outside email service, before any real caregiver data | **Approved** (owner chose A, 2026-11-25) | docs/architecture.md, parts 3 and 10 |
| A "Set up your care circle" screen comes right after the first sign-in | **Approved** (owner chose A, 2026-11-25) | docs/architecture.md, part 2 |
| The circle screen asks for a label (parent, spouse or partner) and a nickname the caregiver picks, not a real name | **Approved** (owner chose A, 2026-11-25) | docs/architecture.md, parts 2 and 6 |
| All six foundation tables (accounts, care circles, cared-for person, circle members and roles, consent records, access log) are created together in one migration file with access rules on each | **Approved** (owner chose A, 2026-11-25; the six tables are in T2.1.1, approved 2026-11-15) | docs/architecture.md, part 6 |
| The foundation is planned screens first, then server, then database | **Approved** (owner chose A, 2026-11-25) | docs/architecture.md, part 2 |
| The owner continues with the basic homework only | **Approved** (owner, 2026-11-25; also 2026-11-15) | `caregiving-coordinator/docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md` |
| The four foundation screens are: sign up, log in, set up your care circle, signed-in home (with log out) | **Proposed** (the owner approved each choice above; the full list and the server details were saved as a draft but not approved as a whole) | docs/architecture.md, part 2 |
| The circle, the cared-for person and the main caregiver membership are made all together or not at all | **Proposed** | docs/architecture.md, part 2 |
| No extra profile table, since Supabase Auth keeps the email and password | **Proposed** | docs/architecture.md, part 6 |

## 2. Key findings and data
| Finding | Source | Confidence |
|---|---|---|
| App pull request 4 (docs/architecture.md) is **merged**. App `main` is at commit d5509f5. | `git log origin/main`, `gh pr view 4`, 2026-11-25 | Authoritative |
| App pull request 3 (the Next.js app) is **still open.** Its GitHub check passed. | `gh pr view 3`, `gh run list`, 2026-11-25 | Authoritative |
| The local app folder is on the old branch add-architecture-draft, with an untracked next-env.d.ts. After the owner confirms the merges it needs `git switch main` and `git pull --ff-only`. | `git branch`, `git status`, 2026-11-25 | Authoritative |
| Course repository `main` is at fb2f6a0 (pull request 100 merged). Two unrelated uncommitted changes are still there (docs/sources/INDEX.md modified, an untracked folder immigrant-data-security-2026-11-20). Never touch them. | `git log`, `git status`, 2026-11-25 | Authoritative |
| Week 2 coding challenge, requirement 6, asks for a build plan with Vercel, Supabase, GitHub and user accounts with secured data. The saved build plan covers all four. | `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Week 2 Coding Challenge - Develop Product Specifications for the ADHD Budgeting App (Notion copy 2026-11-13).md`, lines 86 to 91; `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` | Authoritative |
| The 8 basic homework items are all done in the saved files. Feature analysis was skipped, the pitch deck was not made (bonus list), and the Backlog board holds 11 of the 27 tasks (the lecture says only the next two weeks are made ready). | `caregiving-coordinator/docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md`; memory note week-2-3-task-level-done-2026-11-16 (9 days old, not re-verified) | Credible secondary |
| The owner's Week 2 and 3 specs are copied into the app repository (12 files in docs/specs, plus docs/risk-profile.md). The build plan copy is identical to the original. | `git ls-tree origin/main docs/specs/`, `diff`, 2026-11-25 | Authoritative |
| The specs do not say whether new users must confirm their email. They say an outside email service sends sign-in and invite emails and that it is not chosen. | `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` lines 25, 45, 102; `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md` lines 20 and 53 (searched five files, not all) | Authoritative |
| The specs hold no list of screens. The epics file holds outcomes, not screens. | `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md` | Authoritative |
| Morgan's Week 2 and 3 technical architecture page has more than ours (failure fallbacks, scale and cost, a "what this does not promise" note), but those are not required by the Week 2 course page. His product also uses an AI service, which ours leaves out. | Notion page https://app.notion.com/p/9ca9219a46918354aa3f01a6b57fc5b9 and four of its subpages, read 2026-11-25 (four other subpages not read) | Credible secondary |
| The owner's Notion Build and Launch Checklist copy had only step 1 ticked at 22:34 UTC. The wording matches the other copy. | https://app.notion.com/p/d929219a469182e580b301c1e92cc0f7, fetched 2026-11-25 | Authoritative |
| Checks on docs/architecture.md: the architecture gate passed and the 21 hook tests passed. GitHub's own check on the branch also passed. | Command output; `gh run list`, 2026-11-25 | Authoritative |

## 3. Excluded and deferred
- **How business rules are coded (Transaction Scripts or Domain Model).** Not a checklist step. It sits in part 5 of Morgan's page. Not decided. Comes back when part 5 is filled.
- **Forgot password.** The course does not ask for it. Not proposed for now.
- **Two-step sign-in.** The build plan says ask the owner in Week 5.
- **The relative invite screen.** It belongs to Epic 3. Not planned.
- **Screens for Epic 3 and later epics.** Not planned yet. See open decision 1.
- **Morgan's extras** (failure fallbacks, scale and cost, a "does not promise" note). Optional. The owner can ask for them in part 7 of Morgan's page.
- **ADRs (step 6), database design (step 7), Supabase project (step 8), features (step 9).** Each at its numbered step.
- **Vercel import and deploy:** step 11. A half-finished Vercel project may exist; unknown.
- **Bonus homework** (feature analysis, pitch deck, prototypes, advanced usability tests). The owner is doing the basic homework only.
- **The unrelated course-repository changes** in section 2.
- **Owner-only items:** the "What I Did" and "What I Learned" summary (no AI), sharing and emailing the submission page, and submitting the Premium paper. I never write or edit them.

## 4. Open decisions
1. **How to finish step 5 (the owner has not answered).** Why it matters: it decides whether we plan screens for more epics before calling step 5 done. Choices: **A**, plan the screens for Epic 3 first (about a dozen more questions, my guess); or **B**, call step 5 finished with the foundation plan already merged, and plan each later feature's screens when we build it at step 9. I recommended B, because step 9 says to build one feature at a time. That is my reading, not the owner's documents. After A, I draft Epic 3's screens, server and tables one question at a time and update docs/architecture.md. After B, step 5 is finished and we start step 6.
2. **Merge app pull request 3 (owner action).** It holds the Next.js and Material UI app (step 4). Choices: merge it, or ask me to change it first. After the merge, the local app folder needs `git switch main` and `git pull --ff-only`.
3. **What "the entire MVP #1" means for the Week 4 build.** The course page says the whole MVP #1 is built. The roadmap holds 27 tasks in six epics. The owner said there is no deadline. Choices: build in roadmap order until done, or narrow the first release. Do not decide alone.
4. **The email service** that sends relative invites. Needed before the first invite task. Email confirmation must also be turned on before real data.
5. **Where consent is collected.** The specs say no health note is saved without a collect consent but not which screen records it. Decide when planning Epic 3's screens.
6. **How business rules are coded** (part 5 of Morgan's page). Ask only when part 5 is reached, with the teacher's chart (Figma node 3079:10802) in front of the owner.
7. **The rows marked † in the non-functional list** (for example the Supabase region us-east-1 and Vercel iad1). Confirm when the Supabase project is made (step 8).
8. **Add `npm ci`, lint and build to the GitHub check?** Today it runs only the architecture gate and the hook tests.
9. **Fix line 11 of the steps page** (it names the old repository) and **update the build plan line** that says branch protection is not used. Both wait for the owner's yes.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The six foundation tables and the rules in part 6 | Step 7, the Database Design Template and one migration file with access rules on every table | Step 7 says to save the tables as a migration file and turn on access rules for every table |
| Choices in parts 2 and 3 (Next.js with Material UI, Vercel, Supabase, Supabase Auth, email confirmation off in Week 4) | Step 6, ADRs in docs/adr (does not exist yet). At least three: Next.js with Material UI, Vercel, Supabase | Step 6 says one ADR for each big choice |
| The four foundation screens and the server behavior | Step 9, feature 1: sign-up and log-in | Step 9 says to start with sign-up and log-in |
| Part 10, open decisions | The next sessions' questions | Nothing is lost |

## 6. First steps
1. Run `git fetch` in both repositories. In the app repository run `gh pr view 3`. If pull request 3 is still open, say one line: "App pull request 3 isn't merged yet. Merge it first, or keep going?" The owner decides.
2. Read this report, the Week 4 reference report and the files in section 8. Say in a few short sentences where we are, using only the owner's checklist numbers and its four groups. Do not recap this report.
3. Ask the owner open decision 1 (A or B) and **wait**. Say the question in plain words. Do not start Epic 3 screens, ADRs or code unasked.
4. If the owner chooses B: after the owner confirms the merge, run `git switch main` and `git pull --ff-only` in the app repository, remind the owner to tick step 5 on the Notion checklist, and then start step 6 (ADRs) one decision at a time, using the architecture-decision-records skill.
5. If the owner chooses A: plan Epic 3's screens one question at a time (outcome first, two options with plain trade-offs, a recommendation, the source), then update docs/architecture.md on a new branch with its own pull request.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md`, the project memory index, the app repository's CLAUDE.md, and `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md` (read first).
- **Never make anything up.** Name the file or command behind every fact. If not found, say "I did not find this" or "I am guessing."
- **Use only the owner's Build and Launch Checklist numbers.** There are 14 steps in four groups. Never say "step N of 7" or "part 4" without saying which list it belongs to. The owner has been confused by this twice.
- **Short replies, plain words.** The owner has ADHD and wants short answers with sources. One decision per message, as a small table when there are choices, with a recommendation marked as mine.
- **Every decision explains itself:** what it is, why it matters, the choices, and what happens after each.
- **Show the source before asking a decision,** and say plainly when something is my proposal and not in the owner's documents. Do not compare the owner's work to Morgan's example as if it were the requirement. The requirement is the course page.
- **One step at a time.** Questions get answers, not edits.
- **Every task gets a new branch and a pull request.** The owner merges. I never run `gh pr merge` and never commit to `main`.
- **Ask before** Firecrawl, Chrome, the browser pane, or changing GitHub settings.
- **The owner writes "What I Did" and "What I Learned."** I never write or edit them.
- **Fake data only. No secret keys in the repository.**
- **Project skills:** `enterprise-architecture-standards` applies to step 5, `architectural-decision-records` to step 6. Say which skills you applied or judged not relevant before calling work done.

## 8. Where things live
- **Reference report (read first):** `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md`
- **Earlier handoff (replaced by this one):** `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-25-handoff-week-4-step-5-architecture-plan.md`
- **Steps page:** `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`
- **Checklist (the order of work):** `Resources/Week_4/Build and Launch Checklist (Notion copy 2026-11-13).md`. The owner's own tick-off copy: https://app.notion.com/p/d929219a469182e580b301c1e92cc0f7
- **Morgan's Architecture page (the guide for step 5):** `Resources/Week_4/WEEK 4 Example - Architecture (Notion copy 2026-11-13).md`
- **The architecture plan itself:** app repository, docs/architecture.md (on `main`)
- **Saved specs, originals (course repository):** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`, `caregiving-coordinator/docs/risk-profile.md`, `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md`. Copies are in the app repository under docs/specs.
- **Week 2 course page (the requirement):** `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Week 2 Coding Challenge - Develop Product Specifications for the ADHD Budgeting App (Notion copy 2026-11-13).md`
- **Morgan's Week 2 and 3 technical architecture page:** https://app.notion.com/p/9ca9219a46918354aa3f01a6b57fc5b9
- **Git, course repository** (`LDoomD/AI-Development-Residency`): `main` at fb2f6a0. This report is on its own new branch with its own pull request. The two unrelated changes in section 2 stay uncommitted.
- **Git, app repository** (`LDoomD/Week_4_Caregiving-Coordinator`, private): `main` at d5509f5. Pull request 3 (branch add-nextjs-app) is open. The local folder is on the branch add-architecture-draft.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. Owner decisions are chat replies on 2026-11-25. Repository and pull request facts come from `gh` and `git` output on 2026-11-25. The Week 2 requirement comes from the course page copy named in section 2.
- **Checks run:** `check_handoff.py` on this report (result in the chat); `gh pr view` on app pull requests 3 and 4; `git log origin/main` and `git ls-tree` in the app repository; `git status` in the course repository.
- **Not checked:**
  - Whether pull request 3 was merged after this report was written. Check it first.
  - Whether the specs hold a screen list or an email-confirmation decision beyond the five files searched.
  - The live Notion pages and Figma boards for the Week 2 and 3 deliverables were not re-opened. The "all basic homework done" finding rests on the backlog file and a memory note up to 9 days old.
  - Four subpages of Morgan's Week 2 and 3 page (AI Agent Prompt, the ADR list, Title Override List, Hat Match Rule Changes) were not read.
  - The 11 spec files in the app repository other than the build plan were not compared line by line with the originals.
  - Whether Vercel kept a half-finished project, and whether the GitHub check is free for this private repository.
- **How this prevents drift:** outcomes are tagged Approved or Proposed, the open step 5 question and the scope question are the owner's, the first step asks the owner one question and waits, and the rules name the numbering mix-up so it is not repeated.
