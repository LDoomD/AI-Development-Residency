# Why four VA cells changed (2026-11-05, approved by the owner)

**Where:** Competitive Analysis 3, VA row ([Figma 2645:12741](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2645-12741)); repo copy `docs/competitive-analysis-3-reader-v3.md`; cells built by `../grid/build_grid_v5.py` (0 problems).

**The rule:** a table cell holds a theme found across many posts, or a fact from the company's own pages. One or two posts are not enough.

## What changed

| Cell | Before | After | Why |
|---|---|---|---|
| What it doesn't do well | Strict rules to qualify, limited aide hours, and unreliable aides. | Strict rules to qualify: the veteran needs a 70% or higher disability rating, and the veteran and caregiver must apply together. | "Hard application or eligibility rules" is named in 14 of the 45 relief posts that name the VA, a real theme. "Limited aide hours" had about 3 posts (p18y0ng6, p1m6kjs8, p1v60a2m). "Unreliable aides" had 5 posts that name the VA somewhere, but the aides may have come from other agencies. The new facts come from the VA's page: "70% or higher" and "You and the Veteran will need to apply together." |
| Help with money and papers | Partly: free legal and financial planning and a stipend. Approval can take months. | Partly: free legal and financial planning and a monthly payment. | "Approval can take months" came from one post (p1mbxwso). "Stipend" changed to plain words. |
| Getting started | …in person. One caregiver waited 7 months for approval. | The veteran and caregiver apply together online, by mail or in person. | The same one post (p1mbxwso). |
| Customer experience | …weekday phone line. Some calls go unanswered. | Local caregiver support teams and a weekday phone line. | One post (p1vfh78m). A second post (p1p9dkvh) says respite calls only reached an answering service. Two posts are still not a theme. |

## What was not done, and why

- The 187-post VA reading (checklist: `research-checklist-va-2026-11-05.md`) was **not run**. The owner and Claude agreed it would not change any coming decision: the VA is named in about 5% of adult-child posts (23 of 486) and about 12% of spouse posts (12 of 98).
- **If needed later:** during the feature analysis, if "help applying for programs" makes the shortlist, read posts about qualifying for **all** programs (Medicaid 77 posts, hospice 45, the VA 44, aging offices 26), using this checklist as a starting point.

## Files

- `va_ids.json`: the 45 relief posts that name the VA
- `va_archive_ids.json`: 178 archive posts that name the VA and caregiving (not read)
