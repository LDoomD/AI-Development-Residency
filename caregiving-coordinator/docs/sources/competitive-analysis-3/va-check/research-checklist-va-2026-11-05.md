# Research checklist: checking the VA row in Competitive Analysis 3 (2026-11-05)

Filled in before any reading starts (Rule #1). Waiting for the owner's OK.

## 1. What this task is for

- **Task:** three cells in the VA row rest on one caregiver's post each. Read every saved post about the VA to see whether these are real themes:
  1. "Approval can take months" (help with money and papers)
  2. "One caregiver waited 7 months for approval" (getting started)
  3. "Some calls go unanswered" (customer experience)
- **Deliverable it updates:** Competitive Analysis 3, the VA row ([Figma 2645:12741](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2645-12741); `docs/competitive-analysis-3-reader-v2.md`).
- **Later deliverables it can change:** the feature analysis (if slow applications are a real theme, "help applying for programs" is a feature idea) and positioning (gap 4: relief exists, but caregivers can't reach it).

## 2. What the earlier deliverables already set

| Set by | What it sets | How this task uses it |
|---|---|---|
| Audience page (`docs/audience-teacher-format-2026-11-04.md`) | Audience 1 = adult child caring for a parent. Audience 2 = spouse or partner. | Every count is split by audience. |
| Market analysis (`docs/market-analysis-3.md`, CORRECTED 2026-11-05) | Segment 11, respite: the VA is named in 44 posts. Paperwork and rules to qualify block 86 posts. | The same posts are the starting point. |
| Competitive analysis (`docs/competitive-analysis-3-reader-v2.md`) | 9 competitors, 5 criteria, business questions, 4 gaps | Only the VA row's cells change. |
| Open question: who pays | The VA pays for qualifying veterans' families | Not changed by this task. |

## 3. All saved research on the VA

| File | What it has | Used, or left out and why |
|---|---|---|
| `docs/sources/market-analysis-3/segments-11-12/codes/` | 45 relief posts that name the VA (the count of 44 came from a slightly different rule) | **Used:** read in full again |
| Saved Reddit archive (`docs/sources/reddit/arctic-shift-2026-11-03/`, 49,315 posts) | 178 posts that name the VA and caregiving; 36 of them are already in the 45 | **Used:** the other 142 are read too, so the check covers all saved VA posts, not just the ones about breaks |
| VA's own pages (`docs/sources/competitors-4/va-caregiver/`) | What the VA says about applying and timelines | **Used:** to compare what the VA promises with what caregivers say |
| `market-analysis-segments-11-12-findings.md`, `research-checklist-ca3-exhaustion.md` | Older VA counts (28), now corrected | Left out: replaced by the corrected counts |
| `audience-goals-use-cases.md` | One quote about a VA disability rating | Left out: it's one quote, already among the posts |
| Audit and inventory reports (11-05) | Notes that the VA count was too low | Left out: no new evidence |
| `academic-findings.md` | Nothing about the VA (matched the word "veteran" elsewhere) | Left out |

**Total to read: 187 posts** (45 + 142).

## 4. How the research splits

- **By audience, always.** Each post records who the writer cares for: parent, spouse or partner, other relative, child, client, unclear. Of the 45 relief posts already labeled: parent 23, spouse or partner 12, other relative 5, unclear 5. The other 142 get labeled during reading.
- **Only family caregivers count.** Posts by veterans about themselves, paid aides or VA staff are marked "not relevant."

## 5. The questions

| Question | Where it comes from |
|---|---|
| Is the post by a family caregiver about VA help for caregiving? | Rule: only caregiver experiences count |
| Who does the writer care for? | Audience split (Rule #1) |
| Did the writer apply, and how long did approval take (or is it still waiting)? | VA row, cells 1 and 2 |
| Did the writer try to reach the VA (phone line, social worker, support team), and did anyone answer or call back? | VA row, cell 3 |
| What else went well or badly with the VA? (to catch themes we haven't named) | Rule: cells come from themes across all the data |

## 6. What will be produced, and how the owner can audit it

- **Files** (each logged in `docs/sources/INDEX.md`), in `docs/sources/competitive-analysis-3/va-check/`:
  - `va_ids.json`, `va_archive_ids.json`: the post lists
  - reading instructions, and each reader's answers with an exact quote per answer
  - `count_va.py` → `va-results.json`: every number, with the post ids behind it
- **Checks:** a script confirms every quote matches its post word for word, and every post is answered once.
- **How the cells get decided:**
  - A theme found in several posts stays in the cell, written as a theme. The count goes in the evidence file only.
  - A claim found in only one or two posts comes out of the cell.
  - The new cells are shown to you before anything changes. Then a new version, with nothing deleted.
- **Limits:** people who post online are often having a hard time, so this shows patterns, not how often it happens nationally. VA rules have changed over the years, so older posts may describe old rules; each answer records the post's date.
