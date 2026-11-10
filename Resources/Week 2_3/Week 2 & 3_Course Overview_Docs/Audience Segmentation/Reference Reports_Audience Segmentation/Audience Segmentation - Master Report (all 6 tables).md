# Audience Segmentation: Master Report (all 6 tables)

Written 2026-11-09. Built from the 6 data tables in `Data Tables_Audience Segmentation/`. Those tables were copied from the owner's Figma section "Audience Segmentation, Goals, Motivations, and Use Cases" (node 2842:17342), and every cell was checked against Figma.

**Tags:**
- **Fact** = copied from a table, a saved file or the course lecture.
- **Approved** = the owner decided it.
- **Proposed** = my reading. The owner has not reviewed it yet.

**How to use this report:** you can understand the whole audience segmentation from this file alone.
- Sections 1 to 3 say what audience segmentation is and how the tables fit together.
- Section 4 gives the key content of every table.
- Sections 5 and 6 give the outcomes and what was discovered.
- Section 7 says what was learned.
- Sections 8 and 9 list what disagrees and what is missing.
- Section 10 says where it points next.

---

## 1. Purpose of this report

- **Plain words:** one report that holds the result of the whole audience segmentation, so no one has to reopen the Figma section or the 6 tables.
- **What audience segmentation is** (Fact, Week 2 lecture, 1:37:48 to 1:39:30): a description of the groups of people the product serves. It is not a set of personas. It follows a template:
  - what motivates each audience
  - their situational goals (what they want in the moment)
  - their life goals
  - a table of problems, when each problem happens, and what the business wants to change
- **Where it feeds** (Fact, Week 2 lecture):
  - "What we want to change" holds business goals: what, not how. They go into the vision boards (1:39:00 to 1:39:30).
  - Positioning statements are written one per audience (1:37:36).
  - Vision boards are one board per audience per release (1:42:01).
- **Required:** audience segmentation is part of the required minimum for the Week 2 coding challenge, with product positioning and the unique value proposition (Fact, lecture 1:26:37 to 1:26:58).
- **What this report can answer:**
  - who the two audiences are
  - what drives them and what they want
  - which problems they have, and how often each comes up
  - how far to trust the numbers
- **What it cannot answer:**
  - how many caregivers nationally belong to each audience in each problem
  - who pays for help
  - which product to build (the scenarios are open problems, not features)

## 2. The two audiences (Approved)

| Audience | Who | Approved |
|---|---|---|
| **Audience 1** | Adult child (or child-in-law) caring for a parent | Yes (2026-11-07 handoff, section 1) |
| **Audience 2** | Spouse or partner caring for a husband, wife or partner | Yes (same) |

- **National size** (Fact, table 1):
  - 40% of caregivers care for a parent, and 7% for a parent-in-law.
  - 15% care for a spouse or partner.
  - So Audience 1 is about three times larger than Audience 2 (Proposed reading of those numbers).

## 3. How the 6 tables fit together

| # | File | Section | Question it answers | Rows | Split by audience? |
|---|---|---|---|---|---|
| 1 | `Audience Segmentation Definition.csv` | 1 | Who caregivers are: where they live, what they do, who they are, their money situation | 20 | No, all US caregivers |
| 2a | `Audience Motivations and Goals.csv` | 2 | Why each audience acts, what they want now, what they want for their own life | 34 | Yes |
| 2b | `Audience Use Cases.csv` | 2 | Each audience's problems, when they happen, what should change, scenarios to support | 21 | Yes |
| 2c | `Audience Sources and Limits.csv` | 2 | How 2a and 2b were made, and their limits | 16 | Notes |
| 3a | `Top Problems.csv` | 3 | Top problems, with each kind of source side by side | 11 | No, both together |
| 3b | `Top Problems Sources and Limits.csv` | 3 | Who the posts are about, other problems, and limits | 17 | Notes |

**How they flow:**
- Table 1 gives the national picture.
- Table 3a ranks the problems across every source.
- Tables 2a and 2b go deeper for each audience: why they act, what they want, and what to change.
- Tables 2c and 3b say how far to trust them.

**How the samples fit** (Proposed, from the numbers):
- Tables 2a and 2b use 303 Reddit posts (268 about a parent, 35 about a spouse) and 109 forum threads (55 parent, 54 spouse) (2c).
- Those match the parent and spouse posts inside the samples of table 3a: 269 parent and 35 spouse of the 412 Reddit posts, and 55 parent and 54 spouse of the 117 forum threads (3b).
- So 2a and 2b look like the parent and spouse part of the same samples. There is one difference of 1 post (268 vs 269), covered in section 8.

