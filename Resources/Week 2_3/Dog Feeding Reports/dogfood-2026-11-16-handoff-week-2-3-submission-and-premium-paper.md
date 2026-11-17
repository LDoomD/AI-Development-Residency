# Handoff: Caregiving Coordinator → Week 2 and 3 submission, then the Premium paper (2026-11-16)

> **Replaced by `dogfood-2026-11-17-handoff-security-paper-source-reading.md` for the Premium paper.** The plan in this report to update section 8 of the agentic-workflows paper is obsolete: the owner chose advanced information security on 2026-11-17. The Week 2 and 3 facts below still hold.

Replaces: `dogfood-2026-11-15-handoff-use-case-scenarios-and-share-consent.md` (all its work is finished). Older reports stay replaced: `dogfood-2026-11-15-handoff-task-stories-and-acceptance-criteria.md`, `dogfood-2026-11-15-handoff-week-2-3-repo-and-build-plan.md`, `dogfood-2026-11-15-handoff-week-2-3-iteration-2.md` and earlier.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Run `git fetch`, `git status` and `gh pr list --state open`, and check whether the handoff-report pull request was merged. Then tell me which of my four own items (section 4) I still have to do, and show me the Premium paper's section 8 next to the current MVP #1 before changing anything. Use plain words. Say 'done' plainly when something is done. Read back every Notion and Figma change. Ask before Firecrawl, the browser pane, Chrome or my Gmail."

