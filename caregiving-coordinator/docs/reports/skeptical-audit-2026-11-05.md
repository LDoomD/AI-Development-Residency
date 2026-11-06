# Skeptical audit of discovery, start of 2026-11-05

Scope: the end-of-day report (`Dog Feeding Docs/Week 2_3/dogfood-2026-11-04-end-of-day.md`), memory, the current audience segmentation, market analysis and competitive analysis, checked against the Week 2-3 course materials. Method: the `skeptical-audit` skill. Every claim is tagged with how it is known.

Evidence states:
- **observed:** checked this session
- **documented:** read in a saved primary source
- **inferred:** reasoned from observed facts
- **reported:** stated earlier, not rechecked

## 1. Checks rerun this session

| Check | Result | State |
|---|---|---|
| Grid version 3 and business table version 2 (`build_grid_v3.py`) | Grid 117 cells and 214 sources; business 45 cells and 82 sources; 0 problems | observed |
| Relief reader codes (`verify_codes.py`) | 11 packs, every quote exact, every item coded once: OK | observed |
| Audience labels (`verify_audience.py`) | 5 packs: OK | observed |
| Recount by audience (`count_by_audience.py`) | Same numbers as the report: 831 relevant, 486 adult children, 98 spouses, 38 of 40 spot-check agree | observed |
| AARP 39% vs 13% respite | Found word for word in the saved report: "Although 39 percent of caregivers say respite would be helpful, only 13 percent use it" (`docs/sources/aarp-nac-caregiving-in-the-us-2025/full-report.paged.txt`) | observed |
| Git | Clean. Last commit 692d180 on `feature-analysis`. | observed |
| Rerunning `count_results.py` | Same counts, but tied barriers come out in a different order, so the file shows as changed. Restored from git. | observed |

## 2. Claims from the report, tagged

| Claim | State | Source | Limit or correction |
|---|---|---|---|
| Exhaustion is the #1 problem: 138 adult-child posts, 45 spouse posts | documented | `docs/audience-teacher-format-2026-11-04.md` | Counts from 412 posts and threads (forums plus Reddit) |
| "51% of the Reddit random sample" | observed | `docs/market-analysis-3.md` | **Wording fix:** 51% *mention* it; 25% have it as the *main* topic |
| Respite: 341 posts, 128 used, 78 couldn't get it, 81 looking | observed | `results.json` (rerun) | Posts, not caregivers' national rates. Respite types are combined because readers labeled them differently. |
| 26% need a break with no help (adult children 25%, spouses 30%) | observed | `results-by-audience.json` | Spouse base is 98 posts |
| Barrier shares by audience (cost 16%, parent refuses 15%, and so on) | observed | Same | Each post was coded by **one** reader. No second-reader check on barriers (only the audience labels were spot-checked). Free-text barriers were grouped by keyword rules, first match wins. |
| Burnout apps in "9 of 49,315 posts" | observed, **lower bound** | `term-counts.json` | Narrow patterns ("Calm app," "use Headspace") so ordinary words weren't counted; other phrasings are missed. Talkspace's 2 are the same post shared twice, so 8 distinct writings. "Almost never" holds; the exact 9 doesn't. |
| "Who pays for relief today: mostly government" | **downgraded to not supported** | `results.json` `payer_cost` | Of 153 posts that say who pays, about 60 name a public payer and about 58 name the family, out of pocket or a price (keyword count). The *providers named* are mostly government; who *pays* is split. Rewrite: "caregivers name government programs as providers far more than companies; families and public programs both pay." |
| Only 12% would pay out of pocket; $70 a month cap | documented | Audience box: CAN 2026 (272 self-selected people), Schulz 2016 (monitoring technology) | Neither study is about relief or coordination help |
| "Since 70% of caregivers have jobs" (gap 2 opening) | **overstated** | `docs/audience-segmentation.md`: "70% of caregivers aged 18 to 64 (p.38); 60% of all caregivers (p.130)" | Rewrite: "70% of working-age caregivers have jobs (60% of all)." It appears in the reader version 2, Figma section 2645:12741 and the end-of-day report. |
| Gap 3: money and accounts is "the strongest unmet need among the software segments" | **inferred (Claude's reading)** | `docs/market-analysis-3.md` line 67: "Reading (Claude's, not a decision)… The owner chooses." | The competitive analysis states it as fact. The owner never decided it. |
| Gap 2: the Alzheimer's helpline's advice is "called generic" | observed, **thin** | 5b themes: "Generic advice, didn't listen" in 2 posts | 2 posts. Not enough to judge the helpline overall. |
| VA row: "Approval can take months" | observed, **thin** | 1 post ("seven months to get approved"), plus 15 posts about eligibility rules | "Months" rests on one writer |
| "Segments 11 and 12 had never been researched" | **overstated** | `docs/market-research-segments.md` (respite market size), `docs/exhaustion-dementia-research.md` (10 offerings, 2026-11-02) | Partly researched before, but never assessed in the market opportunity or carried forward |
| Feature analysis "not started for this round" | **incomplete** | `docs/feature-analysis-3.md` (2026-11-04), Figma 2584:10359 | Feature Analysis 3 exists, but it is built on Competitive Analysis **2's** 10 competitors. Only 3 overlap with the current 9 (Caring Village, Everplans, group texts). Under Rule #1 it is out of date. |
| Open items list | **incomplete** | Memory: `market-analysis-updated-2026-11-04.md` | The report leaves out two open decisions: (1) remove the duplicate audience section 2061:543 in FigJam Q5jRpN3MbONqFQF6KTS70j; (2) keep or remove the unrequested Feature Analysis 3 gaps-report rewrite |
| Vision Board #1 is for Audience 1 | reported | Memory: `progress-2026-11-03-board-fixes.md` (owner's decision, 2026-11-03, sticky 2398:7622) | Not rechecked on the board this session |

