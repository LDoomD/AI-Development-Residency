# Handoff: Caregiving Coordinator → Build plan, fixed to the real Week 4 (2026-11-12, evening)

Replaced by: `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md` (2026-11-12, night).

Replaces: `dogfood-2026-11-12-handoff-build-plan-and-nfr.md` (same day, morning). Everything there still holds except what section 3 below says is out of date. Older reports stay replaced too: `dogfood-2026-11-11-handoff-requirements.md`, `dogfood-2026-11-11-handoff-epics-features-tasks.md`, `dogfood-2026-11-10-handoff-positioning-statements.md`, `dogfood-2026-11-10-handoff-vision-and-scope-part-3.md`.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few lines where we are. Then show me the list of fixes in section 6, step 2, as a short table before changing anything. Keep replies short, one thing at a time. Suggest only verified data (Approved or Fact)."

## 0. Start here
- **Where we are:**
  - The laws research and the risk profile are done and merged (PR 49).
  - The build plan is drafted. Boxes 1 to 4 are approved and on the owner's FigJam board. Box 5 is drafted but not approved. Box 6 hasn't started.
- **What happened at the end:** the owner asked whether Weeks 3 and 4 had been checked carefully. They hadn't. The live Week 4 page and the lecture board's Week 4 row show that some of the build plan draft rests on an out-of-date local copy of the course.
- **Owner decision (Approved, 2026-11-12):** "We don't have to follow those dates. It's okay that I'm behind." The course's Nov 16 deadline does not drive the plan. The approved roadmap's order stays.
- **Next milestone:** fix the build plan to match the real Week 4 page, then finish boxes 5 and 6. Then open one PR for the build plan, with the access log line added to the risk profile.
  - **Template:** board `mqryoCyR9mAw3v6kyDlmes`, node 576:5825.
  - **Week 4 deliverables:** see section 2.

## 1. Locked outcomes

### Earlier milestones (all Approved, merged)
- Positioning, epics, roadmap, Notion backlog and the requirements handoff: PRs 43 to 48. The tables are in `dogfood-2026-11-11-handoff-requirements.md`, section 1.
- **Laws research and risk profile: PR 49, merged 2026-11-12** (`main` at `d7c4f73`; source: `gh pr view 49`, run 2026-11-12).
  - `docs/risk-profile.md` is **Approved** by the owner on 2026-11-12.
  - Findings: `docs/sources/laws-consent-research-2026-11-12/verified-findings-2026-11-12.md`.
  - Research checklist: `docs/research-checklist-laws-database-2026-11-12.md`.

### Build plan: `docs/build-plan-nfr-draft-2026-11-12.md` (not committed)
| Box | Status | Main content | Source |
|---|---|---|---|
| 1. Tool selection | **Approved** 2026-11-12 | Claude Code, GitHub, Vercel, Supabase, Supabase Auth, Material UI, plus an outside email service (no service chosen). Left out: trackers, data-pulling integrations, an outside AI service, payment tools. | `docs/build-plan-nfr-draft-2026-11-12.md` |
| 2. Database architecture | **Approved** 2026-11-12 | Foundation tables: accounts, care circles, cared-for person, members and roles, consent records, access log. Epic 3: care notes, care tasks and owners. Epics 5 and 6: money, benefits and coverage. | `docs/build-plan-nfr-draft-2026-11-12.md` |
| 3. System architecture | **Approved** 2026-11-12 | Browser → Next.js on Vercel (iad1) → Supabase in a US region, with row-level security. Supabase Auth with cookie sessions. An outside email service for invites, because Supabase's built-in email only reaches the project team. | `docs/build-plan-nfr-draft-2026-11-12.md` |
| 4. Security protocol | **Approved** 2026-11-12 | 11 rules: row-level security, two consents, admin key on the server only, no trackers, sign-in checks, HTTPS and encryption at rest, deletion, safe errors, locked packages, an access log, a 60-day breach plan. | `docs/build-plan-nfr-draft-2026-11-12.md` |
| 5. Development operations | **Proposed**, waiting on the owner | Branch → commit checks → PR checks → Vercel preview → owner merges → instant rollback. Migrations in GitHub. Keys in Vercel environment settings. | `docs/build-plan-nfr-draft-2026-11-12.md` |
| 6. Quality engineering | Not started | — | `docs/build-plan-nfr-draft-2026-11-12.md` |

- **Access log: Approved** (owner, "Yes, add it"). It's in boxes 2 and 4. **Not yet in `docs/risk-profile.md` on main.**
- **Two-step sign-in:** a reminder to ask about it in Week 5 is saved in memory (`week-5-two-step-signin-reminder.md`). **Approved** (owner: "make a reminder").
- **FigJam:** the section "Non-Functional Requirements and Build Plan (2026-11-12)" is node `3073:8029` in board `HcDDdEGAnikTImO8v7UPMp`, on page 2782:15415, to the right of the backlog section. It shows boxes 1 to 4 green and box 5 yellow.

