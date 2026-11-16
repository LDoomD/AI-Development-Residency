# Handoff: Caregiving Coordinator → use case scenarios check, the share-consent gap, then the release roadmap (2026-11-15, night)

Replaces: `dogfood-2026-11-15-handoff-task-stories-and-acceptance-criteria.md` (its Epic 1 pages, story fixes and technical requirements work is now finished). Older reports stay replaced: `dogfood-2026-11-15-handoff-week-2-3-repo-and-build-plan.md`, `dogfood-2026-11-15-handoff-week-2-3-iteration-2.md` and earlier.

> **Update 2026-11-16 (read this first):** the work this report points to is done. Section 4 decision 1 (share consent) was approved and applied to all five Epic 3 pages and their Notion cards. Decision 4 (the submission-page row) was applied. Use case scenarios, BDD and technical acceptance were checked on all 11 pages. Epic 1 task flows (Flow 3 and Flow 4) were drawn in Figma (`3118:9375`) and saved in `task-flows-epic-1-2026-11-16.md`. Still open: decisions 2 and 3 (lawyer questions), the owner reading the Epic 3 developer rules and the Epic 1 flows, and backlog item 3 (release roadmap). The iteration log in `week-2-3-remaining-work-backlog-2026-11-15.md` has the detail.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Run `git fetch`, `git status` and `gh pr list --state open`. Then show me section 4 decision 1 (the missing share-consent scenario on the five pages about getting a parent or partner to accept help), explained, before doing anything else. Use plain words, not the words 'epic' or 'technical requirements' without saying what they mean. Give a recommendation with every decision. Check every fact against my saved files and show the file and line. Read back every Notion and Figma change after writing it. Ask before Firecrawl, the browser pane or Chrome. One step at a time."

