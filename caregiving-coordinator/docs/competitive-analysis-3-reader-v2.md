# Competitive Analysis 3: reader version 2 (2026-11-04)

> **SUPERSEDED 2026-11-05 by `docs/competitive-analysis-3-reader-v3.md`** (four VA cells fixed). Kept for history.

Version 2 adds two competitors for the #1 caregiver problem (exhaustion), rewords gap 2 and adds gap 4 (approved by the owner 2026-11-04). Version 1 is kept: `docs/competitive-analysis-3-reader.md`. Checklist: `docs/research-checklist-ca3-exhaustion.md`. Corrected 2026-11-05 after audits (`docs/reports/update-inventory-2026-11-05.md`, `docs/reports/audit-2026-11-05-results.md`): grid version 4 and business table version 3 (`build_grid_v4.py`), respite and VA cells fixed, gap 2 reworded with Medicare GUIDE, gap 4 narrowed: "70% of working-age caregivers," and the unconfirmed "strongest unmet need" ranking removed (it was Claude's reading, not the owner's decision).

The same approved content as `docs/competitive-analysis-3.md`, put in the teacher's template order with clear titles. The working file keeps the full build history (first versions, replaced steps). Figma: section "UPDATED 2026-11-04: COMPETITIVE ANALYSIS 3".

## 1. The problems this analysis should help us solve

*What we need to learn from competitors, for caregivers and for our business.*

1. **User:** caregivers' biggest problems (burnout, dementia behavior, the parent refusing help, choosing a place) aren't covered by the competitors we studied.
   *Source: `docs/market-analysis-3.md` (top problems), `docs/audience-teacher-format-2026-11-04.md` (Audience 1 use cases: exhaustion 138, dementia behavior 82, the parent refuses help 60, choosing a place 46), `docs/competitive-analysis-2.md`.*
2. **User:** families stitch together free tools (group chats, notebooks, alert buttons) instead of using the coordination apps. We don't know why.
   *Source: competitive analysis board, "What families use instead" (Figma 2508:9836).*
3. **Business:** we're not sure what our unique value is, now that the top problems changed.
   *Source: `docs/market-analysis-3.md`.*
4. **Business:** we don't know who pays for help in this space: families, employers or Medicare.
   *Source: `docs/exhaustion-dementia-research.md`. Audience page socioeconomic box (Figma 2378:7195): only 12% would pay out of pocket (CAN 2026), and willing payers cap near $70 a month (Schulz 2016).*

> Written from the market analysis (3rd version), the audience page (Audience 1 use cases), Competitive Analysis 2, the board's "what families use instead" table and the audience socioeconomic box. Approved 2026-11-04 (option C).

## 2. What we asked about every competitor

*The 7 biggest caregiver problems from our research, narrowed to 5 caregiver needs, plus 5 business questions.*

### 2a. The 7 biggest caregiver problems, from our research

| Problem | Audience 1 (seen in) | Audience 2 (seen in) | Market analysis (Reddit / forums) | Covered by the 10 competitors in Competitive Analysis 2? |
|---|---|---|---|---|
| 1. Exhaustion, doing it alone | 138 | 45 | 51% / 43% (top) | No |
| 2. Dementia behavior, hard talks | 82 | 24 | 24% / 34% | No |
| 3. Money, legal papers, the parent's accounts | 74 (+132 accounts posts in the targeted search) | 13 | 28% / 33% | Partly (Everplans, MyChart) |
| 4. Medicines and hands-on care | 62 | 24 | 13% / 16% (+17 hands-on posts) | Medicines only (Medisafe, Caring Village) |
| 5. The parent refuses help | 60 | 9 | 20% / 10% (new) | No |
| 6. Relatives don't help | 48 | 12 | 24% / 24% | Yes (Caring Village, CaringBridge, Lotsa, group texts) |
| 7. Choosing and paying for a place | 46 | 9 | 22% / 30% | No |

