# Audit results: yesterday's updates (2026-11-05)

Six independent agents audited the 2026-11-04 updates, working blind where they re-read posts. Checklist: `docs/research-checklist-audit-2026-11-05.md`. Every agent's files are in `docs/sources/audit-2026-11-05/`:
- `compare-results.json` (audits 1-3)
- `audit-4-market.md`, `audit-5-audience.md`, `audit-6-competitive.md`

Evidence states follow the skeptical-audit skill. **Nothing in the deliverables has been changed by this audit.** Fixes wait for the owner.

## 1. Is the underlying data reliable?

| Check | Result | State | Meaning |
|---|---|---|---|
| Second reader, 50 posts, blind (audit 1) | Relevance agreed 49 of 50. "Needs a break, no help" agreed 49 of 49. Status agreed 44 of 49. Kinds of help fully agreed 35 of 49 (average overlap 83%). Barriers agreed well for the parent refusing (7 of 7) and cost (5 of 6), weaker for quality worries (4 of 7) and eligibility rules (4 of 7). | observed (`compare.py`) | The big counts hold. Barrier counts are approximate, especially quality worries and eligibility rules. |
| Relevance, 40 posts left out (audit 2) | 37 of 40 confirmed. 3 should have been included (support groups, a VA program). | observed | About 7% of left-out posts were wrongly excluded, so relevant counts are slightly low. |
| Audience labels made by readers, 40 posts (audit 3) | 39 of 40 agree. The 1 disagreement is a paid friend (unclear vs client). | observed | Audience labels are reliable: 95% for script labels, 97.5% for reader labels. |
| Quote and code checks | `verify_codes.py`, `verify_audience.py`, `build_grid_v3.py` all pass | observed (rerun by 3 agents and by me) | Quotes are real and exact. |

## 2. Problems found, by deliverable (most important first)

### Market analysis (audit 4; repo `market-analysis-3.md` end sections, findings file, Figma [2704:13380](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2704-13380))

| # | Problem | Evidence | Proposed fix |
|---|---|---|---|
| M1 | **"Family or friends won't help" (93) is inflated.** It was built by my keyword rule from free-text barriers, and the rule caught unrelated text ("groups geared to spouses," "facility declined combative husband," "reason not given"). | Audit 4 estimates about 17 false matches. My own check finds 7 to 12, depending on how "husband or spouse won't agree" is counted. True count: about 76 to 86, roughly tied with eligibility rules (86). | Fix the grouping rule, recount, and say "two of the top three barriers (cost, the parent refusing) aren't in AARP's list" instead of three |
| M2 | **Provider counts undercount.** Only exact names were counted. | Audit 4: VA 38 (not 28), Medicaid and waivers about 32 (not about 16), Area Agencies 14 (not 10). A broader count gives VA 40, Medicaid 77 and aging offices 26. Either way, **Medicaid is the most named payer or provider, not the VA**. | Recount with one written rule, publish the rule, and update the "who provides" cells |
| M3 | **Verdicts too strong.** "The gap is access, not supply" ignores waitlists (59) and no trained providers (38). "Confirms AARP's 39% vs 13%": Reddit can't confirm a national rate. "VA and Medicaid applications (86)": only 59 of the 86 name them. | audit-4-market.md | "The main gap is access: cost, eligibility rules, the parent refusing and family not helping. Waitlists and too few providers also limit supply." "Consistent with AARP," not "confirms." |
| M4 | **Spouse vs adult child "no help" (30% vs 25%) isn't a real difference** on 98 posts. The support group difference (22% vs 12%) is. | Audit 4 and audit 5 (statistical test) | Report "both about a quarter"; keep the support group difference |
| M5 | Small wording errors: 4 of 5 cost examples in quote marks aren't word for word, one isn't respite, "26% of caregivers" should be "26% of posts," and "labels were checked" covered only the script labels | audit-4-market.md | Correct each |
| M6 | The old opportunity answer ([2601:12718](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2601-12718)) has only a small callout, not the big yellow banner CLAUDE.md requires for superseded work | CLAUDE.md "Superseded work" | Add a yellow banner across that part, pointing to 2704:13380 |
| M7 | The repo says the board's segments section is "2026-11-01"; the section itself is dated 2026-11-04 (its rows say "Researched 2026-11-01") | audit-4-market.md | Reword |

