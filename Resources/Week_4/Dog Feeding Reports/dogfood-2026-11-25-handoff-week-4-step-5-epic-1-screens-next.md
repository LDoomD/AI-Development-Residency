# Handoff: Week 4 step 5, plan Epic 1's screens next (2026-11-25, sixteenth report)

Replaces: `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-25-handoff-week-4-step-5-after-foundation-plan.md`. What changed: the architecture plan now covers the foundation and Epic 3 (merged), the UX laws reference was added to the project's UX skill, and the owner said step 5 is not finished until the other epics are planned. Every path in this report starts at the top folder of the course repository (`AI Developer Residency `). Paths for the app repository are written in plain text because that repository sits outside this one.

> Paste to start: "Read this handoff report, then the Week 4 reference report and the files in section 8. Confirm in a few short, plain sentences where we are, using only my Build and Launch Checklist and its four groups. Run git fetch in both repositories and tell me whether any pull request is open. Then start planning Epic 1's screens with me, one question at a time, using the ux-ui-design-review skill. Short sentences. Name the file or command behind every fact. Never make anything up. Ask before Firecrawl, Chrome or the browser pane."

## 0. Start here
- **Where we are:** Week 4. The owner's Build and Launch Checklist has four groups: (1) Set up your accounts and tools, steps 1 to 3, finished; (2) Build the app on your computer, steps 4 to 10, in progress; (3) Launch it on the internet, steps 11 to 14, not started; (4) Move your tickets as you work, not started. Step 4 (the Next.js app) is finished and merged. **Step 5, "Architect the app," is not finished.**
- **The outcome so far, in one sentence:** docs/architecture.md in the app repository is merged and plans the screens, server rules and tables for the foundation and Epic 3 only, which is 1 of the 6 epics and 5 of the 27 tasks.
- **Next milestone:** finish step 5 by planning the screens, server code and database for Epics 1, 2, 4, 5 and 6, starting with Epic 1. Step 5 word for word from the Notion checklist: "Architect the app. Plan the screens (tier 1), the server code (tier 2), and the database (tier 3). Ask Claude to write the plan in a document and save it in your repository before you write any code."
- **How the owner wants answers:** say done or not done plainly (the owner said: "Is it finished, or is it not finished?"), one A or B decision per message, short, with sources. See section 7.

## 1. Locked outcomes
All of these were chosen by the owner in chat on 2026-11-25. They are saved in docs/architecture.md in the app repository unless noted.

| Outcome | Tag | Where it lives |
|---|---|---|
| Sign-up asks only for an email and a password | **Approved** | docs/architecture.md, part 2 |
| Email confirmation is off in Week 4 (fake data only). It must be turned on, with an outside email service, before any real caregiver data | **Approved** | docs/architecture.md, parts 3 and 10 |
| A "Set up your care circle" screen right after the first sign-in, asking for a label (parent, spouse or partner) and a nickname the caregiver picks | **Approved** | docs/architecture.md, parts 2 and 6 |
| All six foundation tables (accounts, care circles, cared-for person, circle members and roles, consent records, access log) are created together in one migration file with access rules on each | **Approved** | docs/architecture.md, part 6 |
| Epic 3's screens depend on the care circle's label | **Approved** | docs/architecture.md, part 2 |
| A parent circle gets one list page ("Things to try with" the nickname). "Add" asks for a health step, a safer move, or paid help or aids | **Approved** | docs/architecture.md, part 2 |
| A spouse or partner circle gets two pages: "Topics to talk about" and "Who does what" | **Approved** | docs/architecture.md, part 2 |
| The consent to collect notes is asked when the person first tries to save a note | **Approved** | docs/architecture.md, part 2 |
| The consent to share notes is a separate "Share notes with the circle" step on the circle page, off by default | **Approved** | docs/architecture.md, part 2 |
| "Forgot password?" stays out of the plan for now and stays in part 10 | **Approved** | docs/architecture.md, part 10 |
| A UX laws and Nielsen Norman Group reference was added to the ux-ui-design-review skill, and the skill may review planned screens. Use it whenever it fits | **Approved** | `caregiving-coordinator/.claude/skills/ux-ui-design-review/references/ux-laws-and-nngroup-guidance.md`; the same files in the app repository |
| The owner continues with the basic homework only | **Approved** | `caregiving-coordinator/docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md` |
| Rules for the screens from the planned-screen UX review: keep the typed note at the consent step, a way to add a second circle, password rules and "show password," a first-visit home page | **Proposed** (merged in the document, not individually approved) | docs/architecture.md, part 2 |

