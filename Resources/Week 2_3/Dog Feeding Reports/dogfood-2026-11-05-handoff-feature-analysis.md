> **Replaced by `dogfood-2026-11-05-handoff-skill-evals-then-feature-analysis.md`** (2026-11-05). Its project outcomes (sections 3-6) are still correct and are the inputs for the feature analysis.

# Handoff report: start the feature analysis (2026-11-05)

**This is the newest dog feeding report.** It replaces the three 2026-11-05 reports:
- `dogfood-2026-11-05-all-deliverables-clean.md`
- `dogfood-2026-11-05-clean-page.md`
- `dogfood-2026-11-05-audit-and-corrections.md`

Those are history only.

**What this report is for:** it briefs Claude on everything the next deliverable needs, in a new session or this one: where we are, what each finished deliverable found, what to reference, and exactly where to start. **Claude should be able to start the feature analysis from this file alone.** The Figma links are there for checking, not for re-reading everything.

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what the feature analysis starts from. Then fill in docs/research-checklist.md for the feature analysis and show it to me before doing anything else."

---

## 1. Where we are, and where to start

- **Homework:** Week 2 bonus work, deliverable #2 of 6: market, competitive and feature analysis, then unique positioning. Then #3, release vision and scope.
- **Done and approved today:** the market analysis, the audience segmentation and the competitive analysis. They're audited, corrected and moved to one clean Figma page: [Week 2 & 3_Updated Deliverables](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2782-15415) (page 2782:15415). **Read deliverables only from this page or this report.** Older board sections are records only.
- **The outcome so far:** the largest opportunity is **helping worn-out caregivers get relief**. Exhaustion is the #1 problem for both audiences. Help exists, but caregivers can't reach it, because of the cost, a parent who says no, paperwork and rules to qualify, and family who won't help.
- **Next deliverable: the feature analysis** (section 6 has the step-by-step start).

---

## 2. Rules (follow every one)

1. **Rule #1: one connected project.**
   - Each deliverable builds on the earlier ones.
   - Fill in `caregiving-coordinator/docs/research-checklist.md` and show it before any research or new table.
   - Split everything by audience: **Audience 1 = adult child caring for a parent; Audience 2 = spouse or partner.**
2. **INVEST.** Split work into small stories.
   - Grade each of the 6 letters pass or fail, and explain each fail.
   - Write Given/When/Then checks.
   - Wait for the owner's OK before the next story.
3. **Outcome first.** Each deliverable holds only what answers its own question. Ask: what is this for, and how does it affect the next step?
4. **Write for the owner.** 8th-grade English and UX writing: meaning first, then the number. No research jargon.
5. **Titles:**
   - Keep the template's and the existing tables' titles.
   - New or merged titles are short names, never sentences.
6. **Every cell answers its column's title.**
   - No edit history, research steps or jargon.
   - Bullets when a cell has several facts.
   - At most 4 bullets per cell, each 12 words or fewer.
7. **Table cells come from themes across the data,** never from one post. Thin data means getting more data.
8. **New research gets merged into the existing rows, use cases and verdicts,** not added as a separate section. If it means redoing a whole table, make a second version so the records are kept.
9. **Preview before Figma.** Design tables in a markdown file, mark every change with its reason, and build only after approval.
10. **Questions get answers, not edits.** Change files only after a clear yes.
11. **Never delete or overwrite deliverables.** Make new versions, and put a big yellow banner on old ones.
12. **Cite every claim** with a link and a page. Save sources in `docs/sources/` with an INDEX.md entry.
13. **Never suggest caregiver interviews.**
14. **Commit or push only when asked.**
15. **Ask before using the owner's browser.**
16. **Don't mention routine checks** (the secret scan, the arch gate) unless they find a real problem.
17. **Do only the deliverable the owner names.** Remind the owner to ask for a report at key moments.

---

## 3. Outcomes of each finished deliverable

### 3A. Audience segmentation (clean page, row 2)

**Audiences:**
- **Audience 1:** adult child (or child-in-law) caring for a parent.
- **Audience 2:** spouse or partner caring for a husband, wife or partner.

**Segmentation definition** ([2834:2844](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2834-2844)). AARP/NAC 2025, PDF pages, all checked:
- **Geographic:**
  - 40% of caregivers live with the person; 35% live within 20 minutes; more than 10% live an hour or more away (p.22).
  - Urban 35%, suburban 44%, rural 20% (p.130).