## 2. Key findings and data

### The real Week 4 page (live, fetched 2026-11-12)
Source: [Week 4 Coding Challenge - Code and Launch a Web App](https://tech-fleet-community-dao.notion.site/f4b1a3bddce583c1a1ed0161a0078312) (Firecrawl scrape, 2026-11-12). It is linked from the lecture board's Week 4 homework, node 2490:6825. **Not saved in `docs/sources/` yet.**

| What it asks for | Detail | Confidence | Source |
|---|---|---|---|
| Build the entire MVP #1 | "Every epic, feature, and task in your Week 2 MVP #1 scope works in your live app." Due date: Nov 16. **The owner set the date aside.** | Authoritative (course) | Live Week 4 page |
| Repo | Use the Week 2 repo, "Week 3 - ADHD Budgeting App." "Do not make a new one." | Authoritative | Live Week 4 page |
| Stack | Next.js with Material UI, Vercel (free plan), Supabase (free plan) | Authoritative | Live Week 4 page |
| Accounts | People sign up and log in, and each person sees only their own information | Authoritative | Live Week 4 page |
| ADRs | At least 3 in `docs/adr` (Next.js with Material UI, Vercel, Supabase), plus a new one for every other big choice | Authoritative | Live Week 4 page |
| Database | Use the Database Design Template. SQL saved as migration files. Row-level security on every table. A database diagram in `docs`. | Authoritative | Live Week 4 page |
| Safety | Keep keys out of GitHub. Follow the "Keep Your App Safe Checklist." **Use fake data only.** | Authoritative | Live Week 4 page |
| Templates | Build and Launch Checklist (14 steps), ADR, Database Design, Keep Your App Safe, Submission (the owner writes it, NOT using AI) | Authoritative; templates not opened yet | Live Week 4 page |
| Submit | `Week 4 Coding Challenge/SUBMISSION.md` in the repo, a PR merged, and an email with the repo, Vercel and diagram links | Authoritative | Live Week 4 page |

### The lecture board's Week 4 and Week 5 rows (read 2026-11-12)
- **Week 4:** "Hosting Three-Tier Architecture Websites." Sections:
  - Technical Architecture Deliverables (node 2281:7123)
  - ADRs (node 2501:5349)
  - Layers of Software Architecture (node 2323:8108)
  - Software Patterns (node 2280:4144)
  - Business Logic Design (node 2343:8258)
  - Design Systems (node 2536:7815)
  - Web Servers and Database Servers (node 2485:6149)
  - In This Class, This Is How You Launch (node 2490:6455)
  - When Something Breaks (node 2572:5628)
  - Deliverables for Code and Launch (node 2490:6845): "ADRs in docs/adr... Database design, Software layer design, Software pattern design"
- **Week 5:** "Enterprise QA (Quality Assurance)." Sections: CI / CD (node 3642:12561; source: lecture board), DevOps for Product Teams (node 3611:10597), "What Should Continuous Integration Checks Include?" (node 3778:12705), Test Case Scenarios, Types of QA Testing. **Boxes 5 and 6 belong to this week's detail.**
- Only the Week 4 homework, Deliverables and Technical Architecture Deliverables sections were read word for word. The others were seen by title only.

## 3. Excluded and deferred
- **Out of date because of the live Week 4 page (fix these first, section 6):**
  - Box 1's correction says "Week 4's OpenRouter is not for this product... a separate career chatbot." **Wrong.** The local `week-4.md` (copied 2026-10-28) is out of date. Week 4 builds the owner's own app.
  - Box 1 says "Supabase Pro ($25 a month) before any real caregiver data." The course says free plans and **fake data only**. Keep the rule for later real data, but say that Week 4 uses free plans and fake data.
  - Box 2 says the database diagram is "a Week 3 deliverable." It's a Week 4 deliverable, saved in `docs`.
  - Box 3 says the repo name is open (two names on the old Week 3 page). **Settled by the Week 4 page:** use the Week 2 repo. Check whether that repo exists; the 11-12 morning handoff said it wasn't made yet.
  - Box 5's PR-check pipeline (GitHub Actions) is Week 5 detail. Keep it Proposed, and mark it "detail in Week 5."
- **The course dates (Nov 16):** set aside by the owner. The roadmap order stays (Epic 3, then 1, 4, 5 and 6, then 2).
- **Earlier exclusions still hold:** visit recordings, AI notes, medication lists and stored portal logins (out of MVP #1); who pays; Reddit and Arctic Shift.

## 4. Open decisions
The next session must not decide these alone.
- **Approve box 5,** after the Week 4 and 5 fixes.
- **What "MVP #1" means for the build:** the course wants all of it. The owner has set the dates aside but hasn't said how much to build first.
- **Which email service** sends invites.
- **Whether the Week 2 GitHub repo exists**, and its exact name.
- **Lawyer questions** (from the risk profile): whose consent is valid; California's medical privacy law (CMIA).
- **Where the build plan's PR goes:** one PR for the build plan draft, its sources, `INDEX.md` and the risk profile access log line. Proposed, not asked yet.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Live Week 4 page | Fixes to boxes 1, 2, 3 and 5 | It is the current course requirement |
| Box 1 tool choices | ADRs 1 to 3 (Next.js with MUI, Vercel, Supabase) | The Week 4 page requires one ADR for each |
| Box 2 tables | The Database Design Template, migrations and the diagram | Week 4 deliverable |
| Box 4 rules | The "Keep Your App Safe Checklist" | Compare the two, and add anything missing |
| Week 5 board row | Boxes 5 and 6 | That's where CI/CD and QA are taught |
| `docs/risk-profile.md` | Add the access log line | The owner approved it in box 4 |

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr list --state open` and `git status`. The current branch is `laws-research-and-risk-profile` (merged), so start a new branch from `origin/main` for the build plan.
2. **Show the owner the fix list** (section 3, first bullet) as a short table. Change nothing until the owner says yes.
3. **Save the live Week 4 page** in `docs/sources/build-plan-2026-11-12/`, log it in `INDEX.md`, and update the local `.claude/skills/residency-context/reference/week-4.md`, which is out of date. Ask first: it's a skill reference file.
4. After a yes, **apply the fixes** to the markdown, then to FigJam node `3073:8029`.
5. **Ask the owner to approve box 5,** then draft box 6 (Quality engineering), using the Week 5 board row.
6. **Then ask about one PR** for the build plan.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. The rules most likely to be broken next:
- **Read the live course page, not the local copy.** The local `residency-context` copies are from 2026-10-28 and were wrong about Week 4. Check the lecture board row for the current week.
- **Data-driven only.** Tag every line Approved, Fact or Proposed. Label general knowledge as general knowledge.
- **One box at a time.** Show it, wait for approval, then add it to FigJam.
- **FigJam:** add to node `3073:8029` only. Never change other content. Load the `figma-use` and `figma-generate-design` skills before `use_figma`.
- **Questions get answers, not edits.** Short replies.
- **One deliverable = one branch = one PR.** The owner merges.
- **Never write the owner's Submission Template or homework summary.**
- **Laws: never conclude.** Never say "compliant."

## 8. Where things live
- **Build plan draft:** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (boxes 1 to 5).
- **Build plan sources:** `docs/sources/build-plan-2026-11-12/` (files 01 to 10: Supabase SMTP, invite, SSR, RLS and migrations; Vercel Next.js, Git deployments and environments; MUI with Next.js; GitHub protected branches), logged in `docs/sources/INDEX.md`.
- **Risk profile:** `docs/risk-profile.md` (Approved, on main).
- **Laws findings:** `docs/sources/laws-consent-research-2026-11-12/verified-findings-2026-11-12.md`.
- **FigJam:** board `HcDDdEGAnikTImO8v7UPMp`, section `3073:8029` ([link](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3073-8029)).
- **Lecture board:** `mqryoCyR9mAw3v6kyDlmes`.
  - Week 4 row: around y = -66,000.
  - Week 5 row: around y = -31,000.
  - Template: 576:5825.
- **Lecture transcript:** `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`.
- **Git (2026-11-12, evening):**
  - No open PRs. `origin/main` is at `d7c4f73` (PR 49 merged).
  - The local branch is `laws-research-and-risk-profile` (merged).
  - **Uncommitted:**
    - `docs/build-plan-nfr-draft-2026-11-12.md`
    - `docs/sources/build-plan-2026-11-12/`
    - `docs/sources/INDEX.md` (the build plan section)
    - this report
    - the morning handoff
    - the "Replaced by" note in `dogfood-2026-11-11-handoff-requirements.md`
  - Left uncommitted on purpose: `docs/sources/competitive-analysis-4/live-pages/raw/il.html` and `dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** see sections 1 and 2. The box approvals are the owner's chat replies ("Approve, next box," "Sure...," "Approve, add to board," "Yes, add it"). The dates decision is the owner's own words, quoted in section 0.
- **Checks run:**
  - PR 49 confirmed merged (`gh pr view 49`).
  - FigJam screenshots after each board update: no overlap or cut-off text.
  - 27 law quotes were checked word for word earlier today.
  - The live Week 4 page was read in full through Firecrawl.
  - The lecture board's Week 4 homework, Deliverables and Technical Architecture text was read through `use_figma`.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - The Week 4 templates (Build and Launch Checklist, Database Design, Keep Your App Safe, ADR, Submission) weren't opened.
  - Most Week 4 and Week 5 board sections were seen by title only.
  - Whether the Week 2 repo exists wasn't checked.
  - Box 5's GitHub Actions point is general knowledge.
- **How this prevents drift:**
  - The out-of-date items are listed one by one, with the source that corrects them.
  - The owner's dates decision is quoted.
  - First step 2 stops for the owner before any edit.
