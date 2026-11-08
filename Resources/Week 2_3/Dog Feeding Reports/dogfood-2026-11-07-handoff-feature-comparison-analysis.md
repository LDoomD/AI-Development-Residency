# Handoff: Caregiving Coordinator → feature comparison analysis (Feature Analysis 4) (2026-11-07)

Replaces: `dogfood-2026-11-06-handoff-competitive-analysis-4.md` (its steps 3 to 5 are done or moved into this report). Also replaces, by chain, `dogfood-2026-11-06-handoff-feature-analysis.md` and `dogfood-2026-11-05-handoff-skill-evals-then-feature-analysis.md`. The audience and market tables from `dogfood-2026-11-05-handoff-feature-analysis.md`, sections 3A and 3B, still stand. Its competitive tables (3C) are **replaced** by section 2 of this report.

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what the feature comparison analysis starts from. Then show me the research checklist for it before doing anything else. Keep replies short, plain, and one question at a time."

## 0. Start here
- **Where we are:** the competitive analysis (deliverable 3) is finished and live in Figma. The owner's three deliverables so far are market analysis, audience segmentation and competitive analysis. The goal of the whole homework is a product the owner can position, then a release vision and backlog.
- **The outcome so far, in one sentence:** none of the 16 competitors gives an ordinary family caregiver a clear Yes on the parent's money, on a parent who refuses help, or on relatives sharing the work. Only 5 of 80 need cells are a clear Yes, and 4 of those 5 are limited to employees, veterans or people who find a center (`competitive-analysis-4-updated-2026-11-07.md`, section 4c).
- **Next milestone:** the **feature comparison analysis**, in the teacher's format (Figma example node 5:638). Rows are the 16 competitors plus a blank OUR COMPANY row. Columns are 6 fact columns plus the 9 feature columns the owner approved. Cells hold only ✅ or 🚫. Build a markdown preview first, then Figma.
- **Pull request check (2026-11-07):** the competitive analysis pull request was opened on 2026-11-07 from branch `competitive-analysis-4-updated`, with its draft file and this report. The owner reviews and merges it. Before the next step, run `gh pr list --state open`. If it is still open, say one line: "The competitive analysis PR isn't merged yet. Merge it first, or keep going?" (project rule, `CLAUDE.md`, item 4 of "Remind the user").

## 1. Locked outcomes

**Market analysis** (Figma 2808:13693, 2812:14373, 2813:14661, 2815:15035; record `docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`)
- Largest opportunity: helping worn-out caregivers reach relief (segments 11 and 12). **Approved** 2026-11-05 (`docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`). Not changed today.

**Audience segmentation** (Figma 2834:2844, 2834:2867, 2834:16750; record `docs/clean-deliverables/audience-review-2026-11-05.md`)
- Audience 1 is an adult child caring for a parent. Audience 2 is a spouse or partner. **Approved**. Not changed today.
- The audience for the table is "anybody": any caregiver, paid or unpaid, registered or not. **Approved** 2026-11-06.

**Competitive analysis** (finished 2026-11-07; Figma section 2949:2168; record `docs/clean-deliverables/competitive-analysis-4-updated-2026-11-07.md`)
- **20 cell corrections** to the 9 approved rows, from the Nov 6 audits. **Approved**: the owner said "No" to leaving any of the 18 differences out on Nov 6, approved 3 Caring Village cells and all 7 rating changes on Nov 7. Record: `docs/clean-deliverables/competitive-analysis-4-updated-2026-11-07.md`, change log. One correction moved: the VA's 70% rating claim sits in the Weaknesses cell, not the Type cell.
- **Care manager price** is $150 to $350 an hour in 4 places (`docs/clean-deliverables/competitive-analysis-4-updated-2026-11-07.md`, "Price fix"). **Approved**.
- **7 new competitors added**: Care.com; Medicaid and state paid-caregiver programs; support groups (the Alzheimer's Association's groups count inside this row); Facebook caregiver groups; therapist; aide paid by the family; aide paid by a program. **Approved** 2026-11-07.
- **Cell format:** each needs cell is the score, "because" and the reason, then "Open to:" for Yes and Partly. **Approved**.
- **Five plain column titles:** Knowing what to do; A real break; The parent's money; Parent accepts help; Relatives share the work. **Approved**.
- **"How they keep customers"** reads "None: no company behind it" for the 6 rows that are not companies. **Approved**.
- **Figma method:** a new section beside the old one, built by cloning the owner's layout and changing only the data. The old section has a yellow banner and stays. **Approved** (option A).

