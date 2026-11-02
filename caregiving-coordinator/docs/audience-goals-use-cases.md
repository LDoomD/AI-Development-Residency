# Audience labels, motivations, goals and use cases (3rd Version work, started 2026-11-02)

Process: the Community template "Audience Segmentation, Goals, Motivations, and Use Cases Workshop" (copy in `docs/sources/audience-workshop-template/template-text.md`). Steps: (1) segment traits, done in the original section and the 2nd Version; (2) pick audiences and write a label and traits for each; (3) motivations; (4) situational and life goals; (5) use cases; (6) prioritize with the owner. **DRAFT for the owner to approve each step. Nothing here is chosen. Anything marked "guess" has no source.**

AARP report = AARP and NAC, Caregiving in the US 2025, full report: https://www.aarp.org/content/dam/aarp/ppi/topics/ltss/family-caregiving/caregiving-in-us-2025.doi.10.26419-2fppi.00373.001.pdf . **"p." is the PDF page** (printed page = PDF page minus 6). Saved copy and page-marked text: `docs/sources/aarp-nac-caregiving-in-the-us-2025/`. Every figure below was found by script on the cited page.

## Step 2. Audiences, labels and traits (candidates A and B; the owner picks)

### Audience A: "The family coordinator" (an adult child organizing a parent's care)
| Trait | Evidence | Link and page |
|---|---|---|
| Cares for a parent (40%) or parent-in-law (7%) | "Most are caring for a parent (40 percent) or parent-in-law (7 percent) or for a spouse or partner (15 percent)" | AARP report p.17 |
| Mid-life, mostly women | Average age 50.6; 61% women, 38% men | AARP report p.15 |
| Usually has a job | "Seventy percent of working-age caregivers are employed while also providing care" | AARP report p.38, p.39 (ages 18 to 64, n = 5,074) |
| Watches health and deals with providers | "70 percent monitor care recipients' health conditions, 64 percent communicate with care recipients' providers" | AARP report p.35 |
| Finds coordinating care hard | "only 6 in 10 report that coordinating care with health professionals is easy (58 percent)", down from 65% in 2015 | AARP report p.36 |
| Shares or fights over the work with family | Forum sample, 117 caregiving threads: siblings or family do not help 14, conflict 10, help 13, not mentioned 59, unclear 21 (family coordination is the main topic of 7 threads, 6%, and appears in 28, 24%) | `docs/community-voice-findings.md` (counts from our saved AgingCare and ALZConnected threads; each thread file starts with its web link) |
| Also the project owner's own case | The owner and sisters bought gadgets for their father (Apple Watch, smart blood pressure cuff). One case, told in chat, not checked | Owner, 2026-11-02 chat |
| Lives with or apart (forum threads that say) | 24 threads about a parent say where they live: 16 live apart, 8 live together. Most threads do not say | `docs/sources/forum-relevance/forum-final.json` |

### Audience B: "The one who does it all" (main caregiver, often living with the person)
| Trait | Evidence | Link and page |
|---|---|---|
| Lives with the person | "Forty percent of caregivers live with their care recipient (up from 34 percent in 2015)" | AARP report p.22 |
| Has less family help when living together | "Caregivers who live with their care recipient have less unpaid family help than caregivers who live apart" | AARP report p.22 |
| High-intensity care | "Four in 10 caregivers are in high-intensity situations (44 percent)"; average 27 hours a week, 24% give 40 or more | AARP report p.33, p.8 |
| Often alone in it | 34% have no other help (Figure 11) | AARP report p.25 |
| Long-term | Average 5.5 years; nearly 30% five years or more | AARP report p.28 |
| Medical tasks without training | 55% do medical or nursing tasks; 22% received training | AARP report p.34 |
| Did not choose it | "(56 percent) felt they had no choice in taking on their" role (the page text runs two columns together); "42 percent of involuntary caregivers find purpose in caregiving" | AARP report p.50 |
| Feels alone and stressed | 24% say they feel alone (up from 21% in 2020) | AARP report p.9 |
| Burned out and guilty | Burnout, guilt, isolation and grief is the main topic of 23 of 117 caregiving forum threads (20%) and appears in 50 (43%), the top or second theme in every source | `docs/community-voice-findings.md` |
| Includes spouses | 15% of caregivers care for a spouse or partner. The report has no separate figures for them in our extraction, so they are folded into this audience | AARP report p.17 |

