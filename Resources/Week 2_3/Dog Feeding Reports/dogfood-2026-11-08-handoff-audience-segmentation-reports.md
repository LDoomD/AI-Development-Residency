# Handoff: Caregiving Coordinator → audience segmentation reference reports (2026-11-08)

Replaces: none. It sits beside `dogfood-2026-11-07-handoff-feature-comparison-analysis.md`, which still holds the feature comparison plan and the audience, market and competitive outcomes.

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what the audience segmentation reference reports start from. Then ask me for the first audience segmentation table as a CSV and wait. Keep replies short, plain, and one thing at a time. Confirm every change against the saved research and original sources before making it."

## 0. Start here
- **Where we are:** the owner is building a reference report for each finished deliverable, so any new session can start from them. The market analysis is done: four reference reports (one per data table) and a master report. Audience segmentation is next, then competitive analysis. The feature comparison analysis waits until those reports exist (owner, 2026-11-08).
- **The outcome so far, in one sentence:** the market analysis points to helping worn-out caregivers reach relief, in respite and adult day services (segment 11) and caregiver mental health (segment 12) (`Market Analysis - Master Report (all 4 tables).md`, section 9).
- **Next milestone:** reference reports for the audience segmentation tables, one table at a time, in the same 9-section layout as the market analysis reports.

## 1. Locked outcomes
- **Opportunity: helping worn-out caregivers reach relief, segments 11 and 12.** **Approved** 2026-11-05 (`dogfood-2026-11-07-handoff-feature-comparison-analysis.md`, section 1).
- **Report layout for each table:** the same 9 sections as `Market Analysis Research - Reference Report - 1 of 4.md`: purpose, Discovery link, columns, every row and cell, most important things, patterns (with the check against earlier tables inside), what is missing, where it points, verification receipt. **Approved** 2026-11-08 (the owner asked that report 4 follow reports 1 to 3).
- **The four reference reports and the master report are written.** **Proposed**: the owner has not reviewed them. Folder: `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Reference Reports_Market Analysis/`.
- **9 cells in the owner's tables were changed on 2026-11-08 at the owner's request** (listed in section 2). **Approved.**
- **Figma was not updated.** **Approved** (owner, 2026-11-08: skip it if it cannot be done at 100% without an audit). The Figma tables still have the old wording in those 9 cells (see the table in section 2, `Data Tables_Market Analysis/`).
- **Rule from this session:** confirm every change against all saved research and the original sources before editing, never after. **Approved** (owner, 2026-11-08; saved as memory `confirm-before-changing`).

## 2. Key findings and data

**What the market analysis shows** (all from the master report and the four CSV tables in `Data Tables_Market Analysis/`):

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Burnout is the top caregiver problem | 210 of 412 Reddit posts (51.0%); 55 of 141 forum threads (39.0%) | `Market Opportunity.csv` row 11; `docs/community-voice-findings.md` theme table | Credible secondary |
| Respite posts, all outcomes | 341 = 128 used + 78 couldn't get it + 81 looking + 18 tried and stopped + 32 mentioned only + 4 recommends | `docs/sources/market-analysis-3/segments-11-12/results.json`, recounted 2026-11-08 | Credible secondary |
| Market sizes | Respite $19.3B global ($7.6bn US); mental health apps $7.48B to $8.2B | `Market Size.csv` rows 13 and 14; IBISWorld saved page | Estimate (global, not caregiver-only) |
| Evidence ratings for the 16 sized rows | Low 8, Medium 7, High 1 (the High row is password managers, not caregiver-specific) | `Market Size.csv`, Evidence column | Credible secondary |
| Segments judged | Not open 3, Crowded 3, Different customer 2, hard to enter 2, others 4 | `Market Opportunity.csv`, Verdict column | Credible secondary |

**The 9 cells changed on 2026-11-08** (each confirmed first against saved research or the original page):

