# Dog feeding report: audit and corrections (2026-11-05)

**This is the newest dog feeding report. Start the next session with it.** It replaces `dogfood-2026-11-04-end-of-day.md` (still useful as history).

> Paste to start: "Read this report, then the files in section 8. Tell me what you have and what's missing. Then fill in docs/research-checklist.md for the next step and show it to me before doing anything."

---

## 1. Rules to follow (read first)

1. **Rule #1: every deliverable is part of one project.** Market analysis, audience segmentation, competitive analysis, feature analysis, positioning and vision boards build on each other. No research, reading pass or new table starts until `caregiving-coordinator/docs/research-checklist.md` is filled in and shown to the owner. Every research pass splits by the two audiences:
   - Audience 1 = adult child caring for a parent
   - Audience 2 = spouse or partner
2. **Write for the owner (new today).** Every output uses UX writing best practices at an 8th-grade reading level: what it means first, then the number; full sentences; caregiver words, not research jargon. Test: would the owner understand it on first read?
3. **Questions get answers, not edits.** Change files only after a clear yes.
4. **Never delete or overwrite old versions.** Make a corrected version and put a big yellow banner on the old one.
5. **Homework order (decided today):** the owner is doing the full Week 2 **bonus** work, in the order of the 6 Week 2 deliverable templates:
   1. Audience segmentation, business goals, use cases
   2. **Market, competitive and feature analysis, then unique positioning (we are here)**
   3. Release vision and scope
   4. Epics, features and tasks
   5. Notion Kanban board
   6. Pitch deck
   Don't reopen this.
6. **Read deliverables from the newest versions only.** The Figma board is newer than the repo copies of the market tables. Yesterday's errors came from reading old repo copies.

All of these are in `caregiving-coordinator/CLAUDE.md` and memory.

---

## 2. What happened today, in order

