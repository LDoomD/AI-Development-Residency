# Competitive Analysis 3 (started 2026-11-04)

Built step by step from the saved documents listed in `Dog Feeding Docs/Week 2_3/dogfood-2026-11-04-start-competitive-analysis.md`. Each step is approved by the owner before the next. Figma: the "UPDATED 2026-11-04: COMPETITIVE ANALYSIS 3" section on the competitive analysis page.

## Inputs that lead this analysis (the newest versions, checked 2026-11-04)

The owner's rule: the newest market research and audience segmentation, with all their data, lead every step of this analysis.

| Input | Version used | Data behind it |
|---|---|---|
| Market analysis | 3rd version, 2026-11-04 (`docs/market-analysis-3.md`, Figma 2598:10950) | 117 forum threads, 412 Reddit caregiver posts (random sample), 672 targeted Reddit posts, app reviews, AARP/NAC 2025, Alzheimer's Association 2026 |
| Audience goals and use cases | Teacher-format section, 2026-11-04 (`docs/audience-teacher-format-2026-11-04.md`, Figma 2623:76) | 412 posts and threads read in full (303 Reddit, 109 forum), 777 coded moments (`docs/sources/market-analysis-3/audience-v2/`) |
| Audience labels, traits and segmentation boxes | The current boxes on the audience page, marked FINAL 2026-11-03 (Figma 2378:7111, 2378:7177, 2378:7186, 2378:7189, 2378:7192, 2378:7195) | AARP/NAC 2025, forum threads, Schulz 2016, CAN 2026 |
| Reddit notes on the segmentation boxes | Only in the superseded section, 2026-11-04 (Figma 2605:638, `docs/market-analysis-3.md`) | 412 Reddit caregiver posts. Used as data. They don't yet have a home in a current section. |

## Step 1: Problems to solve related to the competitive analysis (approved 2026-11-04, option C)

Teacher's question (Figma 2:16): *What business and user-related problems is your team trying to solve that leads to opportunities for competitive analysis?*

1. **User:** caregivers' biggest problems (burnout, dementia behavior, the parent refusing help, choosing a place) aren't covered by the competitors we studied.
   *Source: `docs/market-analysis-3.md` (top problems), `docs/audience-teacher-format-2026-11-04.md` (Audience 1 use cases: exhaustion 138, dementia behavior 82, the parent refuses help 60, choosing a place 46), `docs/competitive-analysis-2.md`.*
2. **User:** families stitch together free tools (group chats, notebooks, alert buttons) instead of using the coordination apps. We don't know why.
   *Source: competitive analysis board, "What families use instead" (Figma 2508:9836).*
3. **Business:** we're not sure what our unique value is, now that the top problems changed.
   *Source: `docs/market-analysis-3.md`.*
4. **Business:** we don't know who pays for help in this space: families, employers or Medicare.
   *Source: `docs/exhaustion-dementia-research.md`. Audience page socioeconomic box (Figma 2378:7195): only 12% would pay out of pocket (CAN 2026), and willing payers cap near $70 a month (Schulz 2016).*

## Step 2: Which problems and use cases the competitors should cover (approved 2026-11-04, option A)

Cover the top 7 problems. Each is seen in 46 or more Audience 1 posts and threads, and in at least 1 in 5 of the Reddit posts or forum threads. Audience 1 leads because Vision Board #1 is for them.

| Problem | Audience 1 (seen in) | Audience 2 (seen in) | Market analysis (Reddit / forums) | Covered by the 10 competitors in Competitive Analysis 2? |
|---|---|---|---|---|
| 1. Exhaustion, doing it alone | 138 | 45 | 51% / 43% (top) | No |
| 2. Dementia behavior, hard talks | 82 | 24 | 24% / 34% | No |
| 3. Money, legal papers, the parent's accounts | 74 (+132 accounts posts in the targeted search) | 13 | 28% / 33% (strongest unmet need) | Partly (Everplans, MyChart) |
| 4. Medicines and hands-on care | 62 | 24 | 13% / 16% (+17 hands-on posts) | Medicines only (Medisafe, Caring Village) |
| 5. The parent refuses help | 60 | 9 | 20% / 10% (new) | No |
| 6. Relatives don't help | 48 | 12 | 24% / 24% | Yes (Caring Village, CaringBridge, Lotsa, group texts) |
| 7. Choosing and paying for a place | 46 | 9 | 22% / 30% | No |

