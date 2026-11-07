# A Place for Mom (APFM): independent audit, pass 3 (2026-11-06)

Auditor: a fresh reviewer who did none of the earlier work. Goal: try to prove the earlier files wrong.
Files audited: `EVIDENCE.md` (withdrawn by the owner), `PASS1-HOWWELL.md`, `PASS2-HOWWELL.md` in this folder.
Paths are under `docs/sources/` unless they start with `feature-analysis-4/`.

Rule I followed: I never fetched `aplaceformom.com` (its robots.txt blocks ClaudeBot; the owner deleted the 23 saved pages). Everything I say about what APFM's own site offers comes from third-party pages or from older saved pages under `competitors/a-place-for-mom/`. I also skipped Trustpilot, bbb.org (live), yelp, glassdoor, indeed, aginglifecare.org.

Conflicts I keep in view:
- AgingCare is owned by APFM. Its forum posts are flagged "AgingCare (APFM-owned)".
- ConsumerAffairs and BBB 5-star reviews may be invited by the company (not stated either way).
- SeniorLiving.org says it is "supported by commissions from providers", so it is not neutral.
- `elderlawms.com` (a law firm) republished an APFM-written article (it ends "Find this article online here" with an APFM link). I treat that text as APFM's own words, not independent.

Evidence states: proven, observed (I saw it myself), inferred, documented (a company or agency says it), reported (a person said it), not-assessed.

## Short answer (plain English)

- Quotes: no made-up quotes. All 86 PASS2 quotes, all PASS1 Reddit and BBB quotes, and the old-page quotes are in the cited saved files. The 12 quotes in the withdrawn `EVIDENCE.md` cite deleted pages, so nobody can re-check them (not-assessed).
- Counts: the arithmetic in both HOWWELL files is right (the totals add up to the rows). But several rows should not be counted the way they were (a non-user, a non-APFM service, a rule explained rather than lived, a survey follow-up). The big F1 numbers (27 + 25 worked) are mostly real but nearly half of the 25 new "worked" come from ConsumerAffairs reviews that may be invited.
- The claim "F2 settled as NO" does not hold. The family reports say APFM does not help with Medicaid placement (1 first-hand, 3 weaker). But APFM's own VA-benefits article says its "VA-accredited partners" help families with VA benefits, and APFM is paid if you use one. That is LIMITED, not NO.
- 12 corrections are listed below with file and line.

## Check 1: do the quotes exist in the cited files?

Command and script: see Appendix A (`quotecheck.py`; full text in `cariloop/AUDIT-PASS3.md`, Appendix A). Run: `python3 -I quotecheck.py a-place-for-mom/{EVIDENCE,PASS1-HOWWELL,PASS2-HOWWELL}.md`.

| File | Quotes tested | Found in cited file | Cited file missing | Not found | After hand checks |
|---|---|---|---|---|---|
| EVIDENCE.md | 13 | 1 (the BBB "lie" quote) | 12 (deleted APFM pages) | 0 | 12 not-assessed. The 1 found is exact. |
| PASS1-HOWWELL.md | 34 | 12 | 22 | 0 | The 22 rows had no file in the row. I tested them against the right file by hand: 15 BBB quotes in `competitors-4/review-sites/bbb_2026-11-04.txt` (all 15 found, exact), 6 old-page phrases in `competitors/a-place-for-mom/www_aplaceformom_com_.txt` and `..._about.txt` (all found), 1 fragment. |
| PASS2-HOWWELL.md | 92 | 86 | 6 | 0 | The 6 are search strings, not quotes. |

