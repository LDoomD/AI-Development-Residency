# Epic 1 task pages (master copy, started 2026-11-15)

**What this is:** the text of the six Epic 1 task pages in the owner's Notion Kanban board ("Tasks Go Here"), in the same format as the Epic 3 pages (`task-pages-epic-3-2026-11-15.md`): the course's eight headings (Background, User Story, Problems to Solve, Task Goals, Expected Deliverables, Use Cases to Support, Acceptance, Technical Requirements), a definition of done, a business-need line, and full BDD scenarios. This file is the master copy. A Notion page must say the same, word for word, except that the INVEST grades live only in this file.

**Why these pages exist:** the owner decided on 2026-11-15 to do the standard homework and all 11 first tasks (5 in Epic 3, 6 in Epic 1), because the Notion board already holds all 11 cards and the roadmap puts Epic 1 in the second of the next two weeks (`release-roadmap-2026-11-11.md`, `notion-backlog-2026-11-11.md`).

**Rules used on every page:** record-only slices (no invented advice, because the saved research counts how often problems come up but not what helps). Anything in Claude's own words is tagged Proposed. No task flow is drawn for Epic 1 (task flows are bonus homework, and Epic 3's two flows are already done).

**Status:**
| Task | Notion page | Status |
|---|---|---|
| 1.1.1 Having family or paid help that steps in | `4159219a-4691-8136-b33e-dd1edca61ce9` | Approved 2026-11-15 |
| 1.1.2 Coping with guilt and grief, and knowing next steps | `4159219a-4691-81ad-ba5f-d537641f80f8` | Approved 2026-11-15 |
| 1.1.3 Setting limits without guilt or judgment | `4159219a-4691-81c1-8b02-c76cb46c35c4` | Approved 2026-11-15 |
| 1.2.1 Having people who understand to lean on | `4159219a-4691-813b-8a57-c73044940a60` | Approved 2026-11-15 |
| 1.2.2 Getting through the paperwork to qualify for help | `4159219a-4691-81fc-9cd8-dd627cde0606` | Approved 2026-11-15 |
| 1.2.3 Feeling close to their partner again | `4159219a-4691-81ab-bf15-d45cf8e518bf` | Approved 2026-11-15 |

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
**Approved rules (from the non-functional list):** T2.2.1 (row-level security), T4.1.1 (members see only their own circle), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** a new table `care_breaks`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, care circle, who created it, start date, end date, who covers it (a relative, paid help the caregiver names, or no one yet), the covering circle member (only for a relative), the covering name (only for paid help), cover status (not asked, asked, confirmed or fell through) and the time it last changed, break outcome (not yet, happened or did not happen) and the time it was recorded, and created. Left out, as the page says: costs, finding or qualifying for a program, and notes about the parent's needs.
- **Access:** circle members can read a break (T2.2.1, T4.1.1), and people outside the circle get nothing. Only the caregiver who created a break can add or change it. The private-records rule T4.1.4 does not apply here, because a break is shared with the circle by design.
- **Deletion:** the page has no deletion line, so this is new. Deleting the cared-for person or the circle deletes its breaks, and deleting the caregiver who created a break deletes it too.
- **Date last changed:** changing the cover status or the outcome sets its time from the server's clock. When the cover falls through, the earlier person or name stays visible. Only the latest change is kept; there is no separate history table for now.
- **Counting:** numbers per caregiver for breaks planned, covered (confirmed) and taken (happened). For now, "a real break" means a break marked happened. This is an assumption to check after Week 4.
- **Checks:** adding a break with a start and end date; choosing who covers it (all three choices work, and a bad choice is rejected); changing the cover status and the outcome moves the date; a fake person outside the circle sees an empty list and cannot add or change a break; the count function returns the right numbers.

**Open (not decided here):** what counts as "a real break" for the KPI.

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
As an adult child caring for a parent, I want to cope with my guilt and grief and know what to do next, so that I don't carry them alone until I burn out.

### Problems to Solve
"Today, adult children carry the care, often alone, and can't get a break even when help exists." (approved scope row)

