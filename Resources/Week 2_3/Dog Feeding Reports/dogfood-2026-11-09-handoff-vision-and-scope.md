# Handoff: Caregiving Coordinator → product vision and scope (2026-11-09)

> **Replaced by:** `dogfood-2026-11-10-handoff-vision-and-scope-part-3.md` (Parts 1 and 2 of the vision and scope are done).

Replaces: `dogfood-2026-11-08-handoff-audience-segmentation-reports.md` (all its steps are done or carried over here). It sits beside `dogfood-2026-11-07-handoff-feature-comparison-analysis.md`, which still holds the feature comparison plan (deferred, section 3).

> Paste to start: "Read this handoff report and the three master reports it lists. Confirm in a few lines where we are and what the vision and scope starts from. Then ask me for the vision and scope template and which audience goes first, and wait. Keep replies short, plain, and one thing at a time. Confirm every change against the saved research and original sources before making it."

## 0. Start here
- **Where we are:** every discovery deliverable now has one master reference report, merged to `main`: market analysis, audience segmentation and competitive analysis. The owner fed all three into this session on 2026-11-09 and asked to build the **product vision and scope** from them next.
- **The outcome so far, in one sentence:** all three reports point the same way: help worn-out caregivers actually reach a real break, including getting the parent to agree and relatives to cover (each report, section "Where it points").
- **Next milestone:** product vision and scope. One vision board per audience per release (MVP, then MMP), with "What we want to change" as the business goals. The template is in the owner's Week 2 and 3 instructor notes and is **not saved locally**, so ask for it.

## 1. Locked outcomes

**Market analysis** (master report: `Reference Reports_Market Analysis/Market Analysis - Master Report (all 4 tables).md`)
- Opportunity: helping worn-out caregivers reach relief, segment 11 (respite and adult day services) and segment 12 (caregiver mental health). **Approved** 2026-11-05 (source: `Market Analysis - Master Report (all 4 tables).md`, section 9).
- The findings in the master report's sections 5, 6, 8 and 9 are **Proposed** (not reviewed by the owner).

**Audience segmentation** (master report: `Reference Reports_Audience Segmentation/Audience Segmentation - Master Report (all 6 tables).md`)
- Audience 1 = adult child (or child-in-law) caring for a parent. Audience 2 = spouse or partner. **Approved**.
- The Figma deliverable (node 2842:17342) was rebuilt by the owner into 3 sections. The old "Exhaustion and getting a break" section was merged into use case 1. **Approved** (owner, 2026-11-09).
- 6 CSV tables, an index (`00`) and an AI prompt (`01`) made from the Figma section, every cell checked; also added to Figma as section 2997:4593. **Approved** (owner asked for each; PR 36 merged; `Data Tables_Audience Segmentation/`).
- Findings and lessons in the master report are **Proposed**.

**Competitive analysis** (master report: `Reference Reports_Competitive Analysis/Competitive Analysis - Master Report.md`)
- 16 competitors, 5 needs, 4 gaps. The 9 original rows were approved 2026-11-06, the 7 new rows 2026-11-07. **Approved** (source: `Competitive Analysis - Master Report.md`, sections 3 and 5).
- 13 places corrected in Figma V2 (node 2949:2168) on 2026-11-09: problem 1 wording, gap 1 wording, all 6 respite groups, the respite source, 2 segment names, 5 "Covered by competitors?" cells, and the intro line. **Approved** (owner said "Yes, edit V2" and "Yes, both").
- Findings in the master report are **Proposed**.

**Session decisions (2026-11-09)**
- Skip the feature comparison and positioning for now and go straight to vision and scope. **Proposed by owner, not yet confirmed as final:** the owner was told two steps are skipped and did not object.
- "Who pays" and the 8 Verify cells need no research now. "Who pays" goes on the board as one line marked unproven. **Approved** (owner, 2026-11-09).