- **Problems 8 and 9 (safety at home 37, answers from doctors 30):** stay covered by the competitors already studied (Lively, Medical Guardian, MyChart). No new research.
- **Problem 10 (being far away, 20):** too small to drive the analysis.
- **Audience 2's aides, hospice and trusting helpers (14):** waits until the Audience 2 work.

*Sources: `docs/audience-teacher-format-2026-11-04.md` (seen-in counts), `docs/market-analysis-3.md` (top problems, shares), `docs/competitive-analysis-2.md` (coverage).*

### Do the top 7 hold up in both the previous and the new research? (checked 2026-11-04)

Audience 1 counts, from `docs/sources/market-analysis-3/audience-v2/moments-by-usecase.json`. Previous research: 55 forum threads. New research: 268 Reddit posts.

| Problem | Previous (forums): rank (threads) | New (Reddit): rank (posts) |
|---|---|---|
| Exhaustion | 1 (22) | 1 (116) |
| Dementia behavior | 2 (18) | 2 (64) |
| Money and papers | 3 (15) | 3 (59) |
| Medicines and hands-on care | 4 (12) | 5 (50) |
| The parent refuses help | 8 (4) | 4 (56) |
| Relatives don't help | 5 (10) | 6 (38) |
| Choosing a place | 6 (9) | 7 (37) |

6 of the 7 are in the top 7 of both. **"The parent refuses help" comes almost entirely from the new Reddit research.** The forums barely mention it. Treat it as the least proven of the 7 in the older data. (In the forums alone, safety at home would be 7th.)

## Step 3 (first version, REPLACED 2026-11-04 by the second version below)

Kept as a record. Replaced because its competitors weren't taken from the market analysis segment table (see `docs/reports/competitive-analysis-3-change-report-2026-11-04.md`).

### Step 3, first version: which competitors to analyze (approved 2026-11-04, option A)

The list is rebuilt around the top 7 problems from step 2. Evidence: `docs/sources/competitors-4/evidence.json`. Proof check: `docs/sources/competitors-4/verify_quotes.py` (18 quotes found in the saved pages, 0 not found).

**Direct competitors (7):**

| Competitor | Problems it touches (step 2 numbers) | Source |
|---|---|---|
| Caring Village | 4 medicines, 6 relatives | Competitive Analysis 2 |
| CaringBridge | 6 relatives | Competitive Analysis 2 |
| Everplans | 3 money, papers, accounts | Competitive Analysis 2 |
| Trualta (online caregiver skills training) | 2 dementia, 4 hands-on care, 5 refusal of care | PMC study PMC8293668; Central Ohio AAA and AgeWays pages (free through local aging agencies) |
| Cariloop (employer-paid caregiver coaching) | 1 exhaustion | cariloop.com coaching page (saved 2026-11-02) |
| A Place for Mom (senior living referral) | 7 choosing a place | aplaceformom.com/about (saved 2026-11-01) |
| Geriatric care managers (Aging Life Care professionals) | 5 parent refuses help, 7 choosing a place, 2 hard talks | aginglifecare.org (read in a browser 2026-11-04); AARP article for prices |

**Indirect competitors:**

| Competitor | Problems it touches | Source |
|---|---|---|
| Alzheimer's Association 24/7 Helpline | 1 exhaustion, 2 dementia | alz.org helpline page (saved 2026-11-02) |
| Eldercare Locator and Area Agencies on Aging | 1 exhaustion, 3 money, 7 choosing a place | usaging.org, eldercare.acl.gov (saved 2026-11-04) |
| Medicare GUIDE Model | 1 exhaustion, 2 dementia | cms.gov GUIDE page (saved 2026-11-02) |
| Medisafe | 4 medicines | Competitive Analysis 2 |
| Aeroflow Urology | 4 hands-on care (supplies) | aeroflowurology.com (saved 2026-11-04) |
| Group texts and paper notebooks | 6 relatives | Competitive Analysis 2 |
| Calm (general mental health app) | 1 exhaustion | calm.com (saved 2026-11-02) |
| Headspace (general mental health app) | 1 exhaustion | headspace.com (saved 2026-11-02) |

