# Task flows for Epic 3 (approved 2026-11-15)

**What this is:** one task flow per Epic 3 use case, drawn in Figma in the section "TASK FLOWS (Epic 3)" inside "Create Epics, Features, Tasks." This file is the master copy. The Figma boxes must say the same words.

**Why:** the instructor's board lists Task Flows as a Week 2 deliverable under the Requirements milestone. The lecture says "There might be one flow chart that you put together per use case. And each ticket might have one to three or four use cases." Task flows "show each step, the decisions that users or the system must make, and the paths that result in decisions being made" (instructor's board, "Task Flows"). The board also asks for both the happy path and the non-happy path.

**What each flow draws:** only what the five approved Epic 3 task pages do (`task-pages-epic-3-2026-11-15.md`). No screens or features are added. The consent check comes from the approved rule T4.1.2 in `non-functional-epics-features-tasks-2026-11-15.md`: no health note is saved without a collect consent.

**Tags:** the flows are Claude's wording (Proposed), approved by the owner on 2026-11-15. Boxes carry the task number they belong to.

## Flow 1: Getting the parent to accept outside help
Use case 1. Tasks 3.1.2 (a safer move) and 3.1.3 (paid help or aids).
1. Start.
2. The caregiver raises a safer move, or paid help or aids, with the parent, outside the app.
3. The caregiver opens the care circle.
4. Decision: is the collect consent recorded?
   - No: the note is not saved, and the caregiver is asked to record consent first.
   - Yes: continue.
5. The caregiver notes the date and what the parent said (3.1.2, 3.1.3).
6. Decision: what did the parent answer?
   - Accepted (happy path): it shows as accepted with the date. End.
   - Not yet or refused (non-happy path): the caregiver notes the reason and one next step, and the item stays open. Go to Flow 2.

## Flow 2: Trying small steps when the answer is no
Use case 2. Tasks 3.1.1 and 3.1.3.
1. Start from an agreed health step (3.1.1) or from an open item with a next step (3.1.3).
2. The caregiver tries the step with the parent, outside the app.
3. The caregiver records what happened.
4. Decision: did the parent follow through or accept?
   - Yes (happy path): it shows as done or accepted and leaves the open list. End.
   - No (non-happy path): the caregiver adds another next step, the earlier steps stay visible, and the item stays open. The next try goes back to step 2.

## Flow 3: Spouses bringing in help the partner will accept
The use case "Spouses bringing in help the partner will accept," with two of its scenarios. Tasks 3.2.1 and 3.2.2. Pairing a scenario with a task is Claude's reading of the audience table.
1. Start.
2. The caregiver opens the care circle.
3. Decision: is the collect consent recorded? No: nothing is saved, and the caregiver is asked to record consent first. Yes: choose one branch.
4. **Branch A, plan a topic (3.2.1, scenario "raise hard topics without a fight"):**
   1. The caregiver adds a topic.
   2. They talk with the partner, outside the app.
   3. Decision: how did it go?
      - Calm or agreed (happy path): it shows as agreed with the date. End.
      - Turned into a fight (non-happy path): it stays open with a note on what to try next time. The next try goes back to the talk.
5. **Branch B, who does what (3.2.2, scenario "agree on who does what"):**
   1. The caregiver adds a care task or a money task.
   2. They choose who handles it: the caregiver, the partner, or a helper they name.
   3. Decision: did they agree?
      - Yes (happy path): it shows that person and the date. End.
      - No (non-happy path): it is marked not agreed with a note on why, and it stays open.

## What is not drawn
- Advice on how to raise a topic, a move or a next step. The saved research does not say what works (open item).
- Inviting other people by email, money records, and reminders.
- The scenario "bring in help the partner will accept" (a helper): no Epic 3 task covers it yet.
- The consent rule for a parent or partner who never signs up is unresolved (risk profile, open question 1, needs a lawyer). The flows show the check, not the answer.

## Known limits
- The three flows follow the five task pages, which are Claude's wording approved by the owner. If a page changes, the flow changes.
- Flows describe the record-only slices. They do not describe how the product would help a parent accept, because the research for that has not been done.
