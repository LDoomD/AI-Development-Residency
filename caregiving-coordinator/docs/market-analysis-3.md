# Market analysis updated with the Reddit research (2026-11-04)

Same content as the Figma section "UPDATED 2026-11-04 — MARKET ANALYSIS WITH THE NEW REDDIT RESEARCH" (market page, below the CURRENT SET; node `2598:10950`), plus the audience update (Audience page, node `2605:638`). The earlier versions are unchanged, and each has a SUPERSEDED sticky pointing to the new one.

**Method:** a random sample of 500 Reddit posts with no keyword filter (200 from r/CaregiverSupport, 200 from r/AgingParents, 100 from 11 other communities; seed 20261104; `build_sample.py`). It was coded with the same 14 themes as the forum research (`CODING-INSTRUCTIONS.md`, `codes/`). 412 posts were by caregivers. Every quote was checked word for word, and the counts come from `count_themes.py`, `other_groups.py` and `count_by_audience.py`. All numbers in the text were filled by `build_ma3.py`. The Figma text was hash-checked against the source.

## TOP PROBLEMS 3rd Version: all sources side by side (2026-11-04)

The Top four problems 2nd Version is unchanged. That version was built from forums, YouTube and papers, and said "Reddit was blocked." This version adds two kinds of Reddit research: (1) a random sample of 500 posts with no keyword filter, coded with the same 14 themes as the forum research, so the numbers can be compared (412 were written by caregivers), and (2) the 672 caregiver posts about tools and needs from 2026-11-03. Numbers read as main topic / mentioned anywhere. Not a ranking and not a choice: the owner picks the problem.