## 4. Key content of every table (Fact)

### Table 1: Who family caregivers are (AARP/NAC 2025 unless noted)

| Segment type | Main facts |
|---|---|
| Geographic | 40% live with the person; 35% live within 20 minutes; more than 10% live an hour or more away. Urban 35%, suburban 44%, rural 20%. |
| Behavioral | 44% are in high-intensity care, averaging 27 hours a week. 34% have no other help. 55% do medical or nursing tasks, but only 22% were trained. Only 58% find coordinating with providers easy. Remote monitoring is used by 25%, up from 13% in 2020. |
| Demographic | 63 million US adults (about 24%) are caregivers. Average age 50.6; 61% women. 70% of those aged 18 to 64 have a job. 29% have children or grandchildren under 18 at home. |
| Socioeconomic | 47% had at least one negative financial impact; about 1 in 5 report high financial strain. 20% left bills unpaid or paid late. Median household income $68,770. Willingness to pay: about 20% would pay nothing, and willing payers cap near $70 a month, for monitoring (Schulz 2016). 12% would pay out of pocket (Caregiver Action Network 2026). |

### Table 2a: What drives each audience (top items; rank 1 = most common)

| | Audience 1: adult child | Audience 2: spouse or partner |
|---|---|---|
| **Top motivation** | Keeping their parent safe and comfortable, and sparing them suffering | Love, loyalty and their vows |
| **2nd motivation** | Doing the right thing and not carrying guilt or blame | Keeping their partner safe, comfortable and with dignity |
| **Top situational goal** | Understand what is happening and what to do next | Get help, relief or services |
| **2nd situational goal** | Get help, relief or services | Understand what is happening and what to do |
| **Top life goal** | Keep their own health and sanity | Keep their own health and sanity |
| **2nd life goal** | Keep their own life, job and money | Keep their own life, job and money |
| **Count** | 6 motivations, 8 situational goals, 6 life goals | 4 motivations, 6 situational goals, 4 life goals |

### Table 2b: Each audience's problems (rank, problem, posts and threads seen in)

| Rank | Audience 1: adult child | Seen in | Audience 2: spouse or partner | Seen in |
|---|---|---|---|---|
| 1 | Carry the care, often alone, and can't get a break even when help exists | 138 | Carry the care, often alone, and lose health, sleep, closeness and breaks | 45 |
| 2 | A parent's anger, confusion and anxiety make visits, calls and big talks hard | 82 | The partner's confusion and mood swings turn daily life and talks into fights | 24 |
| 3 | Care costs, benefits and legal papers pile up | 74 | Hands-on care and medicines every day, sometimes with a partner who resists | 24 |
| 4 | Daily hands-on care, meals and medicines | 62 | Finding helpers they trust, and understanding hospice | 14 |
| 5 | The parent says no to doctors, help, moving or giving up the car | 60 | Worry about income, insurance and treatment costs | 13 |
| 6 | Relatives stay away, refuse to help or fight over decisions | 48 | Family and friends criticize, doubt or drift away | 12 |
| 7 | Choosing, affording and arranging a new home | 46 | Waiting and pushing for a diagnosis | 11 |
| 8 | A parent at home falls, wanders or gets hurt | 37 | The partner denies needs and refuses help or changes | 9 |
| 9 | Waiting for answers, being dismissed, hearing about problems late | 30 | Choosing and paying for memory care, and the move | 9 |
| 10 | Living far away and not knowing how the parent really is | 20 | Fear the partner will get lost or hurt when out or alone | 8 |
| 11 | Can't get into the parent's bank, phone or online accounts | 8 | | |

Each problem in table 2b also has 2 to 4 "when it happens" moments, "what we want to change" goals and "scenarios to support". See the CSV for those.

### Table 3a: Top problems across all sources (rank 1 = biggest)