### Task Goals
"We want them to cope with guilt and grief, and know next steps." (`Audience Use Cases.csv`, line 9)

### Expected Deliverables (Proposed)
- A working way for the caregiver to record how they are holding up and one next step, and keep track of whether it was done, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The caregiver can record how they are holding up in their own words with a date, choose one next step, and see and change whether it is not started, done or not done, using fake data. Only the person who wrote it can see it. All the scenarios below pass. Not included: advice on how to cope, referrals to counselors, grief resources, support groups, and any crisis help.

### Use Cases to Support
Use case "Handling guilt and setting limits they can keep" (feature 1.1). No task flow is drawn for Epic 1.
- Happy path (Proposed): they write a check-in and do the step.
- Non-happy path (Proposed): the step is not done.

### Acceptance (Proposed)
- The caregiver can record how they are holding up, in their own words, and see the date they recorded it.
- The caregiver can choose one next step for themselves and keep it with that record.
- The caregiver can see whether their step is not started, done or not done, and can change that status.
- After a step is marked not done, the caregiver can still see their earlier record and can choose a new step.
- No one else, including other members of the care circle, can see what the caregiver recorded.
- If the caregiver is deleted, everything they recorded is deleted with them.
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
**Approved rules (from the non-functional list):** T2.2.1 (row-level security on every table), T2.2.3 (deleting the caregiver deletes what they entered), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** records go in the shared table `private_records`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, owner, kind, parent record, text in the person's own words, contact note, date, status, the time the status last changed, and created. This task uses kind `check_in` (text and date) and kind `check_in_step` (text, the check-in it belongs to, and a status of not started, done or not done). The database allows only those statuses for that kind.
- **Access:** only the owner can read, add, change or delete these rows. There is no link to a care circle, so nothing can leak through circle membership. A denied read shows nothing, as if the record does not exist. This depends on T4.1.4, which is still Proposed and open for a lawyer.
- **Deletion:** deleting the caregiver deletes all their rows in one step, and deleting a record deletes its steps.
- **Date last changed:** every status change sets the time from the server's clock, not the browser's. Only the latest change is kept; there is no separate history table for now.
- **Counting:** a database function returns numbers only (for example, rows per kind per status), never the text. Whether anyone may count private rows is still open.
- **Checks:** a second fake user in the same fake circle sees zero of these rows and cannot add, change or delete them; deleting the fake owner leaves zero rows; the count function returns the right numbers and no text; changing a step's status moves its date; after a step is marked not done, the first check-in stays and a new step can be added.

**Open (not decided here):** what the screen shows if someone writes about harming themselves (no approved rule; a safety and legal question and a launch blocker), and whether a caregiver's own mental-health notes fall under state health-data laws (a lawyer's question).

---

## Task 1.1.3: Setting limits without guilt or judgment
Epic 1, feature 1.1 (Audience 1). Approved by the owner on 2026-11-15.

**INVEST (as named):** Independent fail (needs sign-in and private records first; a build-order dependency), Negotiable pass, Valuable pass (supports the KPI "% of caregivers who get a real break"), Estimable fail ("limits" is open and no saved research says which limits help), Small fail (talks with the parent, scripts and messages to relatives are all wide), Testable fail. Fix: a record-only slice of about 1 week, where the caregiver records the limits they choose and whether each was kept. After the cut: Independent still fails (build order), the other five pass. Size is a guess.

### Background
"Burnout, guilt, isolation, grief" is the top forum theme: 210 of 412 Reddit posts (51%) and 50 of 117 forum threads (43%), read by one person and not double-checked. Adult children carry the care, often alone, and the audience table asks for help to "set limits without guilt or judgment." The saved research counts the problem but not what helps. This task serves Epic 1, business goal 1, with the KPI "% of caregivers who get a real break."