## 2. Key findings and data

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Burnout is the top caregiver problem | 210 of 412 Reddit posts (51%); 55 of 141 forum threads (39%) | Market master report, section 5 | Credible secondary |
| Not getting a break is rank 1 for both audiences | Adult children 138, spouses 45 posts and threads | Audience master report, section 4 (table 2b) | Credible secondary |
| People want a break but don't get one | 39% say a break would help; 13% have used one | AARP/NAC 2025, PDF pp.26-27 (audience and competitive reports) | Authoritative |
| Respite posts by outcome | 341 = 128 used + 78 couldn't + 81 looking + 18 tried and stopped + 32 mentioned + 4 recommended | `docs/sources/market-analysis-3/segments-11-12/results.json` (market and competitive reports) | Credible secondary |
| Respite market size | $19.3B worldwide (2025); $7.6B US | Market master report, segment 11 | Estimate (not caregiver-only) |
| No competitor fully helps with 3 of 5 needs | 0 Yes on the parent's money, a parent who refuses help, relatives sharing | Competitive master report, section 4c | Credible secondary |
| A parent who refuses help is the emptiest need | 11 of 16 competitors score No, none Yes | Competitive master report, section 6 | Credible secondary |
| Willingness to pay | 12% would pay out of pocket; willing payers cap near $70 a month | Audience master report, table 1 (CAN 2026, Schulz 2016) | Credible secondary |
| Audience 1 is larger | 40% care for a parent and 7% for a parent-in-law, vs 15% for a spouse | AARP/NAC 2025 p.17 (audience report, table 1) | Authoritative |
| Caregivers have jobs | 70% of caregivers aged 18 to 64 are employed | AARP/NAC 2025 pp.38-39 (audience report, table 1) | Authoritative |

**How the two audiences differ** (audience master report, sections 4 and 6; **Proposed** reading)

| | Audience 1: adult child | Audience 2: spouse or partner |
|---|---|---|
| Why they act | Duty, safety, guilt | Love and their vows |
| First situational goal | Understand what's happening | Get help, relief or services |
| What blocks a break | Cost, paperwork, a refusing parent, siblings who won't help | Paperwork (often the VA's), trusting helpers, loneliness in the marriage |
| Problems mostly theirs | Money and papers (74), a refusing parent (60), relatives (48), far away (20), accounts (8), per audience table 2b | Trusted helpers and hospice (14), diagnosis (11), memory care (9), per audience table 2b |

**The 4 competitive gaps** (competitive master report, section 4)
1. No one handles a parent who refuses help or gets relatives to share the work.
2. Personal guidance is locked behind an employer or $150 to $350 an hour (source: competitive table 4b).
3. Money and accounts help works only if the parent prepared ahead.
4. Relief exists, but caregivers can't reach it.

## 3. Excluded and deferred
- **The feature comparison table** (plan in the 2026-11-07 handoff). Deferred: the owner went to vision and scope first. It comes back if the owner asks.
- **Positioning** (one statement per audience). Deferred for the same reason.
- **The 8 Verify cells** in the competitive analysis (Care.com ×3, support groups, Facebook groups, and 3 need-5 cells). Set aside by the owner. They don't change the gaps.
- **Research on who pays.** Not now. It appears on the board as an unproven assumption.
- **Old to-dos from the 2026-11-08 handoff that are still open but not needed for vision:** the wrong Global Industry Analysts link (`docs/market-research-prompt2-results.md` line 174), the "412 vs 825 Reddit posts" check, the CSV vs PNG check, and the Figma update for 9 market cells (owner skipped). The visit-notes app check was dropped by the owner (it changes no verdict).

## 4. Open decisions
The next session must not decide these alone.
- **Which audience gets the first vision board.** Audience 1 is about 3 times larger, with more evidence.
- **Where the vision and scope lives:** Figma, a markdown file, or both, and in which folder.
- **Whether skipping the feature comparison and positioning is final.**
- **Who pays** (stays open; shown as an assumption).
- **What to do about the empty folder** `Audience Segmentation_Data Tables/`, which the owner may have made.
- **Whether to update** `docs/clean-deliverables/competitive-analysis-4-updated-2026-11-07.md` with the 13 Figma fixes. It still has the old wording.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| Market opportunity (segments 11 and 12) | The vision statement and the "why now" | It's the approved opportunity |
| Audience motivations and life goals (audience table 2a) | Who the board is for, and what they care about | One board per audience |
| "What we want to change" for each use case (audience table 2b) | The business goals on the board | The lecture says business goals go on the vision board (1:39:00 to 1:39:30) |
| The 4 competitive gaps and their openings | What sets the product apart, and the scope | Scope should fill the gaps |
| The blockers to a break (cost, refusing parent, relatives, paperwork, eligibility) | What's in scope for the first release | They're why relief goes unused |
| Who pays, consent and health data | Assumptions and risks on the board | They're unproven or risky |