| Rank | Problem | Reddit: mentioned in (of 412) | Forums: mentioned in (of 117) |
|---|---|---|---|
| 1 | Burnout, guilt, isolation, grief | 210 (51%) | 50 (43%) |
| 2 | Money, accounts and legal papers | 117 (28%) | 39 (33%) |
| 3 | Choosing, placing and paying for care | 90 (22%) | 35 (30%) |
| 4 | Family coordination and siblings | 97 (24%) | 28 (24%) |
| 5 | Dementia behavior and communication | 99 (24%) | 40 (34%) |
| 6 | The person refuses help | 83 (20%) | 12 (10%) |
| 7 | Medications | 55 (13%) | 19 (16%) |
| 8 | Safety and knowing a parent is OK | 77 (19%) | 28 (24%) |
| 9 | Doctors, appointments, records | 88 (21%) | 23 (20%) |
| 10 | Hands-on personal care, equipment and supplies | Main topic in 17 (4%) | Not a forum theme |
| 11 | The caregiver's own life (job, money, health) | 113 (27%) | 30 (26%) |

- **National data in table 3a:** 39% say a break would help, but only 13% have used one (AARP/NAC 2025). 59% of dementia caregivers report high emotional stress (Alzheimer's Association 2026).
- **Who is cared for** (3b): in the Reddit sample, 65% are parents and 8% are spouses. The forums are split almost evenly (55 parent, 54 spouse), because ALZConnected has many spouses.

## 5. Outcomes: what the audience segmentation produced

| Outcome | Status | Where |
|---|---|---|
| Two audiences defined | **Approved** | Section 2 above |
| Motivations, situational goals and life goals for each audience, ranked from 412 posts and threads | **Fact** (built and on the Figma clean page) | Table 2a |
| 11 use cases for Audience 1 and 10 for Audience 2, each with when, what to change, and scenarios | **Fact** | Table 2b |
| A ranked list of 11 top problems across four kinds of sources | **Fact** | Table 3a |
| National facts on who caregivers are | **Fact** | Table 1 |
| The use cases fed the competitive analysis need columns: the break (use case 1), a parent who refuses help (use cases 5 and 8), relatives (use case 6) and accounts (use case 11) | **Approved** (2026-11-07 handoff, sections 1 and 5) | `dogfood-2026-11-07-handoff-feature-comparison-analysis.md` |
| The data is now in 6 CSV tables, an index and an AI prompt, also in Figma (section 2997:4593) | **Fact** (2026-11-09; PR 36 open) | `Data Tables_Audience Segmentation/` |

## 6. What was discovered (all **Proposed**, each based on the table named)

1. **Not getting a break is the number 1 problem for both audiences.**
   - It is rank 1 for both audiences in table 2b: 138 posts and threads for adult children, 45 for spouses.
   - Burnout is rank 1 in table 3a, mentioned in 51% of Reddit posts and 43% of forum threads.
   - This matches the market analysis opportunity: helping worn-out caregivers reach relief (Approved 2026-11-05).
2. **The break exists but people can't reach it.** Nationally, 39% say a break would help but only 13% have used one (table 3a, 2c). The blockers named in table 2b, use case 1:
   - cost
   - paperwork, often the VA's for spouses
   - a refusing parent
   - siblings who won't step in
3. **The two audiences want different things.**
   - **Adult children act from duty and safety.** Their motivations include guilt and blame (2a, motivation 2).
   - **Spouses act from love and their vows.** They lose closeness and feel alone in the marriage (2a, life goal 3; 2b, use case 1).
   - **Adult children first want to understand what is happening.** Spouses first want help (2a, situational goal 1).
4. **Some problems belong mostly to Audience 1:**
   - money, benefits and legal papers (rank 3, 74)
   - a parent who refuses help (rank 5, 60)
   - relatives who won't share the work (rank 6, 48)
   - living far away (rank 10, 20)
   - getting into a parent's accounts (rank 11, 8)
5. **Some problems belong mostly to Audience 2:**
   - finding helpers they trust and understanding hospice (rank 4, 14)
   - waiting for a diagnosis (rank 7, 11)
   - choosing memory care (rank 9, 9)
   - losing closeness inside the marriage (rank 1)
6. **Both audiences share** confusion and mood swings (rank 2 for both) and daily hands-on care and medicines (rank 4 for adult children, rank 3 for spouses) (table 2b).
7. **Caregivers protect their own life too.** Both audiences' top life goals are their own health and sanity, then their own job and money (2a). Nationally, 70% of caregivers aged 18 to 64 have a job (table 1).
8. **Money is tight, and paying is uncertain.**
   - 47% had a negative financial impact (table 1).
   - Only 12% would pay out of pocket.
   - Willing payers cap near $70 a month (table 1).
   - So the question "who pays" stays open.
9. **A random sample can hide a real problem.** Account access is only 8 posts in the random sample (2b, rank 11), but a targeted search found 132 posts about it (2c, 3a).
10. **The refusing-person problem looks different by source.** It is the main topic in 9% of Reddit posts but only 3% of forum threads (table 3a). For adult children it is use case 5, with 60 posts and threads (2b).

## 7. What was learned (all **Proposed**)

**About the method**
- **One reader coded each post, and no person double-checked** (2c, 3b). Treat counts as directional, not exact.
- **People who post online lean toward hard moments** (2c, 3b). The tables show the harder side of caregiving.
- **Audience 2 is thin:** 35 Reddit posts (2c). Its ranking is less certain, and ties exist (ranks 2 and 3 both 24; ranks 8 and 9 both 9).
- **Targeted searches find what random samples miss.** The account access gap shows this (8 vs 132).
- **Different tables count differently.** Table 3a counts both audiences across all sources. Table 2b counts each audience on its own. Their numbers can't be added or matched one to one.

**About the deliverable**
- **Audience segmentation is not personas.** It describes groups by motivations, goals and problems (lecture 1:37:54).
- **"What we want to change" is the business goal.** It says what, not how, and it feeds the vision boards (lecture 1:39:00 to 1:39:30).
- **Scenarios are open problems, not features** (2b description, 2c).
- **Each audience needs its own positioning statement and its own vision board** (lecture 1:37:36, 1:42:01).

## 8. Where the tables disagree or need checking

| # | What was found | Where | Status |
|---|---|---|---|
| 1 | Forum totals differ: 117 threads here, 141 in the market analysis | Table 3a vs `Market Opportunity.csv` | **Open.** No saved file explains it |
| 2 | Parent posts: 268 in 2c, 269 in 3b | Tables 2c and 3b | **Open.** One post apart |
| 3 | The Nov 5 audience review approved 4 sections, including "Exhaustion and getting a break, by audience" (2834:3088). That section is no longer in Figma | `docs/clean-deliverables/audience-review-2026-11-05.md` vs Figma | **Resolved.** The owner rebuilt the audience sections (2026-11-09). The break content is merged into use case 1 for both audiences, table 2c (831 break posts) and the national break numbers. Not lost |
| 4 | Table 2c's "About this section" note says "Where the data comes from is at the bottom", which refers to the Figma layout | Table 2c, row 1 | **Left.** Copied word for word from Figma |
| 5 | 14 of 34 rows in table 2a have no examples | Table 2a | **Left.** Figma gives none |
| 6 | AARP page numbers: some say "PDF p." and some only "p.", so it isn't clear whether they are PDF or printed pages | Tables 1 and 3a | **Open** |

## 9. What is missing or worth checking (all **Proposed**)

- **Table 1 isn't split by audience.** National facts for adult children vs spouses would sharpen the segmentation.
- **There are no national counts for each use case.** The counts come from online posts only.
- **More spouse posts** would make Audience 2's ranking firmer.
- **Business goals are written per problem, not as one goal per audience.** The vision board will need a short list per audience.
- **Who pays is still open.** It's also open in the market analysis.

## 10. Where it points (**Proposed**)

- **The audience segmentation backs the market analysis opportunity:** help worn-out caregivers reach a real break (use case 1 for both audiences, burnout rank 1).
- **For Audience 1:** the break is blocked by cost, paperwork, a refusing parent and relatives who won't help.
- **For Audience 2:** the break is blocked by paperwork (often the VA's), trust in helpers, and loneliness inside the marriage.
- **Next deliverables that use this report:**
  - positioning, with one statement per audience
  - vision boards, with one per audience per release, using "What we want to change" as business goals

---

## 11. Verification receipt

- **Built from:** the 6 CSV files in `Data Tables_Audience Segmentation/` (each cell checked against Figma on 2026-11-09), the Week 2 lecture transcript (`Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`), `docs/clean-deliverables/audience-review-2026-11-05.md`, and the 2026-11-07 and 2026-11-08 handoff reports.
- **Checks run:** every number in this report was looked up in the 6 CSVs, the lecture or the named file (script result in chat, 2026-11-09).
- **Not checked:**
  - the original posts and threads (counts were read from the tables)
  - the AARP, Alzheimer's Association, Schulz and Caregiver Action Network reports themselves
  - the 268 vs 269 parent-post gap (one post; it changes no ranking)
- **Owner review:** everything tagged Proposed is waiting for the owner.