- **Behavioral:**
  - 44% are in high-intensity care, averaging 27 hours a week (p.33, p.8).
  - Only 58% find coordinating with providers easy (p.36).
  - 55% do medical or nursing tasks, but only 22% were trained (p.34).
  - 34% have no other help (p.25).
  - Remote monitoring use is 25% (p.37).
- **Demographic:**
  - 63 million US caregivers (p.12); average age 50.6; 61% women (p.15).
  - 40% care for a parent and 15% for a spouse (p.17).
  - 29% have children under 18 at home (p.24).
  - 70% of working-age caregivers have jobs (p.38-39).
- **Socioeconomic:**
  - 47% had a negative financial impact, and about 1 in 5 report high strain (p.43, p.42).
  - Median income is $68,770 (p.130).
  - Only 12% would pay out of pocket (CAN 2026), and willing payers cap near $70 a month (Schulz 2016).

**Motivations and goals** ([2834:2867](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2834-2867)), most common first:

| | Audience 1 (adult children) | Audience 2 (spouses) |
|---|---|---|
| Motivations | Keep the parent safe and comfortable; do the right thing without guilt; love and promises; let the parent stay home and choose | Love, loyalty and their vows; keep the partner safe and with dignity; keep the partner at home; do right by the partner |
| Situational goals | Understand what's happening and what to do next; get help, relief or services; get money, bills and legal papers under control; keep the parent safe | Get help, relief or services (including veterans' programs); understand what to expect; find and pay for the right place; keep the partner safe |
| Life goals | Keep their own health and sanity; keep their job and money; get time and breaks without guilt; protect their own family | Keep their own health and sanity; keep their life, job and money; companionship and someone who understands; real breaks |

**Use cases**, with the number of posts each was "seen in" (from 412 posts and threads; Audience 2 has fewer posts, so its order is less certain):

| # | Audience 1: adult children | Seen in | Audience 2: spouses | Seen in |
|---|---|---|---|---|
| 1 | **Carry the care, often alone, and can't get a break even when help exists** | 138 | **Carry the care, often alone, and lose health, sleep, closeness and breaks** | 45 |
| 2 | Parent's anger, confusion and anxiety make talks hard | 82 | Partner's confusion and mood swings turn talks into fights | 24 |
| 3 | Care costs, benefits and legal papers pile up | 74 | Hands-on care and medicines every day | 24 |
| 4 | Daily hands-on care, meals and medicines | 62 | Finding helpers they trust; understanding hospice | 14 |
| 5 | The parent says no to doctors, help, moving or the car | 60 | Worry about income, insurance and treatment costs | 13 |
| 6 | Relatives stay away, refuse to help or fight | 48 | Family and friends criticize or drift away | 12 |
| 7 | Choosing, affording and arranging a new home | 46 | Waiting and pushing for a diagnosis | 11 |
| 8 | Falls, wandering and injuries at home | 37 | The partner refuses helpers or care | 9 |
| 9 | Waiting for answers from doctors and hospitals | 30 | Choosing and paying for memory care | 9 |
| 10 | Living far away and not knowing | 20 | Fear the partner gets lost or hurt | 8 |
| 11 | Can't get into the parent's accounts (132 posts in a targeted search) | 8 | | |

**Use case 1, updated with the break research** (831 posts about getting a break: 486 from adult children, 98 from spouses):

| | Adult children | Spouses |
|---|---|---|
| When it happens | Carrying the care alone for years; **cost, paperwork or a refusing parent blocks a break**; **siblings won't step in**; juggling work and family | Carrying it alone with no time away; **paperwork and rules (often the VA's) block a break**; grief or setbacks; loneliness |
| What we want to change | Real breaks they can afford; family or paid help that steps in; coping with guilt and grief; limits without guilt | People who understand; real breaks; getting through the paperwork to qualify; closeness with the partner |
| Scenarios to support | Find a break they can afford and qualify for; get the parent to accept outside help; get relatives to cover time off; handle guilt and set limits | Find a support group or someone who understands; qualify for help, including VA programs; take a break knowing the partner is cared for; keep closeness |

