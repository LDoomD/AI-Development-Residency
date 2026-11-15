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
- A working way to note one agreed health step and whether it happened, using fake data.
- The Given/When/Then scenarios below pass.
- The care notes table exists with its security rules.

### Use Cases to Support
Use case 2 of feature 3.1, "trying small steps when the answer is no" (scenario: "Help them try small steps when the answer is no").
- Happy path (Proposed): the parent accepts one small step, and the caregiver can see it happened.
- Non-happy path (Proposed): the parent refuses again, and the caregiver can see it did not happen.
- Not included: knowing when to step in for safety (an MMP candidate, not in MVP #1) and tracking medicines (out of MVP #1 per the risk profile).

### Acceptance (Proposed)
- The caregiver can note one health step the parent agreed to, in plain words, with a date.
- The caregiver can mark whether it happened or not.
- Only people in that parent's care circle can see it.
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- Given a step the parent agreed to, when I mark it done, then it shows as done with the date.
- Given a step the parent agreed to, when the parent refuses and I mark it not done, then it shows as not done and the agreement stays visible.

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log) and T4.2.3 (fake data only in Week 4). Anything beyond these comes from the developer role (Claude Code) later.

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

### Use Cases to Support
- Use case 1, "getting the parent to accept outside help," is the closest fit. No MVP use case is named "a safer move." The situation sits under problem 5, so this use case covers it. Happy path (Proposed): the parent agrees to the move or a first step toward it.
- Use case 2, "trying small steps when the answer is no." Non-happy path (Proposed): the parent refuses, and the caregiver records the reason and one next step to try.
- Not included: finding or paying for a new home (MMP), arranging the move or moving to prevent falls (MMP), giving up the car, and knowing when to step in for safety (an MMP candidate).

### Acceptance (Proposed)
- The caregiver can note the date a safer move was raised and what the parent said, in plain words.
- The caregiver can mark the answer: accepted, not yet, or refused.
- The caregiver can note the reason the parent gave and one next step to try.
- Only people in that parent's care circle can see it.
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- Given I raised a safer move, when the parent agrees, then it shows as accepted with the date.
- Given I raised a safer move, when the parent refuses and I record the reason and a next step, then it shows as refused with that next step, and the move stays an open item.

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log) and T4.2.3 (fake data only in Week 4). Anything beyond these comes from the developer role (Claude Code) later.

---

## Task 3.1.3: Finding next steps the parent will accept
Epic 3, feature 3.1 (Audience 1). Approved by the owner on 2026-11-15, with the three batch tasks together. The choices match task 3.1.2: record-only slice, no invented advice, no new use case.

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

### Use Cases to Support
Use case 2, "trying small steps when the answer is no" (scenarios: "Help them try small steps when the answer is no" and "Help them keep going after a refusal").
- Happy path (Proposed): the parent accepts one small step.
- Non-happy path (Proposed): the parent refuses again.

### Acceptance (Proposed)
- The caregiver can see every open refused item with its next step.
- They can record that a step was tried and the answer: accepted, not yet, or refused.
- After a new refusal they can add another next step, and the earlier ones stay visible.
- Only people in that parent's care circle can see it.
- A health note is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the parent deletes the notes about them.
- Given a refused item with a next step, when I try it and the parent accepts, then the item shows as accepted and leaves the open list.
- Given a refused item, when the parent refuses again and I add another next step, then the item stays open with both steps visible.

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log) and T4.2.3 (fake data only in Week 4). Anything beyond these comes from the developer role (Claude Code) later.

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

### Use Cases to Support
Use case "Spouses bringing in help the partner will accept," scenario "Help them raise hard topics without a fight."
- Happy path (Proposed): the caregiver and the partner talk about the topic without it turning into a fight.
- Non-happy path (Proposed): the talk turns into a fight.

### Acceptance (Proposed)
- The caregiver can add a topic they want to plan with their partner.
- They can mark it: not raised yet, talked calmly, turned into a fight, or agreed.
- They can note what to try next time.
- Only people in the care circle can see it.
- A note about the partner is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the partner deletes the notes about them.
- Given a topic I want to plan, when we talk calmly and agree, then it shows as agreed with the date.
- Given a topic, when the talk turns into a fight, then it shows as turned into a fight, stays open, and keeps my note on what to try next.

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.1.2 (care notes table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.2 (two consents), T4.1.3 (access log) and T4.2.3 (fake data only in Week 4). Anything beyond these comes from the developer role (Claude Code) later.

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

### Use Cases to Support
Use case "Spouses bringing in help the partner will accept," scenario "Help them agree on who does what."
- Happy path (Proposed): they agree who handles each care task and money task.
- Non-happy path (Proposed): they cannot agree.

### Acceptance (Proposed)
- The caregiver can add a care task or a money task.
- They can choose who handles it: the caregiver, the partner, or another helper they name.
- It shows the date it was agreed. If the owner changes, the earlier owner stays visible.
- A task can be marked "not agreed" with a note on why.
- Only people in the care circle can see it.
- A note about the partner is not saved until the collect consent is recorded. Whose consent counts is still an open lawyer question (risk profile).
- Deleting the partner deletes the notes about them.
- Given a task, when we agree who handles it, then it shows that person and the date.
- Given a task, when we cannot agree, then it shows as not agreed with my note, and stays open.

### Technical Requirements
These are the approved rules from the non-functional list, not new ones: T2.1.2 (care notes and care tasks table), T2.2.1 (row-level security), T2.2.3 (deletion), T4.1.1 (members see only their own circle), T4.1.2 (two consents), T4.1.3 (access log) and T4.2.3 (fake data only in Week 4). Anything beyond these comes from the developer role (Claude Code) later.

---

## Open items from these pages
- **Research on what parents and partners accept.** Tasks 3.1.2, 3.1.3 and 3.2.1 leave out advice on how to raise a move, which next step to try, and how to raise hard topics. The saved research counts how often these problems come up but not what works. Do this research before any advice text is written.
- **Whose consent counts for a parent or partner who never signs up** (risk profile, open question 1, needs a lawyer).
- **A second slice for 3.1.1,** "seeing follow-through across steps over time," is written down as later work and has no page.
- **Audience 2's evidence is thin** (9 posts and threads, table 2b).
- **Size estimates** (about 1 week each) are guesses, not a team's.
