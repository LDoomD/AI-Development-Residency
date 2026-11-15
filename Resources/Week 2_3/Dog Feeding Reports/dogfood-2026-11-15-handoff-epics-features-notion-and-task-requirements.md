# Handoff: Caregiving Coordinator → Epics, Features and Tasks requirements in Notion, with Figma kept in step (2026-11-15)

Replaces: `dogfood-2026-11-13-handoff-homework-hub-and-build-plan.md`. Everything in it still holds except what sections 1 to 4 below change. Older reports stay replaced: `dogfood-2026-11-13-handoff-build-plan-fixes-and-course-sources.md`, `dogfood-2026-11-12-handoff-build-plan-fixes-and-week-2-status.md`, `dogfood-2026-11-12-handoff-build-plan-week-4-fixes.md`, `dogfood-2026-11-12-handoff-build-plan-and-nfr.md`, `dogfood-2026-11-11-handoff-requirements.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Then show me the Notion text for all 10 features (section 2, table 'Feature-level text') and wait for my yes before writing anything to Notion or Figma. Explain every decision I must make: what it is, why it matters, the choices, what happens after each. Base everything on my most up-to-date deliverables and the three master reports. Ask before using Firecrawl, the browser pane or Chrome."

## 0. Start here
- **Where we are:** the 8 build plan fixes are applied to the build plan markdown file. The feature-level user stories and use case lists for Epic 3 are saved and approved. The owner decided to follow the instructor's own templates, which put stories and use cases in two Notion places (the Epics and Features page and the 11 task pages) and leave the Figma epic, feature and task boxes as the instructor's template shows them.
- **The outcome so far, in one sentence:** the course's own templates and lecture now tell us exactly what "stories and use cases" means for this homework, and Epic 3 is done in that form as a saved master file.
- **Next milestone:** fill the Notion "Epics and Features" page for all 10 features, then the task pages for the 11 backlog tasks, one at a time, and add one small pointer note in Figma so Figma and Notion never confuse a reviewer. The owner wants Figma to reflect what is done in Notion.
- **Owner's track (Approved, 2026-11-12):** Premium. The owner builds their own app, the caregiving coordinator.
- **Course dates do not drive the plan (Approved, 2026-11-12).**
- **Order change (Approved, 2026-11-15):** the epics, features, tasks and use cases section comes first. The 6 build plan gaps and boxes 5 and 6 wait until it is finished.
- **Term:** "EFTs" means epics, features and tasks.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| The 8 build plan fixes are applied in the markdown file, each backed by a course quote | **Approved** (owner, 2026-11-15, after the data check) | `docs/build-plan-nfr-draft-2026-11-12.md`; quotes in `docs/sources/build-plan-2026-11-12/11-course-facts-live-weeks.md`, listed in `docs/sources/INDEX.md` |
| The Figma build plan section was NOT updated with the fixes | Fact | Figma section `3073:8029` still has the old text (not re-read). Source: `dogfood-2026-11-13-handoff-homework-hub-and-build-plan.md`, section 0, and no Figma write was made to that section this session |
| Every decision I ask the owner to make must explain itself | **Approved** (owner, 2026-11-15) | `caregiving-coordinator/CLAUDE.md` (Dog feeding section); memory `complete-sentences-with-context.md` |
| Feature-level format is simple: one user story and a list of use case statements per feature. Happy and non-happy paths belong to task-level requirements | **Approved** (owner: "Pull is the right thing to do", 2026-11-15) | `docs/clean-deliverables/feature-stories-and-use-cases-epic-3-2026-11-15.md` |
| Epic 3 user stories and use cases | **Approved** (owner: "Approve draft", 2026-11-15). The two story sentences are Claude's wording | The same file |
| Epic 3 decision on four extra scenarios: raise hard topics without a fight and agree on who does what are supported as scenarios under "Spouses bringing in help the partner will accept"; keep going after a refusal is covered by the small-steps use case; know when to step in for safety is not in MVP #1 | **Approved** by delegation (owner: decide from the data, "yes" if data-driven). The pairing of scenarios with "we want" lines is **Proposed** | The same file, section "Decision on four scenarios" |
| Figma: five boxes I added beside Epic 3 were deleted the same day because they looked like features. The section is back to its original 52 children | Fact (checked by reading the section back) | Figma section `3068:9983` on the "Updated Deliverables" page |
| Rule for how many use cases: each feature lists the use cases from the Vision and Scope list that belong to it, so every use case appears once and the total stays 17 | **Approved** (owner accepted the rule, 2026-11-15) | `feature-stories-and-use-cases-epic-3-2026-11-15.md`, section "How many use cases"; the 17 comes from `vision-and-scope-boards-2026-11-10.md` |
| Figma and Notion must use identical names and point to each other | **Approved** (owner, 2026-11-15) | See section 6, steps 3 to 5 |

Earlier milestones (positioning, epics, roadmap, Notion backlog, laws research, risk profile, course sources, Notion hubs) are in the 2026-11-13 report, section 1.

## 2. Key findings and data
### What the course instructions require (Authoritative: the course's own pages)
| Template or lecture point | What it says | Source |
|---|---|---|
| Notion "Epics and Features" template | Under each feature: a "Feature-Level User Story" heading and a "Feature-Level Use Case Scenarios" heading. No count, no format | `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Epics and Features (template)...md` |
| Notion Kanban task template ("Task #1") | Eight headings: Background, User Story, Problems to Solve, Task Goals, Expected Deliverables, Use Cases to Support, Acceptance, Technical Requirements | Notion page `a819219a4691829c92f581871e30e5b5` (fetched 2026-11-15). The owner's 11 task pages carry the same headings, empty (checked on "Seeing the parent take care of their health", `47c9219a469183f39d35016e94ec08e8`) |
| User story formula | One sentence: "As a [audience], I want [goal] so that [problem or value, not the solution]" | Week 2 lecture transcript, 57:39 to 1:00:10 |
| Use case size | "Usually just one statement." A ticket "might have one to three or four use cases" | Transcript, 1:02:56 to 1:03:02 and about 1:05:02 |
| Happy and non-happy paths, task flows, BDD | Part of task-level requirements | Week 2 and 3 lecture notes, "Scoping Tasks" |
| Instructor's seven steps | Step 7 is "Create the tasks in the backlog and start writing requirements." The owner is on step 7 | Template "How to Get from 0 to Backlog" (read in Lucy's Figma copy and the owner's page) |
| Where deliverables may live | "Drop the links to your product requirements deliverables (however you produced them: in Notion, in Figjam, whatever suits you best)." The submission is an email with the link to a Notion page | `reference/week-2-3.md` (Links and How to Submit) |
| Instructor's example task wording | Tasks start with a verb, for example "Help teams build knowledge about Scrum." Owner's tasks are outcome phrases like "Having family or paid help that steps in" | Template text in Lucy's Figma copy; `epics-features-tasks-2026-11-11.md` |

### Use cases: the count and the map (Proposed mapping; counts are Fact)
Your Vision and Scope lists 11 use cases for Audience 1 and 6 for Audience 2, so 17 in MVP #1 (`vision-and-scope-boards-2026-11-10.md`, lines 97 to 108 and 168 to 174). I matched each to a feature by the problem it sits under in the audience table (`docs/audience-teacher-format-2026-11-04.md`, lines 40 to 50 and 81 to 90):

| Epic | Use cases (count) |
|---|---|
| 1 Real break | Feature 1: finding a break they can afford and qualify for; handling guilt and setting limits they can keep; getting relatives to cover time off. Feature 2: taking a break knowing their partner is cared for; qualifying for help including VA programs; finding a support group (6) |
| 2 Not alone | Feature 1: splitting care and costs among relatives; keeping every relative informed. Feature 2: asking for specific help; showing family what the care really involves (4) |
| 3 Accepts help | Feature 1: getting the parent to accept outside help; trying small steps when the answer is no. Feature 2: bringing in help the partner will accept (3) |
| 4 Guidance | Feature 1: preparing for a hard talk; calming an outburst in the moment. Feature 2: none (2) |
| 5 Money and papers | Feature 1: getting legal papers in place before a crisis; finding and applying for benefits (2) |
| 6 Own health, job, money | Feature 2: none (0) |

Total 17 (source: `vision-and-scope-boards-2026-11-10.md`, lines 97 to 108 and 168 to 174). The placement of "getting relatives to cover time off" under Epic 1 is the least certain (it could be Epic 2).

### Feature-level text (Proposed; Epic 3 is Approved). This is chat-only before this report, so it is saved here
| Epic and feature | User story |
|---|---|
| 1, Getting real breaks they can afford (A1) | As an adult child caring for a parent, I want real breaks I can afford, even when help exists but I can't reach it, so that I keep my own health and life. |
| 1, Getting real breaks and a life outside caring (A2) | As a spouse or partner caring for my partner, I want real breaks and a life outside caring so that I keep my health, my sleep and my closeness with my partner. |
| 2, Having siblings share the care and costs (A1) | As an adult child caring for a parent, I want my siblings and other relatives to share the care and costs so that I'm not carrying it alone. |
| 2, Having relatives who support, not criticize (A2) | As a spouse or partner caring for my partner, I want relatives who support me instead of criticizing so that I'm not alone with the care. |
| 3, Getting the parent to accept doctors or help (A1) | **Approved:** As an adult child caring for a parent, I want my parent to accept the doctors and help they need, with their own choices respected, so that their care happens instead of stopping at a refusal. |
| 3, Bringing in outside help the partner accepts (A2) | **Approved:** As a spouse or partner caring for my partner, I want to bring in outside help my partner accepts so that care continues without every talk turning into a fight. |
| 4, Calming outbursts and calls, and staying calm themselves (A1) | As an adult child caring for a parent, I want to handle my parent's anger, confusion and anxiety and stay calm myself so that visits, calls and hard talks don't fall apart. |
| 4, Understanding the behavior and how to respond (A2) | As a spouse or partner caring for my partner, I want to understand my partner's behavior and how to respond so that daily life and talks stop turning into fights. |
| 5, Having legal authority and papers sorted in time (A1) | As an adult child caring for a parent, I want the legal papers, benefits and bills sorted in time so that care costs and paperwork don't pile up into a crisis. |
| 6, Protecting their money and avoiding debt (A2) | As a spouse or partner caring for my partner, I want to protect our money and avoid debt so that we keep our home, food, coverage and healthcare. |

### What the examples showed (Credible secondary: other students' work, used only to compare formats)
- **Jasmine (telehealth), Notion hub read in Chrome on 2026-11-15** after the owner approved clicking through Notion's "flagged" warning: her epics page has epics, lettered features and verb-led tasks, with no feature-level stories. Only 10 of 87 tasks got full specs ("golden path"). A full card has user story, background, problem statement, goals, deliverables, scope and done, task flow, acceptance criteria and BDD scenarios titled "Use case: ...". Her Non-Functional page is the source of the 6 build plan gaps. Her hub says it mirrors a GitHub repo, and her reflection says Claude filled it in, so it is not a model to copy. Notes: memory `telehealth-student-example.md`.
- **Lucy, Figma board read through the Figma connector:** functional backlog with numbered "The user can..." statements, a separate non-functional backlog (T1 to T13), a phased build plan with gates, and a vision board with a "Use cases to support" list. Her Notion page was never readable (connector said not found). Notes: memory `lucy-example-links.md`.

### Evidence behind Epic 3
| Finding | Number | Source | Confidence |
|---|---|---|---|
| Posts and threads about a parent who refuses help | 60 | Audience Segmentation Master Report, table 2b | Credible secondary (one reader, not double-checked) |
| Posts and threads about a partner who denies needs | 9 | Same table | Estimate (thin) |
| Competitors scoring a Yes on "parent accepts help" | 0 of 16 (11 score No) | Competitive Analysis Master Report, table 4c and discoveries | Credible secondary |
| Need 4 wording | "works when the parent refuses, and respects the parent's choices" | Same report, table 2b | Authoritative (the owner's own table) |

### Problems found in the owner's own deliverables (Fact unless marked)
1. **Two features have tasks but no MVP use case.** Epic 4's Audience 2 feature and Epic 6's feature lost their use cases when the owner took four Medium and Low Audience 2 use cases off MVP #1 (`vision-and-scope-boards-2026-11-10.md`, line 176). Their scope rows and tasks are still in the approved epics file.
2. **The Costs box in Vision and Scope says "We don't know the money and time costs of the release yet."** The instructor's example and Lucy list cost types. The build plan now has data to list them (optional).
3. **Box 5 of the build plan** says `main` accepts only pull requests whose checks pass, which needs branch protection. Week 5 says "You do not need branch protection, because you are on GitHub's free plan." Not changed; noted in the plan (Proposed).
4. **Other lines in the build plan still use the course's old week numbers.** Only the 8 fixes were changed.
5. **The saved record `competitive-analysis-4-updated-2026-11-07.md` has the old wording for 13 fixes already made in Figma** (Competitive Analysis Master Report, section 9, item 4).

### A tooling lesson (Fact)
My plain-text extraction of Figma dropped the second and later lines of multi-line cells. It made me wrongly say the board had one situation per problem. The raw Figma output has all four situations and four scenarios. **Search the raw output, never an extraction.**

## 3. Excluded and deferred
- **A Notion "overview" page copying Jasmine's layout:** dropped. Her hub is AI-filled and does not follow the course layout. A small plain index file in the repo may replace it later (Proposed, not asked for).
- **Her UAE-specific content, and her whole layout:** never copied.
- **Happy and non-happy paths, task flows, BDD:** parked for the task pages. The Epic 3 draft wording is kept in the Epic 3 file, section "Kept for task-level requirements."
- **"Help them know when to step in for safety":** not in MVP #1, an MMP candidate.
- **The 6 build plan gaps, boxes 5 and 6, the phased build order with gates:** on hold until the epics section is finished (owner, 2026-11-15).
- **Premium paper and sharing the homework hub with the instructor:** "We will get to this, but not yet" (owner, 2026-11-15).
- **Weeks 6 to 9, the Week 7 label question, and who pays:** unchanged from the 2026-11-13 report.
- **Changing the Notion submission page:** not done yet. Its item 4 still says feature-level stories "have not been written," which is out of date.

## 4. Open decisions
The next session must not decide these alone. Each is explained so the owner can decide.

1. **Approve the Notion text for the 10 features.** What it is: the story and use case list per feature, from the table in section 2. Why it matters: it is what the instructor's Epics and Features page asks for, and the owner has only approved Epic 3. Choices: approve all, change some, or change the format. After approval: it is written to the Notion page `cfc9219a469183c6945281ff637f4185`, read back, and compared with the saved file.
2. **Epic 4's and Epic 6's Audience 2 features have no MVP use case.** Why it matters: a reviewer will notice tasks with no use case. Choices: leave as is and record the gap (my suggestion, nothing else changes); put the four use cases back, which means the Audience 2 list grows and the Vision and Scope must be updated; or mark those two features MMP, which changes the epics file and the roadmap.
3. **The pointer note in Figma.** What it is: one gray note in the "Create Epics, Features, Tasks" section saying where stories, use cases and task requirements live, with Notion links, file names and a date. Why: so Figma and Notion never confuse a reviewer. Choice: approve the wording (to be shown first), or skip it.
4. **Task pages for the 11 backlog tasks.** What it is: fill the eight task headings. Choices: one task at a time with approval (my suggestion), or all at once. The User Story, Acceptance and Expected Deliverables headings are Claude's wording and must trace to approved tasks without inventing features.
5. **Reword tasks from outcome phrases to action verbs?** The instructor's example tasks start with a verb. Low priority. Changing would touch the epics file, Figma, the Kanban board and the roadmap.
6. **Fill the Costs box from build plan data?** Optional.
7. **Parked from the 2026-11-13 report:** apply the 6 gaps, approve box 5, the new repo's name, how and when to share the homework hub, the Premium paper, renaming the older Notion hub, the two lawyer questions, the email service, how much of MVP #1 to build first, and one pull request for the build plan.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The Epic 3 file and the 10 feature stories | The Notion Epics and Features page | The course template has those headings under each feature |
| The scope table's "Associated Problem" for a task | Task page, "Problems to Solve" | The template heading asks for it |
| The audience table's "we want" line for a task | Task page, "Task Goals" | Same outcome, same words |
| The Vision and Scope use case list | Task page, "Use Cases to Support" | Counts reconcile to 17 |
| Build plan boxes 1 to 4 and `docs/risk-profile.md` | Task page, "Technical Requirements" | Approved rules for data, access and consent |
| Task pages' scenarios | Week 5 BDD scenarios and automatic checks | Week 5 builds its checks from them |
| The saved master file | Notion page, then the Figma pointer note | One master copy, identical names, names compared after each update |

## 6. First steps
1. Confirm where we are in a few complete sentences. Run `git status` and `gh pr list --state open`. Start a new branch from `origin/main` for any new commit (the working tree is on an old, already-merged branch).
2. Read the files in section 8, especially the Epic 3 file, `epics-features-tasks-2026-11-11.md` and the three master reports.
3. **Show the owner the Notion text for the 10 features and wait for a yes.** Show decision 2 in section 4 with its choices.
4. After a yes, write to the Notion Epics and Features page, add the link to the Figma section at its top, read it back and compare names and text with the saved file. Save the five-epic text to a file first so the saved file stays the master.
5. Show the Figma pointer note wording. After a yes, add one gray note at the top of section `3068:9983`. Do not touch existing boxes.
6. Then do the task pages one at a time, starting with the five Epic 3 tasks, showing each draft first.
7. Remind the owner to save the work: a commit and a pull request (one deliverable, one branch, one PR).
8. Later, carry the 8 build plan fixes to Figma section `3073:8029`.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory (`MEMORY.md`). The ones most likely to break next:
- **Write complete sentences with context. Explain every decision** (what, why, choices, what happens after). The owner flagged this many times.
- **Data first.** Use the most up-to-date deliverables and the three master reports before suggesting anything, and say where each line came from. Mark my own wording Proposed.
- **Read raw sources.** Search raw Figma text. Read the whole file before summarizing.
- **Do not copy other students' content or layouts.** Use examples only to compare.
- **Ask before Firecrawl, the browser pane or Chrome.** The owner approved Chrome for the two student examples on 2026-11-15. Never click through a security warning without the owner's explicit yes.
- **One step at a time. Questions get answers, not edits.** Show text before writing it to Notion or Figma.
- **Figma, Notion and the saved file use identical epic, feature and task names.** Update the saved file first.
- **Tasks stay outcome-based until requirements are written.** Task requirements must trace to an approved task and must not invent features.
- **Never write the owner's "What I Did," "What I Learned" or one-page summary.**
- **Laws: never conclude.** Never say "compliant."

## 8. Where things live
- **Epic 3 master file:** `docs/clean-deliverables/feature-stories-and-use-cases-epic-3-2026-11-15.md` (untracked).
- **Epics, features, tasks (Approved 2026-11-11):** `docs/clean-deliverables/epics-features-tasks-2026-11-11.md`. **Roadmap:** `release-roadmap-2026-11-11.md`. **Notion backlog record:** `notion-backlog-2026-11-11.md`. **Vision and Scope:** `vision-and-scope-boards-2026-11-10.md`. **Audience table:** `docs/audience-teacher-format-2026-11-04.md`.
- **Three master reports:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/` in `Audience Segmentation/Reference Reports_Audience Segmentation/`, `Market Analysis/Reference Reports_Market Analysis/` and `Competative Analysis/Reference Reports_Competitive Analysis/`.
- **Build plan (not committed):** `docs/build-plan-nfr-draft-2026-11-12.md`, sources in `docs/sources/build-plan-2026-11-12/` (new file `11-course-facts-live-weeks.md`), logged in `docs/sources/INDEX.md`. **Risk profile:** `docs/risk-profile.md`.
- **Figma file** `HcDDdEGAnikTImO8v7UPMp`, page "Updated Deliverables" (`2782:15415`): Vision and Scope `3068:8597` and `3068:8831`, Create Epics, Features, Tasks `3068:9983` (Epic 3 header `3068:10013`), roadmap `3068:9448`, build plan `3073:8029`, audience `2842:17342`, market `2842:17341`, competitive `2949:2168`, positioning `3045:19393`. Link: https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3068-9983
- **Notion (workspace "Orlando's Notion"):** Epics and Features page `cfc9219a469183c6945281ff637f4185` and Kanban board `0579219a469182f1954401f71214631a` in the older hub "TechFleet: AI Residency Resource Hub" (`4029219a-4691-8000-83bc-cfbd15b50c3c`). Homework submission page "Week 2 and 3 - Product Specifications" `4179219a-4691-8157-976e-dbc20a0a829f` in the private hub `4179219a-4691-8176-8eb1-cf901f72e045`. Course task template `a819219a4691829c92f581871e30e5b5`.
- **Examples:** Lucy's Figma board https://www.figma.com/board/jnkig04mKaWHpd5esSfjKb/Lucy-s-AI-Dev-Residency (file key `jnkig04mKaWHpd5esSfjKb`; Vision and Scope `1:4857`, Functional Backlog `102:6069`, canvas "Vision / Scope / EFTs" `1:1838`). Jasmine's hub https://app.notion.com/p/Telehealth-Platform-Week-2-Product-Spec-41087ab2db21813d8ed7cb9d8cfd030d (flagged by Notion; readable only in Chrome after clicking through).
- **Course files:** skill `.claude/skills/residency-context/` in the folder above the repo; copies under `Resources/`.
- **Git (2026-11-15):** branch `course-skill-accuracy-and-handoff-2026-11-13` (its PR 52 is merged); `origin/main` at `c6558f4`; no pull request open. **Uncommitted:** `CLAUDE.md` (new rule), `docs/sources/INDEX.md`, `docs/build-plan-nfr-draft-2026-11-12.md`, `docs/sources/build-plan-2026-11-12/`, the Epic 3 file, this report. Also untracked and not part of this work: `il.html` and `dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-15. Template headings were read from Notion on 2026-11-15. Lecture quotes were read from the saved transcript.
- **Checks run:**
  - The Epic 3 Figma text was read back and compared with the master file phrase by phrase (23 phrases; one wording difference fixed). Those boxes were later deleted, and the section was re-read: 52 children, none of the five left.
  - The three master reports were read in full on 2026-11-15.
  - The two Figma examples and Jasmine's pages were read as described in section 2.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - Jasmine's pages 00 to 03, 05, 06 and 12, and the contents of most of her cards.
  - Lucy's Notion (never readable) and parts of her canvas (roadmap, problem prioritization).
  - Whether the owner's whole Figma Vision and Scope section matches the saved file word for word (only use case and task wording was spot-checked).
  - The use case-to-epic mapping beyond the problem rows in the audience table.
  - The five-epic story text: it is my wording and not yet reviewed by the owner.
  - The Figma build plan section text (not re-read).
- **How this prevents drift:** Approved and Proposed tags separate decisions from suggestions. First step 3 stops for the owner before anything is written to Notion or Figma. The master file is updated first, and names are compared across the three places after each update. The raw-Figma lesson is a written rule.