Sources:
- Audience Segmentation Master Report: table 3a, row 1 (line 122), table 2b, rank 1 (line 104), and table 2a, motivation 2 (line 93).
- `Audience Use Cases.csv`: lines 4 to 13, with the goal on line 10 and the scenario on line 13.
- `vision-and-scope-boards-2026-11-10.md`: the use case "Handling guilt and setting limits they can keep" (line 101) and the scope row (line 116).
- `docs/risk-profile.md`: no saved rule covers a caregiver's own notes (open item).
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want to set limits on what I take on without guilt or judgment, so that I don't take on more than I can keep up.

### Problems to Solve
"Today, adult children carry the care, often alone, and can't get a break even when help exists." (approved scope row)

### Task Goals
"We want them to set limits without guilt or judgment." (`Audience Use Cases.csv`, line 10)

### Expected Deliverables (Proposed)
- A working way for the caregiver to record the limits they choose and keep track of whether each one was kept, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The caregiver can record one or more limits for themselves in their own words with a date, and see and change whether each is not tried yet, kept or not kept, using fake data. Only the person who recorded them can see them. All the scenarios below pass. Not included: advice on which limits to set, scripts, messages to the parent or relatives, referrals to counselors, and any crisis help.

### Use Cases to Support
Use case "Handling guilt and setting limits they can keep" (feature 1.1). No task flow is drawn for Epic 1.
- Happy path (Proposed): they record a limit and keep it.
- Non-happy path (Proposed): the limit is not kept.

### Acceptance (Proposed)
- The caregiver can record a limit for themselves, in their own words, and see the date they recorded it.
- The caregiver can record more than one limit.
- The caregiver can see whether each limit is not tried yet, kept or not kept, and can change that status.
- A limit marked not kept is shown without wording that blames or shames the caregiver.
- After a limit is marked not kept, the caregiver can still see it and can change it or record a new one.
- No one else, including other members of the care circle, can see what the caregiver recorded.
- If the caregiver is deleted, everything they recorded is deleted with them.
- The record can be counted, so the KPI "% of caregivers who get a real break" can be measured later.

