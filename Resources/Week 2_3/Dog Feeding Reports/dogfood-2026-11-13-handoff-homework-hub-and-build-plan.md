# Handoff: Caregiving Coordinator → Homework (build plan fixes, then the rest of Weeks 2 and 3), with the course sources, Notion hubs and course skill finished (2026-11-13, evening)

Replaces: `dogfood-2026-11-13-handoff-build-plan-fixes-and-course-sources.md` (earlier the same day, already merged in PR 51). Everything there still holds except what sections 1 to 3 below change. Older reports stay replaced: `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md`, `dogfood-2026-11-12-handoff-build-plan-week-4-fixes.md`, `dogfood-2026-11-12-handoff-build-plan-and-nfr.md`, `dogfood-2026-11-11-handoff-requirements.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few lines, in complete sentences, where we are. Then show me the 8 build plan fixes and the 6 gaps from section 2 as two short tables, and wait for my yes before changing anything. Write complete sentences with context and never use shorthand. Suggest only verified data (Approved or Fact). Ask before using Firecrawl, the browser pane or Chrome."

## 0. Start here
- **Where we are:** the course sources are finished and merged. The owner's two Notion hubs exist. The course skill is upgraded for accuracy. The homework itself is the next thing: the build plan has boxes 1 to 4 approved, box 5 proposed, box 6 not started, and the list of fixes is not applied.
- **What this session did, in one paragraph:** the owner found that the local copies of the course used old week numbers, because Morgan reorganized the course. The session fixed that. It saved fresh word-for-word copies of Weeks 1 to 5 (PR 50), rebuilt the `residency-context` skill around the live numbering, wrote the 2026-11-13 handoff (PR 51), and then built two Notion hubs: a shareable reference-only hub of Tech Fleet's pages, and the owner's private homework hub with a Week 2 and 3 page. It also upgraded the skill with a reading rule, tables of contents, word-for-word submit checklists and a course guide, and saved a new rule about writing in complete sentences.
- **The outcome so far, in one sentence:** every course question can now be answered from a dated, word-for-word copy of the live pages, and the owner has a place to collect and submit each week's homework.
- **Next milestone:** apply the build plan fixes (after the owner says yes), approve box 5, draft box 6, open one pull request for the build plan, then finish the open Week 2 and 3 items (section 2, status table).
- **Owner's track (Approved, 2026-11-12):** Premium. The owner builds their own app, the caregiving coordinator. The ADHD budgeting app is only the course's example.
- **Owner decision (Approved, 2026-11-12):** the course dates do not drive the plan. The roadmap order stays (Epic 3, then 1, 4, 5 and 6, then 2).

## 1. Locked outcomes

### Earlier milestones (Approved, merged)
Positioning, epics, roadmap, Notion backlog: PRs 43 to 47. Laws research and risk profile: PR 49. Details are in `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md`, section 1.

### This session
| Outcome | Tag | Source and where it lives |
|---|---|---|
| Fresh word-for-word copies of Weeks 1 to 5, Syllabus and Weekly Lesson Space, saved under `Resources/` | **Approved**, merged | PR 50, merge commit `95e93f2` (`gh pr view 50`) |
| The 2026-11-13 handoff report | **Approved**, merged | PR 51, merge commit `dde942b` (`git log origin/main`) |
| Rebuilt `residency-context` skill: live week numbers, old files kept in `reference/_superseded-2026-10-28/` | **Approved**, merged | PR 50 |
| Weeks 1 to 5 now, Weeks 6 to 9 later (choice A) | **Approved** | The owner's chat reply, 2026-11-13 |
| Skip podcasts, quizzes, flashcards, class working agreements, training signup and Drive videos; keep lecture notes, transcripts and syllabus | **Approved** | The owner's chat reply, 2026-11-13 |
| Skill upgrade: table of contents, reading rule, word-for-word submit checklists, course guide, duplicate lecture-notes copies removed | **Approved** (owner: "do whatever you suggest would optimize accuracy"), **not committed yet** | `.claude/skills/residency-context/` and this wrap-up's pull request |
| Rule "write complete sentences with context, never shorthand" | **Approved** | `caregiving-coordinator/CLAUDE.md` (Dog feeding section); memory `complete-sentences-with-context.md` |
| Rule "ask before Firecrawl, the browser pane or Chrome" | **Approved** | Memory `ask-before-firecrawl-or-browser.md` |
| Notion reference hub, retitled "REFERENCE ONLY - Tech Fleet course copies (do not submit from here)", with no references to the owner's own pages and a "How to use this hub" section written as toggles | **Approved** | Notion page `4179219a-4691-813a-b7af-cc52ff63b30b` |
| Notion homework hub, titled "Orlando - AI Residency Homework Submissions", one page per week, Week 2 and 3 page laid out like Tech Fleet's six Week 2 templates | **Approved** | Notion pages `4179219a-4691-8176-8eb1-cf901f72e045` and `4179219a-4691-8157-976e-dbc20a0a829f` |
| Reference hub Step 4 prompt now also tells Claude to read whole files, report which files it read, and never write the student's own submission sections; plus an optional toggle "make Claude's reading safer" | **Approved** (owner: "Sounds good") | Notion page `4179219a-4691-813a-b7af-cc52ff63b30b` |

### Build plan: `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (not committed)
| Box | Status | Source |
|---|---|---|
| 1. Tool selection | **Approved** | build plan draft |
| 2. Database architecture | **Approved** | build plan draft |
| 3. System architecture | **Approved** | build plan draft |
| 4. Security protocol (eleven rules) | **Approved** | build plan draft |
| 5. Development operations | **Proposed** | build plan draft |
| 6. Quality engineering | Not started | build plan draft |

