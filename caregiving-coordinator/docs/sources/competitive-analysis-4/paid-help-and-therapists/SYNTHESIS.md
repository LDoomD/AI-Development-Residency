# Paid help and therapy: what caregivers actually say (competitive analysis 4)

Date: 2026-11-06. Group: paid help (agencies, Care.com, companions) and therapy. Every number below comes from reading text, not from counting names. Each claim has a state, a source and a limit (skeptical-audit method). Files are in `docs/sources/competitive-analysis-4/paid-help-and-therapists/`.

## 1. The answer in plain words

1. **Only Care.com has enough caregiver reports to decide on.** 52 independent family caregivers wrote about it; 18 of them used it. Of those 18: 1 said it worked, 5 mixed, 7 did not work, 5 gave no result. The big problems are aides who vanish or quit, cost, and fear of strangers.
2. **Home care agencies are a real kind of help, but brand names are thin.** Home Instead has 8 caregiver reports (4 used it). Visiting Angels has 13 (5 used it, 2 said it worked). Senior Helpers, Right at Home and Comfort Keepers have 0 reports from a caregiver who used them. Their names show up only in lists, ads, and job posts.
3. **No therapy brand has enough evidence.** BetterHelp has 4 reports, Psychology Today 1, SonderMind 1, Zencare 1, Papa 1. Talkspace has 0 (both hits are an ad). Headway has 0 (all 8 hits are the English phrase "make headway"). Open Path has 0 hits at all.
4. **Most raw counts from the first pass were wrong in meaning.** "Home Instead" 53 hits: only 12 name the company (the rest are "at home instead of"). "Care.com" 132 is repeat mentions inside 82 posts, and 18 of those 82 are paid aides looking for work, not families. "Headway" 8 hits: 0 real.
5. **The big picture is not brands.** Caregivers use generic things: an aide paid by the family, an aide paid by a program (VA, Medicaid waiver, Area Agency on Aging), a respite worker, an agency, and "a therapist." In the 831 relief posts, almost no one names a business.
6. **What blocks relief most:** cost, aides who do not show up or quit, not trusting a stranger, the parent or spouse saying no, waitlists and eligibility rules for program-paid help, and (for therapy) finding someone who understands caregiving and takes their insurance.
7. **Who is missing:** spouses and partners (Audience 2). They are 1 of 52 Care.com reports and 0 of 13 Visiting Angels reports. They show up more in generic therapy (23 reports) and in program-paid aides (5).


## 2. How I read it (method, filters, raw hit counts)

**Data used (all saved, nothing scraped):**
- `docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl` (43,665 posts) plus `posts_targeted.jsonl` (5,650). No id overlaps, so 49,315 Reddit posts. The files hold the post text only, **not Reddit comments** (fields: key, type, subreddit, created, url, num_comments, text).
- `docs/sources/forums/agingcare/` and `forums/alzconnected/`: 142 thread files, split into 1,232 messages (359 AgingCare, 873 ALZConnected). Member names are replaced by "[member]", so I cannot tell if two comments are by one person.
- The 831 relevant relief posts: `market-analysis-3/segments-11-12/codes/` (ids), `packs/` (text), `audience-labels.json` (who is cared for).

**Part A (named names).** I searched the full corpus with the filters below, then read every hit in context (about 200 mentions). I wrote a label, fields and an exact quote for each one in `MENTIONS-READ.jsonl` (163 lines). A script checked every quote against the source text: 163 of 163 found, none over 20 words. The check ignores curly-versus-straight apostrophes and repeated spaces only.

| Name | Filter (case-insensitive unless noted) | Raw hit posts | Real mentions after reading |
|---|---|---|---|
| Care.com | `\bcare\.com\b` or `care dot com` | 82 (132 repeat mentions; plain text "care.com" appears in 105 posts, the other 23 are agingcare.com and similar) | 82 (all are the company) |
| Home Instead | `home instead` | 53 | 12 (41 are "home instead of" or "go home instead") |
| Visiting Angels | `visiting angels?` | 22 | 22 |
| Senior Helpers | `senior helpers?` | 5 | 2 (a forum list and a job ad); the other 3 are "Sensi senior helpers" (twice, a possibly different company) and the phrase "senior helper/companion" |
| Right at Home | `right at home` | 4 | 4 |
| Comfort Keepers | `comfort keepers?` | 1 | 1 |
| Papa | `joinpapa`, `papa pals`, `papa app/inc/health`, capital-P `Papa` | 9 | 2 (the other 7 mean grandfather or father) |
| BetterHelp | `better ?help` | 13 | 4 (9 are the words "better help") |
| Talkspace | `talk ?space` | 2 | 2 (same ad twice) |
| Headway | `headway` | 8 | 0 (all "make headway") |
| Psychology Today | `psychology today` | 3 | 1 |
| SonderMind | `sonder ?mind` | 1 | 1 |
| Zencare | `zencare` | 1 | 1 |
| Open Path | `open ?path` | 0 | 0 |

