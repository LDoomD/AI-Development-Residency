# Handoff: Caregiving Coordinator → Build plan fixes, then the rest of Week 2 (2026-11-12, night)

Replaced by: `dogfood-2026-11-13-handoff-build-plan-fixes-and-course-sources.md` (2026-11-13).

Replaces: `dogfood-2026-11-12-handoff-build-plan-week-4-fixes.md` (same day, evening). Everything there still holds except what section 3 below corrects. Older reports stay replaced: `dogfood-2026-11-12-handoff-build-plan-and-nfr.md`, `dogfood-2026-11-11-handoff-requirements.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few lines where we are. Then show me the 8 build plan fixes in section 6, step 2, as a short table, and wait for my yes before changing anything. Keep replies short, one thing at a time. Suggest only verified data (Approved or Fact)."

## 0. Start here
- **Where we are:** the build plan is drafted. Boxes 1 to 4 are **Approved** and on FigJam. Box 5 is **Proposed**, waiting on the owner. Box 6 is not started.
- **What this session did:** read the live Week 2 page, the live Week 4 templates page and its 5 basic templates. Made a list of 8 fixes so the build plan matches the live course. **Nothing was edited.**
- **Owner correction (Approved, 2026-11-12): the owner is on the Premium track.** "ADHD Budgeting App" is only the course's example. The owner builds their own app, the caregiving coordinator. Never use the example's names (like the repo "Week 3 - ADHD Budgeting App") as the owner's.
- **Owner decision (Approved, 2026-11-12, earlier):** "We don't have to follow those dates. It's okay that I'm behind."
- **Week 2 and Week 3 are one assignment** (owner, 2026-11-12). There is no separate Week 3 homework.
- **Next milestone:** apply the 8 fixes (after a yes), approve box 5, draft box 6, then one PR for the build plan. Then the rest of the Week 2 homework (section 2, status table).

## 1. Locked outcomes

### Earlier milestones (all Approved, merged)
| Deliverable | Status | Where |
|---|---|---|
| Market, competitor, feature analysis, audience segmentation | Approved | FigJam; master reports in `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/` |
| Vision and scope | Approved | PR 43 |
| Positioning | Approved | PR 44 |
| Epics, features, tasks | Approved | PR 45 |
| Release roadmap | Approved | PR 46 |
| Notion backlog (11 tasks, first 2 weeks, Epics 3 and 1) | Approved | PR 47 |
| Laws research and risk profile | Approved 2026-11-12 | PR 49 (`main` at `d7c4f73`, source: `git log origin/main`, run 2026-11-12) |

### Build plan: `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (not committed)
| Box | Status | Main content |
|---|---|---|
| 1. Tool selection | **Approved** | Claude Code, GitHub, Vercel, Supabase, Supabase Auth, Material UI, an outside email service (not chosen) |
| 2. Database architecture | **Approved** | Foundation tables (accounts, care circles, cared-for person, members and roles, consent records, access log), Epic 3 tables, Epics 5 and 6 tables |
| 3. System architecture | **Approved** | Browser → Next.js on Vercel (iad1) → Supabase US region with row-level security; Supabase Auth cookie sessions; outside email service |
| 4. Security protocol | **Approved** | 11 rules, including admin key on the server only, no trackers, access log, 60-day breach plan (source: build plan draft, box 4) |
| 5. Development operations | **Proposed** | Branch → PR → Vercel preview → owner merges → instant rollback |
| 6. Quality engineering | Not started | — |

- Access log: **Approved**, in boxes 2 and 4, not yet in `docs/risk-profile.md`.
- Two-step sign-in: Week 5 reminder in memory (`week-5-two-step-signin-reminder.md`).

## 2. Key findings and data

