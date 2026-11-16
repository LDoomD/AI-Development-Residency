# Handoff: Caregiving Coordinator → task-level user stories and acceptance criteria (Epic 1 pages, then the check against the Basic homework) (2026-11-15, late)

> **Replaced by** `dogfood-2026-11-15-handoff-use-case-scenarios-and-share-consent.md` (2026-11-15, night). The Epic 1 pages, story fixes and technical requirements in this report are finished; start from the newer report.

Replaces: `dogfood-2026-11-15-handoff-week-2-3-repo-and-build-plan.md` (the earlier night report; its repository, build plan and Epic 3 task page work is finished, and the backlog file has moved on). Older reports stay replaced: `dogfood-2026-11-15-handoff-week-2-3-iteration-2.md`, `dogfood-2026-11-15-handoff-epics-features-notion-and-task-requirements.md`, `dogfood-2026-11-13-handoff-homework-hub-and-build-plan.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Run `git fetch`, `git status` and `gh pr list --state open`. Then show me section 4 decision 1 (the task 1.1.2 story) explained, before doing anything else. Explain every decision I must make: what it is, why it matters, the choices, what happens after each. Base everything on my up-to-date saved files and the three master reports, show the file and line for each fact, and write the user story as the course says (goal in I want, not the solution). Ask before Firecrawl, the browser pane or Chrome. Do one step at a time."

## 0. Start here
- **Where we are:** the user story statements at the epic level and the feature level are finished, corrected to the course rules, and saved in a file and in Notion. At the task level, 7 of the first 11 tasks have a story and a full task page (5 in Epic 3, 2 in Epic 1). Six of those seven pass the course rules. Task 1.1.2's story needs a rewrite (decision 1).
- **The outcome so far, in one sentence:** all 20 epic and feature stories now put the goal in "I want" and the value in "so that," as the course's user story lesson says, so task-level stories and acceptance criteria can follow the same rule.
- **Next milestone:** finish the four Epic 1 task pages still unwritten (1.1.3, 1.2.1, 1.2.2, 1.2.3), each starting with its user story and then its acceptance criteria and BDD scenarios, two pages at a time. Then the short check of the Basic homework items "technical requirements" and "user requirements," then the roadmap update. Source: `week-2-3-remaining-work-backlog-2026-11-15.md`, "Next, in this order," items 1 to 3.
- **Answer to the owner's question "when are we done with user stories and ready for acceptance criteria":** done at epic and feature level now. At task level the story is the first part of each task page, and the acceptance criteria are the next part of the same page. So the work moves to acceptance criteria one task at a time, once its story is approved. Task 1.1.2's story must be fixed first. The tasks in Epics 2, 4, 5 and 6 (16 tasks) wait. Basis: the backlog file says only the first two weeks are made ready.
- **Owner's track and scope (Approved 2026-11-15):** Premium, own app. Standard homework only. The owner will not do the bonus homework (pitch deck, prototypes, more flows) to catch up (`week-2-3-remaining-work-backlog-2026-11-15.md`, lines 16 to 21).

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| 10 epic-level and 10 feature-level user stories, all rewritten to the course rules: the goal is in "I want," and "so that" gives a value taken from the audience board's motivations. The wording is Claude's | **Approved** (owner, 2026-11-15, each rewrite approved before it was written) | `epic-and-feature-user-stories-2026-11-15.md` and Notion page "Epics and Features" (`cfc9219a469183c6945281ff637f4185`), read back |
| The 20 stories, as of today. Features 2.1, 2.2 and 6.1 and Epics 2 and 4 were rewritten after the rule check (7 changes). Epic 3's four stories were rewritten earlier. The other 9 passed as they were | **Approved** | `epic-and-feature-user-stories-2026-11-15.md` and Notion page "Epics and Features", read back |
| Feature-level use cases listed under six features: 1.1 (3), 1.2 (3), 2.1 (2), 2.2 (2), 4.1 (2), 5.1 (2). Features 3.1 and 3.2 were done earlier. **Features 4.2 and 6.1 are left empty** | **Approved** (owner: "leave 4.2 and 6.1 empty") | Same file ("Feature-level use case scenarios" section) and Notion |
| All 17 MVP use cases appear under exactly one feature, so the count matches Vision and Scope | **Approved**. Three placements are Claude's reading: "Getting relatives to cover time off" (1.1), "Finding a support group or someone who understands" and "Qualifying for help, including VA programs" (both 1.2) | `vision-and-scope-boards-2026-11-10.md` lines 97 to 108 and 168 to 174 (the 17 names); `epic-and-feature-user-stories-2026-11-15.md`, use case section |
| The four extra scenarios (know when to step in for safety; keep going after a refusal; raise hard topics without a fight; agree on who does what) count as **supported in MVP #1** | **Approved** (owner). The placement under tasks 3.1.2, 3.1.3, 3.2.1 and 3.2.2 is **Proposed** | `feature-stories-and-use-cases-epic-3-2026-11-15.md` (decision table) |
| Epic grouping stays as it is. A theme check found no missing scope outcome (27 of 27 tasks, 10 of 10 scope rows) | **Approved** (owner: "leave all of it as is"). No overlap notes were added | `epics-features-tasks-2026-11-11.md` |
| Standard homework only; pitch deck, prototypes and further flows are bonus | **Approved** | Backlog file |
| Empty public GitHub repository "Week 3 - Caregiving Coordinator" created. Build plan boxes 5 and 6 approved; T5 and T6 saved; Figma build plan section updated with the eight fixes | **Approved** (done by an earlier session today; I did not recheck it) | Backlog file lines 36 to 43; https://github.com/LDoomD/Week-3---Caregiving-Coordinator; Figma `3073:8029` |
| Epic 3's five task pages (full format) and Epic 1's pages 1.1.1 and 1.1.2 | Pages written and approved by the owner in the other session. The wording is Claude's (Proposed inside each page) | `task-pages-epic-3-2026-11-15.md`, `task-pages-epic-1-2026-11-15.md`, Notion |

## 2. Key findings and data
### The course's user story rules (the owner pasted the lesson on 2026-11-15; chat only, not saved to a file)
| Rule | What it says |
|---|---|
| Shape | One sentence. "As a [who], I want [goal], so that [why]." The "when" is optional |
| Goal, not solution | "I want" describes the user goal and not the how. "Sometimes the so that part is actually the goal, and you need to refine the statement so the goal is in the proper place." Take the goal from the problem checklist (the audience board) |
| The "so that" | Either the problem to avoid or the value. The rule of thumb: value at epic and feature level, problem to avoid at task level. The writer decides |
| Voice | Plain words, no jargon, concise, from the audience's side, in the persona's own tone. Each person who benefits gets a separate story |
| Where | Stories at every level. Epics and features get stories and no acceptance criteria. Tasks get stories plus acceptance criteria |

### Source of the "so that" values I used (Audience Segmentation Master Report data, `docs/sources/market-analysis-3/audience-v2/figma-teacher-format.json`)
| Audience | Motivations used |
|---|---|
| Audience 1 (adult child) | "Keeping their parent safe and comfortable"; "Doing the right thing and not carrying guilt or blame"; the vision statement's "keep their own health and life" |
| Audience 2 (spouse or partner) | "Keeping their partner safe, comfortable and with dignity"; "Doing right by their partner"; "Keeping their partner at home"; the vision statement's "keep their own health and life" |

Confidence: Credible secondary (the board is the owner's own synthesis of posts read by one person and not double-checked).

### Task-level story check, 2026-11-15 (Proposed, Claude's reading)
| Task | Verdict |
|---|---|
| 1.1.1, 3.1.1, 3.1.3, 3.2.1, 3.2.2 | Pass |
| 3.1.2 | Pass, with a note: "accept a safer move" in "I want" is the board's own task wording. Epic and feature stories use "get the help they need" instead. Left as it is |
| 1.1.2 | **Needs a look.** The story reads "I want to write down how I'm holding up and one step I'll take." "Write down" is a how (a feature). The goal is to cope with guilt and grief and know what to do next |

## 3. Excluded and deferred
- **Task pages and stories for Epics 2, 4, 5 and 6 (16 tasks).** Only the first two weeks are made ready (backlog file line 12 and "Later iterations").
- **The other student's heavy layout** (codes, emoji, a glossary page, a Notion overview mirroring the repo). Not copied. Only ideas worth borrowing: a short master-copy statement at the top, and full requirements for a few key tasks only.
- **A "Deliverables overview (for Claude)" Notion page** in the private homework hub. Never created; the owner has not approved it. Optional and last.
- **The six non-functional gaps** (input safety, reliability, accessibility gate, data-subject rights, policies and retention, quality gates). Raised earlier and not decided here.
- **Bonus homework:** pitch deck, prototypes, further task flows, use cases for other epics' tasks beyond the lists above.
- **"Not yet" items, off the owner's list until raised:** whether the Premium paper was submitted, and sharing the homework hub with the instructor.

## 4. Open decisions
The next session must not decide these alone.
1. **The story for task 1.1.2 ("Coping with guilt and grief, and knowing next steps").** What it is: the saved story names a feature ("write down") instead of the goal. Why it matters: the course says the goal belongs in "I want," and the task page's acceptance criteria are built on this story. Choices: (a) Claude drafts a corrected story with its source for the owner to approve, and then updates the Epic 1 file and the Notion page; (b) leave it as it is. After (a) the page's scenarios may need a check against the new goal.
2. **The extra Epic 3 section in Figma (node `3109:9375`).** What it is: a section I added at the owner's "yes" that shows the Epic 3 feature stories, situations, use cases and happy and non-happy paths at feature level. Why it matters: an earlier file records that the owner wanted Figma left as the instructor's template shows it, and that happy and non-happy paths belong at task level. The section's wording of the two feature stories is current. Choices: keep it; remove it; reduce it to stories and use case names. Nothing else depends on it.
3. **Whether to add the four supported scenarios to the use case lists in `vision-and-scope-boards-2026-11-10.md`.** What it is: that file lists 11 and 6 use cases and does not include the four scenarios. Why it matters: the file and the owner's decision now disagree. The owner asked why Vision and Scope would be changed while the work was on user stories, so nothing was changed. Choices: leave it and note the difference; add the four scenarios; add them as scenarios under their use cases. Nobody should change that file until the owner says so.
4. **Epic 1 open items from the other session (task 1.1.2, `task-pages-epic-1-2026-11-15.md` lines 195 to 200).** "Visible only to the writer" is proposed and not in the non-functional list; what happens if someone writes about harming themselves is not decided; a table for break records is not in the approved database list. These are a lawyer and developer-role questions. They are not for Claude to decide.
5. **Task wording.** The instructor's example tasks start with a verb (Help, Model, Develop). The owner's tasks are "-ing" outcome phrases. Raised earlier; not decided. It would change names in three places.
6. **Saving today's work.** Many files and the Notion edits are uncommitted (section 8). Per the project's rule, a new branch from `origin/main`, then a pull request. The owner decides when, and merges.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The course's user story rules (section 2) | Every new task-level story | Goal in "I want," problem to avoid in "so that" at task level |
| The approved 20 stories | The top of each task page's "Background" | The page's story must serve its feature's value |
| The 17 use cases placed under features | Each task page's "USE CASE" line | The Epic 1 pages already cite them, for example "Getting relatives to cover time off" (feature 1.1) |
| The Epic 3 pages (the pattern) | Pages 1.1.3, 1.2.1, 1.2.2, 1.2.3 | Same eight headings, INVEST grades, BDD scenarios and sources |
| Features 4.2 and 6.1 have no use case | Any later pages in those features | Their tasks will have no use case to cite until the four off-MVP use cases return in MMP |

## 6. First steps
1. Confirm where we are in a few sentences. Run `git fetch`, `git status` and `gh pr list --state open`. Check whether the current branch has already been merged and, if so, start a new branch from `origin/main` for any commit.
2. Read the files in section 8, then the five Epic 3 task pages and the two Epic 1 pages in `docs/clean-deliverables/`.
3. Show the owner decision 1 explained and wait. If the owner approves a corrected 1.1.2 story, show the old and new sentence and its source, then update the saved file and the Notion page, and read the Notion page back.
4. Then write task 1.1.3's story first, check it against the course rules in section 2, show it to the owner, and only then write its acceptance criteria and BDD scenarios. Do 1.2.1, 1.2.2 and 1.2.3 the same way, two at a time. Use the `invest-task-scoping` skill, one page at a time; grades go in the saved file, not the chat.
5. When the four pages are done, do backlog item 2 (a short read of the pages against "technical requirements" and "user requirements") and item 3 (the roadmap), showing each before writing.
6. Remind the owner to save the work in a pull request and write a new handoff report before compacting.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory (`MEMORY.md`). The ones most likely to break next:
- **Search for existing files before writing a new one.** Today I wrote an Epic 3 file that duplicated a committed file from earlier work. I deleted it after the owner approved. Run `ls docs/clean-deliverables` and grep for the topic first.
- **Read the whole lesson before applying a rule.** I applied only the "so that" note first and over-corrected. The owner had to paste the full section.
- **Explain every decision** (what, why, choices, what happens after). Complete sentences. No shorthand.
- **Show new wording before writing it, then read it back.** Saved file first, then Notion and Figma. The same words in all three.
- **Notion edits use exact old text.** Fetch the page and read it back after each change.
- **Tag Claude's own wording Proposed.** Quote the owner's own decisions as Approved with the date.
- **Do one step at a time.** Do not offer the next step unasked, and do not edit Vision and Scope or any other file the current step does not need. A question gets an answer, not an edit.
- **Never write the owner's "What I Did," "What I Learned" or one-page summary.**
- **Ask before Firecrawl, the browser pane or Chrome.** Never change sharing settings.
- **Laws: never conclude. Never say "compliant."**
- **Do not move the owner's Figma boxes.** The owner reorganizes by hand.

## 8. Where things live
- **User stories and use cases (all in `docs/clean-deliverables/`):** `epic-and-feature-user-stories-2026-11-15.md` (20 stories, the use case section, "Known limits"), `feature-stories-and-use-cases-epic-3-2026-11-15.md` (Epic 3, the decision on four scenarios), `epics-features-tasks-numbered-2026-11-15.md`, `epics-features-tasks-2026-11-11.md`.
- **Task pages and flows:** `task-pages-epic-3-2026-11-15.md`, `task-pages-epic-1-2026-11-15.md`, `task-flows-epic-3-2026-11-15.md`, `notion-backlog-2026-11-11.md`.
- **Order of work:** `week-2-3-remaining-work-backlog-2026-11-15.md` (current; its iteration log was last updated by the other session).
- **Vision, scope and the master reports:** `vision-and-scope-boards-2026-11-10.md`; audience data in `docs/sources/market-analysis-3/audience-v2/` (`uc-A1.json`, `uc-A2.json`, `figma-teacher-format.json`); the three master reports in `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/`.
- **Figma file `HcDDdEGAnikTImO8v7UPMp`, page "Updated Deliverables" (`2782:15415`):** Create Epics, Features, Tasks `3068:9983`; functional green list `3093:9247`; the Epic 3 section I added `3109:9375`; non-functional list `3094:9079`; task flows `3097:9079`; build plan `3073:8029`; roadmap `3068:9448`; the course tip text box `3068:10002`.
- **Notion (workspace "Orlando's Notion"):** Epics and Features page `cfc9219a469183c6945281ff637f4185`. Epic 3 task pages: 3.1.1 `47c9219a469183f39d35016e94ec08e8`, 3.1.2 `4159219a469181b793ffeaf1b2e3d74d`, 3.1.3 `4159219a46918192bba3c7710c0fe790`, 3.2.1 `4159219a469181a5be2be352b2b768fe`, 3.2.2 `4159219a469181bc9721f77519efe07a`. The Epic 1 pages 1.1.1 and 1.1.2 were written by the other session; their Notion ids are in `task-pages-epic-1-2026-11-15.md` or the Notion board. Submission page `4179219a-4691-8157-976e-dbc20a0a829f`.
- **Git (checked 2026-11-15 late):** branch `epics-numbered-stories-task-pages-2026-11-15`, last commit `618a12b`. Pull requests 53, 54 and 55 are merged (55 on 2026-11-15, 22:38). `gh pr list` showed no open pull request. **Uncommitted changes:** `epic-and-feature-user-stories-2026-11-15.md`, `feature-stories-and-use-cases-epic-3-2026-11-15.md`, `non-functional-epics-features-tasks-2026-11-15.md`, `task-pages-epic-3-2026-11-15.md`, `week-2-3-remaining-work-backlog-2026-11-15.md`, `docs/sources/INDEX.md`. **Untracked:** `task-pages-epic-1-2026-11-15.md`, `docs/build-plan-nfr-draft-2026-11-12.md`, `docs/sources/build-plan-2026-11-12/`, and this report. Also untracked and not part of this work: `il.html` and `dogfood-2026-11-05-audit-and.textClipping`.
- **Another session:** a forked session ("Dog feeding report review (fork)") wrote the repository, build plan, task page rewrites and the Epic 1 pages. Read its output files before changing them.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-15. The Notion page was fetched and compared after each of the five update rounds.
- **Checks run:**
  - After each story or use case rewrite, the saved file was searched for leftover old wording: none remained in `epic-and-feature-user-stories-2026-11-15.md`.
  - The Notion "Epics and Features" page was fetched after each update. All 20 stories and the six use case lists match the saved file.
  - Figma: the two Epic 3 feature story sentences were read back from node `3109:9376`.
  - The task-level check read the story line of each of the 7 saved task pages.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - Whether Notion copies of the task-level stories match the saved task page files, and the five full backlog pages from 2026-11-11.
  - The build plan, T5 and T6, the repository and the Figma build plan update: reported by the backlog file, not re-verified by me.
  - Whether PR 55 contains everything, and whether the current branch is stale.
  - The Epic 1 Notion page ids; the other session wrote them.
  - The use case count (22 in Figma's "Key Use Cases" box against 17 in Vision and Scope) was flagged earlier and is not resolved.
  - The course's user story lesson was read from the owner's paste, not from the saved course copy.
- **How this prevents drift:** Approved and Proposed tags separate decisions from suggestions. Decisions 1 to 6 stop the next session from deciding for the owner. The first step requires a git check and owner review before any writing. The saved files are the master copies, and Notion and Figma must say the same words.