## 2. Key findings and data
| Finding | Source | Confidence |
|---|---|---|
| App pull requests 3, 4, 5 and 6 are merged. Course pull requests 100, 101 and 102 are merged. No pull request is open in either repository. | `gh pr view`, `gh pr list`, 2026-11-25 | Authoritative |
| App `main` is at commit 6e6202f. The local app folder is on `main` and clean. | `git log`, `git status`, 2026-11-25 | Authoritative |
| The numbered epics file has 6 epics, 10 features and 27 tasks. Tasks per epic: Epic 1 has 6, Epic 2 has 5, Epic 3 has 5, Epic 4 has 5, Epic 5 has 3, Epic 6 has 3. Epic 3 and the foundation are planned. | `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md` | Authoritative |
| Task pages and task flows exist only for Epic 1 (6 tasks) and Epic 3 (5 tasks). Epics 2, 4, 5 and 6 have only the numbered task names and the user stories. | `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-1-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-3-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-1-2026-11-16.md`, `caregiving-coordinator/docs/clean-deliverables/epic-and-feature-user-stories-2026-11-15.md` | Authoritative (listing only; Epic 1 pages not read this session) |
| Epic 1's records are two tables, care_breaks (the care circle can see them) and private_records (only the writer can see them). The private-records rule (T4.1.4) is Proposed, not approved, and is open for a lawyer. | `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`, T2.1.3 and T4.1.4 | Authoritative |
| The Week 2 course page asks for a build plan with Vercel, Supabase, GitHub and user accounts with secured data. The saved build plan covers all four. | `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Week 2 Coding Challenge - Develop Product Specifications for the ADHD Budgeting App (Notion copy 2026-11-13).md`, lines 86 to 91 | Authoritative |
| The specs hold no list of screens. Screens were decided with the owner in this session. | `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md` | Authoritative |
| 48 UX source copies were saved: 30 from lawsofux.com and 18 from nngroup.com, with index entries. A helper retyped the page text, so the copies are not byte-for-byte. NN/g has no Hick's law article, only a video page that was not watched. | `caregiving-coordinator/docs/sources/ux-laws-2026-11-25/`, `caregiving-coordinator/docs/sources/INDEX.md` | Credible secondary |
| NN/g's registration checklist (a 2017 article about mobile forms) says to ask for email and password only and not to ask people to confirm registration by email. It also says to include a "Forgot password?" link. | `caregiving-coordinator/docs/sources/ux-laws-2026-11-25/nngroup/checklist-registration-login.md`, read 2026-11-25 | Credible secondary |
| Gate and 21 hook tests passed in both repositories before the last pushes. GitHub showed no check results on the pull requests when looked at. | Command output, 2026-11-25 | Authoritative |

## 3. Excluded and deferred
- **Business-logic approach (Transaction Scripts or a Domain Model).** Not a checklist step. It sits in part 5 of Morgan's page. Not decided. Ask only when part 5 is reached, with the teacher's chart (Figma node 3079:10802).
- **Forgot password, two-step sign-in, and the relative invite screen.** Out for now (see section 1 and part 10 of the document).
- **Parts 4, 5, 7, 8 and 9 of Morgan's Architecture page.** Not on the owner's step 5 text. Part 9 (ADRs) is step 6.
- **ADRs (step 6), database design (step 7), Supabase project (step 8), features (step 9), tests (step 10).** Each at its numbered step. Do not start early.
- **Vercel import and deploy:** step 11. A half-finished Vercel project may exist; unknown.
- **Bonus homework** (feature analysis, pitch deck, prototypes, advanced usability tests). Not being done.
- **Owner-only items:** the "What I Did" and "What I Learned" summary (no AI), sharing and emailing the submission page, submitting the Premium paper, ticking steps on the owner's Notion checklist. I never write or edit the summary.
- **Deleted on 2026-11-25 at the owner's request:** the unrelated immigrant-data-security folder and its INDEX.md lines. They were never committed and cannot be recovered. Do not look for them.
- **The app repository's local branches** and old merged branches may still exist. Tidy only when the owner asks.