### Week 2 page (live, Firecrawl, 2026-11-12)
Source: [Week 2 Coding Challenge](https://tech-fleet-community-dao.notion.site/Week-2-Coding-Challenge-Develop-Product-Specifications-for-the-ADHD-Budgeting-App-30d1a3bddce5824b87d88176985ad522). Not saved in `docs/sources/` yet.
- Premium objective: "you are building the app you chose based on your specialization." (Authoritative)
- Build plan must assume a three-tier app with stored data: Vercel, Supabase, GitHub, user accounts with secured user data. Boxes 1, 3 and 4 already match. (Authoritative)
- A new **public** GitHub repo, no code yet, for the app. The example name is the ADHD one; the owner picks their own. (Authoritative)
- Results go in Notion. Submit by email with the Notion link. One-page summary written without AI. (Authoritative)

### Week 4 templates (live, Firecrawl, 2026-11-12)
Source: [Week 4 Build and Launch Templates](https://tech-fleet-community-dao.notion.site/Week-4-Coding-Challenge-Build-and-Launch-Templates-40a1a3bddce581adbe51fab0234a66d4) and its 5 basic templates (Build and Launch Checklist, ADR, Database Design, Keep Your App Safe, Submission). Not saved yet. Bonus templates (rapid prototype tests) not opened.
| Template | What it asks | Build plan box |
|---|---|---|
| Build and Launch Checklist, 14 steps | Free Vercel and Supabase accounts; Next.js with MUI in the Week 2 repo; 3-tier plan saved before code; ADRs; database design; one feature at a time, sign-up first; 2-account test; connect Vercel; test live and on phone; move Kanban tickets to Done (source: Build and Launch Checklist page) | 1, 3, 4, 5, 6 |
| ADR | `docs/adr/0001-...md`, one decision each: Context, Options, Decision, Consequences. Add a line to `CLAUDE.md` to read every ADR. | 1 |
| Database Design | `docs/database-design.md`; RLS on every table; 2-account test; diagram in `docs` (Schema Visualizer screenshot or Mermaid); migration files | 2 |
| Keep Your App Safe | Keys in `.env.local`, listed in `.gitignore`; keys in Vercel settings; secret key never in the browser; make a new key if one reaches GitHub; fake data only | 4 |
| Submission | `Week 4 Coding Challenge/SUBMISSION.md`; links to repo, Vercel, diagram, `docs/adr`; 2+ paragraphs "What I Did" and "What I Learned," **no AI** | Owner only |

### The 8 build plan fixes (Proposed, not applied)
| # | Box | Now says | Fix |
|---|---|---|---|
| 1 | 1 | Week 4's OpenRouter is for a separate chatbot | Remove; Week 4 builds the owner's own app |
| 2 | 1 | Supabase Pro ($25/mo) before real data | Week 4 uses free plans and fake data; keep Pro for real data later (source: Week 4 checklist step 1; build plan box 1) |
| 3 | 2 | Diagram is a Week 3 deliverable (line 87) | Week 4 deliverable, saved in `docs` (source: Database Design template) |
| 4 | 3 | Repo name open | A new public repo for the caregiving app; **owner picks the name**. Not "ADHD Budgeting App." |
| 5 | 5 | PR checks with GitHub Actions | Keep Proposed; mark "detail in Week 5" |
| 6 | 4 | `.env` files | Use the course's name, `.env.local` |
| 7 | 4 | (missing) | If a key reaches GitHub, make a new key right away |
| 8 | 4, 5 | Preview copies never use real data (line 184) | Fake data everywhere in Week 4 (source: Keep Your App Safe checklist) |

### Week 2 homework status (checked 2026-11-12)
| Homework | Status | Source |
|---|---|---|
| Market, competitor, feature analysis, positioning, audience segmentation | Done | PRs 43 to 44; FigJam |
| Vision and scope; epics, features, tasks | Done | PRs 43, 45 |
| Backlog | Started (11 tasks, Epics 3 and 1) | PR 47 |
| Build plan and non-functional requirements | Almost done (box 5 waiting, box 6 not started) | build plan draft |
| Technical requirements | Not started | `ls docs` (no file) |
| User requirements (feature user stories and scenarios) | Not started | `ls docs`; Notion Epics and Features page is blank |
| GitHub repo for the app | Not made | `gh repo list` showed none |
| Notion product specs page | Blank template (Market Research, Vision and Scope, Epics and Features) | Notion fetch, 2026-11-12 |
| Pitch deck | Not started (PowerPoint, PDF or Figma Slides) | Notion Product Pitch Deck page |
| Prototypes (bonus) | Not started | — |
| One-page summary | Owner writes, no AI | Week 2 page |

## 3. Excluded and deferred
- **Corrected from the evening report:** its box 3 fix said "use the Week 2 repo" and this session first named it "Week 3 - ADHD Budgeting App." **Wrong for Premium.** The repo is for the caregiving app, named by the owner.
- **Where Week 4 files live** (new repo vs `caregiving-coordinator`): deferred until the repo is set up.
- **Course dates (Nov 16):** set aside by the owner. Roadmap order stays (Epic 3, then 1, 4, 5 and 6, then 2).
- **Still out of MVP #1:** visit recordings, AI notes, medication lists, stored portal logins. Who pays, Reddit and Arctic Shift stay parked.

## 4. Open decisions
- Apply the 8 fixes now, or wait until Week 4.
- Approve box 5.
- The new repo's name.
- Order of the remaining Week 2 homework (repo, technical and user requirements, Notion page, pitch deck, prototypes).
- How much of MVP #1 to build first. Which email service. The 2 lawyer questions (whose consent counts; California CMIA).
- One PR for the build plan (draft, sources, `INDEX.md`, risk profile access log line): Proposed, not asked yet.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The 8 fixes | Build plan markdown, then FigJam node `3073:8029` | Match the live course |
| Week 5 board row | Boxes 5 and 6 | CI/CD and QA are taught there |
| Box 1 tools | ADRs 0001 to 0003 | Week 4 ADR template |
| Box 2 tables | `docs/database-design.md`, migrations, diagram | Week 4 Database Design template |
| Box 4 rules | Keep Your App Safe checklist | Compared; 2 rules to add (fixes 6, 7) |
| Backlog tasks and epics | User requirements, Notion Epics and Features page | Blank, still Week 2 homework |

## 6. First steps
1. Confirm where we are in a few lines. Run `git status` and `gh pr list --state open`. The branch is `laws-research-and-risk-profile` (merged), so start a new branch from `origin/main` for the build plan.
2. **Show the owner the 8 fixes** (section 2) as a short table. Change nothing until the owner says yes.
3. After a yes: save the Week 2 page and Week 4 templates in `docs/sources/build-plan-2026-11-12/` and log them in `INDEX.md`. Apply the fixes to the markdown, then FigJam.
4. Ask the owner to approve box 5, then draft box 6 using the Week 5 board row.
5. Ask about one PR for the build plan.
6. Then ask which Week 2 homework comes next.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory. Most likely to break next:
- **Premium track: the owner's own app.** Never use the ADHD example's names or scope as the owner's.
- **Read the live course page, not the local copy** (`residency-context` copies are from 2026-10-28 and out of date).
- **Questions get answers, not edits.** The owner asked "why are we making fixes?": explain, don't edit.
- **One box at a time.** Show it, wait for approval, then FigJam (node `3073:8029` only).
- **Tag every line** Approved, Fact or Proposed.
- **Never write the owner's Submission Template or one-page summary.**
- **Laws: never conclude.** Never say "compliant."
- **Short replies, 8th-grade words, small tables.**

## 8. Where things live
- Build plan draft: `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (195 lines, boxes 1 to 5).
- Build plan sources: `docs/sources/build-plan-2026-11-12/` (files 01 to 10), logged in `docs/sources/INDEX.md`.
- Risk profile: `docs/risk-profile.md` (Approved, on main).
- FigJam: board `HcDDdEGAnikTImO8v7UPMp`, section `3073:8029`.
- Lecture board: `mqryoCyR9mAw3v6kyDlmes` (template node 576:5825; Week 5 row near y = -31,000).
- Notion product specs: [Orlandos: Week 2 Coding Challenge - Product Specs Template](https://app.notion.com/p/4119219a469180b1b6c9dc4d19059d02).
- Git (2026-11-12, night): no open PRs; `origin/main` at `d7c4f73`; branch `laws-research-and-risk-profile` (merged).
  - Uncommitted: the build plan draft, `docs/sources/build-plan-2026-11-12/`, `docs/sources/INDEX.md`, this report, the two earlier 11-12 reports, the "Replaced by" note in `dogfood-2026-11-11-handoff-requirements.md`.
  - Left uncommitted on purpose: `docs/sources/competitive-analysis-4/live-pages/raw/il.html`, `dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The Premium correction and "Week 2 and 3 are one" are the owner's chat words, 2026-11-12.
- **Checks run:** live Week 2 page and 6 Week 4 pages read through Firecrawl; build plan lines found with `grep`; `gh repo list` (no app repo); Notion pages fetched; `git log origin/main`; `check_handoff.py` on this report.
- **Not checked:** the Backlog Kanban Board page in Notion; the 2 bonus Week 4 templates; most Week 4 and 5 lecture board sections (titles only); the course pages are not saved in `docs/sources/` yet.
- **How this prevents drift:** the Premium correction is stated first; the wrong repo name is listed as wrong; fixes are Proposed and step 2 stops for the owner.
