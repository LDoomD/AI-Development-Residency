# Task flows for Epic 3 (approved 2026-11-15)

**What this is:** two task flows for Epic 3, one per audience, drawn in Figma in the section "TASK FLOWS (Epic 3)" inside "Create Epics, Features, Tasks." This file is the master copy. The Figma boxes must say the same words.

**Why two flows (changed 2026-11-15):** the first version had three flows, one per use case, because the lecture says "one flow chart per use case." Morgan's and Lucy's boards each have one flow, and the instructor's board says use cases "change per audience." The first two flows were really one story for Audience 1: the "parent says no" ending of the first is the starting point of the second, so they were joined as Part 1 and Part 2 of one flow. The owner found the first merged version confusing (an unclear connector label and no explanation), so on 2026-11-15 the parts got headings. The owner then pointed out that the junction still repeated itself and said "stays open," so the junction and the "stays open" boxes were reworded in plain words. Audience 2 keeps its own flow. Each flow shows both the happy path and the non-happy path, as the board asks. A happy-path-only narrative, like Lucy's, is left for the pitch deck.

**Why flows at all:** the instructor's board lists Task Flows as a Week 2 deliverable under the Requirements milestone. The lecture says "There might be one flow chart that you put together per use case. And each ticket might have one to three or four use cases." Task flows "show each step, the decisions that users or the system must make, and the paths that result in decisions being made" (instructor's board, "Task Flows"). The board also asks for both the happy path and the non-happy path.

**What each flow draws:** only what the five approved Epic 3 task pages do (`task-pages-epic-3-2026-11-15.md`). No screens or features are added. The consent check comes from the approved rule T4.1.2 in `non-functional-epics-features-tasks-2026-11-15.md`: no health note is saved without a collect consent.

**Tags:** the flows are Claude's wording (Proposed), approved by the owner on 2026-11-15. Boxes carry the task number they belong to.

## Flow 1: Audience 1, adult child. Getting the parent to accept help, then trying small steps
Use cases 1 and 2. Tasks 3.1.1, 3.1.2 and 3.1.3. It is one continuous story in two parts. Part 1 is raising something with the parent and recording the answer. If the parent says not yet or no, the caregiver writes down the reason and one thing to try, and the flow continues into Part 2, where the caregiver tries that step. The connector between the parts reads "Then the caregiver tries that step with the parent (Part 2)."

**Part 1 (use case 1; tasks 3.1.2 and 3.1.3): the caregiver raises it with the parent and records the answer**
1. Start.
2. The caregiver raises a safer move, or paid help or aids, with the parent, outside the app.
3. The caregiver opens the care circle.
4. Decision: is the collect consent recorded?
   - No: the note is not saved, and the caregiver is asked to record consent first.
   - Yes: continue.
5. The caregiver notes the date and what the parent said (3.1.2, 3.1.3).
6. Decision: what did the parent answer?
   - Accepted (happy path): it shows as accepted with the date. End.
   - Not yet or refused (non-happy path): the caregiver writes down why the parent said no and one thing to try next, and the item stays on the list. The arrow from that box into Part 2 reads "Then the caregiver tries that step with the parent (Part 2)."

**Part 2 (use case 2; tasks 3.1.1 and 3.1.3): when the answer is no, or a health step was agreed, the caregiver tries small steps**
1. Start from the open item in Part 1, or start here when the parent agreed to a health step (3.1.1). The second start box reads "Also start here: the parent agreed to a health step (3.1.1)."
2. The caregiver tries the step with the parent, outside the app.
3. The caregiver records what happened (3.1.1, 3.1.3).
4. Decision: did the parent follow through or accept?
   - Yes (happy path): it shows as done or accepted and comes off the list. End.
   - No (non-happy path): the caregiver adds another thing to try (3.1.3), the earlier ones stay visible, and the item stays on the list. The loop back to step 2 reads "Try again with the new step."

## Flow 2: Audience 2, spouse or partner. Bringing in help the partner will accept
The use case "Spouses bringing in help the partner will accept," with two of its scenarios. Tasks 3.2.1 and 3.2.2. Pairing a scenario with a task is Claude's reading of the audience table.
1. Start.
2. The caregiver opens the care circle.
3. Decision: is the collect consent recorded? No: nothing is saved, and the caregiver is asked to record consent first. Yes: choose one branch.
4. **Branch A, plan a topic (3.2.1, scenario "raise hard topics without a fight"):**
   1. The caregiver adds a topic.
   2. They talk with the partner, outside the app.
   3. Decision: how did it go?
      - Calm or agreed (happy path): it shows as agreed with the date. End.
      - Turned into a fight (non-happy path): the topic stays on the list, with a note on what to try next time. The next try goes back to the talk.
5. **Branch B, who does what (3.2.2, scenario "agree on who does what"):**
   1. The caregiver adds a care task or a money task.
   2. They choose who handles it: the caregiver, the partner, or a helper they name.
   3. Decision: did they agree?
      - Yes (happy path): it shows that person and the date. End.
      - No (non-happy path): it is marked not agreed, with a note on why, and the task stays on the list.

## What is not drawn
- Advice on how to raise a topic, a move or a next step. The saved research does not say what works (open item).
- Inviting other people by email, money records, and reminders.
- The scenario "bring in help the partner will accept" (a helper): no Epic 3 task covers it yet.
- Paid help or aids for a parent is covered by task 3.1.3 (widened 2026-11-15), shown in Flow 1.
- The consent rule for a parent or partner who never signs up is unresolved (risk profile, open question 1, needs a lawyer). The flows show the check, not the answer.

## Known limits
- The two flows follow the five task pages, which are Claude's wording approved by the owner. If a page changes, the flow changes.
- Flows describe the record-only slices. They do not describe how the product would help a parent accept, because the research for that has not been done.
