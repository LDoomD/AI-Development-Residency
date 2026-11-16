# Feature user stories and use cases: Epic 3 (simplified 2026-11-15, owner approved)

**What this is:** the feature-level user story and the use cases for the two features under Epic 3, "Increase how often a parent or partner accepts outside help." The course's Notion "Epics and Features" template asks for a "Feature-Level User Story" and "Feature-Level Use Case Scenarios" under every feature, and gives no count or format. This file is the master copy. Any copy elsewhere must say "same as this file, [date]" and match it word for word.

**Where it lives:** in this file only. Figma is not changed: the epics, features and tasks stay exactly as the instructor's Figma template shows them (the five boxes I added on 2026-11-15 were removed the same day because they looked like features and are not in the template).

**History:** the first version (also 2026-11-15) had a When, Happy path and Non-happy path table for every use case. The owner questioned that layout. The course materials show those paths belong at task level (lecture 1:02:56 to 1:06:23 and the lecture notes), and neither Morgan's nor Lucy's nor the telehealth student's epics pages have them at feature level. The paths are kept in the last section for the task-level requirements.

## How many use cases
The course sets no number. The lecture says a use case is "usually just one statement" and that a ticket "might have one to three or four." Rule used here: each feature lists the use cases from `vision-and-scope-boards-2026-11-10.md` that belong to it, so every use case appears once across the epics and the total reconciles with the Vision and Scope (11 for Audience 1 plus 6 for Audience 2, 17 in all). Epic 3 holds 3 of the 17.

## Who wrote what
| Part | Source | Tag |
|---|---|---|
| Epic, feature and task wording | `epics-features-tasks-2026-11-11.md` | Approved 2026-11-11 |
| Use case names | `vision-and-scope-boards-2026-11-10.md`, lines 97 to 108 (Audience 1) and 168 to 174 (Audience 2), and the owner's Figma "Updated Deliverables" page | Fact |
| Scenarios listed under a use case | Audience use cases table, `docs/audience-teacher-format-2026-11-04.md` lines 44 and 88, confirmed in the raw Figma text on 2026-11-15 | Fact |
| "Respects the parent's choices" in the Feature 1 story | Competitive Analysis Master Report, section 4, table 2b, need 4 | Fact |
| The two user story sentences | Written by Claude from the sources above | Proposed wording, approved by the owner on 2026-11-15 |

User story format: "As a [audience], I want [goal] so that [problem or value, not the solution]" (lecture 57:39 to 1:00:10).

## Feature 1: Getting the parent to accept doctors or help (Audience 1)

**Feature-level user story:** As an adult child caring for a parent, I want my parent to get the doctors and help they need, with their own choices respected, so that they stay safe and comfortable.

**Tasks (unchanged):** Seeing the parent take care of their health. Getting the parent to accept a safer move. Finding next steps the parent will accept.

**Use cases to support:**
1. Adult children getting the parent to accept outside help.
2. Adult children trying small steps when the answer is no. This also covers the audience table's scenario "Help them keep going after a refusal."

## Feature 2: Bringing in outside help the partner accepts (Audience 2)

**Feature-level user story:** As a spouse or partner caring for my partner, I want my partner to get the help they need, so that they stay safe, comfortable and with dignity.

**Tasks (unchanged):** Planning together without causing anger. Settling who handles care tasks and money.

**Use cases to support:**
1. Spouses bringing in help the partner will accept. It has three scenarios from the audience table: bring in help the partner will accept, raise hard topics without a fight, and agree on who does what.

## Decision on four scenarios (2026-11-15; the owner said to decide from the data)
Four scenarios are in the audience table and on the board but were not placed on the use case priority grid and are not in the Vision and Scope list (0 hits in the grid section of the raw Figma text).

| Scenario | Decision | Data behind it |
|---|---|---|
| Help them raise hard topics without a fight (Audience 2) | Supported, as a scenario under the use case "Spouses bringing in help the partner will accept" | It sits beside the "we want" line "plan together without causing anger," which is Feature 2, task 1. |
| Help them agree on who does what (Audience 2) | Supported, as a scenario under the same use case | It sits beside "settle who handles care tasks and money," which is Feature 2, task 2. Without it an approved task has no supported situation. |
| Help them keep going after a refusal (Audience 1) | Covered by the use case "Trying small steps when the answer is no" | Its non-happy path is a refusal that happens again. |
| Help them know when to step in for safety (Audience 1) | **Supported in MVP #1 (owner decision, later on 2026-11-15; replaces "Not in MVP #1, candidate for MMP").** Placed under Feature 1, task "Getting the parent to accept a safer move" (Claude's reading, Proposed). | It sits in the same audience-table group as that task (`docs/sources/market-analysis-3/audience-v2/uc-A1.json`). It was not on the priority grid. It pulls against need 4 in the competitive report, "respects the parent's choices," so its wording must keep the parent's choices respected. |

**Owner decision, later on 2026-11-15 (Approved):** all four scenarios count as supported in MVP #1. Still to do: add them to the use case lists in `vision-and-scope-boards-2026-11-10.md` (not changed yet). Figma has an extra section, "EPIC 3: FEATURE STORIES AND USE CASES" (node `3109:9375`), added the same day at the owner's yes. It differs from this file (it shows happy and non-happy paths at feature level), and the owner has not yet decided whether it stays.

The pairing of each scenario with a "we want" line rests on their order and wording in the audience table. The audience master report lists them as separate columns and does not say they pair one to one, so the pairing is Claude's reading (Proposed).

## Moved to other epics (checked in the audience table)
- "Preparing for a hard talk" belongs to Epic 4 (the problem about a parent's anger and big talks).
- "Asking for specific help" belongs to Epic 2 (the spouse problem about family and friends who criticize).

## Kept for task-level requirements (not feature level)
These are Claude's wording (Proposed). They are kept for when full requirements are written for the key tasks in the Notion backlog cards, as the lecture's 13 Notion steps (steps 12 and 13) and the telehealth student's "golden-path" approach do.

| | Getting the parent to accept outside help | Trying small steps when the answer is no |
|---|---|---|
| When | The parent turns down paid help or aids. | The parent refuses doctors, treatment or medicine, or won't change habits or do therapy. |
| Happy path | The parent agrees to try the help. | The parent accepts one small step. |
| Non-happy path | The parent says no. The next use case applies. | The parent refuses again. |

| | Bringing in help the partner will accept | Raising hard topics without a fight | Agreeing on who does what |
|---|---|---|---|
| When | The partner refuses a helper. | The partner denies needs or resists reminders. | The partner puts off medical care or big changes. |
| Happy path | The partner agrees to a helper. | The caregiver and the partner talk about the topic without it turning into a fight. | The caregiver and the partner agree who handles each care task and the money. |
| Non-happy path | The partner refuses. | The talk turns into a fight. | They cannot agree. |

The audience table lists three situations and three scenarios for the partner problem but does not pair them. The pairing in the "When" row above is Claude's reading.

## Known limits
- Audience 2's problem here appears in only 9 posts and threads, so Feature 2 rests on thin evidence (Audience Segmentation Master Report, table 2b).
- Counts come from online posts, read by one person and not double-checked (both master reports).
- The tasks are outcome phrases and have not been checked against INVEST. That check comes when each task's own requirements are written.
- The Vision and Scope still lists 6 Audience 2 use cases. This file keeps that count by placing the two extra scenarios under an existing use case.

Read: the audience use cases table, the vision and scope file, the three master reports, the epics file, the lecture notes and transcript sections on user stories and use cases, the Epics and Features template, and Morgan's and Lucy's and the telehealth student's epics pages.
