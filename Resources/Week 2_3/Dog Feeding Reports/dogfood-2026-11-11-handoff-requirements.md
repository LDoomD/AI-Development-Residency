# Handoff: Caregiving Coordinator → Requirements (2026-11-11)

Replaces: `dogfood-2026-11-11-handoff-epics-features-tasks.md` (its next milestone, epics, features and tasks, is done, and so are the roadmap and the first backlog). Older reports stay replaced: `dogfood-2026-11-10-handoff-positioning-statements.md`, `dogfood-2026-11-10-handoff-vision-and-scope-part-3.md`.

Replaced by: `dogfood-2026-11-12-handoff-build-plan-and-nfr.md`.

> Paste to start: "Read this handoff report and the 5 records it lists in section 8. Confirm in a few lines where we are. Then ask me which Requirements step comes first (or the pitch deck, or the Notion product specs page), and wait. Keep replies short, plain, and one thing at a time. Suggest only verified data (Approved or Fact)."

## 0. Start here
- **Where we are:** Discovery and Vision and Scope are **done**. On 2026-11-11 the owner finished 4 deliverables, each approved, saved in markdown, written to its board or Notion, read back, and merged:
  1. Positioning (PR 44)
  2. Epics, features and tasks (PR 45)
  3. Release roadmap (PR 46)
  4. The first 2 weeks of the Notion backlog (PR 47)
- **The outcome so far, in one sentence:** the MVP #1 release is broken into 6 epics (the business goals), 10 features (one value per audience) and 27 tasks (outcomes), with a roadmap from Nov 16 to Dec 18. The first 11 tasks (Epic 3, then Epic 1) are in the Notion Kanban backlog.
- **Next milestone:** **Requirements.** The lecture lists acceptance criteria, the Kanban board, flow charts, the build plan, BDD scenarios and technical requirements (1:20:00 to 1:20:43). The non-functional requirements go here too (44:09 to 50:22). The owner hasn't picked the order yet. Other open homework: the pitch deck, the Notion product specs page, and the submission.

## 1. Locked outcomes

### Positioning (Approved 2026-11-11, PR 44 merged)
- Record: `caregiving-coordinator/docs/clean-deliverables/positioning-statements-2026-11-11.md`. On FigJam: board `HcDDdEGAnikTImO8v7UPMp`, node 3045:19393.
- All 7 boxes of the instructor's template (lecture board node 581:5924): audiences, top 5 problems per audience, 6 direct competitors and 4 gaps, impact, how impact differs, unique value, and 2 positioning statements.
- **Audience 1 statement, "Unlike other businesses, we":** "focus on getting caregivers to the real breaks that already exist; getting a parent to accept help and relatives to share the work; personal, ongoing guidance without an employer or a high hourly bill; and the money, papers and accounts, even when the parent didn't prepare ahead."
- **Audience 2 statement:** the same, minus the money line, with "a partner" instead of "a parent."
- Not copied to Notion yet (owner said "not now").

### Epics, features and tasks (Approved 2026-11-11, PR 45 merged)
- Record: `caregiving-coordinator/docs/clean-deliverables/epics-features-tasks-2026-11-11.md`. On the vision board: section 20:1588 (template block plus 5 gray spaces; 37 empty template boxes removed).
- **Rules (Approved):** Epic = business goal, word for word. Feature = the scope table's value for each audience. Task = that row's outcomes, word for word. This follows Morgan's backlog ("TASK (outcome)", node 4162:5439). MVP #1 only.

| Epic (business goal) | Audience 1 feature | Audience 2 feature |
|---|---|---|
| 1. Remove the barriers that keep caregivers from getting a real break. | Getting real breaks they can afford | Getting real breaks and a life outside caring |
| 2. Make sure caregivers don't carry the care alone, with relatives sharing the work. | Having siblings share the care and costs | Having relatives who support, not criticize |
| 3. Increase how often a parent or partner accepts outside help. | Getting the parent to accept doctors or help | Bringing in outside help the partner accepts |
| 4. Make personal, ongoing guidance reachable without an employer or a high hourly bill. | Calming outbursts and calls, and staying calm themselves | Understanding the behavior and how to respond |
| 5. Make the money, papers and accounts manageable, even when nothing was prepared ahead. | Having legal authority and papers sorted in time | none |
| 6. Protect caregivers' own health, job and money while they care. | none | Protecting their money and avoiding debt |