**Feature comparison analysis rules** (set 2026-11-07)
1. ✅ means any caregiver can use the feature. A limited offer (employer-paid, veterans only, one state, a paid plan) is 🚫 with a short tag under the icon, for example "Employer-paid only." A legend line sits above the table. **Approved**.
2. Behavior and hard talks is ✅ only with real help for the behavior itself. Help with hard talks alone is 🚫, with a note. **Approved**.
3. Caring Village is ✅ for relatives cover time (tasks can be assigned or claimed and show who finished). The 2-member free plan limit goes in the evidence row. **Approved**.
4. The 9 feature columns, with row-2 questions, were approved 2026-11-06 (table below). The first six columns for the original 9 competitors were also approved 2026-11-06. **Approved**.
5. Cells that the saved results cannot answer say "verify," never a guessed 🚫. A silent page is not a 🚫. **Approved** (2026-11-06).
6. Feature Analysis 3 and the teacher's example are **format only**. Figma is the source of truth. **Approved**.

The 9 feature columns and their row-2 questions (source: the Nov 6 session transcript `88c39ed8`, messages 18 to 21):

| # | Column | Row-2 question | Comes from |
|---|---|---|---|
| 1 | RELIEF FINDER | Does the product offer ways to find respite, adult day or in-home breaks near the caregiver? | Gap 4, use case 1 |
| 2 | ELIGIBILITY AND APPLICATIONS | Does the product offer ways to check eligibility and apply for programs that give or pay for relief? | Gap 4 |
| 3 | PAYING FOR RELIEF | Does the product offer ways to learn what a break costs and how to pay for it? | Gap 4, use case 3 |
| 4 | REFUSING PARENT SUPPORT | Does the product offer ways to help a caregiver get a parent or partner who says no to accept help? | Gap 1, use cases 5 and 8 |
| 5 | RELATIVES COVER TIME | Does the product offer ways to give real tasks or time off to relatives and see that they happen? | Gap 1, use case 6 |
| 6 | ACCOUNT ACCESS | Does the product offer ways to help a caregiver get into a parent's bank, insurance or online accounts when the parent can't set it up? | Gap 3, use case 11 (`docs/clean-deliverables/audience-review-2026-11-05.md`) |
| 8 | PERSONAL GUIDANCE | Does the product offer ongoing one-to-one guidance from a coach or care expert? | Gap 2 |
| 9 | BEHAVIOR AND HARD TALKS HELP | Does the product offer ways to understand dementia behavior and handle hard talks? | Use case 2 |
| 10 | PEOPLE WHO UNDERSTAND | Does the product offer ways to connect caregivers with support groups or other caregivers? | Audience 2 use case 1, segment 12 (`docs/clean-deliverables/audience-review-2026-11-05.md`) |

Columns 7 (papers and documents) and 11 (shared care updates) were dropped: they overlap columns 6 and 5 and answer no gap (`docs/reports/feature-analysis-4-change-report-2026-11-06.md`, section 3, error 3). The numbers above keep the original numbering.

## 2. Key findings and data

