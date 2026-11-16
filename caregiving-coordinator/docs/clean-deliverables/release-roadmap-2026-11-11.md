# Release roadmap for MVP #1 (Approved 2026-11-11)

**What this is:** the owner's release roadmap for the vision board section "Create your Release Roadmap Based on Your Epics, Features, and Tasks" (board `PQFzfyqTUQhAgEEe1P6ygs`, node 22:6807; calendar 22:4543). It's saved here first, and copied to the board only after the owner approves.

**On the board (written 2026-11-11, read back word for word, 0 overlaps):** calendar 22:4543. The instructor's example row is kept. The 4 empty rows hold epics 3, 1, 4 and 5, and 2 copied rows hold epics 6 and 2 (the calendar and its section grew by 1,824 to fit). Each feature shows its audience. Each task is a 1-week bar in its epic's week. The calendar's week labels come from an older year, so the nearest columns are used: 11/17, 11/24, 12/01, 12/08 and 12/15.

**Where it came from:** the 6 epics, 10 features and 27 tasks in `epics-features-tasks-2026-11-11.md` (Approved 2026-11-11). The dates are the owner's plan, not research.

## The rules used (Approved by the owner, 2026-11-11)

| Choice | Decision | Why |
|---|---|---|
| Keep the roadmap? | Yes | Week 2 and 3 objective 3: "organize the work in a prioritized backlog and roadmap" (`.claude/skills/residency-context/reference/week-2-3.md`, line 23) |
| Time window | The rest of the residency, Nov 16 to Dec 18, 2026 | Lecture: "I need a vision of three weeks from now, six weeks from now, 10 weeks from now" (42:37 to 42:43). Residency calendar in `syllabus.md`. |
| Holiday week (Nov 23, no class) | Used for work | Owner's choice |
| Epic order | The Top square first, then by how often caregivers wrote about the problem | Part 2 problem grid (Epic 3 is the only Top square); audience table 2b rank |
| Task length | 1 week per task; both audiences' features run side by side | INVEST "Small": done in 1 or 2 weeks (lecture 55:43) |

## Epic order

| Order | Epic | Why it's here |
|---|---|---|
| 1 | Epic 3: Increase how often a parent or partner accepts outside help. | The only Top square |
| 2 | Epic 1: Remove the barriers that keep caregivers from getting a real break. | Rank 1 for both audiences |
| 3 | Epic 4: Make personal, ongoing guidance reachable without an employer or a high hourly bill. | Rank 2 for both audiences |
| 4 | Epic 5: Make the money, papers and accounts manageable, even when nothing was prepared ahead. | Rank 3 for Audience 1 |
| 5 | Epic 6: Protect caregivers' own health, job and money while they care. | Rank 5 for Audience 2 |
| 6 | Epic 2: Make sure caregivers don't carry the care alone, with relatives sharing the work. | Rank 6 for both audiences |

## The roadmap

| Week | Epic | Features (tasks run all week) |
|---|---|---|
| Nov 16 to 20 | Epic 3 | Getting the parent to accept doctors or help *(A1, 3 tasks)*; Bringing in outside help the partner accepts *(A2, 2 tasks)* |
| Nov 23 to 27 (no class) | Epic 1 | Getting real breaks they can afford *(A1, 3 tasks)*; Getting real breaks and a life outside caring *(A2, 3 tasks)* |
| Nov 30 to Dec 4 | Epic 4 | Calming outbursts and calls, and staying calm themselves *(A1, 3 tasks)*; Understanding the behavior and how to respond *(A2, 2 tasks)* |
| Dec 7 to 11 | Epic 5 and Epic 6 | Having legal authority and papers sorted in time *(A1, 3 tasks)*; Protecting their money and avoiding debt *(A2, 3 tasks)* |
| Dec 14 to 18 | Epic 2 | Having siblings share the care and costs *(A1, 3 tasks)*; Having relatives who support, not criticize *(A2, 2 tasks)* |

The task names are in `epics-features-tasks-2026-11-11.md`, word for word.

## Update 2026-11-16 (Proposed, added under the owner's instruction to finish the roadmap)

**What changed on the board:** one new row, "FOUNDATION (Proposed)," was added at the bottom of the roadmap calendar in Figma (section "Your Release Roadmap," node `3068:9449`, new nodes `3120:9605` to `3120:9625`). The existing rows, dates and tasks were not moved or edited. The calendar's column stripes and the section grew by 912 to fit the row.

**What did not change:** the six epics, their order, the weeks, and the 27 task names. I checked them against `epics-features-tasks-numbered-2026-11-15.md` and the Figma calendar (all 27 task bars read and compared name by name on 2026-11-16). The 11 tasks in the first two weeks (5 in Epic 3, 6 in Epic 1) are the same tasks that now have full pages in `task-pages-epic-3-2026-11-15.md` and `task-pages-epic-1-2026-11-15.md`.

**Why a Foundation row:** each of the 11 task pages needs shared groundwork first. The INVEST lines on the pages say so: for example "needs sign-in, the care circle and a table for break records first" (1.1.1) and "needs sign-in, care circle, consent records and the care notes table first" (3.1.2). That groundwork is the non-functional list T1 to T6 in `non-functional-epics-features-tasks-2026-11-15.md`, which the roadmap built on 2026-11-11 did not yet have.

| Bar | Week on the board | Why this week |
|---|---|---|
| T1 Tools and hosting, T2 Database, T3 System architecture, T4 Security protocol | Nov 16 to 20 | Epic 3, the first epic, depends on sign-in, the care circle, consent records and its tables. The course's Week 6 starts Nov 16 on information security (`syllabus.md`, line 147). |
| T5 Development operations, T6 Quality engineering | Nov 23 to 27 | The checks that run on every push and the hand-run test scenarios are needed before the second epic's work is called done. |

The weeks for the Foundation bars are the same kind of forecast as the epics' weeks: my proposal, not research. Bar names are the T group names from the non-functional list, word for word. No task cards were added to the Notion board for them, because the board holds only the first two weeks of epic work and the Foundation tasks have no pages yet (the developer role writes those).

## Known limits
- The dates are a forecast. The board says to change the roadmap when plans change (node 23:1637), and the lecture says the backlog and roadmap will change after each release (42:02 to 42:12).
- The busiest weeks hold 6 tasks. The class weeks also have their own coding challenges (`syllabus.md`).
- The tasks aren't sized with INVEST yet. "1 week per task" is a starting estimate.
- Order rank 4 to 6 compares ranks from different audiences (Audience 1 rank 3, Audience 2 rank 5, both rank 6).
