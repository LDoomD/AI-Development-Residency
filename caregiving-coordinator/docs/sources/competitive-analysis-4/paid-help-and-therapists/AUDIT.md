# Independent audit: paid help and therapists (competitive analysis 4)

Date: 2026-11-06. Auditor: a fresh reader who did none of the earlier work. Method: skeptical-audit (each claim has a state, a source you can reopen, and a limit). Plain words.
Folder: `docs/sources/competitive-analysis-4/paid-help-and-therapists/`. Nothing existing was edited. New files: this file and the `check*.py`, `audit_load.py`, `check*_output.txt`, `check*_packet/blind*.txt`, `check*_ids/labels.json` files next to it.

States: **proven** = a check that could fail was run and passed (command and output shown). **observed** = I saw it directly. **inferred** = follows from observed facts. **documented**, **reported**, **not-assessed** as usual.

Run any check again: `python3 -I check1_quotes.py` (same for the others, from this folder). `audit_load.py` is my own loader (50,547 messages: 49,315 Reddit posts, 1,232 forum messages), not the helper's `corpus.py`.

## Bottom line

| Question | Answer | State |
|---|---|---|
| Are the quotes real? | Yes. 163 of 163 are exact text in the cited post. 0 are over 20 words. | proven |
| Are the labels right? | Mostly. Blind on 40 mentions: label agreement 39 of 40 (98%). | observed |
| Are the brand counts right? | Yes. Care.com 82 posts / 132 repeats / 18 users, Visiting Angels 22, Home Instead 53 raw and 12 real all reproduce from raw data. | proven |
| Anything wrong? | Yes, 10 corrections (list below). The biggest: "5 used Visiting Angels" is 4, the aide "outcome" numbers are soft (agreement 46 to 58%), and "aide paid by the family" is an assumption in 57 of 84 posts. | observed |
| What did the helper miss? | A Place for Mom (about 20 family posts, not in the helper's Part A), CareYaya (9 posts, 0 users), Lyra (1 user), and a few single hits. None changes the 15-report test except A Place for Mom (see Section 4). | observed |
| Enough to include Care.com as a competitor? | Yes: 52 independent posts (target 15). Only 13 of those tell how it went. | proven |
| Any other single brand at 15? | No. Visiting Angels 13, Home Instead 8, CareYaya 6, all therapy brands 4 or fewer. A Place for Mom is probably 15 or more but is a placement referral service, not relief, and I read only snippets. | observed / inferred |

---

## Check 1. Quotes

Script: `check1_quotes.py`. Output: `check1_output.txt`.

```
messages loaded: 50547 reddit: 49315 forum: 1232 dup keys 0
MENTIONS-READ rows: 163 exact/whitespace-only: 163 needed curly-quote/dash fold: 0 MISS: 0
quotes >20 words: []
rows whose cited post does not contain the business name at all: []
SYNTHESIS quoted strings found: 78
```

| Claim | State | Source | Limit |
|---|---|---|---|
| All 163 quotes in MENTIONS-READ.jsonl appear word for word in the post or forum message named in the row | proven | `check1_quotes.py` (exact substring, spaces collapsed only; no apostrophe folding was needed) | Proves the words exist. It does not prove the label or outcome given to them. |
| No quote is over 20 words | proven | same script, longest quote under 20 | Counts words split on spaces |
| Every row's post contains the business name (in text or in a link) | proven | same script | A name can still mean something else (that is what label 5 is for) |
| 78 quoted strings in SYNTHESIS.md: 65 are found in the corpus (case ignored), 13 are not | observed | same script, "SYN-MISS" lines | Searched the whole corpus, not only the cited post |

The 13 misses, one by one (none is a fake caregiver quote):
- 9 are labels, column names or questions the helper wrote (for example `paid aide or companion`, `Independent reports`, `help for worn-out caregivers`, `is it better or worse than agencies?`). Not quotes.
- 2 are phrases put in quote marks that are **not word for word**: SYNTHESIS.md line 131 `"has anyone used it?"` (the two Wellthy posts both say "Has anyone used" but then name the service) and line 221 `"could not get one"` (the helper's own summary, not a caregiver's words). Cosmetic.
- 1 is a search phrase, `"private pay agency"` (line 184). Not a quote.
- 1 is a broken fragment from the regex (`), so treat counts as`). Not a quote.

Limit for the whole check: quotes in SYNTHESIS.md that sit inside a longer quote with an ellipsis were checked piece by piece.

---

## Check 2. Blind reclassification of 40 mentions

Scripts: `check2_sample.py` (picks 40, seed 20261106, every one of the 13 names and every label 1 to 5; writes the packet without labels), `check2_compare.py`, `check2_dups.py`. My labels are in `check2_my_labels.json`, the text I read is `check2_blind_packet.txt`.

Sample: 14 Care.com, 5 Home Instead, 4 Visiting Angels, 3 BetterHelp, 3 Right at Home, 2 each Senior Helpers, Headway, Papa, 1 each of the other 6. Labels: 8 used, 7 asking, 5 advice, 13 vendor, 7 wrong meaning.

```
label 39 / 40 98%
outcome 19 / 20 95%        (compared where either of us gave label 1 to 3)
cared_for 19 / 20 95%
real(1-3) vs not(4-5): 40 / 40
```

| Field | Agreement | State | Limit |
|---|---|---|---|
| Label 1 to 5 | 39 of 40 (98%) | observed | n = 40. I had earlier seen the helper's notes for some Care.com, Visiting Angels and Home Instead rows (see Check 3), so this is not perfectly blind. |
| Real family mention (1 to 3) versus not (4 to 5) | 40 of 40 | observed | same |
| Outcome (worked / mixed / did not work / none) | 19 of 20 (95%) | observed | Only 20 rows had a family caregiver in them |
| Who is cared for | 19 of 20 (95%) | observed | same |

Every disagreement (3):

| # | Row | Helper | Audit | Why |
|---|---|---|---|---|
| 11 | p18eibme, Visiting Angels | label 2, no outcome | label 1, mixed | "We just can't afford to keep funding that" means the family already used it. Borderline. |
| 11 | same row | no outcome | mixed | same reason |
| 26 | agingcare-499812-COMMENT6, Care.com | cared for: unclear | n/a | The writer owns a care agency and gives advice to a stranger; nobody is being cared for. Trivial. |

**No person counted twice?** (`check2_dups_output.txt`)
- 86 rows have label 1 to 3, but only 80 distinct post ids. The 6 extra rows are 4 posts that name several brands (`alzconnected-77395-COMMENT2` names 4 agencies; p11bowfc, p15mkqm3, p17wkj4q name 2 each). That is one person counted once per brand, which is correct per brand. It would be wrong to add the brand counts together as people. proven.
- 8 repeat posts are already marked `independent=false` by the helper (for example the 3 "Libelous Reviews" posts, the Talkspace ad twice, Home Instead Dayton/Daytona). My own near-duplicate scan found 4 identical-text pairs, all 4 already flagged. proven for what is saved.
- p1k2n2pf and p1k2q90r (both Care.com, same day, same group) are different stories (a dad and a mom). Not the same post.
- Limit: the data has **no author names** (Reddit rows have no username; forum names are "[member]"). One person posting twice with different words cannot be found. not-assessed.

---

## Check 3. Trying to disprove the conclusions

### 3a. Re-derive the counts (script `check3a_counts.py`, output `check3a_output.txt`)

| Claim | My number | Verdict | State | Limit |
|---|---|---|---|---|
| Care.com in 82 posts | 82 (78 Reddit, 4 forum) by `\bcare\.com\b` or "care dot com"; helper's 82 ids match mine exactly (0 missing, 0 extra) | holds | proven | Regex I chose |
| 132 repeat mentions | 132 occurrences in those 82 | holds | proven | |
| "care.com" text in 105 posts | 105 with no word boundary (agingcare.com etc.) | holds | proven | |
| Label split 18 used / 34 asking / 1 advice / 18 vendor / 11 wrong | same in the file | holds | proven | counts the file, not the labels |
| 52 independent family reports | 52 (53 minus one repeat) | holds | proven | One post per person is assumed |
| 18 users, outcome 1 worked / 5 mixed / 7 did not / 5 none | I read all 18 myself: 1 / 5 / 7 / 5 | holds | observed | |
| ...but "used" means different things | Of 18 users, 13 describe how it went. Of the 5 with no result: 1 hired someone (p1h5qaga); 4 had only posted an ad, were about to interview, or were still searching (p1k82n50, p1ntv6ba, p1xb0ayu, p1sffjum) | correction | observed | |
| Visiting Angels 22 real mentions | 22 by `visiting angels?`, same ids as the helper | holds | proven | |
| Visiting Angels "5 used it, 2 worked" | 2 worked is right (p1kl4i3n, p1ovlon8). The 5 includes **p1724omw**: the agency would not take her mother ("they would not take her"). That is "tried, was turned away", not "used". So 4 used. p1nuphf8 (arranged 3 visits a week) and p1nbfe8b (father's helper had not come yet) are real but weak. | correction | observed | `MENTIONS-READ.jsonl` line 52 |
| Visiting Angels 13 independent, 7 staff or ad | 13 and 7 hold. 6 of the 7 are staff or job posts, 1 is an ad list. | holds | proven | |
| Home Instead 53 raw, 12 real | 53 raw. All 41 left out are "home instead of" or "go/take home instead" (I read the 12 that were not followed by "of"; none names the company). | holds | observed | |
| Home Instead "4 used it" | p14ahwv3 says the check was written and "They are coming tomorrow", so service had not started. 3 had service (p1pxe7ba, p1faqh6s, p1qu598w). | correction | observed | line 64 |

### 3b. Names the helper may have missed (script `check3b_names.py`, output `check3b_counts_output.txt`; I read every hit)

The helper's own Not checked list says these were not searched. I searched them across all 50,547 messages.

| Name | Hits | What the hits are | In helper's file? | Counts toward 15? |
|---|---|---|---|---|
| Rula | 0 | | no | no |
| Grow Therapy | 0 | | no | no |
| Alma (company) | 0 real (2 hits are "Alma Mater") | | no | no |
| Lyra | 1 | p1uh613t: "started family therapy with my dad through Lyra". One user, employer benefit. | no | 1 |
| CareYaya | 9 posts | 6 ask "has anyone used it?" (p1fhdu59, p1f4ap45, p1f4o2es, p1wxr4t6, and 2 removed-body titles p1jwxzc6 and p1mgdcmi), 3 are promotion (p1b43qmh, p1ttwugx by its founder, agingcare-499537-COMMENT10). 0 say they used it. p1f4ap45 and p1f4o2es read like templates. | 1 (inside p1fhdu59) | 6 asking, 0 users |
| Homewatch | 1 | in the ad list p1pwakzb | yes | 0 |
| Interim HealthCare | 3 | the same ad list plus 2 "[removed]" ad titles | 1 | 0 |
| BrightStar | 1 | "a bright star" (not the company) | no | 0 |
| Comfort Keepers | 1 | ad list | yes | 0 |
| Right at Home | 4 | 1 asking (p11bowfc), 1 forum list, 2 identical removed ads | yes | 2 |
| Senior Helpers | 5 | job ad, "Senai" AI-call complaint (maybe a different company), "senior helper/companion", forum list | yes | 1 |
| Honor (home care) | 0 (23 hits are the word "honor") | | no | 0 |
| Home Instead, real use only | 3 had service + 1 about to start (see 3a) | | yes | 8 independent |
| Papa | 9 hits; 2 real (p18a42uc asking; p1pwakzb ad list); 7 are "Papa" = grandfather | | yes | 1 |
| Wellthy | 2 (both ask "has anyone used it?") | p1h9p97b, p15edl7o | no (only Part B) | 2 asking |
| Torchlight | 1 asking | p1e6j86w | no | 1 |
| Amada | 1 ("F Amada Senior Care. It's All Lies" with removed body, p1hgmck0) | likely a complaint, writer role unknown | no | 0 or 1 |
| Bayada | 2 (1 praise for hospice, p1g25c0k by a former caregiver; 1 removed title) | | no | 1 |
| Aetna-CareLinx | 1 (p16i2oht, an info post that says the benefit gives caregivers a break) | | no | 0 |
| CarePatrol, Seniorly-type placement | 2 / 8 senior-advisor posts | placement referral | 1 | 0 |
| **A Place for Mom** | **31 posts; 3 in helper's file** | About 20 are in a family caregiver's voice: warnings about spam calls, "used it", or asking. I read snippets, not full posts. About 9 say they contacted it (p1bvdp2t, p1j1vrmx, p11zvnoj, p17kp1k8, p1fm6k24, p1i1hskc, p1icxwp0, p1kocgug, alzconnected-77373-COMMENT6). | partly | **probably 15 or more** |
| Caring.com, Teladoc, Thriveworks, Charlie Health, Headspace (app), Amedisys, Synergy HomeCare, Home Helpers (capital) | 0 to 2 | ads, lists, or the word "headspace" | no | 0 |

State: observed (regex, then I read the context lines in the script output; for A Place for Mom the read is of the 110-character snippet around the name, not the whole post). Limit: counts are posts, not people, and the corpus has no Reddit comments.

Generic business types the Part B list may have missed (counts are 831-post keyword hits, so inferred): live-in caregiver 10, nanny or babysitter comparison 12, church or faith volunteers 24, adult day program 58, nursing-student or pre-health caregivers 1, Craigslist 0. Only "live-in" is absent from the helper's generic table; the rest are in other folders or tiny. Scope note: this folder covers 2 of the 8 kinds of help in the earlier coding (paid aide 185, therapist 139). In-home respite (105), adult day (101), short-stay respite (106) and support groups (114) are not read here.

### 3c. "The 831 relief posts name almost no business" (script `check3c_831.py`, output `check3c_output.txt`)

I used a different method from the helper: a list of about 80 business names plus a "capitalized name after called/named/through/hired/with" finder over the 831 posts.
- Result: holds. Businesses named, each in 1 to 2 posts: Home Instead 2, Wellthy 2, Care.com 1, Visiting Angels 1, Papa Pals 1, Torchlight 1, Zencare 1, Centerwell 1, A Place For Mom 2, Seniors Helping Seniors 1, Aegis 1, Passages 1. One the helper did not list: **Welbe Health** (p1m9ig5r, a clinic, not paid help). Everything else the finder returned was a program, insurer or medical word.
- State: observed. Limit: a business named in an unusual way (no capital letter, a nickname) would be missed by both methods.

### 3d. Type counts (script `check3d_sample.py`, `check3d_my_codes.py`, outputs `check3d_output.txt`, `check3d_cues_output.txt`)

Counts reproduce from `manual_codes.json`: family-paid (PV) 84, program-paid (PR) 41, agency 19, respite worker 6, therapist 123, couples 6; paid-aide set 185 and therapist set 139 equal the earlier coding exactly; union 298. proven (counting the file).

Blind recount: 30 random posts of each of the 3 main types, I read the text (cue-sentence view, full text where unclear) and coded type and outcome without seeing the helper's code.

| Type | Type agrees | Outcome agrees | What the disagreements are | State |
|---|---|---|---|---|
| Aide paid by the family (PV), n = 29 (1 post not judgeable from the saved thread text) | 29 of 29 (100%) | 17 of 29 (58%) | 5 times the helper wrote "no outcome" where the writer wanted help and could not get it (the helper's own rule says that is "did not work") | observed |
| Aide paid by a program (PR), n = 30 | 27 of 30 (90%) | 14 of 30 (46%) | After rereading the full post I agree with the helper on 2 of my 3 type misses (p1qzh1m2 has in-home workers; p1u5wh64 got 9 to 20 VA hours). 1 stays a miss (p1udyrtl is about a VA support group). Outcomes: 4 times mixed vs worked/none, 4 times "did not work" vs mixed. | observed |
| Therapist (TH), n = 28 (2 not judgeable from saved text) | 28 of 28 (100%) | 23 of 28 (82%) | small shifts between worked, mixed, none | observed |

Why 3 posts could not be judged: forum "ids" like `alzconnected-77470` are whole threads, and the therapy or aide words are in a reply, not in the first message. I confirmed each of those threads has a cue word in a reply (`check3d_cues_output.txt`). Not an error, but my sample for those 3 was thinner.

Two problems found while doing this:
1. **"Aide paid by the family" is mostly "payer not stated."** Only 27 of the 84 posts name a payer or a price (the earlier coder's `payer_cost` field). In 57 the helper assumed the family pays. Type is still right in my sample (it is a paid aide), the payer label is not proven.
2. **The helper's outcome rule was not applied evenly.** Its rule (SYNTHESIS.md line 44): "did not work" includes "wanted it and could not get it". The earlier readers marked 25 aide posts "wanted but couldn't get"; the helper coded only 6 of them as "did not work" and 17 as "no outcome". Applying the helper's own rule (this is a mechanical recode of the earlier status field, I did not reread them):

| Type | Helper W / M / N / none | Own rule applied W / M / N / none |
|---|---|---|
| Aide paid by family or payer not stated (84) | 12 / 17 / 5 / 50 | 12 / 17 / 19 / 36 |
| Aide paid by a program (41) | 6 / 11 / 8 / 16 | 6 / 11 / 11 / 13 |
| Agency (19) | 1 / 5 / 7 / 6 | no change |
| Therapist (123) | 27 / 10 / 20 / 66 | 27 / 10 / 23 / 63 |

Agency, respite worker and couples counts were not blind-rechecked (not in my 90-post sample).

---

## Check 4. Verdicts

HOLD = count and conclusion stand. HOLD WITH CORRECTIONS = the main conclusion stands, numbers change. FAIL = conclusion does not follow.

### Candidates (named businesses)

| Candidate | Helper's count / conclusion | Verdict | Corrected numbers | Confidence | 15+ independent reports? |
|---|---|---|---|---|---|
| Care.com | 82 posts, 52 independent, 18 users; include | HOLD WITH CORRECTIONS | 52 independent posts (33 asking, 18 users, 1 advice). 13 users say how it went (1 worked, 5 mixed, 7 did not). 5 users gave no result (4 only posted an ad or were about to hire). | High on counts, medium on outcomes | **Yes: 52 posts.** 13 with a result is under 15. |
| Visiting Angels | 22 real, 13 independent, 5 used; "no" as a brand | HOLD WITH CORRECTIONS | 22 real mentions, 13 independent, **4 used** (1 turned away), 2 worked. SYNTHESIS lines 8, 55, 97; jsonl line 52. | High | No: 13 |
| Home Instead | 12 real of 53, 8 independent, 4 used | HOLD WITH CORRECTIONS | 53 raw, 12 real, 8 independent, **3 had service, 1 not started** (SYNTHESIS lines 8, 54, 96; jsonl line 64) | High | No: 8 |
| Senior Helpers | 5 hits, 1 report | HOLD | 5 hits, 1 report | High | No: 1 |
| Right at Home | 4 hits, 2 reports | HOLD | same | High | No: 2 |
| Comfort Keepers | 1 hit, ad | HOLD | same | High | No: 0 |
| Papa | 9 hits, 1 report | HOLD | same | High | No: 1 |
| BetterHelp | 13 hits, 4 reports | HOLD | same (2 used, 2 priced it; one "use" is about selling data, no therapy result) | High | No: 4 |
| Talkspace | 2 hits, 1 ad | HOLD | UTM tags `paidsocial`, `grassroots` confirmed in text p1k2fdi8 | High | No: 0 |
| Headway | 8 hits, 0 real | HOLD | I read the 2 in my sample: both "make headway" | High | No: 0 |
| Psychology Today, SonderMind, Zencare | 1 each | HOLD | same | High | No: 1 each |
| Open Path | 0 | HOLD | 0 hits in 50,547 messages | High | No: 0 |
| **CareYaya** (not in helper's file) | "count unknown" | NEW | 9 posts: 6 asking, 0 users, 3 promotion | Medium | No: 6 |
| **A Place for Mom** (not in helper's Part A) | 1 post of 831; "not used for paid help" | FAIL to notice it | 31 posts across the corpus, about 20 in family voice, about 9 say they contacted it. A placement referral service, not relief. Snippet-level read only. | Low until read in full | **Probably yes (about 20)** |
| Wellthy, Torchlight, Lyra, Bayada, Amada | not counted | NEW, small | Wellthy 2 asking, Torchlight 1 asking, Lyra 1 user, Bayada 1 praise, Amada 1 complaint (writer unknown) | Medium | No |

### Types

| Type | Helper's count / conclusion | Verdict | Corrected numbers | Confidence | 15+ reports? |
|---|---|---|---|---|---|
| Aide paid by family | 84; 12 W / 17 M / 5 N / 50 none; include as workaround | HOLD WITH CORRECTIONS | Still 84 paid-aide posts (type right in 29 of 29). Payer named in only 27, so call it "aide, family-paid or payer not stated". Outcomes with own rule: 12 / 17 / 19 / 36. Blind outcome agreement 58%. | High on type, low on outcomes | Yes: 84 posts, 48 with a result after the recode |
| Aide paid by a program | 41; 6 / 11 / 8 / 16 | HOLD WITH CORRECTIONS | 41. Own rule: 6 / 11 / 11 / 13. Blind outcome agreement 46%, type 90% (97% after full reread). | Medium on type, low on outcomes | Yes: 41 |
| Home care agency (type) | 19; 1 / 5 / 7 / 6 | HOLD (counts only) | Not blind-rechecked. Count reproduces. | Medium | Yes: 19 (13 with a result) |
| Respite worker | 6 | HOLD (counts only) | Not blind-rechecked | Low | No: 6 |
| Therapist for the caregiver | 123; 27 / 10 / 20 / 66 | HOLD WITH CORRECTIONS | 123. Type 28 of 28. Own rule: 27 / 10 / 23 / 63. Outcome agreement 82%. | High on type, medium on outcomes | Yes: 123 (60 with a result) |
| Couples or family counseling | 6 | HOLD (counts only) | Not blind-rechecked | Low | No: 6 |
| "Almost no one names a business in the 831" | observed | HOLD | Welbe Health is one more name. | High | n/a |
| Care.com spouse/partner gap (1 of 52) | | HOLD | recomputed: parent 35, unclear 11, other relative 5, spouse 1 | High | n/a |

### Is the evidence enough to include each as a competitor in "help for worn-out caregivers"? (target 15 independent reports)

| Candidate | Independent reports that exist | Enough? |
|---|---|---|
| Care.com | 52 posts (13 with a result; 18 users) | **Yes** to include. Author-level independence cannot be proven (no author field). |
| Visiting Angels | 13 (4 users) | No as a named brand |
| Home Instead | 8 (3 had service) | No as a named brand |
| Senior Helpers / Right at Home / Comfort Keepers | 1 / 2 / 0 | No |
| Papa | 1 | No |
| BetterHelp | 4 | No |
| Talkspace, Headway, Open Path | 0 | No |
| Psychology Today, SonderMind, Zencare | 1 each | No |
| CareYaya | 6 asking, 0 users | No |
| Lyra, Wellthy, Torchlight | 1, 2, 1 | No |
| A Place for Mom | about 20 (snippet read) | Possibly. It needs a full read of those posts and a decision by the owner on whether placement referral counts as "help for worn-out caregivers." |
| Home care agency as one type | 19 (13 with a result) | Yes, as a type, not by brand |
| Ordinary therapist, program-paid aide, family-paid aide | 123 / 41 / 84 | Yes, as types |

---

## Corrections list (file and line)

| # | File and line | What it says | What it should say |
|---|---|---|---|
| 1 | `SYNTHESIS.md` lines 8, 55, 97; `MENTIONS-READ.jsonl` line 52 (p1724omw) | Visiting Angels "5 used it", outcomes W2 / N1 / none2 | 4 used. p1724omw was turned away by the agency; move it to label 2 ("tried, declined"). Users: W2 / none2. |
| 2 | `SYNTHESIS.md` lines 8, 54, 96; `MENTIONS-READ.jsonl` line 64 (p14ahwv3) | Home Instead "4 used it" | 3 had service. p14ahwv3's service "starts tomorrow." Move it to label 2. Users: M2 / N1. |
| 3 | `SYNTHESIS.md` lines 7, 254 (and 3.1) | Care.com "18 used it" with 5 "no result" | Add: 13 told how it went. Of the 5 with none, 4 had only posted an ad, were about to interview, or were still searching. |
| 4 | `SYNTHESIS.md` lines 11, 196, 204, 214, 219 | "Aide paid by the family (hired directly, or not named)", outcome 12 / 17 / 5 / 50 | Rename "aide, family-paid or payer not stated" (payer named in 27 of 84). With the helper's own rule: 12 / 17 / 19 / 36; "34 with a result" becomes 48. The A1/A2 outcome split on line 204 must be recomputed the same way. |
| 5 | `SYNTHESIS.md` lines 197, 205, 220 | Program-paid aide 6 / 11 / 8 / 16, "25 with a result" | 6 / 11 / 11 / 13, 28 with a result |
| 6 | `SYNTHESIS.md` lines 199, 207, 222 | Therapist 27 / 10 / 20 / 66, "57 with a result" | 27 / 10 / 23 / 63, 60 with a result |
| 7 | `SYNTHESIS.md` lines 131, 221 | Quote marks around `has anyone used it?` and `could not get one` | Remove the quote marks (they are the helper's wording) |
| 8 | `SYNTHESIS.md` line 136 | A Place For Mom: "1 post ... not used for paid help" | True for the 831 only. Across the corpus: 31 posts, about 20 in family voice. Mention it as a separate referral candidate. |
| 9 | `SYNTHESIS.md` lines 138, 274 | CareYaya, Lyra "counts unknown / not searched" | CareYaya 9 posts (6 asking, 0 users, 3 promotion), Lyra 1 user, Wellthy 2, Torchlight 1, Bayada 1, Amada 1. Add Welbe Health (p1m9ig5r) to Part B 4.1. |
| 10 | `SYNTHESIS.md` line 276 | "No second reader, no agreement score" | Now there is one: 98% label agreement on 40, 95% on outcome and who is cared for (this file). The 3 type outcome tables agree 46 to 82%. |

Not an error but worth saying: SYNTHESIS.md line 11 says "In the 831 relief posts, almost no one names a business." It holds. It should also say the 831 are the posts read earlier, not all posts, and that A Place for Mom and CareYaya are named often **outside** the 831.

---

## Evidence table (skeptical audit of my own claims)

| Claim | State | Source | Limit |
|---|---|---|---|
| 163 of 163 quotes are exact | proven | `check1_quotes.py` output | text only |
| Label agreement 98% (39/40) | observed | `check2_compare.py` | n = 40; not perfectly blind (see Check 2) |
| Care.com 82 / 132 / 105 / 52 reproduce | proven | `check3a_counts.py` | one regex |
| Visiting Angels 22 reproduces; 4 not 5 used | proven (22) / observed (4) | same; p1724omw read in full | |
| Home Instead 53 raw, 12 real, 41 phrase | proven / observed | same | |
| Types 84 / 41 / 19 / 6 / 123 / 6 and 185 / 139 / 298 reproduce | proven | `check3d_my_codes.py`, `check4_audience_blockers.py` | counts the file |
| Type precision 100 / 90 / 100% on 30-ish each | observed | `check3d_output.txt` | tests posts coded as the type, not posts missed |
| Outcome agreement 58 / 46 / 82% | observed | same | my codes are one reader; many outcomes are judgment calls |
| Family-paid payer named in 27 of 84 | proven | `payer_cost` field in `market-analysis-3/segments-11-12/codes/` | field was filled by the earlier reader |
| Own-rule recode N 19 / 11 / 23 | inferred | earlier readers' `status` field x `manual_codes.json` (`check3d_my_codes.py`) | I did not reread those posts |
| CareYaya 9 posts, 6 asking, 0 users | observed | `check3b_names.py` and context lines | Reddit posts only |
| A Place for Mom about 20 family posts | observed (snippets) | `check3b_hits` context | not read in full |
| 831 relief posts name almost no business | observed | `check3c_831.py` | name lists I chose |
| Audience counts (A1 58 / A2 16 etc.) reproduce | proven | `check4_audience_blockers.py` | uses `audience-labels.json` as given |
| Blocker counts (cost 14, reliability 9 ...) in 3.1 | inferred | free-text blockers in the jsonl, roughly match | free text, cannot recompute exactly |

## Not checked

- **Reddit comments.** Not in the data. People often name companies in replies. The independence and brand counts are posts only. (The helper said so too.)
- **Authors.** No author names anywhere. One person posting twice with different words cannot be found. So "independent" means "different post," not "different person."
- **Recall of types.** I tested whether posts coded as a type fit it. I did not test posts coded as something else (for example "in-home respite" or "family or friend") that also describe a paid aide or a therapist.
- **Agency (19), respite worker (6), couples (6) type counts.** Counts only, no blind sample.
- **Outcome rule for the remaining 54 aide posts and 95 therapist posts** I did not read.
- **The 424 relief posts the helper did not read for Part B**, and the Part B keyword rule counts (62, 41, 38 ... in 4.2 and 4.3). Not rerun.
- **Blocker tables** (cost / refuses / trust / rules / waitlist). Free text; my keyword recount only roughly matched.
- **A Place for Mom** full posts (snippets only), and whether placement referral belongs in this competitive analysis.
- **Real-world fact checks** (are these businesses still operating, Care.com fees, Papa Pals coverage). I did not use any web source; no robots.txt question came up.
- **Skills:** skeptical-audit applied. security-review, accessibility-check, judge-arch and the other code skills were judged not relevant (no code or UI of the product changed; scripts here are one-off audit scripts). data-lifecycle-compliance judged not relevant (all text is public posts already saved).
