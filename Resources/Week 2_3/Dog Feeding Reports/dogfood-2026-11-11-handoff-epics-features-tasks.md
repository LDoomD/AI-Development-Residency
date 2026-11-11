# Handoff: Caregiving Coordinator → epics, features and tasks (2026-11-11)

Replaced by: `dogfood-2026-11-11-handoff-requirements.md`

Replaces: `dogfood-2026-11-10-handoff-positioning-statements.md` (its next milestone, positioning, is done; its open decisions are answered or carried over here). Also confirms `dogfood-2026-11-10-handoff-vision-and-scope-part-3.md` stays replaced.

> Paste to start: "Read this handoff report and the 2 records it lists (positioning and vision and scope). Confirm in a few lines where we are. Run `gh pr view 44`. Then ask me which comes next (epics, features and tasks; the Notion copy; or the roadmap question), and wait. Keep replies short, plain, and one thing at a time. Suggest only verified data (Approved or Fact)."

## 0. Start here
- **Where we are:** positioning is **done**. The instructor's "Unique Value Proposition and Product Positioning" template has all 7 boxes filled, each approved by the owner, saved in markdown and copied to the owner's FigJam board. It's in PR 44, which isn't merged yet (as of 2026-11-11).
- **The outcome so far, in one sentence:** for each audience there's now a positioning statement: who it's for, their top 5 problems, what competitors do today, and how this is different (real breaks, a parent or partner accepting help, relatives sharing the work, affordable guidance, and money and papers for Audience 1).
- **Next milestone (not chosen by the owner yet):** most likely **epics, features and tasks**, on the vision board, section "How to Build a Backlog of Work" (node 15:1222). That section is still an empty template. It takes the 4 scope tables' outcomes and sorts them into epics, features and tasks (Morgan's example is in it). Other choices: the Notion copy of positioning, or the roadmap (Part 6).

## 1. Locked outcomes

**Positioning (all Approved by the owner, 2026-11-11, one box at a time)**
- Record: `caregiving-coordinator/docs/clean-deliverables/positioning-statements-2026-11-11.md`
- On FigJam: board `HcDDdEGAnikTImO8v7UPMp` ("Orlandos AI Dev Residency Work"), node 3045:19393. Read back word for word, 0 overlaps. Morgan's 8 example blocks were removed. The template's titles and instruction text were kept.

| Box | Content | Source |
|---|---|---|
| 1 Target audiences | "Adult Children (or children-in-law) caring for a parent"; "Spouses or partners caring for a husband, wife or partner" | Target Audiences stickies, node 1:487 |
| 2 Problems | MVP #1 top 5 per audience (owner chose these over all MMP problems) | `vision-and-scope-boards-2026-11-10.md` |
| 3 Competitors and gaps | 6 direct competitors (what it is, fully meets, biggest weakness) and the 4 gaps | Competitive master report, tables 3, 4b, 4c, section 5 |
| 4 Impact | 5 value stickies per audience. Heading "Impact on caregivers' problems", not "of our solution" | MVP #1 boards |
| 5 How impact differs | 5 rows: "Today, competitors … We aim to: <business goal 1 to 5>". Goal 6 left out (not compared) | Competitive tables 2a, 4b, 4c; business goals |
| 6 Unique value | Table: each gap → its UVP sticky. Audience 2 gets the first 3 rows. No slogan (it would be new wording) | Gaps; UVP stickies, node 1:690 |
| 7 Positioning | One per audience, Morgan's 4 labels (below) | Boxes 1 to 6; lecture 1:37:26 |

**The 2 positioning statements (Approved)**
- **Audience 1:** AUDIENCE Adult Children (or children-in-law) caring for a parent. Problems: box 2's 5. Other businesses in the space: "Care managers, respite and the VA give real breaks, but only to families who can pay or get in. Cariloop gives guidance only through an employer. Caring Village can't get relatives to join. Everplans is useless unless the parent filled it in. Nothing works once the parent says no." Unlike other businesses, we "focus on getting caregivers to the real breaks that already exist; getting a parent to accept help and relatives to share the work; personal, ongoing guidance without an employer or a high hourly bill; and the money, papers and accounts, even when the parent didn't prepare ahead."
- **Audience 2:** AUDIENCE Spouses or partners caring for a husband, wife or partner. Problems: box 2's 5. Other businesses: the first 3 sentences above (Everplans and "nothing works once the parent says no" left out: measured for parents only). Unlike other businesses, we "focus on getting caregivers to the real breaks that already exist; getting a partner to accept help and relatives to share the work; and personal, ongoing guidance without an employer or a high hourly bill."

