# A Place for Mom: how well do the features work for families? (PASS 1, saved data only)

Date: 2026-11-06. No website was scraped. Paths are under `docs/sources/` unless they start with `feature-analysis-4/`. States: every count is **reported** (a person said it). The site pages were withdrawn by the owner, so capability for most cells is VERIFY. I used only the Reddit file, the full saved archive and forums, the BBB save, and the older saved pages in `competitors/a-place-for-mom/`.

## Short answer

- Independent reports found: **27** (11 Reddit/forum reports, 15 BBB excerpts, 1 YouTube comment). Reddit and forums had 34 raw hits (33 Reddit, 1 forum); only 11 describe real use. The rest are warnings from hearsay, news, vendors or the plain words "place for mom".
- BBB total is 109 complaints and 272 reviews, but only **15 excerpts** are saved (7 complaints, 8 reviews). I counted all 15 and no more.
- Finding places (F1): 2 WORKED, 12 DID NOT WORK, 1 MIXED. Almost all failures are about phone calls and sharing contact details, not about bad places.
- Parent who refuses (F4): only 1 report (BBB: advisor said to lie). Advisor guidance (F8): 2 WORKED, 3 DID NOT WORK.
- Costs (F3): 0 WORKED, 4 DID NOT WORK, 1 MIXED, 1 USED NO VERDICT. A Medicaid-only family says APFM cannot help.

## (a) Table: one row per cell

| Cell | Capability (EVIDENCE.md) | WORKED | DID NOT WORK | MIXED | USED, NO VERDICT | Total reports |
|---|---|---|---|---|---|---|
| F1 Relief finder | VERIFY (pages withdrawn) | 2 | 12 | 1 | 0 | 15 |
| F2 Eligibility and applications | VERIFY | 0 | 0 | 0 | 0 | 0 |
| F3 Paying for relief | VERIFY (pages withdrawn) | 0 | 4 | 1 | 1 | 6 |
| F4 Refusing parent support | complaint on record only | 0 | 1 | 0 | 0 | 1 |
| F5 Relatives cover time | VERIFY | 0 | 0 | 0 | 0 | 0 |
| F6 Account access | VERIFY | 0 | 0 | 0 | 0 | 0 |
| F8 Personal guidance | VERIFY (pages withdrawn) | 2 | 3 | 0 | 0 | 5 |
| F9 Behavior and hard talks help | VERIFY (pages withdrawn) | 0 | 0 | 0 | 0 | 0 |
| F10 People who understand | VERIFY (pages withdrawn) | 0 | 0 | 0 | 0 | 0 |

The YouTube comment (WORKED, "for support") and BBB C5 (opt-out complaint) fit no cell and are in the total only. A report that names two cells (F1+F3, F1+F8) is counted once in each cell. Unique reports = 27.

## (b) The reports behind each count

### Reddit and forum reports (all read in full around the match)

| Post id | Cell | Class | Quote (exact, max 20 words) | Audience | Source file and link | Limit |
|---|---|---|---|---|---|---|
| p17kp1k8 | F1 | DID NOT WORK | "my phone has been ringing off the hook with cold calls ever since" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/17kp1k8/ | Poster wanted only information; says contact info went to every facility. |
| p1d55k9e | F8 | DID NOT WORK | "when you actually need their help will not respond to your call, emails nothing" | unclear | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1d55k9e/ | Short rant; no detail on what help was needed. |
| p1icxwp0 | F1+F3 | DID NOT WORK | "they cannot help. They only deal in private pay." | unclear (loved one on Medicaid) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1icxwp0/ | Counted in two cells (F1 and F3), one report. |
| p1kocgug | F1 | DID NOT WORK | "They will call and email you nonstop for YEARS." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1kocgug/ | Says they found a place on their own. |
| p1fm6k24 | F3 | DID NOT WORK | "They have since inundated me with scammy sounding phone calls." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1fm6k24/ | Poster wanted a cost idea; post does not say whether a price was given. |
| p1j1vrmx | F1 | DID NOT WORK | "This was far better than the help we got from A Place for Mom" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1j1vrmx/ | Compares county ombudsman list with APFM help; no APFM details. |
| p1cr1bvr | F1 | DID NOT WORK | "I looked at a placeformom and now I’m getting non-stop calls from random numbers." | unclear | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1cr1bvr/ | Found only by a second search (spelling "placeformom"). |
| p1ijdg4c | F1 | DID NOT WORK | "The psych ward told me to go to APlaceforMom.com for help, what a joke" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1ijdg4c/ | Unclear whether she actually used the site. |
| p11zvnoj | F3 | MIXED | "i see some listings with real prices, so that's a start" | unclear | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/11zvnoj/ | Also: had to give name, phone and email to see listings; calls them "spammy". |
| p1h0fxvm | F3 | DID NOT WORK | "very little information on the process that wasn't SEO content from A Place For Mom" | adult child (grandparent) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1h0fxvm/ | About APFM articles on the nursing home/Medicaid process, not about advisors. Pages are withdrawn, so cannot re-check. |
| 77373.txt | F3 | USED, NO VERDICT | "This representative was quoting me much lower rates" | unclear | docs/sources/forums/alzconnected/discussions-recent/77373.txt  | Poster calls the lower quotes "suspicious" and asks others; she does not say they were wrong. |