## 0. Start here
- **Where we are:** all Week 2 and 3 specification work is finished for the first 11 tasks (5 Epic 3, 6 Epic 1). The owner approved everything and granted bypass permissions for the work. Nothing is left for Claude on the specs.
- **The outcome so far, in one sentence:** the six sections of the instructor's task-level lesson (user stories, acceptance criteria, use case scenarios, task flows, BDD, technical acceptance), the release roadmap and the Notion submission page are all done and were read back.
- **Next milestone:** the owner submits Week 2 and 3 (four owner-only items in section 4), then decides on the Premium paper (not submitted, due date Oct 19 has passed).
- **Method (Approved):** agile, standard homework only, Premium track, own app. The owner follows the instructor's Figma board in order.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| Six task-level sections finished for the 11 task pages. BDD structure check run on all 11 (every scenario in order USE CASE, AS A, GIVEN, WHEN, THEN; every page has a happy and a non-happy path) | **Approved** | `docs/clean-deliverables/task-pages-epic-1-2026-11-15.md`, `task-pages-epic-3-2026-11-15.md`; 11 Notion cards, read back |
| Separate share consent: each Epic 3 page has one Acceptance line, a "not recorded" scenario and a "recorded" scenario, and a developer check line | **Approved** | `task-pages-epic-3-2026-11-15.md`; 5 Notion cards, read back |
| Epic 1 task flows (Flow 3 Audience 1, Flow 4 Audience 2, three branches each). The owner read them and said they are good | **Approved** | Figma `3118:9375` (file `HcDDdEGAnikTImO8v7UPMp`), `task-flows-epic-1-2026-11-16.md`, 6 Notion cards link to them |
| Epic 3 task flows (Flow 1, Flow 2) | **Approved** | Figma `3097:9079`, `task-flows-epic-3-2026-11-15.md` |
| Feature analysis was **skipped**. A draft table exists in `docs/feature-analysis-3.md` but its OUR COMPANY row is blank | **Approved** (owner's correction 2026-11-16) | Submission page says "Skipped" |
| T4.1.4 (private records visible only to the writer) and the caregiver-deletion reading stay Proposed for a lawyer ("keep both") | **Approved** to keep Proposed | `non-functional-epics-features-tasks-2026-11-15.md`, Epic 1 and Epic 3 pages |
| Deletion and counting scenarios are not added; the developer Checks lists cover them | **Approved** (owner: "skip them") | Page "Technical Requirements" sections |
| Release roadmap: weeks, order and 27 task names unchanged (compared name by name with the Figma calendar). One new row "FOUNDATION (Proposed)" for T1 to T4 (Nov 16 to 20) and T5, T6 (Nov 23 to 27) | **Proposed** (Claude's weeks, applied under the owner's instruction to finish) | Figma `3068:9449`, new nodes `3120:9605` to `3120:9625`; `release-roadmap-2026-11-11.md`, section "Update 2026-11-16" |
| Notion "Product Release Vision and Scope" page filled from the approved file (MVP #1 and MMP) | **Approved** (content approved 2026-11-10; owner said go on the Notion fill) | Notion `c6f9219a469183029dd3015ad1211c02`, read back |
| Submission page "Week 2 and 3 - Product Specifications" rebuilt in the instructor's order (Discovery, Vision and Scope, Requirements), real Figma and GitHub links, toggle titles fixed | **Approved** (the owner's idea, then "go") | Notion `4179219a46918157976edbc20a0a829f`, read back |

## 2. Key findings and data
| Finding | Detail | Source | Confidence |
|---|---|---|---|
| Course Basic homework list has 8 items | Vision, scope, epics/features/tasks, build plan, non-functional, technical, user requirements, backlog. All done | `.claude/skills/residency-context/reference/week-2-3-submit-checklist.md` (saved copy of 2026-11-13; the live page could not be opened with the Notion connector) | Authoritative (course, saved copy) |
| Both GitHub repositories are public | `AI-Development-Residency` (specs) and `Week-3---Caregiving-Coordinator` (empty, as the course asks) | `gh repo view`, checked 2026-11-16 | Authoritative |
| Premium paper does not match MVP #1 | Paper section 8 was rewritten 2026-10-28 for visit-note extraction. MVP #1 uses no outside AI service (T1.3.1, T3.2.3) | `docs/specialization-research-paper.md` (header and review notes only read), `non-functional-epics-features-tasks-2026-11-15.md` | Credible secondary (section 8 text itself not read) |
| Course Week 6 starts Nov 16 on information security | The Foundation row puts T4 (security) in that week | `.claude/skills/residency-context/reference/syllabus.md`, line 147 | Authoritative |
| Instructor's board "Deliverables for Product Requirements" | Discovery; Vision and Scope; Requirements (Kanban, flow charts, build plan, BDD, technical requirements). The headings-to-lists mapping is Claude's reading of the export | Owner's Figma export pasted 2026-11-15 and 2026-11-16 | Authoritative (the mapping is an assumption) |

## 3. Excluded and deferred
- **Pitch deck, prototypes, feature analysis:** Bonus homework, not doing (owner, 2026-11-15; feature analysis skipped).
- **Task pages and flows for Epics 2, 4, 5 and 6:** the lecture says to prepare only the next two weeks. They come back when those epics start.
- **Foundation (non-functional) task pages and Notion cards:** none written. The developer role writes them; not requested yet.
- **Deletion and counting scenarios:** skipped on purpose.
- **Lawyer questions (never decided here, never say "compliant"):** whose consent counts for a parent or partner who never signs up; California's medical privacy law; T4.1.4; the caregiver-deletion reading; behavior if someone writes about self-harm (a launch blocker).

## 4. Open decisions
1. **Four items only the owner can do.** (a) Write "What I Did" and "What I Learned" on the submission page, in no fewer than 2 paragraphs each, without AI (Claude never writes them). (b) Make the submission page shareable. Sharing is not set up, and Claude never changes sharing settings. (c) Email the page link to mdenner@techfleet.org. (d) Check that the instructor can open the Figma board (Claude cannot check Figma sharing).
2. **Premium paper (not submitted).** Choices: (1) send it as is, which is fine if the instructor does not need the vision to match the current app; (2) update section 8 to the current MVP #1 and say where agents could fit later without breaking the no-AI rule, then send it. Recommendation: option 2, because section 8 describes an older version of the app. If chosen, read section 8 and the 2026 vision files first, show the text, then save. Submitting means an email plus the course's Google form. Claude may search the owner's Gmail for a sent copy only after the owner says yes.
3. **Foundation row weeks (Proposed).** Choices: keep the weeks as drawn, or move them. Changing them is the owner's call; nothing else depends on them yet.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| The submission page with real links | The owner's email to the instructor | The instructor opens that page and follows the links |
| Paper section 8 vs. MVP #1 and T1.3.1 | The Premium paper update | The paper must describe the app being built |
| The roadmap's Foundation row | The Week 4 build and the developer role's task pages | The pages' INVEST lines say sign-in, circle, consent records and tables come first |

## 6. First steps
1. Confirm where we are, run the git checks, and check whether the handoff-report pull request was merged (commits pushed after a pull request merges are not on `main`).
2. Tell the owner which of the four own items (section 4, item 1) are still open. Do not write any of them.
3. If the owner wants the paper done: read paper section 8, show it beside MVP #1, wait for a choice, then edit.
4. Remind the owner to save work in a pull request and to write a new handoff report before compacting.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and memory (`MEMORY.md`, note `week-2-3-task-level-done-2026-11-16`). The ones most likely to be broken next:
- **Say "done" plainly.** Do not end a status message with a list of gaps and things for the owner to approve when bypass permission was granted. Separate "only you can do this" from "optional."
- **Plain words, full sentences.** Name pages by title and say where they are (Notion link or file path). The owner could not find the submission page until given the link.
- **Check every fact against saved files.** Read the file first. Do not cite line numbers not read in this session.
- **Read back every Notion and Figma write.** Notion toggles: the title must be the first line inside the toggle; an empty first line makes a blank title.
- **Owner's words win:** feature analysis was skipped, whatever an older file says.
- **Never write the owner's "What I Did," "What I Learned" or one-page summary.**
- **Ask before** Firecrawl, the browser pane, Chrome and the owner's Gmail. Never change sharing settings. Do not move the owner's Figma boxes. Laws: never conclude.

## 8. Where things live
- **Specs (in `docs/clean-deliverables/`):** `task-pages-epic-1-2026-11-15.md`, `task-pages-epic-3-2026-11-15.md`, `task-flows-epic-1-2026-11-16.md`, `task-flows-epic-3-2026-11-15.md`, `release-roadmap-2026-11-11.md`, `vision-and-scope-boards-2026-11-10.md`, `non-functional-epics-features-tasks-2026-11-15.md`, `epics-features-tasks-numbered-2026-11-15.md`, `epic-and-feature-user-stories-2026-11-15.md`, `week-2-3-remaining-work-backlog-2026-11-15.md` (iteration log).
- **Paper:** `docs/specialization-research-paper.md`. Course page for it: `.claude/skills/residency-context/reference/week-2-premium-specialization-paper.md`.
- **Notion:** submission page `4179219a46918157976edbc20a0a829f` (private area "Orlando - AI Residency Homework Submissions"); hub "Week 2 & 3 / Orlandos: Week 2 Coding Challenge - Product Specs Template" with Vision and Scope `c6f9219a469183029dd3015ad1211c02`, Epics and Features `cfc9219a469183c6945281ff637f4185`, Kanban board `0579219a469182f1954401f71214631a`, Market Research page `30f9219a4691839dbf50013fc05790b8`. The 11 task cards are listed in `task-pages-epic-1-2026-11-15.md` and `task-pages-epic-3-2026-11-15.md`.
- **Figma file `HcDDdEGAnikTImO8v7UPMp`, page "Updated Deliverables":** vision and scope `3089:9633`, epics section `3068:9983`, non-functional `3094:9079`, build plan `3073:8029`, roadmap `3068:9449` (Foundation row `3120:9605` to `3120:9625`), flows `3097:9079` and `3118:9375`.
- **Git (checked 2026-11-16, night):** pull requests 57, 58 and 59 are all merged (59 merged 2026-11-16 04:04 UTC, merge commit `10e97c8`), so all specs, the roadmap update and the log rows are on `main`. This report is on branch `handoff-report-2026-11-16` in its own pull request (the owner merges). Untracked and not part of this work: `il.html` and a `.textClipping` file.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. Decisions are the owner's chat replies on 2026-11-16.
- **Checks run:**
  - Notion pages read back after every write (11 task cards, submission page twice, Vision and Scope page, hub pages).
  - Figma: Epic 1 flows and the roadmap Foundation row checked by screenshot and a text read of the new nodes.
  - 27 roadmap task names compared with the numbered epics file by script: no differences.
  - BDD structure script run on all 11 pages: no problems.
  - `check_handoff.py` run on this report.
- **Not checked:**
  - The live course page (different Notion workspace); the saved 2026-11-13 copy was used.
  - Whether the owner's Figma board and Notion page are shareable to the instructor.
  - Paper section 8's actual text.
  - How the Notion toggles display on the owner's screen after the title fix (saved text only).
  - Whether the owner has read the Epic 3 developer rules (they are approved under the blanket approval).
- **How this prevents drift:** Approved and Proposed tags separate decisions from suggestions, exclusions are listed, and the first step makes the next session check git and the owner's four items before editing anything.