### Audience (audit 5; repo `audience-segmentation.md`, `audience-teacher-format-2026-11-04.md`, Figma [2704:15080](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2704-15080))

| # | Problem | Proposed fix |
|---|---|---|
| A1 | **Wrong page:** the Alzheimer's Association 59% is on PDF page 54 (printed p.52), not 55. Also wrong in `exhaustion-dementia-research.md`. | Correct in all 3 places |
| A2 | "Spouses turn more to therapy (26% vs 17%)" counts any mention; actual use is 14% vs 10%, not a real difference. "No help, 30% vs 25%" isn't a real difference either. | Keep only the support group difference; describe the rest as similar |
| A3 | Wording too strong: "often the VA" (3 of 10 posts); "the top thing caregivers want help with" (it tops a help-or-information list, a different question from respite); "neither audience uses burnout apps" (none appear in relief posts; a few appear elsewhere) | Soften each |
| A4 | **Repo and Figma don't match:** the spouse blocker list has 3 items in one file and 5 in another; the adult-child list leaves out quality worries (bigger than waitlists) | Make all three copies the same |

### Competitive analysis (audit 6; repo `competitive-analysis-3-reader-v2.md`, Figma [2645:12741](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2645-12741))

| # | Problem | Proposed fix |
|---|---|---|
| C1 | **Respite row, need 1, is contradicted:** "No: gives a break, not guidance" — the saved adult day page lists family counseling and behavior help | "Partly: adult day centers offer family counseling and behavior help. Respite itself is a break." |
| C2 | Respite "how they keep customers" doesn't answer the question, and "fees per day or stay" isn't in any saved source; the sliding-scale fact covers adult day only | Rewrite from sources, or get a source |
| C3 | **VA row is missing its key limit:** the stipend, planning help and 30 days of respite are for the main program (PCAFC), which needs a 70% or higher disability rating and 6 months of care. VA respite can carry a copay. "Approval can take months" and "some calls go unanswered" each rest on one post. | Add the limit; soften or drop the one-post claims |
| C4 | **Gap 2 overstated:** it leaves out Medicare GUIDE (care navigator, respite up to $2,500 a year, paid by Medicare). Cariloop can be kept for $249 a month after leaving a job. "Advice called generic" is 2 posts vs 3 that say the helpline worked. | Reword gap 2 with GUIDE and the Cariloop limit; drop "called generic" |
| C5 | Gap 4: "13%" means "have ever used respite"; the page is missing; "for adult children and spouses alike" is too strong | Add "ever used" and the page; soften |
| C6 | **Two of this morning's fixes were incomplete:** the "Data behind the gaps" row still says "70% are employed"; "strongest unmet need" remains in the older copies (`competitive-analysis-3.md`, the v1 reader, the inputs file); "Respite and the VA now cover the #1 problem" is too strong | Finish them |
| C7 | Repo and Figma gap 2 and gap 4 wording differ; Figma gap 4 is missing one sentence | Make them match |

## 3. What this changes

- **The core findings hold:**
  - exhaustion is the #1 problem
  - respite is wanted far more than used
  - cost and the parent refusing are top blockers
  - burnout apps are rarely used
  - the audiences are labeled reliably
- **What changes:**
  - Family not helping is roughly tied with eligibility rules, not clearly third.
  - Medicaid is the most named payer or provider.
  - Several audience differences shrink to "similar."
  - Gap 2 needs Medicare GUIDE.
  - The VA row needs its eligibility limit.

## 4. Not checked

- The readers' judgments on posts outside the 130 re-read
- The live websites (only saved copies were read)
- The CAN 2026 and Schulz 2016 PDFs
- Grand View's scope for the $19.3B adult day figure
- The version 1 competitor rows
