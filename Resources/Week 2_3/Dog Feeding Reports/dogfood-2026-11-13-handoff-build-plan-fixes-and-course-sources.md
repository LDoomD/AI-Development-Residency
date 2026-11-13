# Handoff: Caregiving Coordinator → Build plan (fixes, boxes 5 and 6, one PR), then the rest of Week 2 homework (2026-11-13)

Replaces: `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md` (2026-11-12, night). Everything there still holds except what sections 2 and 3 below correct. Older reports stay replaced: `dogfood-2026-11-12-handoff-build-plan-week-4-fixes.md`, `dogfood-2026-11-12-handoff-build-plan-and-nfr.md`, `dogfood-2026-11-11-handoff-requirements.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few lines where we are. Then show me the build plan fixes and gaps in section 2 as two short tables, and wait for my yes before changing anything. Keep replies short, one thing at a time. Suggest only verified data (Approved or Fact). Ask before using Firecrawl, the browser pane or Chrome."

## 0. Start here
- **Where we are:** the build plan is drafted. Boxes 1 to 4 are **Approved** and on FigJam. Box 5 is **Proposed**. Box 6 is not started. The list of fixes is **not applied**.
- **What this session did:** it did not touch the build plan. It fixed the course sources.
  - Found that the local course copies used old week numbers (Morgan reorganized the course).
  - Saved fresh, word-for-word copies of Weeks 1 to 5 and rebuilt the `residency-context` skill. **PR 50 is merged** (`main` at `95e93f2`, merged 2026-11-13 22:42 UTC, source: `gh pr view 50`).
  - Compared a student's Non-Functional Requirements page with our build plan: 6 gaps (section 2).
  - Judged the Vercel "agent-browser" tool not worth using now (section 3).
- **The outcome so far, in one sentence:** the course now has a single, dated map of the live weeks and due dates, and the build plan can be fixed against the real Week 4 and Week 5 pages.
- **Next milestone:** apply the build plan fixes (after a yes), approve box 5, draft box 6, then open one PR for the build plan. After that, the rest of the Week 2 homework.
- **Owner's track (Approved, 2026-11-12):** Premium. The owner builds their own app, the caregiving coordinator. Never use the ADHD example's names as theirs.
- **Owner decision (Approved, 2026-11-12):** the course dates (Nov 16) do not drive the plan. The roadmap order stays.

## 1. Locked outcomes

### Earlier milestones (Approved, merged)
Positioning, epics, roadmap, Notion backlog: PRs 43 to 47. Laws research and risk profile: PR 49. Details: `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md`, section 1.

### This session (Approved by the owner in chat, 2026-11-13)
| Outcome | Where it lives |
|---|---|
| Fresh copies of the live course pages for Weeks 1 to 5, plus Syllabus and Weekly Lesson Space. **PR 50 merged.** | `Resources/` (section 8); `git log origin/main` |
| Rebuilt `residency-context` skill: live week numbers, old files kept in `reference/_superseded-2026-10-28/` | `.claude/skills/residency-context/` |
| Weeks 1 to 5 now, Weeks 6 to 9 later ("A") | owner's chat reply |
| Left out of the copies: podcasts, quizzes, flashcards, class working agreements, training signup, Drive videos. Kept: lecture notes, transcripts, syllabus. | owner's chat reply |
| Ask before using Firecrawl, the browser pane or Chrome | memory `ask-before-firecrawl-or-browser.md` |

### Build plan: `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (not committed)
| Box | Status |
|---|---|
| 1. Tool selection | **Approved** |
| 2. Database architecture | **Approved** |
| 3. System architecture | **Approved** |
| 4. Security protocol (eleven rules) | **Approved** |
| 5. Development operations | **Proposed** |
| 6. Quality engineering | Not started |

Access log is **Approved** and still not in `docs/risk-profile.md`. FigJam section `3073:8029` shows boxes 1 to 4 green.

## 2. Key findings and data

### The live course, as of 2026-11-13
Source: homework index copy and syllabus copy (`Resources/Course Hub (Notion copy 2026-11-13)/`; `reference/homework-index.md` in the skill). Confidence: Authoritative (course).