## 0. Start here
- **Where we are:** user story statements are finished at every level. Acceptance criteria (the whole task page: story, background, goal, checklist called "Acceptance," example situations called scenarios, and a developer section called "Technical Requirements") are finished for all 11 first task pages. Each page is saved in a file and filled on its Notion card, and all 11 cards were read back on 2026-11-15.
- **The outcome so far, in one sentence:** the 6 pages for "Remove the barriers that keep caregivers from getting a real break" (Epic 1) and the 5 pages for "Increase how often a parent or partner accepts outside help" (Epic 3) now hold a goal-based story, a checklist that says what is needed and not how to build it, scenarios with happy and non-happy paths, and developer-role rules tied to the approved non-functional list.
- **Next milestone:** the board's next section, **use case scenarios**, then task flows, BDD and the rest of the task-level lesson. The lecture says each task has one to four use cases, each with a happy and a non-happy path. All 11 pages already list theirs, so the first job is to check that with the owner, not to assume there is work.
- **The owner's words that set the pace (2026-11-15):** "I have my approval for everything, let's complete this acceptance criteria already and move on to the next section, which is use case scenarios." The owner also asked for data-driven work, verified against files, never assumed.
- **Method (Approved):** agile. Standard homework only. Premium track, own app. The owner follows the Figma lecture board in the order of its sections.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| 20 epic and feature user stories, all to the course rule (goal in "I want") | **Approved** | `epic-and-feature-user-stories-2026-11-15.md`, Notion "Epics and Features" `cfc9219a469183c6945281ff637f4185` |
| Features 4.2 and 6.1 list their four MMP use cases marked "MMP, not in MVP #1." Option 1 of three, chosen by the owner | **Approved** | Same file and Notion page, read back |
| Feature 1.2 also lists "Spouses keeping moments of closeness with their partner" (audience table, `Audience Use Cases.csv` line 116), marked as not in the 17 MVP use cases. It is in neither the 6 MVP nor the 4 MMP lists | **Proposed by Claude, applied under the owner's blanket approval** | Same file and Notion page |
| Task 1.1.2 story rewritten: "I want to cope with my guilt and grief and know what to do next, so that I don't carry them alone until I burn out." Its Acceptance reworded as needs | **Approved** (each shown first) | `task-pages-epic-1-2026-11-15.md`, Notion `4159219a469181adba5fd537641f80f8` |
| New pages 1.1.3, 1.2.1, 1.2.2 and 1.2.3, each with a story, Acceptance, four scenarios and developer section. The story for each was approved before the page was written | **Approved** | Same file; Notion `4159219a469181c18b02c76cb46c35c4`, `4159219a4691813b8a57c73044940a60`, `4159219a469181fc9cd8dd627cde0606`, `4159219a469181abbf15d45cf8e518bf` |
| Developer-role rules for the six Epic 1 pages: tables `care_breaks` (circle-visible) and one shared `private_records` (owner-only); no status history table; no access log for private records; "a real break" means a break marked happened | **Approved** (owner approved the draft with Claude's recommendations) | Epic 1 file, Technical Requirements sections; Notion cards |
| Checklist lines and definition of done on 1.1.1 and the five Epic 3 pages reworded as needs (record, say, see and change; no "mark," "note," "add," "choose") | **Approved** (owner's blanket approval) | `task-pages-epic-1-...` and `task-pages-epic-3-2026-11-15.md`; Notion cards, read back |
| Developer-role rules for the five Epic 3 pages (tables `care_notes` and `care_tasks` from the approved list, access, deletion, counting, checks) | **Approved only under the blanket approval; the owner has not read this draft.** Claude changed one line and flagged another (section 4) | Epic 3 file; Notion cards, read back |
| T4.1.4 (private records visible only to the writer) and T2.1.3 (the Epic 1 tables) added to the non-functional list | **Proposed.** T4.1.4 is open for a lawyer. T2.1.3 follows the approved Epic 1 draft | `non-functional-epics-features-tasks-2026-11-15.md`; Figma T4 box `3094:9083`, T2 box `3094:9081` |
| Notion submission page "Week 2 and 3 - Product Specifications" updated in five places | **Approved** (owner said yes after seeing the old and new lines) | Notion `4179219a-4691-8157-976e-dbc20a0a829f`, read back |

## 2. Key findings and data
| Finding | Detail | Source | Confidence |
|---|---|---|---|
| What the course means by technical requirements | "How to design the database, how to flow the data," what a developer or architect decides. Claude plays that role and the product manager checks it | Week 2 lecture transcript 1:07:40 to 1:09:26; Figma board "Technical Acceptance": "DO NOT WRITE TECHNICAL REQUIREMENTS YOURSELF" | Authoritative (course) |
| What the board says acceptance criteria must do | Dictate the need, not the solution; cover the user, business and technical need; be explicit ("if it's not in here, it doesn't exist") | Figma node `3079:16725`, and the owner's two markdown exports in `/Users/landodoom/Desktop/Figjam_.md_files/` | Authoritative (course) |
| What use case scenarios are | A scenario you decide to support; each task has one to four; each needs a happy and a non-happy path | Lecture transcript 1:02:54 to 1:05:10; lecture notes lines 134 to 146; board section "Use Case Scenarios" | Authoritative (course) |
| No Epic 3 page mentions the separate share consent | The approved list requires a separate share consent (T2.2.4, T4.1.2) and the risk profile says consent to share is a separate step (lines 38 to 40). The five pages test only the collect consent | `grep "share consent"` on `task-pages-epic-3-2026-11-15.md` returned nothing | Authoritative (our own files) |
| T2.2.3 says "Deleting a cared-for person or a caregiver also deletes the health data entered about that person" | It does not say deleting a caregiver deletes the notes that caregiver wrote. Risk profile line 52 says an account deletion "must also handle the data they entered" | NFR file line 41; risk profile line 52 | Authoritative (our own files) |
| Atlassian's acceptance criteria article | Story says why, criteria say what success looks like; five traits (clear, testable, outcome not recipe, measurable, independent). It is a vendor article, not the course rulebook | `atlassian.com/work-management/project-management/acceptance-criteria`, read with Firecrawl on 2026-11-15 | Credible secondary |
| The closeness scenario is in no use case list | Not in the 6 MVP use cases (`vision-and-scope-boards-2026-11-10.md` lines 168 to 174) or the 4 MMP ones (line 176) | Same file and `Audience Use Cases.csv` line 116 | Authoritative |

## 3. Excluded and deferred
- **Task pages for the 16 tasks in Epics 2, 4, 5 and 6.** The lecture says to make only the next two weeks ready. Backlog file, "Later iterations."
- **Bonus homework:** pitch deck, prototypes, extra task flows.
- **A status history table, an access log for private wellbeing records, and advice text on coping or on what parents accept.** Decided or left out on purpose; advice needs research the saved files do not have.
- **Lawyer questions, not Week 4 decisions:** whose consent counts for a parent or partner who never signs up; other people's names and notes about a partner's benefits or relationship; behavior if someone writes about self-harm (a launch blocker).
- **"Not yet" items, off the list until the owner raises them:** whether the Premium paper was submitted, and sharing the Notion page with the instructor.

## 4. Open decisions
The next session must not decide these alone. Each needs a recommendation and what happens after.
1. **Add the share-consent check to the five Epic 3 pages (3.1.1, 3.1.2, 3.1.3, 3.2.1, 3.2.2).** What it is: the approved list says nothing is shared with another member without a separate share consent, but no page has a checklist line or scenario for it. Why it matters: without one, nothing would catch a relative seeing a parent's notes too early. Choices: (a) add one checklist line and one scenario to each page (recommended); (b) leave it recorded as open on each page, which is the current state. After (a), the saved file and five Notion cards change and the Open line on each page shrinks.
2. **The deletion reading on the five Epic 3 pages.** The draft says deleting a caregiver deletes the notes that caregiver wrote. T2.2.3 does not say that. The pages label it a proposed reading. Choices: approve it, or leave it open. Recommendation: leave it open until a lawyer answers the consent question.
3. **T4.1.4 (private records visible only to the writer).** Still Proposed. Five Epic 1 pages depend on it. It is open for a lawyer too.
4. **Three Notion submission page lines are out of date.** The row "Technical requirements and user requirements" still says the five Epic 3 pages "leave anything beyond [the approved rules] to the developer role." That is no longer true. Show the new line before changing it.
5. **Saving the work.** Pull request 57 holds only the earlier Epic 1 work. The Epic 1 file, the Epic 3 file and the backlog file have newer edits that are not committed. The owner merges. The next pull request should start from a merged `main`.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Each page's "Use Cases to Support" (happy and non-happy paths) | The use case scenarios section | The board and lecture say each task has one to four use cases with both paths |
| The Epic 3 task flows (`task-flows-epic-3-2026-11-15.md`, Figma `3097:9079`) | The task flows section | Already drawn as bonus work; the lecture says one flow per use case |
| The four scenarios on each page (Given, When, Then) | The BDD section | The board says BDD scenarios are an addition to the acceptance criteria |
| The developer sections and T2.1.3, T4.1.4 | The "Technical Acceptance" section | Same content; confirm with the owner whether more is needed |
| Any change to slices or dates | The release roadmap (`3068:9448`, `release-roadmap-2026-11-11.md`) and the Notion board | Backlog item 3. It is a separate deliverable and comes after the task pages |

## 6. First steps
1. Confirm where we are in a few sentences. Run `git fetch`, `git status` and `gh pr list --state open`. Check whether PR 57 was merged. Check the other session ("Week 2/3," idle when this report was written) before editing the same files.
2. Read the files in section 8, then the 11 pages' Technical Requirements and Open lines.
3. Show the owner decision 1 explained, with the recommendation, and wait.
4. If approved, add one checklist line and one scenario to each of the five Epic 3 pages in the file, show the exact lines first, then update the five Notion cards and read each back.
5. Show the owner the corrected submission-page lines (decision 4) and update that page after a yes.
6. Then check the use case scenarios section against the 11 pages with the owner. Say plainly what each page already has. Do not invent work.
7. Remind the owner to save the work in a pull request, and write a new handoff report before compacting.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory (`MEMORY.md`). The ones most likely to be broken next:
- **Plain words, every time.** The owner did not understand "epic," "technical requirements" and "acceptance criteria" as used. Say what each means the first time and name pages by their titles.
- **Every decision needs a recommendation and what happens after each choice.** The owner said "I don't know, you're having me make a decision that affects this product. If you do, tell me."
- **Check every fact against the saved files and show the file and line.** The owner said not to assume. Read the file before making a claim. Do not cite line numbers you have not read in this chat.
- **Read back every Notion and Figma write.** Fetch the page after each update.
- **Explain the reasoning behind any grade or structure.** Showing a list of "fails" with no reason upset the owner.
- **One step at a time. Do not jump to the next backlog item.** The owner stopped the move to the roadmap because task-level work was unfinished.
- **Questions get answers, not edits.**
- **The course board's rules for acceptance:** the goal in "I want," the problem to avoid in "so that" for tasks, needs not solutions, explicit lines.
- **Never write the owner's "What I Did," "What I Learned" or one-page summary.**
- **Ask before Firecrawl, the browser pane or Chrome.** The owner approved Firecrawl once for the Atlassian page. Never change sharing settings.
- **Do not move the owner's Figma boxes.** Laws: never conclude, never say "compliant."

## 8. Where things live
- **Task pages and stories (all in `docs/clean-deliverables/`):** `task-pages-epic-1-2026-11-15.md` (six pages), `task-pages-epic-3-2026-11-15.md` (five pages), `epic-and-feature-user-stories-2026-11-15.md` (20 stories and the use case lists), `non-functional-epics-features-tasks-2026-11-15.md` (T1 to T6, T2.1.3, T4.1.4), `week-2-3-remaining-work-backlog-2026-11-15.md` (order of work and iteration log), `task-flows-epic-3-2026-11-15.md`, `vision-and-scope-boards-2026-11-10.md`, `release-roadmap-2026-11-11.md`.
- **Master reports and data:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/` (Audience Segmentation, Competative Analysis, Market Analysis). Audience CSV: `Data Tables_Audience Segmentation/Audience Use Cases.csv`. Risk profile: `docs/risk-profile.md`.
- **Course material:** `.claude/skills/residency-context/reference/week-2-3.md` and `week-2-3-submit-checklist.md` (one folder above the repo); lecture transcript and notes in `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/`. The owner's Figma exports are in `/Users/landodoom/Desktop/Figjam_.md_files/`.
- **Figma file `HcDDdEGAnikTImO8v7UPMp`, page "Updated Deliverables":** the instructor's task-level lesson `3079:16725`; non-functional list `3094:9079` (T2 box `3094:9081`, T4 box `3094:9083`); task flows `3097:9079`; roadmap `3068:9448`; build plan `3073:8029`.
- **Notion:** Epics and Features `cfc9219a469183c6945281ff637f4185`. Epic 1 cards: 1.1.1 `4159219a-4691-8136-b33e-dd1edca61ce9`, 1.1.2 `...81ad-ba5f-d537641f80f8`, 1.1.3 `...81c1-8b02-c76cb46c35c4`, 1.2.1 `...813b-8a57-c73044940a60`, 1.2.2 `...81fc-9cd8-dd627cde0606`, 1.2.3 `...81ab-bf15-d45cf8e518bf` (all prefixed `4159219a-4691-`). Epic 3 cards: 3.1.1 `47c9219a-4691-83f3-9d35-016e94ec08e8`, 3.1.2 `4159219a-4691-81b7-93ff-eaf1b2e3d74d`, 3.1.3 `4159219a-4691-8192-bba3-c7710c0fe790`, 3.2.1 `4159219a-4691-81a5-be2b-e352b2b768fe`, 3.2.2 `4159219a-4691-81bc-9721-f77519efe07a`. Submission page `4179219a-4691-8157-976e-dbc20a0a829f`.
- **Git (checked 2026-11-15 night):** branch `epic-1-pages-technical-requirements-2026-11-15`, last commit `b23fd64`. Pull request 57 is open: https://github.com/LDoomD/AI-Development-Residency/pull/57 (no checks on the repository). **Uncommitted:** `task-pages-epic-1-2026-11-15.md`, `task-pages-epic-3-2026-11-15.md`, `week-2-3-remaining-work-backlog-2026-11-15.md`, and this report. Also untracked and not part of this work: `il.html` and `dogfood-2026-11-05-audit-and.textClipping`.
- **Another session:** "Week 2/3," a Claude Desktop session, was idle at the time of writing. Read its output before changing shared files.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-15. Quoted lines were read in this session from the saved files named.
- **Checks run:**
  - All six Epic 1 cards and all five Epic 3 cards were fetched and compared with the saved files after each write (Acceptance, definition of done and Technical Requirements).
  - The Epics and Features page and the submission page were fetched after changes.
  - The Figma T2 and T4 boxes were checked for font, size and a screenshot of the T4 box.
  - The draft's claims about T2.2.3, T2.2.4, T6.2.2, T6.4.1, T6.4.2 and the risk profile were checked against the files. One was corrected (the deletion reading) and one extended (all five pages lack a share-consent line, not three).
  - A key and password scan of the four files in pull request 57 found only a sentence about what to do if a key leaks.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - The other five Figma boxes of the non-functional list after adding T2.1.3.
  - Whether each Epic 3 scenario still matches its reworded Acceptance line by line.
  - What the other session changed.
  - The line numbers the developer-role agent cited in its own report. I did not verify them.
  - The Epic 3 developer draft was never read by the owner.
  - The use case count (22 in Figma's Key Use Cases box against 17 in Vision and Scope) is still unresolved.
- **How this prevents drift:** Approved and Proposed tags separate decisions from suggestions. The first step stops for the owner on decision 1. The saved files are the master copies and Notion must say the same words. The rules in section 7 come from the owner's complaints in this session.