| Problem | Forums (117 caregiving threads) | Reddit random sample (412 caregiver posts) | Reddit posts about tools and needs (672) | App reviews and national data | What changed from the 2nd Version |
|---|---|---|---|---|---|
| 1. Burnout, guilt, isolation, grief | 23 (20%) / 50 (43%) | 102 (25%) / 210 (51%) | Doing it alone, family won't help 110; burnout with no one who understands 30; no respite 16 | Not a topic in app reviews. AARP/NAC 2025: 24% feel alone; 30% want help managing stress (p.53). Alzheimer's Association 2026: 59% of dementia caregivers report high emotional stress (p.55). | Confirmed as the top problem in every source. On Reddit it's the main topic of 1 in 4 posts and comes up in half. |
| 2. Money, accounts and legal papers | 10 (9%) / 39 (33%); logins or accounts in 17 | 32 (8%) / 117 (28%) | Getting into the parent's accounts 132 (banks refuse 46, lost passwords 32, codes to the parent's phone 22); documents and POA 97 (POA missing or rejected 29, papers scattered 22) | App reviews: access for another person 14 of 192 problem reviews. JMIR 2025: 49% of US adults have had digital proxy duties. AARP/NAC: 26% need help with paperwork (p.52). | Confirmed and stronger. Second most mentioned theme in the Reddit sample. The tool posts show the exact blocks: banks, passwords, sign-in codes, POA. |
| 3. Choosing, placing and paying for care | 11 (9%) / 35 (30%) | 29 (7%) / 90 (22%) | Not measured (the tool posts were sorted by 8 tool features) | Not a topic in app reviews. | Confirmed but a little lower. The old "biggest problem (21 sources)" came from the unsaved NotebookLM summary. Neither the forums nor the Reddit sample show it as biggest. |
| 4. Family coordination and siblings | 7 (6%) / 28 (24%) | 17 (4%) / 97 (24%) | Siblings won't share the work 63; information spread across chats, calendars and paper 32; updates lost or ignored in group chats 28 | App reviews: relatives can't see the same information 7 of 192. AARP/NAC: 53% have unpaid help (p.25). NHATS: about three quarters of older adults get help from one child. | Same pattern in both sources: rarely the main topic, but mentioned in 1 in 4. Reddit shows the core problem is siblings not helping, more than missing information. |
| 5. Dementia behavior and communication | 19 (16%) / 40 (34%) | 35 (8%) / 99 (24%) | Not measured | Alzheimer's Association 2026: 48% of caregivers of older adults care for someone with dementia (p.49). AARP/NAC: 12% want help with challenging behaviors (p.53). | Lower on Reddit than in the forums (one forum, ALZConnected, is a dementia community), but still mentioned in about 1 in 4 posts. Stays on the list. |
| 6. The person refuses help (NEW to this list) | 3 (3%) / 12 (10%) | 38 (9%) / 83 (20%) | Parent forgets or refuses medications 25; parent won't wear the alert device 11 | Competitor reviews: Lively is hard for the older person to use (13); Medical Guardian parents stop wearing it (5). | New. The second most common main topic among the named themes in the Reddit sample, much higher than in the forums. It also explains why tools fail: the parent won't use them. |
| 7. Medications | 8 (7%) / 19 (16%) | 8 (2%) / 55 (13%) | 77 posts (medication changes not shared 24; parent forgets or refuses 25) | App reviews: reminders failing 3 of 192. AARP/NAC: 55% do medical or nursing tasks, only 22% were trained (p.34). | Lower as a main topic on Reddit. When it comes up, the risk is changes not being shared (near double doses). |
| 8. Safety and knowing a parent is OK | 6 (5%) / 28 (24%) | 16 (4%) / 77 (19%) | 59 posts (no way to know the parent is OK 19; won't wear the device 11) | App reviews: wrong readings or location 43 and danger with the tool not helping 19, of 192 (mostly two apps the team chose). AARP/NAC: remote monitoring use rose from 13% to 25% (p.37). | Similar to the forums. Families want alerts to reach them. |
| 9. Doctors, appointments, records | 4 (3%) / 23 (20%) | 10 (2%) / 88 (21%) | 67 posts (too many portals or proxy blocked 25; doctors' offices don't share 16) | AARP/NAC: 64% talk with providers, only 58% find coordinating easy (p.35-36). | Similar: rarely the main topic, mentioned in about 1 in 5. |
| 10. Hands-on personal care, equipment and supplies (NEW) | Not a forum theme | 17 (4%) posts as main topic (found in Other) | Not measured | AARP/NAC: 55% do medical or nursing tasks, only 22% were trained (p.34). | New from Reddit: incontinence, bedbound hygiene, wound care, lifting, finding equipment and supplies. |
| 11. The caregiver's own life (job, money, health) | 1 (1%) / 30 (26%) | 20 (5%) / 113 (27%) | Not measured | Not a topic in app reviews. | Similar: rarely the main topic, but mentioned in about 1 in 4. |

WHO IS CARED FOR: Reddit sample: parent 269 (65%), other relative 68 (17%), spouse or partner 35 (8%), paid client 11 (3%), child 3 (1%), unclear 26 (6%) (of 412). Forums: parent 55, spouse or partner 54, other relative 5, unclear 3 (of 117). Reddit is mostly adult children caring for a parent. The forums were split because ALZConnected has many spouses.

OTHER PROBLEMS FOUND IN THE REDDIT SAMPLE (main topic, not in the 14 forum themes): hands-on personal care, equipment and supplies 17 (4%); technology the older person can't use or is misled by 9 (2%); end-of-life decisions and conversations 7 (2%); paid caregivers asking about their own work 7 (2%); sharing good moments 7 (2%); one-offs 20 (5%). Grouping: docs/sources/market-analysis-3/other-groups.json.

LIMITS: one reader coded each post once, and no person double-checked. The sample is posts only (no comments), mostly from r/CaregiverSupport and r/AgingParents (357 of 412). Reddit and forum writers choose to post and lean toward hard moments. Percentages from about 400 posts can move a few points by chance. Data: docs/sources/market-analysis-3/ (build_sample.py, CODING-INSTRUCTIONS.md, codes/, count_themes.py).

## UPDATED 2026-11-04 — MVP AND MMP SCORING 4th Version (adds Reddit evidence; no score changed)

The 3rd Version is unchanged. This version keeps every 3rd Version score as it was. The scores are the owner's judgment, so Claude doesn't change them. It adds what the Reddit research shows for each problem, and a note where that evidence might move a score, for the owner to decide. Three problems are added at the bottom from the Reddit sample and the market analysis short list. They're left unscored for the owner. Scoring method as before: Minimal, Valuable, Testable, Learnable.

| Candidate problem | Minimal | Valuable | Testable | Learnable | What Reddit adds (2026-11-04) | Could this move a score? (owner decides) |
|---|---|---|---|---|---|---|
| 1. Family members hold scattered, different information about the care | Medium | Medium | High | High | Family coordination, siblings 17 (4%) / 97 (24%). Tool posts: siblings won't share the work 63, information scattered 32, updates lost in group chats 28. | Maybe Valuable: the bigger Reddit signal is siblings not helping, not only scattered information. |
| 2. Family and doctors don't know which medicines are current | High | Medium | High | Medium | Medications 8 (2%) / 55 (13%). Tool posts: 77 (changes not shared 24). | No: still a small main topic. |
| 3. Not remembering what the doctor said and recommended | Medium | Medium | High | Medium | Doctors, appointments, records 10 (2%) / 88 (21%). Tool posts: doctors' offices don't share 16. | No. |
| 4. Access to accounts and records when the person who holds the login is unavailable | Low | High | Medium | Medium | Money, insurance, legal papers 32 (8%) / 117 (28%), the second most mentioned theme. Tool posts: 132 (banks refuse 46, lost passwords 32, codes to the parent's phone 22). | Supports the High Valuable score. Testable may still be Medium. |
| 5. Choosing and paying for care | Low | High | Low | Low | Choosing, placing and paying for care 29 (7%) / 90 (22%). | No: still real, but not the biggest need on Reddit. |
| 6. Burnout, guilt and exhaustion | Low | High | Low | Low | Burnout, guilt, isolation, grief 102 (25%) / 210 (51%), top again. Tool posts: doing it alone 110. | No: confirms High Valuable. |
| 7. Insurance, benefits and paperwork | Low | Medium | Low | Low | Counted inside money, insurance, legal papers 32 (8%) / 117 (28%). Tool posts: documents and POA 97. | Maybe Valuable: POA problems are concrete and common (29). |
| 8. Knowing a parent is safe when you're not there, and trusting the alert | Low | Medium | Low | Low | Safety 16 (4%) / 77 (19%). Tool posts: 59 (no way to know the parent is OK 19). | No. |
| 9. NEW: Dementia behavior and hard conversations (from the market analysis short list) | Owner to score | Owner to score | Owner to score | Owner to score | Dementia behavior and communication 35 (8%) / 99 (24%). Forums: 19 (16%) / 40 (34%). | New row for the owner. |
| 10. NEW: The person refuses help | Owner to score | Owner to score | Owner to score | Owner to score | Care recipient refuses help 38 (9%) / 83 (20%), the second most common main topic among the named themes. Tool posts: parent forgets or refuses medications 25, won't wear the device 11. | New row for the owner. |
| 11. NEW: Hands-on personal care, equipment and supplies | Owner to score | Owner to score | Owner to score | Owner to score | 17 (4%) posts as main topic (incontinence, bedbound care, wound care, lifting, supplies). | New row for the owner. |

## UPDATED 2026-11-04 — MARKET OPPORTUNITY 3rd Version (adds Reddit)

Copy of the Market Opportunity 2nd Version with one new column on the right: what the Reddit research adds for each segment. The 2nd Version is unchanged. The "Unmet need?" column still shows the first version's NotebookLM figures ("15 Reddit sources", "biggest problem (21 sources)"). Those sources were never saved, so use the new column instead. Effect: segment 4 (choosing and paying for care) is not the biggest need on Reddit. Burnout is (segments 11 and 12). Segment 10 (digital vaults) is supported more strongly than before: the parent's accounts and papers are the second most mentioned theme.

**What market segment has the largest opportunity? Why? (updated 2026-11-04, DRAFT for the owner)**

The template's three tests are: big enough, few competitors, and a need that isn't fully met. Here's what Reddit changes for each segment it touches.

• Segment 10, digital vaults and emergency access (the parent's accounts and papers): the unmet-need test is now passed more clearly than any other software segment. Money, insurance and legal papers is the second most mentioned theme (32 (8%) / 117 (28%)). In the tool posts, 132 are about getting into the parent's accounts (banks refuse the caregiver 46, lost passwords 32, codes go to the parent's phone 22). Competitive Analysis 2 shows no competitor covers banks or insurers, and MyChart proxy access is hard to get. Against: the size figure is for all password managers ($3.1B to $3.75B), not caregivers. Much of the block is bank and legal policy a family can't change. It has the highest security and liability risk.

• Segment 12, caregiver mental health and burnout: the biggest need in every source (102 (25%) / 210 (51%)), but it fails "few competitors" (Calm, Headspace and other general apps). On Reddit the problem is people not helping, not a missing app.

• Segment 1, family care-coordination apps: confidence stays LOW. Family coordination is the main topic of 17 (4%) / 97 (24%), about the same as the forums. The core complaint is siblings not helping (63 tool posts), and the competitors share news but don't get relatives to act. Caregivers rarely name these apps.

• Segment 4, choosing and paying for care: real (29 (7%) / 90 (22%)), but not the biggest need. The old "biggest problem (21 sources)" came from the unsaved NotebookLM summary. One fee-funded company still dominates.

• Segment 6, remote monitoring: the family side fails (Competitive Analysis 2: Lively works 36, problems 100), but the market is crowded and depends on devices.

Reading (Claude's, not a decision): by the three tests, segment 10 now has the strongest evidence of an unmet need among the software segments. Segment 12 has the biggest need but is crowded. Segment 1 stays low. The owner chooses.

## UPDATED 2026-11-04 — POSSIBLE MARKET SEGMENTS 3rd Version (adds Reddit) / UPDATED 2026-11-04 — MARKET SIZE 3rd Version (adds Reddit demand evidence)

Copy of the Possible Market Segments 2nd Version with one new column on the right: the matching Reddit theme for each segment. The 2nd Version is unchanged.
Copy of the Market Size 2nd Version with one new column on the right. The market sizes themselves do NOT change: Reddit says nothing about money. The new column only adds how often caregivers raise each segment's problem. The 2nd Version is unchanged.

The new column, by segment (the same text is used in the opportunity, segments and size tables):

- Segment 1: Family coordination, siblings: 17 (4%) / 97 (24%). Tool posts: siblings won't share the work 63, information scattered 32. Caregivers rarely name the coordination apps (Caring Village 3 posts).
- Segment 2: Medications: 8 (2%) / 55 (13%). Tool posts: 77 (changes not shared 24, parent forgets or refuses 25). App makers post a lot on this topic.
- Segment 3: Medications: 8 (2%) / 55 (13%). Packaging specifically was not checked.
- Segment 4: Choosing, placing and paying for care: 29 (7%) / 90 (22%). Not the biggest problem on Reddit; burnout is.
- Segment 5: Paid caregivers and agencies: 18 (4%) / 50 (12%). Plus 7 (2%) posts by paid caregivers about their own work.
- Segment 6: Safety: 16 (4%) / 77 (19%). Tool posts: 59 (no way to know the parent is OK 19; won't wear the device 11). Families want alerts to reach them.
- Segment 7: No matching theme. Closest: the caregiver's own life (job, money, health): 20 (5%) / 113 (27%). The buyer here is the employer.
- Segment 8: Doctors, appointments, records: 10 (2%) / 88 (21%). Visit notes specifically were not checked.
- Segment 9: Doctors, appointments, records: 10 (2%) / 88 (21%). Tool posts: too many portals or proxy blocked 25; MyChart is the competitor caregivers most often describe actually using (36 posts).
- Segment 10: Money, insurance, legal papers: 32 (8%) / 117 (28%). Tool posts: getting into the parent's accounts 132 (lost passwords 32, codes to the parent's phone 22); documents and POA 97.
- Segment 11: Burnout, guilt, isolation, grief: 102 (25%) / 210 (51%). Tool posts: no respite or breaks 16.
- Segment 12: Burnout, guilt, isolation, grief: 102 (25%) / 210 (51%), the top theme. Tool posts: doing it alone 110, burnout 30.
- Segment 13: No matching theme in the Reddit sample.
- Segment 14: Money, insurance, legal papers (includes insurance): 32 (8%) / 117 (28%). Tool posts: documents and POA 97.
- Segment 15: Same as segment 1: family coordination, siblings 17 (4%) / 97 (24%).

## UPDATED 2026-11-04 — MARKET ANALYSIS 3rd Version (one note corrected)

Copy of the Market Analysis 2nd Version. Only one note changed, in the senior care referral row: it said "Largest need in the Reddit research (21 of about 86 sources)". That figure came from the unsaved NotebookLM summary. The real Reddit sample shows choosing, placing and paying for care as the main topic of 29 (7%) / 90 (22%), behind burnout. Sizes, funding and every other cell are the same. The 2nd Version is unchanged.

## UPDATED 2026-11-04 — AUDIENCE EVIDENCE FROM REDDIT (adds to the audience segmentation and use cases; nothing removed)

Same 14 themes as the forum research, coded on a random sample of 500 Reddit posts (412 by caregivers). The audience boxes, labels, use cases and prioritization on this board are unchanged. This adds the Reddit numbers next to them so the owner can see where Reddit agrees or disagrees. Numbers read as main topic / mentioned anywhere.
The forum counts on the board look like 'mentioned anywhere' counts (23 of 55 = 42% matches burnout's 43% anywhere share), so they are compared with Reddit's 'anywhere' share.

GEOGRAPHIC
• Long-distance caregiving: 2 (0%) / 33 (8%) of Reddit caregiver posts (forums: 1 (1%) / 8 (7%) of 117). Both sources agree it's a small share.

BEHAVIORAL
• The person refuses help (won't accept aides, moving, doctors or devices): 38 (9%) / 83 (20%). Forums: 3 (3%) / 12 (10%). Much bigger on Reddit.
• Family coordination and siblings: 17 (4%) / 97 (24%). Forums: 7 (6%) / 28 (24%). Same share mentioned.
• Hands-on personal care (incontinence, bedbound care, wound care, supplies): 17 (4%) posts as main topic. Not a forum theme.
• Tools families name (672 Reddit posts about tools, 2026-11-03): group chats and texts, paper notebooks, calendars, spreadsheets and pill boxes come up far more than any caregiving app.

DEMOGRAPHIC
• Who is cared for (Reddit sample): parent 269 (65%), other relative 68 (17%), spouse or partner 35 (8%), paid client 11 (3%), child 3 (1%), unclear 26 (6%). Forums: parent 55, spouse or partner 54 of 117. Reddit is mostly adult children caring for a parent (Audience 1). Spouse posts (Audience 2) are a small share on Reddit.

SOCIOECONOMIC
• The caregiver's own life (job, money, health): 20 (5%) / 113 (27%). Forums: 1 (1%) / 30 (26%).
• Money, insurance and legal papers: 32 (8%) / 117 (28%). Forums: 10 (9%) / 39 (33%).

### AUDIENCE 1 (adult child caring for a parent): the use cases on this board, with Reddit added

| Use case on the board | Forum threads (of 55 parent threads, as on the board; % = count ÷ 55) | Reddit posts about a parent (269): main / anywhere | What Reddit shows |
|---|---|---|---|
| Exhaustion, guilt and no life of their own | 23 of 55 | Burnout 50 (19%) / 138 (51%); the caregiver's own life 15 (6%) / 72 (27%) | Forums 42%, Reddit 51% mention it. Top in both. |
| Dementia behavior and hard conversations | 14 of 55 | 27 (10%) / 72 (27%) | Forums 25%, Reddit 27%. Same. |
| Money, legal papers and facility bills | 11 of 55 | 21 (8%) / 86 (32%) | Forums 20%, Reddit 32%. Bigger on Reddit, and the second most mentioned theme for parents. |
| Relatives don't help, or block each other | 10 of 55 | 15 (6%) / 63 (23%) | Forums 18%, Reddit 23%. Similar. Rarely the main topic. |
| Medicines, eating and personal care | 8 of 55 | Medications 5 (2%) / 37 (14%); hands-on personal care as main topic 11 | Forums 15%; Reddit medications 14%. Similar. Hands-on personal care (incontinence, bedbound care, supplies) also shows up on its own. |
| Choosing and arranging a place for them | 6 of 55 | 24 (9%) / 68 (25%) | Forums 11%, Reddit 25%. Bigger on Reddit. |
| Staying safe at home | 6 of 55 | 11 (4%) / 57 (21%) | Forums 11%, Reddit 21%. Bigger on Reddit. |
| Getting answers from doctors and hospitals | 4 of 55 | 7 (3%) / 62 (23%) | Forums 7%, Reddit 23%. Much bigger on Reddit. |
| Being far away and not knowing what is happening | 2 of 55 | 2 (1%) / 29 (11%) | Forums 4%, Reddit 11%. Small in both. |
| NEW (not a use case on the board yet): The parent refuses help | Not a use case (forums: 3 of 117 threads as main topic) | 29 (11%) / 63 (23%) | New: after burnout, the most common main topic among the named themes in parent posts. Open for the owner to add as a use case. |

AUDIENCE 2 (spouse or partner): only 35 spouse posts in the Reddit sample, too few to rank use cases. Burnout is the main topic of 19 (54%) / 25 (71%).

LIMITS: one reader coded each post once, and no person double-checked. Posts only, no comments. The forum counts on the board came from a different reader and method, so compare the shares, not exact numbers. Data: caregiving-coordinator docs/sources/market-analysis-3/ (count_by_audience.py, reddit-sample-by-audience.json).

## UPDATED 2026-11-04 — AUDIENCES, MOTIVATIONS, GOALS AND USE CASES, WITH THE NEW REDDIT RESEARCH

Figma: Audience page (node 2378:7107), section 2605:638. Hash-checked. Data in docs/sources/market-analysis-3/goals/.

Everything on this page checked against the new Reddit research: a random sample of 500 Reddit posts (412 by caregivers). 269 are about a parent (Audience 1) and 35 are about a spouse or partner (Audience 2). Each post was coded with the same lists this page uses: the 14 problem themes, the motivations, situational goals and life goals, plus anything new. The boxes to the left are unchanged. Read the tables as forums versus Reddit. The Reddit readers marked more items per post than the forum readers, so compare the order (rank), not the exact percentages.

WHAT CHANGED, IN SHORT
AUDIENCES: still two. Audience 1 (adult child caring for a parent) is backed more strongly: 65% of Reddit caregiver posts are about a parent. Audience 2 (spouse or partner) has only 35 Reddit posts, so its changes are a signal, not proof.

AUDIENCE 1
• Motivations: the top two are the same: keeping the parent safe and comfortable first, avoiding blame or guilt second. Love, loyalty and promises moves up from #4 to #3. New: honoring the parent's wishes and making the time left count (5), and relieving the other parent who is the main caregiver (4).
• Situational goals: the order changed. "Understand what is happening and what to do" moves from #4 to #1 (71 of 269 posts). Money and legal affairs stays #3 but is close behind (46). Finding a place drops from #2 to #5. New: getting the parent to accept care and look after their own health (16), handling the parent's behavior (7), and technology for the parent (7).
• Life goals: the order flips. "Their own health and sanity" moves from #3 to #1 (72 posts), and "time and breaks" drops to #3. New: protecting their own marriage, children and family (9).
• Use cases: all 9 hold. Two candidates are open for the owner to add: the parent refuses help (29 main, 63 mentioned), and getting into a parent's accounts (added 2026-11-03). Money, choosing a place, doctors and safety come up more often on Reddit.

AUDIENCE 2 (small sample)
• Motivations: love, loyalty and promises moves to #1 (15 of 35).
• Situational goals: understanding what is happening and what to do shows up first (9 of 35). It isn't on this audience's board yet.
• Life goals: same order, and their own health and sanity is still first. New and large: companionship, intimacy and someone who understands (11 of 35).
• Use cases: exhaustion is still top. Dementia behavior is much lower on Reddit, because the forum spouses came mostly from a dementia community.


### Audience 1: adult child caring for a parent

AUDIENCE 1 LABEL AND TRAITS, added: on Reddit, 269 of 412 caregiver posts (65%) are about a parent, compared with 55 of 117 forum threads. Everything else in the label box stands.

**Motivations**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Keep them safe and comfortable, spare them suffering (on the board) | 7 (13%) | 60 (22%) | #1 → #1 |
| Do the right thing, avoid blame or guilt (on the board) | 6 (11%) | 30 (11%) | #2 → #2 |
| Love, loyalty and promises (on the board) | 3 (5%) | 23 (9%) | #4 → #3 |
| Keep them at home and in control of their own life (on the board) | 5 (9%) | 19 (7%) | #3 → #4 |
| NEW from Reddit: Honor their wishes and make the time left count | not on the board | 5 (2%) | new |
| NEW from Reddit: Relieve the other parent who is the main caregiver | not on the board | 4 (1%) | new |
| NEW from Reddit: I'm the only one, they need me | not on the board | 2 (1%) | new |
| NEW from Reddit: Preserve their life stories | not on the board | 2 (1%) | new |

**Situational goals**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Understand what is happening and what to do (on the board) | 2 (4%) | 71 (26%) | #4 → #1 |
| Get help, relief or services (on the board) | 11 (20%) | 47 (17%) | #1 → #2 |
| Manage money and legal affairs (on the board) | 3 (5%) | 46 (17%) | #3 → #3 |
| Keep them safe and watch over them (on the board) | 2 (4%) | 36 (13%) | #5 → #4 |
| Find, choose or pay for a place (on the board) | 6 (11%) | 31 (12%) | #2 → #5 |
| Medicines (on the board) | 1 (2%) | 19 (7%) | #6 → #6 |
| NEW from Reddit: Get the parent to accept care and look after their own health | not on the board | 16 (6%) | new |
| NEW from Reddit: Handle the parent's behavior and emotions | not on the board | 7 (3%) | new |
| NEW from Reddit: Technology and simple devices for the parent | not on the board | 7 (3%) | new |
| NEW from Reddit: End-of-life plans and wishes | not on the board | 5 (2%) | new |
| NEW from Reddit: Equipment, hygiene and hands-on care | not on the board | 5 (2%) | new |
| NEW from Reddit: Hold a facility to account and stay in touch with them | not on the board | 4 (1%) | new |
| NEW from Reddit: Family roles and costs | not on the board | 4 (1%) | new |

**Life goals**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Their own health and sanity (on the board) | 1 (2%) | 72 (27%) | #3 → #1 |
| Keep their own life, job and money (on the board) | 3 (5%) | 49 (18%) | #2 → #2 |
| Time and breaks for themselves (on the board) | 4 (7%) | 19 (7%) | #1 → #3 |
| NEW from Reddit: Protect their own marriage, children and family | not on the board | 9 (3%) | new |
| NEW from Reddit: Not be alone, and be seen | not on the board | 5 (2%) | new |
| NEW from Reddit: A life and a home after caregiving | not on the board | 4 (1%) | new |

**Use cases**

| Use case on the board | Forum threads (of 55 parent threads, as on the board; % = count ÷ 55) | Reddit posts about a parent (269): main / anywhere | What Reddit shows |
|---|---|---|---|
| Exhaustion, guilt and no life of their own | 23 of 55 | Burnout 50 (19%) / 138 (51%); the caregiver's own life 15 (6%) / 72 (27%) | Forums 42%, Reddit 51% mention it. Top in both. |
| Dementia behavior and hard conversations | 14 of 55 | 27 (10%) / 72 (27%) | Forums 25%, Reddit 27%. Same. |
| Money, legal papers and facility bills | 11 of 55 | 21 (8%) / 86 (32%) | Forums 20%, Reddit 32%. Bigger on Reddit, and the second most mentioned theme for parents. |
| Relatives don't help, or block each other | 10 of 55 | 15 (6%) / 63 (23%) | Forums 18%, Reddit 23%. Similar. Rarely the main topic. |
| Medicines, eating and personal care | 8 of 55 | Medications 5 (2%) / 37 (14%); hands-on personal care as main topic 11 | Forums 15%; Reddit medications 14%. Similar. Hands-on personal care (incontinence, bedbound care, supplies) also shows up on its own. |
| Choosing and arranging a place for them | 6 of 55 | 24 (9%) / 68 (25%) | Forums 11%, Reddit 25%. Bigger on Reddit. |
| Staying safe at home | 6 of 55 | 11 (4%) / 57 (21%) | Forums 11%, Reddit 21%. Bigger on Reddit. |
| Getting answers from doctors and hospitals | 4 of 55 | 7 (3%) / 62 (23%) | Forums 7%, Reddit 23%. Much bigger on Reddit. |
| Being far away and not knowing what is happening | 2 of 55 | 2 (1%) / 29 (11%) | Forums 4%, Reddit 11%. Small in both. |
| NEW (not a use case on the board yet): The parent refuses help | Not a use case (forums: 3 of 117 threads as main topic) | 29 (11%) / 63 (23%) | New: after burnout, the most common main topic among the named themes in parent posts. Open for the owner to add as a use case. |

### Audience 2: spouse or partner

AUDIENCE 2 LABEL AND TRAITS, added: on Reddit, 35 of 412 caregiver posts (8%) are about a spouse or partner, compared with 54 of 117 forum threads. That's too few to change the label. The traits from AARP and the forums stand.

**Motivations**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Love, loyalty and promises (on the board) | 9 (17%) | 15 (43%) | #2 → #1 |
| Keep them safe and comfortable, spare them suffering (on the board) | 11 (20%) | 3 (9%) | #1 → #2 |
| Do the right thing, avoid blame or guilt (on the board) | 1 (2%) | 0 (0%) | not seen on Reddit |
| Keep them at home and in control of their own life (on the board) | 4 (7%) | 0 (0%) | not seen on Reddit |

**Situational goals**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Understand what is happening and what to do (not on this audience's board) | not on the board | 9 (26%) | new → #1 |
| Get help, relief or services (on the board) | 6 (11%) | 5 (14%) | #2 → #2 |
| Manage money and legal affairs (not on this audience's board) | not on the board | 2 (6%) | new → #3 |
| Find, choose or pay for a place (on the board) | 7 (13%) | 1 (3%) | #1 → #4 |
| Keep them safe and watch over them (on the board) | 5 (9%) | 1 (3%) | #3 → #5 |
| Medicines (on the board) | 1 (2%) | 1 (3%) | #4 → #6 |

**Life goals**

| Item | Forum threads (count, % of the audience's threads) | Reddit posts (count, % of the audience's posts) | Rank: forums → Reddit |
|---|---|---|---|
| Their own health and sanity (on the board) | 7 (13%) | 15 (43%) | #1 → #1 |
| Keep their own life, job and money (on the board) | 4 (7%) | 9 (26%) | #2 → #2 |
| Time and breaks for themselves (on the board) | 2 (4%) | 4 (11%) | #3 → #3 |
| NEW from Reddit: Companionship, intimacy and someone who understands | not on the board | 11 (31%) | new |

**Use cases**

| Use case on the board | Forum threads (of 54 spouse threads, as on the board; % = count ÷ 54) | Reddit posts about a spouse (35): main / anywhere | What Reddit shows (small sample) |
|---|---|---|---|
| Exhaustion, loneliness and own health | 22 of 54 (41%) | Burnout 19 (54%) / 25 (71%); own life 3 (9%) / 16 (46%) | Top in both. |
| Dementia behavior and hard conversations | 18 of 54 (33%) | 1 (3%) / 4 (11%) | Much lower on Reddit. The forum spouses came mostly from a dementia community (ALZConnected). |
| Personal care and medicines | 12 of 54 (22%) | Medications 0 (0%) / 7 (20%) | Similar. |
| Safety when they are alone or out | 9 of 54 (17%) | 0 (0%) / 2 (6%) | Lower on Reddit. |
| Aides, hospice and trusting others | 8 of 54 (15%) | 1 (3%) / 3 (9%) | Similar or lower. |
| Placing them and care costs | 7 of 54 (13%) | 0 (0%) / 3 (9%) | Similar or lower. |
| Money, scams and bills | 6 of 54 (11%) | 2 (6%) / 10 (29%) | Higher on Reddit. |
| Diagnosis and doctor delays | 4 of 54 (7%) | 1 (3%) / 12 (34%) | Much higher on Reddit. |
| Relatives and others not helping or criticizing | 3 of 54 (6%) | 0 (0%) / 4 (11%) | Similar. |

LIMITS: one reader coded each post once, and no person double-checked. Posts only, no comments. The forum and Reddit readers differ, so compare order, not exact shares. Audience 2 has 35 Reddit posts. The 'NEW' groups are Claude's grouping of the readers' notes (docs/sources/market-analysis-3/goals/group_new.py). Data: docs/sources/market-analysis-3/goals/ (GOALS-INSTRUCTIONS.md, codes-1..3.json, count_goals.py, build_audience.py). Nothing on the page was chosen or removed; adding or moving anything is the owner's call.

---

## UPDATED 2026-11-04 — Segments 11 and 12 researched (respite and adult day; caregiver burnout support). Approved by the owner.

> **SUPERSEDED 2026-11-05:** corrected after an audit. Use the section "CORRECTED 2026-11-05 — Segments 11 and 12" at the end of this file.

Why: exhaustion is the #1 caregiver problem, and segments 11 and 12 had been sized and listed (Figma 2598:10950, 2026-11-01) but never studied from caregivers' own experience of relief. (Corrected 2026-11-05: an earlier version said they "had never been researched," based on older repo copies.) Market size note: the Figma board uses adult day care, $19.3B (Grand View); this update cites elderly respite, $374.1M (Coherent Market Insights). The scopes differ. Nothing above this section was changed. Full findings: `docs/market-analysis-segments-11-12-findings.md`. Inputs (every saved document on the topic, used or left out): `docs/market-analysis-segments-11-12-inputs.md`. Data: `docs/sources/market-analysis-3/segments-11-12/`.

**What was read:** 1,086 items in full: all 632 saved Reddit posts that mention respite or adult day, 115 posts naming programs and payers, random samples of 150 support-group and 150 therapist posts, and 39 forum threads. 831 were family caregivers writing about relief. Every quote was checked word for word by script.

| Segment | Who provides it (as caregivers name it, plus the earlier research) | What the research shows | Verdict |
|---|---|---|---|
| 11. Respite care and adult day services | Respite (in-home, facility, hospice), adult day programs, the VA (28 posts), Medicaid waivers (about 16), Medicare hospice respite, Area Agencies on Aging (10). From the earlier research: ARCH National Respite Network, Medicare GUIDE (respite up to $2,500 a year), Papa ($30 an hour). | 341 posts about respite: 128 used it, 78 wanted it and couldn't get it, 81 were still looking. 214 of 831 caregivers need a break and have no help. Barriers: cost 118, the parent refuses 96, family won't help 93, eligibility rules 86, rigid hours and minimum stays 59, waitlists 59, quality worries 52, guilt 38. AARP/NAC 2025: 39% say respite would help, 13% use it. Market size: elderly respite $374.1M in 2026 (Coherent Market Insights, free page). | **A real unmet need. The gap is access, not supply.** Help exists, but cost, eligibility rules, waitlists, rigid hours, the parent refusing and family not helping block it. |
| 12. Caregiver mental health and burnout support | Therapists and counselors, support groups, online communities (Reddit, Facebook groups, ALZConnected). Apps named in the segment: ianacare, Sanvello, Talkspace, Calm. | Therapy: 139 posts, 82 used it. Barriers: therapy doesn't help or isn't caregiver-aware 27, cost 16. Support groups: 114 posts, 49 used them; they help caregivers feel less alone, but 19 say no group fits. Burnout and meditation apps: 9 posts in 49,315 (BetterHelp 5, Calm app 2, Talkspace 2; several say they can't afford them). No dedicated market size found. | **The need is large, but "crowded" was wrong for caregivers.** Burnout apps are crowded in general, yet caregivers almost never use them. They rely on therapy, support groups and peer communities. |

**What this changes in the opportunity reading above:** segment 12 is no longer "the biggest need, but crowded." The biggest need is exhaustion, and its unmet part is access to relief (segment 11). Two of the three biggest barriers (the parent refusing, family not helping) are the same problems with no competitor coverage in Competitive Analysis 3 (criteria 4 and 5). Getting through VA and Medicaid applications (86 posts) links to segment 10 (accounts and papers) and to the who-pays research.

**Limits:** Reddit and forum writers aren't a random sample and lean toward people having a hard time. Counts are posts, not national rates. Respite types are combined because readers labeled them differently.

**By audience (added 2026-11-04, approved):** of the 831 relief posts, 486 are from adult children caring for a parent (Audience 1) and 98 from spouses or partners (Audience 2). The labels were checked; a 40-post spot check agreed 95%.

| | Audience 1 (486) | Audience 2 (98) |
|---|---|---|
| Need a break, no help in place | 25% | 30% |
| Respite, any type | 42% (79 used, 48 couldn't get it) | 35% (12 used, 9 couldn't get it) |
| Therapy for themselves / support groups | 17% / 12% | 26% / 22% |
| Top barriers | Cost 16%, the parent refuses 15%, family won't help 12% | Family won't help 12%, eligibility rules 10%, cost 8% (small numbers) |

Both audiences face the same access gap. Adult children are blocked most by cost and the parent refusing. Spouses are more often left with no help and lean on therapy and support groups. Details: `docs/market-analysis-segments-11-12-findings.md`, "split by audience."


---

## CORRECTED 2026-11-05 — Segments 11 and 12: how worn-out caregivers get a break, and what stops them

This replaces the 2026-11-04 section above. It was rechecked by 6 independent agents (`docs/reports/audit-2026-11-05-results.md`). The counts were recounted with a fixed rule (`docs/sources/market-analysis-3/segments-11-12/count_results.py`).

**What was read:** 1,086 caregiver posts and forum threads, read in full; 831 were from family caregivers writing about getting a break. A second reader re-read 50 of them without seeing the first answers and mostly agreed (49 of 50 on whether a post counts; 44 of 49 on what happened).

**Words used here:**
- **Respite:** a short break for the caregiver while someone else takes over the care, at home, at an adult day center, or in a short stay at a facility.
- **Adult day center:** a place where the parent spends the day with staff and activities.

| Segment | Who gives the help (programs caregivers name most) | What caregivers told us | What it means |
|---|---|---|---|
| 11. Respite care and adult day services | Medicaid and its waiver programs (77 posts), hospice (45), the VA (44), Area Agencies on Aging and local aging offices (26). Earlier research also found ARCH (a national directory of respite providers), Medicare GUIDE (pays up to $2,500 a year for respite for people with dementia), and Papa ($30 an hour). | Caregivers want breaks far more than they get them. Of 341 posts about respite, 128 had gotten a break, 78 wanted one but couldn't get it, and 81 were still trying. About a quarter of the 831 caregivers need a break and have no help at all. What stops them most: the cost (118 posts), the parent saying no (96), paperwork and rules to qualify (86; about 60 of these name the VA or Medicaid), and family who won't step in (83). Waitlists (59) and too few trained workers (38) also get in the way. | Help for worn-out caregivers exists, but many can't get it. The biggest blocks are cost, a parent who says no, paperwork and family who won't help. In some areas there also isn't enough help. This matches the national survey: 39% of caregivers say a break would help, but only 13% have ever used respite (AARP/NAC 2025, PDF pp.26-27). |
| 12. Caregiver mental health and burnout support | Therapists and counselors, support groups, and online caregiver groups (Reddit, Facebook groups, ALZConnected). | Caregivers almost never mention burnout or meditation apps (a handful of posts out of 49,315). Of 139 posts about a therapist, 82 had one; some say it doesn't help or they can't afford it. Of 114 posts about support groups, 49 went; groups help them feel less alone, but some can't find one that fits. | The need is large, but the apps that crowd this market don't reach caregivers. Caregivers get support from people: therapists, support groups and other caregivers online. |

**By audience** (486 posts from adult children caring for a parent; 98 from spouses or partners, a small number):

| | Adult children caring for a parent | Spouses or partners |
|---|---|---|
| Need a break and have no help | About 1 in 4 | About 1 in 4 |
| Got a break through respite | 79 of 486 posts | 12 of 98 posts |
| Go to support groups | 12% of posts | 22% of posts (a real difference) |
| What stops them most | The cost, the parent saying no, family who won't step in, paperwork and rules | Paperwork and rules (often the VA), family who won't step in, the cost, not finding reliable helpers |
| Programs named most | Medicaid, hospice, the VA | The VA |

**What changed from the 2026-11-04 version, and why:**
1. "Family won't help" dropped from 93 to 83 posts. The sorting rule had counted unrelated reasons.
2. The provider counts were too low (only exact names were counted). Medicaid, not the VA, is named most.
3. "The gap is access, not supply" was rewritten in plain words. It also leaves out that waitlists and too few workers matter in some areas.
4. "Spouses are more often left with no help (30% vs 25%)" was removed. On only 98 posts, that difference isn't real. The support group difference is real.
5. "Confirms AARP" became "matches the national survey," because online posts can't confirm a national rate.
6. The board's segment rows are dated "Researched 2026-11-01," inside sections dated 2026-11-04.

**Limits:** people who post online are often the ones having a hard time, so these numbers show patterns, not national rates. Each post was read by one reader; a second reader agreed on most points, but the reasons for not getting a break are less certain than the main counts.