| Table and cell | Old | New | Confirmed against |
|---|---|---|---|
| Market Size, Caregiver App Market, Notes | (5 firms) | (4 firms) | 5 publishers' pages (`docs/market-research-prompt2-results.md` table; saved Wise Guy and VMR pages; live pages of 3 others) |
| Market Size, Elderly Care row, Notes | "more than 100 times" | "about 1,600 times" | Mordor $1.20B (saved page), Prophecy $1,916.3B (live page) |
| Market Size, Patient Portal row, Notes | Most estimates $5.2B to $6.6B, growth 10.9% to 18.4% | Estimates $4.4B to $7.0B, growth 10.9% to 19.55% | Live pages (source: each firm's own report page): Grand View $4.4B, SNS $4.79B, Data Bridge $6.43B, Reports and Data $6.48B, Market Research Future $7.02B |
| Market Size, Patient Portal row, Evidence | Medium: most firms agree | Medium: five firms within about 1.6 times of each other | Recomputed from the five portal pages above (`Market Size.csv` row 9): $7.02B / $4.4B = 1.6 |
| Market Analysis Research, Patient portals row, Notes | same as the portal Notes change | same | same |
| Market Opportunity row 4, What caregivers say | "The biggest worry in the forums..." | "Burnout is bigger on both Reddit (210 of 412) and the forums (55 of 141)" | `docs/community-voice-findings.md` (55 vs 38 of 141) |
| Market Opportunity row 8, Few competitors? | Kin is free, 43 of 46 five-star, several indie launches | Kin has 1,120 Apple ratings, $9M seed May 2026, four newer apps named | Table 1 and `docs/market-research-template-run.md`. The removed claims had no source |
| Market Opportunity row 9, Big enough? | $3.9B to $6.6B | $4.4B to $7.0B | The five portal pages listed in the row above (source: `Market Opportunity.csv` row 9 and the firms' report pages) |
| Market Opportunity row 11, Unmet need? | 128 + 78 + 81 of 341 | all six groups listed | `results.json` recount and `verify_codes.py` (passes) |

**Errors and conflicts found, and their status** (source for all: `Reference Reports_Market Analysis/Market Analysis - Master Report (all 4 tables).md`, section 7, and this session's checks)

| # | What was found | Where | Status |
|---|---|---|---|
| 1 | Firm count differed: "(5 firms)" vs "(4 firms)" | `Market Size.csv` Caregiver App row vs `Market Analysis Research.csv` row 1 | **Fixed** (now 4). Both were right: five publishers in all, Wise Guy is the headline |
| 2 | Digital legacy shows $25B, the top of a $1.1B to $25B range | `Market Size.csv` Digital Legacy row | **Left.** Kenresearch's saved page does state $25B (2025), 13.8% to $54B (2031). Owner's choice |
| 3 | Two dollar figures not in other tables: $0.8B (row 3) and $3.9B (row 9) | `Market Opportunity.csv` rows 3 and 9 | **$0.8B confirmed** (Global Industry Analysts $844.2M, 2023, press release). **$3.9B not confirmed** (Market Research Future now says $7.02B), so row 9 was changed |
| 4 | "Biggest worry in the forums" was choosing care, but burnout is larger | `Market Opportunity.csv` row 4 vs row 11 | **Fixed** |
| 5 | Respite counts added to 287 but the row said 341 | `Market Opportunity.csv` row 11 | **Fixed** (all six groups listed, they sum to 341) |
| 6 | "Medium" means a size in table 4 and a trust level in table 3 | Tables 3 and 4 | **Left.** Wording only |
| 7 | Table 4 drops table 3's Evidence ratings | Table 4 | **Left.** Possible choice to keep it short |
| 8 | Elder care and segment 15 handled differently across tables | Tables 1 to 4 | **Left.** Possible scope choice |
| 9 | "More than 100 times" understates the elder care gap | `Market Size.csv` Elderly Care row | **Fixed** (about 1,600 times) |
| 10 | My report 3 listed the wrong rows for US-only sizes | `Market Size - Reference Report - 3 of 4.md`, gaps table | **Fixed** |
| 11 | Respite row mixes two samples: the 412 random Reddit sample and a separate targeted set of 831 relief posts | `Market Opportunity.csv` row 11 | **Noted.** Not an error |
| 12 | Kin's "free" and "43 of 46 five-star" had no source | `Market Opportunity.csv` row 8 | **Removed** |
| 13 | Patient portal estimates have moved since the saved research | Tables 1, 3, 4 | **Fixed** (all say $4.4B to $7.0B) |
| 14 | Portal Evidence said "most firms agree," but the spread is now 1.6 times | `Market Size.csv` Patient Portal row | **Fixed** |
| 15 | Four stated growth rates differ from their own size and forecast by 0.5 to 1.0 points | Family organizers, mental health (Grand View), digital vaults, telehealth (IMARC) | **Not errors.** The firms' own pages state those rates |
| 16 | The saved research cites a wrong link for Global Industry Analysts' $844.2M (it points to a different report, $1.13B in 2024) | `docs/market-research-prompt2-results.md` line 174 | **Not fixed** (see still-to-do) |
| 17 | My own process slips: edited three cells before confirming; ran extra research unasked; my first CSV edit changed line endings; one wording had a comma that split a row | This session | **All fixed or undone** and turned into working rules (section 7) |

## 3. Excluded and deferred
- **Figma update for the 9 cells above.** Skipped by the owner. It comes back only if the owner wants it and can audit it. Do not edit the owner's Figma tables unasked.
- **Left as they are, the owner's call:** "Medium" means a size in table 4 and a trust level in table 3; table 4 drops table 3's evidence ratings; elder care and segment 15 are handled differently across tables.
- **Not confirmed:** the four newer visit-notes apps (AlignCare, Neatly, VisitNotes, Hoy) against the app stores; the $3.9B portal figure (it was replaced, not confirmed); Kin's "free" and "43 of 46" claims (removed).
- **Not started:** reference reports for audience segmentation and competitive analysis; the feature comparison table (plan in the 2026-11-07 handoff).
- **Not used:** NotebookLM for research; INVEST for analysis work.

## 4. Open decisions
The next session must not decide these alone.
- **Whether to update Figma** (the 9 cells) and who audits it.
- **Where the audience segmentation reference reports are saved.** Do not create folders unasked.
- **Whether to merge the pull request** for this work. The owner merges it.
- **Still open from earlier handoffs:** who pays for relief; the Week 2 due date; the instructor repo invite; `CLAUDE.md` still points to the old `Dog Feeding Docs/` folder.

**Still to do (not decisions):**
1. Update the 9 changed cells in Figma, only if the owner wants it and can audit it.
2. The owner reviews and merges the pull request for this work.
3. Write the audience segmentation reference reports, one table at a time (next).
4. Then the competitive analysis reference reports.
5. Then the feature comparison table (plan in the 2026-11-07 handoff).
6. Fix the wrong Global Industry Analysts link in `docs/market-research-prompt2-results.md` line 174 (the figure is right; the link points to a different report).
7. Check the four newer visit-notes apps (AlignCare, Neatly, VisitNotes, Hoy) against the app stores.
8. Reconcile "412 Reddit posts" with the earlier Reddit pass recorded in memory as 825 posts (not reconciled).
9. Update `CLAUDE.md` so it points to the `Resources/` folders instead of `Dog Feeding Docs/`.
10. Compare the CSV tables with their PNG versions (not done).

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The four market tables have no split by Audience 1 (adult child) and Audience 2 (spouse) | The audience segmentation reports | That split is the first thing the audience tables should supply |
| Burnout as the top theme, and the respite barriers (cost, a parent who says no, paperwork, family who won't help) | The audience problems and use cases | They should match the audience tables' top problems |
| The 4-step method (read every cell, check against earlier tables, cross-check numbers by script, list what is missing) | Each new reference report | It kept the market analysis reports accurate |
| The master report layout | An audience master report, later | Same sections, same receipt |

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr list --state open`. If this work's pull request is still open, say one line and ask: merge it first, or keep going? Do not offer INVEST.
2. **Ask the owner for the first audience segmentation table as a CSV** (CSV reads exactly; the PNG does not). Wait.
3. **Read it in full.** Check it against the market tables and `docs/clean-deliverables/audience-review-2026-11-05.md`. Search all saved research on the topic first (`docs/`) and say which files were used.
4. **Write the reference report** in the 9-section layout. Run a script that matches every CSV cell to the report. Do not edit any table or report without confirming first.
5. **Stop and wait** after each table. When all audience tables are done, ask whether to write an audience master report.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. Most likely to be broken next:
- **Confirm before changing.** Saved research and the original source first, then edit. If it cannot be confirmed, say so and leave it.
- **Answer the question asked.** Do not start research, searches or edits the owner did not ask for. Short replies, plain words, one thing at a time.
- **Keep CSV files intact:** open with `newline=""` so line endings do not change, and put no commas in unquoted cells (a comma split a row on 2026-11-08).
- **Say which file or cell every answer came from.** Never claim a table is read until it is.
- **The owner merges their own pull requests.** One deliverable, one branch, one pull request. Never run `gh pr merge`.
- **Never write the owner's homework summary.**

## 8. Where things live
- **Owner's tables (CSV):** `/Users/landodoom/Desktop/AI Developer Residency /Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Data Tables_Market Analysis/` (`Market Analysis Research.csv`, `Possible Market Segments.csv`, `Market Size.csv`, `Market Opportunity.csv`).
- **Reference reports and master:** `.../Week 2 & 3_Course Overview_Docs/Reference Reports_Market Analysis/` (four reports "1 of 4" to "4 of 4", and `Market Analysis - Master Report (all 4 tables).md`).
- **Saved research used for checks:** `caregiving-coordinator/docs/` (`market-research-prompt2-results.md`, `community-voice-findings.md`, `market-analysis-3.md`, `market-analysis-segments-11-12-findings.md`, `market-research-template-run.md`, `sources/market-analysis-3/segments-11-12/results.json`, `sources/market-reports/`).
- **Earlier handoff:** `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-07-handoff-feature-comparison-analysis.md`.
- **Memory:** `/Users/landodoom/.claude/projects/-Users-landodoom-Desktop-AI-Developer-Residency-/memory/` (new: `confirm-before-changing.md`).
- **Git (2026-11-08):** the work is on a new branch cut from the latest `main`, with a pull request for the owner to merge. Left out on purpose: `docs/sources/competitive-analysis-4/live-pages/raw/il.html` (holds a map token GitHub blocks) and a stray `.textClipping` file.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2 name a file for each item. Approvals are from this chat on 2026-11-08 and from the 2026-11-07 handoff.
- **Checks run:**
  - Scripts matched every table cell to its report: 208 of 208, 90 of 90, 144 of 144, 84 of 84, none missing, after all edits.
  - A diff against backups showed only the intended lines changed in each CSV.
  - 132 numbers in the master report were looked up in the tables, reports and saved research: none missing.
  - Respite counts were recounted independently from the saved codes (they match `results.json`) and `verify_codes.py` passed.
  - Forum theme counts were recounted from the saved per-thread tags: they reproduce the saved table, except one extra thread (142 vs 141) that moves choosing care by one.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - Figma after the edits (it was not changed).
  - The four newer visit-notes apps against the app stores.
  - The CSVs against the PNG versions of the tables.
  - Most research firms' own pages beyond those listed in section 2.
  - The Reddit and forum posts themselves (counts were read from saved results).
- **How this prevents drift:** decisions are tagged Approved or Proposed, the changed cells and their evidence are listed, exclusions are named, and step 2 stops for the owner before any reading.