### Alternative: Audience C, "The one far away" (not drafted unless the owner wants it)
About 11% of caregivers live an hour or more away (AARP report p.22: "More than 10 percent live an hour or more away"; the chart label is 11%). The report has no breakdown of them by age or income.

## What I need from the owner
1. Which two audiences, and the label wording.
2. Whether the traits above are the ones to keep (the template says to pick "the most impactful traits").
Then step 3 (motivations) uses forum quotes with their web links.

---

## Steps 3 and 4. Motivations, situational goals and life goals (DRAFT, from the forum threads; the owner approves)

Source: the 109 forum threads that the strict check confirmed as caregiving and tagged as caring for a parent (55) or a spouse or partner (54) (`docs/sources/forum-relevance/forum-final.json`). Reader agents extracted exact quotes from each thread; a script confirmed all 428 quotes are exact matches to the saved thread text. **Counts are the number of threads where a reader found a clear statement of that kind. They are minimums, not shares of all caregivers**: readers kept up to 6 items per thread, and the forums are AgingCare and ALZConnected (a dementia community), not a sample of all caregivers. Groups are formed by keyword rules on the readers' labels (`themes_motiv.py`), so a quote can sit in a group that is only approximately right. Each quote links to its original forum thread.

### Audience A: The family coordinator: caring for a parent (55 threads)

**Motivations: what drives them**