- **Problems 8 and 9 (safety at home 37, answers from doctors 30):** stay covered by the competitors already studied (Lively, Medical Guardian, MyChart). No new research.
- **Problem 10 (being far away, 20):** too small to drive the analysis.
- **Audience 2's aides, hospice and trusting helpers (14):** waits until the Audience 2 work.

> Audience 1 and 2 counts come from 412 caregiver posts and threads read in full (303 Reddit, 109 forum), with 777 moments coded (`docs/sources/market-analysis-3/audience-v2/`). The Reddit and forum shares come from the market analysis, 3rd version (a random sample of 412 Reddit posts, and 117 forum threads). A problem made the list if it was seen in 46 or more Audience 1 posts and threads, and in at least 1 in 5 Reddit posts or forum threads. Approved 2026-11-04 (option A).

### 2b. The 5 caregiver needs we scored each competitor on (narrowed from the 7 problems)

| # | Criterion | Audience data (Figma 2623:76, segmentation boxes) | Market analysis (Figma 2598:10950) |
|---|---|---|---|
| 1 | Does it help the caregiver understand what's happening, handle hard behavior, and know what to do next? | #1 situational goal (73). Use case #2, dementia behavior (82). 55% do medical tasks, only 22% were trained (AARP p.34). | Dementia behavior 24% / 34%. No market segment serves it. |
| 2 | Does it give the caregiver real relief: time, breaks, their own health? | Use case #1, exhaustion (138). #1 life goal, health and sanity (73). 34% have no other help (AARP p.25). | Burnout 51% / 43%, top everywhere. Segment 12: burnout apps are crowded, but caregivers rarely use them. Owner's scoring: Valuable High. |
| 3 | Does it get the parent's money, papers and accounts under control? | Use case #3 (74). Situational goal #3 (49). | 28% / 33%; 132 targeted accounts posts. Segment 10: strong evidence of an unmet need. Owner's scoring: Valuable High. |
| 4 | Does it still work when the parent refuses help, and respect the parent's choices? | Use case #5 (60). Motivation: let the parent stay home and choose (24). | 20% / 10% (new from Reddit). No market segment serves it. |
| 5 | Does it get relatives to actually share the work? | Use case #6 (48). 34% have no other help. | Family coordination 24% / 24%. Families use group chats, not apps (99 posts). Owner's scoring: Medium. |

> Fleety (Tech Fleet) advised about 5 criteria taken from the audience's top needs, and the teacher's template has 5 question columns. Each need comes from Audience 1's top use cases and goals, checked against the audience section (Figma 2623:76), the segmentation boxes and the updated market analysis (Figma 2598:10950). Medicines and hands-on care, and choosing a place, were considered and not chosen (owner's choice). Approved 2026-11-04. It replaced a first version with 8 questions.

### 2c. The 5 business questions

1. How do they make money?
2. Who pays, and what does it cost?
3. How do they keep customers?
4. How do they approach customer experience?
5. What does it take to get started?

> These come from the board's "Questions to answer about the competitors" section (Figma 4:533). They were left out of the first grid and brought back on 2026-11-04 when the owner asked for the business questions.

## 3. The 9 competitors we compared, and why

*5 direct and 2 indirect, picked from the market analysis segments, with who was left out and why.*