The access log is **Approved** (owner, 2026-11-12) and is still not in `docs/risk-profile.md`. FigJam section `3073:8029` shows boxes 1 to 4 green.

## 2. Key findings and data

### The live course (Authoritative: the course's own pages, read 2026-11-13)
| Course week | Challenge | Due | Source |
|---|---|---|---|
| 1 | Github and Claude Code Skills | Oct 19 | `reference/homework-index.md` |
| 2 (Premium only) | Research Paper and Proposal | Oct 19 | `reference/homework-index.md` |
| **2 and 3, one block** | Develop Product Specifications | Nov 2 | `reference/homework-index.md` |
| 4 | Code and Launch a Web App | Nov 16 | `reference/homework-index.md` |
| 5 | Build a CI/CD Pipeline | Nov 23 | `reference/homework-index.md` |
| 6 | Security Test a Code Base | Nov 30 | `reference/homework-index.md` |
| 7 | AI Chatbot for Career Coaching (the syllabus calls it "Building Agent-Based Apps"; the homework table row's "Progressive Web App" label is a leftover) | Dec 7 | `reference/syllabus.md` |
| 8 | Integrate Apps Together | Dec 14 | `reference/homework-index.md` |
| 9 | SEO / AEO Strategy | Jan 5 | `reference/homework-index.md` |

- **There is no separate Week 3 challenge.** Weeks 2 and 3 are one assignment. The mapping from old numbers to live numbers is in the course map: `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Course Map - live schedule, page list and copy status (2026-11-13).md`.
- **Week 2 Basic Homework** lists technical requirements and user requirements. **Week 4** lists them only under Advanced Homework, as changes after usability tests. Both are from the course pages (`reference/week-2-3.md`, `reference/week-4.md`).
- **Week 5 uses GitHub Actions** and asks for automatic checks built from the owner's own MVP requirements, a gate-check of the Week 1 Claude Skills, and two manual test case scenarios. Premium applies it to their own app (`reference/week-5.md`).

### The 8 build plan fixes (Proposed, not applied)
| # | Box | Now says | Fix | Source |
|---|---|---|---|---|
| 1 | 1 | Week 4's OpenRouter is for a separate chatbot | Remove it. Week 4 builds the owner's own app. The chatbot is Week 7. | Week 4 page; Week 7 page |
| 2 | 1 | Supabase Pro ($25/mo) before real data | Week 4 uses free plans and fake data. Keep Pro for real data later. | Week 4 page, Tools; build plan box 1 |
| 3 | 2 | Diagram is a Week 3 deliverable | It is a Week 4 deliverable, saved in `docs`. | Week 4 page, Deliverables |
| 4 | 3 | Repo name open | A new public repo for the caregiving app. The owner picks the name. | Week 2 page, requirement 5; owner, 2026-11-12 |
| 5 | 5 | PR checks with GitHub Actions | Keep Proposed. Cite the Week 5 page: GitHub Actions is the course's choice. | `reference/week-5.md` |
| 6 | 4 | `.env` files | Use the course's name, `.env.local`. | Keep Your App Safe Checklist (`Resources/Week_4/`) |
| 7 | 4 | (missing) | If a key reaches GitHub, make a new key right away. | Keep Your App Safe Checklist |
| 8 | 4, 5 | Preview copies never use real data | Fake data everywhere in Week 4. | Week 4 page, Requirements 7 |

### Six gaps found by comparing a student's Non-Functional Requirements page (Proposed)
Source for all six: the student's page `app.notion.com/p/4179219a4691805b8d9ac1d4f59a69a9` (a UAE telehealth app, used only to find gaps, not copied). Our boxes already cover its hosting, database, security, consent and CI/CD sections.

| # | Gap in our build plan | Where it would go |
|---|---|---|
| 1 | Input safety: validate input, rate-limit sensitive actions | Box 4 |
| 2 | Reliability: a service being down, error monitoring, a tested restore, recovery targets | Box 5 or a new rule |
| 3 | Accessibility (WCAG 2.2 AA) as a blocking check before release | Box 6 |
| 4 | Data-subject rights: view and correct (we have delete only) | Box 4 |
| 5 | Privacy policy and records-retention policy | Box 4 |
| 6 | Box 6 model: critical-path tests, and a release blocked unless tests plus accessibility and security checks pass | Box 6 |

### Week 2 and 3 homework status (checked 2026-11-13)
| Course requirement | Status | Source |
|---|---|---|
| 1. Audience segmentation, use cases | Done | `docs/audience-segmentation.md`, `docs/audience-goals-use-cases.md`, FigJam |
| 2. Market, competitor, feature analysis, positioning | Done | `docs/clean-deliverables/` files; PR 44 |
| 3. Vision and scope (MVP #1 and MMP) | Done in the repository; the Notion template page is empty | `docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md` (PR 43); Notion page `c959219a4691827fac7281ab308fe0d1` fetched 2026-11-13 |
| 4. Epics, features, tasks | Done in the repository; the Notion template page is empty | `docs/clean-deliverables/epics-features-tasks-2026-11-11.md` (PR 45); Notion page `cfc9219a469183c6945281ff637f4185` fetched 2026-11-13 |
| 7. Backlog on the Notion Kanban board | Started: 11 tasks for Epics 3 and 1 | `docs/clean-deliverables/notion-backlog-2026-11-11.md` (PR 47) |
| 5. GitHub repo for the app | Not made | `gh repo list`, 2026-11-12 |
| 6. Build plan | Boxes 1 to 4 approved; 5 proposed; 6 not started | build plan draft |
| 8. Pitch deck | Not started | `ls docs` |
| Technical and user requirements | Not started | `ls docs` |
| Premium research paper | A file exists; submission unconfirmed | `docs/specialization-research-paper.md` |
| 9. One-page summary | The owner writes it, no AI | Week 2 page |

### Other findings
- **An instructor-side audit is inside the copies.** The page "Week 2 Coding Challenge - Product Specs Template (1)" in the reference copies has a long section titled "Rubric Audit (added by Claude)." It argues that Week 2 is overloaded and recommends splitting it into Core and Extended tiers and moving the architecture plan to Weeks 3 to 5. It is a proposal, not a requirement. It was on Tech Fleet's page before the copy was made, and it is not in the saved markdown files or the skill. Source: Notion page `ca89219a469183699caa01a6fd4eb7ec`.
- **Agent-browser (Vercel's browser tool) was judged not worth using now.** It looks safe (Apache-2.0, Vercel Labs, npm provenance) but needs an install and a Chrome download, and its token-saving figure is the vendor's own claim. Revisit when the live app needs repeatable browser tests. Source: `gh` and npm registry reads, 2026-11-13.
- **File sizes, measured with `wc -c`** (about 4 characters per token): `course-map.md` 9 KB, one skill week file 10 to 16 KB, one Week 4 lecture-notes file 110 KB, the Week 2 transcript 100 KB.

## 3. Excluded and deferred
- **Weeks 6 to 9 as markdown:** deferred by the owner's choice A. They are already copied in the Notion reference page. The skill's `week-6.md` to `week-9.md` are the old snapshot, renumbered and marked "not re-checked."
- **Word-for-word checks of the lecture notes and other retyped files:** not done. Only the Week 1 and Week 2 transcripts were checked (0 differences), and the Week 2 challenge file was compared with the earlier master copy.
- **Sharing the homework hub with the instructor:** the owner said "Not yet." The hub is private.
- **Sharing the reference hub with another student:** not set up. The owner plans to do it.
- **Workshop Space copy:** left out because the owner's message about it was unclear.
- **Morgan's Week 2 and 3 example:** incomplete. ADR-0001 to 0039 and about 14 deeper pages were not saved.
- **Cookie-based Notion exporters** (notion-exporter, notiondl): rejected because they need the owner's Notion login cookie.
- **Agent-browser:** deferred, see section 2.
- **Course dates:** set aside by the owner. Earlier exclusions still hold: visit recordings, AI notes, medication lists and stored portal logins stay out of MVP #1, and who pays, Reddit and Arctic Shift stay parked.

## 4. Open decisions
The next session must not decide these alone.
- Apply the 8 fixes now, or wait until Week 4. Which of the 6 gaps to add.
- Approve box 5.
- The new repo's name.
- How to share the homework hub with the instructor (invite him by email with view access, or another way), and when.
- Whether the Premium research paper was submitted.
- Whether the older Notion hub "TechFleet: AI Residency Resource Hub" should be renamed (the owner never answered).
- Whether to fill in the two empty Notion template pages (Vision and Scope, Epics and Features) from the repository files.
- Order of the remaining Week 2 and 3 homework: repo, technical requirements, user requirements, pitch deck, summary.
- How much of MVP #1 to build first. Which email service. The 2 lawyer questions (whose consent counts; California CMIA).
- One pull request for the build plan: Proposed, not asked yet.
- Whether the Week 7 row label is a leftover: only Morgan can say. The owner raises it, not Claude.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Week 4 and Week 5 pages | The 8 fixes; boxes 1, 5 and 6 | Match the live course |
| Week 5 page | Boxes 5 and 6 detail | CI/CD and manual test cases are taught there |
| The 6 student-page gaps | Boxes 4 to 6 | Proposed additions |
| Morgan's Technical Requirements example (`Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Morgan Hat Check/`) | The technical requirements deliverable | Shows the course's format |
| Week 4 templates (Database Design, Keep Your App Safe, ADR) | Boxes 2 and 4, ADRs 0001 to 0003 | Week 4 deliverables |
| The Week 2 and 3 homework page | The owner's Week 2 and 3 submission | The place to collect links and fill in the Submission Template |
| The skill's checklist files | Each week's submission | A word-for-word shortcut for "what do I submit?" |

## 6. First steps
1. Confirm where we are in a few complete sentences. Run `git status` and `gh pr list --state open`. Start a new branch from `origin/main` for any new work.
2. **Show the owner the 8 fixes and the 6 gaps** (section 2) as two short tables. Change nothing until the owner says yes.
3. After a yes: save the Week 4 and Week 5 facts as sources in `docs/sources/build-plan-2026-11-12/` and log them in `INDEX.md`. Apply the fixes to the build plan markdown, then to FigJam node `3073:8029`.
4. Ask the owner to approve box 5, then draft box 6 from the Week 5 page and the Week 5 lecture notes.
5. Ask about one pull request for the build plan.
6. Then ask which Week 2 and 3 item comes next. When the owner starts a new week, read that week's whole file in the skill and create its page in the homework hub.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory. The ones most likely to break next:
- **Write complete sentences with context. Never use shorthand** such as "linked, not moved" or "those copies." Say what you will do, to which named page or file, and what is different afterwards. The owner has flagged this many times.
- **Accuracy over token savings.** Read all of a week's file. End each course answer with "Read: files. Requirements used: numbers."
- **Course questions:** read `.claude/skills/residency-context/reference/course-map.md` first, then the whole week file. Never use `_superseded-2026-10-28/` for requirements.
- **Ask before Firecrawl, the browser pane or Chrome.** Try the Notion connector first for Notion pages.
- **Never put references to the owner's own pages or name in the reference hub.** The owner shares it with other students.
- **Never change sharing settings or write the owner's "What I Did," "What I Learned" or summary.** The owner writes them without AI.
- **Do one step at a time and don't suggest the next step unasked.** Questions get answers, not edits.
- **One box at a time** for the build plan: show it, wait for approval, then FigJam (node `3073:8029` only). Tag every line Approved, Fact or Proposed.
- **Laws: never conclude.** Never say "compliant."
- **Short replies, 8th-grade words, small tables.**

## 8. Where things live
- **Notion (workspace "Orlando's Notion"):**
  - Reference hub: `4179219a-4691-813a-b7af-cc52ff63b30b` ("REFERENCE ONLY - Tech Fleet course copies (do not submit from here)").
  - Homework hub: `4179219a-4691-8176-8eb1-cf901f72e045` ("Orlando - AI Residency Homework Submissions"), with the page "Week 2 and 3 - Product Specifications" (`4179219a-4691-8157-976e-dbc20a0a829f`).
  - The owner's older hub "TechFleet: AI Residency Resource Hub" (`4029219a-4691-8000-83bc-cfbd15b50c3c`) holds the working pages and the Kanban board `0579219a469182f1954401f71214631a`.
- **Course copies as files:** `Resources/Week_1/`, `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/`, `Resources/Week_4/` (27 files), `Resources/Week_5/` (7 files), `Resources/Course Hub (Notion copy 2026-11-13)/`.
- **Course map:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Course Map - live schedule, page list and copy status (2026-11-13).md`.
- **Skill:** `.claude/skills/residency-context/` (`SKILL.md`, `reference/course-map.md`, the week files, and the `week-N-submit-checklist.md` extracts).
- **Build plan draft:** `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` (195 lines, boxes 1 to 5, not committed). Sources: `caregiving-coordinator/docs/sources/build-plan-2026-11-12/`, logged in `docs/sources/INDEX.md`. Risk profile: `docs/risk-profile.md`.
- **FigJam:** board `HcDDdEGAnikTImO8v7UPMp`, section `3073:8029`. Lecture board: `mqryoCyR9mAw3v6kyDlmes`.
- **Git (2026-11-13, evening):** `origin/main` was at `dde942b` (PRs 50 and 51 merged) before this wrap-up. This report, the skill upgrade, the course map update, the two deleted duplicates and the `CLAUDE.md` rule are committed on a new branch in this wrap-up's pull request (find its number with `gh pr list --state all`).
  - **Left uncommitted on purpose** (the build plan deliverable): the build plan draft, `docs/sources/build-plan-2026-11-12/`, and the change to `docs/sources/INDEX.md`. Also not committed: `il.html` and `dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-13. Due dates come from the homework index and syllabus copies.
- **Checks run:**
  - PR 50 and PR 51 confirmed merged with `gh pr view`.
  - The Homework table copy matched the live scrape read the same day.
  - The Week 1 and Week 2 transcripts matched Notion word for word (16,865 and 8,016 words, 0 differences).
  - The skill folder: every renumbered file still contains its full original text; all 13 originals are in `_superseded-2026-10-28/`; every path `SKILL.md` names exists.
  - All 168 table-of-contents line numbers in the skill files match their headings, and every submit-checklist section is a word-for-word substring of its week file (script).
  - The two deleted lecture-notes files were compared first: they differed only in a link line and header lines.
  - The two empty Notion template pages were fetched on 2026-11-13.
  - Secrets scan on the files in PR 50: no keys or tokens.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - The lecture notes, other Weeks 1 to 3 pages, Syllabus and Weekly Lesson Space copies were retyped from the connector and not diffed word for word.
  - Weeks 6 to 9 skill files are old text, unverified against the live pages.
  - Whether the Premium paper was submitted, and whether it is complete.
  - The student page's claims; it was used only to find gaps.
  - Agent-browser's source code and known vulnerabilities.
  - The two prompts added to the reference hub were not tested on a fresh copy.
- **How this prevents drift:** the week renumbering is tied to a map file. Fixes and gaps are tagged Proposed. First step 2 stops for the owner before any edit. The reading rule and the end-of-answer "Read:" line make missed details visible.