- State: observed. Limit: the script proves the words are in the saved file, not that the saved file matches the live page.
- Fabricated quotes: 0. Over the 20-word limit: 0.
- The helper's note in `PASS2-consumeraffairs-apfm-page1-2026-11-06.txt` says the ConsumerAffairs text is a "Firecrawl search excerpt", with "[...]" cuts. So the copy is partial.
- Other facts re-checked: BBB line "complaints closed past 3 years: 109 ... Customer reviews: 272, average 3.95 stars" is in the BBB save (observed). The BBB save heading says "most recent 10" for complaints and for reviews, but only 7 complaints and 8 reviews are in the file, so 15 is right as saved.
- Archive hits, my own recount: `place for mom|aplaceformom|apfm|a place 4 mom` = 33 Reddit posts + 1 forum file + 0 app reviews = 34 (matches). The "extra spellings: 3 new hits" in PASS1 line 106 does not reproduce: my wider pattern (`place ?for ?mom|place ?4 ?mom|placeformom`) adds only 1 new post (p1cr1bvr).
- YouTube: exactly 1 APFM comment ("I recommend the GUIDE Program and A Place for Mom for support"). My other file hit was a false match inside a comment ID.

## Check 2: recount, blind reclassification, double counting

### 2a. Arithmetic and structure (script `apfm_parse.py`, Appendix B)

Parsed all 86 rows of PASS2 and re-added by cell:
`F1 25 W / 37 D / 12 M; F2 0/4/0; F3 1/5/1; F4 0/1/0; F8 10/2/0; NONE 1 W + 1 D` and no duplicate comment IDs. These match the table in PASS2 lines 20 to 28. State: proven (script). Limit: it proves the table matches the rows, not that the rows are right.

By source, F1 new reports (before my corrections): Reddit 13 W / 26 D / 10 M; AgingCare (APFM-owned) 0/1/1; AlzConnected 0/4/0; ConsumerAffairs 12/6/1. So 12 of the 25 new "worked" are ConsumerAffairs.

### 2b. Blind reclassification of all 54 Reddit comments and 8 forum posts, plus the 15 randomly chosen items

I printed the raw comment text with no labels (`blind_win.py`), classified each, then compared. Limit: I had read the tables before, so I was not fully blind.

Random sample of 15 (seed 3, Python `random.sample` over all 86 IDs): A02, A09, A17, A25, A30, A31, A34, A48, A61, A70, A71, A75, A76, A78, A81.

| ID | My class from raw text | Earlier class | Agree? |
|---|---|---|---|
| A02 | F1 DID NOT WORK | same | Agree |
| A09 | F1 MIXED (called, went another way, calls stopped when told) | same | Agree (really "no verdict") |
| A17 | F1 WORKED (mild: "a spot to look up these different services") | same | Agree |
| A25 | MIXED, but writer does not clearly say they used APFM | F1 MIXED | Agree on class, own use unclear |
| A30 | F1 WORKED | same | Agree |
| A31 | F1 and F8 WORKED | same | Agree |
| A34 | F1 DID NOT WORK | same | Agree |
| A48 | F1 DID NOT WORK (pulled out; never got service) | same | Agree |
| A61 | F1 DID NOT WORK; F2 and F3: the Medicaid part is advice ("if your LO is going to be admitted as Medicaid...") not the writer's own case | F1, F2, F3 DNW | Disagree on F2 and F3 |
| A70 | F8: not guidance. "The follow up emails and text showed me that you really care" is an automatic follow-up | F8 WORKED | Disagree |
| A71 | F8: not guidance. "genuinely interested in my mother" is a feeling about staff | F8 WORKED | Disagree |
| A75 | F1 WORKED | same | Agree |
| A76 | F1 WORKED (cousin) | same | Agree |
| A78 | F8: weak. Check-in calls after placement | F8 WORKED | Partly agree |
| A81 | F1 DID NOT WORK, but the writer never got service (hung up at the contact-info wall) | same | Agree, with a note |

Result: 3 clear disagreements (A61 cells, A70, A71) and 1 partial (A78) in 15.

Disagreements from my full read of the Reddit and forum rows (not only the sample):