| # | Competitor | Type | Market analysis segment | Criteria it touches | Caregiver evidence |
|---|---|---|---|---|---|
| 1 | Caring Village | Direct (business) | 1 Family care-coordination apps | 5, 3 | 29 caregiver reviews |
| 2 | Everplans | Direct (business) | 10 Digital vaults and emergency access | 3 | Thin: 1 caregiving review |
| 3 | Cariloop | Direct (business, employer-paid) | 7 Employer caregiver benefits | 2, 3 | 0 posts; company pages and price saved |
| 4 | A Place for Mom | Direct (business) | 4 Senior care referral (owner's scoring: Valuable High) | 2 | 21 caregiver posts |
| 5 | Geriatric care managers | Direct (private professionals) | No segment; fills the gap for criteria 1 and 4 | 1, 4, 2 | 31 caregiver posts |
| 6 | Group texts and notebooks | Indirect (workaround) | What families use instead | 5 | Named in about 100 posts each |
| 7 | Area Agencies on Aging | Indirect (government program) | What families use instead | 2, 3 | 47 caregiver posts, 29 describe using it |
| 8 | Respite and adult day services (added in version 2) | Indirect (local care services) | 11 Respite care and adult day services | 2 | 434 caregiver posts about respite or adult day |
| 9 | VA caregiver programs (added in version 2) | Indirect (government program) | 11 (VA benefits for veterans' families) | 2, 3, 5 | 43 caregiver posts |

**Left out, with reasons:**
- CaringBridge, Lotsa: same segment and criterion as Caring Village.
- Caring.com: same segment as A Place for Mom, 2 mentions.
- Trustworthy, Cake, AARP Digital Vault, 1Password, Keeper: 0 caregiver mentions.
- Calm, Talkspace, Sanvello, BetterHelp, ianacare: 0 to 5 mentions, general apps.
- Wellthy, Carallel: 0 to 2 mentions.
- Medication apps, pharmacies, home care: medicines isn't a criterion.
- Alert devices, visit notes, MyChart, Chapter: their problems aren't in the top 7.
- Trualta, Medicare GUIDE, the Alzheimer's helpline: almost no caregiver evidence.

**Trade-off (the owner kept the list as is):** burnout and meditation apps (segment 12) stay out because caregivers rarely use them. Respite and adult day services and VA caregiver programs were added on 2026-11-04 to cover exhaustion, the biggest need.

> The candidates are every company the market analysis names in a segment that touches the 5 needs (`docs/competitive-analysis-3-inputs.md`), plus what families use instead. Caregiver mentions were counted in 49,315 saved Reddit posts (`docs/sources/competitive-analysis-3/count_segment_candidates.py`). The owner chose the final 7 on 2026-11-04. It replaced a first version with 15 competitors.

## 4. How the 9 competitors compare

*Four tables: who they are, how they make money, what they do well and badly, and how well they meet the 5 caregiver needs.*

### 4a. Who they are and what they offer

| Competitor | Type | Market segment | Website | Main features | How they stand out |
|---|---|---|---|---|---|
| **Caring Village** | Direct (business) | 1 Family care-coordination apps | caringvillage.com | A shared family app with a calendar, to-dos, medication lists, documents and an AI helper. | Built by former caregivers as one place for the whole family's care. |
| **Everplans** | Direct (business) | 10 Digital vaults and emergency access | everplans.com | Online vault for documents, accounts and wishes, shared with chosen family. | Walks a person through organizing all their life details and next steps. |
| **Cariloop** | Direct (business, employer-paid) | 7 Employer and health-plan caregiver benefits | cariloop.com | A personal care coach, a care-booking marketplace, a family Care Team and document storage. | Full-time coaches who take no money from the care providers they suggest. |
| **A Place for Mom** | Direct (business) | 4 Senior care referral and placement | aplaceformom.com | A free advisor, a care and cost check, local places with prices, and tours. | Says it has the country's largest senior care network. |
| **Geriatric care managers** | Direct (private professionals) | None of the 14 segments (private care management) | aginglifecare.org (to find one) | Home visits, care plans, hiring and checking aides, appointments, and help for families far away. | Trained local professionals who see the parent and the home in person. |
| **Group texts and notebooks** | Indirect (workaround) | What families use instead (not a company) | n/a | Family group chats, notebooks, binders and whiteboards. | Everyone already has them, they're free, and there's nothing to install. |
| **Area Agencies on Aging** | Indirect (government program) | None of the 14 segments (free public service) | eldercare.acl.gov (finds your local agency) | Caregiver information, help finding services, counseling, support groups, training and respite. | Local, government-funded and free to families who qualify. |
| **Respite and adult day services** | Indirect (local care services) | 11 Respite care and adult day services | archrespite.org (to find one) | In-home sitters, short facility stays, hospice respite, and adult day centers with activities, meals and rides. | Staff take over the care for hours or days, so the caregiver can rest and run errands. |
| **VA caregiver programs** | Indirect (government program) | 11 Respite care and adult day services (VA benefits for veterans' families) | caregiver.va.gov | Respite of at least 30 days a year, a monthly stipend, counseling, training, legal and financial planning, and a support line. The stipend, planning help and 30 days of respite require the veteran to have a 70% or higher disability rating. | Pays family caregivers directly and lets the veteran name up to 2 backup caregivers. |

> Company websites saved on 2026-11-04 (`docs/sources/competitors-4/`, saved by a script that respects robots.txt; blocked pages were read in the built-in browser and saved in `manual-saves/`), plus Competitive Analysis 2. Every cell is checked against its saved source (`build_grid_v2.py`).

### 4b. How they make money and keep customers

| Competitor | How do they make money? | Who pays, and the cost | How do they keep customers? | How do they approach customer experience? | What does it take to get started? |
|---|---|---|---|---|---|
| **Caring Village** | Monthly subscriptions, a free plan with ads, sales to businesses and gift subscriptions. | The caregiver pays: free for 2 people, or $14.99 to $24.99 a month. | The free plan caps at 2 members, pushing families to pay. Daily to-dos and reminders bring people back. Use ends when the parent dies. | Self-serve: help center, email, guided setup and an AI assistant. No phone support. | Sign up with email, Apple or Google in minutes, then invite relatives. Works on iPhone, Android and the web. |
| **Everplans** | Yearly subscriptions, plus deals through financial advisors and partners. | The parent pays: free for 3 items, or $99.99 a year. | The free plan stops at 3 items. Date reminders bring people back. | Self-serve: FAQs, a contact form, articles and checklists. | The parent fills in their own plan on the web or the app. |
| **Cariloop** | Employer contracts, priced per employee per month or in blocks of cases. | The employer pays. At MSU, keeping the coach yourself costs $249 a month. | Employer contracts. Members who leave the job get 30 days to switch to a paid individual plan. | Full-time care coaches who answer in under 2 hours on average. | An employer benefit first, then the web or mobile app. |
| **A Place for Mom** | Referral fees: senior living places pay when a family moves in, and home care agencies pay per referral. | Senior living places pay it when a family moves in. Free to families. | Families are leads, not paying customers. Signing up allows calls and texts from its paying communities. | A free local advisor, a care quiz and a cost calculator. | Take a care quiz or contact a local advisor. Sales calls from communities follow. |
| **Geriatric care managers** | Hourly fees of $150 to $300, a one-time first assessment, and sometimes travel time. | The family pays $150 to $300 an hour. Medicare and Medicaid usually don't. | Ongoing retainers and regular home visits. Families pay even in quiet months. | In person: home visits, doctor appointments, and reports back to the family. | A paid first assessment of 4 to 6 hours in the parent's home. |
| **Group texts and notebooks** | None: free tools families already have. | Nobody: they're free or nearly free. | None. Caregivers mute, leave or refuse group chats to protect themselves. | None. No company stands behind them. | Nothing to install. Getting everyone onto one app is hard. |
| **Area Agencies on Aging** | No revenue: federal funding through the Administration on Aging, with grants to states. | Federal and state grants pay. Free to families who qualify. | None: a free public service with no paying customers. | Phone, text, chat or email with trained staff. Staff are kind but often hard to reach. | Contact the Eldercare Locator, then meet eligibility rules and wait for services. |
| **Respite and adult day services** | Fees, sliding scales at many adult day centers, state respite vouchers, and some payment from Medicaid, the VA and hospice. | Mostly families. Medicaid helps very low incomes, hospice the dying, and the VA some veterans. | Families come back for regular days or repeat stays while the parent needs care. | In person: staff, activities, meals and often rides. | Find a provider, then tour, apply, meet eligibility rules and often wait. |
| **VA caregiver programs** | No revenue: a federal benefit for veterans' families. | The VA pays, though respite may have a copay. Only qualifying veterans' families can use it. | Ongoing benefits with reassessments. Families stay while they qualify. | Local caregiver support teams and a weekday phone line. Some calls go unanswered. | The veteran and caregiver apply together online, by mail or in person. One caregiver waited 7 months for approval. |

> Company FAQ, home and policy pages (Cariloop, A Place for Mom), the AARP care manager article, the Eldercare Locator pages, Competitive Analysis 2 (Caring Village, Everplans, group texts) and caregiver posts. Checked word for word against saved sources (`build_business.py`: 35 cells, 57 sources, 0 problems).

### 4c. What they do well and what they don't

| Competitor | What they do well | What they don't do well |
|---|---|---|
| **Caring Village** | Shared calendar and medication list keep all siblings on the same care information. | Loses entries, resets the care plan, shows medical details to friends, and cannot get relatives to join. |
| **Everplans** | Gives adult children the parent's accounts, insurance policies and end-of-life wishes in one place. | Useless unless the parent filled it in. The iPad app runs only at phone size. |
| **Cariloop** | Assigns a full-time care coach who guides families through a crisis. | Available only through employers with 100 or more workers. The app freezes. |
| **A Place for Mom** | Lists nearby senior living options with prices and books tours. | Shares families' contact details, causing nonstop sales calls. Commission-paid advisors know little about the places. |
| **Geriatric care managers** | Attend doctor visits, evaluate care facilities and arrange respite during a crisis. | Cost $150 to $300 an hour, offer unclear services, and sometimes never make the agreed care plan. |
| **Group texts and notebooks** | Reach every relative instantly for free. A whiteboard schedule reduces a parent's repeated questions. | Help requests get ignored or just a 'like.' Notes and calendars get lost or erased. |
| **Area Agencies on Aging** | Connect families to free local services, support groups and Medicare counseling. Some fund respite. | Mostly referrals, long waitlists, hard-to-reach staff and strict eligibility. |
| **Respite and adult day services** | Give caregivers sleep, trips, dates and time alone while the parent is cared for. | Cost too much, have waitlists and minimum stays, and many parents refuse to go. |
| **VA caregiver programs** | Pays caregivers, funds home aides and respite, and teaches care tips. | Strict rules to qualify, limited aide hours, and unreliable aides. |

> What caregivers and customers report. Competitive Analysis 2 review themes (Caring Village: 29 caregiver reviews; group texts). 207 Reddit and forum mentions read in full, 135 from caregivers (A Place for Mom, care managers, Area Agencies on Aging). BBB: A Place for Mom has 272 reviews and 109 complaints in 3 years. Everplans: 8 App Store reviews and 2 Reddit comments from adult children. Cariloop: Google Play and 1 Reddit comment from a member. Checked word for word (`build_grid_v2.py`: 0 problems).

### 4d. How well they meet the 5 caregiver needs

*Yes = it does this. Partly = it does some of it, or only for some families. No = it doesn't.*

| Competitor | 1. Understand, handle behavior, know what to do | 2. Real relief for the caregiver | 3. Money, papers, accounts | 4. Works when the parent refuses help | 5. Relatives share the work |
|---|---|---|---|---|---|
| **Caring Village** | Partly: an AI helper answers care questions. No help with dementia behavior. | Partly: less stress and back-and-forth. Takes no care tasks off the caregiver. | Partly: stores documents. No help getting into bank, insurer or portal accounts. | No: nothing for a parent who refuses help. | Partly: relatives join free with their own login. Can't make them do tasks. |
| **Everplans** | No: stores papers only. No care or behavior advice. | No: takes no care work or time off the caregiver. | Yes, if the parent fills it in: accounts, papers, insurance and wishes in one vault. | No: the parent must fill it in and can lock sections until death. | Partly: relatives see chosen sections. Nothing splits the work. |
| **Cariloop** | Yes: coaches explain diagnoses like Alzheimer's and find the right doctors and care. | Partly: coaches find and book care. Only if the employer offers it. | Yes: help paying for care, with Medicare, Medicaid and VA benefits, and POAs. | Partly: coaches handle family dynamics. Nothing for a parent who refuses. | Partly: relatives join the Care Team and get updates. Tasks aren't split. |
| **A Place for Mom** | Partly: an advisor guides the search. Advisors often don't know the places. | Partly: saves search time. Nonstop calls add stress. | Partly: cost calculator and assessment. No help for Medicaid-only families. | No: an advisor told one family to lie to the parent to move her. | No: one family contact. Nothing for relatives to share. |
| **Geriatric care managers** | Yes: explain hard topics to the parent and family, and make a care plan. | Yes, for a price: respite, doctor visits and place tours taken off the caregiver. | Partly: advise on financial options. One took power of attorney without telling the family. | Partly: talk with the parent directly. Some parents still refuse them. | Partly: stand up to difficult relatives. Family fights often follow. |
| **Group texts and notebooks** | Partly: a written guide lets someone else step in. No advice on what to do. | No: constant messages wear the caregiver down. | Partly: a binder holds papers. Records pile up and can't be searched. | Partly: work without the parent using any tech. Nothing helps when the parent refuses. | Partly: everyone hears at once. Requests get silence or a 'like'. |
| **Area Agencies on Aging** | Partly: information and training. Staff often don't know the answer. | Partly: can pay for respite or home help. Long waits and strict rules. | Partly: Medicare counseling. Otherwise referrals, no hands-on help with accounts. | No: can't act without the parent's consent. | No: services go to one caregiver. Nothing for relatives to share. |
| **Respite and adult day services** | Partly: some adult day centers offer family counseling and behavior help. Respite itself is a break. | Yes, when families can get it: time to rest, run errands and travel. | No: doesn't touch the parent's money, papers or accounts. Applying adds more paperwork. | No: the parent refusing to go is a top reason respite goes unused. | No: nothing helps relatives share. Family not helping keeps caregivers from taking breaks. |
| **VA caregiver programs** | Partly: training and a support line, for veterans' families only. | Yes, if approved: at least 30 days of respite a year and paid aide hours. | Partly: free legal and financial planning and a stipend. Approval can take months. | No: nothing works unless the veteran agrees and applies with the caregiver. | Partly: the veteran can name up to 2 backup caregivers. |

> Each answer combines what the company offers (its own pages) with what caregivers report (the same sources as 4c). Checked word for word against saved sources (`build_grid_v2.py`).

## 5. The 4 gaps we could fill (unique value opportunities)

*Where every competitor falls short, the opening for us, and the risk.*

1. **No one handles a parent who refuses help or gets relatives to share the work.**
   - **Gap:** every competitor gets Partly or No on both. A Place for Mom's advisor even told a family to lie to the parent. Caring Village can't get relatives to join.
   - **Opening:** help that works around a refusing parent and splits real tasks among relatives.
2. **Personal, ongoing guidance is mostly locked behind an employer or a $150-an-hour bill.** (Reworded 2026-11-05 after the audit.)
   - **Gap:** Cariloop comes mostly through employers; keeping it after leaving a job costs $249 a month. Care managers cost $150 to $300 an hour. Free and public help is limited: Medicare GUIDE (a care navigator and up to $2,500 a year for respite) covers only people with dementia; the VA covers only veterans; the Alzheimer's helpline gives free advice, though a few caregivers found it general; Area Agencies on Aging mostly give referrals. Only 12% of caregivers would pay out of pocket, and willing payers cap near $70 a month.
   - **Opening:** coach-level guidance under $70 a month, or sold through employers, since 70% of working-age caregivers have jobs.
3. **Help with money and accounts works only if the parent prepared ahead of time.**
   - **Gap:** Everplans is useless unless the parent filled it in. Caring Village stores documents but can't get the caregiver into bank or insurer accounts. The market analysis found 132 posts about getting into a parent's accounts.
   - **Opening:** getting caregivers into a parent's accounts after the parent can no longer set it up.
   - **Risk:** health data and consent. Caring Village shows medical details to invited friends, and Everplans lets parents lock sections.
4. **Relief exists, but caregivers can't reach it.** (New in version 2.)
   - **Gap:** 39% of caregivers say respite would help, but only 13% have ever used it (AARP/NAC 2025, PDF pp.26-27). In caregiver posts, 128 used respite, 78 couldn't get it and 81 were still looking. Cost, the parent refusing, family not helping, eligibility rules, waitlists and rigid hours block it, for adult children most of all. Spouses face the same blocks, in a slightly different order. Respite services and the VA give real relief once a family gets in.
   - **Opening:** helping caregivers find, qualify for, pay for and actually use relief, including getting the parent to agree and relatives to cover.

**Also noted:**
- Burnout and meditation apps (segment 12) stay out of the grid: caregivers almost never use them (9 of 49,315 posts). Respite services and the VA now represent the #1 problem in the comparison.
- Medicines and hands-on care, and choosing a place, stay in the competitor rows but aren't takeaways.

### Data behind the 4 gaps

| Input | Where it comes from | Used for |
|---|---|---|
| No competitor gets a Yes on criteria 4 (parent refuses) or 5 (relatives share) | Step 5 grid | Takeaway 1 |
| Problem sizes: parent refuses 60, relatives don't help 48 | Audience page (`docs/audience-teacher-format-2026-11-04.md`) | Takeaway 1 |
| Cariloop comes mostly through employers ($249 a month to keep); care managers cost $150 to $300 an hour | Step 5 grid | Takeaway 2 |
| Only 12% would pay out of pocket; willing payers cap near $70 a month; 70% of working-age caregivers have jobs | Audience socioeconomic box (Figma 2378:7195; CAN 2026, Schulz 2016, AARP/NAC 2025) | Takeaway 2 |
| Employer benefits verdict: a different customer (the employer pays) | Market segment 7 (`docs/competitive-analysis-3-inputs.md`) | Takeaway 2 |
| Money, papers and accounts: 132 posts about getting into a parent's accounts | Market segment 10, `docs/market-analysis-3.md` | Takeaway 3 |
| Health data and consent are treated as a risk | Step 4 note | Takeaway 3 |
| Free and public help is limited: Medicare GUIDE (dementia only), the VA (veterans only), the Alzheimer's helpline (free advice; a few found it general), Area Agencies (mostly referrals) | `sources/competitors-4/basics-5a.json`, 5b themes, VA pages | Takeaway 2 (reworded) |
| Respite: 39% would like it, 13% use it; 128 used, 78 couldn't get it, 81 looking; barriers by audience | AARP/NAC 2025; `docs/market-analysis-segments-11-12-findings.md` | Takeaway 4 |
| Burnout apps barely used (9 of 49,315 posts) | Market analysis segment 12 update | Note |
| Medicines and hands-on care, and choosing a place, stay visible | Step 4 note | Note |

## 6. Still to research: who pays

**Open research: who pays (agreed 2026-11-04, from step 1 business problem 4)**

- **When:** after the feature analysis, before positioning. It's new research, so it updates the market analysis first.
- **Why:** positioning and the value proposition depend on who the customer is: families, employers or Medicare.
- **What we already know:**
  - Families: only 12% would pay out of pocket, and willing payers cap near $70 a month (CAN 2026, Schulz 2016).
  - Employers pay for Cariloop (segment 7).
  - Senior living places pay A Place for Mom when a family moves in.
  - Grants fund Area Agencies on Aging.
  - Medicare and Medicaid usually don't pay for care managers.
- **Research needed:**
  1. **Employers:** do they buy caregiver benefits, which employers, and what do they pay per employee? (Cariloop's $249 a month at MSU is the only price so far.)
  2. **Medicare and government programs:** what Medicare GUIDE pays for dementia care help, who can bill it, and whether it covers family caregiver support. It's named in `docs/exhaustion-dementia-research.md` but not researched yet. Also check other public programs that pay for caregiver support.
  3. **Families:** confirm the 12% and $70-a-month figures, and what families pay today for the alternatives.
-
