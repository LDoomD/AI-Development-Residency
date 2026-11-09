# Market Analysis: Master Report (all 4 tables)

Written 2026-11-08. Built from the four data tables in `Data Tables_Market Analysis/` and the four reference reports in this folder. All four reports and all four tables were reviewed before this was written (section 10 lists what was reviewed and how). Tags: **Fact** = copied from a table or report. **Proposed** = my reading, not yet reviewed by the owner.

**How to use it:** a new session can start the next deliverable from this file. Sections 1 to 3 say what market analysis is and how the four tables fit. Section 4 gives every segment across all four tables. Sections 5 and 9 give the outcome. Sections 7 and 8 list what disagrees and what is missing.

---

## 1. Purpose of this report

- **Plain words:** one report that holds the result of the whole market analysis, so no one has to reopen four tables and four reports.
- **What market analysis is** (owner's description, 2026-11-08): studying a market to understand its dynamics, identify opportunities, and make informed decisions. It turns scattered facts into a clear read on the opportunity: what people want, what problems they have, and what they might buy.
- **What it should achieve when complete** (owner's description): a clear picture of the market landscape, validated customer needs, evidence that the opportunity is real, what problems are already solved and by whom, and the gaps worth pursuing.
- **How it connects to Discovery** (owner's description): Discovery is about learning the "current state" before planning solutions. Market analysis gives the landscape, segmentation tells you who is in it, competitive analysis shows who else is building for them, and feature analysis helps decide what to build.
- **What this report can answer:** which segments are open, crowded or closed, how big and how fast they are, how far to trust the numbers, and what the opportunity is.
- **What it cannot answer:** who pays for relief, how many caregivers have each need, whether the answer differs for adult children (Audience 1) and spouses (Audience 2), and a caregiver-only market size. Every dollar figure is for a wider market.

## 2. How the four tables fit together

| Table | Question it answers | Size | What it gave the next table |
|---|---|---|---|
| 1. Market Analysis Research | What segments exist, how big, how fast, who competes, how much money they raised. A numbers view (owner's description) | 16 rows, 13 columns | Core, Nearby, Indirect and Background labels, sizes, ratings, funding |
| 2. Possible Market Segments | Who is out there, which caregiver problem each solves, what sector. A words view (owner's description) | 15 rows, 6 columns | Numbered segments 1 to 15 and a problem for each. Burnout appears in only 2 |
| 3. Market Size | How big each market is today, how fast it grows, how reliable the number is (owner's description) | 16 rows, 9 columns | A size, growth rate and Low, Medium or High evidence rating |
| 4. Market Opportunity | Is it big enough, are there few competitors, is there an unmet need, and what is the verdict. The owner gave no description, so this comes from the headings | 14 rows, 6 columns | The verdict for each segment, with caregiver post counts. The final answer |

**The flow:** scan (table 1), map (table 2), size and rate (table 3), judge (table 4). Table 4 takes segment numbers from table 2, dollar ranges from tables 1 and 3, and competitor names and ratings from tables 1 to 3. It drops table 3's Evidence rating, the Census figures and the funding detail.

## 3. How it connects to the Discovery milestone

| What a finished market analysis should give you | Status | Where it comes from | What limits it |
|---|---|---|---|
| A clear picture of the market landscape | **Achieved** | Tables 1, 2, 3: 16 research rows, 15 mapped segments, 16 sized rows | Sizes are mostly global and not caregiver-only |
| Validated customer needs | **Partly** | Table 4: theme counts from 412 Reddit posts and 141 forum threads. Table 2 names a problem for each segment | Reddit and forums only (412 caregiver posts from a random Reddit sample, 141 forum threads). Four pairs of rows share one count. The respite counts use a separate targeted set. Problems are not ranked in table 2 |
| Evidence that the opportunity is real | **Partly** | Tables 3 and 4: sizes with evidence ratings, no consumer app for respite, burnout as the top theme | 1 of 16 sized rows is rated High and it is not about caregivers. Both Core rows are Medium. No one has said who pays |
| What problems are already being solved and by whom | **Achieved** | Tables 1 to 4: competitors, ratings, funding, "Few competitors?" | Example lists differ in length from table to table |
| Where the gaps worth pursuing are | **Achieved** | Table 4 rows 11 and 12, backed by tables 1 to 3 | For mental health the gap is support from people, so the shape of a product is still open |

## 4. Every segment across all four tables

Segment numbers 1 to 15 are table 2's. Row 16 is table 1's elder care row, which has no number in table 2. Sizes are "today → forecast (year), yearly growth." "Evidence" is table 3's rating. Post counts are from table 4 (of 412 Reddit posts, of 141 forum threads). Rows 11 and 12 are in bold.

| # | Segment | Link (table 1) | Size and growth | Evidence (table 3) | Who competes and what they have | Problem and sector (table 2) | Verdict and caregiver evidence (table 4) |
|---|---|---|---|---|---|---|---|
| 1 | Family care-coordination apps | Nearby | $1.71B (2025) → $7.5B (2035), 16% | Low: firms disagree widely | CaringBridge 19,469 Apple ratings; ianacare 57; Lotsa 52; Caring Village 36. Cozi 402,176 is the real substitute | Updates, siblings, long-distance coordination. Mixed: CaringBridge is a nonprofit | Need is real; apps don't solve it. 97 of 412 posts, 29 of 141 threads |
| 2 | Medication reminder apps | Nearby | $845M (2025) → $2,380M (2034), 12.2% | Medium: two firms roughly agree | Medisafe 101,546 ratings, raised $30M (2021) | Medications. For-profit | Crowded and small. 55 of 412, 20 of 141 |
| 3 | Pharmacy packaging and delivery | Indirect | $1.1B (2023) → about $2.0B (2034), 5.6% | Low: may count packaging products | Amazon bought PillPack for about $753M (2018). Capsule raised $300M (2021) | Medications, refills. For-profit | Not open. 55 of 412 (shared count) |
| 4 | Senior care referral and placement | Nearby | Not separately sized. Table 3 uses all senior care, $804.7B (2025) → $1,385.8B (2035), 5.59% | Low: measures all senior care | A Place for Mom. Its revenue is disputed: $50M vs $505M | Choosing and paying for care. For-profit: care providers pay referral fees | Large need, hard to enter. 90 of 412, 38 of 141 |
| 5 | Home care and marketplaces | Indirect | $8.7B (2025) → $18.7B (2033), 10.2% | Medium: two firms agree | Care.com Caregiver 163,758 ratings. Visiting Angels sales about $1B (2023). Papa valued at $1.4B (2021) | Hands-on care, respite. For-profit | Crowded. 50 of 412, 14 of 141 |
| 6 | Remote monitoring and medical alert | Indirect | $7.91B (2025) → $11.86B (2034), 4.6% | Medium: firms agree on growth, not size | Lively sold for $800M (2018). Philips bought Lifeline for $750M (2006) | Checking on a parent from far away, safety. For-profit | Crowded. 77 of 412, 32 of 141 |
| 7 | Employer and health-plan benefits | Nearby | $547.5M (2025) → $3,050M (2036), 16.9% | Low: only one firm | Cariloop raised $20M (2024); Wellthy $25.5M (2023). Ratings: 23 each | Navigation, coaching, time and stress. For-profit | Different customer (employers buy). No caregivers raised it. Closest theme: the caregiver's own job, money and health, 113 of 412 |
| 8 | Patient-side AI visit notes | Nearby | $1.67B (2025) → $9.67B (2035), 19.21% | Low: measures doctors' tools | Kin 1,120 ratings. Abridge raised $300M (2025, doctor side) | Remembering what the doctor said. For-profit | Open but unproven. No one asked for it. Doctors, appointments and records: 88 of 412, 27 of 141 |
| 9 | Patient portals with proxy access | Nearby | $6.43B (2025) → $18.13B (2033), 13.84% | Medium: five firms within about 1.6 times of each other | MyChart 736,347 ratings. Epic (MyChart) earns $5.7B a year (2024) | Appointments, results, records. For-profit: hospitals buy | Not open. 88 of 412 (shared count) |
| 10 | Digital vaults and emergency access | Nearby | Password managers $3.1B (2025) → $14.8B (2034), 18.5%. Digital legacy $25B (2025) → $54B (2031), 13.8% | Password managers High: three firms agree. Digital legacy Low: firms disagree widely | 1Password valued at $6.8B (2022). Keeper 231,964 ratings | Shared logins and documents. Mixed: AARP is a nonprofit | Clear need, hard to enter (bank rules and security risk). 117 of 412, 46 of 141 |
| **11** | **Respite care and adult day services** | **Core** | **$19.3B (2025) → $29.2B (2033), 5.3%. US only: $7.6B (2025)** | **Medium: one firm; others use different scopes** | **Many local providers. No consumer app category. Closest app: Care.com Caregiver, 163,758 ratings** | **Burnout, exhaustion. Mixed: about half the industry's revenue is nonprofit (2022), plus Medicaid, the VA and hospice** | **Help for worn-out caregivers exists, but many can't get it. Burnout: 210 of 412, 55 of 141. Of 341 respite posts: 128 got a break, 78 couldn't, 81 were still trying, 18 tried and stopped, 36 only mentioned or recommended it** |
| **12** | **Caregiver mental health and burnout** | **Core** | **$7.48B (2024) or $8.2B (2025) → $17.52B (2030) or $40.9B (2035), 14.6% or 17.4%** | **Medium: two firms, not caregiver-specific** | **Calm 1,991,711 ratings; Headspace 973,759. BetterHelp earns $950.4M a year (2025)** | **Burnout, guilt. Mixed: apps are for-profit; support groups often nonprofit** | **The need is large, but the big apps don't reach caregivers, who get support from therapists, support groups and other caregivers online. Burnout: 210 of 412** |
| 13 | Telehealth and virtual care | Indirect | $27.1B to $126.1B (2024 or 2025) → $119.4B to $403.2B (2033 or 2034), 11.5% to 17.39% | Low: three firms disagree widely | Teladoc 741,666 ratings, earns $2.53B a year (2025) | Getting a parent to appointments. For-profit | Not open. Caregivers didn't raise it |
| 14 | Insurance and benefits navigation | Nearby | $10.1B to $10.3B (2023) → $17.7B (2030) or about $21B (2032), 8.4% | Medium: two firms agree | Alight 303,650 ratings, earns $2.26B a year (2025) | Insurance, benefits and money. For-profit | Different customer (B2B). 117 of 412, 46 of 141 (shared count). 26% need help with paperwork (AARP/NAC p.52, as cited in the table) |
| 15 | General family organizers and shared calendars | Indirect | $1.2B (2025, family calendar apps for kids) → $2.3B (2034), 8.5% | Low: a nearby category | Cozi 402,176 ratings; TimeTree 93,227. No firm sizes it alone | Shared coordination, including care tasks. For-profit | No row in table 4. Its substitute (Cozi, group texts) is folded into row 1 |
| 16 | Elder care overall | Background | $804.7B (2025) → $1,385.8B (2035), 5.59% | Used as the stand-in for segment 4 (Low) | All senior care providers | Not in table 2 | Not in table 4 |

**Counts behind the table (recomputed from the CSVs):** table 1 links: Core 2, Nearby 8, Indirect 5, Background 1. Table 2 sectors: For-profit 11, Mixed 4, nonprofit-only 0. Table 3 evidence: Low 8, Medium 7, High 1 (16 rows, because segment 10 has two rows). Table 4 verdicts: Not open 3, Crowded 3, Different customer 2, hard to enter 2, and one each for "Need is real," "Open but unproven," respite, and mental health.

## 5. The most important things the market analysis shows (all **Proposed**)

1. **Two segments are Core to the caregiver problem:** respite and adult day services (11) and caregiver mental health (12). They are the only rows labeled Core in table 1 and the only rows where table 2 names burnout as the problem.
2. **Burnout is the top caregiver problem in the evidence:** 210 of 412 Reddit posts (51.0%) and 55 of 141 forum threads (39.0%). The next theme is money, accounts and legal papers at 117 (28.4%) and 46 (32.6%).
3. **Respite is the open opportunity.** The market is large ($19.3B global, $7.6B US only), many local providers serve it, no consumer app category exists, and many caregivers cannot get a break: of 341 posts about respite, 78 couldn't get one and 81 were still trying. The named blocks are cost, a parent who says no, paperwork, and family who won't help.
4. **In mental health the big apps don't reach caregivers.** Calm and Headspace have 1,991,711 and 973,759 ratings, but caregivers almost never use burnout or meditation apps. They rely on people: therapists, support groups and other caregivers online.
5. **Every other segment is closed, hard to enter, a different buyer, or unproven.** Not open: 3, 9, 13. Crowded: 2, 5, 6. Different customer: 7, 14. Hard to enter: 4, 10. Open but unproven: 8. Real need but apps don't solve it: 1.
6. **Products built for caregivers are tiny, and the big money is elsewhere.** CaringBridge has 19,469 Apple ratings; ianacare 57, Caring Village 36, Cariloop 23, Wellthy 23. Caregiver companies raised $8.2M to $25.5M. Capsule and Abridge raised $300M each.
7. **The sizes are soft.** Only 1 of 16 sized rows is rated High (password managers, not caregiver-specific). The two markets built for caregivers are both Low. Both Core rows are Medium. No size is caregiver-only.
8. **Who pays for relief is not answered.** Segments 4, 7, 9 and 14 are sold to someone other than the family, and the two Core rows do not say who would pay.

## 6. Patterns and tensions across all four tables (all **Proposed**)

**Growth versus evidence (stated growth; evidence from table 3)**

| Growth | Segments | Evidence |
|---|---|---|
| Fastest: 16% to 19.21% | AI visit notes 19.21% (Low), password managers 18.5% (High), employer benefits 16.9% (Low), caregiver apps 16% (Low) | Mostly Low |
| Fast: 11.5% to 17.4% | Mental health 14.6% to 17.4% (Medium), telehealth 11.5% to 17.39% (Low), patient portals 13.84% (Medium), digital legacy 13.8% (Low), medication apps 12.2% (Medium) | Mixed |
| Middle and slow: 4.6% to 10.2% | Home care 10.2%, family organizers 8.5%, insurance navigation 8.4%, pharmacy 5.6%, elder care 5.59%, respite 5.3%, remote monitoring 4.6% | Mixed. Respite (Medium) is among the slowest |

**Where the evidence is strong and weak (table 3 ratings by table 1 link)**

| Link | Rows | High | Medium | Low |
|---|---|---|---|---|
| Core | respite, mental health | 0 | 2 | 0 |
| Nearby | caregiver apps, employer, medication, elder care (stand-in), AI notes, portals, password managers, digital legacy, insurance navigation | 1 | 3 | 5 |
| Indirect | pharmacy, home care, remote monitoring, family calendar, telehealth | 0 | 2 | 3 |

**Why the 8 Low ratings are Low:** firms disagree widely (caregiver apps, digital legacy, telehealth), only one firm (employer benefits), or the number measures something else (pharmacy packaging, all senior care, doctors' AI tools, kids' calendar apps).

**What caregivers say (table 4; posts can fall under more than one theme)**

| Theme (segments that use it) | Reddit (of 412) | Forums (of 141) |
|---|---|---|
| Burnout and exhaustion (11, 12) | 210 (51.0%) | 55 (39.0%) |
| Money, accounts and legal papers (10, 14) | 117 (28.4%) | 46 (32.6%) |
| The caregiver's own job, money and health (7) | 113 (27.4%) | not given |
| Family coordination (1) | 97 (23.5%) | 29 (20.6%) |
| Choosing, placing and paying for care (4) | 90 (21.8%) | 38 (27.0%) |
| Doctors, appointments and records (8, 9) | 88 (21.4%) | 27 (19.1%) |
| Safety (6) | 77 (18.7%) | 32 (22.7%) |
| Medicines (2, 3) | 55 (13.3%) | 20 (14.2%) |
| Paid caregivers and agencies (5) | 50 (12.1%) | 14 (9.9%) |
| Employer benefits, telehealth | none raised | not given |

**Other patterns**
- **Most segments solve information and logistics problems** (10 of 15 in table 2). Burnout is named in only 2.
- **The market is mostly for-profit:** 11 of 15 segments. The 4 Mixed ones are 1, 10, 11 and 12. The biggest nonprofit and government role is in 11 and 12.
- **Buyer is not the user** in segments 4 (care providers pay referral fees), 7 (employers), 9 (hospitals) and 14 (employers and plans).
- **Traction does not predict money:** Medisafe has 101,546 ratings and raised $30M. Capsule has 6,010 ratings and raised $300M.
- **A few research firms shape several rows:** Grand View Research supplies 5 of 16 research rows, Global Market Insights 3 and MarketIntelo 2 (table 1).
- **Shared theme counts:** one count serves two segments for medicines (2, 3), doctors and records (8, 9), money and legal papers (10, 14) and burnout (11, 12). A segment in those pairs has no evidence of its own.

**Tensions**

| Tension | What the tables show |
|---|---|
| Biggest need, no product | Burnout is the top theme, yet respite has no consumer app and the mental health apps don't reach caregivers |
| Real need, but not an app | Caregivers get burnout support from people. A product may need to connect people, not replace them |
| Strong evidence is far from caregivers | The one High row is password managers, which table 4 calls "hard to enter" |
| Caregiver-built markets are the weakest | Both are Low in table 3 |
| Core sizes are stand-ins | Adult day care for respite, all mental health apps for mental health |
| Fast growth is not caregiver growth | AI notes, vaults and portals are not measured for caregivers |
| Big market, slow growth | Respite is $19.3B but grows 5.3% global and 1.5% in the US only |
| Wrong buyer | Segments 4, 7, 9 and 14 have a need but the family does not pay |

## 7. Where the tables and reports disagree or need fixing

These are the conflicts found when all four tables and reports were checked against each other. Items 1 to 9 are in the owner's tables. Item 10 is a wording error in one of my reports. Item 11 is a note about two different samples. Items 1, 3, 4, 5 and 11 were then checked against the project's saved research in `docs/` and are marked in the Status column. On 2026-11-08, eight cells in tables 1, 3 and 4 were changed at the owner's request (items 1, 3, 4, 5 and 9, the Kin claims in table 4 row 8, and the patient portal notes in tables 1 and 3, and the portal Evidence label in table 3), and the reference reports were updated to match (the Status column says which).

| # | Item | Where | Detail | Status |
|---|---|---|---|---|
| 1 | Firm count differs | Table 3 row 1 vs table 1 row 1 | "(5 firms)" vs "(4 firms)" for the other caregiver app estimates | **Resolved and fixed in table 3** (now "4 firms"). Both counts were right. The saved research lists five publishers: Verified Market Research, Wise Guy, Market Research Intellect, Data Horizzon, Business Research Insights. Wise Guy is the headline number, so "other estimates" come from 4. Table 3's "5" counts all five. The change was wording only. Source: `docs/market-research-prompt2-results.md` (publisher table) and `docs/market-size-table.md` row 1 |
| 2 | Digital legacy headline is the top of its range | Table 3 row 11 | Shows $25B as today's size; the note and table 1 say firms range from $1.1B to $25B | Open. **Confirmed:** Kenresearch's saved page states $25B in 2025, 13.8% growth to $54B by 2031. Showing the top of the range may be the owner's choice |
| 3 | Two dollar figures not in tables 1 to 3 | Table 4 row 3 ($0.8B) and row 9 ($3.9B) | The tables show $1.1B (2023) and $1.12B to $1.78B for pharmacy packaging, and $5.2B to $6.6B and $6.43B for portals | **Resolved and fixed in table 4 row 9.** **$0.8B is confirmed:** Global Industry Analysts' report states $844.2M in 2023 (Yahoo Finance press release). The link in the saved research points to a different report ($1.13B in 2024), so that link is wrong, not the figure. **$3.9B was not confirmed:** Market Research Future's page now states $7.02B for 2025. Row 9 now says $4.4B to $7.0B, the range on the pages checked (Grand View $4.4B, SNS $4.79B, Data Bridge $6.43B, Market Research Future $7.02B). Four of the five portal firms are between $5.2B and $6.6B. Table 1's notes left both out. The tables were not changed. Source: `docs/market-research-prompt2-results.md` |
| 4 | Biggest forum worry | Table 4 row 4 vs row 11 | Row 4 calls choosing care "the biggest worry in the forums" (38 of 141). Row 11 gives burnout as 55 of 141 | **Resolved and fixed in table 4 row 4** (now says burnout is bigger on both). The saved forum read: burnout is in 55 of 141 threads (39%) and the main topic of 25 (17%). Choosing care is in 38 (26%) and the main topic of 12 (9%). The "biggest worry" line looks like it came from an older summary where the two were tied (my reading). Source: `docs/community-voice-findings.md` theme table |
| 5 | Respite counts do not add up | Table 4 row 11 | 128 + 78 + 81 = 287, but the row says 341 posts | **Resolved and fixed in table 4 row 11** (now lists all six groups). 341 = 128 used + 78 wanted but couldn't get + 81 looking or considering + 18 tried and stopped + 32 mentioned only + 4 recommends to others. Table 4 showed three of the six groups. Source: `docs/sources/market-analysis-3/segments-11-12/results.json` and `docs/market-analysis-segments-11-12-findings.md` section 2 |
| 6 | "Medium" means two things | Table 3 vs table 4 | A size in table 4, a trust level in table 3 | Open. Wording only |
| 7 | Table 4 drops the evidence ratings | Table 4 | A reader of table 4 cannot see that row 1's $1.3B to $4B is Low and row 11's $19.3B is Medium | Open. May be a choice to keep the table short |
| 8 | Elder care and segment 15 are handled differently | Tables 1 to 4 | Table 1 has elder care as a Background row. Table 3 uses it as the stand-in for segment 4. Tables 2 and 4 have no elder care row. Segment 15 has no row in table 4 | Open. May be a choice about scope |
| 9 | "More than 100 times" understates a gap | Table 3 row 5 | $1,916B / $1.2B is about 1,600 times (recomputed) | **Fixed in table 3 row 5** (now "about 1,600 times"; Mordor $1.20B and Prophecy $1,916.3B confirmed on 2026-11-08) |
| 10 | US-only size row is worded wrongly | My report on table 3, gaps table | It lists row 5 as having a US figure (it has none) and says row 6 has "only franchise sales" (its notes also give $166.7B for all US home care providers) | **Fixed in report 3** on 2026-11-08 |
| 11 | Table 4 row 11 mixes two samples | Table 4 row 11 | "210 of 412 Reddit posts" comes from a random sample of 500 Reddit posts, of which 412 were caregiver posts. The 341 respite posts come from a separate targeted set: 831 relief posts, from 1,086 items read. They are not inside the 412 | **Noted.** Not an error, but the two numbers have different bases. Source: `docs/market-analysis-3.md`, `docs/market-analysis-segments-11-12-findings.md`, `docs/competitive-analysis-3.md` |

**Also checked and agreeing:** segment names and numbers across tables 1 to 4 (12 of 15 names exact, 3 shortened in table 2); Core labels (table 1 respite and mental health = table 2 segments 11 and 12 = table 4 rows 11 and 12); the "about half nonprofit" claim for respite (47%, recomputed from $36.5B of $77.3B); competitor ratings that appear in more than one table; every dollar range in tables 3 and 4 (rounded figures count as matches; the two that did not match are item 3, now traced).

**Growth rates that differ from their own size and forecast (recomputed):** general family organizers 8.5% stated, 7.5% recomputed; mental health (Grand View) 14.6% vs 15.2%; digital vaults 18.5% vs 19.0%; telehealth (IMARC) 17.39% vs 17.9%. 15 of 19 land within 0.3 points. The firms' own pages state these rates (Market Intelo 8.5% and 18.5%, Grand View 14.6%, Global Market Insights 17.4%, IMARC 17.39%; saved pages checked 2026-11-08), so the gaps are the firms' own rounding or start years, not errors in the tables.

## 8. What is missing or worth validating (all **Proposed**)

| Gap | Where it shows | Why it matters |
|---|---|---|
| No caregiver-only market size for any segment | Tables 1, 3, 4 | The opportunity rests on stand-in numbers |
| Who pays for relief | Tables 1 to 4 | Segments 4, 7, 9 and 14 sell to others. The Core rows are silent |
| Why 412 posts and 141 threads | Table 4 | **How they were chosen is now known:** 412 caregiver posts from a random sample of 500 Reddit posts (seed 20261104), and 141 forum threads (AgingCare 40, ALZConnected 101). Source: `docs/market-analysis-3.md`, `docs/community-voice-findings.md`. Still open: an earlier Reddit pass is recorded in memory as 825 posts, not reconciled here |
| No split by audience | Tables 2 and 4 | Audience 1 (adult child) and Audience 2 (spouse or partner) are not separated |
| Problems are not ranked in table 2, and counts are shared across segment pairs | Tables 2 and 4 | Four segment pairs have no evidence of their own |
| Evidence ratings have no stated cutoffs | Table 3 | "Medium" and "High" are not tied to a number of firms |
| Funding not found for several names | Table 1 | Caring Village, Lotsa Helping Hands, Cozi, FamilyWall, MyTherapy, Round Health, A Place for Mom, Caring.com, adult day providers |
| App store usage not checked for two segments | Table 1 | Senior care referral and elder care overall |
| Sources that are not the firm's own page | Table 3 | Home care via gii.tw (a report reseller), pharmacy packaging via a press release, four with no web address |
| Outside sources behind table 4 | Table 4 | **Confirmed 2026-11-08:** AARP/NAC report p.52 (26% need help with paperwork or eligibility) and IBISWorld (US $7.6bn, 2025). **Removed from table 4 row 8** (no source): Kin is "free" and "43 of 46 reviews five-star." Row 8 now uses Kin's ratings and $9M seed (table 1) and four newer apps named in the saved research |
| Portal market sizes have moved | Tables 1, 3 and 4 | **Fixed.** Tables 1, 3 and 4 now all say $4.4B to $7.0B (live pages: Grand View $4.4B, SNS $4.79B, Data Bridge $6.43B, Reports and Data $6.48B, Market Research Future $7.02B). Growth range is now 10.9% to 19.55% (SNS) |
| Sources behind table 2's examples | Table 2 | **Partly resolved.** The saved research counts the programs (Medicaid and waivers 77 posts, hospice 45, the VA 44, Area Agencies on Aging 26) and explains ARCH (a national directory of respite providers), Medicare GUIDE (up to $2,500 a year for respite for people with dementia) and Papa ($30 an hour). Table 2 itself does not say. Source: `docs/market-analysis-3.md` |
| Census figures too broad for 7 rows | Table 1 | No US revenue check for the software rows |
| Dates | Tables 1, 3 | Base years 2023 to 2025. Funding looked up 2026-11-02 |
| Original research reports not opened | All | The sources are as the owner's tables state them |

## 9. Where the market analysis points (**Proposed**)

**The outcome.** The market analysis points to **helping worn-out caregivers reach relief**: respite and adult day services (segment 11) and caregiver mental health (segment 12). These are the Core segments in table 1, the burnout segments in table 2, Medium-rated markets in table 3, and the open needs in table 4. Burnout is the top caregiver problem in the evidence. Respite is a large market with no consumer app, and many caregivers cannot get a break. In mental health the big apps don't reach caregivers, who rely on people.

**What was achieved.** The landscape, who already serves caregivers, and the gaps are covered. Validated needs and proof that the opportunity is real are only partly covered (section 3).

**How it relates to the approved work.** This is the opportunity the owner already approved on 2026-11-05: helping worn-out caregivers reach relief, segments 11 and 12 (`dogfood-2026-11-07-handoff-feature-comparison-analysis.md`, section 1). The four tables are the evidence trail behind that choice.

**What it handed on.** The help caregivers name for these two segments (Medicaid and waiver programs, therapists, support groups, online caregiver groups) led to the 7 competitor rows added to the competitive analysis on 2026-11-07 (same handoff report, section 5). The next deliverable is the feature comparison analysis.

**What it does not settle.** Who pays, how many caregivers have the need, whether the answer differs for Audience 1 and Audience 2, and a caregiver-only market size.

## 10. Verification receipt

**What was reviewed (all on 2026-11-08)**

| File | Lines | How it was reviewed |
|---|---|---|
| `Reference Reports_Market Analysis/Market Analysis Research - Reference Report - 1 of 4.md` | 427 | Read: sections 1 to 3 and 5 to 9 in full, row blocks by script and by reading every "In plain words" line |
| `Reference Reports_Market Analysis/Possible Market Segments - Reference Report - 2 of 4.md` | 311 | Read in full |
| `Reference Reports_Market Analysis/Market Size - Reference Report - 3 of 4.md` | 448 | Read: sections 1 to 3 and 5 to 10 in full, row blocks by script and by reading every "In plain words" line |
| `Reference Reports_Market Analysis/Market Opportunity - Reference Report - 4 of 4.md` | 371 | Read: sections 1 to 3 and 5 to 9 in full, row blocks by script and by reading every "In plain words" line |
| `Data Tables_Market Analysis/Market Analysis Research.csv` | 16 rows, 13 columns | Read in full; every cell matched to report 1 |
| `Data Tables_Market Analysis/Possible Market Segments.csv` | 15 rows, 6 columns | Read in full; every cell matched to report 2 |
| `Data Tables_Market Analysis/Market Size.csv` | 16 rows, 9 columns | Read in full; every cell matched to report 3 |
| `Data Tables_Market Analysis/Market Opportunity.csv` | 14 rows, 6 columns | Read in full; every cell matched to report 4 |
| The owner's context on what market analysis is (refresher, and the intros for tables 1 to 3) | n/a | Used in sections 1 to 3. Table 4 had no owner description |
| Saved research in `docs/`: `market-research-prompt2-results.md`, `market-size-table.md`, `community-voice-findings.md`, `market-analysis-3.md`, `market-analysis-segments-11-12-findings.md`, `competitive-analysis-3.md`, and `sources/market-analysis-3/segments-11-12/results.json` | n/a | Searched and read for the lines cited in section 7. Respite status counts were read from `results.json` |

**Checks run**
- **Pass 1, read:** all four reports and all four tables were read. A script matched every table cell to its report: 208 of 208, 90 of 90, 144 of 144, 84 of 84, none missing.
- **Pass 2, recomputed:** counts of links (2, 8, 5, 1), sectors (11, 4, 0), evidence (8, 7, 1) and verdicts; the percentages of 412 and 141; the 341 respite counts (287 as first written, 341 after the 2026-11-08 edit); the 47% nonprofit share; the 1,600 times gap; and the growth rates. They match what the reports state, except for the one wording error in section 7 item 10.
- **Pass 3, master against sources:** a script extracted every dollar figure, percentage and large number in this report and looked each up in the four tables and four reports. Result after the saved-research update: 132 distinct numbers checked against the four tables, four reports and the saved research files, 0 not found; all 7 `docs/` paths cited exist. The first run found one (a "12%" range label I had written); it was changed to "11.5%" and the check rerun. I also re-read the segment table, evidence counts and growth groups against the reports by hand, and a script confirmed every markdown table has consistent columns.
- **Pass 4, saved research:** conflicts 1, 3, 4 and 5 were looked up in the project's saved research. The `results.json` respite counts sum to 341 (128 + 78 + 81 + 32 + 18 + 4). The tables and reports were not edited.
- **Pass 6, original pages:** the figures for the five caregiver app publishers were confirmed (saved copies for Verified Market Research and Wise Guy; live pages for Market Research Intellect, Data Horizzon and Business Research Insights). The respite counts and forum counts were recounted from the saved codes (see conflicts 4 and 5). Also confirmed: adherence packaging $844.2M (Global Industry Analysts press release), IBISWorld $7.6bn, Kenresearch $25B, AARP/NAC p.52 (26%), and the firms' stated growth rates. The $3.9B portal figure was not confirmed and the unsourced Kin claims were removed from table 4 (item 3, section 8).
- **Pass 5, updates:** the owner's three cells were edited in `Market Size.csv` and `Market Opportunity.csv` (3 lines changed, checked against a backup). Reports 2, 3 and 4 were updated to match, and the cell-by-cell matches were re-run on all four reports. The report 3 wording error was fixed.
- **Conflicts:** nine in the owner's tables (items 1, 4 and 5 now fixed), one in my report 3 (now fixed) and one note on two samples (section 7).

**Not checked**
- The underlying posts and threads. Counts were read from the saved results files, not recounted.
- The research firms' own pages, except those listed under Pass 6. The four newer visit-notes apps against the app stores.
- The CSVs against the PNG versions of the tables.
- The approved-opportunity and 7-competitor statements in section 9 against Figma. They rest on the 2026-11-07 handoff report.
- Sections 5, 6, 8 and 9 and the "Proposed" notes are my reading, not reviewed by the owner.