- **Added 2026-11-04 after a check against the market analysis:** Calm and Headspace. The market analysis names them as crowding the burnout segment (segment 12), so leaving them out would contradict it. Proof check: 22 quotes found, 0 not found.
- **Not carried forward:** Lively, Medical Guardian and Epic MyChart cover safety and doctors, which aren't in the top 7. Their Competitive Analysis 2 rows stay as they are.
- **Gap:** nothing was found that's built specifically for a parent who refuses help. Care managers and Trualta touch it, but neither is made only for it.
- **Fixed 2026-11-04:** pages blocked to the save script were read in the desktop app's built-in browser and saved in `docs/sources/competitors-4/manual-saves/`: aginglifecare.org, coaaa.org (Trualta) and hr.msu.edu (Cariloop's $249-a-month price). trualta.com failed at first (HTTP 500), then loaded when the owner opened it, and was saved. aging.ny.gov and teepasnow.com are no longer needed (other sources cover Trualta, and Teepa Snow isn't on the list).

## Step 4 (first version, REPLACED 2026-11-04 by the 5 criteria below)

Kept as a record. Replaced after the owner reviewed Fleety's (Tech Fleet) advice: use about 5 criteria taken from the audience's top needs.

### Step 4, first version: which questions to answer about the competitors (approved 2026-11-04, option A, refined with the whole audience page)

The owner approved option A and asked that it reflect everything on the audience segmentation page. The four questions marked "refined" were widened using that page: the labels and traits, the four segmentation boxes (geographic, behavioral, demographic, socioeconomic), and the motivations, goals and use cases.

| # | Direct or indirect | Question | Where it comes from |
|---|---|---|---|
| 1 | Both | What's their business model, who pays (the family, an employer, insurance or the government), and what does it cost a family? **(refined)** | Step 1, line 4. Socioeconomic box: median household income $68,770, 30% under $50,000; only 12% would pay out of pocket; willing payers cap near $70 a month (AARP p.130, CAN 2026, Schulz 2016) |
| 2 | Direct | How do they keep customers coming back? | Teacher's original question |
| 3 | Both | Does it help the caregiver understand what's happening, what to do next, and where to get help? **(refined)** | Audience 1's situational goals #1 (understand, 73) and #2 (get help or services, 58). Behavioral box: 55% do medical or nursing tasks, only 22% were trained (AARP p.34) |
| 4 | Both | Does it protect the caregiver's own health, job, time and breaks? **(refined)** | Audience 1's life goals #1 (health, 73), #2 (job, life and money, 52) and #3 (time and breaks, 23). Demographic box: 70% of caregivers aged 18 to 64 are employed (AARP p.38-39). Problem 1 (exhaustion, 138) |
| 5 | Both | What does it do when the parent refuses help or won't use it, and does it respect the parent's own choices? **(refined)** | Problem 5 (60). Audience 1 motivation: let the parent stay home and make their own choices (24) |
| 6 | Both | Does it get other relatives to share the work, each with their own access? | Problems 6 (48) and 3 (accounts, 132 posts). Behavioral box: 34% have no other help (AARP p.25) |
| 7 | Both | How does it treat health data and consent? | Current question 6; the product's risk profile (`docs/risk-profile.md`) |
| 8 | Both | Do caregivers actually use it, and what do they use instead? | Step 1, line 2 ("what families use instead", Figma 2508:9836) |

- **Dropped from the 11-02 questions:**
  - "How their customer experience differs" (already a column in the teacher's table).
  - "Emergencies and failure" (safety isn't in the top 7).
  - "Setup and phones" (not tied to a top-7 problem).
- **Not turned into a question:**
  - Geographic (more than 10% live an hour or more away, AARP p.22): "being far away" is small (20) and wasn't in the top 7.
  - Audience 2's "companionship and someone who understands" (11): waits for the Audience 2 work.

*Sources: `docs/audience-teacher-format-2026-11-04.md`. Audience page boxes in Figma: 2378:7111 (Audience 1 label), 2378:7186, 2378:7189, 2378:7192 and 2378:7195 (the four segmentation boxes). Competitive analysis board: 4:764 (the 11-02 questions).*

## Step 5a: Basics for all 15 competitors (approved 2026-11-04)

The teacher's template columns, plus question 1. New competitors: `docs/sources/competitors-4/basics-5a.json`, proof `verify_basics_5a.py` (130 quotes found, 0 not found). Kept competitors: `docs/competitive-analysis-2.md`, with Medisafe's price added from the App Store.

### Direct competitors

| Competitor | Market segment | Website | Main features | How they stand out | Business model | Who pays, and the cost (question 1) | Source |
|---|---|---|---|---|---|---|---|
| Caring Village | Family care-coordination apps | https://caringvillage.com/ | One shared app for a family's care: calendar, to-dos, medication lists, care plan, journal, group messages, document storage, and an AI helper called Julia. | Claims to be one 'command center' that replaces scattered texts and spreadsheets, built by former caregivers, with a 24/7 AI assistant. | Freemium subscription. A free plan with ads, plus paid Circle and Village plans. It also sells to businesses for their patients or clients, and offers gift subscriptions. No funding figure found. | The caregiver who creates the 'village' pays. Everyone invited joins free. Free: 2 members. Circle: $14.99 a month (5 members). Village: $24.99 a month (50 members on the pricing page, 25 in the FAQ). 17% off yearly. | Competitive Analysis 2 |
| CaringBridge | Family care-coordination apps | https://www.caringbridge.org/ | A private web page or app journal for health updates, with comments, a help calendar for meals and rides, and links to GoFundMe and Meal Train. | Claims to be the established nonprofit (since 1997) built only for health journeys: private, ad-free, and never selling personal data. | A free, donation-funded nonprofit: about $10.6M revenue in FY2025, 97% from contributions. It asks users for gifts, and its privacy policy also lists sharing data for targeted ads. | A patient or family caregiver creates the page, and friends and family read it. It's free for everyone. Donors fund it, often the same families (6). | Competitive Analysis 2 |
| Everplans | Digital vaults and emergency access | https://www.everplans.com/ | A secure online vault for documents, IDs, accounts and wishes, with guided checklists and 'deputies' who get access to chosen sections. | Claims to organize all of a person's life details and tell them what to do next, using a smart planning system. | Freemium: free (3 items) or Premium at $99.99 a year, plus deals through financial advisors and partners. Owned by Precoa since October 2024. | People organizing their own affairs pay for Premium themselves, or get it through an advisor (who pays then isn't stated). $99.99 a year. | Competitive Analysis 2 |
| Trualta | None of these: online skills training for family caregivers (personalized lessons on dementia care, safety, personal care and self-care). | https://www.trualta.com/ (read in a browser on 2026-11-04). | A library of lessons for caregivers (behavior, personal care, safety, self-care), 24/7 caregiver forums, and weekly live events; local partners add support. | Personalized lessons written by nurses, therapists and social workers. A 30-day study co-written by Trualta staff reported 84.4% used a learned skill. | Offered through partners such as Area Agencies on Aging, which give caregivers free subscriptions. What partners pay Trualta is not stated. The 2021 study was grant-funded. | Free to families: "offered at no cost through local partnerships" (examples: six Michigan counties, eight Central Ohio counties). The partner pays; what it pays isn't stated. | `basics-5a.json` |
| Cariloop | 7 Employer and health-plan caregiver benefits. | https://www.cariloop.com/ | Licensed care coaches, backup care with subsidies, a vetted provider network to search, book and pay, and a shared family case with document uploads and a mobile app. | Full-time licensed coaches (average 12+ years) who reply in under 2 hours, no referral fees from providers, B Corp status, and a claimed 3x employer ROI. | Sold to employers, mostly priced per employee per month or in blocks of cases, usually for groups of 100+ employees. | The employer pays, as a benefit. Example (Michigan State University): free to employees for 30 days of coaching, then $249 a month to extend coaching. | `basics-5a.json` |
| A Place for Mom | 4 Senior care referral and placement. | https://www.aplaceformom.com/ (the saved page text does not print the URL; the page title names the service). | A free local advisor, care and financial assessment, a tailored list with pricing, tour scheduling, a care quiz, a cost calculator, family reviews, and VA benefits guides. | Claims the largest US senior care network, 400+ advisors, 2.3M+ families helped and 25 years. Network counts differ between pages (11K to 14K+ communities). | Referral fees: communities pay when a referred family moves in, home care agencies pay per referral. Lead forms also consent to calls from its community customers. | Senior living communities and home care agencies pay. The advice service is free to families, with no fees claimed. | `basics-5a.json` |
| Geriatric care managers | None of these: private care managers (usually nurses or social workers) that families hire to plan and coordinate an older adult's care. | https://www.aginglifecare.org/ (Aging Life Care Association; read in a browser on 2026-11-04). | Home assessments and safety checks, hiring and monitoring aides, booking appointments and rides, care plans, hospital discharge plans, respite, and acting for distant families. | In-person assessment, local connections and clinical training, so families hire the right help and skip services they don't need. | Hourly fees of $150 to $300 by region, often a 4 to 6 hour first assessment, and sometimes mileage and travel time. | The family, out of pocket. Medicare and Medicaid usually don't pay; long-term care insurance or an employer EAP may cover some. One family budgets $650 to $900 a month. | `basics-5a.json` |

### Indirect competitors

| Competitor | Market segment | Website | Main features | How they stand out | Business model | Who pays, and the cost (question 1) | Source |
|---|---|---|---|---|---|---|---|
| Alzheimer's Association 24/7 Helpline | None of these: a free dementia phone helpline for information, local referrals, crisis help and emotional support. | https://www.alz.org/help-support/resources/helpline | 24/7 phone line, weekday live chat, online form, 200+ languages, free care consultations with master's-level dementia experts, and sign-up for support groups. | Always open, a live person, confidential, free, and dementia-specific. | Nonprofit. The helpline is funded 44% by a federal ACL grant and 56% by non-government sources; the site asks for donations. | Free to families. Paid for by the federal government grant and non-government funding such as donors. | `basics-5a.json` |
| Eldercare Locator and Area Agencies on Aging | None of these: a government information and referral service that connects families to local aging services. | https://eldercare.acl.gov | Search by location, plus phone, text, chat or email with trained staff who refer people to 600+ local Area Agencies on Aging on transport, housing, benefits and home services. | The only national referral service of its kind, running since 1991, handling about 400,000 requests a year. | No revenue model: funded by the U.S. Administration on Aging and run by the nonprofit USAging. | The federal government pays. The saved pages call it a public service but don't state a price to families. | `basics-5a.json` |
| Medicare GUIDE Model | None of these: a Medicare-paid dementia care program delivered by participating care teams, with caregiver support and respite. | https://www.cms.gov/priorities/innovation/innovation-models/guide | Assessment and care plan, a care navigator, a 24/7 support line, caregiver training, respite up to $2,500 a year, and links to meals and transport. | A voluntary national Medicare test that supports both the person with dementia and the caregiver; 292 participants; regular Medicare benefits stay the same. | CMS pays participating providers tiered monthly per-patient payments plus up to $2,500 a year per patient for respite. An 8-year test from July 2024. | Medicare (government) pays. Patient needs dementia, Medicare Parts A and B as primary insurance, no hospice or PACE. Any cost to the family is not stated. | `basics-5a.json` |
| Medisafe | Medication reminder apps | https://medisafeapp.com/ | Medication reminders and refill alerts, drug-interaction warnings, one account for several family members' meds, and a 'Medfriend' who is alerted to missed doses. | Claims to be the number-one medication reminder, ranked first by pharmacists, with complicated dosing and security certifications. | Free app with a paid subscription (price not shown, the pricing pages saved as 404s). It also sells a platform to drug makers and providers and may share de-identified data commercially. Raised a $30M Series C in 2021. | Patients and family members use it; drug companies and providers are business customers. Free app; Premium on the App Store costs $2.99 to $9.99 a month or $27.99 to $39.99 a year (several price points listed). | Competitive Analysis 2 + App Store (Firecrawl 2026-11-04) |
| Aeroflow Urology | None of these: a medical supplier that delivers insurance-covered incontinence products to the home each month. | https://aeroflowurology.com/ (the saved page text does not print the URL; the page title names the company). | Online eligibility check, help getting the prescription and paperwork, filing the Medicaid claim, monthly home delivery, resupply reminders, product changes, and help with denials. | Specialists who know every state's Medicaid rules do the insurance paperwork so supplies arrive at $0. | A Medicaid-accredited supplier that files insurance claims for the products it ships; the pages do not spell out its payment terms. The site also has a cart. | Medicaid or the insurance plan pays; $0 to eligible families with a diagnosis and prescription. Not offered in some states (such as California, New York). Limits may apply. | `basics-5a.json` |
| Group texts and paper notebooks | Workaround, not a company | n/a | Family group chats and texts; notebooks, binders and wall calendars. | Not companies: free, already there, nothing to install. | Not companies. Free or nearly free. | Used by the main caregiver, relatives and paid aides. Free. | Competitive Analysis 2 |
| Calm | 12 Caregiver mental health and burnout support (a general stress and sleep app, not caregiver-specific). | https://www.calm.com (the saved page text does not print the URL; the page title names the app). | Guided meditations, 500+ Sleep Stories, soundscapes and music, quick breathing and Panic SOS exercises, a sleep check-in, on phones, web, TV and watches. | Claims to be the number-one app, with 2 million+ five-star reviews and research-based tools. Nothing on the page is aimed at caregivers. | Free trial, then a paid subscription that unlocks the library; also family plans, gifts, and plans sold to organizations. | The individual, or an employer through Calm for Organizations. Calm's plan page: 7-day trial, then $79.99 a year. A review lists a $99.99-a-year family plan for six. | `basics-5a.json` |
| Headspace | 12 Caregiver mental health and burnout support (a general mental health app, not caregiver-specific). | https://www.headspace.com (the saved page text does not print the URL; the page title names the app). | 1,000+ meditations and exercises, sleepcasts, mental health coaching, online therapy that takes insurance, an AI companion (Ebb), and family plans. | Evidence-based tools since 2010, used by thousands of employers and health plans, and HSA/FSA eligible. Nothing on the page is aimed at caregivers. | Consumer subscriptions (annual, monthly, student, family, gifts) plus sales to employers and health plans, including full EAP replacement, therapy and psychiatry. | The individual (HSA/FSA allowed), or an employer or health plan. Official price: $69.99 a year (14-day free trial) or $12.99 a month. | `basics-5a.json` |

**What stands out:**
- Who pays splits four ways: the family (care managers, Everplans, Calm, Headspace), an employer (Cariloop), the government or Medicaid (Eldercare Locator, GUIDE, Aeroflow, Trualta through agencies), and businesses paying referral fees (A Place for Mom).
- 7 of the 15 fit none of the market analysis's 14 segments: caregiver training, helplines, government programs, private care managers and supply delivery aren't captured.

**Limits:**
- Trualta's own site was read in the browser on 2026-11-04 (it failed earlier that day). Its satisfaction figures are its own claims. The PMC study was co-written by Trualta staff.
- Cariloop's $249 a month comes from one employer (Michigan State University).
- Medisafe lists several App Store price points.
- The care managers' prices come from an AARP article.

## Step 4, second version: the 5 criteria (approved 2026-11-04)

Following Fleety's advice and the teacher's template (which has 5 question columns), each competitor is judged on 5 criteria taken from Audience 1's top needs. Checked against Figma: the audience section 2623:76, the segmentation boxes 2378:7186 to 2378:7195, and the updated market analysis 2598:10950.

| # | Criterion | Audience data (Figma 2623:76, segmentation boxes) | Market analysis (Figma 2598:10950) |
|---|---|---|---|
| 1 | Does it help the caregiver understand what's happening, handle hard behavior, and know what to do next? | #1 situational goal (73). Use case #2, dementia behavior (82). 55% do medical tasks, only 22% were trained (AARP p.34). | Dementia behavior 24% / 34%. No market segment serves it. |
| 2 | Does it give the caregiver real relief: time, breaks, their own health? | Use case #1, exhaustion (138). #1 life goal, health and sanity (73). 34% have no other help (AARP p.25). | Burnout 51% / 43%, top everywhere. Segment 12: biggest need, crowded. Owner's scoring: Valuable High. |
| 3 | Does it get the parent's money, papers and accounts under control? | Use case #3 (74). Situational goal #3 (49). | 28% / 33%; 132 targeted accounts posts. Segment 10: strongest unmet need. Owner's scoring: Valuable High. |
| 4 | Does it still work when the parent refuses help, and respect the parent's choices? | Use case #5 (60). Motivation: let the parent stay home and choose (24). | 20% / 10% (new from Reddit). No market segment serves it. |
| 5 | Does it get relatives to actually share the work? | Use case #6 (48). 34% have no other help. | Family coordination 24% / 24%. Families use group chats, not apps (99 posts). Owner's scoring: Medium. |

- **Kept in the template's own columns, not criteria:** business model, who pays and the cost (only 12% would pay out of pocket), and what customers say (do caregivers use it).
- **Considered for criterion 5 but not chosen (owner's choice):** medicines and hands-on care (62); choosing and paying for a place (46, owner's scoring Valuable High). Both stay visible in the competitor rows and the takeaways.
- **Health data and consent:** treated as a risk in the takeaways.

**Next:** step 3 is redone from the market analysis segments (`docs/competitive-analysis-3-inputs.md`). The new competitor list is 7: 5 from the segments, plus what families use instead (group texts and notebooks), plus Area Agencies on Aging. Parts 5a and 5b above are kept as evidence and will be redone for the final list.

## Step 3, second version: the 7 competitors, taken from the market analysis segments (approved 2026-11-04)

Candidates: every company the market analysis names in a segment that touches the 5 criteria (`docs/competitive-analysis-3-inputs.md`). Caregiver mentions were counted by `docs/sources/competitive-analysis-3/count_segment_candidates.py` (49,315 saved Reddit posts).

| # | Competitor | Type | Market analysis segment | Criteria it touches | Caregiver evidence |
|---|---|---|---|---|---|
| 1 | Caring Village | Direct (business) | 1 Family care-coordination apps | 5, 3 | 29 caregiver reviews |
| 2 | Everplans | Direct (business) | 10 Digital vaults (strongest unmet need) | 3 | Thin: 1 caregiving review |
| 3 | Cariloop | Direct (business, employer-paid) | 7 Employer caregiver benefits | 2, 3 | 0 posts; company pages and price saved |
| 4 | A Place for Mom | Direct (business) | 4 Senior care referral (owner's scoring: Valuable High) | 2 | 21 caregiver posts |
| 5 | Geriatric care managers | Direct (private professionals) | No segment; fills the gap for criteria 1 and 4 | 1, 4, 2 | 31 caregiver posts |
| 6 | Group texts and notebooks | Indirect (workaround) | What families use instead | 5 | Named in about 100 posts each |
| 7 | Area Agencies on Aging | Indirect (government program) | What families use instead | 2, 3 | 47 caregiver posts, 29 describe using it |

**Left out, with reasons:**
- CaringBridge, Lotsa: same segment and criterion as Caring Village.
- Caring.com: same segment as A Place for Mom, 2 mentions.
- Trustworthy, Cake, AARP Digital Vault, 1Password, Keeper: 0 caregiver mentions.
- Calm, Talkspace, Sanvello, BetterHelp, ianacare: 0 to 5 mentions, general apps.
- Wellthy, Carallel: 0 to 2 mentions.
- Medication apps, pharmacies, home care: medicines isn't a criterion.
- Alert devices, visit notes, MyChart, Chapter: their problems aren't in the top 7.
- Trualta, Medicare GUIDE, the Alzheimer's helpline: almost no caregiver evidence.

**Trade-off (the owner kept the list as is):** segment 12, mental health and burnout (the biggest need, but crowded), has no competitor in the grid.

## Step 5: The competitor grid (approved 2026-11-04)

7 competitors from step 3, the teacher's template columns, and the 5 criteria from step 4. Every cell answers its column's question from data, in the owner-approved style (CLAUDE.md, "How to answer a table question from data").

**Sources and checks:**
- `docs/sources/competitive-analysis-3/grid/build_grid_v2.py` lists the saved source behind every point.
- The output is `grid-v2.json`, checked with 91 cells, 158 sources and 0 problems.
- Version 1 (`build_grid.py`) is kept and replaced.

### The basics

| Competitor | Type | Market segment | Website | Main features | How they stand out | Who pays, and the cost |
|---|---|---|---|---|---|---|
| **Caring Village** | Direct (business) | 1 Family care-coordination apps | caringvillage.com | A shared family app with a calendar, to-dos, medication lists, documents and an AI helper. | Built by former caregivers as one place for the whole family's care. | The caregiver pays: free for 2 people, or $14.99 to $24.99 a month. |
| **Everplans** | Direct (business) | 10 Digital vaults and emergency access | everplans.com | Online vault for documents, accounts and wishes, shared with chosen family. | Walks a person through organizing all their life details and next steps. | The parent pays: free for 3 items, or $99.99 a year. |
| **Cariloop** | Direct (business, employer-paid) | 7 Employer and health-plan caregiver benefits | cariloop.com | A personal care coach, a care-booking marketplace, a family Care Team and document storage. | Full-time coaches who take no money from the care providers they suggest. | The employer pays. At MSU, keeping the coach yourself costs $249 a month. |
| **A Place for Mom** | Direct (business) | 4 Senior care referral and placement | aplaceformom.com | A free advisor, a care and cost check, local places with prices, and tours. | Says it has the country's largest senior care network. | Senior living places pay it when a family moves in. Free to families. |
| **Geriatric care managers** | Direct (private professionals) | None of the 14 segments (private care management) | aginglifecare.org (to find one) | Home visits, care plans, hiring and checking aides, appointments, and help for families far away. | Trained local professionals who see the parent and the home in person. | The family pays $150 to $300 an hour. Medicare and Medicaid usually don't. |
| **Group texts and notebooks** | Indirect (workaround) | What families use instead (not a company) | n/a | Family group chats, notebooks, binders and whiteboards. | Everyone already has them, they're free, and there's nothing to install. | Nobody: they're free or nearly free. |
| **Area Agencies on Aging** | Indirect (government program) | None of the 14 segments (free public service) | eldercare.acl.gov (finds your local agency) | Caregiver information, help finding services, counseling, support groups, training and respite. | Local, government-funded and free to families who qualify. | Federal and state grants pay. Free to families who qualify. |

### What they do well, and what they don't

| Competitor | What they do well | What they don't do well |
|---|---|---|
| **Caring Village** | Shared calendar and medication list keep all siblings on the same care information. | Loses entries, resets the care plan, shows medical details to friends, and cannot get relatives to join. |
| **Everplans** | Gives adult children the parent's accounts, insurance policies and end-of-life wishes in one place. | Useless unless the parent filled it in. The iPad app runs only at phone size. |
| **Cariloop** | Assigns a full-time care coach who guides families through a crisis. | Available only through employers with 100 or more workers. The app freezes. |
| **A Place for Mom** | Lists nearby senior living options with prices and books tours. | Shares families' contact details, causing nonstop sales calls. Commission-paid advisors know little about the places. |
| **Geriatric care managers** | Attend doctor visits, evaluate care facilities and arrange respite during a crisis. | Cost $150 to $300 an hour, offer unclear services, and sometimes never make the agreed care plan. |
| **Group texts and notebooks** | Reach every relative instantly for free. A whiteboard schedule reduces a parent's repeated questions. | Help requests get ignored or just a 'like.' Notes and calendars get lost or erased. |
| **Area Agencies on Aging** | Connect families to free local services, support groups and Medicare counseling. Some fund respite. | Mostly referrals, long waitlists, hard-to-reach staff and strict eligibility. |

### The 5 criteria

| Competitor | 1. Understand, handle behavior, know what to do | 2. Real relief for the caregiver | 3. Money, papers, accounts | 4. Works when the parent refuses help | 5. Relatives share the work |
|---|---|---|---|---|---|
| **Caring Village** | Partly: an AI helper answers care questions. No help with dementia behavior. | Partly: less stress and back-and-forth. Takes no care tasks off the caregiver. | Partly: stores documents. No help getting into bank, insurer or portal accounts. | No: nothing for a parent who refuses help. | Partly: relatives join free with their own login. Can't make them do tasks. |
| **Everplans** | No: stores papers only. No care or behavior advice. | No: takes no care work or time off the caregiver. | Yes, if the parent fills it in: accounts, papers, insurance and wishes in one vault. | No: the parent must fill it in and can lock sections until death. | Partly: relatives see chosen sections. Nothing splits the work. |
| **Cariloop** | Yes: coaches explain diagnoses like Alzheimer's and find the right doctors and care. | Partly: coaches find and book care. Only if the employer offers it. | Yes: help paying for care, with Medicare, Medicaid and VA benefits, and POAs. | Partly: coaches handle family dynamics. Nothing for a parent who refuses. | Partly: relatives join the Care Team and get updates. Tasks aren't split. |
| **A Place for Mom** | Partly: an advisor guides the search. Advisors often don't know the places. | Partly: saves search time. Nonstop calls add stress. | Partly: cost calculator and assessment. No help for Medicaid-only families. | No: an advisor told one family to lie to the parent to move her. | No: one family contact. Nothing for relatives to share. |
| **Geriatric care managers** | Yes: explain hard topics to the parent and family, and make a care plan. | Yes, for a price: respite, doctor visits and place tours taken off the caregiver. | Partly: advise on financial options. One took power of attorney without telling the family. | Partly: talk with the parent directly. Some parents still refuse them. | Partly: stand up to difficult relatives. Family fights often follow. |
| **Group texts and notebooks** | Partly: a written guide lets someone else step in. No advice on what to do. | No: constant messages wear the caregiver down. | Partly: a binder holds papers. Records pile up and can't be searched. | Partly: work without the parent using any tech. Nothing helps when the parent refuses. | Partly: everyone hears at once. Requests get silence or a 'like'. |
| **Area Agencies on Aging** | Partly: information and training. Staff often don't know the answer. | Partly: can pay for respite or home help. Long waits and strict rules. | Partly: Medicare counseling. Otherwise referrals, no hands-on help with accounts. | No: can't act without the parent's consent. | No: services go to one caregiver. Nothing for relatives to share. |

## Next steps (not started)

6. Three takeaways: where competitors fail the audience, and where the opening is, tied to the market opportunity verdicts.
7. Figma section, then the starting brief for the feature analysis.