1. **Read the homework.** A subagent read the full Week 2 lecture transcript and the saved course pages.
   - **Feature analysis:** features you choose; check marks for has / doesn't have; an "our company" column; find what's unique; double-check AI work.
   - **Positioning:** five questions (who, what problems, which competitors, what impact, how it's different), built from the gaps, with one positioning statement per audience.
   - **Vision boards:** one per audience per release.
   - Not read yet: the Week 2-3 slides on NotebookLM (they need the owner's Google sign-in).
2. **Skeptical audit of yesterday's report:** `caregiving-coordinator/docs/reports/skeptical-audit-2026-11-05.md`.
3. **Inventory of what was and wasn't updated last night,** checked against git, the session logs and the board: `docs/reports/update-inventory-2026-11-05.md`.
   - **Main finding:** segments 11 and 12 were already sized and listed on the board before 2026-11-04. Yesterday's claim that they "had never been researched" was wrong; it came from older repo copies.
4. **First fixes:** "70% of working-age caregivers"; the unconfirmed "strongest unmet need" ranking removed (it was my reading, never the owner's decision); outdated segment 12 notes; a misleading audience note.
5. **6-agent independent audit** (checklist: `docs/research-checklist-audit-2026-11-05.md`; results: `docs/reports/audit-2026-11-05-results.md`). **The data holds up:**
   - A second reader re-read 50 posts without seeing the first answers: agreed 49 of 50 on whether a post counts, 49 of 49 on "needs a break, no help," and 44 of 49 on what happened.
   - Of 40 posts left out as not relevant, 37 were right to leave out.
   - The audience labels agreed 39 of 40 (plus 38 of 40 in the earlier check).
6. **The audit found real problems.** All were reviewed with the owner in plain words and fixed:
   - "Family won't help" was overcounted (93 → **83**) because of a sorting rule. The rule is fixed in the script.
   - Provider counts were too low. **Medicaid is named most**, not the VA.
   - Several verdicts and audience differences were stated too strongly.
   - A wrong page number (the 59% stress figure is on printed page 52, Figure 12).
   - The respite row's "No" on guidance was contradicted by its own source.
   - The VA row was missing its main limit (a 70% or higher disability rating).
   - Gap 2 left out Medicare GUIDE.
7. **Main market analysis table:** a new column was added for respite and burnout support, "what caregivers say about getting a break."

---

## 3. Where each deliverable is now (use these, not older versions)

Figma file: https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/

| Deliverable | Current version on the board | Current repo copy | Older versions (marked) |
|---|---|---|---|
| Market analysis | Main tables in [2598:10950](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2598-10950), plus **[CORRECTED 2026-11-05 — Segments 11 and 12 (2767:13680)](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2767-13680)**. The main table [2598:11951](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2598-11951) has the new column. | `docs/market-analysis-3.md`, section "CORRECTED 2026-11-05" at the end | 2704:13380 (yellow SUPERSEDED banner); Market Opportunity 3rd Version 2598:11148 (yellow PARTLY SUPERSEDED banner on rows 11-12 and the answer). The repo files `possible-market-segments-table.md`, `market-opportunity.md` and `market-size-table.md` are marked "older than the board." |
| Audience segmentation | Teacher format [2623:76](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2623-76), plus **[CORRECTED 2026-11-05 — Exhaustion and getting a break (2772:1657)](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2772-1657)** | `docs/audience-segmentation.md` and `docs/audience-teacher-format-2026-11-04.md`, "CORRECTED 2026-11-05" sections at the end | 2704:15080 (yellow SUPERSEDED banner) |
| Competitive analysis | **[Competitive Analysis 3 (2645:12741)](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2645-12741)**, corrected in place today (the subtitle notes what changed) | `docs/competitive-analysis-3-reader-v2.md`; cells from `docs/sources/competitive-analysis-3/grid/build_grid_v4.py` (0 problems) | `competitive-analysis-3.md` and `competitive-analysis-3-reader.md` are marked superseded |
| Feature analysis | Feature Analysis 3, 2584:10359: **out of date** (built on the old competitors) | `docs/feature-analysis-3.md` | |

---

## 4. What the research says now (corrected numbers)

**Words used:**
- **Respite:** a short break for the caregiver while someone else takes over the care.
- **Adult day center:** a place where the parent spends the day with staff and activities.

1. **Exhaustion is the #1 caregiver problem** for both audiences.
2. **Help exists, but many caregivers can't get it.**
   - 39% of caregivers say a break would help, but only 13% have ever used respite (AARP/NAC 2025, PDF pp.26-27).
   - Of 341 caregiver posts about respite, 128 got a break, 78 couldn't get one and 81 were still trying.
   - About 1 in 4 caregivers in both audiences need a break and have no help.
3. **What stops them** (posts out of 831):
   - the cost: 118
   - the parent saying no: 96
   - paperwork and rules to qualify: 86
   - family who won't step in: 83
   - waitlists: 59
   - too few trained workers: 38
4. **By audience:**
   - Adult children are blocked most by cost and the parent saying no.
   - Spouses' top blockers are paperwork and rules (sometimes the VA), family and cost. Spouse numbers are small (98 posts).
   - Spouses use support groups more (22% vs 12% of posts).
5. **Programs caregivers name most:** Medicaid and waivers (77 posts), hospice (45), the VA (44), Area Agencies on Aging and local aging offices (26).
6. **Burnout and meditation apps almost never come up.** Caregivers get support from therapists, support groups and online caregiver groups.
7. **Who pays for relief:** families pay about as often as public programs do. Only 12% of caregivers would pay out of pocket, and willing payers cap near $70 a month.
8. **The 4 gaps** (Competitive Analysis 3):
   1. No one handles a parent who refuses help or gets relatives to share the work.
   2. Personal, ongoing guidance is mostly locked behind an employer (Cariloop) or a $150-an-hour bill (care managers). Free and public help is limited: Medicare GUIDE covers only dementia, the VA only veterans, and the helpline gives free advice.
   3. Help with money and accounts works only if the parent prepared ahead of time (132 posts about getting into a parent's accounts).
   4. Relief exists, but caregivers can't reach it.

**Limits:** people who post online are often having a hard time, so these show patterns, not national rates. Each post was coded by one reader; the second-reader check agreed on most points, less on the exact reasons.

---

## 5. Mistakes made today, and the rule for each

| Mistake | Rule now |
|---|---|
| Used older repo copies instead of the newer Figma board | Read deliverables from the newest board versions; the old repo copies are now marked |
| Stated my own reading ("strongest unmet need") as if it were a decision | Never present Claude's reading as a finding; the owner decides |
| A sorting rule overcounted "family won't help" | Any free-text grouping rule is checked by a second reader before numbers are published |
| Wrote in research jargon ("access, not supply," "keyword rule") | Write for the owner: 8th-grade, meaning first |
| Mixed PDF and printed page numbers | Cite as "PDF p.X" (or say "printed page X"), checked in the saved file |
| A script rewrote an older data file as a side effect (`grid-v3.json`) | Restored from git; new scripts write new files only |

---

## 6. Next steps, in order (one at a time, the owner approves each)

1. **Commit today's work.** Nothing from today is committed yet (see section 9).
2. **Two leftover VA claims** (each based on one post), waiting for the owner's yes:
   - The money and papers cell: "Approval can take months" → "Approval can be slow."
   - The customer experience cell: "Some calls go unanswered" → "One caregiver's calls went unanswered."
3. **Clean tables for one new Figma page.** Once the fixes are done, make simple tables with only the correct, current data for the audience segmentation, market analysis and competitive analysis. The owner builds one new Figma page from them, and from then on Claude reads deliverables only from that page. Ask first whether the owner wants markdown, CSV or Figma.
4. **Feature analysis: full audit and rebuild** from the corrected audience, market and competitive analyses (9 competitors, 4 gaps, exhaustion and relief, both audiences). The current feature list covers coordination only, with nothing for finding respite, qualifying for programs, a refusing parent or relatives covering breaks. Fill in the research checklist first.
5. **Unique value proposition and positioning:** five questions, one positioning statement per audience.
6. Then deliverable #3: release vision and scope.

**Still open, the owner's call:**
- Professional title rewrite for the competitive analysis: proposed 2026-11-04, never approved.
- Who-pays research: employers, Medicare GUIDE, families.
- Remove the duplicate audience section 2061:543 in FigJam Q5jRpN3MbONqFQF6KTS70j.
- Keep or remove the unrequested Feature Analysis 3 gaps-report rewrite.
- The Week 2-3 slides (NotebookLM): the owner signs in to the built-in browser, or exports a PDF.

---

## 7. Numbers to trust and where they come from

| Number | Source |
|---|---|
| 39% would like respite, 13% have ever used it | AARP/NAC 2025, PDF pp.26-27 (`docs/sources/aarp-nac-caregiving-in-the-us-2025/`) |
| Managing stress is the top help topic, 30% | AARP PDF p.53 |
| 59% of dementia caregivers report high stress | Alzheimer's Association 2026, Figure 12, printed p.52 (PDF p.54) |
| 831 relief posts; 486 adult children, 98 spouses | `docs/sources/market-analysis-3/segments-11-12/results-by-audience.json` |
| Barrier and provider counts | `results.json` (recounted 2026-11-05) |
| 70% of working-age caregivers have jobs (60% of all) | AARP PDF p.39 and p.38 |

---

## 8. Files to give the next session

1. This report.
2. `caregiving-coordinator/CLAUDE.md`.
3. `caregiving-coordinator/docs/research-checklist.md`.
4. `caregiving-coordinator/docs/reports/audit-2026-11-05-results.md` (what was wrong and fixed).
5. `caregiving-coordinator/docs/market-analysis-3.md` (the "CORRECTED 2026-11-05" section at the end).
6. `caregiving-coordinator/docs/audience-segmentation.md` and `docs/audience-teacher-format-2026-11-04.md` ("CORRECTED 2026-11-05" sections).
7. `caregiving-coordinator/docs/competitive-analysis-3-reader-v2.md`.
8. `caregiving-coordinator/docs/feature-analysis-3.md` (to audit next).
9. `caregiving-coordinator/docs/sources/INDEX.md`.

---

## 9. Git

Branch `feature-analysis`, open PR LDoomD/AI-Development-Residency#23. The last commit is 692d180 (2026-11-04). **Everything from 2026-11-05 is uncommitted:**
- the corrected sections in the market, audience and competitive files
- the audit folder and reports
- `build_grid_v4.py`, `grid-v4.json`, `business-v3.json`
- the fixed `count_results.py` and its outputs
- `CLAUDE.md`
- this report