**Course rules for vision and scope** (Week 2 lecture transcript, `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`):
- Vision and scope are drafts and assumptions that change as research comes in (32:26 to 32:40).
- From them, break the work into categories to build a backlog, with just enough work for the first two weeks (32:40 to 32:50).
- One board per audience per release; with two audiences, an MVP and an MMP for each (1:42:01 to 1:42:18).
- The week's deliverables also include functional and non-functional requirements, acceptance criteria, a Kanban board and flow charts (1:20:12 to 1:20:29).

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr list --state open`. If the wrap-up PR for this report is still open, say one line: "This handoff's PR isn't merged yet. Merge it first, or keep going?"
2. **Ask the owner for the vision and scope template** (Figma link or file) and **which audience goes first.** Wait.
3. **Read the template in full.** Then show an inputs table: each item from the three master reports, used or left out, and why (CLAUDE.md rule).
4. **Draft one board** for the chosen audience and MVP only. Tag every line Fact or Proposed, and mark "who pays" as unproven. Show it before saving anything.
5. **Stop and wait** after each board.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. The ones most likely to be broken next:
- **One part at a time.** Do only the step asked, then stop.
- **Questions get answers, not edits.** Change files or Figma only after a clear yes.
- **Confirm before changing.** Check every change against the saved research and the original source first.
- **Earlier deliverables lead.** Start from the master reports' actual tables. Show an inputs table before giving options.
- **Short replies, plain words.** Name every file the first time. Use small tables.
- **Never edit the owner's Figma unasked.** If the owner asks for a new version, clone the section and put a big yellow banner on the old one.
- **The owner merges their own PRs.** One deliverable = one branch = one PR. Never add commits to a PR after handing it over; check `origin/main` before saying a file is on main (memory `push-before-owner-merges`).
- **Never write the owner's homework summary.**

## 8. Where things live
- **Master reports:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/`
  - `Reference Reports_Market Analysis/Market Analysis - Master Report (all 4 tables).md` (plus 4 per-table reports)
  - `Reference Reports_Audience Segmentation/Audience Segmentation - Master Report (all 6 tables).md`
  - `Reference Reports_Competitive Analysis/Competitive Analysis - Master Report.md`
- **Data tables:** `Data Tables_Market Analysis/` (4 CSVs), `Data Tables_Audience Segmentation/` (6 CSVs, `00` index, `01` AI prompt).
- **Figma file** `HcDDdEGAnikTImO8v7UPMp`, page "Week 2 & 3_Updated Deliverables" (2782:15415):
  - audience segmentation 2842:17342
  - audience CSV tables 2997:4593
  - competitive analysis V2 2949:2168
- **Lecture:** `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`.
- **Memory:** `progress-2026-11-09-reference-reports-done.md`, `push-before-owner-merges.md`.
- **Git (2026-11-09):**
  - PRs 36, 37 and 38 merged.
  - This report and the wrap-up commit go on a new branch with their own PR.
  - Left out on purpose: `caregiving-coordinator/docs/sources/competitive-analysis-4/live-pages/raw/il.html` (a map token GitHub blocks) and `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-05-audit-and.textClipping` (stray file).

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2 name a master report or file for each item. Approvals are from this chat on 2026-11-09 and from the 2026-11-05 and 2026-11-07 handoffs.
- **Checks run:**
  - All three master reports were read in full in this session (216, 238 and 275 lines).
  - The numbers in section 2 were copied from those reports, which were checked by script when written (128, 75 and 132 numbers, none missing).
  - PRs 36 to 38 were confirmed merged with `gh pr view`.
  - Lecture timestamps were read from the saved transcript.
  - `check_handoff.py` was run on this report (result in chat).
- **Not checked:**
  - the vision and scope template (not saved locally)
  - Figma after today's last edits, beyond reading back each changed cell
  - the original posts and the outside reports themselves
- **How this prevents drift:** decisions are tagged Approved or Proposed, exclusions are named, and step 2 stops for the owner before any drafting.