### BBB excerpts (`docs/sources/competitors-4/review-sites/bbb_2026-11-04.txt`)

| Item | Cell | Class | Quote (exact) | Audience | Limit |
|---|---|---|---|---|---|
| C1 | F1 | DID NOT WORK | "distributed my phone number and email to every assisted living facility in my area without my consent" | unclear | BBB complaint excerpt |
| C2 | F1 | DID NOT WORK | "I was inundated with emails, texts, and calls from assisted living facilities" | unclear | BBB complaint excerpt |
| C3 | F8 | DID NOT WORK | "it was clear this is a commission-based enterprise and he wasn't there to help me at all" | unclear | BBB complaint excerpt |
| C4 | F1 | DID NOT WORK | "proceeded to contact some local nursing homes and list me as a referral from them" | unclear | BBB complaint excerpt |
| C5 | none (privacy) | DID NOT WORK | "remove my contact info and delete my contact information from their call list. I am still receiving calls" | unclear | BBB complaint excerpt; about opt-out, not a feature cell. |
| C6 | F8 | DID NOT WORK | "They took my information but never responded to my calls, voicemails, or text messages." | unclear | BBB complaint excerpt |
| C7 | F1 | DID NOT WORK | "I begin receiving up to 12 phone calls a day from this company." | unclear | BBB complaint excerpt |
| R1 | F1 | WORKED | "figure out the process of finding a place for mom when I had no idea of where to even start" | unclear | BBB 5-star excerpt; reviewers are invited by the company in some cases (not known here). |
| R2 | F1+F8 | WORKED | "the setting up of appointments and all the knowledge that she passed on to me" | unclear | BBB 5-star excerpt |
| R3 | F8 | WORKED | "the help and guidance and the advice on coping with my wife's move" | spouse | BBB 5-star excerpt |
| R4 | F1 | MIXED | "The places that you suggested for assisted living was a great help" | unclear | BBB 4-star: also says a "home assist" referral caused "an avalanche of unwanted texts and emails". |
| R5 | F1 | DID NOT WORK | "they send my name to entire area facility without my knowledge" | unclear | BBB 1-star excerpt |
| R6 | F3 | DID NOT WORK | "the place they came up with was 1000 dollars more then if u find them yourself" | unclear | BBB 1-star excerpt; also says pushy about selling mom's house. |
| R7 | F1 | DID NOT WORK | "high pressure tactics, nonstop phone calls" | unclear | BBB 1-star excerpt |
| R8 | F4 | DID NOT WORK | "Told me the best way to get our mother in a nursing home is to just lie to her" | adult child | BBB 1-star excerpt |

### YouTube comment (outside Reddit)

| p8sRNKTGj9g comment | unclear feature | WORKED | "I recommend the GUIDE Program and A Place for Mom for support." | adult child (caring for two parents) | YouTube comment, not Reddit; "for support" is not tied to one cell. (`docs/sources/youtube/comments-raw/p8sRNKTGj9g/comments-p2.json`) |

### Read but NOT counted (name only, hearsay, vendor, news, or not APFM)