**Owner choices made 2026-11-11 (Approved)**
- Use the instructor's template (lecture board node 581:5924) as the guide, all 7 boxes, not just box 7.
- Markdown first, then FigJam, then Notion.
- "A parent or partner" narrowed to "a parent" (Audience 1) and "a partner" (Audience 2) in box 7.
- Respite and VA (indirect) not added to box 3's table; gap 4 covers them.
- Edits allowed: "a high hourly bill" for the report's dollar figure, and Cariloop's company-size limit cut (no numbers on the board). Source: competitive master report, gap 2 and table 4b.

**Earlier milestones (unchanged):** the vision boards and scope tables (`docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md`, Approved 2026-11-10, PR 43 merged) and the 3 master reports.

## 2. Key findings and data

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Positioning belongs in Discovery, with the competitive analysis | Board label "Product Positioning (Competitive Analysis Workshop)" | Lecture board `mqryoCyR9mAw3v6kyDlmes`, milestone diagram; deliverables list node 550:11450 | Authoritative (course) |
| Positioning format | "For these audiences, our product solves the problem… other businesses do this… unlike other businesses, we do this." One per audience | Lecture 1:36:50 to 1:37:43 | Authoritative (course) |
| UVP inputs = template boxes 1 to 5 | Who, problems, competitors, impact, how impact differs | Lecture 1:34:03 to 1:34:36 | Authoritative (course) |
| No competitor fully meets 3 of 5 needs | 0 Yes on money, parent accepts help, relatives share | Competitive master report, table 4c | Credible secondary |
| The week's deliverables list | Discovery (incl. positioning statements); Vision and Scope (boards, scope, epics/features/tasks); Requirements (acceptance criteria, Kanban, flow charts, build plan, BDD, technical requirements) | Lecture board node 550:11450 | Authoritative (course) |
| A roadmap is named in the objectives | Objective 3: "organize the work in a prioritized backlog and roadmap" | `residency-context/reference/week-2-3.md` | Authoritative (course) |
| Every drafted line traced to a source | 38 of 38 (boxes 1 to 4), 11 of 11 (box 5 phrases) | Check scripts run in chat 2026-11-11 | Credible secondary |

**Fleety (Tech Fleet bot), checked 2026-11-11:** its definitions of UVP and positioning match the lecture. Its claim that positioning lives in the Vision milestone and Vision and Scope workshop does **not** match the instructor's board. Its later deliverable entry says "Built in Discovery", which does match.

## 3. Excluded and deferred
- **Notion copy of positioning:** the owner said "not now" (2026-11-11). It comes back when the owner asks, or at homework submission (the homework says "produce results in Notion").
- **Feature comparison and the 8 Verify cells:** still set aside (Agile). They come back only if the owner asks.
- **Research on who pays:** not now. It's on every board as unproven.
- **Goal 6 in box 5:** left out, because the competitive analysis doesn't compare competitors on caregivers' own health, job and money.
- **Marketing and go-to-market** (named by Fleety): not due this week.
- **Out of scope per the lecture:** personas, empathy maps, journey maps (1:25:31 to 1:25:40), problem statements (1:26:25 to 1:26:35). Prototypes are optional.
- **The template line "List the top 5 to 7 direct competitors…"** under every box was left as is (instructor text).

