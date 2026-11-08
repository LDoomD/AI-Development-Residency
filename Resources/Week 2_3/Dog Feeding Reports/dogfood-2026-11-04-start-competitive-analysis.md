# Dog feeding report: start the competitive analysis (2026-11-04)

**This is the newest dog feeding report.** It replaces `dogfood-2026-11-04.md` as the file to start the next session with.

**How to start the next session:** give Claude this file and the saved documents in section 6, then say:
> "Read this report and the files it lists. Tell me what you have and what's missing. We're doing the competitive analysis, one part at a time."

---

## 1. How we work (dog feeding)

Source: the teacher's board "Steps to Produce Literally Anything" (Figma node 2390:7831).

- **Each new document is made from saved, checked documents.** Claude doesn't remember other chats, so the work lives in markdown files.
- **One part at a time.** The owner makes each choice. Claude does only the step asked, then stops.
- **Ask where each answer came from.** It must come from the saved documents, not guesses.
- **When a part is approved,** save it as a new markdown version. Never overwrite.
- **Order of work:**
  1. Market analysis ✅ updated
  2. Audience segmentation ✅ updated
  3. **Competitive analysis ← next**
  4. Feature analysis
  5. Design patterns
  6. Positioning
  7. Vision boards
- **Board rules:**
  - New work goes in a new dated section.
  - Replaced work gets a big yellow SUPERSEDED banner. Nothing is deleted.
  - Tables follow `docs/sources/market-analysis-3/audience-v2/TABLE-RULES.md`: short bullets, no IDs or quotes in cells, big text.

---

## 2. What changed in the market analysis (2026-11-04)

**New research:** a random sample of 500 Reddit posts (412 by caregivers), coded with the same 14 problem themes as the 117 forum threads, so the two can be compared.

**Why:** the new Reddit research must update the market analysis first. Earlier it was put straight into the competitive analysis and skipped this step.

**Six tables were updated** (Figma section 2598:10950, readable copy `docs/market-analysis-3.md`):