**Scenario 1: I record a limit (happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **WHEN** I record a limit in my own words
- **THEN** it is saved with the date
- **AND** only I can see it

**Scenario 2: I keep the limit (happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I have a limit marked not tried yet
- **WHEN** I mark it kept
- **THEN** it shows as kept
- **AND** it shows the date I marked it

**Scenario 3: I don't keep the limit (non-happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I have a limit marked not tried yet
- **WHEN** I mark it not kept
- **THEN** it shows as not kept
- **AND** the limit stays visible
- **AND** I can change it or record a new one
- **AND** nothing on the screen blames me

**Scenario 4: another member of my care circle (non-happy path)**
- **USE CASE:** Handling guilt and setting limits they can keep (feature 1.1)
- **AS A:** another member of the care circle
- **GIVEN** I am signed in
- **WHEN** I try to open the caregiver's limits
- **THEN** I cannot see them

### Technical Requirements
**Approved rules (from the non-functional list):** T2.2.1 (row-level security on every table), T2.2.3 (deleting the caregiver deletes what they entered), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** records go in the shared table `private_records`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, owner, kind, parent record, text in the person's own words, contact note, date, status, the time the status last changed, and created. This task uses kind `limit` (text, date and a status of not tried yet, kept or not kept). The database allows only those statuses for that kind. Marking a limit not kept does not delete or lock it.
- **Access:** only the owner can read, add, change or delete these rows. There is no link to a care circle, so nothing can leak through circle membership. A denied read shows nothing, as if the record does not exist. This depends on T4.1.4, which is still Proposed and open for a lawyer.
- **Deletion:** deleting the caregiver deletes all their rows in one step.
- **Date last changed:** every status change sets the time from the server's clock, not the browser's. Only the latest change is kept; there is no separate history table for now.
- **Counting:** a database function returns numbers only (for example, rows per kind per status), never the text. Whether anyone may count private rows is still open.
- **Checks:** a second fake user in the same fake circle sees zero of these rows and cannot add, change or delete them; deleting the fake owner leaves zero rows; the count function returns the right numbers and no text; changing a limit's status moves its date; a limit marked not kept can still be changed or replaced; a person checks that nothing on the screen blames the caregiver.

**Open (not decided here):** whether a caregiver's own notes fall under state health-data laws (a lawyer's question).

**Assumptions to check when it is built (agile):** caregivers will actually record limits, and one week is the right size.

---

## Task 1.2.1: Having people who understand to lean on
Epic 1, feature 1.2 (Audience 2). Approved by the owner on 2026-11-15.

**INVEST (as named):** Independent fail (needs sign-in and private records first; a build-order dependency), Negotiable pass, Valuable pass (serves the audience's need for people who understand; supports the Epic 1 KPI only indirectly, because support groups "give comfort, not a break," Competitive Analysis Master Report line 141), Estimable fail (who the "people" are is open and no saved research says what works), Small fail (matching people, running groups or chat are each wide), Testable fail. Fix: a record-only slice of about 1 week, where the spouse keeps a short list of people or groups who understand and records when they last reached out. After the cut: Independent still fails (build order), the other five pass. Size is a guess.

### Background
"Burnout, guilt, isolation, grief" is the top forum theme: 210 of 412 Reddit posts (51%) and 50 of 117 forum threads (43%), read by one person and not double-checked. Spouses carry the care, often alone, and this is their rank 1 problem (45 posts and threads). Support groups give comfort, not a break. The saved research counts the problem but not what kind of support helps. This task serves Epic 1, business goal 1, and supports its KPI "% of caregivers who get a real break" only indirectly.

Sources:
- Audience Segmentation Master Report: table 3a, row 1 (line 122), and table 2b, rank 1 (line 104).
- `Audience Use Cases.csv`: lines 107 to 115, with the goal on line 110 and the scenario on line 113.
- Competitive Analysis Master Report: the support groups rows (lines 108 and 141).
- `vision-and-scope-boards-2026-11-10.md`: the use case "Finding a support group or someone who understands" (line 171) and the scope row (line 182).
- `docs/risk-profile.md`: no saved rule covers a caregiver's own notes or other people's details (open item).
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As a spouse or partner caring for my partner, I want people who understand what this is like to lean on, so that I don't carry it alone and wear myself down.

### Problems to Solve
"Today, spouses carry the care, often alone, and lose health, sleep, closeness and breaks." (approved scope row)

### Task Goals
"We want them to have people who understand to lean on." (`Audience Use Cases.csv`, line 110)

### Expected Deliverables (Proposed)
- A working way for the spouse to keep a short list of people or groups who understand, and record when they last reached out, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The spouse can add a person or group who understands (a name and a note on how to reach them, in their own words), record the date they last reached out, and change or remove an entry, using fake data. Only the person who recorded them can see them. All the scenarios below pass. Not included: finding new groups or people, matching, chat, advice on who to lean on, referrals to counselors, and any crisis help.

### Use Cases to Support
Use case "Finding a support group or someone who understands" (feature 1.2). No task flow is drawn for Epic 1. This slice covers recording people the spouse already knows. Finding new groups is a later piece.
- Happy path (Proposed): they add someone and record reaching out.
- Non-happy path (Proposed): the person is no longer someone they can lean on, so they remove or change the entry.

### Acceptance (Proposed)
- The spouse can record a person or group who understands what caring is like, in their own words, with a note on how to reach them.
- The spouse can record more than one.
- The spouse can record the date they last reached out to each, and change it.
- The spouse can change or remove an entry at any time.
- No one else, including other members of the care circle and the people on the list, can see what the spouse recorded.
- If the spouse is deleted, everything they recorded is deleted with them, including the names and notes about other people.
- The record can be counted (how many entries and reach-outs), so use can be measured later.

**Scenario 1: I add someone who understands (happy path)**
- **USE CASE:** Finding a support group or someone who understands (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **WHEN** I record a person or group who understands, in my own words
- **THEN** it is saved
- **AND** only I can see it

**Scenario 2: I reach out (happy path)**
- **USE CASE:** Finding a support group or someone who understands (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have someone on my list
- **WHEN** I record that I reached out today
- **THEN** the entry shows the date I last reached out

**Scenario 3: they are no longer someone I can lean on (non-happy path)**
- **USE CASE:** Finding a support group or someone who understands (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have someone on my list
- **WHEN** I remove that entry
- **THEN** it no longer appears
- **AND** the rest of my list stays as it was

**Scenario 4: another member of my care circle (non-happy path)**
- **USE CASE:** Finding a support group or someone who understands (feature 1.2)
- **AS A:** another member of the care circle
- **GIVEN** I am signed in
- **WHEN** I try to open the spouse's list
- **THEN** I cannot see it

### Technical Requirements
**Approved rules (from the non-functional list):** T2.2.1 (row-level security on every table), T2.2.3 (deleting the caregiver deletes what they entered), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** records go in the shared table `private_records`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, owner, kind, parent record, text in the person's own words, contact note, date, status, the time the status last changed, and created. This task uses kind `support_person` (text for the name of the person or group, a contact note in the spouse's own words, and the date last reached out, empty until then). It has no status.
- **Access:** only the owner can read, add, change or delete these rows. The people listed cannot see them, and they are not users of the app. There is no link to a care circle. A denied read shows nothing, as if the record does not exist. This depends on T4.1.4, which is still Proposed and open for a lawyer.
- **Deletion:** deleting the spouse deletes all their rows in one step, including the names and notes about other people. Removing one entry deletes only that row.
- **Date last changed:** the date last reached out is stored as the latest date only.
- **Counting:** a database function returns numbers only (for example, how many entries and how many have a reach-out date), never the text. Whether anyone may count private rows is still open.
- **Checks:** a second fake user in the same fake circle sees zero of these rows and cannot add, change or delete them; deleting the fake owner leaves zero rows; the count function returns the right numbers and no text; removing one entry leaves the rest of the list unchanged.

**Open (not decided here):** keeping other people's names and contact notes is not covered by the approved list or the risk profile (a lawyer's question), and counting reach-outs over time would need a history table, which is not added for now.

**Assumptions to check when it is built (agile):** spouses will keep such a list, finding new people may matter more to them than recording people they already know, and one week is the right size.

---

## Task 1.2.2: Getting through the paperwork to qualify for help
Epic 1, feature 1.2 (Audience 2). Approved by the owner on 2026-11-15.

**INVEST (as named):** Independent fail (needs sign-in and private records first; a build-order dependency), Negotiable pass, Valuable pass (paperwork blocks the break for spouses, so it serves the Epic 1 KPI directly), Estimable fail (programs differ and no saved research holds their rules), Small fail (explaining eligibility and filing forms for each program are each wide), Testable fail. Fix: a record-only slice of about 1 week, where the spouse records the program they are applying to, the steps they need to do and where each stands. After the cut: Independent still fails (build order), the other five pass. Size is a guess.

### Background
Spouses carry the care, often alone, and this is their rank 1 problem (45 posts and threads, read by one person and not double-checked). The audience table names the blocker: "paperwork and rules, often the VA's" block a break. The competitive report says VA caregiver programs help only veterans' families who qualify, and Medicaid and state programs bring "paperwork errors, income and asset rules, waits that can run for years." The saved research counts the problem but holds no eligibility rules and no evidence of what helps. This task serves Epic 1, business goal 1, and its KPI "% of caregivers who get a real break."

Sources:
- Audience Segmentation Master Report: table 2b, rank 1 (line 104).
- `Audience Use Cases.csv`: lines 107 to 115, with the moment on line 108, the goal on line 112 and the scenario on line 114.
- Competitive Analysis Master Report: the VA row (line 139) and the Medicaid row (line 140).
- `vision-and-scope-boards-2026-11-10.md`: the use case "Qualifying for help, including VA programs" (line 170) and the scope row (line 182).
- `docs/risk-profile.md`: benefits and coverage details are data about someone who didn't sign up (line 21).
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As a spouse or partner caring for my partner, I want to get through the paperwork to qualify for help, so that paperwork and waiting don't stop me from getting the break I need.

### Problems to Solve
"Today, spouses carry the care, often alone, and lose health, sleep, closeness and breaks." (approved scope row)

### Task Goals
"We want them to get through the paperwork to qualify for help." (`Audience Use Cases.csv`, line 112)

### Expected Deliverables (Proposed)
- A working way for the spouse to record a program they are applying to and the steps they need to do, and keep track of where each step stands, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The spouse can record a program they are applying to (a name, in their own words), add the steps they need to do (in their own words), and see and change where each step stands, with the date they last changed it, using fake data. Only the person who recorded them can see them. All the scenarios below pass. Not included: eligibility rules, what a program offers, filling in or sending forms, any link to the VA or a state office, advice on which program to choose, referrals, and any crisis help.

### Use Cases to Support
Use case "Qualifying for help, including VA programs" (feature 1.2). No task flow is drawn for Epic 1.
- Happy path (Proposed): they record a program and its steps and finish a step.
- Non-happy path (Proposed): the program turns them down, and they keep their record.

### Acceptance (Proposed)
- The spouse can record a program they are applying to, in their own words.
- The spouse can add more than one step for a program, in their own words.
- The spouse can see where each step stands (for example, not started, in progress, sent and waiting, finished, or turned down), can change it, and can see the date they last changed it.
- After a program turns them down, the spouse can still see their record and can add steps or record another program.
- No one else, including other members of the care circle, can see what the spouse recorded.
- If the spouse is deleted, everything they recorded is deleted with them, including notes about the partner's benefits.
- The record can be counted (programs, steps and where each stands), so use can be measured later.

**Scenario 1: I record a program and its steps (happy path)**
- **USE CASE:** Qualifying for help, including VA programs (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **WHEN** I record a program I am applying to and a step I need to do, in my own words
- **THEN** both are saved
- **AND** only I can see them

**Scenario 2: I finish a step (happy path)**
- **USE CASE:** Qualifying for help, including VA programs (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have a step marked in progress
- **WHEN** I mark it finished
- **THEN** it shows as finished
- **AND** it shows the date I changed it

**Scenario 3: the program turns me down (non-happy path)**
- **USE CASE:** Qualifying for help, including VA programs (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have a program with a step marked sent and waiting
- **WHEN** I record that I was turned down
- **THEN** it shows as turned down
- **AND** my record stays visible
- **AND** I can add steps or record another program

**Scenario 4: another member of my care circle (non-happy path)**
- **USE CASE:** Qualifying for help, including VA programs (feature 1.2)
- **AS A:** another member of the care circle
- **GIVEN** I am signed in
- **WHEN** I try to open the spouse's programs
- **THEN** I cannot see them

### Technical Requirements
**Approved rules (from the non-functional list):** T2.2.1 (row-level security on every table), T2.2.3 (deleting the caregiver deletes what they entered), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** records go in the shared table `private_records`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, owner, kind, parent record, text in the person's own words, contact note, date, status, the time the status last changed, and created. This task uses kind `program` (text, and a status of in progress, approved or turned down) and kind `program_step` (text, the program it belongs to, and a status of not started, in progress, sent and waiting, finished or turned down). The database allows only those statuses for each kind.
- **Access:** only the owner can read, add, change or delete these rows. There is no link to a care circle, so nothing can leak through circle membership. A denied read shows nothing, as if the record does not exist. No program rules are stored. This depends on T4.1.4, which is still Proposed and open for a lawyer.
- **Deletion:** deleting the spouse deletes all their rows in one step, including notes about the partner's benefits, and deleting a program deletes its steps.
- **Date last changed:** every status change sets the time from the server's clock, not the browser's. Only the latest change is kept; there is no separate history table for now.
- **Counting:** a database function returns numbers only (for example, programs, steps and each status per spouse), never the text. Whether anyone may count private rows is still open.
- **Checks:** a second fake user in the same fake circle sees zero of these rows and cannot add, change or delete them; deleting the fake owner leaves zero rows; the count function returns the right numbers and no text; changing a status moves its date; after a program is turned down, the record stays and new steps or programs can be added.

**Open (not decided here):** notes about the partner's benefits or military service are not covered by the approved list or the risk profile, and consent belongs to the person the data is about (a lawyer's question).

**Assumptions to check when it is built (agile):** spouses will track paperwork this way, one set of statuses may not fit every program, and one week is the right size.

---

## Task 1.2.3: Feeling close to their partner again
Epic 1, feature 1.2 (Audience 2). Approved by the owner on 2026-11-15.

**INVEST (as named):** Independent fail (needs sign-in and private records first; a build-order dependency), Negotiable pass, Valuable pass (serves the spouse's need; supports the Epic 1 KPI only indirectly, because closeness is not a break), Estimable fail (what "close" means is personal and no saved research says what helps), Small fail (anything beyond recording is wide), Testable fail. Fix: a record-only slice of about 1 week, where the spouse records moments of closeness they want to keep and whether each happened. After the cut: Independent still fails (build order), the other five pass. Size is a guess.

### Background
Spouses carry the care, often alone, and this is their rank 1 problem, which includes losing closeness (45 posts and threads, read by one person and not double-checked). The audience table names the moment, "When they feel lonely, unheard or without affection" (line 110), and the scenario, "Help them keep moments of closeness with their partner" (line 116). That scenario is not in Vision and Scope's lists of MVP or MMP use cases, so the page cites it from the audience table. The saved research counts the problem but holds no evidence of what helps. This task serves Epic 1, business goal 1, and supports its KPI "% of caregivers who get a real break" only indirectly.

Sources:
- Audience Segmentation Master Report: table 2b, rank 1 (line 104), and table 2a, top motivation (line 92).
- `Audience Use Cases.csv`: lines 107 to 116, with the moment on line 110, the goal on line 113 and the scenario on line 116.
- `vision-and-scope-boards-2026-11-10.md`: the scope row (line 182). The closeness scenario is not among its use cases (lines 168 to 174).
- `docs/risk-profile.md`: no saved rule covers a caregiver's own notes or details about a partner (open item).
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.2.1 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As a spouse or partner caring for my partner, I want to feel close to my partner again, so that caring doesn't crowd out the closeness we had.

### Problems to Solve
"Today, spouses carry the care, often alone, and lose health, sleep, closeness and breaks." (approved scope row)

### Task Goals
"We want them to feel close to their partner again." (`Audience Use Cases.csv`, line 113)

### Expected Deliverables (Proposed)
- A working way for the spouse to record moments of closeness they want to keep with their partner, and keep track of whether each one happened, using fake data.
- The scenarios below pass.
- **Definition of done (Proposed):** The spouse can record one or more moments of closeness they want to keep with their partner (in their own words, with a date), and see and change whether each is still to come, happened or did not happen, using fake data. Only the person who recorded them can see them. All the scenarios below pass. Not included: advice on how to be close, prompts or ideas, referrals to counselors, messages to the partner, and any crisis help.

### Use Cases to Support
Use case "Spouses keeping moments of closeness with their partner" (feature 1.2), from the audience table (`Audience Use Cases.csv`, line 116). It is not one of the 17 MVP use cases. No task flow is drawn for Epic 1.
- Happy path (Proposed): they record a moment and it happens.
- Non-happy path (Proposed): the moment does not happen, and they keep their record.

### Acceptance (Proposed)
- The spouse can record a moment of closeness they want to keep with their partner, in their own words, with a date.
- The spouse can record more than one.
- The spouse can see whether each moment is still to come, happened or did not happen, can change it, and can see the date they last changed it.
- After a moment is marked did not happen, the spouse can still see it and can change it or record a new one.
- No one else, including other members of the care circle and the partner, can see what the spouse recorded.
- If the spouse is deleted, everything they recorded is deleted with them.
- The record can be counted (how many moments and how many happened), so use can be measured later.

**Scenario 1: I record a moment of closeness (happy path)**
- **USE CASE:** Spouses keeping moments of closeness with their partner (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **WHEN** I record a moment of closeness I want to keep, in my own words
- **THEN** it is saved with the date
- **AND** only I can see it

**Scenario 2: the moment happens (happy path)**
- **USE CASE:** Spouses keeping moments of closeness with their partner (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have a moment marked still to come
- **WHEN** I mark it happened
- **THEN** it shows as happened
- **AND** it shows the date I changed it

**Scenario 3: the moment does not happen (non-happy path)**
- **USE CASE:** Spouses keeping moments of closeness with their partner (feature 1.2)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I have a moment marked still to come
- **WHEN** I mark it did not happen
- **THEN** it shows as did not happen
- **AND** it stays visible
- **AND** I can change it or record a new one

**Scenario 4: another member of my care circle (non-happy path)**
- **USE CASE:** Spouses keeping moments of closeness with their partner (feature 1.2)
- **AS A:** another member of the care circle
- **GIVEN** I am signed in
- **WHEN** I try to open the spouse's moments
- **THEN** I cannot see them

### Technical Requirements
**Approved rules (from the non-functional list):** T2.2.1 (row-level security on every table), T2.2.3 (deleting the caregiver deletes what they entered), T4.2.3 (fake data only in Week 4) and T4.3.1 (plain error messages, and a failed check denies access).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** records go in the shared table `private_records`, which is not in the approved database list (T2.1.2) yet and is added there as a Proposed line. Fields: id, owner, kind, parent record, text in the person's own words, contact note, date, status, the time the status last changed, and created. This task uses kind `closeness_moment` (text, date and a status of still to come, happened or did not happen). The database allows only those statuses for that kind.
- **Access:** only the owner can read, add, change or delete these rows. The partner cannot see them, and the partner may not be a user of the app. There is no link to a care circle. A denied read shows nothing, as if the record does not exist. This depends on T4.1.4, which is still Proposed and open for a lawyer.
- **Deletion:** deleting the spouse deletes all their rows in one step.
- **Date last changed:** every status change sets the time from the server's clock, not the browser's. Only the latest change is kept; there is no separate history table for now.
- **Counting:** a database function returns numbers only (for example, how many moments and how many happened), never the text. Whether anyone may count private rows is still open.
- **Checks:** a second fake user in the same fake circle sees zero of these rows and cannot add, change or delete them; deleting the fake owner leaves zero rows; the count function returns the right numbers and no text; changing a status moves its date; after a moment is marked did not happen, it stays and can be changed or replaced.

**Open (not decided here):** notes about a partner or a relationship are not covered by the approved list or the risk profile, and the partner may not be a user (a lawyer's question).

**Assumptions to check when it is built (agile):** spouses will record moments this way, closeness is personal and may not suit a list, and one week is the right size.

---

## Open items from these pages
- **Privacy of a caregiver's own records (1.1.2, 1.1.3, 1.2.1, 1.2.2, 1.2.3).** "Visible only to the writer" is now written as T4.1.4 in the non-functional list, but it is still Proposed. A caregiver's own mental-health notes, other people's names, and notes about a partner's benefits or relationship may fall under state health-data laws, and the risk profile does not cover them. Needs a lawyer.
- **Crisis safety (1.1.2).** What the screen shows if someone writes about harming themselves is not decided. It is a safety and legal question for the developer role and a lawyer. No advice text is written.
- **Tables for Epic 1 records.** `care_breaks` (1.1.1) and `private_records` (the five private tasks) were drafted by the developer role and approved by the owner on 2026-11-15. They are added to the non-functional list as a Proposed line, T2.1.3, and are not yet in the approved T2 list.
- **Decided on 2026-11-15, to check after Week 4:** no history table for status changes, no access log for private wellbeing records, and "a real break" means a break marked happened.
- **Research on what helps** a caregiver cope, and on how to ask relatives or paid helpers, is not saved. No advice text is written until it is.
- **Size estimates** (about 1 week each) are guesses, not a team's.