## 4. Open decisions
The next session must not decide these alone.
- **What comes next:** epics, features and tasks (15:1222), the Notion copy, or the roadmap.
- **The roadmap (Part 6, node 22:6807):** not decided. The last session's view: keep it, because objective 3 and section 15:1222's own text ("…for your Product Roadmap") name it, and the lecture (42:28) says a roadmap "might be for other people." Part 6's template hasn't been opened.
- **Who pays:** stays open.
- **The order after epics:** acceptance criteria, Kanban board, flow charts, build plan, BDD and technical requirements (lecture 1:20:00 to 1:20:43). The owner hasn't picked the order.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The 4 scope tables (outcomes) | Epics, features and tasks (15:1222) | The section says "Your scope of outcomes can be organized into epics, features, and tasks" |
| MVP #1 scope tables | The first epics (near-term) | The lecture puts only "just enough work to deliver the first two weeks" in the backlog (32:47 to 32:55) |
| Business goals and use cases | Epic and feature names | Morgan's example epics read as outcomes ("Learning Agile Principles") |
| Positioning statements | Notion, and the pitch deck later | Homework requirement 8: a pitch deck summarizing everything |
| Epics, features and tasks | The roadmap (Part 6) and the Kanban backlog | Part 6 is titled "Create your Release Roadmap Based on Your Epics, Features, and Tasks" |

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr view 44`. If it isn't merged, say: "Positioning's PR isn't merged yet. Merge it first, or keep going?"
2. **Ask the owner what comes next** (epics, features and tasks; Notion; or the roadmap), and wait.
3. **For epics, features and tasks:**
   - Re-read the lecture on epics, features and tasks (37:22 to 42:50, 54:12 to 56:21 for INVEST) and cite timestamps.
   - Read section 15:1222 in full, including Morgan's example (node 20:1588) and its styling.
   - Show an inputs table: each scope table and outcome, used or left out, and why.
4. **Draft one part at a time.** Show it. Wait for "yes".
5. **Write to the board only after approval.** Read it back after, with an overlap check.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files (`vision-scope-source-of-truth.md`, `only-verified-suggestions.md`, `discovery-no-solution-framing.md`). The ones most likely to be broken next:
- **Verified only.** Every line is Approved or Fact, with its source. Copy approved wording word for word; say every edit you make.
- **Outcomes, not solutions.** Epics, features and tasks name what changes, not how (lecture 35:43 to 36:31). Never say "build". The lecture's own epic example ("Help teams build knowledge…") is about people building knowledge, not a product.
- **Check the lecture first** for each step, and cite the timestamp.
- **Read the template's instructions and Morgan's example first,** including styling.
- **Pasted notes (Fleety and others) are claims, not sources.** Check them against the lecture and the instructor's board.
- **Run a check script** that finds each drafted line in its source before showing it. The owner asked for this on 2026-11-11.
- **Read the board back after every write,** with an overlap check.
- **One part at a time. Questions get answers, not edits.**
- **The owner merges their own PRs.** One deliverable = one branch = one PR.

## 8. Where things live
- **Owner's work board** `HcDDdEGAnikTImO8v7UPMp` ("Orlandos AI Dev Residency Work"): positioning template, node 3045:19393.
- **Vision board** `PQFzfyqTUQhAgEEe1P6ygs`: Part 1 4054:1999; Part 2 grids 2018:1806, 2129:2447; vision and scope 2032:3998; backlog section 15:1222 (empty); roadmap 22:6807; backlog population 2001:1620.
- **Instructor's lecture board** `mqryoCyR9mAw3v6kyDlmes`: positioning template 581:5924; deliverables list 550:11450; milestone diagram 525:3238.
- **Records:** `caregiving-coordinator/docs/clean-deliverables/positioning-statements-2026-11-11.md` and `vision-and-scope-boards-2026-11-10.md`.
- **Master reports:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/` (Market Analysis, Audience Segmentation, "Competative Analysis").
- **Lecture:** `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md` (it ends at 1:51:37, mid-word).
- **Homework:** `.claude/skills/residency-context/reference/week-2-3.md`.
- **Git:** branch `positioning-statements`, commit `4b2fc1d`, PR 44 open. This report isn't committed. Left uncommitted on purpose: `docs/sources/competitive-analysis-4/live-pages/raw/il.html` and `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** see section 1. Every box was approved by the owner in chat on 2026-11-11, saved to the record file, and read back from FigJam by script.
- **Checks run:**
  - `check_handoff.py` on this report (result in chat).
  - Source-match scripts: boxes 1 to 4 (38 of 38 lines) and box 5 (11 of 11 phrases) found word for word in the saved reports.
  - FigJam read-back of node 3045:19393: text matches the record; 0 overlaps.
  - Lecture passages re-read: 1:26:16 to 1:27:12, 1:33:48 to 1:37:48, 35:43 to 36:31, 1:42:39 to 1:42:47.
- **Not checked:**
  - Part 6 (roadmap) template not opened.
  - The lecture board was searched by keyword (1.1 million characters), not read sticky by sticky.
  - The original posts behind the master reports weren't re-read.
  - Box 6's table header row styling wasn't checked up close (the screenshot was small).
- **How this prevents drift:** every outcome is tagged Approved with its source; Fleety's wrong claims are named; exclusions are listed; step 2 stops for the owner before any drafting.
