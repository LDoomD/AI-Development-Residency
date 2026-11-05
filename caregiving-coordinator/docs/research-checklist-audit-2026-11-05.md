# Research checklist: multi-agent audit of yesterday's updates (2026-11-05)

Filled in from `docs/research-checklist.md`. Nothing runs until the owner approves.

## 1. What this task is for

- **Task:** independently audit every update made on 2026-11-04 and the data behind it, before the feature analysis builds on it.
- **Deliverables checked:**
  - market analysis (segments 11 and 12 update)
  - audience segmentation (exhaustion and relief by audience)
  - competitive analysis (version 2: 2 new rows, gaps 2 and 4)
- **Later deliverables it protects:** the feature analysis and unique positioning (deliverable #2), then release vision and scope (#3).

## 2. What the earlier deliverables set

| Set by | What it sets | How the audit uses it |
|---|---|---|
| Audience page (2378:7111, 2378:7177) | Audience 1 = adult child; Audience 2 = spouse or partner | Every check reports Audience 1 and 2 separately |
| Market analysis reading pass (`docs/sources/market-analysis-3/segments-11-12/READING-INSTRUCTIONS.md`) | The codes: help used, status, barriers, "wanted a break, no help" | The second reader uses the same instructions, without seeing the first reader's codes |
| The cell rules (`CLAUDE.md`) | Every cell answers its column's question from data | Agents check meaning, not just that a quote exists |

## 3. Data and documents to audit

| What | Where (repo) | Where (Figma, file HcDDdEGAnikTImO8v7UPMp) |
|---|---|---|
| Relief reading codes (1,086 items, 831 relevant) | `docs/sources/market-analysis-3/segments-11-12/codes/`, `results.json` | — |
| Audience labels (831) | `audience-labels.json`, `results-by-audience.json` | — |
| Market analysis update | `docs/market-analysis-3.md` (sections dated 2026-11-04 at the end), `docs/market-analysis-segments-11-12-findings.md` | 2704:13380; the older opportunity answer 2601:12718 |
| Audience update | `docs/audience-segmentation.md`, `docs/audience-teacher-format-2026-11-04.md` (sections at the end) | 2704:15080 |
| Competitive analysis version 2 | `docs/competitive-analysis-3-reader-v2.md`, `grid-v3.json`, `business-v2.json`, new pages in `docs/sources/competitors-4/` | 2645:12741 |

## 4. The audit, split into 6 agents (each works alone, without seeing my conclusions)

| # | Agent | What it checks | Pass rule |
|---|---|---|---|
| 1 | **Second reader** | Re-codes a random 50 relevant posts (25 adult children, 15 spouses, 10 others; fixed seed) from the instructions alone. A script then compares its codes with the first reader's. | Help kinds and status agree on 80% or more of posts. Barrier agreement is reported per barrier. |
| 2 | **Relevance check** | Re-reads a random 40 posts the first readers marked *not* relevant | 90% or more confirmed as not relevant |
| 3 | **Audience labels** | Re-labels a random 40 posts the *readers* labeled (the first spot check only covered script labels) | 90% or more agree |
| 4 | **Market analysis update** | Every number and claim in the segments 11 and 12 update (repo and Figma 2704:13380) against `results.json`, the AARP report and the saved market size pages; also whether the older opportunity answer (2601:12718) is marked as updated | Every claim traced to its source, or flagged |
| 5 | **Audience update** | Every number and claim in the audience additions (repo and Figma 2704:15080) against `results-by-audience.json`, the AARP report and the Alzheimer's Association report | Same |
| 6 | **Competitive analysis version 2** | The 2 new rows and gaps 2 and 4 (repo and Figma 2645:12741): does each cell's *meaning* match its source, not just its quote? Plus the 7 spots already flagged ("70% of caregivers," "strongest unmet need" in 5 places) | Same |

A script then compares the numbers across the repo files, the Figma sections and yesterday's dog feeding report, to catch any copy that doesn't match.

## 5. Questions

| Question | From |
|---|---|
| Would a second reader code the same help and barriers? | Today's audit, "each barrier coded by one reader" |
| Were posts wrongly left out as not relevant? | Reading pass limits |
| Are the reader-made audience labels as accurate as the script labels? | Audience split checklist |
| Does every published number match its data, in every place it appears? | Rule #1 (one connected project) |

## 6. What will be produced, and how to audit it

- `docs/sources/audit-2026-11-05/`: each agent's sample, codes and report, plus the comparison scripts and their output
- `docs/reports/audit-2026-11-05-results.md`: one table of findings, each with its evidence state (skeptical-audit), a link to the file or Figma node, and a proposed fix
- **Nothing in the deliverables changes until the owner approves the fixes.**
- **Size:** 6 agents, about the cost of one of yesterday's reading packs each.
