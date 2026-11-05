# Dog feeding report: Competitive Analysis 3, progress and mistakes (2026-11-04, before compacting)

**This is the newest dog feeding report.** Start the next session with it.

> "Read this report and the files in section 5. Tell me what you have and what's missing. Then we fix the grid cells so each one directly answers its question."

---

## 1. Where the competitive analysis stands

Working file: `caregiving-coordinator/docs/competitive-analysis-3.md`. Inputs file: `caregiving-coordinator/docs/competitive-analysis-3-inputs.md`.

| Step | Status | What it holds |
|---|---|---|
| 1. Problems to solve | Approved (option C) | 2 user problems and 2 business problems, sourced from the market analysis and audience page |
| 2. Problems to cover | Approved (option A) | Audience 1's top 7: exhaustion 138, dementia behavior 82, money and papers 74, medicines and hands-on care 62, the parent refuses help 60, relatives don't help 48, choosing a place 46 |
| 3. Competitors | **Second version approved** (the first was replaced) | 7, taken from the market analysis segments (see below) |
| 4. Criteria | **Second version approved** (the first, with 8 questions, was replaced) | 5 criteria from Audience 1's top needs (see below) |
| 5a, 5b (first round) | Kept only as evidence | Built for the old 15-competitor list |
| **Grid (7 × template columns + 5 criteria)** | **Drafted, NOT approved** | The owner rejected the cell wording twice (see section 3). `docs/sources/competitive-analysis-3/grid/build_grid.py` → `grid.json` |
| 3 takeaways, gaps and value opportunities | Not started | |
| Figma board | Steps 1 and 2 only (section 2645:12741) | Build the rest at the end (token plan) |

**The 7 competitors (step 3, second version):**
- **Direct:**
  - Caring Village (segment 1, coordination)
  - Everplans (segment 10, vaults)
  - Cariloop (segment 7, employer benefits)
  - A Place for Mom (segment 4, referral)
  - Geriatric care managers (no segment; they fill the gap for criteria 1 and 4)
- **Indirect:**
  - Group texts and notebooks (workaround)
  - Area Agencies on Aging (government program)
- **Trade-off the owner accepted:** no competitor for segment 12 (mental health and burnout).

**The 5 criteria (step 4, second version):**
1. Does it help the caregiver understand what's happening, handle hard behavior, and know what to do next?
2. Does it give the caregiver real relief: time, breaks, their own health?
3. Does it get the parent's money, papers and accounts under control?
4. Does it still work when the parent refuses help, and respect the parent's choices?
5. Does it get relatives to actually share the work?

**Business columns kept from the teacher's template:** type, segment, website, features, how they stand out, what they do well, what they don't do well, and who pays and the cost.

---

## 2. Evidence gathered (all saved, all checked by script)

- **Company pages:** `docs/sources/competitors-4/` (save script respects robots.txt). Blocked pages were read in the desktop app's built-in browser and saved in `manual-saves/`:
  - Trualta, Aging Life Care, Central Ohio AAA
  - MSU's Cariloop page ($249 a month)
  - the ACL caregiver program page
  - Cariloop's Google Play listing
- **Review sites:** `competitors-4/review-sites/`:
  - **BBB:** A Place for Mom has 272 reviews (3.95 stars) and 109 complaints in 3 years. Cariloop has 0 complaints and 0 reviews.
  - **Trustpilot:** Everplans has 1 review.
- **App reviews:** `app-reviews/reviews4.csv` (8 Everplans App Store reviews).
- **Caregiver posts:** `competitive-analysis-3/5b/` (207 Reddit and forum mentions read, 135 relevant, themes counted). Plus `segment-candidate-mentions.json`.
- **Prices:** Headspace and Medisafe official prices came through Firecrawl.
- **Grid sources:** checked by `build_grid.py` (91 cells, 131 sources, 0 problems). The *sources* are fine. The *wording* is the problem.
- **Not yet pulled:** A Place for Mom's roughly 1,169 Trustpilot reviews.
- **Truly thin:** Cariloop has almost no public reviews, because it's sold only to employers.