## 3. Course requirements vs. where the project stands

From the Week 2 lecture transcript (saved, read in full; it cuts off at 1:51:37) and the residency's saved course pages.

| Requirement | What the course says | Status | Gap |
|---|---|---|---|
| Audience segmentation, motivations, goals, use cases | "Not personas… a semantic description"; use cases say "what," not "how" | Done, updated 2026-11-04 | None found |
| Market analysis | Channels, segments, size, top companies, growth; "check its sources" | Done, plus the segment 11 and 12 update | Who-pays research still open |
| Competitive analysis | Competitors from the market analysis; your own questions; "prove it… cite your sources" | Version 2 approved | Three wording fixes above (70% jobs, gap 3, who pays) |
| **Feature analysis** | Features you come up with; check marks for has / doesn't have; "our company" column; find what's unique; double-check AI | **Out of date** (built on the old competitors) | Rebuild from the 9 current competitors and the 4 gaps |
| **Unique value proposition and positioning** | Five questions (who, what problems, which competitors, what impact, how it's different); built from gaps; **one positioning statement per audience** | **Not started** | Next after the feature analysis |
| Release vision (vision boards) | 9 questions; **MVP #1 board first, then the market release (MMP)**; **one board per audience per release** | Not started | Conflict: memory says "Week 1 says define MMP first"; the Week 2 lecture says MVP first. The owner decides. |
| Release scope | Outcomes, not solutions; then epics, features, tasks | Not started | |
| Build plan, repo, Notion backlog, pitch deck, one-page summary (the owner writes it, no AI) | Listed for Week 2 | Not started (summary is the owner's) | |
| **Week 3:** live app on Vercel, Supabase database diagram, GitHub repo | Week 3 is dated Nov 2 | **Not started. The date has passed.** | Schedule risk to raise with the owner |

**Two sources disagree (both reported, neither picked):**
1. **What's required:** the lecture says the bare minimum is "product positioning, unique value proposition and audience segmentation." The course page lists market, competitor and feature analysis and positioning as *bonus*.
2. **Feature table layout:** the lecture describes features as rows with "our company" and competitors as columns. The teacher's Figma example (5:823), used for Feature Analysis 3, has companies as rows and features as columns.

## 4. Not checked

- **The Week 2-3 slides (NotebookLM link):** need the owner's Google sign-in, not opened.
- **The six course template pages:** only their titles are saved.
- **Figma boards:** not re-screenshotted today. The last check was 2026-11-04: no overlaps.
- **Reader agreement on barrier codes:** not measured. Only the audience labels were spot-checked.
- **Market size figures:** come from free summary pages of paid reports; methods not read.