## 4. Open decisions
1. **Plan Epic 1's screens next.** Why: step 5 is not finished until the screens, server rules and tables for the other epics are planned. Epic 1 has six task pages and flows already. Choice: yes, start now (recommended: it uses the owner's existing task pages). After a yes, I read the Epic 1 task pages and flows, then propose the screens one question at a time and update docs/architecture.md on a new branch with its own pull request.
2. **How to plan Epics 2, 4, 5 and 6, which have no task pages.** Why: the screens would come from only the feature and task names and the user stories. Choices: **A**, plan from those names and stories and mark them thin; or **B**, write the task pages first (more work, closer to the owner's Week 2 method). Ask this after Epic 1 is done.
3. **What "the entire MVP #1" means for the Week 4 build.** The course page says the whole MVP #1 is built. The owner said there is no deadline. Choices: build in roadmap order until done, or narrow the first release. Do not decide alone.
4. **Private records in Epic 1 (T4.1.4).** Why it matters: it decides who can see a caregiver's own wellbeing notes. It is Proposed and open for a lawyer. Ask when Epic 1's tables are planned.
5. **The email service, "Forgot password," and turning email confirmation on.** All three depend on each other and are needed before real caregiver data.
6. **How a second person joins a circle.** Invites need the email service. The share-consent scenarios need another member, which matters at step 10.
7. **How business rules are coded** (part 5 of Morgan's page). Ask only when part 5 is reached.
8. **The rows marked † in the non-functional list** (for example the Supabase region us-east-1 and Vercel iad1). Confirm when the Supabase project is made (step 8).
9. **Add `npm ci`, lint and build to the GitHub check?** Today it runs only the architecture gate and the hook tests.
10. **Fix line 11 of the steps page** (it names the old repository) and **update the build plan line** that says branch protection is not used. Both wait for the owner's yes.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Epic 1's task pages and flows | Part 2 (screens) and part 6 (tables) of docs/architecture.md | Step 5 asks for the screens, server and database plan |
| The six foundation tables, care notes and care tasks, and Epic 1's two tables | Step 7, the Database Design Template and one migration file with access rules on every table | Step 7 says to save the tables as a migration file and turn on access rules |
| Choices in parts 2 and 3 (Next.js with Material UI, Vercel, Supabase, Supabase Auth, email confirmation off in Week 4) | Step 6, ADRs in docs/adr (does not exist yet). At least three: Next.js with Material UI, Vercel, Supabase | Step 6 says one ADR for each big choice |
| The foundation screens and server behavior | Step 9, feature 1: sign-up and log-in | Step 9 says to start with sign-up and log-in |
| The UX reference and the ux-ui-design-review skill | A review of each epic's planned screens now, and of built screens at step 10 | The owner asked to use the skill whenever it fits |

## 6. First steps
1. Run `git fetch` in both repositories. Run `gh pr list` in each. If any pull request is open, say so in one line and let the owner decide.
2. Read this report, the Week 4 reference report and the files in section 8. Say in a few short sentences where we are, using only the owner's checklist numbers and its four groups. Do not recap this report. Say plainly that step 5 is not finished and why.
3. Switch the app repository to a new branch only when editing docs/architecture.md. The local app folder should be on `main`.
4. Read the Epic 1 task pages and flows. Then run the ux-ui-design-review skill's steps on each screen you propose. Propose Epic 1's screens one decision at a time: outcome first, two options with plain trade-offs, a recommendation marked as yours, the source, then wait for the owner's A or B.
5. When Epic 1 is planned, update docs/architecture.md on a new branch, run the gate and hook tests, and open a pull request. The owner merges. Then ask open decision 2.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md`, the project memory index, the app repository's CLAUDE.md, and `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md` (read it first).
- **Never make anything up.** Name the file or command behind every fact. If not found, say "I did not find this" or "I am guessing."
- **Use only the owner's Build and Launch Checklist numbers.** 14 steps in four groups. Never say "step N of 7" or "part 4" without saying which list. If a part of Morgan's page is meant, say "part N of Morgan's Architecture page."
- **Say done or not done plainly.** Do not ask the owner whether something counts as finished. State it from the checklist text and the files, then say what is left.
- **Use the ux-ui-design-review skill whenever it fits** (the owner asked). Name the law or guideline next to each screen choice, with its source. Use accessibility-check once screens are built.
- **Use every required Week 2 and 3 deliverable,** not one file. The owner reminded me twice. Compare the owner's work with the course page, not with Morgan's example.
- **Short replies, plain words.** One decision per message, with a recommendation marked as mine. Say what "A" and "B" do in plain sentences.
- **Show what is in a file or folder before deleting it,** and say if git cannot recover it.
- **One step at a time.** Questions get answers, not edits.
- **Every task gets a new branch and a pull request.** The owner merges. I never run `gh pr merge` and never commit to `main`.
- **Ask before** Firecrawl, Chrome, the browser pane, or changing GitHub settings.
- **The owner writes "What I Did" and "What I Learned."** I never write or edit them.
- **Fake data only. No secret keys in the repository.**
- **Project skills:** `enterprise-architecture-standards` applies to step 5, `architectural-decision-records` to step 6. Say which skills you applied or judged not relevant before calling work done.

## 8. Where things live
- **Reference report (read first):** `Resources/Week_4/Week 4 Reference Report - Figma, Notion and Checklist Review (2026-11-25).md`
- **Earlier handoff (replaced by this one):** `Resources/Week_4/Dog Feeding Reports/dogfood-2026-11-25-handoff-week-4-step-5-after-foundation-plan.md`
- **Steps page:** `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`
- **Checklist (the order of work):** `Resources/Week_4/Build and Launch Checklist (Notion copy 2026-11-13).md`. The owner's own tick-off copy: https://app.notion.com/p/d929219a469182e580b301c1e92cc0f7
- **Morgan's Architecture page (the guide for the document):** `Resources/Week_4/WEEK 4 Example - Architecture (Notion copy 2026-11-13).md`
- **The architecture plan itself:** app repository, docs/architecture.md (on `main`)
- **Epic 1 pages to read next:** `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-1-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/task-flows-epic-1-2026-11-16.md`, `caregiving-coordinator/docs/clean-deliverables/epic-and-feature-user-stories-2026-11-15.md`
- **Already read for Epic 3:** `caregiving-coordinator/docs/clean-deliverables/task-pages-epic-3-2026-11-15.md`
- **Specs, originals (course repository):** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md`, `caregiving-coordinator/docs/risk-profile.md`, `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-numbered-2026-11-15.md`, `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`. Copies are in the app repository under docs/specs.
- **UX skill and sources:** `caregiving-coordinator/.claude/skills/ux-ui-design-review/references/ux-laws-and-nngroup-guidance.md` and `caregiving-coordinator/docs/sources/ux-laws-2026-11-25/`
- **Git, course repository** (`LDoomD/AI-Development-Residency`): `main` at de58391 before this report. This report is on its own new branch with its own pull request.
- **Git, app repository** (`LDoomD/Week_4_Caregiving-Coordinator`, private): `main` at 6e6202f. No open pull request. The local folder is on `main`.
- **Memory notes written this session** (project memory folder): feedback-week-4-working-style (new), app-repo-and-current-week (updated).

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. Owner decisions are chat replies on 2026-11-25. Repository and pull request facts come from `gh` and `git` output on 2026-11-25.
- **Checks run:** `check_handoff.py` on this report (result in the chat); `gh pr view` and `gh pr list` in both repositories; `git status` and `git log` in both repositories; the architecture gate and 21 hook tests in both repositories before the last pushes.
- **Not checked:**
  - Whether anything changed in either repository after this report was written. Check with `git fetch` first.
  - The Epic 1 task pages, flows and stories were not read this session. Only the Epic 3 task pages, the Epic 3 flows and the user stories file were read in full.
  - GitHub's own checks on the merged pull requests were not seen (the status tool showed no checks).
  - The skill's own evals were not re-run.
  - The 48 saved UX source copies were not compared line by line with the live pages.
  - Whether the owner ticked steps 2, 3 and 4 on the Notion checklist.
  - Whether Vercel kept a half-finished project, and whether the GitHub check is free for this private repository.
- **How this prevents drift:** outcomes are tagged Approved or Proposed, the scope and email questions are the owner's, the first step reads the Epic 1 pages before proposing anything, and the working rules name the mistakes the owner corrected today.