---

## 3. The mistakes, repeated today (and the rule for each)

| # | Mistake | Example | Rule |
|---|---|---|---|
| 1 | **Cells don't answer the question.** Tags, labels or fragments instead of an answer. | "Shows options and some prices." "Long waits, lowest priority, no timeline." | Read the column's question, then write the answer to it in one plain sentence. |
| 2 | **Cells use research or file words, not plain answers.** | "No caregiver evidence: 0 mentions in 49,315 posts." "(company claim)." "Too little caregiver evidence." | Never put method words in a cell. If data is thin, **get more data**. Labels like "company claim" go in the evidence file, not the cell. |
| 3 | **Cells mix two loose points with a semicolon, so they're not a clear answer.** | Everplans "don't do well": "Only works if the parent set it up first; the iPad app is phone-sized." | One clear finding per cell: the biggest, data-backed one, stated as what the company fails to do for the caregiver. |
| 4 | **The earlier deliverables didn't lead.** | Step 3 picked competitors from handy sources, not the market analysis segment table. | Start every step from the earlier deliverables' tables. Show an inputs table first. |
| 5 | **Too big instead of sharp.** | 15 competitors, 8 questions. | About 5 criteria from the audience's needs, and the competitors chosen from the market analysis (Fleety and the teacher's template). |
| 6 | **Different entities in one row, unlabeled.** | Eldercare Locator plus Area Agencies on Aging. | One entity per row, labeled business, nonprofit, government program or workaround. |
| 7 | **Not checking against the owner's examples before showing work.** | Cells didn't read like Competitive Analysis 2 or the 11-01 camps. | Compare with the owner's earlier table before every draft. |
| 8 | **Claimed something was checked when it wasn't fully.** | "Triple checked?" Only checked after being asked. | Run the checks before showing work, and say exactly what was checked. |

**What a correct cell looks like:**
- **Question:** "What do they not do well?" (for a caregiver)
- **Wrong:** "Only works if the parent set it up first; the iPad app is phone-sized."
- **Right (form):** "It can't help a caregiver whose parent never filled it in." Use one clear finding, and confirm it from the data (Competitive Analysis 2 says "Everplans needs the parent to set everything up ahead of time"; no caregiver use was found).
- **Criterion cells:** answer the "Does it…?" question first (Yes, Partly or No), then *why*, in the caregiver's terms. No hedges, no method words.

---

## 4. Next steps after the compact (one at a time, owner approves each)

1. **Rewrite every grid cell** (all 7 rows, the do well and don't do well columns, and the 5 criteria) as a direct, plain answer to its column's question, using the data. Fill any thin cell with more data (for example, more Cariloop sources, or A Place for Mom's Trustpilot reviews), not with "no evidence."
2. The owner approves the grid. Save it in `competitive-analysis-3.md`.
3. Write the 3 takeaways (where competitors fail the audience, and where the opening is), tied to the market opportunity verdicts.
4. Build the Figma section, commit, and write the starting brief for the feature analysis.

---

## 5. Files to give the next session

1. This report.
2. `caregiving-coordinator/docs/competitive-analysis-3-inputs.md` (market analysis and audience inputs, segments and companies).
3. `caregiving-coordinator/docs/competitive-analysis-3.md` (steps 1 to 4, approved).
4. `caregiving-coordinator/docs/sources/competitive-analysis-3/grid/build_grid.py` and `grid.json` (the current grid, its sources and its checker).
5. `caregiving-coordinator/docs/competitive-analysis-2.md` (the owner's example of good cells).
6. `caregiving-coordinator/docs/reports/competitive-analysis-3-change-report-2026-11-04.md`.
7. `caregiving-coordinator/CLAUDE.md`, with the rules "Earlier deliverables lead the next one" and "Dog feeding."

**Git:** commit f7c4c49 holds steps 1 to 5a. Everything after it is **not committed**: the step 3 and 4 second versions, the grid, the new review sources, the inputs file and the change report.
