# Task flows for Epic 1 (drawn 2026-11-16, read and accepted by the owner 2026-11-16)

**What this is:** two task flows for Epic 1, "Remove the barriers that keep caregivers from getting a real break," one per audience, in the same shape as the two Epic 3 flows (`task-flows-epic-3-2026-11-15.md`). They are drawn in Figma in the section "TASK FLOWS (Epic 1)," next to "TASK FLOWS (Epic 3)." This file is the master copy. The Figma boxes must say the same words.

**Why they exist:** the board's lesson "Task Flows" says they "describe the sequence, logic, and expected outcomes of use cases" and "show each step, the decisions that users or the system must make, and the paths that result in decisions being made" (Figma export `Task Flow.md`). The lecture says "There might be one flow chart that you put together per use case. And each ticket might have one to three or four use cases." The Epic 3 flows were done on 2026-11-15. On 2026-11-16 the owner listed task flows as a section to finish for the first 11 tasks, so the six Epic 1 pages get theirs. The earlier line "No task flow is drawn for Epic 1" on each Epic 1 page is replaced by a link to these flows.

**Why two flows, not six:** the Epic 3 decision stands. Use cases "change per audience" (the board's "Use Case Scenarios" lesson), and Morgan's and Lucy's boards each draw one flow. So Audience 1 gets one flow with three branches, and Audience 2 gets one flow with three branches. Each branch is one task page.

**What each flow draws:** only what the six approved Epic 1 pages say (`task-pages-epic-1-2026-11-15.md`). No screens or features are added. Each branch shows the happy path and the non-happy path, as the board asks. There is no consent check in these flows. The Epic 1 pages hold the caregiver's own records and a break plan, not health notes about the parent or partner, so the approved collect and share consents (T4.1.2) do not apply to them. Whether the caregiver's own records need a consent is a lawyer's question (risk profile, open question 1).

**Tags:** Claude's wording, drawn from the six pages. The owner read the flows on 2026-11-16 and said they are good.

## Flow 3: Audience 1, adult child. Getting a break and coping
Use cases "Getting relatives to cover time off" and "Handling guilt and setting limits they can keep" (feature 1.1). Tasks 1.1.1, 1.1.2 and 1.1.3. Three branches.
1. Start.
2. The caregiver signs in.
3. Choose one branch.
4. **Branch A, a break and who covers it (1.1.1):**
   1. The caregiver adds a break they want, with a start and end date.
   2. They choose who covers it: a relative, paid help they name, or no one yet.
   3. Decision: did the cover confirm?
      - Yes (happy path): the break shows as covered, with who and the dates. After the break, the caregiver records whether it happened. Decision: did the break happen? Yes: it shows as taken with the date. End.
      - The cover fell through (non-happy path): the break shows as not covered, the earlier person stays visible, and the break stays on the list. The caregiver chooses who covers it again (back to step 2).
5. **Branch B, how I am holding up, and one next step (1.1.2):**
   1. The caregiver writes how they are doing and one next step. Both are saved with the date, and only the caregiver can see them.
   2. They try the step, outside the app.
   3. Decision: did they do the step?
      - Yes (happy path): it shows as done with the date. End.
      - No (non-happy path): it shows as not done, the first check-in stays visible, and the caregiver can write a new next step (back to step 2).
6. **Branch C, a limit I set for myself (1.1.3):**
   1. The caregiver records a limit in their own words. It is saved with the date, and only the caregiver can see it.
   2. They try to keep it, outside the app.
   3. Decision: did they keep it?
      - Yes (happy path): it shows as kept with the date. End.
      - No (non-happy path): it shows as not kept, with no wording that blames the caregiver. The limit stays visible, and the caregiver can change it or record a new one (back to step 2).

## Flow 4: Audience 2, spouse or partner. People who understand, paperwork, and closeness
Use cases "Finding a support group or someone who understands," "Qualifying for help, including VA programs" and "Spouses keeping moments of closeness with their partner" (feature 1.2). Tasks 1.2.1, 1.2.2 and 1.2.3. Three branches. The third use case comes from the audience table, not from the 17 MVP use cases (`epic-and-feature-user-stories-2026-11-15.md`).
1. Start.
2. The caregiver signs in.
3. Choose one branch.
4. **Branch A, people who understand (1.2.1):**
   1. The caregiver adds a person or group who understands, with a note on how to reach them. It is saved, and only the caregiver can see it.
   2. They reach out, outside the app.
   3. Decision: is this still someone they can lean on?
      - Yes (happy path): the caregiver records that they reached out, and the entry shows the date they last reached out. End.
      - No (non-happy path): the caregiver removes the entry. It no longer appears, and the rest of the list stays as it was.
5. **Branch B, paperwork to qualify for help (1.2.2):**
   1. The caregiver records a program they are applying to and a step they need to do.
   2. They do the step, outside the app, and change where it stands.
   3. Decision: what happened?
      - A step is finished (happy path): it shows as finished with the date. End.
      - The program turns them down (non-happy path): it shows as turned down, the record stays visible, and the caregiver can add steps or record another program (back to step 1).
6. **Branch C, a moment of closeness (1.2.3):**
   1. The caregiver records a moment of closeness they want to keep, in their own words. It is saved with the date, and only the caregiver can see it.
   2. The moment comes, outside the app.
   3. Decision: did it happen?
      - Yes (happy path): it shows as happened with the date. End.
      - No (non-happy path): it shows as did not happen and stays visible. The caregiver can change it or record a new one (back to step 1).

## What is not drawn
- Advice on how to cope, which limits to set, who to lean on, which program to choose or how to be close. The saved research counts how often these problems come up but not what helps (open item on the pages).
- Finding or qualifying for a program, costs, and finding new support groups. They are outside the record-only slices.
- Crisis help. What the screen shows if someone writes about harming themselves is not decided (launch blocker, open on task 1.1.2).
- The checks that keep other circle members and people outside the circle from seeing a record. They are scenarios on each page (Scenario 4), not steps the caregiver takes, so the flows do not draw them.
- The rule that private records are visible only to the writer (T4.1.4) is still Proposed and open for a lawyer. The flows show it, they do not settle it.

## Known limits
- The two flows follow the six task pages, which are Claude's wording approved by the owner on 2026-11-15. If a page changes, the flow changes.
- The flows describe the record-only slices. They do not describe how the product would help a caregiver cope or get a break, because the research for that has not been done.
- The Epic 1 pages were written before the flows, so no flow step was checked against the pages by anyone but Claude.