**Part B and C (discovery).** From the 1,086 posts read in the earlier relief pass, 831 were relevant. 185 were coded "paid aide or companion", 139 "therapist or counselor for the caregiver", 298 in either. I ran a cue-word filter (aide, agency, hired, home care, companion, sitter, CNA, therapist, counselor, psychologist, EAP, social worker, helper, and the brand names) over all 831: **832 sentences in 407 posts**. I read all 832 (saved as `PART-B-SENTENCES-READ.txt`). 424 posts had no cue word and were **not** read for this part. I also ran a capital-letter name finder over the 831 to catch brand names I might miss: it found nothing new. For the 324 paid-aide and therapist posts I read one line each (earlier readers' status, helped, barriers and quote) and wrote my own type and outcome (`manual_codes.json`).

**How I judged outcomes.** WORKED = the writer says it helped. DID NOT WORK = tried and it failed, or wanted it and could not get it. MIXED = both good and bad in the same report. NO OUTCOME = asking, planning, or no result stated.


## 3. Part A: every named candidate

Labels: 1 caregiver used it, 2 considering or asking, 3 recommends or warns, 4 vendor, staff, ad or survey-bait, 5 passing mention or wrong meaning. "Independent reports" = labels 1 to 3, no repeats. Outcome among those who used it: W worked, M mixed, N did not work, none = no result stated.

| Name | Read | 1 used | 2 asking | 3 advice | 4 vendor | 5 wrong | Independent reports (1-3) | Outcome of users | Who is cared for | 15 or more? |
|---|---|---|---|---|---|---|---|---|---|---|
| Care.com | 82 | 18 | 34 | 1 | 18 | 11 | 52 | W1 / M5 / N7 / none5 | parent 35, unclear 11, other relative 5, spouse or partner 1 | YES |
| Home Instead | 12 | 4 | 2 | 3 | 3 | 0 | 8 | W0 / M2 / N1 / none1 | parent 4, unclear 3, other relative 1 | NO |
| Visiting Angels | 22 | 5 | 7 | 1 | 7 | 2 | 13 | W2 / M0 / N1 / none2 | parent 10, unclear 3 | NO |
| Senior Helpers | 5 | 0 | 0 | 1 | 1 | 3 | 1 | - | unclear 1 | NO |
| Right at Home | 4 | 0 | 1 | 1 | 2 | 0 | 2 | - | unclear 2 | NO |
| Comfort Keepers | 1 | 0 | 0 | 0 | 1 | 0 | 0 | - | - | NO |
| Papa | 9 | 0 | 1 | 0 | 1 | 7 | 1 | - | parent 1 | NO |
| BetterHelp | 13 | 2 | 2 | 0 | 0 | 9 | 4 | W0 / M0 / N1 / none1 | other relative 3, parent 1 | NO |
| Talkspace | 2 | 0 | 0 | 0 | 2 | 0 | 0 | - | - | NO |
| Headway | 8 | 0 | 0 | 0 | 0 | 8 | 0 | - | - | NO |
| Psychology Today | 3 | 1 | 0 | 0 | 0 | 2 | 1 | W1 / M0 / N0 / none0 | unclear 1 | NO |
| SonderMind | 1 | 1 | 0 | 0 | 0 | 0 | 1 | W1 / M0 / N0 / none0 | unclear 1 | NO |
| Zencare | 1 | 0 | 1 | 0 | 0 | 0 | 1 | - | unclear 1 | NO |
| Open Path | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | NO |


State: observed. Source: `MENTIONS-READ.jsonl` (counts computed from it). Limit: reading is by one reader (me); a second reader could label some posts differently. Reddit comments are not in the data, so these are original posts plus forum messages only.

### 3.1 Care.com (52 independent family reports)

- **Who:** 35 care for a parent, 5 another relative, 1 a spouse, 11 unclear. Spouse and partner evidence is almost missing.
- **What they used it for:** finding an aide to cover daily hours (mostly while the writer works), plus a few weekend or overnight shifts. No one says they used it for "a break" by name. Relief is a side effect.
- **Outcome of the 18 who used it:** 1 worked, 5 mixed, 7 did not work, 5 no result stated.
- **Worked:** "and she was great, plus me 1x a week and other family a few times over for tea" (a father with a part-time aide 3 days a week).
- **Mixed:** "but it definitely isn't the best."; "got an avalanche of responses, but it's a super mixed bag."
- **Did not work:** "Then they fall off the face of the earth."; "Almost all the people I've reached out to from Care.com, they cant do the pay rate we are offering."; "We tried that and found that people wanted to be paid in cash or unreliable."
- **Safety and trust case:** "On Monday, I fired her." (the aide had 30 five-star reviews, then asked the mother, who has dementia, to write a check; the family fired her and feared retaliation).
- **Top blockers (count of reports):** cost 14 (rates of $25 to $35 an hour; a membership fee of about $40 a month to read applications); aide reliability 9 (no-shows, leaving, "lemons"); trust or safety 9 (fear of scams, asking how to vet); parent refuses 2; payroll taxes and paperwork 1.
- **Needs it serves:**

| Need | Does Care.com serve it? | Evidence |
|---|---|---|
| 1 Understand and know what to do next | Partly. It lists people. Families are left to vet, interview and handle contracts alone. | 33 asking posts, for example "how were you able to “vet” the person, so to speak?" and "do I have to worry about payroll taxes and such?" |
| 2 Real relief | Partly. Works when the aide stays. 7 of 18 users say it did not work. | p1fysvb7 worked; p1hhindo, p1k2q90r did not |
| 3 Money, papers, accounts | Mostly no. The family pays and handles payroll taxes. | cost 14; p1tw89y8; p1gtrgpo |
| 4 Works when the parent refuses | No report shows it working. | p1dku3g0 (mother refused and was rude to the people sent); p1eqjlc0 |
| 5 Relatives share the work | Not assessed. No writer mentions it. | none |

- **Enough to decide?** Yes for "is it a real, used, mixed-quality way to find a paid aide?" (52 reports, 18 users). No for "is it better or worse than agencies?" (only a handful of posts compare agency versus private hire).
- **Raw-count trap:** 18 of the 82 posts are paid caregivers, agencies, spam or product-research posts (label 4), and 11 more are empty or passing mentions. They are not family caregivers using it.

### 3.2 Home Instead and Visiting Angels (franchise home care agencies)

- **Home Instead (8 independent family reports; 4 used it):** outcomes of users: 2 mixed, 1 did not work, 1 no result. Mixed: "Now she has Home Instead coming 3 hours in the morning and evening" (the mother says the aide has nothing to do for 2.5 hours). Did not work: "We had hired Home Instead to help for a few weeks." (the aide was 22 and quit the day before Thanksgiving; the writer lost 9 hours a week away). Cost: "My mom gave Home Instead a check for over $30k for 30 days of service." Blockers: aide quality and turnover 5, cost 1, parent refuses respite 1.
- **Visiting Angels (13 independent family reports; 5 used it):** outcomes of users: 2 worked, 1 did not work, 2 no result. Worked: "it worked out great for me to be able to go to work."; "the in-home care is 1billion times better since its legit 1:1" (cheaper than assisted living; not covered by insurance). Did not work: "we tried and they would not take her since everybody else they served were worse off than her". Blockers: cost 4 (it is called "expensive as hell"), parent refuses or does not cooperate 3, trust or mixed reviews 1, agency declined the client 1, safety 1 ("his helper (Visiting Angels) was coming on Monday.").
- **Senior Helpers, Right at Home, Comfort Keepers:** 0 reports from a caregiver who used them. Only names in a forum list of agencies (alzconnected-77395), one question ("I am looking into them for some occasional care relief."), a list that reads like an ad, and job posts.
- **Needs:** 2 Real relief: yes when the aide is consistent (2 of 9 users said it worked). 3 Money: no; family pays, insurance does not. 4 Parent refuses: no (p1bdjmrp, p1dlyyun, p1nuphf8). 1 Next step: partly; agencies match and schedule, a forum writer warns they "send whoever they can get." 5 Relatives: not assessed.
- **Enough to decide?** No for a brand-by-brand call (4 and 5 users). Yes for the idea that franchise agencies are a real, used, expensive option that works only if the aide stays.

### 3.3 Therapy and therapist-finding names

- **BetterHelp (4 reports):** 2 used it, 2 only priced it. "I also joined BetterHelp, but nothing has erased this constant anxiety" (did not work for her anxiety). "Betterhelp.com sold people's information" (a trust problem; no therapy result stated). Two writers said they could not afford it: "I'm too poor to afford better insurance or to pay for any online services like BetterHelp."; "We can't afford BetterHelp." (this one is about therapy for the person cared for, not the caregiver).
- **Psychology Today (1 report):** "I found my therapist though the Psychology Today website. It is a great resource." It worked for that writer. The other two hits are links to articles.
- **SonderMind (1 report):** "I found a gem through SonderMind." It worked.
- **Zencare (1 report):** "I want to find someone who understands caregiving stress." (asking for a site; says caregiving is not a search filter).
- **Talkspace (0 reports):** both hits are one ad. The link carries `utm_campaign=grassroots` and `utm_medium=paidsocial`, and the therapy was for a mother grieving, not the caregiver. Treat as an ad.
- **Papa (1 report):** "Does anyone here have experience with this company?" Papa Pals is paid for by a Medicare supplement plan, so the family pays nothing. No one reports using it.
- **Headway, Open Path:** 0 reports.
- **Enough to decide?** No, for every therapy brand. Even all five together are 8 reports. What caregivers describe is a generic therapist (Section 5).


## 4. Part B: every business, agency type, program or app named for paid help or therapy

Counts are **separate posts among the 831 relief posts** whose text matches a rule I wrote (rules in `scripts/rules.py`). I spot-checked 6 random matches for 9 of the rules; the rules over-count (in my 6-match checks about 7 in 10 were on target; the online-therapy rule was weakest, about half, because it matches "zoom"), so treat counts as "named or described in this many posts," not as users. For types I also give the hand-coded count (Section 5), which is the reliable one.

### 4.1 Real businesses and marketplaces (named by a caregiver)

| Name | Kind | Posts (of 831) | Ids | Note |
|---|---|---|---|---|
| Care.com | marketplace | 1 | p1eqjlc0 | In the 831 only once; 82 across the whole corpus (Section 3). |
| Home Instead | agency (franchise) | 2 | p1pxe7ba, p1qu598w | 12 across the whole corpus. |
| Visiting Angels | agency (franchise) | 1 | p1nuphf8 | 22 across the whole corpus. |
| Papa Pals | companion service (insurer-paid) | 1 | p18a42uc |  |
| Seniors Helping Seniors | companion franchise or group idea | 1 | p139urv3 | Also asked about in p11bowfc (outside the 831). |
| Centerwell | home health company (doctor-ordered visits) | 1 | p1c9w7gg | Named as the agency sending nurses and therapists. |
| Advanced Care at Home | hospital-at-home program | 1 | p1wombot | Brings nurses to the house; the writer says it gives no respite for her. |
| Aegis | respite or senior living facility | 1 | p1abmgsr | Asked about cost of respite care. Not paid in-home help. |
| Passages | respite or care program | 1 | p1qzh1m2 | Asked if programs like it cover extended time off. |
| Wellthy | employer benefit (care coordination) | 2 | p1h9p97b, p15edl7o | Both ask "has anyone used it?" |
| Torchlight | employer benefit (advising) | 1 | p1e6j86w | Asks "is it worth the time?" |
| Zencare | therapist directory | 1 | p196re2l |  |
| Psychology Today | therapist directory | 1 | alzconnected-77427 |  |
| SonderMind | therapist network | 1 | alzconnected-77427 | Same thread as Psychology Today (counted as 1 thread). |
| A Place For Mom | referral service | 1 | p1h0fxvm | Called "SEO content"; not used for paid help. |

Not found in the 831: BetterHelp, Talkspace, Headway, Open Path, Senior Helpers, Right at Home, Comfort Keepers, CareYaya, Homewatch, Interim, Brightstar, Amada. (CareYaya, Homewatch, Interim, Brightwood Health and NannyServices appear in other posts I read for Part A: p1fhdu59, p1pwakzb, p1d60pgp. They were not searched on purpose, so their counts are unknown.)

### 4.2 Programs (government or nonprofit, not businesses)

| Program or channel | Posts (rule) |
|---|---|
| Medicaid waiver (any state: waiver, HCBS) | 62 |
| Hospice aide, respite or counseling | 41 |
| VA caregiver, respite or aide program | 38 |
| Medicare home health (agency visits) | 37 |
| Family paid as caregiver (waiver, AAA, VA stipend) | 28 |
| Local senior center / church / volunteer sitters | 26 |
| Area Agency on Aging / Council on Aging | 25 |
| Geriatric care manager / social worker for the caregiver | 11 |
| UK or Canada public care (NHS, carers service, social care, Ontario Health at Home) | 7 |
| Private-pay home care company (typed phrase "private pay") | 7 |
| Meals on Wheels | 6 |
| IHSS (California) | 4 |
| PACE | 4 |
| CDPAP / IRIS / state self-directed pay | 3 |
| Respite voucher / grant | 2 |
| Employer EAP | 1 |


These are the big sources of paid in-home help in the data. They are what a family uses when it cannot pay out of pocket.

### 4.3 Generic types (not a business)

| Type | Posts (rule) |
|---|---|
| Therapist or counselor for the writer | 126 |
| Aide paid by a program: Medicaid waiver, VA, Area Agency on Aging, IHSS | 95 |
| Doctor-ordered home health visits (nurse, aide, CNA) | 50 |
| Home care agency or care company | 36 |
| Aide or caregiver hired directly or privately | 34 |
| Respite worker or in-home respite | 31 |
| Couples, marriage or family counseling | 14 |
| Cleaner, housekeeper, meal delivery | 13 |
| Free, public or insurance-limited therapy | 11 |
| Online or telehealth therapy | 9 |
| Hospice, carer-service or peer counselor | 6 |
| Employer program (EAP, benefit) | 4 |
| Companion service (Papa, Seniors Helping Seniors, non-medical) | 3 |
| Psychiatrist for the writer | 2 |


Not found as a named thing: "private pay agency" shows up as a phrase in 7 posts only (no company); no employer EAP is described as used (1 post tells someone to ask their employer, alzconnected-77379); no hospital program besides Advanced Care at Home.

State: observed (rules and counts in `partb_counts.json`, `prog_counts.json`). Limit: keyword rules; 424 of 831 posts had no cue word and were not read for this part; forum posts are excerpts around a mention, not whole threads.


## 5. Part C: every type, with outcomes

Source: my hand-coding of the 185 "paid aide or companion" and 139 "therapist or counselor" posts (`manual_codes.json`). 31 paid-aide posts were not paid in-home help (facility respite, day program, therapy) and 4 were repeats, so 150 count. 10 therapy posts were not therapy for the writer, leaving 129 (123 individual, 6 couples or family). W = worked, M = mixed, N = did not work or could not get, none = no result stated (asking, planning).

| Type | Independent reports | W | M | N | none | Who is cared for (A1 parent, A2 spouse or partner) |
|---|---|---|---|---|---|---|
| Home care agency or care company | 19 | 1 | 5 | 7 | 6 | A1 15, A2 0, other 4 |
| Aide paid by the family (hired directly, or not named) | 84 | 12 | 17 | 5 | 50 | A1 58, A2 16, other 10 |
| Aide paid by a program (VA, Medicaid waiver, Area Agency on Aging, hospice, county) | 41 | 6 | 11 | 8 | 16 | A1 22, A2 5, other 14 |
| Respite worker or sitter hired for a break | 6 | 0 | 4 | 1 | 1 | A1 6, A2 0, other 0 |
| Therapist or counselor for the caregiver | 123 | 27 | 10 | 20 | 66 | A1 72, A2 23, other 28 |
| Couples or family counseling | 6 | 1 | 0 | 2 | 3 | A1 4, A2 2, other 0 |


**Audience split of outcomes (A1 parent / A2 spouse or partner):**
- Aide paid by the family: A1 W8 M10 N4 none36; A2 W2 M5 none9.
- Aide paid by a program: A1 W4 M6 N3 none9; A2 W1 M3 none1.
- Agency: A1 W1 M2 N7 none5 (no spouse reports).
- Therapist: A1 W15 M4 N14 none39; A2 W5 M5 N1 none12.

**Top blockers (posts with the barrier; earlier readers' codes, my type and outcome):**

| Type | Cost | Person refuses | Quality or trust | Rules or eligibility | Waitlist |
|---|---|---|---|---|---|
| Agency (19) | 10 | 4 | 7 | 3 | 1 |
| Family-paid aide (84) | 24 | 22 | 12 | 7 | 4 |
| Program-paid aide (41) | 10 | 10 | 8 | 15 | 9 |
| Therapist (123) | 16 | 13 | 9 | 7 | 5 |

**What the types tell us:**
- **Family-paid aide (84 reports; 34 with a result):** 12 worked, 17 mixed, 5 did not. It works when the aide is reliable and the parent accepts that one person. Mixed reports are mostly cost (for example $225 a week for 9 hours of a respite worker the mother accepts) and an aide who will not work the hours needed for "a true break" ("My mom has a care aid who comes and helps me but doesn't want to work the hours I need").
- **Program-paid aide (41; 25 with a result):** 6 worked, 11 mixed, 8 did not. The blockers are rules and waitlists: "In Oregon, you can only get a caregiver if the person has assets valued below 2000$." ; "That waiver for support is an 8-10 year wait list unless the state decides it's a priority level one" Good result: "The VA has been great about getting him an aide. Hopefully they'll continue to provide respite care."
- **Agency (19; 13 with a result):** 1 worked, 5 mixed, 7 did not. Most "did not" are "could not get one": minimum hours ("every agency we've tried to go through has a minimum hours for their caregivers that is more than what my"), no staff ("They either want full time, don't service my area, won't do homes with pets"), wait lists ("There a minimum wait or 2 years for an aide.").
- **Therapist (123; 57 with a result):** 27 worked, 10 mixed, 20 did not. Worked: "I've seen a therapist multiple times now. He helps me out a lot."; "I do have my own counselor that I see weekly and she is probably the only person that has kept". Did not: "I see a therapist but it’s no help."; "Most therapists are not well versed in coping with caregiving". Main failure is not the therapy but getting in: cost (16 posts), "can't find anyone in network" ("Can’t find a grief support group and the caregiver support group never called back."), waitlists, and therapists who "are not well versed in coping with caregiving." I hand-checked 16 posts about finding a therapist who understands caregiving or can be reached: p11bq3kp, p11mfwvk, p14vh0k9, p14w0n8e, p16yoywf, p196re2l, p1at8dq1, p1conram, p1d5bh5a, p1dsqqkz, p1i7mzri, p1k4w8fb, p1mnxlq5, p1xfgola, p1xlkn1i, alzconnected-77427.
- **When the person refuses (Need 4):** 39 paid-aide posts name a refusing parent or spouse. Of those, 24 have no result, 4 did not work, 8 mixed, 3 worked. The mixed and worked ones are cases where the parent already accepts one named person (a respite worker, p10vv5x0, p11265me) or a VA aide arrived by order (p1u5wh64). No type works on its own when the person says no.

**Which of the 5 needs each type serves (inferred from the evidence above):**

| Type | 1 Understand next step | 2 Real relief | 3 Money, papers | 4 Parent refuses | 5 Relatives share |
|---|---|---|---|---|---|
| Care.com | Partly (list only) | Partly (7 of 18 users failed) | No | No | Not assessed |
| Agencies (Home Instead, Visiting Angels) | Partly (they schedule) | Yes when aide stays (2 of 9 users) | No (family pays) | No | Not assessed |
| Family-paid aide | No | Yes, 12 worked | No | Only if parent accepts that person | Not assessed |
| Program-paid aide | No, it is hard to find and apply | Yes when approved (6 worked) | Yes, it pays | Rarely | Not assessed |
| Therapist | Partly | Emotional relief, not hours off (27 worked) | No | No | Couples counseling 1 of 6 worked |


## 6. Which candidates are real competitors for "help for worn-out caregivers"?

| Candidate | Include as a competitor? | Why (from the data) |
|---|---|---|
| Care.com | **Yes** | 52 reports, 18 users. It is the main marketplace a family uses to find a paid aide. Weak spots are reliability, cost and trust. |
| Home care agencies as one row (Home Instead, Visiting Angels as examples) | **Yes, as a type** | Real, used, expensive. Brand-level evidence is thin (4 and 5 users). Use one row: "franchise home care agency." |
| Senior Helpers, Right at Home, Comfort Keepers | No | 0 caregiver users in the data. Names appear only in lists, ads and job posts. |
| Papa | Watch only | 1 question. Insurer pays, so it is a different business model. |
| BetterHelp, Talkspace, Headway, Open Path, Zencare, SonderMind, Psychology Today | No as separate rows | 8 reports together; Talkspace is an ad; Headway is not a company in these posts. If the analysis needs a therapy row, use "ordinary therapist (found through insurance, a doctor, or a directory)." |
| Ordinary therapist or counselor | **Yes, as a workaround** | 123 reports, 27 worked, 20 did not. The unmet need is finding one who understands caregiving, takes the insurance, and has an open slot. |
| Paid-by-a-program aide (VA, Medicaid waiver, Area Agency on Aging) | **Yes, as government programs** | 41 reports. Pays the bill but blocked by rules and waitlists. Not businesses. |
| Family-paid private aide with no marketplace | **Yes, as a workaround** | 84 reports. The most common route in the data. |


## 7. Evidence table (skeptical audit)

| Claim | State | Source | Limit |
|---|---|---|---|
| 52 independent family reports name Care.com; 18 used it | observed | `MENTIONS-READ.jsonl` (name=Care.com, label 1 to 3, independent=true) | One reader; Reddit comments not in data; forum authors masked |
| Of 18 Care.com users: 1 worked, 5 mixed, 7 did not, 5 no result | observed | same file, outcome field | Outcome is my reading of the writer's words |
| Home Instead has 12 real mentions, not 53 | observed | script check of `home instead` hits; each read | Only the saved corpus |
| Headway has 0 real mentions | observed | 8 hits read; all "make headway" | Corpus only |
| Talkspace hits are one ad | observed | p1k2fdi8 link contains `utm_campaign=grassroots`, `utm_medium=paidsocial` | Ad intent is inferred from the link tags |
| No therapy or agency brand besides Care.com reaches 15 reports | observed | Section 3 table | Corpus only; real-world use is larger |
| Spouse and partner evidence is thin for named brands | observed | Section 3 audience column | Audience taken from `audience-labels.json` for the 831 and from my reading for others |
| Family-paid aide: 12 worked, 17 mixed, 5 did not, 50 no result (84) | inferred | `manual_codes.json` from earlier readers' lines plus sentences I read | I did not reread every full post; outcome follows the earlier readers' codes and quote |
| Therapist: 27 worked, 10 mixed, 20 did not, 66 no result (123) | inferred | same | same |
| Almost no one names a business in the 831 relief posts | observed | 832 cue sentences read; name finder found nothing new | 424 posts without a cue word not read for this part |
| Care.com is "better" or "worse" than agencies | not-assessed | no head-to-head data | n/a |
| Programs named (waiver, VA, AAA) are the main funding route for paid aides | inferred | rule counts 62, 38, 25 | rule counts, spot-checked only |


## 8. Not checked

- **Reddit comments.** The saved data holds posts only. People often name companies in replies; none of that is here. A reply search would add users and warnings, especially for Care.com, BetterHelp and agencies.
- **Same person twice.** Forum names are masked. I removed obvious repeats (same text posted twice, same-minute duplicate posts) and counted each forum message once. Two forum messages could be one person.
- **Whole posts for Part B.** I read the sentences with paid-help or therapy cue words (832 sentences in 407 posts), not every sentence of every post. 424 of the 831 posts were not read for this part.
- **Outcomes for types** follow the earlier readers' code lines plus the cue sentences, not a full reread of 324 posts.
- **Other names.** I did not search for other therapy companies (for example Rula, Grow Therapy, Alma, Lyra, Cerebral) or other agencies or marketplaces (CareYaya, Homewatch, Interim, Brightstar, Amada, NannyServices). They appeared only incidentally. Run a second pass if the owner wants them.
- **Rule precision.** The Part B rules were spot-checked on 6 random matches each for 9 rules; precision was not measured for the rest.
- **Second reader.** No one else labeled these mentions, so there is no agreement score.
- **Skills not applied:** none of the code, accessibility, security or release skills apply (no code or UI was changed). Applied: skeptical-audit (state, source and limit on every claim). `data-lifecycle-compliance` was judged not relevant: all text is public posts already saved; no personal data was added beyond ids and URLs already in the repo.
