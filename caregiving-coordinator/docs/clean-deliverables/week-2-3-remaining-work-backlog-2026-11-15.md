# Week 2 and 3: remaining work, in order (agile backlog, started 2026-11-15)

**What this is:** the ordered list of everything still open for the Week 2 and Week 3 homework, with why each item is in its place, what "done" means, and what each iteration changed. It is a living file: update it at the end of every iteration, then update the release roadmap and write a new handoff report.

## Why this is an agile backlog
The instructor's "Week 2 and 3: Product Delivery Management" board says it plainly (section "The Process for Agile Product Management"):
- Agile teams do **not** "make a 30 page requirements doc for the entire product," "gather all requirements first," or "build all specifications before starting work."
- Agile teams **do** "gather requirements all of the time," "gather the most important requirements first," "build the most important stuff (MVP!) all the time," and "work in parallel."
- The loop is: draft vision, draft scope, break scope into epics and features, get the first tickets ready, start the work, then "keep adjusting after you deliver work chunks. Repeat."
- "Requirements are assumptions": every decision is an assumption until real users use the product, so each new delivery forms new assumptions to validate.
- The roadmap "is a deliverable that you maintain over time... Don't let it sit there collecting dust."
- Tickets are refined with INVEST, and only the next two weeks of work are made ready (lecture, as the 2026-11-11 notion-backlog file records).

**How the order is chosen:** (1) things the homework requires and the board's green "this week" boxes name come first; (2) among those, whatever blocks other work goes first; (3) the highest-priority epic (Epic 3, the "Top" problem for both audiences) is finished end to end before widening to other epics; (4) things only the owner can do are listed separately; (5) nice-to-haves from other students' boards wait.

## Iteration 1: shipped 2026-11-15
| Done | Where |
|---|---|
| Epics, features and tasks numbered 1, 1.1, 1.1.1, with a business goal and KPI trace on each epic | Figma "Create Epics, Features, Tasks" and `epics-features-tasks-numbered-2026-11-15.md` |
| Non-functional list T1 to T4, next to the functional list | Figma and `non-functional-epics-features-tasks-2026-11-15.md` |
| 20 user stories (10 epic-level, 10 feature-level) | Notion "Epics and Features" and `epic-and-feature-user-stories-2026-11-15.md` |
| Five Epic 3 task pages with the eight headings, INVEST grades and sources | Notion Kanban board and `task-pages-epic-3-2026-11-15.md` |
| Notion submission page items 4 and 5 brought up to date | Notion "Week 2 and 3 - Product Specifications" |
| Pull request 54 (four files), merged 2026-11-15. Pull request 55 (task flows, this backlog, the 3.1.3 change, handoff reports) | GitHub, 54 merged, 55 open |

## Ordered backlog
Sizes are guesses, not a team's estimate.

### Iteration 2: finish what is required and unblock the rest
| # | Item | Why now (data) | Depends on | Done when | Who |
|---|---|---|---|---|---|
| 1 | **Task flows for Epic 3** (DONE 2026-11-15, two flows, one per audience: drawn in Figma "TASK FLOWS (Epic 3)", saved in `task-flows-epic-3-2026-11-15.md`, linked from the five Notion pages) | The board's green "this week" boxes list Task Flows, Acceptance Criteria / User Stories and Use Case Scenarios / BDD Scenarios under the Requirements milestone. You have no task flows. The lecture: "one flow chart per use case; each ticket might have one to three or four use cases." Epic 3 is the Top problem. | The five Epic 3 pages (done) | Two flows (Audience 1: accept help, then small steps; Audience 2: partner accepts help) with happy and non-happy paths, drawn in Figma beside the epics, linked from the Notion pages, and described in a saved file | Claude drafts, owner approves |
| 2 | **Name and create the empty public GitHub repository** | Week 2 requirement 5. Week 4 builds in that same repository. Quick, and nothing else waits on it except Week 4. | The owner choosing a name (the course example name belongs to the ADHD app) | Public repo exists with no code, link ready for the submission page | Owner decides the name. Claude creates it only on the owner's go. |
| 3 | **Finish the build plan** | Week 2 requirement 6 and Basic Homework items 4 and 5. Boxes 1 to 4 are approved. Box 5 (development operations) is Proposed, box 6 (quality engineering) is not written, and the Figma section `3073:8029` still has the old text without the 8 fixes. | The owner approving box 5, including the branch protection question | Boxes 5 and 6 approved, T5 and T6 added to the non-functional list, Figma updated, files saved | Claude drafts, owner approves |

