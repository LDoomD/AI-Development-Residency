# Epic 1 task pages (master copy, started 2026-11-15)

**What this is:** the text of the six Epic 1 task pages in the owner's Notion Kanban board ("Tasks Go Here"), in the same format as the Epic 3 pages (`task-pages-epic-3-2026-11-15.md`): the course's eight headings (Background, User Story, Problems to Solve, Task Goals, Expected Deliverables, Use Cases to Support, Acceptance, Technical Requirements), a definition of done, a business-need line, and full BDD scenarios. This file is the master copy. A Notion page must say the same, word for word, except that the INVEST grades live only in this file.

**Why these pages exist:** the owner decided on 2026-11-15 to do the standard homework and all 11 first tasks (5 in Epic 3, 6 in Epic 1), because the Notion board already holds all 11 cards and the roadmap puts Epic 1 in the second of the next two weeks (`release-roadmap-2026-11-11.md`, `notion-backlog-2026-11-11.md`).

**Rules used on every page:** record-only slices (no invented advice, because the saved research counts how often problems come up but not what helps). Anything in Claude's own words is tagged Proposed. No task flow is drawn for Epic 1 (task flows are bonus homework, and Epic 3's two flows are already done).

**Status:**
| Task | Notion page | Status |
|---|---|---|
| 1.1.1 Having family or paid help that steps in | `4159219a-4691-8136-b33e-dd1edca61ce9` | Approved 2026-11-15 |
| 1.1.2 Coping with guilt and grief, and knowing next steps | `4159219a-4691-81ad-ba5f-d537641f80f8` | Approved 2026-11-15 |
| 1.1.3 Setting limits without guilt or judgment | not written | |
| 1.2.1 Having people who understand to lean on | not written | |
| 1.2.2 Getting through the paperwork to qualify for help | not written | |
| 1.2.3 Feeling close to their partner again | not written | |

---

## Task 1.1.1: Having family or paid help that steps in
Epic 1, feature 1.1 (Audience 1). Approved by the owner on 2026-11-15.

**INVEST (as written):** Independent fail (needs sign-in, the care circle and a table for break records first: an order dependency), Negotiable pass, Valuable pass, Estimable fail ("steps in" is open, and finding or paying for help is unknown), Small fail (the wide version includes finding programs, qualifying and paying), Testable fail. Fix: a record-only slice of about 1 week, where the caregiver records a planned break and who covers it. Size is a guess, not a team estimate.

### Background
Adult children carry the care, often alone, and can't get a break even when help exists. This shows up in 138 posts and threads, the top problem for adult children, read by one person and not double-checked. Only 128 of 341 respite posts describe actually using relief. This task serves Epic 1, business goal 1, with the KPI "% of caregivers who get a real break."

Sources:
- Audience Segmentation Master Report: table 2b, rank 1 (line 104).
- `Audience Use Cases.csv`: lines 4 to 13.
- Competitive Analysis Master Report: table 2a, row 1 (line 64), and finding 4 (line 202).
- `vision-and-scope-boards-2026-11-10.md`: the Audience 1 scope row "Getting real breaks they can afford" and the use case "Getting relatives to cover time off."
- `docs/risk-profile.md`.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1, T4.1.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want family or paid help to step in when I need a break, so that I'm not carrying the care alone with no time off.

### Problems to Solve
"Today, adult children carry the care, often alone, and can't get a break even when help exists." (approved scope row)

### Task Goals
"We want them to have family or paid help that steps in." (`Audience Use Cases.csv`, line 8)

### Expected Deliverables (Proposed)
- A working way to record a break, who covers it and whether it happened, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The caregiver can add a break with start and end dates, choose who covers it (a relative, paid help they name, or no one yet), mark the cover as not asked, asked, confirmed or fell through, and mark whether the break happened, using fake data. Only people in the care circle can see it. All the scenarios below pass. Not included: finding or qualifying for a program, costs, advice on how to ask, and notes about the parent's needs for the helper (those would be a health note).

### Use Cases to Support
Use case "Getting relatives to cover time off" (feature 1.1). Paid help is recorded by name. Finding it, qualifying for it and paying for it are not part of this task. No task flow is drawn for Epic 1.
- Happy path (Proposed): someone steps in and the break happens.
- Non-happy path (Proposed): the cover falls through.

### Acceptance (Proposed)
- The caregiver can add a break they want, with a start and end date.
- They can choose who covers it: a relative, paid help they name, or no one yet.
- They can mark the cover: not asked, asked, confirmed, or fell through.
- After the break they can mark whether it happened.
- Only people in the care circle can see it.
- The record of each break (planned, covered, taken) can be counted, so the KPI "% of caregivers who get a real break" can be measured later.

