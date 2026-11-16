# Epic 3 task pages (master copy, started 2026-11-15)

**What this is:** the text of the five Epic 3 task pages in the owner's Notion Kanban board ("Tasks Go Here"), using the course's eight task headings: Background, User Story, Problems to Solve, Task Goals, Expected Deliverables, Use Cases to Support, Acceptance, Technical Requirements. This file is the master copy. A Notion page must say the same, word for word.

**How each page is made:** INVEST is graded first (instructor's board: tickets are checked against I.N.V.E.S.T. at refinement). Each page lists its sources in Background. Anything in Claude's own words is tagged Proposed. Pages are shown to the owner one at a time and added here after the owner says yes.

**Status:**
| Task | Notion page | Status |
|---|---|---|
| 3.1.1 Seeing the parent take care of their health | `47c9219a469183f39d35016e94ec08e8` | Approved 2026-11-15 |
| 3.1.2 Getting the parent to accept a safer move | `4159219a469181b793ffeaf1b2e3d74d` | Approved 2026-11-15 (owner delegated the choices to Claude, data-driven) |
| 3.1.3 Finding next steps the parent will accept | `4159219a46918192bba3c7710c0fe790` | Approved 2026-11-15 |
| 3.2.1 Planning together without causing anger | `4159219a469181a5be2be352b2b768fe` | Approved 2026-11-15 |
| 3.2.2 Settling who handles care tasks and money | `4159219a469181bc9721f77519efe07a` | Approved 2026-11-15 |

---

## Task 3.1.1: Seeing the parent take care of their health
Epic 3, feature 3.1 (Audience 1). Approved by the owner on 2026-11-15.

**INVEST (as written):** Independent fail (needs sign-in, care circle, consent records and the care notes table first: an order dependency), Negotiable pass, Valuable pass, Estimable fail ("see" and "health" are open), Small fail (covers doctors, treatment, habits, therapy and medicine), Testable fail. Fix: scoped to one slice of about 1 week. A second slice, "seeing follow-through across steps over time," is written down as later work and has no page yet. Size is a guess, not a team estimate.

### Background
The parent says no to doctors, help, moving or giving up the car. This shows up in 60 posts and threads, read by one person and not double-checked. None of the 16 competitors scores a Yes on getting a parent to accept help. This task serves Epic 3, business goal 3, with the KPI "% of caregivers whose parent or partner accepts outside help."

Sources:
- Audience Segmentation Master Report: table 2b, rank 5 (line 108), and finding 10 (line 183).
- `Audience Use Cases.csv`: lines 48 and 51.
- Competitive Analysis Master Report: finding 2 (line 197) and table 4c.
- `vision-and-scope-boards-2026-11-10.md`: the scope row and the goal 3 KPI.
- `docs/risk-profile.md`: medication lists out of MVP #1, consent, and deletion.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.1.2, T2.2.1, T2.2.3, T4.1.2, T4.1.3 and T4.2.3.
- The user story, acceptance items, Given/When/Then scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want to know whether my parent follows through on a health step they agreed to, so that I'm not left guessing whether they are taking care of their health.

### Problems to Solve
"Today, the parent says no to doctors, help, moving or giving up the car." (approved scope row, from table 2b)

### Task Goals
"We want them to see the parent take care of their health." (`Audience Use Cases.csv`, line 48)

### Expected Deliverables (Proposed)
- A working way to record one agreed health step and whether it happened, using fake data.
- The Given/When/Then scenarios below pass.
- The care notes table exists with its security rules.
- **Definition of done (Proposed):** The caregiver can record one health step the parent agreed to, record whether it was done or not done, and see the date, using fake data. Only people in that parent's care circle can see it. All the scenarios below pass. Not included: tracking medicines, knowing when to step in for safety, and seeing follow-through across steps over time.

### Use Cases to Support
Task flow: Flow 1, the Audience 1 flow (this task is Part 2, trying small steps) (https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079), in the Figma section "TASK FLOWS (Epic 3)."
Use case 2 of feature 3.1, "trying small steps when the answer is no" (scenario: "Help them try small steps when the answer is no").
- Happy path (Proposed): the parent accepts one small step, and the caregiver can see it happened.
- Non-happy path (Proposed): the parent refuses again, and the caregiver can see it did not happen.
- Not included: knowing when to step in for safety (an MMP candidate, not in MVP #1) and tracking medicines (out of MVP #1 per the risk profile).

### Acceptance (Proposed)
- The caregiver can record one health step the parent agreed to, in plain words, with a date.
- The caregiver can record whether the step happened or not.
- Only people in that parent's care circle can see it.
- Another member of the care circle can see a note only after the separate share consent is recorded. Until then, only the person who wrote it can see it. Whose consent counts is still an open lawyer question (risk profile).
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- The record of each health step (done or not done) can be counted, so the goal 3 KPI can be measured later.

**Scenario 1: the parent follows through (happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** I have noted a health step my parent agreed to
- **WHEN** I mark the step as done
- **THEN** it shows as done
- **AND** it shows the date I marked it

**Scenario 2: the parent does not follow through (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** I have noted a health step my parent agreed to
- **WHEN** I mark the step as not done
- **THEN** it shows as not done
- **AND** the step my parent agreed to stays visible
- **AND** it shows the date I marked it

**Scenario 3: consent is not recorded (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is not recorded for my parent
- **WHEN** I try to note a health step
- **THEN** the note is not saved
- **AND** I am asked to record the consent first

**Scenario 4: someone outside the care circle (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** a person who is not in my parent's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the parent
- **WHEN** I try to open the parent's health notes
- **THEN** I cannot see them

**Scenario 5: share consent is not recorded (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is not recorded for my parent
- **WHEN** I try to open the parent's health notes
- **THEN** I cannot see them

**Scenario 6: share consent is recorded (happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is recorded for my parent
- **WHEN** I try to open the parent's health notes
- **THEN** I can see them

### Technical Requirements
**Approved rules (from the non-functional list):** T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deleting the person deletes the notes), T4.1.2 (two consents), T4.1.3 (access log), T4.2.3 (fake data only in Week 4), T4.3.1 (plain error messages, and a failed check denies access) and T6.2.2 (consent, circle access and deletion tested at the lowest level).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** the approved table `care_notes` (T2.1.2). The approved list names the table but not its fields, so these are proposed: id, care circle, cared-for person, who wrote it, kind, text in the caregiver's own words, status, the time the status last changed, and created. This task uses kind `health_step` with statuses agreed, done and not done. The database allows only those statuses for that kind. Left out, as the page says: medicines and knowing when to step in for safety.
- **Access:** circle members can read (T2.2.1). A write is accepted only if a collect consent record exists for that cared-for person (T4.1.2), and the database checks this, not only the screen. If the check fails, access is denied and the screen shows a plain "record the consent first" message (T4.3.1). A person outside the circle gets nothing, as if the record does not exist. Another member sees a note only after the share consent record exists (T2.2.4, T4.1.2).
- **Deletion:** deleting the cared-for person deletes their notes (T2.2.3). Deleting the caregiver deletes the notes that caregiver wrote. This is a proposed reading of T2.2.3 and of the risk profile (line 52), which says an account deletion must also handle the data the caregiver entered.
- **Date last changed:** marking a step done or not done sets its time from the server's clock, not the browser's. Only the latest change is kept, and there is no separate history table for now. A not-done step is never deleted or locked.
- **Counting:** a database function returns numbers only (steps per status for the caller's own circle), never text.
- **Checks:** with fake data (T4.2.3): add a step and mark it done, then not done, and the date moves each time and the step stays visible; saving with no collect consent is rejected and nothing is stored; a fake person outside the circle gets an empty list and cannot write; deleting the fake parent leaves zero notes; the count function returns the right numbers and no text; a view and a change each add one access log row, and an update to the log is refused (T4.1.3); a circle member who did not write a note sees nothing until the share consent record exists and sees it after (Scenarios 5 and 6).

**Open (not decided here):** whose consent counts for a parent or partner who never signs up (a lawyer's question, risk profile open question 1); whether notes written by other members are deleted when a caregiver is deleted; and whether access log rows are deleted with the person, since T4.1.3 says no one can edit the log and T2.2.3 says to delete the health data. The separate share consent (T2.2.4, T4.1.2) is tested by Scenarios 5 and 6.

---

## Task 3.1.2: Getting the parent to accept a safer move
Epic 3, feature 3.1 (Audience 1). Approved by the owner on 2026-11-15. The owner delegated the choices below to Claude, to be decided from the data.

**INVEST (as written):** Independent fail (needs sign-in, care circle, consent records and the care notes table first: an order dependency), Negotiable pass, Valuable pass, Estimable fail ("a safer move" is open and no saved research says what makes a parent accept one), Small fail (the wide version includes choosing, affording and arranging a home), Testable fail. Fix: scoped to one record-only slice of about 1 week. Size is a guess, not a team estimate.

**Choices made (data-driven):**
1. No research step (spike) for now. The three master reports count how often the problem comes up (60 posts and threads) but not what parents accept. The saved findings files (`community-voice-findings.md`, `qualitative-research-findings.md`) count refusals but not what worked. Advice text would be invented, so it is left out and listed as an open item: research on what parents and partners accept.
2. No new use case. The situation "when the parent resists moving somewhere safer" sits under problem 5 in the master CSV (line 46), and the scenario "Help them raise help in a way the parent accepts" covers it. Use case 1 stands for it. Adding one would reopen the approved Vision and Scope (2026-11-10).

### Background
The parent says no to doctors, help, moving or giving up the car. This shows up in 60 posts and threads, read by one person and not double-checked. None of the 16 competitors scores a Yes on getting a parent to accept help. This task serves Epic 3, business goal 3, with the KPI "% of caregivers whose parent or partner accepts outside help."

Sources:
- Audience Segmentation Master Report: table 2b, rank 5 (line 108).
- `Audience Use Cases.csv`: lines 44 to 53 (the situation, the goal and the scenarios), line 66 ("a hospital or rehab stay forces a fast move") and line 74 (a parent who falls at home).
- Competitive Analysis Master Report: finding 2 (line 197).
- `vision-and-scope-boards-2026-11-10.md`: the MVP scope row and the MMP scope table (rows 7 and 10).
- `docs/risk-profile.md`.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.1.2, T2.2.1, T2.2.3, T4.1.2, T4.1.3 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want my parent to accept a safer move, so that a move isn't forced in a rush after a fall or a hospital stay.

### Problems to Solve
"Today, the parent says no to doctors, help, moving or giving up the car." (approved scope row). The situation: "When the parent resists moving somewhere safer." (`Audience Use Cases.csv`, line 46)

### Task Goals
"We want them to get the parent to accept a safer move." (`Audience Use Cases.csv`, line 49)

### Expected Deliverables (Proposed)
- A working way to record how the parent answered when a safer move was raised, and the next step to try, using fake data.
- The scenarios below pass.
- Not included: advice on how to raise a move in a way the parent accepts. The saved research counts how often parents refuse but not what they accept, so this needs research first (open item).
- **Definition of done (Proposed):** The caregiver can record the date a safer move was raised and what the parent said, the answer (accepted, not yet or refused), the reason, and one next step to try, using fake data. Only people in that parent's care circle can see it. All the scenarios below pass. Not included: advice on how to raise a move, finding or paying for a new home, arranging the move, giving up the car, and knowing when to step in for safety.

### Use Cases to Support
Task flow: Flow 1, the Audience 1 flow (this task is Part 1, raising it and recording the answer) (https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079), in the Figma section "TASK FLOWS (Epic 3)."
- Use case 1, "getting the parent to accept outside help," is the closest fit. No MVP use case is named "a safer move." The situation sits under problem 5, so this use case covers it. Happy path (Proposed): the parent agrees to the move or a first step toward it.
- Use case 2, "trying small steps when the answer is no." Non-happy path (Proposed): the parent refuses, and the caregiver records the reason and one next step to try.
- Not included: finding or paying for a new home (MMP), arranging the move or moving to prevent falls (MMP), giving up the car, and knowing when to step in for safety (an MMP candidate).

### Acceptance (Proposed)
- The caregiver can record the date a safer move was raised and what the parent said, in plain words.
- The caregiver can record the parent's answer: accepted, not yet, or refused.
- The caregiver can record the reason the parent gave and one next step to try.
- Only people in that parent's care circle can see it.
- Another member of the care circle can see a note only after the separate share consent is recorded. Until then, only the person who wrote it can see it. Whose consent counts is still an open lawyer question (risk profile).
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- The record of each answer (accepted, not yet or refused) can be counted, so the goal 3 KPI can be measured later.

**Scenario 1: the parent agrees (happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** I have raised a safer move with my parent
- **WHEN** I record that my parent agreed
- **THEN** it shows as accepted
- **AND** it shows the date I recorded it

**Scenario 2: the parent says not yet or no (non-happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** I have raised a safer move with my parent
- **WHEN** I record that my parent said not yet or no
- **AND** I note the reason my parent gave and one next step to try
- **THEN** it shows as not yet or refused
- **AND** it shows the reason and the next step
- **AND** the safer move stays on my list

**Scenario 3: consent is not recorded (non-happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is not recorded for my parent
- **WHEN** I try to record what my parent said about a safer move
- **THEN** the note is not saved
- **AND** I am asked to record the consent first

**Scenario 4: someone outside the care circle (non-happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** a person who is not in my parent's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the parent
- **WHEN** I try to open the parent's notes about a safer move
- **THEN** I cannot see them

**Scenario 5: share consent is not recorded (non-happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is not recorded for my parent
- **WHEN** I try to open the parent's notes about a safer move
- **THEN** I cannot see them

**Scenario 6: share consent is recorded (happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is recorded for my parent
- **WHEN** I try to open the parent's notes about a safer move
- **THEN** I can see them

### Technical Requirements
**Approved rules (from the non-functional list):** T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log), T4.2.3 (fake data only in Week 4), T4.3.1 (plain error messages, and a failed check denies access), T6.2.2 (consent, circle access and deletion tested at the lowest level) and T6.4.2 (this page's Scenarios 1 and 3 are the two scenarios run by hand).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** the same `care_notes` table as task 3.1.1, with no new table. New kind `safer_move`. Added fields: the date it was raised (typed by the caregiver), the answer (accepted, not yet or refused), and the reason the parent gave. The one next step is a second row of kind `next_step`, linked to the move, so task 3.1.3 can add more next steps with no rework. Left out, as the page says: advice, finding or paying for a home, and arranging the move.
- **Access:** Same as task 3.1.1: the collect consent is checked by the database before any write, a denied read shows nothing, and another member sees a note only after the share consent record exists (T2.2.4, T4.1.2).
- **Deletion:** same as task 3.1.1. Deleting the person or the move deletes its next-step rows.
- **Date last changed:** recording or changing the answer sets its time from the server's clock. The raised date is the caregiver's own typed date and is a separate field. Only the latest change is kept.
- **Counting:** the same numbers-only function, counting moves per answer (accepted, not yet, refused).
- **Checks:** with fake data (T4.2.3): record accepted and it shows with the date (Scenario 1); record not yet or refused with a reason and one next step and the move stays on the list (Scenario 2); saving with no collect consent is rejected (Scenario 3); an outside fake person sees nothing (Scenario 4); deleting the fake parent leaves zero moves and zero next steps; the count function returns the right numbers; a person runs Scenarios 1 and 3 by hand on the live app and writes down what happened (T6.4.1); a circle member who did not write a note sees nothing until the share consent record exists and sees it after (Scenarios 5 and 6).

**Open (not decided here):** the same consent, share consent and deletion questions as task 3.1.1 (the separate share consent is tested by Scenarios 5 and 6). What parents accept is not researched, so no advice text is built.

---

## Task 3.1.3: Finding next steps the parent will accept
Epic 3, feature 3.1 (Audience 1). Approved by the owner on 2026-11-15, with the three batch tasks together. The choices match task 3.1.2: record-only slice, no invented advice, no new use case.

**Change, 2026-11-15:** widened to cover paid help or aids, the one situation in the master CSV (line 47) with no task. The owner asked what to do about the gap, and Claude proposed this instead of a new task. The slice is still about 1 week, and the task's name and number are unchanged.

**INVEST (as written):** Independent fail (it uses the refused items from 3.1.1 and 3.1.2: an order dependency), Negotiable pass, Valuable pass, Estimable fail (no saved evidence says what next steps parents accept), Small fail, Testable fail. Fix: a record-only slice of about 1 week. Size is a guess.

### Background
The parent says no to doctors, help, moving or giving up the car. This shows up in 60 posts and threads, read by one person and not double-checked. None of the 16 competitors scores a Yes on getting a parent to accept help. This task serves Epic 3, business goal 3, with the KPI "% of caregivers whose parent or partner accepts outside help." It builds on the refused items recorded in the two tasks before it (seeing the parent take care of their health, and getting the parent to accept a safer move).

Sources:
- Audience Segmentation Master Report: table 2b, rank 5 (line 108).
- `Audience Use Cases.csv`: lines 44 to 53.
- Competitive Analysis Master Report: finding 2 (line 197).
- `vision-and-scope-boards-2026-11-10.md`: the MVP scope row "Getting the parent to accept doctors or help."
- `docs/risk-profile.md`.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.1.2, T2.2.1, T2.2.3, T4.1.2, T4.1.3 and T4.2.3.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As an adult child caring for a parent, I want to find a next step my parent will accept after they say no, so that one refusal doesn't stop their care.

### Problems to Solve
"Today, the parent says no to doctors, help, moving or giving up the car." (approved scope row)

### Task Goals
"We want them to find next steps the parent will accept." (`Audience Use Cases.csv`, line 50)

### Expected Deliverables (Proposed)
- A working way to see every refused item with its next steps in one place, and to record what happened when a step was tried, using fake data.
- The scenarios below pass.
- Not included: advice on which step to try. The saved research counts how often parents refuse but not what they accept, so this needs research first (open item). Also not included: knowing when to step in for safety (an MMP candidate).
- **Definition of done (Proposed):** The caregiver can see every refused item with its next steps in one place, record what happened when a step was tried (accepted, not yet or refused), record another next step after a new refusal, and record an item with no earlier record, such as paid help or aids the parent turned down, using fake data. Only people in that parent's care circle can see it. All the scenarios below pass. Not included: advice on which step to try, and knowing when to step in for safety.

### Use Cases to Support
Task flow: Flow 1, Part 2 (the next steps) and Part 1 (for paid help or aids), in TASK FLOWS (Epic 3) (https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079).
Use case 2, "trying small steps when the answer is no" (scenarios: "Help them try small steps when the answer is no" and "Help them keep going after a refusal").
- Happy path (Proposed): the parent accepts one small step.
- Non-happy path (Proposed): the parent refuses again.

Also use case 1, "getting the parent to accept outside help," for the situation "When the parent turns down paid help or aids" (`Audience Use Cases.csv`, line 47). The other tasks in this feature cover doctors, treatment, habits, therapy and a safer move. This task covers paid help or aids.

### Acceptance (Proposed)
- The caregiver can see every open refused item with its next step.
- The caregiver can record that a step was tried and the answer: accepted, not yet, or refused.
- After a new refusal, the caregiver can record another next step, and the earlier ones stay visible.
- The caregiver can record an item that has no earlier record, such as the parent turning down paid help or aids, with what was raised, the parent's answer (accepted, not yet, or refused), the reason if given, and a next step if it was not accepted.
- Only people in that parent's care circle can see it.
- Another member of the care circle can see a note only after the separate share consent is recorded. Until then, only the person who wrote it can see it. Whose consent counts is still an open lawyer question (risk profile).
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- The record of each answer (accepted, not yet or refused) can be counted, so the goal 3 KPI can be measured later.

**Scenario 1: the parent accepts the next step (happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** an item my parent refused is on my list with a next step to try
- **WHEN** I try the next step with my parent
- **AND** I record that my parent accepted
- **THEN** the item shows as accepted
- **AND** it comes off my list

**Scenario 2: the parent refuses again (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** an item my parent refused is on my list with a next step to try
- **WHEN** I record that my parent refused again
- **AND** I add another next step to try
- **THEN** the item stays on my list
- **AND** both next steps are visible

**Scenario 3: the parent turned down paid help or aids (non-happy path)**
- **USE CASE:** Getting the parent to accept outside help (feature 3.1, use case 1)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is recorded for my parent
- **AND** my parent turned down paid help or aids
- **WHEN** I add it with what I raised, my parent's answer, the reason my parent gave, and a next step to try
- **THEN** it appears on my list

**Scenario 4: consent is not recorded (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** adult child caring for a parent
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** the collect consent is not recorded for my parent
- **WHEN** I try to add a refused item or a next step
- **THEN** the note is not saved
- **AND** I am asked to record the consent first

**Scenario 5: someone outside the care circle (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** a person who is not in my parent's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the parent
- **WHEN** I try to open the list of refused items
- **THEN** I cannot see it

**Scenario 6: share consent is not recorded (non-happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is not recorded for my parent
- **WHEN** I try to open the list of refused items
- **THEN** I cannot see it

**Scenario 7: share consent is recorded (happy path)**
- **USE CASE:** Trying small steps when the answer is no (feature 3.1, use case 2)
- **AS A:** another member of my parent's care circle
- **GIVEN** I am signed in
- **AND** I am in my parent's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my parent
- **AND** the share consent is recorded for my parent
- **WHEN** I try to open the list of refused items
- **THEN** I can see it

### Technical Requirements
**Approved rules (from the non-functional list):** T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log), T4.2.3 (fake data only in Week 4), T4.3.1 (plain error messages, and a failed check denies access) and T6.2.2 (consent, circle access and deletion tested at the lowest level).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** the same `care_notes` table, with no new table. It reuses the `next_step` rows from task 3.1.2, so one item can have many steps and the earlier ones stay. Each step has its own answer (accepted, not yet or refused) and its own status time. New kind `outside_help` is for paid help or aids the parent turned down. Its fields are what was raised, the answer, the reason and a next step. The list of refused items is a read of existing rows whose item is not accepted, not a new table.
- **Access:** Same as task 3.1.1: the collect consent is checked by the database before any write, a denied read shows nothing, and another member sees a note only after the share consent record exists (T2.2.4, T4.1.2).
- **Deletion:** deleting the person deletes the items and all their steps. Deleting a step never deletes its item.
- **Date last changed:** recording a step's answer sets its time from the server's clock. The item's answer changes in the same database action, so the two cannot disagree. Only the latest change is kept. An accepted item stays stored and only leaves the open list.
- **Counting:** the same numbers-only function, counting items and steps per answer.
- **Checks:** with fake data (T4.2.3): accept a step and the item shows accepted and leaves the list (Scenario 1); refuse again and add a second step and both steps show (Scenario 2); add a paid-help item with no earlier record (Scenario 3); saving with no collect consent is rejected (Scenario 4); an outside fake person sees nothing (Scenario 5); deleting the fake parent leaves zero items and steps; the count function returns the right numbers; a circle member who did not write a note sees nothing until the share consent record exists and sees it after (Scenarios 6 and 7).

**Open (not decided here):** whether a task 3.1.1 step marked "not done" shows in the refused list, since 3.1.1 has no "refused" status; and the same consent, share consent and deletion questions as task 3.1.1 (the separate share consent is tested by Scenarios 6 and 7).

---

## Task 3.2.1: Planning together without causing anger
Epic 3, feature 3.2 (Audience 2). Approved by the owner on 2026-11-15, with the three batch tasks together.

**INVEST (as written):** Independent fail (needs the foundation tables), Negotiable pass, Valuable pass, Estimable fail (no saved evidence says how to talk without a fight), Small fail, Testable fail. Fix: a record-only slice of about 1 week. The evidence is thin (9 posts and threads), so the slice is kept small. Size is a guess.

### Background
The partner denies their needs and refuses helpers, medical care or changes. This shows up in 9 posts and threads, read by one person and not double-checked, so the evidence is thin. This task serves Epic 3, business goal 3, with the KPI "% of caregivers whose parent or partner accepts outside help."

Sources:
- Audience Segmentation Master Report: table 2b, Audience 2 rank 8 (line 111).
- `Audience Use Cases.csv`: lines 165 to 171.
- `vision-and-scope-boards-2026-11-10.md`: the MVP scope row "Bringing in outside help the partner accepts."
- `docs/risk-profile.md`.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.1.2, T2.2.1, T2.2.3, T4.1.2, T4.1.3 and T4.2.3.
- `feature-stories-and-use-cases-epic-3-2026-11-15.md`: the use case and its scenarios. Pairing a scenario with this task is Claude's reading.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As a spouse or partner caring for my partner, I want to plan with my partner without it turning into a fight, so that care decisions get made instead of put off.

### Problems to Solve
"Today, the partner denies needs and refuses help or changes." (approved scope row)

### Task Goals
"We want them to plan together without causing anger." (`Audience Use Cases.csv`, line 167)

### Expected Deliverables (Proposed)
- A working way to list topics to plan with the partner and record how each talk went, using fake data.
- The scenarios below pass.
- Not included: advice on how to raise hard topics. The saved research counts how often this problem comes up but not what partners accept, so this needs research first (open item). Also not included: bringing in a helper.
- **Definition of done (Proposed):** The caregiver can record a topic to plan with their partner, see and change how it went (not raised yet, talked calmly, turned into a fight, or agreed), record what to try next time, and see the date, using fake data. Only people in the care circle can see it. All the scenarios below pass. Not included: advice on how to raise hard topics, and bringing in a helper.

### Use Cases to Support
Task flow: Flow 2, branch A, Spouses bringing in help the partner will accept (https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079), in the Figma section "TASK FLOWS (Epic 3)."
Use case "Spouses bringing in help the partner will accept," scenario "Help them raise hard topics without a fight."
- Happy path (Proposed): the caregiver and the partner talk about the topic without it turning into a fight.
- Non-happy path (Proposed): the talk turns into a fight.

### Acceptance (Proposed)
- The caregiver can record a topic they want to plan with their partner.
- The caregiver can see where each topic stands (not raised yet, talked calmly, turned into a fight, or agreed) and can change it.
- The caregiver can record what to try next time.
- Only people in the care circle can see it.
- Another member of the care circle can see a note about the partner only after the separate share consent is recorded. Until then, only the person who wrote it can see it. Whose consent counts is still an open lawyer question (risk profile).
- A note about the partner is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the partner deletes the notes about them.
- The record of each topic (agreed or turned into a fight) can be counted, so the goal 3 KPI can be measured later.

**Scenario 1: the talk goes well and we agree (happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is recorded for my partner
- **AND** I have added a topic I want to plan with my partner
- **WHEN** I talk with my partner about it
- **AND** I record that we talked calmly and agreed
- **THEN** the topic shows as agreed
- **AND** it shows the date I recorded it

**Scenario 2: the talk turns into a fight (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is recorded for my partner
- **AND** I have added a topic I want to plan with my partner
- **WHEN** I record that the talk turned into a fight
- **AND** I note what to try next time
- **THEN** the topic shows as turned into a fight
- **AND** my note on what to try next time is kept
- **AND** the topic stays on my list

**Scenario 3: consent is not recorded (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is not recorded for my partner
- **WHEN** I try to add a topic
- **THEN** the note is not saved
- **AND** I am asked to record the consent first

**Scenario 4: someone outside the care circle (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** a person who is not in my partner's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the partner
- **WHEN** I try to open the partner's list of topics
- **THEN** I cannot see it

**Scenario 5: share consent is not recorded (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** another member of my partner's care circle
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my partner
- **AND** the share consent is not recorded for my partner
- **WHEN** I try to open the partner's list of topics
- **THEN** I cannot see it

**Scenario 6: share consent is recorded (happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: raise hard topics without a fight)
- **AS A:** another member of my partner's care circle
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** I did not write the note
- **AND** the collect consent is recorded for my partner
- **AND** the share consent is recorded for my partner
- **WHEN** I try to open the partner's list of topics
- **THEN** I can see it

### Technical Requirements
**Approved rules (from the non-functional list):** T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log), T4.2.3 (fake data only in Week 4), T4.3.1 (plain error messages, and a failed check denies access) and T6.2.2 (consent, circle access and deletion tested at the lowest level).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** the same `care_notes` table. New kind `plan_topic`. Fields: the topic in the caregiver's words, the status (not raised yet, talked calmly, turned into a fight, or agreed), and what to try next time. The cared-for person is the partner. The database allows only those four statuses for that kind. Left out, as the page says: advice and bringing in a helper.
- **Access:** Same as task 3.1.1: the collect consent is checked by the database before any write, a denied read shows nothing, and another member sees a note only after the share consent record exists (T2.2.4, T4.1.2). These notes are about the partner, who may never sign up.
- **Deletion:** deleting the partner deletes their topics (T2.2.3). Deleting the caregiver deletes the notes that caregiver wrote. This is a proposed reading of T2.2.3 and of the risk profile (line 52), which says an account deletion must also handle the data the caregiver entered.
- **Date last changed:** each status change sets its time from the server's clock. Only the latest change is kept. The "what to try next time" text is kept after a fight.
- **Counting:** the same numbers-only function, counting topics per status (for example agreed and turned into a fight).
- **Checks:** with fake data (T4.2.3): add a topic and mark it agreed and the date shows (Scenario 1); mark a fight with a next-time note and the topic stays and the note is kept (Scenario 2); saving with no collect consent is rejected (Scenario 3); an outside fake person sees nothing (Scenario 4); deleting the fake partner leaves zero topics; the count function returns the right numbers; a circle member who did not write a note sees nothing until the share consent record exists and sees it after (Scenarios 5 and 6).

**Open (not decided here):** whose consent counts for a parent or partner who never signs up (a lawyer's question, risk profile open question 1); and whether notes about fights should be private to the writer. T4.1.4 does not cover this page, and the page says the circle can see them. The separate share consent (T2.2.4, T4.1.2) is tested by Scenarios 5 and 6.

---

## Task 3.2.2: Settling who handles care tasks and money
Epic 3, feature 3.2 (Audience 2). Approved by the owner on 2026-11-15, with the three batch tasks together.

**INVEST (as written):** Independent fail (needs the foundation tables and the care tasks table), Negotiable pass, Valuable pass, Estimable pass once narrowed, Small fail (as written it could include money records and invitations), Testable fail. Fix: a slice of about 1 week that only records who handles each task. Size is a guess.

### Background
The partner denies their needs and refuses helpers, medical care or changes (9 posts and threads, read by one person and not double-checked, so the evidence is thin), and spouses often carry the care alone. This task serves Epic 3, business goal 3, with the KPI "% of caregivers whose parent or partner accepts outside help."

Sources:
- Audience Segmentation Master Report: table 2b, Audience 2 ranks 1 and 8 (lines 104 and 111).
- `Audience Use Cases.csv`: lines 165 to 171.
- `vision-and-scope-boards-2026-11-10.md`: the MVP scope rows "Bringing in outside help the partner accepts" and "Getting real breaks and a life outside caring."
- `docs/risk-profile.md`.
- `non-functional-epics-features-tasks-2026-11-15.md`: T2.1.2, T2.2.1, T2.2.3, T4.1.1, T4.1.2, T4.1.3 and T4.2.3.
- `feature-stories-and-use-cases-epic-3-2026-11-15.md`: the use case and its scenarios. Pairing a scenario with this task is Claude's reading.
- The user story, acceptance items, scenarios and the one-slice scope are Claude's wording (Proposed).

### User Story (Proposed)
As a spouse or partner caring for my partner, I want us to settle who handles each care task and money task, so that the care and the money don't all fall on one person.

### Problems to Solve
"Today, the partner denies needs and refuses help or changes." and "Today, spouses carry the care, often alone, and lose health, sleep, closeness and breaks." (approved scope rows)

### Task Goals
"We want them to settle who handles care tasks and money." (`Audience Use Cases.csv`, line 169)

### Expected Deliverables (Proposed)
- A working way to list care and money tasks and record who handles each, using fake data.
- The scenarios below pass.
- Not included: inviting other people by email (the email service is not chosen yet), money amounts, accounts or bills (those come with Epics 5 and 6), and reminders.
- **Definition of done (Proposed):** The caregiver can record a care task or a money task, say who handles it (the caregiver, the partner, or a helper they name), change it later with the earlier choice kept visible, and record that it is not agreed and why, using fake data. Only people in the care circle can see it. All the scenarios below pass. Not included: inviting people by email, money amounts, accounts or bills, and reminders.

### Use Cases to Support
Task flow: Flow 2, branch B, Spouses bringing in help the partner will accept (https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3097-9079), in the Figma section "TASK FLOWS (Epic 3)."
Use case "Spouses bringing in help the partner will accept," scenario "Help them agree on who does what."
- Happy path (Proposed): they agree who handles each care task and money task.
- Non-happy path (Proposed): they cannot agree.

### Acceptance (Proposed)
- The caregiver can record a care task or a money task.
- The caregiver can say who handles it: the caregiver, the partner, or another helper they name.
- It shows the date it was agreed. If the owner changes, the earlier owner stays visible.
- The caregiver can record that a task is not agreed, and why.
- Only people in the care circle can see it.
- Another member of the care circle can see a task only after the separate share consent is recorded. Until then, only the person who wrote it can see it. Whose consent counts is still an open lawyer question (risk profile).
- A note about the partner is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the partner deletes the notes about them.
- The record of who handles each task (the caregiver, the partner or a helper) can be counted, so the goal 3 KPI can be measured later.

**Scenario 1: we agree who handles it (happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is recorded for my partner
- **AND** I have added a care task or a money task
- **WHEN** I choose who handles it: me, my partner, or a helper I name
- **THEN** the task shows that person
- **AND** it shows the date we agreed

**Scenario 2: we change who handles it (other path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is recorded for my partner
- **AND** a task already shows who handles it
- **WHEN** I change who handles it
- **THEN** the task shows the new person and the date
- **AND** the earlier person stays visible

**Scenario 3: we cannot agree (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is recorded for my partner
- **AND** I have added a care task or a money task
- **WHEN** I record that we could not agree
- **AND** I note why
- **THEN** the task shows as not agreed
- **AND** my note is kept
- **AND** the task stays on my list

**Scenario 4: consent is not recorded (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** spouse or partner caring for my partner
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** the collect consent is not recorded for my partner
- **WHEN** I try to add a care task or a money task
- **THEN** the note is not saved
- **AND** I am asked to record the consent first

**Scenario 5: someone outside the care circle (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** a person who is not in my partner's care circle
- **GIVEN** I am signed in
- **AND** I am not in the care circle of the partner
- **WHEN** I try to open the partner's list of care and money tasks
- **THEN** I cannot see it

**Scenario 6: share consent is not recorded (non-happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** another member of my partner's care circle
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** I did not add the task
- **AND** the collect consent is recorded for my partner
- **AND** the share consent is not recorded for my partner
- **WHEN** I try to open the partner's list of care and money tasks
- **THEN** I cannot see it

**Scenario 7: share consent is recorded (happy path)**
- **USE CASE:** Spouses bringing in help the partner will accept (scenario: agree on who does what)
- **AS A:** another member of my partner's care circle
- **GIVEN** I am signed in
- **AND** I am in my partner's care circle
- **AND** I did not add the task
- **AND** the collect consent is recorded for my partner
- **AND** the share consent is recorded for my partner
- **WHEN** I try to open the partner's list of care and money tasks
- **THEN** I can see it

### Technical Requirements
**Approved rules (from the non-functional list):** T2.1.2 (care tasks table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.1 (members see only their own circle, role changes visible), T4.1.2 (two consents), T4.1.3 (access log), T4.2.3 (fake data only in Week 4), T4.3.1 (plain error messages, and a failed check denies access) and T6.2.2 (consent, circle access and deletion tested at the lowest level).

**Developer-role rules (Proposed by the developer role, approved by the owner 2026-11-15):**
- **Data:** the approved table `care_tasks` (T2.1.2). It is separate from `care_notes` because a task has a handler and a note does not. The approved list names the table but not its fields, so these are proposed: id, care circle, cared-for person, who added it, kind (care or money), what the task is in words, who handles it (the caregiver, the partner, or a helper), the handler's circle member (only if that person is a member), the helper's name (only for a helper), agreement status (not decided, agreed or not agreed), the time the agreement last changed, the note on why it is not agreed, the one earlier handler, and created. Left out, as the page says: money amounts, accounts, bills, invitations and reminders.
- **Access:** circle members can read (T2.2.1, T4.1.1). A handler who is a member must be in the same circle, which the database checks. The partner may not be an app user, so "partner" is a choice and not a link to an account. A write needs the collect consent (checked by the database). A denied read shows nothing. Another member sees a task only after the share consent record exists (T2.2.4, T4.1.2). Only the main caregiver role can add or change tasks (a proposal).
- **Deletion:** deleting the partner or the circle deletes its tasks (T2.2.3). Deleting the caregiver deletes the notes that caregiver wrote. This is a proposed reading of T2.2.3 and of the risk profile (line 52), which says an account deletion must also handle the data the caregiver entered. The helper's name is deleted with its task.
- **Date last changed:** changing the handler or the agreement sets the time from the server's clock. The page needs the earlier person to stay visible, so one column keeps the one earlier handler, and a third change overwrites the first. There is no separate history table.
- **Counting:** a numbers-only function counting tasks per handler type (caregiver, partner, helper) and per agreement status.
- **Checks:** with fake data (T4.2.3): choose each of the three handlers and the date shows (Scenario 1); change the handler and the new person and date show while the earlier person stays (Scenario 2); mark not agreed with a note and the note is kept and the task stays (Scenario 3); saving with no collect consent is rejected (Scenario 4); an outside fake person sees nothing (Scenario 5); a handler from another fake circle is rejected; deleting the fake partner leaves zero tasks; the count function returns the right numbers; a circle member who did not write a task sees nothing until the share consent record exists and sees it after (Scenarios 6 and 7).

**Open (not decided here):** whether more than one earlier handler must stay visible (this would need a history table, so it is the owner's call); whether invited relatives may change tasks, or only the main caregiver; whether a helper's name needs its own consent (a lawyer's question); whether care and money tasks are written to the access log, which T4.1.3 limits to health notes; and whose consent counts for a parent or partner who never signs up (a lawyer's question, risk profile open question 1). The separate share consent (T2.2.4, T4.1.2) is tested by Scenarios 6 and 7.

---

## Open items from these pages
- **Research on what parents and partners accept.** Tasks 3.1.2, 3.1.3 and 3.2.1 leave out advice on how to raise a move, which next step to try, and how to raise hard topics. The saved research counts how often these problems come up but not what works. Do this research before any advice text is written.
- **Whose consent counts for a parent or partner who never signs up** (risk profile, open question 1, needs a lawyer).
- **Paid help or aids** is covered by task 3.1.3 (widened 2026-11-15), not by a new task.
- **A second slice for 3.1.1,** "seeing follow-through across steps over time," is written down as later work and has no page.
- **Audience 2's evidence is thin** (9 posts and threads, table 2b).
- **Size estimates** (about 1 week each) are guesses, not a team's.