### Iteration 3: widen to the rest of the first two weeks
| # | Item | Why (data) | Depends on | Done when |
|---|---|---|---|---|
| 4 | **Check the use case count (22 in Figma, 17 in Vision and Scope), then write feature-level use cases for the other 8 features** | The Notion template has a "Feature-Level Use Case Scenarios" heading under every feature, and only Epic 3 is filled. Epic 4's and Epic 6's Audience 2 features have no MVP use case, and my recommendation was to leave that gap and record it. | Item 1 (so the pattern is set) | Counts reconciled in one sentence; the Notion headings filled or noted as a known gap |
| 5 | **Epic 1 task pages (six), one INVEST grade each** | Epic 1 is the second epic in the first two weeks of the roadmap and the Notion board (`notion-backlog-2026-11-11.md`: 11 tasks, 5 in Epic 3 and 6 in Epic 1). The page headings include Technical Requirements, which covers the Basic Homework items "technical requirements" and "user requirements" (my reading, Proposed). | Item 3 (so Technical Requirements can cite T5 and T6) | Six pages written, read back, saved |
| 6 | **Update the release roadmap and the Notion board** | The board says the roadmap must change when plans change. Task slicing, task flows and the repo may move dates. | Items 1 to 5 | Roadmap in Figma (`3068:9448`) and `release-roadmap-2026-11-11.md` match the backlog |

### Iteration 4: summarize
| # | Item | Why (data) | Depends on | Done when |
|---|---|---|---|---|
| 7 | **Pitch deck** | Week 2 requirement 8: "a pitch deck summarizing all of this." It needs everything above to exist. | Items 1 to 6 | Deck in the Notion Product Pitch Deck template, linked from the submission page |

### Only the owner can do these
| # | Item | Note |
|---|---|---|
| A | Write the one-page "What I Did" and "What I Learned" | Without AI. Claude never writes it. |
| B | Make the submission page shareable and email the link to the instructor | Sharing is not set up. The owner said "not yet." |
| C | Confirm whether the Premium research paper was submitted | The owner said "not yet." |
| D | Merge pull request 55 and later pull requests | Merging is the owner's. |

### Later iterations (not scheduled)
- **Research on what parents and partners accept.** Tasks 3.1.2, 3.1.3 and 3.2.1 leave out advice because no saved research says what works. Do it before any advice text, and treat the result as a new assumption to validate.
- **A second slice for task 3.1.1:** "seeing follow-through across steps over time."
- **Task pages for Epics 2, 4, 5 and 6.** The lecture says to make only the next two weeks ready.
- **Extras from other students' boards:** phased build plan (five phases), traceability table, KPI alignment, open questions on the board, narrative journey. Not required. Adding them now would be building more than the board asks.
- **Optional:** fill the Costs box in Vision and Scope; bring `competitive-analysis-4-updated-2026-11-07.md` in line with Figma (low priority).
- **The two lawyer questions** (whose consent counts for a parent or partner who never signs up; California's medical privacy law) before any real caregiver data.

## Assumptions to validate (requirements are assumptions)
1. The 1-week size of each task slice is a guess. Check it when the build starts in Week 4.
2. Pairing a scenario with a specific task (3.2.1 and 3.2.2) is Claude's reading of the audience table, which does not pair them.
3. The five Epic 3 pages and the 20 stories are Claude's wording, approved by the owner on 2026-11-15.
4. Task flows: the board's green box lists them, and the lecture says "there might be one per use case." I treat at least one flow per main use case as due this week.
5. Audience 2's problem for Epic 3 is thin: 9 posts and threads (master report table 2b), read by one person and not double-checked.
6. Whose consent counts for a parent or partner who never signs up is unresolved (risk profile, open question 1).

## How we iterate
At the end of each iteration: (1) mark the items above done with the date and the file or page that proves it; (2) record what changed in the Iteration log; (3) update the release roadmap and the Notion board; (4) re-read this list and re-order it if the data changed; (5) write a new handoff report; (6) one pull request per deliverable, merged by the owner.

## Iteration log
| Iteration | Dates | What shipped | What changed in the plan |
|---|---|---|---|
| 1 | 2026-11-15 | See "Iteration 1" above, plus item 1 of Iteration 2 (task flows) | Feature-level stories moved from "parked" to "required" after the instructor's board said epics and features should have stories. Tasks stay outcome-based on the epics list, and each task page narrows to one slice. |
| (same day) | 2026-11-15 | Two task flows (first drawn as three, merged after comparing with Morgan's and Lucy's one flow); task 3.1.3 widened to cover paid help or aids | The owner asked what to do about the one situation with no task. Claude proposed widening 3.1.3 instead of adding a task, so names and numbers stay the same. |
