# Change report: VA row in Competitive Analysis 3 (2026-11-05)

## What changed

Four cells in the VA row were fixed. Approved by the owner 2026-11-05.

| Cell | Before | After |
|---|---|---|
| What it doesn't do well | Strict rules to qualify, limited aide hours, and unreliable aides. | Strict rules to qualify: the veteran needs a 70% or higher disability rating, and the veteran and caregiver must apply together. |
| Help with money and papers | Partly: free legal and financial planning and a stipend. Approval can take months. | Partly: free legal and financial planning and a monthly payment. |
| Customer experience | Local caregiver support teams and a weekday phone line. Some calls go unanswered. | Local caregiver support teams and a weekday phone line. |
| Getting started | The veteran and caregiver apply together online, by mail or in person. One caregiver waited 7 months for approval. | The veteran and caregiver apply together online, by mail or in person. |

## Why

- **Three claims came from one caregiver's post each:** slow approval, the 7-month wait, and unanswered calls. That breaks the owner's rule: a table cell must be a theme across the research, not one person's story.
- **Two parts of the "doesn't do well" cell were weak:**
  - "Limited aide hours" came from about 3 posts.
  - "Unreliable aides" came from 5 posts that may have been about other agencies.
- **What stayed is well supported:**
  - "Strict rules to qualify" comes from 14 of the 45 caregiver posts that name the VA.
  - The other facts come from the VA's own website.

## What we decided not to do, and why

- **We did not read the 187 saved VA posts.** The owner asked whether it would bring value. It wouldn't change any coming decision:
  - The VA is a small part of both audiences: 23 of 486 adult-child posts (about 5%) and 12 of 98 spouse posts (about 12%).
  - The blockers that matter most are cost (118 posts), the parent saying no (96), paperwork and rules to qualify (86) and family who won't help (83).
- **Saved for later:** if "help applying for programs" makes the feature analysis shortlist, read posts about qualifying for all programs (Medicaid, hospice, the VA, aging offices). Start from `docs/sources/competitive-analysis-3/va-check/research-checklist-va-2026-11-05.md`.

## Mistakes and fixes

| What went wrong | Fix |
|---|---|
| The three single-post claims got into the table on 2026-11-05 when the VA row was corrected | Removed. Every cell must be a theme or a fact from the company's own pages. |
| I first suggested softer wording, which still built the table on one post | Withdrawn after the owner questioned it. |
| I suggested keeping the weak "doesn't do well" cell, the same mistake | Fixed after the owner asked "just based on a few posts?" |
| I proposed a 187-post read for three small cells | Weighed against the coming deliverables and skipped. Check the value before starting big research. |
| The first build script emptied an older data file (`grid-v2.json`) | Restored from GitHub right away. The script can no longer write to older files, and none were changed. |

## Where things are

- **Figma:** [Competitive Analysis 3 (2645:12741)](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2645-12741). The 4 cells are updated, and the subtitle says what changed.
- **Repo:** `docs/competitive-analysis-3-reader-v3.md` is the new version. Version 2 is marked superseded.
- **Scripts:** `docs/sources/competitive-analysis-3/grid/build_grid_v5.py` writes `grid-v5.json` and `business-v4.json` (0 problems).
- **Details:** `docs/sources/competitive-analysis-3/va-check/va-cells-change-2026-11-05.md`, with the post ids behind every count.
- **Git:** not committed yet.

## Next

1. Commit these changes.
2. Clean tables for the owner's new Figma page. First, ask whether the owner wants markdown, CSV or Figma.
3. Feature analysis: full audit and rebuild, built around the four big blockers for both audiences.
