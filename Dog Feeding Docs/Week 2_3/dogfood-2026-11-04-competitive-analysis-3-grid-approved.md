# Dog feeding report: Competitive Analysis 3, grid approved (2026-11-04, end of session)

**This is the newest dog feeding report.** Start the next session with it. It replaces `dogfood-2026-11-04-competitive-analysis-3-progress.md`, which is still useful for the history of mistakes.

> "Read this report and the files in section 6. Tell me what you have and what's missing. Then we write the 3 takeaways."

---

## 1. Where the competitive analysis stands

Working file: `caregiving-coordinator/docs/competitive-analysis-3.md`.

| Step | Status |
|---|---|
| 1. Problems to solve | Approved (option C) |
| 2. Problems to cover | Approved: Audience 1's top 7 |
| 3. Competitors | Approved (second version): 7 from the market analysis segments |
| 4. Criteria | Approved (second version): 5 from Audience 1's top needs |
| **5. Competitor grid** | **Approved and saved** as step 5 in `competitive-analysis-3.md` |
| 6. Three takeaways (gaps and value opportunities) | **Approved and saved** as step 6 (after this report was first written) |
| 7. Figma section, then the starting brief for the feature analysis | Not started. Figma has only steps 1 and 2 (section 2645:12741) |

**Git:** everything is committed and pushed. The latest commit is e56343e on branch `feature-analysis`.

---

## 2. The approved grid (short version)

**The 7 competitors:**
- Caring Village
- Everplans
- Cariloop
- A Place for Mom
- Geriatric care managers
- Group texts and notebooks
- Area Agencies on Aging

| Competitor | What they do well | What they don't do well |
|---|---|---|
| Caring Village | Shared calendar and medication list keep all siblings on the same care information. | Loses entries, resets the care plan, shows medical details to friends, and cannot get relatives to join. |
| Everplans | Gives adult children the parent's accounts, insurance policies and end-of-life wishes in one place. | Useless unless the parent filled it in. The iPad app runs only at phone size. |
| Cariloop | Assigns a full-time care coach who guides families through a crisis. | Available only through employers with 100 or more workers. The app freezes. |
| A Place for Mom | Lists nearby senior living options with prices and books tours. | Shares families' contact details, causing nonstop sales calls. Commission-paid advisors know little about the places. |
| Geriatric care managers | Attend doctor visits, evaluate care facilities and arrange respite during a crisis. | Cost $150 to $300 an hour, offer unclear services, and sometimes never make the agreed care plan. |
| Group texts and notebooks | Reach every relative instantly for free. A whiteboard schedule reduces a parent's repeated questions. | Help requests get ignored or just a "like." Notes and calendars get lost or erased. |
| Area Agencies on Aging | Connect families to free local services, support groups and Medicare counseling. Some fund respite. | Mostly referrals, long waitlists, hard-to-reach staff and strict eligibility. |

**What the 5 criteria show (Yes / Partly / No):**

| Criterion | Yes | Partly | No |
|---|---|---|---|
| 1. Understand, handle behavior, know what to do | Cariloop, care managers | Caring Village, A Place for Mom, group texts, Area Agencies | Everplans |
| 2. Real relief for the caregiver | Care managers (for a price) | Caring Village, Cariloop, A Place for Mom, Area Agencies | Everplans, group texts |
| 3. Money, papers, accounts | Everplans (if the parent fills it in), Cariloop | Caring Village, A Place for Mom, care managers, group texts, Area Agencies | none |
| 4. Works when the parent refuses help | none | Cariloop, care managers, group texts | Caring Village, Everplans, A Place for Mom, Area Agencies |
| 5. Relatives share the work | none | Caring Village, Everplans, Cariloop, care managers, group texts | A Place for Mom, Area Agencies |

**What this points to for the takeaways (to discuss, not decided):**
- Nobody fully solves criteria 4 (a parent who refuses help) or 5 (relatives sharing the work).
- The options that do help (Cariloop, care managers) are locked behind an employer or cost $150 to $300 an hour. That clashes with the audience's money facts: only 12% would pay out of pocket, and willing payers cap near $70 a month.

---

## 3. What happened this session

1. Read the earlier progress report, committed (fd9b06d) and pushed.
2. Got more data for the thin rows:
   - **Everplans:** 5 Reddit threads from the Arctic Shift archive.
   - **Cariloop:** 1 Reddit thread and the full Google Play page.
   - **Blocked or refused:** Reddit is blocked in both Firecrawl and the built-in browser. The archive also refused most wide word searches (HTTP 422 and 429), so Cariloop stays thin: it's sold only to employers.