- 27 tasks in all (2 or 3 per feature). The full list is in the record.
- Goal 4 holds the behavior rows because the competitive report's criterion 1 is "Knowing what to do: … handle hard behavior …" (source: competitive master report, line 79), tied to goal 4 in positioning box 5 (`positioning-statements-2026-11-11.md`).
- Audience 2's money row is under goal 6 (owner's choice): it's the spouse's own money.

### Release roadmap (Approved 2026-11-11, PR 46 merged)
- Record: `caregiving-coordinator/docs/clean-deliverables/release-roadmap-2026-11-11.md`. On the vision board: calendar 22:4543 (2 rows added; instructor's example row kept).
- **Window:** the rest of the residency, Nov 16 to Dec 18, 2026, holiday week included. **Order:** the Top square first, then by how often caregivers wrote about each problem (source: audience table 2b rank, `Audience Use Cases.csv`; Part 2 problem grid, node 2018:1806).

| Week | Epic | Source |
|---|---|---|
| Nov 16 to 20 | Epic 3 (the only Top square) | `release-roadmap-2026-11-11.md` |
| Nov 23 to 27 (no class) | Epic 1 (rank 1 for both audiences) | `release-roadmap-2026-11-11.md` |
| Nov 30 to Dec 4 | Epic 4 (rank 2 for both) | `release-roadmap-2026-11-11.md` |
| Dec 7 to 11 | Epic 5 and Epic 6 | `release-roadmap-2026-11-11.md` |
| Dec 14 to 18 | Epic 2 (rank 6 for both) | `release-roadmap-2026-11-11.md` |

- Each task is a 1-week bar, with both audiences' features side by side. The calendar's labels are from an older year, so the nearest columns were used (11/17, 11/24, 12/01, 12/08, 12/15; source: calendar node 22:4543).

### Notion backlog, first 2 weeks (Approved 2026-11-11, PR 47 merged)
- Record: `caregiving-coordinator/docs/clean-deliverables/notion-backlog-2026-11-11.md`.
- Notion: [Backlog Kanban Board](https://app.notion.com/p/0579219a469182f1954401f71214631a). Path: TechFleet: AI Residency Resource Hub → Week 2 & 3 → Week 2 Coding Challenge - Product Specs Template (1) → Backlog Kanban Board. Database "Tasks Go Here", data source `collection://2399219a-4691-836e-ba1b-87a4a7e952a4`.
- **11 tasks:** Epic 3 (5 tasks) and Epic 1 (6 tasks). Fields: Name = task; Epic and Feature = new select choices with full names; Status = Backlog; Responsible People = the owner. The sample row "Task #1" became the first task (nothing deleted). Source: `notion-backlog-2026-11-11.md`.
- **Why only 11:** "I just put just enough work to deliver the first two weeks worth of work" (source: lecture 32:45 to 32:55, `Week 2_Lecture_Transcript.md`).

### Earlier milestones (unchanged)
- Vision boards and scope tables: `vision-and-scope-boards-2026-11-10.md` (Approved 2026-11-10, PR 43 merged).
- The 3 master reports (market, audience segmentation, competitive): `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/`.

## 2. Key findings and data

| Finding | Number or quote | Source | Confidence |
|---|---|---|---|
| The tasks are outcomes, not product features | "show what we want to achieve, not how" | Lecture 35:43 to 36:27 | Authoritative (course) |
| Only near-term work goes in the backlog | First 2 weeks | Lecture 32:45 to 32:55, 41:33 to 41:59 | Authoritative (course) |
| A task must be usable by a person and take 1 to 2 weeks (INVEST) | Independent, Negotiable, Valuable, Estimable, Small, Testable | Lecture 54:12 to 56:19 | Authoritative (course) |
| Non-functional requirements come first, before functional ones | Tools, database, system design, security, quality | Lecture 44:09 to 50:22 | Authoritative (course) |
| Build plan and technical requirements need the tools chosen | "you're going to have to have the selections of the tools" | Lecture 1:21:09 to 1:21:20 | Authoritative (course) |
| Requirements deliverables this week | Acceptance criteria, Kanban, flow charts, build plan, BDD, technical requirements | Lecture 1:20:00 to 1:20:43 | Authoritative (course) |
| The roadmap is a homework objective | "organize the work in a prioritized backlog and roadmap" | `residency-context/reference/week-2-3.md`, line 23 | Authoritative (course) |
| The board's Notion steps | 13 steps; step 12 uses the "Task-Level Acceptance Criteria Template" | Vision board section 2001:1620 | Authoritative (course) |
| The owner's Notion template still has an empty "Epics and Features" page | Feature-level user story and use case scenarios per feature | [Epics and Features](https://app.notion.com/p/cfc9219a469183c6945281ff637f4185) | Observed 2026-11-11 |
| Residency weeks left | Week 5 (Nov 16), holiday (Nov 23), Week 6 (Nov 30), Week 7 (Dec 7), Week 8 (Dec 14) | `residency-context/reference/syllabus.md` | Authoritative (course) |
| Every board and Notion write matched its record | 43 of 43 lines (epics board and roadmap); 11 of 11 rows (Notion) | Read-back scripts run 2026-11-11 | Credible secondary |

## 3. Excluded and deferred
- **Morgan's "Allow users to…" product backlog** (node 4162:5427): product features, which are solutions. It comes back in Requirements, when tasks become usable features.
- **Morgan's non-functional backlog** (node 4162:5437): it names tools (Vercel, Supabase, OpenRouter). It comes back in Requirements, after the owner chooses tools. Inputs already saved: `caregiving-coordinator/docs/risk-profile.md` and the board barrier "Health data and consent are a risk."
- **Epics 4, 5, 6 and 2 in the backlog:** they stay on the roadmap as a forecast and go into Notion after the first delivery.
- **The MMP scope rows:** later releases.
- **Sprint, type and team function fields in Notion** (board 2001:1620, steps 6 to 8): not added; the owner's Kanban doesn't have them.
- **INVEST sizing of the 27 tasks:** not done. The owner turned down the INVEST checklist for analysis work, so use only what the lecture says about INVEST, unless the owner asks for the checklist.
- **Notion copy of positioning:** "not now." It comes back with the product specs page or at submission.
- **Who pays:** still unproven; on every board as a barrier.
- **Out of scope per the lecture:** personas, empathy maps, journey maps, problem statements (1:25:31 to 1:26:35).

## 4. Open decisions
The next session must not decide these alone.
- **Which Requirements step comes first:** acceptance criteria and user stories for the 11 backlog tasks; flow charts; the build plan; BDD scenarios; technical and non-functional requirements. The lecture's order puts non-functional (foundation) before functional for building (44:13 to 44:24), but acceptance criteria can be written first.
- **Tool choices** (needed before the build plan and technical requirements). Memory notes the residency's required shape: a hosted three-tier web app such as Vercel plus Supabase.
- **When to fill the Notion product specs page** (market research, vision and scope, epics and features, pitch deck pages) and the "Epics and Features" page.
- **The pitch deck:** not started.
- **Who pays:** stays open.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The 11 Notion backlog tasks | Task-level acceptance criteria (Notion step 12) and user stories | The board says to write requirements for each task (2001:1620, steps 11 to 13) |
| The 10 features | The Notion "Epics and Features" page: feature-level user stories and use case scenarios | That page's template asks for them |
| Table 2b "Help them…" scenarios and the MVP #1 use cases | Use case scenarios and BDD (Given/When/Then) | They're the verified scenarios for each problem (`Audience Use Cases.csv`) |
| `risk-profile.md` and the health-data barrier | Non-functional requirements (security, privacy) | Health data, shared logins and access by several users are this product's risks |
| The roadmap's week order | The build plan's order of work | The build plan sets what gets delivered first (lecture 44:24 to 45:21) |
| Positioning, vision boards, epics, roadmap | The pitch deck and the Notion product specs page | The homework asks for a pitch deck that sums up everything |

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr list --state open` to check that nothing from this session is left unmerged.
2. **Ask the owner which comes next:** a Requirements step (name the 5 choices in section 4), the pitch deck, or the Notion product specs page. Wait.
3. **For any Requirements step:**
   - Re-read the lecture part for it first and cite timestamps (acceptance criteria and user stories: around 51:00 to 1:09:00; technical requirements 1:07:40 to 1:10:06; build plan 43:59 to 50:30).
   - Read the template on the board or in Notion, and any example by Morgan, before drafting.
   - Show an inputs table: each input, used or left out, and why.
4. **Draft one part at a time.** Show it. Wait for "yes."
5. **Markdown first, then the board or Notion.** Read it back after, with an overlap check on boards.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files (`vision-scope-source-of-truth.md`, `only-verified-suggestions.md`, `discovery-no-solution-framing.md`, `confirm-before-changing.md`). The ones most likely to be broken next:
- **Verified only.** Every line is Approved or Fact, with its source. Copy approved wording word for word, and say every edit you make.
- **Requirements turn outcomes into usable work.** That's where product features are allowed, but each one must trace to an approved task or outcome. Don't invent features the data doesn't support.
- **Check the lecture first** for each step, and cite the timestamp.
- **Read the template's instructions and Morgan's example first,** including styling.
- **Run a check script** that finds each drafted line in its source before showing it.
- **Read the board or Notion back after every write,** with an overlap check on boards. When cloning FigJam nodes, append them to the section (a clone can land on the page root), and remove old nodes only at the end of a script.
- **Ask before writing to Notion or the board,** and before adding fields, rows or branches.
- **One part at a time. Questions get answers, not edits.** Keep replies short.
- **The owner merges their own PRs.** One deliverable = one branch = one PR, started from `main`.
- **Never write the owner's homework summary** ("What I Did", "What I Learned").

## 8. Where things live
- **Records (the 5 to read first):** in `caregiving-coordinator/docs/clean-deliverables/`
  - `positioning-statements-2026-11-11.md`
  - `epics-features-tasks-2026-11-11.md`
  - `release-roadmap-2026-11-11.md`
  - `notion-backlog-2026-11-11.md`
  - `vision-and-scope-boards-2026-11-10.md`
- **Vision board** `PQFzfyqTUQhAgEEe1P6ygs`:
  - Vision and scope 2032:3998.
  - Epics 20:1588. Kitchen instructions 15:1222 and 20:1365 (teaching only).
  - Roadmap 22:6807 (calendar 22:4543). Notion steps 2001:1620.
  - Morgan's example 4165:6061 (functional backlog 4162:5427, non-functional 4162:5437).
- **Owner's work board** `HcDDdEGAnikTImO8v7UPMp`: positioning, node 3045:19393.
- **Instructor's lecture board** `mqryoCyR9mAw3v6kyDlmes`: deliverables list 550:11450.
- **Notion:**
  - [Week 2 Coding Challenge - Product Specs Template (1)](https://app.notion.com/p/4119219a469180b1b6c9dc4d19059d02). It holds the Market Research, Product Release Vision and Scope, Epics and Features, Product Pitch Deck and Backlog Kanban Board pages.
  - [Backlog Kanban Board](https://app.notion.com/p/0579219a469182f1954401f71214631a).
- **Master reports:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/`.
- **Audience table 2b:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/Audience Segmentation/Data Tables_Audience Segmentation/Audience Use Cases.csv`.
- **Lecture:** `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md` (ends at 1:51:37).
- **Homework and syllabus:** `.claude/skills/residency-context/reference/week-2-3.md` and `syllabus.md`.
- **Product risks:** `caregiving-coordinator/docs/risk-profile.md`.
- **Git (2026-11-11):**
  - PRs 44, 45, 46 and 47 are all merged. Current branch: `notion-backlog`, last commit `f694f55`.
  - This report isn't committed.
  - Left uncommitted on purpose: `caregiving-coordinator/docs/sources/competitive-analysis-4/live-pages/raw/il.html` and `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** see section 1. Each deliverable was approved by the owner in chat on 2026-11-11, saved to its record file, written to FigJam or Notion, and read back.
- **Checks run:**
  - Source-match scripts: 36 of 36, then 43 of 43, epic, feature and task lines found word for word in `vision-and-scope-boards-2026-11-10.md` and `epics-features-tasks-2026-11-11.md`.
  - FigJam read-backs: epics section 20:1588, text matches, 0 overlaps, 0 "Enter the…" boxes left. Roadmap calendar 22:4543, text matches, 0 overlaps, every bar in its planned column.
  - Notion read-back: 11 rows, every field matches the record.
  - `gh pr view` for 44 to 47: all merged.
  - `check_handoff.py` on this report (result in chat).
- **Not checked:**
  - The roadmap calendar's tiny date labels weren't read by eye. The weeks were matched by counting 52 columns from 12/31.
  - The lecture parts on acceptance criteria and BDD weren't re-read this session.
  - The Notion "Market Research", "Product Release Vision and Scope" and "Product Pitch Deck" pages weren't opened.
  - The original posts behind the master reports weren't re-read.
- **How this prevents drift:** every outcome is tagged Approved with its record and PR; exclusions say when they come back; step 2 stops for the owner before any drafting.