**The 5 needs for all 16 competitors** (source: `competitive-analysis-4-updated-2026-11-07.md`, section 4c; Figma table 2949:2180). Every cell in the file also says why and who can get it. Confidence: Credible secondary for the 9 approved rows (three audit passes). Estimate for the 7 new rows (the audit did not re-check their need labels, which the helper's own files call "inferred").

| Competitor | 1 Knowing what to do | 2 A real break | 3 The parent's money | 4 Parent accepts help | 5 Relatives share the work |
|---|---|---|---|---|---|
| Caring Village | Partly | Partly | Partly | No | Partly |
| Everplans | No | No | Partly | No | Partly |
| Cariloop | Yes | Partly | Partly | Partly | Partly |
| A Place for Mom | Partly | Partly | Partly | Partly | No |
| Geriatric care managers | Yes | Yes | Partly | Partly | Partly |
| Group texts and notebooks | Partly | No | Partly | No | Partly |
| Area Agencies on Aging | Partly | Partly | Partly | No | Partly |
| Respite and adult day | Partly | Yes | No | No | Partly |
| VA caregiver programs | Partly | Yes | Partly | Partly | Partly |
| Care.com (new) | Partly | Partly | No | No | Verify |
| Medicaid and state programs (new) | Partly | Partly | Partly | No | No |
| Support groups (new) | Partly | No | No | No | No |
| Facebook groups (new) | Partly | No | No | No | No |
| Therapist (new) | Partly | Partly | No | No | No |
| Aide paid by the family (new) | No | Partly | No | Partly | Verify |
| Aide paid by a program (new) | No | Partly | Partly | No | Verify |
| **Clear Yes count** | 2 | 3 | 0 | 0 | 0 |

**The 9-feature grid for the original 9 competitors** (Y = yes, L = limited to some people, N = no, V = verify). Source: the final tables in each company's `docs/sources/feature-analysis-4/<company>/AUDIT-PASS3.md`. Confidence: Credible secondary (three passes; about 1,000 quotes script-checked, almost no invented). This grid **predates** the 20 cell corrections and today's rules. Under rule 1, every L becomes 🚫 with a tag. Counts: 2 clean Yes, 46 L, 3 mixed (respite), 23 No, 7 verify, out of 81.

| Company | Relief finder | Eligibility | Paying | Refusing parent | Relatives cover | Accounts | Guidance | Behavior/talks | People |
|---|---|---|---|---|---|---|---|---|---|
| Caring Village | L | N | L | N | L | N | L | L | N |
| Everplans | N | N | N | N | N | L | N | L | N |
| Group texts, notebooks | N | N | N | N | L | L | N | N | V |
| Cariloop | L | L | L | V | L | V | L | L | L |
| A Place for Mom (pages withdrawn) | L | L | L | V | N | N | L | V | L |
| Geriatric care managers | Y | L | L | L | L | L | Y | L | V |
| Area Agencies on Aging | L | L | L | N | L | L | L | L | L |
| Respite and adult day | Y find / L get | L | Y info / L pay | N | L | N | L | L / V | V |
| VA caregiver programs | L | L | L | L | L | N | L | L | L |

Notes: A Place for Mom's row rests on Reddit, BBB and older pages only (its robots.txt blocks ClaudeBot, so 23 saved pages were deleted). Everplans account access works only on the paid plan and after a death. Cariloop works only through an employer or insurer. Caring Village relatives is ✅ by rule 3.

**Evidence behind the 7 new rows** (none has been scored on the 9 features yet):

| Row | Independent caregiver reports | Source | Confidence |
|---|---|---|---|
| Care.com | 52 (18 used it, 13 told how it went) | `docs/sources/competitive-analysis-4/paid-help-and-therapists/SYNTHESIS.md` 3.1, `AUDIT.md` | Credible secondary |
| Aide paid by the family | 84 (12 worked, 17 mixed, 19 did not, 36 no result; payer named in only 27) | same, section 5, `AUDIT.md` correction 4 | Estimate |
| Aide paid by a program | 41 (6 / 11 / 11 / 13) | same, `AUDIT.md` correction 5 | Estimate |
| Therapist | 123 (27 / 10 / 23 / 63) | same, `AUDIT.md` correction 6 | Credible secondary |
| Medicaid and state programs | 78 (30 dated to one New York payroll change) | `docs/sources/competitive-analysis-4/support-government-community/SYNTHESIS.md` sections 2 and 6, `AUDIT.md` | Credible secondary |
| Support groups | 37 read of at least 114 | same | Credible secondary |
| Facebook groups | 21 (mostly negative) | same | Estimate |

Also found (`paid-help-and-therapists/AUDIT.md`): 39 paid-aide posts name a refusing parent and only 3 worked. Most paid-help failures are "could not get it" (waitlists, minimum hours, eligibility, cost). The "Alzheimer's Association" has 19 reports but 10 are Reddit only.

**The 4 gaps** (unchanged, `docs/clean-deliverables/competitive-preview-2026-11-05.md`; not yet re-checked against the 7 new rows):
1. No one handles a parent who refuses help, or gets relatives to share the work.
2. Personal, ongoing guidance is locked behind an employer or a big hourly bill.
3. Help with money and accounts works only if the parent prepared ahead.
4. Relief exists, but caregivers can't reach it. This is the approved market opportunity.

## 3. Excluded and deferred
- **Alzheimer's Association as its own row.** Counted inside support groups: its groups are already in that row, and half its reports come from its own forum. The owner agreed 2026-11-07.
- **Not enough evidence** (each under 15 reports): Visiting Angels, Home Instead, BetterHelp, CareYaya. **Left out** (0 to 6 reports): Papa, Talkspace, Headway, Wellthy, Lotsa, Cozi, CaringBridge, Meal Train, Teepa Snow, NAMI. Source: the two `AUDIT.md` files above.
- **Meals on Wheels:** about 45 real mentions, but it meets a food need, not relief.
- **Parked until the release vision deliverable:** MVP and MMP scoring (Figma 2598:11009), prioritize use cases (2378:7243), and the who-pays research (employers, Medicare GUIDE, families).
- **Not used:** NotebookLM for research (owner, forever); the INVEST skill for analysis work (owner, 2026-11-06). The hook may offer INVEST at the start of a deliverable. Do not offer it for this one.
- **Stopped:** the report for the owner's teacher meeting.
- **Noted, not researched:** Clubhouse-style live audio rooms for caregivers (the owner's idea).
- **Feature Analysis 3** as a content source. It stays as a format reference and gets a yellow banner in Figma at the end (node 2584:10359).

## 4. Open decisions
The next session must not decide these alone.
- **Feature column titles.** The nine titles above use the teacher's capital-letter style. The owner asked on 2026-11-07 for short titles that are "intuitively easy to understand," like "A real break." Propose plain titles, and let the owner choose.
- **The OUR COMPANY row.** The owner fills it in.
- **The 7 "verify" cells and the 5 unanswered business model cells** (Care.com's own pricing and customer experience; support group and Facebook cost). Research them, or leave them as "verify"? The owner has not said.
- **Re-check the problems table (2a) and the 4 gaps against the 7 new rows.** Figma's subtitle says they were not re-checked.
- **Market analysis:** add the 7 names as examples in segments 5, 11 and 12? No sizes change. Not decided.
- **Merging the competitive analysis pull request.** The owner merges it (learner mode). One deliverable, one branch, one pull request.
- **Where reports and course files live.** The owner moved `Dog Feeding Docs/Week 2_3/` to `Resources/Week 2_3/Dog Feeding Reports/` and added `Resources/` and `Course Overview/`. `CLAUDE.md` (lines 97, 100, 118) still points to the old folder. The `Resources/` layout proposal (weeks with their files inside) and saving the Notion pages were **not approved**.
- **Still open from earlier handoffs:** the new Week 2 due date; the instructor repo invite (`mdenner1234`, check with `gh api repos/LDoomD/AI-Development-Residency/invitations`); the duplicate audience section 2061:543 in FigJam; wrap-up in the app repo; the owner's new enterprise plan type. The repo is **public** for now (the owner will switch it back to private).

## 5. Bridge to the next milestone

**How the earlier deliverables shaped the competitive analysis** (this answers the owner's question):

| Earlier deliverable | What it gave | How it changed the outcome |
|---|---|---|
| Market analysis, segments 11 and 12, and the opportunity answer | The approved answer: help worn-out caregivers reach relief. It names the help caregivers use: Medicaid and waiver programs, therapists, support groups, online caregiver groups. | Decided the 7 new rows. Segment 5 (home care and marketplaces) brought in Care.com and the two aide rows. Their segment labels fill the "Market segment" column. |
| Market analysis, "Few competitors?" and "Unmet need?" columns | Segment 11 verdict: relief exists but many can't get it (78 of 341 respite posts couldn't get a break). | Became Gap 4 and the reason "Open to:" matters in every cell. |
| Audience segmentation, top problems and use cases | Parent refuses help (problem 5; use cases 5 and 8), relatives (problem 6; use case 6), accounts (use case 11), the break (use case 1). | Became needs 3, 4 and 5 and the feature columns. Need 4 shows where no competitor gets a Yes. |
| Audience segmentation, two audiences | Adult children (Audience 1) and spouses (Audience 2). | Every count in the research splits by who is cared for. Spouse evidence is thin for Care.com, Medicaid and aides. |
| The owner's decisions | "Anybody" audience; ✅ means yes; plain words; a reason in every cell. | Changed the cell format, the column titles and how limited offers show. |

**How the competitive analysis feeds the feature comparison:**

| This output | Goes into | Why |
|---|---|---|
| The 16 rows (9 approved plus 7 new) | The ✅/🚫 table, one row each, plus a blank OUR COMPANY row | The competitor set is settled |
| Profile and business model tables (4a, 4b) | The first six columns: company, website, pricing, market, segment, customers | The owner approved these for the first 9 rows. The 7 new rows have draft cells, some "verify" |
| The 9-feature grid and the 3 rules | Every ✅/🚫 cell and its tag | The grid is the evidence. Apply the rules: limited becomes 🚫 with a tag |
| The 5-needs table | The evidence row and a cross-check | Needs 3, 4 and 5 have no clear Yes, so features 4, 5 and 6 should show mostly 🚫 |
| The 4 gaps | The "common, unique, missing" read after the table | Features should fill the gaps |
| Open "verify" cells | A list for the owner | The owner decides whether to research them |

## 6. First steps
1. **Confirm where we are in a few lines.** Run `gh pr list --state open`. If the competitive analysis pull request is still open, say one line and ask: merge it first, or keep going? Do not offer INVEST. If the owner asks for something different, do that first.
2. **Fill in the research checklist for the feature comparison and show it. Stop and wait.** Update `docs/research-checklist-feature-analysis-4-2026-11-06.md` (it predates today). It must list the inputs, split by Audience 1 and 2, and the questions. Say which files it will read.
3. **Search all saved research** on the feature topics (relief, respite, eligibility, refusing parent, accounts, relatives, support group) and show the inputs table: each file, used or left out, and why.
4. **Show the 9 feature columns** with plain titles and the row-2 questions, and let the owner pick the titles (open decision).
5. **Build the grid for the 9 approved competitors** from the audited grid, with the 3 rules. Show it as a plain markdown table in chat. Every limited cell is 🚫 with a short tag. Include the legend line.
6. **Score the 7 new rows on the 9 features from saved results only** (`SYNTHESIS.md` and `AUDIT.md`). Mark "verify" where the results are silent. Show the list of verify cells and ask whether to research any.
7. **Read the finished table** for what is common, unique and missing, and which gaps matter for each audience.
8. **Build it in Figma** as a new section on the clean page, by cloning the teacher's layout and changing only the data (the owner said: use the existing layout and update the data). Then put a yellow banner on Feature Analysis 3.
9. **Save it on a new branch** named for the deliverable, then open the pull request. The owner reviews and merges. Remind the owner to ask for a dog feeding report before a new chat.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. The ones broken today:
- **Open the files before answering.** Today the first answers came from the handoff alone and were wrong. Say which file or Figma node an answer came from.
- **Questions get answers, not edits.** One question at a time. Do not create files, branches, rules or skills the owner has not approved.
- **Show tables in chat as plain markdown tables.** No widgets, no click-to-open views, no markdown files as the first look. The owner said so.
- **Plain, short column titles and cell wording.** Explain every name. A score needs its reason ("Partly, because ..."), not a bare word.
- **Use the existing layout and update the data.** In Figma, clone the owner's section and change the data. Never overwrite the original. Mark replaced work with a yellow banner.
- **Show the owner the whole change before Figma.** Then verify against a screenshot.
- **A raw count is not a finding.** Candidates come from the data and the deliverables, not from Claude's own list.
- **The owner merges their own pull requests.** One deliverable, one branch, one pull request. Never run `gh pr merge`.
- **Never write or edit the owner's homework summary** ("What I Did" and "What I Learned").
- **Cite sources.** Respect robots.txt. Ask before using the owner's browser or the Chrome extension.

## 8. Where things live
- **Figma:** file `HcDDdEGAnikTImO8v7UPMp`, clean page 2782:15415 ("Week 2 & 3_Updated Deliverables").
  - The competitive analysis sits in Section 1 (2948:17476). New section: 2949:2168. Its tables: competitors compared 2949:2177, profiles 2949:2193, business model 2949:2194, needs 2949:2180.
  - Old section: 2843:15117, with the yellow banner 2950:3172.
  - Market analysis: 2808:13693, 2812:14373, 2813:14661, 2815:15035. Audience: 2834:2844, 2834:2867, 2834:16750.
  - The teacher's example: node 5:638 (table 5:823), on the "Tips" page. Feature Analysis 3: 2584:10359.
- **Repo:** `/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator` (note the space before the slash in "Residency /").
  - The finished competitive analysis (markdown): `docs/clean-deliverables/competitive-analysis-4-updated-2026-11-07.md`. It holds the change log, all tables and where each new row's cells come from.
  - The 20-cell changes draft: `docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`.
  - Feature evidence for the 9 competitors: `docs/sources/feature-analysis-4/<company>/` (EVIDENCE, PASS1, PASS2, AUDIT-PASS3).
  - Evidence for the 7 new rows: `docs/sources/competitive-analysis-4/paid-help-and-therapists/` and `.../support-government-community/`.
  - Research checklist: `docs/research-checklist-feature-analysis-4-2026-11-06.md`. Change report: `docs/reports/feature-analysis-4-change-report-2026-11-06.md`.
- **Reports:** `/Users/landodoom/Desktop/AI Developer Residency /Resources/Week 2_3/Dog Feeding Reports/`.
- **Memory:** `/Users/landodoom/.claude/projects/-Users-landodoom-Desktop-AI-Developer-Residency-/memory/`.
- **Git (2026-11-07):** the competitive analysis is on branch `competitive-analysis-4-updated`, in an open pull request (two files: the competitive analysis draft and this report). `main` has pull requests 31 and 32 (the Nov 6 research and the 20-cell draft), merged 2026-11-07 UTC. **Not committed:** the rest of `Resources/` and `Course Overview/`; `docs/sources/anthropic-skills-navigation/` and `docs/sources/arxiv-2611-00544/`; an edit to `docs/sources/INDEX.md`; and the 12 old `Dog Feeding Docs` files, shown as deleted because the owner moved them. This report is at the new `Resources/` path. `docs/sources/competitive-analysis-4/live-pages/raw/il.html` stays untracked on purpose (it holds a map token that GitHub blocked). Commit only when the owner asks.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2 name a file, a Figma node or the Nov 6 session for each item. The owner's approvals are from this chat on 2026-11-07, and from the Nov 6 transcript for the 18 differences and the 9 columns.
- **Checks run:**
  - The "old text" of 19 of the 20 draft cells was matched word for word against the live Figma. The 20th (VA Type) did not match, which found the VA error. It was moved to the Weaknesses cell.
  - All 104 unchanged cells in the draft file matched the live Figma.
  - 22 key numbers and phrases in the new rows were found in the saved `SYNTHESIS.md` and `AUDIT.md` files.
  - A screenshot of the new needs table in Figma shows 16 rows with the right colors.
  - `check_handoff.py` passed on this report (every required part, sources next to numbers).
  - A read-through for the four questions: where we are (section 0), what was decided (section 1), what is excluded (section 3), the first step (section 6). A fresh helper was not used.
- **Not checked:**
  - The need labels for the 7 new rows. The helper marked them "inferred" and the audit did not re-check them. Three "Open to" parts are my reading of existing cells (A Place for Mom money, Caring Village relatives, Area Agencies).
  - Company pages for the 7 new rows: none were fetched, so some cells are "verify."
  - The problems table (2a) and the gaps against the 7 new rows.
  - Whether the owner changed Figma after 2026-11-07.
  - The 9-feature grid against the 20 corrections (it predates them).
  - The owner's usage numbers.
- **How this prevents drift:** decisions are tagged Approved or Proposed, the open decisions are listed, step 1 and 2 require showing the owner a checklist before any research, and each rule names its source.