| ID | Problem | State |
|---|---|---|
| A03 (F4 DID NOT WORK) | Writer says "This is true, they will call and hound you about sending your loved one away." The writer does not say they used APFM. It is a general claim, so the F4 count rests on hearsay. | observed: PASS2 raw file, thread 17kp1k8, comment kk5m7hu |
| A19 (F1 MIXED, F3 MIXED) | "$60 an hour for 4 hours" for errand help. This sounds like a home-care service, not APFM placement. The helper's own note says "May mean home care". It should not count in F1 or F3. | observed |
| A38 (F2 DNW, F3 DNW) | "I just talked to someone from A Place for Mom yesterday... If you do not have the money to afford a place, they can't help you." This explains how APFM works. The writer does not say they were turned down. Class: no verdict. | observed |
| A42 (F1 DNW) | A resident of a 55+ community advertised on APFM. Not a user of APFM's service. Serious allegations not checked. | observed |
| A56 (F1 DNW) | AgingCare answer A2 says "you get to deal with dozens of phone calls". It is advice ("I would not recommend them"), the same kind of answer as A4, which the helper excluded as "advice only". Inconsistent. | observed |
| A55 (F1 MIXED) | The asker wrote "I used something like that here in VA". It is not clear the service was APFM. | observed |
| A62 (F2, F3 DNW) | "they don't deal with Medicaid" appears inside someone else's long answer (c86450) as a claim, not their own case (the helper flagged "may be general knowledge"). | observed |
| A50 (F3 only) | The same comment says half of the places visited came from APFM and the writer chose a Sunrise community: that is also an F1 WORKED. Missing from F1. | observed |
| A66 (F8 WORKED) | "I appreciate the follow-up and the opportunity to share our experience." That is a thank-you for a review invitation. Survey-bait. Do not count as F8. | observed |
| A52 | The Limit note says "Thread has users who suspect paid praise". Thread 1syq5ux has none (0 of 78 comments). The accusation appears in a different thread, 1kocgug. Also the wording ("it is free and they will help match you...") reads like an advert; the same thread has a promo for Oasis Senior Advisors. Possible promo, inferred. | observed |
| A10, A42, A19, A27 | "Other" voices (care worker, resident, older adult buying errands, a facility complaint). Counted as independent reports but are not family caregivers. | observed |

### 2c. Double counting

