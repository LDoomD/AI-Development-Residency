# Handoff: Caregiving Coordinator → Week 2 and 3, iteration 2 (repository, build plan, then use cases, Epic 1 pages, roadmap, pitch deck) (2026-11-15, night)

> **Replaced by** `dogfood-2026-11-15-handoff-task-stories-and-acceptance-criteria.md` (2026-11-15, late). The repository, build plan and use case work in this report is finished; start from the newer report.

Replaces: `dogfood-2026-11-15-handoff-week-2-3-iteration-2.md` (written earlier the same evening, before the task flows were reworded and the owner confirmed them). Older reports stay replaced: `dogfood-2026-11-15-handoff-epics-features-notion-and-task-requirements.md`, `dogfood-2026-11-13-handoff-homework-hub-and-build-plan.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8, especially the ordered backlog `week-2-3-remaining-work-backlog-2026-11-15.md`. Confirm in a few complete sentences where we are. Then check `gh pr list --state open` and show me the two decisions in section 4 that block iteration 2 (the repository name and build plan box 5) before doing anything else. Explain every decision I must make: what it is, why it matters, the choices, what happens after each. Say why you chose a structure when you propose it, and write box and arrow labels in plain words, with no jargon. Base everything on my most up-to-date deliverables and the three master reports, and show the file and line for each fact. This is an agile project: work in small ordered chunks, update the backlog file after each one. Ask before Firecrawl, the browser pane or Chrome."

## 0. Start here
- **Where we are:** iteration 1 of the agile backlog is finished. Epic 3 (the highest-priority epic) is done end to end: numbered epics, features and tasks, 20 user stories, a numbered non-functional list, five task pages, and two task flows. All of it is saved in GitHub in two pull requests: 54 (merged 2026-11-15, 22:15) holds the first four files, and 55 (open, not merged) holds the task flows, the backlog, the task 3.1.3 change and the handoff reports.
- **The outcome so far, in one sentence:** the instructor's board and Morgan's and Lucy's boards told us exactly what the Requirements milestone needs, and Epic 3 now meets it in that form.
- **Next milestone:** iteration 2 of `docs/clean-deliverables/week-2-3-remaining-work-backlog-2026-11-15.md`. Item 1 (task flows) is done. Items 2 and 3 are next: create the empty public GitHub repository, and finish the build plan (boxes 5 and 6, then the Figma update). Items 4 to 7 follow.
- **Method (Approved by the owner, 2026-11-15):** agile. The instructor's board says agile teams "gather the most important requirements first," build the MVP, and "keep adjusting after you deliver work chunks." Requirements are assumptions. The roadmap is maintained, not left alone.
- **Owner's track (Approved, 2026-11-12):** Premium, the owner builds their own app, the caregiving coordinator. Course dates do not drive the plan.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| Layout follows Morgan's and Lucy's boards: readable numbered text lists in green sections, the instructor's template boxes kept, no table (the owner said a table was hard to read and not asked for) | **Approved** (owner, 2026-11-15) | Figma "Create Epics, Features, Tasks" |
| Epics, features and tasks numbered 1, 1.1, 1.1.1 with the same words as the 2026-11-11 file: 6 epics, 10 features, 27 tasks | **Approved** | `epics-features-tasks-numbered-2026-11-15.md` |
| Each epic ends with its business goal and KPI (the 6 epics are the 6 business goals in order) | **Approved** (the owner approved the six tags) | Same file and the Figma green list |
| 20 user stories: 10 feature stories and 10 epic stories, one per audience | **Approved** (owner, all 20). The wording is Claude's | `epic-and-feature-user-stories-2026-11-15.md` and the Notion page "Epics and Features" |
| Non-functional list T1 to T4 (tools, database, system architecture, security) from build plan boxes 1 to 4, including the rows the build plan tags "Proposed" | **Approved** (owner: "include them") | `non-functional-epics-features-tasks-2026-11-15.md` and Figma |
| Five Epic 3 task pages with the eight Notion headings, INVEST grades and a Sources list in Background | **Approved** (3.1.1 alone, 3.1.2 under delegation, then 3.1.3, 3.2.1 and 3.2.2 as a batch). Wording is Claude's (Proposed inside each page) | `task-pages-epic-3-2026-11-15.md` and the five Notion task pages |
| Two task flows, one per audience, both with happy and non-happy paths. First drawn as three, then Flows 1 and 2 were joined into one Audience 1 flow with two parts (Part 1: raise it and record the answer; Part 2: try small steps). The owner found the join confusing twice (an unclear connector label, then repeated wording and the jargon "stays open"). After the junction was reworded in plain words the owner said "It makes sense now" | **Approved** (owner, 2026-11-15) | `task-flows-epic-3-2026-11-15.md` and Figma "TASK FLOWS (Epic 3)" |
| Task 3.1.3 widened to cover a parent turning down paid help or aids, the one situation in the master CSV (line 47) with no task | **Proposed by Claude and applied under the owner's delegation.** The owner asked what to do about the gap and has not objected | `task-pages-epic-3-2026-11-15.md`, the Notion page |
| Ordered agile backlog with reasons, assumptions and an iteration log | **Approved** (owner, 2026-11-15) | `week-2-3-remaining-work-backlog-2026-11-15.md` |
| Every decision asked of the owner must explain itself; show file and line for each fact | **Approved** (rules, 2026-11-15) | `caregiving-coordinator/CLAUDE.md`, memory |

## 2. Key findings and data
### What the instructor's board requires (Authoritative: the owner's copy of the instructor's board, `node-id=3089-14567`)
| Point | What it says |
|---|---|
| User stories at every level | "epics and features also should have user story statements (and not acceptance criteria)." At epic and feature level the "so that" states value; at task level it states the problem to avoid |
| Backlog details | "User story statements, Tasks, Acceptance criteria, Use case scenarios, Task flows, Annotations" |
| Green boxes for this week | Product Positioning, Unique Value Proposition, Problem Statements; MMP Vision Board, MVP Vision Boards, Release-Level Use Cases; MMP Release Scope, MVP Release Scope, Release Roadmap, Epic and Feature Definition; Acceptance Criteria / User Stories, Task Flows, Use Case Scenarios / BDD Scenarios |
| INVEST | Applied at sprint refinement and in the Kanban process, to tasks with requirements |
| Happy and non-happy path | "very important... to write both" |
| Technical requirements | "DO NOT WRITE TECHNICAL REQUIREMENTS YOURSELF." Lean on the developer (Claude Code plays that role) |
| Non-functional order | Tool selection, database architecture, system architecture, security protocol, development operations, quality engineering, then functional work (lecture notes) |
| Agile | Agile teams do not "gather all requirements first" or "build all specifications before starting work" |

### Evidence behind Epic 3
| Finding | Number | Source | Confidence |
|---|---|---|---|
| Posts and threads: the parent says no to doctors, help, moving or giving up the car | 60 (rank 5 for adult children) | Audience Segmentation Master Report, table 2b, line 108 | Credible secondary (one reader, not double-checked) |
| Posts and threads: the partner denies needs and refuses help or changes | 9 (rank 8 for spouses) | Same report, line 111 | Estimate (thin) |
| Competitors scoring a Yes on "parent accepts help" | 0 of 16 (11 score No) | Competitive Analysis Master Report, finding 2, line 197 | Credible secondary |
| MVP use cases | 17 (11 for Audience 1, 6 for Audience 2) | `vision-and-scope-boards-2026-11-10.md` | Authoritative (the owner's file) |
| Use cases in the owner's Figma "Key Use Cases" box | 22 (12 and 10) | Figma "Updated Deliverables" page. The master report's table 2b says 11 and 10 | **Unresolved, probably the full list before prioritizing** |
| Backlog tasks in Notion for the first two weeks | 11 (5 in Epic 3, 6 in Epic 1) | `notion-backlog-2026-11-11.md` | Authoritative |

### Status of the board's green deliverables
Done per earlier handoffs and the Figma sections: positioning, UVP, problem statements, both vision boards, release-level use cases, both release scopes, release roadmap, epic and feature definition. Partly done: acceptance criteria and user stories (20 epic and feature stories, five of 11 task pages), use case scenarios and BDD (five tasks), task flows (Epic 3 only). The positioning, UVP and problem statements were not reopened on 2026-11-15.

## 3. Excluded and deferred
- **Research on what parents and partners accept.** Tasks 3.1.2, 3.1.3 and 3.2.1 leave out advice on how to raise a move, which next step to try and how to raise hard topics. The saved research counts refusals (for example 3 in the qualitative set and 12 in the community-voice set) but not what worked. Do this before any advice text. Backlog: later iterations.
- **A second slice for task 3.1.1** ("seeing follow-through across steps over time"). No page yet.
- **Task pages for Epics 2, 4, 5 and 6.** The lecture says to make only the next two weeks ready.
- **Extras from Lucy's and Morgan's boards:** the five-phase build plan, traceability table, KPI alignment, open questions on the board, a happy-path narrative (for the pitch deck). Not required.
- **Medicine tracking:** out of MVP #1 (risk profile and the MMP scope table).
- **Premium paper status and sharing the homework hub with the instructor:** the owner said "not yet" (2026-11-15), so they are not decisions here.
- **Optional:** fill the Costs box in Vision and Scope, and bring `competitive-analysis-4-updated-2026-11-07.md` in line with Figma.

## 4. Open decisions
The next session must not decide these alone.
1. **The name of the new empty public GitHub repository.** What it is: Week 2 requirement 5 asks for a new public repository with no code. Why it matters: Week 4 builds in that same repository, and the course example name belongs to the ADHD budgeting app. Choices: the owner names it (a short name for the caregiving app), then says go and Claude creates it with `gh`, or the owner creates it. After that the link goes on the submission page.
2. **Build plan box 5 (development operations), including the branch protection question.** What it is: how code reaches users: branches, automatic checks on every pull request, preview copies, migrations, keys. It is only a Proposed draft in `docs/build-plan-nfr-draft-2026-11-12.md`. Why it matters: box 6 and the Figma update wait on it. The live Week 5 page says "You do not need branch protection, because you are on GitHub's free plan," while the draft's step 3 depends on it. Choices: approve as written; approve without the branch protection rule (my suggestion, because the course does not require it); change it. After approval Claude drafts box 6 and adds T5 and T6 to the non-functional list.
3. **Epic 4's and Epic 6's Audience 2 features have no MVP use case.** Why it matters: a reviewer will see features without use cases. Choices: leave the gap and record it (my suggestion; nothing else changes), put four use cases back (changes the Vision and Scope and the count of 17), or mark those features MMP (changes the epics file and the roadmap). It comes up when the other eight features' use cases are written.
4. **Where the numbered epic boxes, the two lists and the flows should sit together in Figma.** The 43 numbered boxes are now in "Section 34" (node `3089:14571`), which the owner moved. The green lists and the flows are still in "Create Epics, Features, Tasks." Choices: leave them apart, or move one group. The owner decides.
5. **Merging pull request 55.** Merging is the owner's. Pull request 54 was merged with only its first commit, so the flows, backlog and reports wait in 55. The next pull request should start from a merged `main`.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Boxes 1 to 4 and the T1 to T4 list | Boxes 5 and 6, then T5 and T6 | The non-functional list follows the lecture's six-part order |
| The Epic 3 pages and flows (the pattern) | Epic 1's six task pages | Same eight headings, INVEST, sources, happy and non-happy paths |
| The 20 stories | The Notion "Feature-Level Use Case Scenarios" headings (eight are empty) | The template asks for stories and use cases under each feature |
| Everything above | The pitch deck | The instructor says the deck summarizes all of it. A happy-path narrative helps here |
| Any change to slices, flows or dates | The release roadmap (`3068:9448`) and the Notion board | The board says to maintain the roadmap |

## 6. First steps
1. Confirm where we are in a few sentences. Run `git status` and `gh pr list --state open`. Start a new branch from `origin/main` for any new commit, once pull request 55 is merged.
2. Read the files in section 8, especially the backlog file, `task-pages-epic-3-2026-11-15.md` and `docs/build-plan-nfr-draft-2026-11-12.md`.
3. Show the owner decisions 1 and 2 in section 4, each explained. Wait for answers.
4. Do iteration 2 item 2 (the repository) only after the owner says go.
5. Do item 3: draft box 6, add T5 and T6, update Figma `3073:8029` with the 8 build plan fixes. Show each before writing.
6. Then items 4 to 7 in order, updating the backlog file and its iteration log after each.
7. Remind the owner to save the work with a pull request, and write a new handoff report before compacting.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory (`MEMORY.md`). The ones most likely to break next:
- **Explain every decision** (what, why, choices, what happens after). Write complete sentences with context.
- **Data first.** Check facts against the three master reports and approved files, and show file and line. Tag Claude's own wording Proposed.
- **Copy Morgan's and Lucy's layout:** text lists in green sections, no tables unless asked.
- **One part at a time. Questions get answers, not edits.** Show text before writing it to Figma or Notion, then read it back.
- **Saved file first, then Figma and Notion.** Names must match in all three.
- **INVEST at task refinement only.** Use the `invest-task-scoping` skill for task pages, one at a time. Grades go in the saved file, not the chat.
- **Never write the owner's "What I Did," "What I Learned" or one-page summary.**
- **Ask before Firecrawl, the browser pane or Chrome.** Never change sharing settings. Never click through a security warning without explicit approval.
- **Do not move the owner's Figma boxes.** The owner reorganizes the board by hand.
- **Explain the reasoning for any structure you propose** (for example, why two flows were joined) at the time, in plain sentences. The owner could not follow a join that had no explanation.
- **Plain words on every diagram label.** No jargon such as "item stays open," no repeating the decision's condition on the arrow after it. Test: would the owner understand the label if it were the only thing on the screen?
- **Laws: never conclude.** Never say "compliant."

## 8. Where things live
- **New files, all in `docs/clean-deliverables/` (the first four were merged in pull request 54; the flows file, the backlog file and the changed task pages file are in pull request 55):** `epics-features-tasks-numbered-2026-11-15.md`, `epic-and-feature-user-stories-2026-11-15.md`, `non-functional-epics-features-tasks-2026-11-15.md`, `task-pages-epic-3-2026-11-15.md`, `task-flows-epic-3-2026-11-15.md`, `week-2-3-remaining-work-backlog-2026-11-15.md`.
- **Earlier approved files:** `epics-features-tasks-2026-11-11.md`, `release-roadmap-2026-11-11.md`, `notion-backlog-2026-11-11.md`, `vision-and-scope-boards-2026-11-10.md`, `docs/risk-profile.md`, `docs/audience-teacher-format-2026-11-04.md`.
- **Three master reports and data tables:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/` (Audience Segmentation, Market Analysis, Competative Analysis). The audience CSV is `Audience Use Cases.csv` under `Data Tables_Audience Segmentation`.
- **Build plan (not committed, on purpose):** `docs/build-plan-nfr-draft-2026-11-12.md`, sources in `docs/sources/build-plan-2026-11-12/`, logged in `docs/sources/INDEX.md`.
- **Figma file `HcDDdEGAnikTImO8v7UPMp`, page "Updated Deliverables":** Create Epics, Features, Tasks `3068:9983`; functional green list `3093:9247`; non-functional green list `3094:9079`; TASK FLOWS (Epic 3) `3097:9079` (link: https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079); the 43 numbered boxes are in Section 34 `3089:14571`; build plan section `3073:8029` (not yet updated with the 8 fixes); roadmap `3068:9448`. The instructor's board copy is `3089:14567`, Morgan's work `3089:9632`, Lucy's work `3089:9631`.
- **Notion (workspace "Orlando's Notion"):** Epics and Features page `cfc9219a469183c6945281ff637f4185`. Epic 3 task pages: 3.1.1 `47c9219a469183f39d35016e94ec08e8`, 3.1.2 `4159219a469181b793ffeaf1b2e3d74d`, 3.1.3 `4159219a46918192bba3c7710c0fe790`, 3.2.1 `4159219a469181a5be2be352b2b768fe`, 3.2.2 `4159219a469181bc9721f77519efe07a`. The six Epic 1 pages are still empty. Submission page "Week 2 and 3 - Product Specifications" `4179219a-4691-8157-976e-dbc20a0a829f` (items 4 and 5 updated 2026-11-15).
- **Git (2026-11-15):** branch `epics-numbered-stories-task-pages-2026-11-15`, last commit before this report `63f500a`, pull request 54 merged (only its first commit, `b938cc3`); pull request 55 open: https://github.com/LDoomD/AI-Development-Residency/pull/55 (no checks). **Uncommitted:** `docs/sources/INDEX.md`, `docs/build-plan-nfr-draft-2026-11-12.md`, `docs/sources/build-plan-2026-11-12/`, and this report. Also untracked and not part of this work: `il.html` and `dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-15. The instructor's rules were read from the owner's copy of the instructor's board (all sections of `3089-14567`, text only, not images). The master report lines were checked on 2026-11-15.
- **Checks run:**
  - The numbered file was compared with the 2026-11-11 file by script: 6 epics, 10 features with audience labels and 27 tasks all match.
  - Figma and Notion were read back after each write: the functional list and trace tags (screenshot), the non-functional section, the 20 stories page, and Notion pages 3.1.1, 3.1.2, 3.1.3, 3.2.1 and 3.2.2.
  - The merged flows were checked in a screenshot after each rewording, and the owner confirmed they make sense.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - The flow-link lines on the Notion pages were relabeled twice (to "Flow 1" and "Flow 2", then to "Part 1" and "Part 2" on pages 3.1.1, 3.1.2 and 3.1.3). Only page 3.1.3 was read back, and only after the first relabel. Pages 3.2.1 and 3.2.2 were not read back after relabeling.
  - Positioning, UVP and problem statements were not reopened.
  - The use case count (22 against 17) is unresolved.
  - Why the 43 boxes moved to Section 34 is unknown, and I did not move them.
  - The size guesses (about 1 week per slice) are not a team's estimate.
  - Lucy's and Morgan's Notion pages were not read; only their Figma boards.
- **How this prevents drift:** Approved and Proposed tags separate decisions from suggestions. First step 3 stops for the owner on the two blocking decisions. The backlog file carries the order and the iteration log. Saved files are the master copies, and names are compared across Figma, Notion and files after each update.