- **Keep them safe and comfortable, spare them suffering**: 7 of 55 threads
  - "I am the only one who brought my Mom items to make her more comfortable in her room." ([thread alz-77413](https://alzconnected.org/discussion/77413/advise-on-clothing-purchases))
  - "I need to remind myself that it's for a better and safer quality of life for her." ([thread alz-77386](https://alzconnected.org/discussion/77386/moving-mom-soon-but-how))
- **Do the right thing, avoid blame or guilt**: 6 of 55 threads
  - "Of course I also kept loads of documentation of everything I did so no one could accuse me of any malfeasance." ([thread agi-499820](https://www.agingcare.com/questions/seeking-advice-for-helping-aging-mom-take-over-household-finances-499820.htm))
  - "my wife and I are planning to have my mother move in with us so we can better support her ongoing care needs." ([thread alz-77396](https://alzconnected.org/discussion/77396/seeking-advice-on-affordable-home-repairs-to-help-support-my-mothers-care))
- **Keep them at home and in control of their own life**: 5 of 55 threads
  - "I felt like I was not allowing her to make the decision herself on the clothes." ([thread alz-77413](https://alzconnected.org/discussion/77413/advise-on-clothing-purchases))
  - "Am I wrong for still wanting to allow Mom to make her own decisions?" ([thread alz-77412](https://alzconnected.org/discussion/77412/am-i-doing-the-right-thing))
- **Love, loyalty and promises**: 3 of 55 threads
  - "I hope that he knew that he was indeed loved, even if the last few years seemed hard and distant from everyone." ([thread alz-77385](https://alzconnected.org/discussion/77385/rip-dad))
  - "I promised my parents I would never put them in a nursing home and I plan to keep that promise." ([thread agi-499448](https://www.agingcare.com/questions/my-mom-has-severe-dementia-what-is-a-good-way-to-handle-heavy-urine-output-at-night-499448.htm))
- **Other**: 2 of 55 threads
  - "My sister and I are praying for direction on how to help both of them!" ([thread alz-77005](https://alzconnected.org/discussion/77005/question-from-new-member))
  - "I what to protect her from his bad decisions, but sometimes I can’t." ([thread alz-76894](https://alzconnected.org/discussion/76894/moms-repetitive-calling-on-cell-phone-help-suggestions-needed))

**Situational goals: what they want to get done in the situation**

- **Get help, relief or services**: 11 of 55 threads
  - "I'm hoping to learn whether anyone knows of nonprofit organizations, community programs, affordable contractors, or other resources that might offer free or reduced-cost assistance with these repairs." ([thread alz-77396](https://alzconnected.org/discussion/77396/seeking-advice-on-affordable-home-repairs-to-help-support-my-mothers-care))
  - "I am contacting yet another avenue to help me with all of the legal aspects of managing what I have been trying to do for years." ([thread agi-499298](https://www.agingcare.com/discussions/am-i-doing-the-right-thing-im-just-not-seeing-the-rewards-of-doing-all-of-this-499298.htm))
- **Find, choose or pay for a place (memory care, assisted living)**: 6 of 55 threads
  - "Who is the best person to help me with his financials and what I can do with them to provide a stream of income, so I can see what he can afford and for how long?" ([thread agi-499890](https://www.agingcare.com/questions/dad-needs-assisted-living-who-is-the-best-resource-to-help-me-with-his-financial-picture-499890.htm))
  - "We are looking for a place where we can benefit from the experiences of others who've already gone further down this road." ([thread alz-77005](https://alzconnected.org/discussion/77005/question-from-new-member))
- **Manage money and legal affairs**: 3 of 55 threads
  - "my siblings and I are trying to figure out how to set up a new finance management system that allows for her to be in the driver’s seat while also allowing for us to step in and help her out as needed." ([thread agi-499820](https://www.agingcare.com/questions/seeking-advice-for-helping-aging-mom-take-over-household-finances-499820.htm))
  - "Does anyone have any advice on how to limit this vulnerability/stopping so much spam or limiting charges?" ([thread alz-77430](https://alzconnected.org/discussion/77430/dealing-with-finances-during-short-term-memory-loss))
- **Understand what is happening and what to do**: 2 of 55 threads
  - "Are these behaviors associated with the cognitive changes? Or is this just a midlife crisis?" ([thread alz-77404](https://alzconnected.org/discussion/77404/isolation))
  - "I guess I am asking for advice on what else we could be doing now" ([thread agi-498825](https://www.agingcare.com/questions/signs-of-decline-in-my-father-where-do-we-begin-to-get-ahead-of-this-498825.htm))
- **Keep them safe and watch over them**: 2 of 55 threads
  - "Looking for a pill box or dispenser that will sense if it's been picked up or opened or similar, and alert a caregiver if it has not." ([thread alz-77417](https://alzconnected.org/discussion/77417/looking-for-a-smart-pillbox-also-my-experience-with-smart-stove-knobs))
  - "use a GPS tracker in the form of a watch that has a lock and can be set for a "green zone"." ([thread alz-77129](https://alzconnected.org/discussion/77129/the-in-between-stages))
- **Medicines**: 1 of 55 threads
  - "I do stay and watch that each set of pills make it into his mouth AND that they stay there" ([thread agi-498744](https://www.agingcare.com/questions/how-do-you-minimize-dropping-pills-on-the-floor-498744.htm))
- **Other**: 9 of 55 threads
  - "I, along with his doctor, believe he should not be living alone and should be somewhere with social interaction, good food and stuff to do." ([thread agi-499890](https://www.agingcare.com/questions/dad-needs-assisted-living-who-is-the-best-resource-to-help-me-with-his-financial-picture-499890.htm))
  - "I was wanting to take Mom so that we could spend time together outside of the facility and most importantly so Mom could pick her own yarn." ([thread alz-77412](https://alzconnected.org/discussion/77412/am-i-doing-the-right-thing))

**Life goals: what they want in their own life**

- **Time and breaks for themselves**: 4 of 55 threads
  - "For my own mental and physical health, I needed to find ways to take a break regularly from caregiving" ([thread agi-499699](https://www.agingcare.com/questions/does-anyone-else-feel-resentment-499699.htm))
  - "I just want to go away for a few days even by myself and chill and shut some of this out." ([thread agi-499298](https://www.agingcare.com/discussions/am-i-doing-the-right-thing-im-just-not-seeing-the-rewards-of-doing-all-of-this-499298.htm))
- **Keep their own life, job and money**: 3 of 55 threads
  - "my spouse and I were not planning on having any dependents in the foreseeable future." ([thread agi-499761](https://www.agingcare.com/questions/recently-moved-my-father-in-law-in-with-us-on-short-notice-he-couldnt-go-back-to-his-home-after-bein-499761.htm))
  - "have come to the cross roads of continuing to care for mama, or continue my own life" ([thread alz-77432](https://alzconnected.org/discussion/77432/assisted-living-guilt))
- **Their own health and sanity**: 1 of 55 threads
  - "I wish I had the courage to stop caregiving" ([thread agi-499771](https://www.agingcare.com/questions/anyone-else-dealing-with-2-sisters-who-live-their-own-lives-go-everywhere-without-me-leave-me-here-t-499771.htm))

### Audience B: The one who does it all: caring for a spouse or partner (54 threads)

**Motivations: what drives them**

- **Keep them safe and comfortable, spare them suffering**: 11 of 54 threads
  - "In the end for me, it has become primarily an issue of safety for her (out of control anger and agitation, losing balance, close to wandering when angry)." ([thread alz-77354](https://alzconnected.org/discussion/77354/can-anybody-relate-to-this))
  - "The lying to him is a hard thing to do since I haven’t lied to him in 45 years….but I will do whatever if it makes this easier for him." ([thread alz-77392](https://alzconnected.org/discussion/77392/time-for-memory-care))
- **Love, loyalty and promises**: 9 of 54 threads
  - "I pray for patience and compassion and I thank God daily for the ability to care for and about my DH’s feelings as he is struggling with what he’s going through." ([thread alz-77263](https://alzconnected.org/discussion/77263/gotta-see-the-humor))
  - "But will she remember the love we have, and the humor between us, at least for a little while before she disappears completely?" ([thread alz-77375](https://alzconnected.org/discussion/77375/the-time-has-come))
- **Keep them at home and in control of their own life**: 4 of 54 threads
  - "The proper dose of the right med would not only make him calmer but also enable me to keep him home and hopefully out of MC." ([thread alz-77414](https://alzconnected.org/discussion/77414/to-drug-or-not-to-drug))
  - "how can I take him away from his friends, his shop, his yard. These are the things that give him pleasure." ([thread alz-77390](https://alzconnected.org/discussion/77390/move-now-or-later))
- **Do the right thing, avoid blame or guilt**: 1 of 54 threads
  - "in this world of trying to do right by our spouse." ([thread alz-77347](https://alzconnected.org/discussion/77347/hospice-time))

**Situational goals: what they want to get done in the situation**

- **Find, choose or pay for a place (memory care, assisted living)**: 7 of 54 threads
  - "I'm wondering if she would be better off living at a memory care facility where she would.have professional care full-time." ([thread alz-77284](https://alzconnected.org/discussion/77284/nothing-to-do))
  - "I still have to work full time so I have finally come to the place it is better for him and me to do this." ([thread alz-77392](https://alzconnected.org/discussion/77392/time-for-memory-care))
- **Get help, relief or services**: 6 of 54 threads
  - "I know I need some help but don't know if I should try the GUIDE PROGRAM and see if he qualifies for VA catastrophic disabity rating of if it's time for a hospice evaluation." ([thread alz-77473](https://alzconnected.org/discussion/77473/signed-hospice-contract))
  - "my thinking is that we can save money on the insurance and could use that to pay for the visit if necessary." ([thread alz-77439](https://alzconnected.org/discussion/77439/dental-insurance))
- **Keep them safe and watch over them**: 5 of 54 threads
  - "her cardiologist wants her to use a BP monitor for daily or twice daily reads since her BPs are trending higher." ([thread alz-77372](https://alzconnected.org/discussion/77372/travel-compact-bp-monitors-for-iphone))
  - "My expectations of the staff is to ensure my DH is feed, showered, and toileted." ([thread alz-77374](https://alzconnected.org/discussion/77374/family-expectations))
- **Medicines**: 1 of 54 threads
  - "After 8 years of dealing with hubby's progressing dementia, and fighting him about taking the 8-15 pills daily, I have started asking about quality of life rather than quantity." ([thread agi-499378](https://www.agingcare.com/questions/how-have-you-been-able-to-get-the-mountainous-piles-of-meds-reduced-499378.htm))
- **Other**: 4 of 54 threads
  - "my goal is to keep him with me until such time as he no longer knows who I am or who he is or where he is" ([thread alz-77364](https://alzconnected.org/discussion/77364/visitation-block))
  - "Does anyone know of organizations who match caregivers to patients as an ongoing care 1 on 1 same person?" ([thread alz-77395](https://alzconnected.org/discussion/77395/our-caregiver-quit-unexpectedly))

**Life goals: what they want in their own life**

- **Their own health and sanity**: 7 of 54 threads
  - "I feel I need to get a divorce for financial reasons as well as my sanity. I don't want to abandon him, but I have to look out for myself." ([thread alz-77428](https://alzconnected.org/discussion/77428/i-dont-think-i-can-do-this))
  - "someone I can talk to without judgement and willing to work WITH me to help with my severe anxiety and depression." ([thread alz-77427](https://alzconnected.org/discussion/77427/time-for-therapy-for-me))
- **Keep their own life, job and money**: 4 of 54 threads
  - "I knew if I quit my job I would be miserable and it would not change the trajectory of the disease." ([thread alz-77383](https://alzconnected.org/discussion/77383/new-to-this))
  - "I am now starting to create a new life for me and my remaining time here on earth." ([thread alz-77470](https://alzconnected.org/discussion/77470/i-live-in-a-world))
- **Time and breaks for themselves**: 2 of 54 threads
  - "I feel like I am losing myself as a caregiver because I don't ever have time to myself to do anything that I want to do?" ([thread agi-499707](https://www.agingcare.com/questions/help-i-feel-like-i-am-losing-myself-as-a-caregiver-499707.htm))
  - "starting with me getting back to taking my 30 minute walks which I used to do at least 5 times a week." ([thread alz-77427](https://alzconnected.org/discussion/77427/time-for-therapy-for-me))

**Not found in the data, so not claimed:** how many caregivers share each motivation; any difference between the two audiences beyond what the counts above show (counts are small and the forums differ: ALZConnected is mostly spouses, AgingCare mostly parents).

---

## Step 5. Use cases to support (DRAFT, 2026-11-02; in the audience workshop board)

Problems: the 286 problem statements that readers extracted from the 109 parent and spouse threads (151 and 135). A reader agent sorted each into a theme by reading the quote (`docs/sources/forum-relevance/usecase-assign-*.json`); counts are the number of threads per theme, so they are minimums and approximate. Examples are exact quotes, each checked against its saved thread (36 of 36). **The last two columns (business goal and future scenarios) are ASSUMPTIONS written as outcomes, not features, and are not research findings.** Themes that fit none (10 and 7 threads for parent and spouse caregivers) are left out. Prioritization on risk and certainty is still to do with the owner.

### Audience 1: The family coordinator (parent)

- Exhaustion, guilt and no life of their own (23 of 55 threads)
- Dementia behavior and hard conversations (14 of 55 threads)
- Money, legal papers and facility bills (11 of 55 threads)
- Relatives do not help, or block each other (10 of 55 threads)
- Medicines, eating and personal care (8 of 55 threads)
- Choosing and arranging a place for them (6 of 55 threads)
- Staying safe at home (6 of 55 threads)
- Getting answers from doctors and hospitals (4 of 55 threads)
- Being far away and not knowing what is happening (2 of 55 threads)

### Audience 2: The one who does it all (spouse or partner)

- Exhaustion, loneliness and own health (22 of 54 threads)
- Dementia behavior and hard conversations (18 of 54 threads)
- Personal care and medicines (12 of 54 threads)
- Safety when they are alone or out (9 of 54 threads)
- Aides, hospice and trusting others (8 of 54 threads)
- Placing them and care costs (7 of 54 threads)
- Money, scams and bills (6 of 54 threads)
- Diagnosis and doctor delays (4 of 54 threads)
- Relatives and others not helping or criticizing (3 of 54 threads)

---

## How the two audiences differ (added 2026-11-02, in the audience workshop board)

Counts are forum threads from the sorted quotes; approximate (one reader sorted each quote; the forums are mostly dementia caregivers).

**The same for both:** exhaustion and loneliness is the top problem (23 of 55 parent threads, 22 of 54 spouse threads); dementia behavior is second (14 and 18); safety, money, finding or paying for a place, and doctor delays appear for both; motivations and life goals use the same themes.

**Different:**
- Where they live (only the threads that say): parent caregivers, 16 apart and 8 together; spouse caregivers, 12 together and 4 apart.
- Relatives not helping or blocking: 10 of 55 parent threads, 3 of 54 spouse threads.
- Love, loyalty and promises as a motivation: 3 of 55 and 9 of 54.
- Own health and sanity as a life goal: 1 of 55 and 7 of 54.
- Trusting aides and hospice: a theme for spouse caregivers (8 of 54 threads), not a separate theme for parent caregivers.
- Being far away and not knowing what is happening: a theme for parent caregivers (2 of 55 threads), not a separate theme for spouse caregivers.

**My reading (not a finding):** the audiences differ more in who they care for, where they live and who else is around to help than in what they want. Whether that is enough to treat them as two audiences is the owner's decision.