**National facts:**
- 39% of caregivers say a break would help, but only 13% have ever used respite (AARP/NAC 2025, PDF pp.26-27).
- 30% want help managing stress (PDF p.53).
- 59% of dementia caregivers report high stress (Alzheimer's Association 2026, Figure 12, printed p.52).
- About 1 in 4 caregivers in both audiences need a break and have no help.
- Spouses use support groups more (22% vs 12% of posts).

**Top problems** ([2834:16750](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2834-16750)). "Mentioned in" counts come from 117 forum threads and 412 Reddit posts:

| Problem | Forum threads | Reddit posts |
|---|---|---|
| 1. Burnout, guilt, isolation, grief | 50 (43%) | 210 (51%) |
| 2. Money, accounts and legal papers | 39 (33%) | 117 (28%) |
| 3. The caregiver's own job, money and health | 30 (26%) | 113 (27%) |
| 4. Dementia behavior | 40 (34%) | 99 (24%) |
| 5. Family coordination and siblings | 28 (24%) | 97 (24%) |
| 6. Choosing, placing and paying for care | 35 (30%) | 90 (22%) |
| 7. Doctors, appointments, records | 23 (20%) | 88 (21%) |
| 8. The person refuses help | 12 (10%) | 83 (20%) |
| 9. Safety | 28 (24%) | 77 (19%) |
| 10. Medications | 19 (16%) | 55 (13%) |
| 11. Hands-on care and supplies | Not a forum theme | 17 posts as the main topic |

The table is shown here in order of Reddit mentions. On the board it keeps its original row order.

### 3B. Market analysis (clean page, row 1)

Sections:
- [1. Main research table](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2808-13693)
- [2. Possible market segments](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2812-14373)
- [3. Market size](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2813-14661)
- [4. Market opportunity](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2815-15035)

**The 14 segments and their verdicts** (section 4, plus the sizes from section 3):

| # | Segment | Problem it addresses | Size | Verdict |
|---|---|---|---|---|
| 1 | Family care-coordination apps | Updates, siblings | $1.3B to $4B (all caregiver apps) | Need is real; apps don't solve it. Caregivers use group texts and Cozi instead. |
| 2 | Medication reminder apps | Medications | $0.6B to $0.85B | Crowded and small |
| 3 | Pharmacy packaging | Medications, refills | $0.8B to $1.8B | Not open |
| 4 | Senior care referral | Choosing and paying for care | Not measurable alone | Large need, hard to enter (A Place for Mom dominates) |
| 5 | Home care and marketplaces | Hands-on care, respite | $8.7B to $9.1B | Crowded |
| 6 | Remote monitoring | Safety | $6.3B to $9.0B | Crowded |
| 7 | Employer caregiver benefits | Coaching, time, stress | $0.55B | Different customer (the employer pays) |
| 8 | Patient-side AI visit notes | Remembering what the doctor said | Not measurable | Open but unproven |
| 9 | Patient portals | Records | $3.9B to $6.6B | Not open (Epic) |
| 10 | Digital vaults (the parent's accounts) | Logins and documents | $3.1B to $3.75B | Clear need, hard to enter (bank rules, security risk) |
| **11** | **Respite and adult day services** | **Burnout, exhaustion** | **$19.3B global; $7.6B US** | **Help exists, but many can't get it. Blocked by cost, a parent who says no, paperwork and family who won't help.** |
| **12** | **Caregiver burnout support** | **Burnout, guilt** | **$7.5B to $8.2B (general mental health apps)** | **The need is large, but the apps don't reach caregivers. They get support from people: therapists, support groups, online caregiver groups.** |
| 13 | Telehealth | Appointments | $27B to $126B | Not open |
| 14 | Insurance and benefits navigation | Insurance, money | $10.1B to $10.3B | Different customer (employers and plans) |

General family organizers (Cozi, TimeTree) are segment 15 in section 2. They're what families actually use to coordinate.

**Programs caregivers name most for getting a break:**
- Medicaid and waiver programs (77 posts)
- Hospice (45)
- The VA (44)
- Area Agencies on Aging (26)
- Also: ARCH (the national respite directory), Medicare GUIDE (up to $2,500 a year for respite, dementia only), and Papa ($30 an hour)

**The approved answer:** "Which segment has the largest opportunity?" **Helping worn-out caregivers get relief (segments 11 and 12).**
- Exhaustion is the #1 problem for both audiences.
- The adult day care market alone is $19.3B.
- Caregivers want breaks far more than they get them (39% vs 13%; 78 of 341 respite posts couldn't get one).
- There's no consumer app for getting relief.
- **The care itself is a physical service.** Our opportunity is helping caregivers **reach** relief, not providing the care.

### 3C. Competitive analysis (clean page, row 3, [2843:15117](https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/?node-id=2843-15117))

**Problems to solve:**
1. **User:** the biggest caregiver problems aren't covered by competitors.
2. **User:** families stitch together free tools instead of apps. We don't know why.
3. **Business:** our unique value is unclear now that the top problems changed.
4. **Business:** we don't know who pays: families, employers or Medicare.

**The 5 caregiver needs each competitor was scored on:**
1. Understand what's happening and what to do next
2. Real relief for the caregiver
3. The parent's money, papers and accounts
4. Works when the parent refuses help
5. Relatives share the work

**The 5 business questions:** how they make money; who pays and the cost; how they keep customers; customer experience; getting started.

**The 9 competitors and how they meet the 5 needs** (Y = yes, P = partly, N = no):

| Competitor | Type | 1. Understand | 2. Relief | 3. Money and accounts | 4. Parent refuses | 5. Relatives share |
|---|---|---|---|---|---|---|
| Caring Village | Direct (app, $14.99 to $24.99 a month) | P | P | P | N | P |
| Everplans | Direct (vault, $99.99 a year) | N | N | Y, if the parent filled it in | N | P |
| Cariloop | Direct (employer-paid coach; $249 a month to keep) | Y | P | Y | P | P |
| A Place for Mom | Direct (free; senior living pays referral fees) | P | P | P | N | N |
| Geriatric care managers | Direct ($150 to $300 an hour) | Y | Y, for a price | P | P | P |
| Group texts and notebooks | Indirect (free workaround) | P | N | P | P | P |
| Area Agencies on Aging | Indirect (free government program) | P | P | P | N | N |
| Respite and adult day services | Indirect (local care; mostly families pay) | P | Y, when families can get it | N | N | N |
| VA caregiver programs | Indirect (government; veterans with a 70%+ rating) | P | Y, if approved | P | N | P |

**Key weaknesses:**
- Caring Village can't get relatives to join.
- A Place for Mom causes nonstop sales calls.
- Care managers are expensive.
- Area Agencies give mostly referrals and long waits.
- Respite costs too much, has waitlists, and many parents refuse to go.
- The VA has strict rules to qualify.

**The 4 gaps** (the unique value opportunities):
1. **No one handles a parent who refuses help or gets relatives to share the work.** Every competitor gets Partly or No on needs 4 and 5.
   - **Opening:** help that works around a refusing parent and splits real tasks among relatives.
2. **Personal, ongoing guidance is locked behind an employer or a $150-an-hour bill.** Free help is limited:
   - Medicare GUIDE covers dementia only.
   - The VA covers veterans only.
   - Area Agencies mostly give referrals.
   - Only 12% would pay out of pocket, and willing payers cap near $70 a month.
   - **Opening:** coach-level guidance under $70 a month, or sold through employers (70% of working-age caregivers have jobs).
3. **Help with money and accounts works only if the parent prepared ahead.** There were 132 posts about getting into a parent's accounts.
   - **Opening:** getting caregivers into accounts after the parent can't set it up.
   - **Risk:** health data and consent.
4. **Relief exists, but caregivers can't reach it** (39% vs 13%).
   - **Opening:** help caregivers find, qualify for, pay for and actually use relief, including getting the parent to agree and relatives to cover.

**How the outcomes connect:** gap 4 is the approved market opportunity. Gap 1 holds two of the four blockers (the parent saying no, family who won't help). Gap 2 covers the paperwork blocker for the guidance side.

---

## 4. What the feature analysis needs to do (from the homework, read 2026-11-05)

- List the **features you choose**, mark each competitor ✅/🚫 per feature, add an **"Our company"** row, find what's unique, and double-check any AI work.
- **The teacher's format** (Figma example 5:823, template 5:3064):
  - Columns: COMPANY, WEBSITE, PRICING STRUCTURE, MARKET, MARKET SEGMENT / CHANNEL, CUSTOMERS OF THE SOFTWARE, then one column per feature.
  - Row 2 asks "Does the product offer ways to …?"
  - OUR COMPANY comes first.
  - Feature cells hold only ✅ or 🚫.
- **The OUR COMPANY row is the owner's to fill.** Claude doesn't choose our features.

## 5. Why the current feature analysis is out of date

**Current version:** Feature Analysis 3, Figma 2584:10359, repo `docs/feature-analysis-3.md`, built 2026-11-04.

**What's wrong with it:**
- **Old competitors:** Caring Village, CaringBridge, Lotsa, Everplans, MyChart, Lively, Medical Guardian, Medisafe, group texts, paper notebook. That's not the competitive analysis's 9.
- **Coordination features only:** shared calendar, one update for everyone, relatives' own access, medication reminders, documents, medical records, emergency alerts, caregiver support.
- **Missing the outcome's features:** nothing for finding or qualifying for relief, a parent who refuses help, relatives covering breaks, or getting into a parent's accounts after the fact.
- **Still useful:** the "how well each feature works" evidence table, and the finding that "relatives join" is offered by everyone but rarely works.

## 6. Exactly where to start the feature analysis

1. **Fill in `docs/research-checklist.md`** for the feature analysis, and show it before anything else. It has to:
   - list the inputs: this report's section 3, Feature Analysis 3, and the teacher's template
   - split by audience
   - name the questions
2. **Inputs table (used, or left out and why):**
   - the 9 competitors from the competitive analysis
   - the 4 gaps
   - the 5 needs
   - use case 1 scenarios for both audiences
   - the 4 blockers
   - the old feature list
3. **Propose a feature list for the owner to choose from.** Features come from the gaps, needs and scenarios. For example:
   - find and compare breaks
   - check eligibility and help with applications (Medicaid waivers, the VA, Area Agencies)
   - cost and payment help
   - help talking a refusing parent into help
   - relatives cover time off
   - support group finder
   - account access help
   - plus the coordination features still worth keeping

   **The owner chooses.**
4. **Mark ✅/🚫 per competitor from saved sources only.** Use the company pages in `docs/sources/competitors-4/` and the competitive analysis cells. If something is missing, research it, cite it and save it.
5. **Use INVEST stories,** show a markdown preview, then build a **new version** (Feature Analysis 4) on the clean page. Feature Analysis 3 is kept and gets a banner.
6. **Then:** unique value proposition and positioning, with one statement per audience. Then release vision.

---

## 7. Open items and parked work

- **Parked for deliverable #3 (release vision):**
  - MVP and MMP scoring (2598:11009)
  - Prioritize use cases (2378:7243)
  - Who-pays research (employers, Medicare GUIDE, families)
- **If "help applying for programs" becomes a feature:** read the posts about qualifying for **all** programs. Start from `docs/sources/competitive-analysis-3/va-check/research-checklist-va-2026-11-05.md`.
- **The owner's call:**
  - the duplicate audience section 2061:543 in FigJam Q5jRpN3MbONqFQF6KTS70j
  - keep or remove the Feature Analysis 3 gaps rewrite
  - the Week 2-3 NotebookLM slides (needs the owner's sign-in or a PDF)

## 8. Where things live

- **Clean page:** 2782:15415.
  - Market analysis sections: 2808:13693, 2812:14373, 2813:14661, 2815:15035.
  - Audience segmentation sections: 2834:2844, 2834:2867, 2834:16750.
  - Competitive analysis: 2843:15117.
- **Records of today's clean-page work:** `caregiving-coordinator/docs/clean-deliverables/` (inventories, reviews, the approved previews).
- **Research data:**
  - break research: `docs/sources/market-analysis-3/segments-11-12/`
  - audience research: `docs/sources/market-analysis-3/audience-v2/`
  - competitor pages: `docs/sources/competitors-4/`
  - competitive grid scripts: `docs/sources/competitive-analysis-3/grid/` (latest `build_grid_v5.py`)
- **Rules:** `caregiving-coordinator/CLAUDE.md`, plus the memory files.

## 9. Git

- Branch `feature-analysis`, PR LDoomD/AI-Development-Residency#23.
- All of today's work is committed and pushed. The latest commit before this report is dc280d2.