| Table | What changed |
|---|---|
| Top problems, 3rd version | All sources side by side. See the problem list below. |
| MVP and MMP scoring, 4th version | No score changed (the owner's call). It adds the Reddit evidence and 3 new rows for the owner to score: dementia behavior, the person refuses help, hands-on care. |
| Market opportunity, 3rd version | Adds a Reddit column. Draft reading: segment 10 (the parent's accounts and papers) has the strongest unmet need; burnout has the biggest need but is crowded; family coordination apps stay low. The owner decides. |
| Possible market segments, 3rd version | Adds how often each segment's problem comes up on Reddit. |
| Market size, 3rd version | The sizes don't change. It only adds how often caregivers raise each problem. |
| Market analysis, 3rd version | One note corrected: the old "largest need" figure came from an unsaved summary. |

**The problem list now (share of Reddit caregiver posts that mention it, plus the forum share):**
1. **Burnout, guilt, doing it alone:** about half the Reddit posts (forums 43%). Top in every source.
2. **Money, accounts and legal papers:** 28% (forums 33%). In a targeted Reddit search, 132 posts were about getting into a parent's accounts.
3. **Dementia behavior and hard conversations:** 24% (forums 34%).
4. **Family coordination and siblings:** 24% (forums 24%). Siblings won't share the work.
5. **Choosing, placing and paying for care:** 22% (forums 30%). Real, but not the biggest.
6. **Doctors, appointments and records:** 21% (forums 20%).
7. **The person refuses help (NEW):** 20% (forums 10%). Much bigger on Reddit.
8. **Safety and knowing a parent is OK:** 19% (forums 24%).
9. **Medications:** 13% (forums 16%). The risk is changes not being shared.
10. **Hands-on personal care, equipment and supplies (NEW):** 17 Reddit posts as the main topic.

Also: 65% of Reddit caregiver posts are about a parent.

---

## 3. What changed in the audience segmentation (2026-11-04)

**New section in the teacher's format:** Figma 2623:76 on the audience page (2378:7107). Readable copy: `docs/audience-teacher-format-2026-11-04.md`.
- **Built from 412 posts and threads,** each read in full: 303 Reddit posts and 109 forum threads.
- **Every list is most common first.** Scripts checked the quotes and counts.
- **First try superseded:** the forum-vs-Reddit rank tables (2605:638) were too confusing. They now have a SUPERSEDED banner.

**The audiences:** still two.
- **Audience 1, adult child caring for a parent:** the main audience. It's the one Vision Board #1 is for.
- **Audience 2, spouse or partner:** a smaller Reddit sample (35 posts), so treat it as a signal.

**Audience 1, most common first:**
- **Motivations:**
  1. Keep the parent safe and comfortable.
  2. Do the right thing without guilt or blame.
  3. Love and promises.
  4. Let the parent stay home and make their own choices.
- **Situational goals:**
  1. Understand what's happening and what to do next (now #1).
  2. Get help or services.
  3. Get money and legal papers under control.
  4. Keep the parent safe.
  5. Find and pay for a place.
  6. Get medicines right.
  7. Get the parent to accept care (new).
- **Life goals:**
  1. Their own health and sanity (now #1).
  2. Keep their job, life and money.
  3. Time and breaks.
  4. Protect their marriage and kids (new).
- **Use cases (11), with "seen in" counts:**
  1. Exhaustion and no life of their own (138)
  2. Dementia behavior and hard talks (82)
  3. Money, legal papers and bills (74)
  4. Medicines, eating and personal care (62)
  5. **The parent refuses help (60, new)**
  6. Relatives don't help (48)
  7. Choosing a place (46)
  8. Safety at home (37)
  9. Answers from doctors (30)
  10. Being far away (20)
  11. **Getting into the parent's accounts (8 here, 132 in the targeted search)**

**Audience 2, most common first:**
- **Motivations:**
  1. Love, loyalty and their vows (now #1).
  2. Keep the partner safe and comfortable.
- **Situational goals:**
  1. Get help.
  2. Understand what's happening (new).
  3. Find a place.
  4. Safety.
- **Life goals:**
  1. Their own health and sanity.
  2. Keep their life and job.
  3. **Companionship and someone who understands (new).**
- **Use cases (10):** exhaustion (45), dementia behavior (24), personal care and medicines (24), aides and hospice (14), money (13), relatives criticizing (12), diagnosis delays (11), partner refuses help (9, new), placing them (9), safety (8).

---

## 4. The competitive analysis today (what exists, Figma page "Market Research/Competitive Analysis/…")

**The teacher's template and instructions:**
- **Instructions (7:4243):**
  - The order is market research, then competitors, then features, then design patterns, then positioning.
  - The analysis is updated continually as priorities change.
  - The Product Manager owns it.
- **Problems to solve related to the competitive analysis (2:16):** for example, "the business isn't sure what its unique value is yet."
- **About competitor analysis (5:3576):**
  - Direct competitors sell the same product to the same customers.
  - Indirect competitors meet the same need in a different way.
- **Questions to answer about the competitors (4:533, 8 questions):**
  - Business model.
  - Retaining customers.
  - Customer experience.
  - Who uses it and who pays.
  - Can a second relative join with their own login?
  - Health data and consent.
  - Emergencies and failure.
  - Setup.
- **Direct competitors (4:494):** list 5 to 7. **Indirect competitors (4:515):** list any.
- **Direct and indirect competitor analysis table (4:619):** competitor, direct or indirect, market segment, website, features, how they stand out, what they do well, what they don't do well, then one column per question.
- **Summarize the gaps and unique value opportunities (5:3580).**
- **Two questions to answer:**
  - "Which other competitors are solving the same problems? Where are the gaps?" (6:3868)
  - "How is your business's impact different?" (6:3860)
- **AI prompt example (41:1268):** website, segment, audiences, channels, business model, offerings, and what people say online.

**The owner's earlier versions, used as examples:**
1. **Competitor camps (11-01, 2218:3262):** competitors grouped into 8 camps, each covering one piece of the problem:
   1. everyday organizers
   2. update and volunteer tools
   3. care-team hubs
   4. medication trackers
   5. visit notes
   6. **finding and paying for care** (A Place for Mom, Caring.com, Papa, Honor)
   7. **employer and plan navigation** (Cariloop, Wellthy, ianacare)
   8. document and login vaults

   For each camp: who pays, what's covered, what reviews praise and what they complain about.
2. **Competitor gaps (11-02, 2399:9704):** 7 areas, each with what competitors do well, what they don't do well, what we could do differently, and the evidence. Superseded.
3. **Version 1 (11-02, 2399:9186, `docs/competitive-analysis.md`):** the teacher's table with 10 competitors. It quoted single comments. Replaced.
4. **Version 2 (11-04, 2564:10354, `docs/competitive-analysis-2.md`), CURRENT:**
   - The same 10 competitors, with every box summarized from 1,101 reviews, posts and forum mentions.
   - Gaps and value opportunities version 2.
   - **Direct:** Caring Village, CaringBridge, Lotsa Helping Hands, Everplans, Epic MyChart, Lively, Medical Guardian.
   - **Indirect:** Medisafe, group texts, a paper notebook.
5. **What families use instead (2508:9836):** Life Alert, Apple Watch, group chats, notebooks and spreadsheets come up most on Reddit. The coordination apps barely come up.

**Removed today at the owner's request:** gaps and value opportunities version 3. They were built without being asked. Version 2 stands.

---

## 5. Why the competitive analysis needs another pass

- **Versions 1 and 2 picked competitors from the old problem list,** so they cover only three areas: coordination, account access and safety.
- **The updated research puts other problems near the top:**
  - burnout and doing it alone
  - money and legal papers
  - dementia behavior
  - the person refuses help
  - choosing a place
  - hands-on care
- **Most of these have no competitor on the board.** The 11-01 camps already named some (finding and paying for care, employer navigation, vaults), but versions 1 and 2 dropped them.
- **The audience use cases now say what each audience needs.** The competitor questions can be checked against them.

**Decisions for the owner, one at a time (Claude doesn't choose):**
1. What problems is the competitive analysis solving? (2:16)
2. Which problems and use cases should the competitor list cover?
3. Which direct (5 to 7) and indirect competitors to analyze. Keep, add or drop from version 2 and the camps.
4. Which questions to answer. Keep the 8, or change them to fit the new audience goals.
5. Then fill the table, then the gaps and value opportunities.

---

## 6. Saved documents to give the next session

1. This report: `Dog Feeding Docs/Week 2_3/dogfood-2026-11-04-start-competitive-analysis.md` (repo top folder)
2. Updated market analysis: `docs/market-analysis-3.md`
3. Audience page, teacher format: `docs/audience-teacher-format-2026-11-04.md`
4. Competitive Analysis 2 (current): `docs/competitive-analysis-2.md`
5. Competitive analysis version 1 and draft questions: `docs/competitive-analysis.md`, `docs/competitive-analysis-draft.md`, `docs/competitor-questions.md`
6. Who already serves exhaustion and dementia: `docs/exhaustion-dementia-research.md`
7. Reddit findings by feature: `docs/reddit-caregiver-findings-2026-11-03.md`
8. Table rules: `docs/sources/market-analysis-3/audience-v2/TABLE-RULES.md`
9. The Figma links above for the teacher's template and the camps. The camps (2218:3262) aren't saved as a markdown file yet. Ask Claude to read them from the board.

## 7. Still open

- Keep or remove the Feature Analysis 3 gaps-report rewrite (done without being asked)?
- Remove the duplicate audience section in the other FigJam file (Q5jRpN3MbONqFQF6KTS70j, 2061:543)?
- Everything above is committed and pushed (branch `feature-analysis`, commit c5ad13a). This report is new and not committed yet.

## 8. When to ask for the next report

- When a part of the competitive analysis is approved: save it as a new markdown version.
- Before a new chat or a compact: write a dog feeding report.
- If something is redone: write a short change report.
- When the competitive analysis is done, before the feature analysis: write a starting brief.