- p1hl0pzj: says APFM charges the community a referral fee (a claim, no use).
- p1htr11h: opinion, first-hand use unclear.
- p1d89242: hearsay ("I hear a place for mom is no good").
- p1eg5z09: social worker, "I've since found out has been exploitative" (no use).
- p1i7ldvl: hearsay ("saw so many posts bashing them").
- p1nw7z5i: hearsay ("I hear they both hound you").
- p1qhihlw: "I heard the horror stories"; asks how to stop calls (no use stated).
- p1l8ln29: hearsay "commission based".
- p1dj429j: news about a US Senate probe (neutral, not a feature).
- p1bvdp2t: gave brother's number to spam him (mention).
- p1fhdu59: asks about APFM (mention).
- p1pwakzb: list post (mention).
- p1f1s43u: lists APFM as a resource (mention).
- p1jlza79: joke about the ad.
- p1lpjcio: asks how families find places (mention).
- p1emgwx5: plans to call APFM (future).
- p1i1hskc: VENDOR: builds a rival free database.
- p1cwnaxy: post removed, no text.
- p10h6p87: plain words "a place for mom", not APFM.
- p1f3x2no: plain words, not APFM.
- p1aqo1wy: plain words, a placement coordinator, not APFM.
- p1r7efxq: plain words, not APFM.
- p1gwnggo: plain words, not APFM.
- p1cgw0j9: plain words, not APFM.

## (c) Search filters and raw hits

| Filter | Raw hits |
|---|---|
| `place for mom|aplaceformom|APFM|a place 4 mom` in Reddit (49,315 posts), forums (142 threads), app reviews (17,956 rows) | 34 |
|    of which Reddit | 33 |
|    of which forum (alzconnected 77373.txt) | 1 |
|    of which app reviews | 0 |
| extra spellings `place ?for ?mom|place ?4 ?mom|placeformom` (new hits beyond the first filter) | 3 |
|    of which real APFM use (p1cr1bvr) | 1 |
| `place for mom` in the feature-analysis-4 Reddit file (headers starting `--- p`) | 33 |
| YouTube comments file, `place for mom` | 1 |
| BBB save, A Place For Mom section | 15 excerpts (7 complaints, 8 reviews) |

I also searched Reddit text for `refus` near APFM names: 0 posts tie APFM to a refusing parent.

## (d) Cells that are VERIFY: does the saved data settle them?

The older saved pages (`competitors/a-place-for-mom/www_aplaceformom_com_.txt` home page and `..._about.txt`, saved 2026-11-01) are allowed and still on disk. State **documented** (company text, not independent).

| Cell | Settled? | Evidence (state) |
|---|---|---|
| F1 Relief finder | Partly | Home page: "Connect with a local expert"; About: "finding senior living and home care through free, personalized guidance from our national network of advisors" (documented). Reported: 2 BBB reviews say advisors helped find places. Respite, adult day: not named on these pages (0 hits for the words) so respite stays VERIFY. |
| F3 Paying for relief | Yes for costs and paying (documented) | Home page: "Try our senior living cost calculator" and "Learn how to pay for care including using Veterans benefits, and more". Reported: 1 Reddit user saw "real prices" after giving contact details. Price of respite: not on these pages. |
| F8 Personal guidance | Partly | About: "free, personalized support from senior living and home care advisors" (documented). Whether support lasts after move-in is still not settled. Reported: 1 BBB review thanks an advisor for advice on a wife's move; 3 reports say advisors did not help or did not respond. |
| F4 Refusing parent support | No | Older pages have 0 hits for "refus" or "resist". Only the BBB complaint (reported). Stays VERIFY, complaint on record. |
| F2, F5, F6, F9 | No | Not in the older pages (0 hits for Medicaid, sibling, respite, refuse). 0 independent reports. Stay VERIFY. |
| F10 People who understand | No | The home page only has a testimonial that mentions "a caregivers' support group" (about a community, not an APFM feature). Stays VERIFY. |

## (e) Not checked

- Trustpilot, Consumer Affairs, Yelp, Google reviews, Senate probe report: not saved. BBB has 109 complaints and 272 reviews; 257 are unread because only 15 excerpts are saved.
- Reddit comments (not saved for most posts). Replies to the warning posts could hold many more first-hand reports.
- F2, F5, F6, F9, F10 for APFM: no search done for these cells in this pass, only F1, F3, F4, F8.
- Whether BBB 5-star reviews were solicited by the company: unknown.
- Respite or adult day through APFM: 0 reports and 0 page text.