3. Rewrote the grid as **version 2** (`build_grid_v2.py` → `grid-v2.json`). Version 1 is kept.
4. The owner rejected the "do well" and "don't do well" cells 3 more times:
   - **Draft 1:** too vague (lists like "easy to use").
   - **Draft 2:** too wordy (full sentences with filler like "quickly gives overwhelmed families...").
   - **Draft 3:** approved. The answer first, no company name, no filler, concrete examples.
5. Wrote the cell-writing rules into `CLAUDE.md`, `TABLE-RULES.md` and memory.
6. Saved the grid in `competitive-analysis-3.md`, committed (e56343e) and pushed.

---

## 4. The rule for writing table cells (now in CLAUDE.md)

"How to answer a table question from data": every cell must pass all 7.

1. Answer the column's question in the first word. Don't repeat the row's name.
2. No filler words ("quickly", "overwhelmed", "for them").
3. Concrete examples from the data, several when the data has several. No vague words like "easy to use."
4. No quotes, counts, IDs or research words in the cell.
5. No fragments, and no long sentences. Two short sentences at most.
6. Thin data means getting more data, never a cell saying it's thin.
7. Yes / Partly / No questions start with that word, then the facts.

**Approved examples:**
- "Lists nearby senior living options with prices and books tours."
- "Shares families' contact details, causing nonstop sales calls. Commission-paid advisors know little about the places."

---

## 5. Next steps (one at a time, the owner approves each)

1. **Three takeaways:**
   - Where competitors fail the audience, and where the opening is.
   - Tie them to the market opportunity verdicts in `competitive-analysis-3-inputs.md`:
     - Segment 10 (vaults) is the strongest unmet need.
     - Segment 12 (burnout) is the biggest need, but crowded.
   - Write them with the 7 cell rules.
2. Save the takeaways in `competitive-analysis-3.md`, then commit.
3. Build the Figma section (steps 3 to 6) next to section 2645:12741.
4. Write the starting brief for the feature analysis.

**Open research: who pays (agreed 2026-11-04, from step 1 business problem 4)**

- **When:** after the feature analysis, before positioning. It's new research, so it updates the market analysis first.
- **Why:** positioning and the value proposition depend on who the customer is: families, employers or Medicare.
- **What we already know:**
  - Families: only 12% would pay out of pocket, and willing payers cap near $70 a month (CAN 2026, Schulz 2016).
  - Employers pay for Cariloop (segment 7).
  - Senior living places pay A Place for Mom when a family moves in.
  - Grants fund Area Agencies on Aging.
  - Medicare and Medicaid usually don't pay for care managers.
- **Research needed:**
  1. **Employers:** do they buy caregiver benefits, which employers, and what do they pay per employee? (Cariloop's $249 a month at MSU is the only price so far.)
  2. **Medicare and government programs:** what Medicare GUIDE pays for dementia care help, who can bill it, and whether it covers family caregiver support. It's named in `docs/exhaustion-dementia-research.md` but not researched yet. Also check other public programs that pay for caregiver support.
  3. **Families:** confirm the 12% and $70-a-month figures, and what families pay today for the alternatives.
- **Rules:** read full primary sources, cite with a link and a page number, save copies in `docs/sources/` with entries in `INDEX.md`.

**Still open from earlier (the owner's call):**
- Keep or remove the Feature Analysis 3 gaps-report rewrite.
- Remove the duplicate audience section 2061:543 in FigJam Q5jRpN3MbONqFQF6KTS70j.

---

## 6. Files to give the next session

1. This report.
2. `caregiving-coordinator/docs/competitive-analysis-3.md` (steps 1 to 5, approved).
3. `caregiving-coordinator/docs/competitive-analysis-3-inputs.md` (market analysis and audience inputs, the opportunity verdicts).
4. `caregiving-coordinator/docs/sources/competitive-analysis-3/grid/build_grid_v2.py` and `grid-v2.json` (the grid and its sources).
5. `caregiving-coordinator/CLAUDE.md` (the rules "How to answer a table question from data", "Earlier deliverables lead the next one" and "Dog feeding").
6. `Dog Feeding Docs/Week 2_3/dogfood-2026-11-04-competitive-analysis-3-progress.md` (the earlier mistake list).