- A49 and A50 (thread 1ly7wn3) are probably one person. A50's parent comment is A48, which is a reply to A49. A50's story (placed a mother, APFM negotiated a Sunrise entry price) matches A49's. Inferred from the reply chain (script `chains.py`, Appendix B); usernames are not saved, so it cannot be proven. If merged, F1 W and F8 W each drop by 0 or 1 and F3 W 1 becomes unsupported by a second voice.
- A48 replies to A49 and is probably the original poster of the thread. Counted once. Fine.
- Pass 1 and pass 2 overlap: no comment ID repeats. The same thread appears in both passes (for example 1kocgug: pass 1 counted the post, pass 2 counted comments by other people). That is correct as long as the writers differ.
- `1kocgug` comments `mspeptr` and `mspeqku` have the same text (the "Do Not Represent Me Form" link). Only one was counted. Correct.
- Post p1cr1bvr is counted twice across companies: here (looked at APFM, got calls: F1 DNW) and in the care-manager file (a local "care advisor" that is not a care manager: separate table). That is a different entity each time, so it is not double counting.
- Pass 1 items that should not count: p1ijdg4c ("The psych ward told me to go to APlaceforMom.com for help, what a joke"; the post does not say the writer used APFM; the helper's own limit says "Unclear whether she actually used the site"). Also the YouTube comment ("I recommend... for support") is not an outcome.

### 2d. Vendor, staff, promo, survey-bait

- Excluded correctly: former APFM staff, rival advisers, the notaplaceformom.com campaign spam (about 20 identical comments in thread 1gzlutn), Facebook and YouTube items.
- Wrongly counted or doubtful: A52 (possible promo), A66 (survey-bait), A20 (a defender in a thread where others accuse defenders of being paid; it is cell-less, so it changes no F count), A10 (care worker).
- Thread 1gzlutn and 1ql34c8 were fetched at the 100-comment cap, so the comment lists there may be cut. Not an error, but a limit.

### 2e. My corrected F1 counts

I removed A19, A42, A56 from F1, added A50 as F1 W, and removed p1ijdg4c from pass 1.

| Group | Earlier (W/D/M) | Corrected (W/D/M) |
|---|---|---|
| Pass 2 new, all sources | 25 / 37 / 12 | 26 / 35 / 11 |
| Pass 1 | 2 / 12 / 1 | 2 / 11 / 1 |
| Combined | 27 / 49 / 13 | 28 / 46 / 12 |
| Of which Reddit and forums only (no BBB, no ConsumerAffairs) | not split | 14 / 34 / 10 |
| Of which ConsumerAffairs | 12 / 6 / 1 | 12 / 6 / 1 |
| Of which BBB | 2 / 6 / 1 | 2 / 6 / 1 |

Plain reading: if you take out the two sources a company can invite (BBB 5-star, ConsumerAffairs), the F1 split is 14 worked to 34 did not work. The failures are about calls and lists that leave out places, not about bad advice. The sample is biased: most Reddit threads here exist because someone is warning others or asking whether APFM is a scam.

Other corrected cells (my counts, first-hand only):

| Cell | Earlier combined (W/D/M) | Corrected | Why |
|---|---|---|---|
| F2 | 0 / 4 / 0 | 0 / 1 / 0 (A57) plus 3 weaker (A38 rule explained, A61 advice, A62 claim) | See 2b |
| F3 | 1 / 9 / 2 | 1 / 4 / 1 plus 4 weak D (p1fm6k24 says nothing about price; p1h0fxvm is about APFM articles; A61; A62) and 1 no-verdict | first-hand: A50 W; D: p1icxwp0, R6, A57, A84; M: p11zvnoj |
| F4 | 0 / 2 / 0 | 0 / 1 / 0 (BBB R8: told to lie) plus 1 weak (A03) | See 2b |
| F8 | 12 / 5 / 0 | 9 / 5 / 0 | Removed A66, A70, A71 (survey or feeling, not guidance). Kept A67, A78 (check-ins) |
| F5, F6, F9, F10 | 0 | 0 | I searched the 172 comments that name APFM (all raw files) for sibling, brother, sister, refus, bank, password, log in, support group, aggress, conversation: 16 hit a keyword and none is a first-hand report of APFM helping with siblings, accounts, behavior or support groups (one is an unrelated adviser in A04) |

I also searched all comments in the raw files for APFM mentions that were not counted: 111 not counted out of 171 total in the APFM and care-manager raw files. I read them. Almost all are hearsay, ads, staff, warnings or other services. A few are first-hand and uncounted (for example 1jlza79/mk90qa9, a possible repeat of A17). I found no large pile of missed real reports.

## Check 3: try to disprove

### 3a. The "F2 settled as NO" claim (PASS2 line 154)

| Search | Result |
|---|---|
| Firecrawl search: "A Place for Mom advisors help veterans Aid and Attendance benefits application" (aplaceformom.com, Trustpilot, bbb.org, yelp, glassdoor, indeed, aginglifecare, usatoday, yespress excluded) | 10 results. Several name APFM-linked VA partners. |
| Read `https://elderlawms.com/assisted-living-benefits-for-veterans-a-comprehensive-guide/` (law firm; page republishes an APFM article) | Says: "A Place for Mom's trusted, VA-accredited partners can help you and your loved one receive expert advice on veterans benefits. These include Elder Veterans Legal Aid Group, P.C. ... and Patriot Angels." And: "Note: A Place for Mom may be compensated if you choose to use Patriot Angels' services." Also "Accredited VA consultants can help families assess eligibility... regulations prohibit consultants from charging families for help with an initial claim that hasn't been denied." Observed 2026-11-06. State: documented (APFM-written text on a third-party site). |
| Read AgingCare thread 477637 (APFM-owned forum) | A user says "We used patriot angels to help obtain my moms Aid and Attendance VA pension... they basically tell you if you're going to be eligible or not before you actually pay them", $750. Another says "Don't pay someone to get VA Aid & Attendance. Your local VA Office will do the forms for free." Observed. State: reported; it is about Patriot Angels, not APFM staff. |

Conclusion: APFM refers families to paid partners who check VA eligibility and help apply. APFM itself does not file applications (no source says it does). For Medicaid, four sources say APFM does not help with Medicaid-only placement (1 first-hand, 3 weaker). So F2 is LIMITED (VA only, through a paid partner; no Medicaid help), not NO. State: inferred from documented and reported items. Confidence: low to medium.

### 3b. Other NO or inferred-NO cells

| Cell | What I searched | Found |
|---|---|---|
| F4 | The 171 comments, the BBB save, the seniorliving.org review | BBB R8 (told to lie, observed). seniorliving.org has a "refuses to go to assisted living" tip but it is SeniorLiving's own guide, not APFM's. APFM guides on refusing parents were recorded in the withdrawn `EVIDENCE.md`; I cannot re-check them. Cell stays VERIFY. |
| F5 | Same searches, plus "sibling" and "family members" | No feature, no report. Inferred NO. |
| F6 | Same, plus "bank", "account", "password" | Nothing. APFM is a placement service. Inferred NO. |

### 3c. YES-like cells: evidence it does not work or is not open to ordinary caregivers

- F1: respite and adult day. Read the SeniorLiving.org review (observed): "If your aging parent wants to age in place, A Place for Mom will also support you with guidance on adult day care and home care." So adult day gets guidance only. Respite: 1 report (A49: a respite placement failed and the specialist found another). Home care referrals: SeniorLiving.org says APFM is paid "when you hire a home care provider that you found through their network". So in-home breaks are covered through paid network agencies. Failures: the list can leave out non-profit and Medicaid places (A14, A22, A61, A80) and calls follow (20 of the 26 Reddit did-not-work reports mention calls, texts or spam in the raw text).
- F3: live check of the AgingCare page (observed 2026-11-06): "We do not charge you any fee – we are paid by the Participating Communities. Some Participating Communities pay us a percentage of the first month's standard rate." So free to families, but paid on placement. SeniorLiving.org says the site shows "average cost of these facilities in my location, how most people pay in my area".
- F8: "Support from first call to move-in" versus "and beyond" were in withdrawn pages; ConsumerAffairs reviewers mention check-ins after a stay (A67, A78) and one BBB reviewer thanks an adviser for advice on a spouse's move. Three reports say advisers stopped answering (p1d55k9e, BBB C3, C6).
- F10: the AgingCare forum (APFM-owned) is an active peer forum: the threads I read have 9 to 19 answers each (observed). That is a service of APFM's sister site, not of APFM's placement advisers.
- F9: "Have they experienced any of these behaviors?" is a question in APFM's intake quiz (SeniorLiving.org review and the AgingCare quiz). That helps match care level; it is not behavior help. Behavior articles were only in the withdrawn pages.

## Corrections list (errors in the earlier files)

| # | File and line | Error | Fix |
|---|---|---|---|
| A-1 | `PASS2-HOWWELL.md` line 154 and line 11 | "F2 Yes, no / settled as NO". Too strong. Evidence: 1 first-hand report (A57) and 3 weak ones; APFM's own VA article points to paid VA partners. | Change to LIMITED (VA via paid partner; no Medicaid help). |
| A-2 | `PASS2-HOWWELL.md` lines 73, 96, 97 (A38, A61, A62) | A38 is a rule explained, A61's Medicaid part is advice, A62 is a claim. All counted as F2/F3 DID NOT WORK. | Keep A57 only as first-hand F2. |
| A-3 | `PASS2-HOWWELL.md` line 38 (A03) | F4 count rests on a writer who does not say they used APFM. | Mark "hearsay" and do not count. |
| A-4 | `PASS2-HOWWELL.md` line 54 (A19) | Probably not APFM placement. | Remove from F1 and F3 or mark "unknown service". |
| A-5 | `PASS2-HOWWELL.md` line 77 (A42) | Resident, not a user. | Remove from F1. |
| A-6 | `PASS2-HOWWELL.md` line 91 (A56) and line 90 (A55) | A56 is advice, A55 may not be APFM. Inconsistent with excluding A4/A5. | Remove A56; mark A55 uncertain. |
| A-7 | `PASS2-HOWWELL.md` line 85 (A50) | Missing F1 WORKED. | Add F1 WORKED. |
| A-8 | `PASS2-HOWWELL.md` lines 101, 105, 106 (A66, A70, A71) and line 14, 158 | Survey thank-you and warm-feeling reviews counted as F8 WORKED. Summary says "10 WORKED (mostly ConsumerAffairs follow-up check-ins)". | F8 W becomes 7 new (9 combined). |
| A-9 | `PASS2-HOWWELL.md` line 87 (A52) | Limit note "Thread has users who suspect paid praise" is wrong for thread 1syq5ux. Comment may itself be promo. | Fix note; flag possible promo. |
| A-10 | `PASS2-HOWWELL.md` lines 9, 20 | A49 and A50 are probably one writer (reply chain). | Add note; count once or flag. |
| A-11 | `PASS1-HOWWELL.md` line 42 (p1ijdg4c) and line 40 (p1j1vrmx) | p1ijdg4c: no evidence the writer used APFM (helper's own limit says so). p1j1vrmx: "far better than the help we got" with no APFM detail; weak. | Remove p1ijdg4c; mark p1j1vrmx weak. |
| A-12 | `PASS1-HOWWELL.md` line 106 | "extra spellings: 3 new hits" does not reproduce (I get 1). | Correct or show the pattern. |
| A-13 | `PASS2-HOWWELL.md` lines 9 and 20 (the "25 worked") | Does not say that 12 of the 25 new worked are ConsumerAffairs reviews that may be invited, and that Reddit-only is 13 W / 26 D / 10 M. | Split by source. |
| A-14 | `PASS2-agingcare-forum-question-448978-2026-11-06.txt` header vs. md | Not an error in numbers; note that the file labels A4 "advice" and the md counts A2 (same kind) as a report. | See A-6. |
| A-15 | `EVIDENCE.md` lines 9 to 20 | Table keeps 12 quotes from deleted pages, with verdicts YES. Banner says withdrawn (good), but the "Differs from Figma" section (lines 30 to 34) still tells the reader to mark F4 YES and says F9 and F10 are covered. | Strike or mark "withdrawn" in that section too. |

Error count for APFM: Check 1: 0 fabricated quotes, 12 unverifiable (withdrawn) quotes, 1 non-reproducing search count (A-12). Check 2: 11 rows miscounted or doubtful (A-2 to A-9, A-11, plus A-10 probable repeat), 1 missing F1 credit (A-7). Check 3: 1 conclusion that does not hold (A-1), 1 wrong Limit note (A-9).

## Final verdict table (A Place for Mom)

Reports = my corrected first-hand family or user reports (worked / did not work / mixed). All are reported, not observed. No independent documented evaluation of APFM exists in the saved files. SeniorLiving.org rates APFM 4.5 of 5 but earns commissions from providers (not independent).

| Cell | Verdict | Confidence | Reports (W/D/M) | Plain reason | Earlier helpers | Differs from Figma? |
|---|---|---|---|---|---|---|
| F1 Relief finder | LIMITED: finds senior living, home care agencies, a respite stay (1 report); adult day gets guidance only; lists can miss non-profit and Medicaid places; calls follow | medium | 28 / 46 / 12 (Reddit and forums only: 14 / 34 / 10; ConsumerAffairs 12 / 6 / 1; BBB 2 / 6 / 1) | It works for shortlists and tours; it fails on sales calls and incomplete lists. Relief (respite, adult day) is not its focus. | "VERIFY, partly settled; Yes, mixed". Mostly agree. | Figma "Partly" agrees. |
| F2 Eligibility and applications | LIMITED: VA benefits through paid partners (APFM may be paid); no Medicaid help; APFM does not file | low to medium | 0 / 1 / 0 (plus 3 weaker D) | APFM refers to VA-accredited partners, but says nothing about doing applications; Medicaid families are turned away. | "Settled as NO". I disagree. | Figma has no F2 cell for APFM. Its F3 note "no help for Medicaid-only" agrees with the reports. |
| F3 Paying for relief | LIMITED: free to families, cost pages and a calculator (old home page, documented), paid by the place on move-in; no help for people who need Medicaid | medium | 1 / 4 / 1 | Costs are shown; paying help is limited to VA partners; commission steers choices. | "Partly". Agree. | Figma "Partly". Agree. |
| F4 Refusing parent support | VERIFY (leans: advisers press to move the parent; no coaching shown) | low | 0 / 1 / 0 (+1 weak) | The only solid report is an adviser said to lie to the parent. Guide pages were in the withdrawn save. | "complaint on record only". Agree. | Figma "No: an advisor told one family to lie". The BBB quote is real (1 review). "No" is not proven. |
| F5 Relatives cover time | NO (inferred) | low to medium | 0 / 0 / 0 | No feature or report found; APFM is one family contact. | VERIFY. I lean NO. | Figma "No". Agree. |
| F6 Account access | NO (inferred) | medium | 0 / 0 / 0 | Not what a placement service does; nothing found. | VERIFY. I lean NO. | Not in Figma for APFM. |
| F8 Personal guidance | LIMITED: a free adviser through the move; check-ins after a stay in some reviews; not an ongoing coach; paid on placement | medium | 9 / 5 / 0 | Some families got kind, responsive help; others got no reply or a sales push. | "Partly". Agree. | Figma "Partly". Agree. |
| F9 Behavior and hard talks help | VERIFY | low | 0 / 0 / 0 | Articles only (in withdrawn pages); the intake quiz asks about behaviors to match care level. No reports. | VERIFY. Agree. | Not in Figma. |
| F10 People who understand | LIMITED: through AgingCare forum (owned by APFM), not APFM's own service | low | 0 / 0 / 0 | The forum is active; the placement adviser does not connect you to peers. | VERIFY. Close. | Not in Figma. |

Cells where I disagree with the earlier helpers: F2 (their "NO" becomes LIMITED). Cells where the earlier work and I agree but the numbers changed: F1, F3, F8. Where the evidence differs from Figma: F4 ("No" is a reading of one review), F2.

## Not checked

- `aplaceformom.com` itself (rule). So the F4, F9, F10 article claims and F8 "move-in" wording from the withdrawn save are not re-checked.
- The APFM-written VA PDF linked from elderlawms.com (not opened; it lives on aplaceformom.com).
- ConsumerAffairs pages beyond the first 35 reviews; whether APFM invited those reviewers; BBB live pages (skipped); Trustpilot (rule).
- The Senate probe, Washington Post, Senior Housing News items; Facebook and YouTube items.
- Whether any commenter is paid by APFM or a rival.
- Keyword search of Reddit for "place for mom" (timeouts; I did not rerun).
- Same-person checks across the 86 rows (usernames not saved; only reply chains used).

## Appendix B: scripts (run 2026-11-06)

`apfm_parse.py`, `chains.py`, `blind_win.py` are small helpers I wrote in my scratch folder:
- `apfm_parse.py` reads the PASS2 table rows, pulls each "cells (class)" string and the `thread X, comment Y` ids, then re-adds the counts by cell and by source (`python3 -I apfm_parse.py`). Output: `86 rows; F1 {MIXED 12, DID NOT WORK 37, WORKED 25}; F2 {DNW 4}; F3 {M 1, DNW 5, W 1}; F4 {DNW 1}; F8 {DNW 2, W 10}; NONE {W 1, DNW 1}; dup comment ids []; Reddit 54, ConsumerAffairs 24, AlzConnected 5, AgingCare 3`.
- `chains.py` lists counted comments whose parent comment is also counted (reply chains). Output: `chain: A48 replies to A49 (thread 1ly7wn3); chain: A50 replies to A48 (thread 1ly7wn3); chains 2`.
- `blind_win.py` prints raw comment text around the first "place for mom" mention with the earlier labels hidden.

The quote-check script is the same `quotecheck.py` printed in full in `cariloop/AUDIT-PASS3.md`, Appendix A.