| Course week | Challenge | Due | Source |
|---|---|---|---|
| 1 | Github and Claude Code Skills | Oct 19 | `reference/homework-index.md` |
| 2 (Premium only) | Research Paper and Proposal | Oct 19 | `reference/homework-index.md` |
| **2 and 3, one block** | Develop Product Specifications | Nov 2 | `reference/homework-index.md` |
| 4 | Code and Launch a Web App | Nov 16 | `reference/homework-index.md` |
| 5 | Build a CI/CD Pipeline | Nov 23 | `reference/homework-index.md` |
| 6 | Security Test a Code Base | Nov 30 | `reference/homework-index.md` |
| 7 | AI Chatbot for Career Coaching (syllabus: Agent-Based Apps; the table row's "Progressive Web App" label is a leftover) | Dec 7 | `reference/homework-index.md` |
| 8 | Integrate Apps Together | Dec 14 | `reference/homework-index.md` |
| 9 | SEO / AEO Strategy | Jan 5 | `reference/homework-index.md` |

- **There is no separate Week 3 challenge.** The course map explains every shift: `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Course Map - live schedule, page list and copy status (2026-11-13).md`.
- **Week 2 Basic Homework** lists technical requirements and user requirements (Week 2 page). **Week 4** lists them only under Advanced Homework, for changes after usability tests (Week 4 page). Both are Authoritative.

### Week 4 and Week 5 pages, for the build plan (Authoritative; files in section 8)
| Fact | Source |
|---|---|
| Free Vercel and Supabase plans; use fake data only | Week 4 page, Tools and Requirements 7 |
| At least 3 ADRs in `docs/adr` (Next.js with MUI, Vercel, Supabase), plus one per big choice | Week 4 page, Basic Homework 10 and 11 |
| Row-level security on every table; keys out of GitHub; Database Design and Keep Your App Safe templates | Week 4 page, Requirements 5 to 7 |
| Submission file: `Week 4 Coding Challenge/SUBMISSION.md`; the owner writes it, no AI | Week 4 page, To Submit |
| CI/CD on **GitHub Actions**: automatic checks from your MVP requirements, gate-check the Week 1 Claude Skills, write two manual test case scenarios; Premium applies it to their own app | Week 5 page (`Resources/Week_5/`) |

### The 8 build plan fixes (Proposed, not applied)
| # | Box | Now says | Fix | Source |
|---|---|---|---|---|
| 1 | 1 | Week 4's OpenRouter is for a separate chatbot | Remove it. Week 4 builds the owner's own app. The chatbot is Week 7 (OpenRouter belongs there). | Week 4 page; Week 7 page |
| 2 | 1 | Supabase Pro ($25/mo) before real data | Week 4 uses free plans and fake data. Keep Pro for real data later. | Week 4 page, Tools; build plan box 1 |
| 3 | 2 | Diagram is a Week 3 deliverable | It is a Week 4 deliverable, saved in `docs`. | Week 4 page, Deliverables |
| 4 | 3 | Repo name open | A new public repo for the caregiving app. **The owner picks the name.** | Week 2 page, requirement 5; owner, 2026-11-12 |
| 5 | 5 | PR checks with GitHub Actions | Keep Proposed. Cite the Week 5 page: GitHub Actions is the course's choice. | Week 5 page (`Resources/Week_5/`) |
| 6 | 4 | `.env` files | Use the course's name, `.env.local`. | Keep Your App Safe Checklist (`Resources/Week_4/`) |
| 7 | 4 | (missing) | If a key reaches GitHub, make a new key right away. | Keep Your App Safe Checklist (`Resources/Week_4/`) |
| 8 | 4, 5 | Preview copies never use real data | Fake data everywhere in Week 4. | Week 4 page, Requirements 7 |

### Gaps from a student's Non-Functional Requirements page (Proposed)
Source: the student's page `app.notion.com/p/4179219a4691805b8d9ac1d4f59a69a9` (UAE telehealth app; used only for gaps, not copied). Format: Morgan's "Technical and Non-Functional Backlog" (Epic T# → Feature → Requirement). Our boxes already cover its hosting, database, security, consent and CI/CD sections.

| # | Gap in our build plan | Where it would go | Source |
|---|---|---|---|
| 1 | Input safety: validate input, rate-limit sensitive actions | Box 4 | student page (T1 to T11) |
| 2 | Reliability: what happens when a service is down, error monitoring, a tested restore, recovery targets | Box 5 or a new rule | student page (T1 to T11) |
| 3 | Accessibility (WCAG 2.2 AA) as a blocking check before release | Box 6 | student page (T1 to T11) |
| 4 | Data-subject rights: view and correct (we have delete only) | Box 4 | student page (T1 to T11) |
| 5 | Privacy policy and records-retention policy | Box 4 | student page (T1 to T11) |
| 6 | Box 6 model: critical-path tests, and a release blocked unless tests plus accessibility and security checks pass | Box 6 | student page (T1 to T11) |

### Morgan's worked example
`Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Morgan Hat Check/` has a "Technical Requirements" page and an "Architecture and Build Plan" page. They show the format the course expects for the technical requirements. Incomplete: ADR-0001 to 0039 and about 14 deeper pages were not saved.

### Week 2 homework status (checked 2026-11-13 by `ls docs`; unchanged from 11-12 except the paper)
| Homework | Status | Source |
|---|---|---|
| Market, competitor, feature analysis, positioning, audience segmentation; vision and scope; epics, features, tasks | Done (PRs 43 to 46) | `git log origin/main` |
| Backlog | Started: 11 tasks, Epics 3 and 1 (PR 47) | `docs/clean-deliverables/notion-backlog-2026-11-11.md` |
| Build plan and non-functional requirements | Boxes 1 to 4 approved; 5 proposed; 6 not started | build plan draft |
| Technical requirements; user requirements | Not started (no file in `docs/`) | `ls docs` |
| GitHub repo for the app | Not made (`gh repo list` on 11-12 showed none) | `gh repo list`, 2026-11-12 |
| Notion product specs page; pitch deck | Not started | 11-12 handoff, section 2 |
| Premium research paper | `docs/specialization-research-paper.md` exists. Whether it was submitted is unconfirmed; ask the owner. | `ls docs` |
| One-page summary | The owner writes it, no AI | Week 2 page, requirement 9 |

## 3. Excluded and deferred
- **Weeks 6 to 9 markdown copies:** deferred by the owner's choice A. They are already copied in Notion (page "Tech Fleet course copies 2026-11-13"). The skill's `week-6.md` to `week-9.md` are the old snapshot, renumbered and marked "not re-checked."
- **Word-for-word checks of the lecture notes and other retyped files:** optional, not done. Only the Week 1 and Week 2 transcripts were checked (0 differences).
- **Agent-browser (Vercel's browser tool):** judged **not worth using now**. Reason: it is safe-looking (Apache-2.0, Vercel Labs, npm provenance) but adds an install and a Chrome download, its token-saving claim is the vendor's own, and our existing tools already read pages as an element list. Revisit when the live app needs repeatable browser tests, with its domain allowlist and action policy turned on. Source: `gh` and npm registry reads, 2026-11-13.
- **Cookie-based Notion exporters** (notion-exporter, notiondl): rejected. They need the owner's Notion login cookie.
- **Course dates (Nov 16):** set aside by the owner. The roadmap order stays (Epic 3, then 1, 4, 5 and 6, then 2).
- **Still out of MVP #1:** visit recordings, AI notes, medication lists, stored portal logins. Who pays, Reddit and Arctic Shift stay parked.
- **Where Week 4 files live** (new repo vs `caregiving-coordinator`): deferred until the repo is set up.

## 4. Open decisions
The next session must not decide these alone.
- Apply the 8 fixes now, or wait until Week 4. Which of the 6 gaps to add.
- Approve box 5.
- The new repo's name.
- Whether the Premium research paper was submitted.
- Order of the remaining Week 2 homework (repo, technical requirements, user requirements, Notion page, pitch deck).
- How much of MVP #1 to build first. Which email service. The 2 lawyer questions (whose consent counts; California CMIA).
- One PR for the build plan (draft, sources, `INDEX.md`, risk profile access log line): Proposed, not asked yet.
- Whether Workshop Space should be copied (the owner's message was unclear, so it was left out).
- Whether the Week 7 row label ("Progressive Web App") is a leftover: only Morgan can say.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Week 4 and Week 5 pages | The 8 fixes; boxes 1, 5 and 6 | Match the live course |
| Week 5 page | Boxes 5 and 6 detail | CI/CD and manual test cases are taught there |
| Student page gaps (6) | Boxes 4 to 6 | Proposed additions |
| Morgan's Technical Requirements example | The technical requirements deliverable (not started) | Shows the course's format |
| Week 4 templates (Database Design, Keep Your App Safe, ADR) | Box 2 and 4, ADRs 0001 to 0003 | Week 4 deliverables |
| Backlog tasks and epics | User requirements; the blank Notion Epics and Features page | Still Week 2 homework |

## 6. First steps
1. Confirm where we are in a few lines. Run `git status` and `gh pr list --state open`. `main` is at `95e93f2` or later. Start a new branch from `origin/main` for the build plan.
2. **Show the owner the 8 fixes and the 6 gaps** (section 2) as two short tables. Change nothing until the owner says yes.
3. After a yes: save the Week 4 and Week 5 pages' facts as sources in `docs/sources/build-plan-2026-11-12/` (the full pages are already in `Resources/`), log them in `INDEX.md`, apply the fixes to the markdown, then FigJam node `3073:8029`.
4. Ask the owner to approve box 5, then draft box 6 from the Week 5 page and the Week 5 lecture notes.
5. Ask about one PR for the build plan.
6. Then ask which Week 2 homework comes next.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory. Most likely to break next:
- **Ask before Firecrawl, the browser pane or Chrome.** Try the Notion connector first for Notion pages.
- **Course questions: read `.claude/skills/residency-context/reference/course-map.md` first.** Use the live week numbers. Never use `_superseded-2026-10-28/` for requirements.
- **Do one step at a time and don't suggest the next step unasked.** The owner said "why are you suggesting that?" when I jumped ahead.
- **Premium track: the owner's own app.** Never use the ADHD example's names.
- **Questions get answers, not edits.**
- **One box at a time.** Show it, wait for approval, then FigJam (node `3073:8029` only).
- **Tag every line** Approved, Fact or Proposed.
- **Never write the owner's Submission Template or one-page summary.**
- **Laws: never conclude.** Never say "compliant."
- **Short replies, 8th-grade words, small tables.** The owner has ADHD; heavy manual work should be done by me where permitted.

## 8. Where things live
- **Course copies (Notion):** page "Tech Fleet course copies 2026-11-13" (`4179219a-4691-813a-b7af-cc52ff63b30b`) in the "Orlando's Notion" workspace. Notion connector workspace: "Orlando's Notion".
- **Course copies (files, on `main`):** `Resources/Week_1/`, `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/` (with `Morgan Hat Check/`), `Resources/Week_4/` (28 files), `Resources/Week_5/` (8 files), `Resources/Course Hub (Notion copy 2026-11-13)/`.
- **Course map:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Course Map - live schedule, page list and copy status (2026-11-13).md`, plus the master Week 2 page copy in the same folder.
- **Skill:** `.claude/skills/residency-context/` (`reference/course-map.md` is the index).
- **Build plan draft:** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (195 lines, boxes 1 to 5, not committed). Sources: `docs/sources/build-plan-2026-11-12/` (files 01 to 10), logged in `docs/sources/INDEX.md`.
- **Risk profile:** `docs/risk-profile.md` (Approved, on main).
- **FigJam:** board `HcDDdEGAnikTImO8v7UPMp`, section `3073:8029`. Lecture board: `mqryoCyR9mAw3v6kyDlmes`.
- **Git (2026-11-13):** `origin/main` at `95e93f2` (PR 50 merged). No open PRs from the course-copies work.
  - **Uncommitted, on purpose** (build plan work): the build plan draft, `docs/sources/build-plan-2026-11-12/`, the `docs/sources/INDEX.md` change, `il.html`, and `dogfood-2026-11-05-audit-and.textClipping`.
  - The 11-12 handoff reports and the "Replaced by" notes travel with this handoff's PR.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-13. Due dates: the homework index and syllabus copies.
- **Checks run:**
  - PR 50 confirmed merged (`gh pr view 50`).
  - The Homework table copy matched the live scrape read the same day.
  - The Week 1 and Week 2 transcripts matched Notion word for word (16,865 and 8,016 words, 0 differences).
  - The skill folder: each renumbered file still contains its full original text; all 13 originals are in `_superseded-2026-10-28/`; every path `SKILL.md` names exists.
  - Secrets scan on the files committed in PR 50: no keys or tokens.
  - Agent-browser: `gh api` reads of metadata, README, `package.json`, `postinstall.js` (first 140 lines), security docs; npm registry.
- **Not checked:**
  - The lecture notes and other Weeks 1 to 3 pages were retyped and not diffed. The Syllabus and Weekly Lesson Space copies were typed from the connector and not diffed.
  - Weeks 6 to 9 files are old text, unverified against the live pages.
  - Whether the Week 2 Premium paper was submitted.
  - Agent-browser's Rust source, binaries and known vulnerabilities.
  - The student page's claims were not verified; it was used only to find gaps in our plan.
  - Whether `docs/specialization-research-paper.md` is complete.
  - `check_handoff.py` was run on this report (result in chat).
- **How this prevents drift:** the week renumbering is stated first and tied to a map file. Fixes and gaps are Proposed. First step 2 stops for the owner before any edit.