**Scenario 1: someone steps in (happy path)**
- **USE CASE:** Getting relatives to cover time off (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I have added a break I want
- **WHEN** I choose who covers it: a relative, or paid help I name
- **AND** I record that they confirmed
- **THEN** the break shows as covered
- **AND** it shows who and the dates

**Scenario 2: the break happens (happy path)**
- **USE CASE:** Getting relatives to cover time off (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** a break shows as covered
- **WHEN** the break is over
- **AND** I record that it happened
- **THEN** it shows as taken
- **AND** it shows the date I recorded it

**Scenario 3: the cover falls through (non-happy path)**
- **USE CASE:** Getting relatives to cover time off (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** a break shows as covered by a person
- **WHEN** I record that the cover fell through
- **THEN** the break shows as not covered
- **AND** the earlier person stays visible
- **AND** the break stays on my list

**Scenario 4: someone outside the care circle (non-happy path)**
- **USE CASE:** Getting relatives to cover time off (feature 1.1)
- **AS A:** a person who is not in my parent's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the parent
- **WHEN** I try to open the break list
- **THEN** I cannot see it

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.2.1 (row-level security), T4.1.1 (members see only their own circle) and T4.2.3 (fake data only in Week 4). The approved database list (T2) has no table for break records, so the developer role (Claude Code) decides where it goes. Anything beyond these comes from the developer role later.

---

## Task 1.1.2: Coping with guilt and grief, and knowing next steps
Epic 1, feature 1.1 (Audience 1). Approved by the owner on 2026-11-15.

**INVEST (as written):** Independent fail (needs sign-in first), Negotiable pass, Valuable pass, Estimable fail ("coping" is open and no saved research says what helps), Small fail (counseling, grief resources and support groups are all wide), Testable fail. Fix: a record-only slice of about 1 week, where the caregiver writes how they are holding up and one step they chose. Size is a guess.

### Background
"Burnout, guilt, isolation, grief" is the top forum theme: 210 of 412 Reddit posts (51%) and 50 of 117 forum threads (43%), read by one person and not double-checked. Support groups give comfort, not a break. The saved research counts the problem but not what helps. This task serves Epic 1, business goal 1, with the KPI "% of caregivers who get a real break."

Sources:
- Audience Segmentation Master Report: table 3a, row 1 (line 122), and table 2b, rank 1 (line 104).
- `Audience Use Cases.csv`: lines 4 to 13.
- Competitive Analysis Master Report: table 2a, row 1 (line 64), and the support groups row (line 141).
- `vision-and-scope-boards-2026-11-10.md`: the Audience 1 scope row "Getting real breaks they can afford" and the use case "Handling guilt and setting limits they can keep."
- `docs/risk-profile.md`: no saved rule covers a caregiver's own feelings (open item).
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want to write down how I'm holding up and one step I'll take, so that guilt and grief don't build up with nothing done about them.

### Problems to Solve
"Today, adult children carry the care, often alone, and can't get a break even when help exists." (approved scope row)

### Task Goals
"We want them to cope with guilt and grief, and know next steps." (`Audience Use Cases.csv`, line 9)

### Expected Deliverables (Proposed)
- A working way to write how the caregiver is doing and one next step, and mark the step, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The caregiver can write how they are doing in their own words with a date, write one next step they chose, and mark it not started, done or not done, using fake data. Only the person who wrote it can see it. All the scenarios below pass. Not included: advice on how to cope, referrals to counselors, grief resources, support groups, and any crisis help.

### Use Cases to Support
Use case "Handling guilt and setting limits they can keep" (feature 1.1). No task flow is drawn for Epic 1.
- Happy path (Proposed): they write a check-in and do the step.
- Non-happy path (Proposed): the step is not done.

### Acceptance (Proposed)
- The caregiver can write how they are doing, with a date.
- They can write one next step they chose for themselves.
- They can mark the step: not started, done, or not done.
- Only the person who wrote it can see it, not other members of the care circle.
- Deleting the caregiver deletes their check-ins.
- The record of check-ins and steps (done or not done) can be counted, so the KPI "% of caregivers who get a real break" can be measured later.

**Scenario 1: I write a check-in and a next step (happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **WHEN** I write how I am doing
- **AND** I write one next step
- **THEN** both are saved with the date
- **AND** only I can see them

**Scenario 2: I do the step (happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I have a next step marked not started
- **WHEN** I mark it done
- **THEN** it shows as done
- **AND** it shows the date I marked it

**Scenario 3: I don't do the step (non-happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I have a next step marked not started
- **WHEN** I mark it not done
- **THEN** it shows as not done
- **AND** my first check-in stays visible
- **AND** I can write a new next step

**Scenario 4: another member of my care circle (non-happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** another member of the care circle
- **GIVEN** I am signed in
- **WHEN** I try to open the caregiver's check-ins
- **THEN** I cannot see them

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.2.1 (row-level security) and T4.2.3 (fake data only in Week 4). The rule "visible only to the person who wrote it" is not in the approved list, so it is a proposed new rule, open for the owner's decision. Anything beyond these comes from the developer role (Claude Code) later.

---

## Open items from these pages
- **Privacy of a caregiver's own feelings (1.1.2).** "Visible only to the writer" is proposed, not approved as a non-functional rule. A caregiver's own mental-health notes may fall under state health-data laws, and the risk profile does not cover them. Needs a lawyer.
- **Crisis safety (1.1.2).** What the screen shows if someone writes about harming themselves is not decided. It is a safety and legal question for the developer role and a lawyer. No advice text is written.
- **A table for break records (1.1.1)** is not in the approved database list. The developer role decides.
- **Research on what helps** a caregiver cope, and on how to ask relatives or paid helpers, is not saved. No advice text is written until it is.
- **Size estimates** (about 1 week each) are guesses, not a team's.
