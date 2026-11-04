# REPORT: What caregivers say on Reddit (desk research, 2026-11-03)

## How to use this report with Claude
Paste this whole report into a chat, or point Claude at `docs/reports/reddit-research-report-2026-11-03.md` in the caregiving-coordinator folder. The full version, with every quote linked, is `docs/reddit-caregiver-findings-2026-11-03.md`. The raw data and scripts are in `docs/sources/reddit/arctic-shift-2026-11-03/`, and each file is explained in `docs/sources/INDEX.md`. Rules that still apply: this is discovery, so nothing assumes a product; no caregiver interviews (desk research is the evidence base); cite every claim.

## 1. Why we did it
In the feature comparison table, the documents column (5) and the caregiver support column (8) were empty, and labels like "Mixed" or "Mostly problems" didn't say what goes wrong. App reviews alone couldn't fill them, so we read what caregivers write on Reddit.

## 2. How (method)
- Source: the Arctic Shift Reddit archive (https://arctic-shift.photon-reddit.com, project https://github.com/ArthurHeitmann/arctic_shift). It's public and needs no login. Reddit itself is blocked in Claude's browser. No usernames were collected.
- Downloaded: 43,665 posts from r/CaregiverSupport (all of 2023 to Nov 2026) and r/AgingParents (2023 to Feb 2026; stopped once there was enough). Plus the newest ~500 posts from each of 11 more communities: dementia, Alzheimer's, caregivers, CaregiversOfReddit, eldercare, Parkinson's, stroke, ALS, MS, COPD and disability (5,650 posts). Total searched: 49,315.
- Picked posts by topic words: apps, calendars, group chats, medications, passwords, portals, "I wish there was" (all kept), plus random samples for documents/POA and burnout/support (too many to read all).
- Claude helpers read and tagged 1,551 posts. For each: written by a caregiver? on topic? which of the 8 feature columns? does it work, fail, or is nothing working? the problem in plain words, any wish, and one word-for-word quote. Every quote was checked against the saved text.
- Removed: 21 posts by app makers pitching their own tools and 13 copies of the same post.
- Counted: 825 posts by caregivers, on topic (672 from the two main communities, 153 from the other 11).

## 3. Findings: what caregivers say for each need (825 posts)
- 8. Support for the caregiver: 292 posts, the biggest topic. Doing it alone because family won't help (137); burnout with no one who understands (57); no respite or breaks (20). "it all falls on me." (r/CaregiverSupport, 2025-05-24)
- 3. Relatives getting access: 147 posts. Banks, insurers or agencies won't deal with the caregiver, even with a POA (52); the parent's passwords are lost, forgotten or on scraps of paper (35); sign-in codes go to the parent's phone (23). "Can't get a code because it gets sent to my moms phone." (r/CaregiverSupport, 2026-01-02)
- 1. Shared calendar and tasks: 144 posts. Siblings won't share the work (77); information spread across group chats, calendars and paper, so things slip (35). "WhatsApp group (17 unread messages), Google Calendar nobody updates, notebook only I write in." (r/AgingParents, 2025-08-27)
- 5. Important documents: 128 posts. No power of attorney, or the POA is rejected or delayed (42); papers scattered across binders, camera rolls and portals (32). A bank rejected a POA as not having "appropriate documentation or basis for successor agent to act" (r/AgingParents, 2024-05-01).
- 6. Medical records: 90 posts. Doctors' offices don't share with the family (31); too many portals, or proxy access blocked (27). "We keep missing dr appointments because I don't know she's getting these calls" (r/dementia, 2026-09-06)
- 4. Medications the family can see: 88 posts. The parent forgets or refuses, so organizers and reminders don't stick (30); medication changes aren't shared, leading to near double doses (25). App makers post a lot on this topic, so it may look bigger than it is.
- 2. One update reaches everyone: 78 posts. Updates get lost or ignored, or start fights, in group chats (29).
- 7. Emergency help and fall alerts: 66 posts. No way for the family to know the parent is OK (22); the parent won't wear the device (11). "I wanted to know if there was a button she could press in an emergency that would JUST CONTACT FAMILY." (r/AgingParents, 2025-03-17)

## 4. Findings: what families use instead
Keyword count across all 49,315 posts (a mention isn't use):
- Safety: Life Alert 137 · Apple Watch 107 · Lively/Jitterbug 68 · Medical Guardian 33 · Life360 14
- Everyday tools: group chat or text 99 · notebook or binder 98 · WhatsApp 84 · pill organizer 79 · spreadsheet 62 · whiteboard 19 · Google Calendar 15
- Our coordination and records competitors: MyChart 46 · CaringBridge 7 · Lotsa 4 · Caring Village 3 · Medisafe 1 · Everplans 0

## 5. Analysis: what this changes in discovery
- Market research: no change. Reddit has no market-size data.
- Audience segmentation: one new use case for Audience 1 (adult child caring for a parent), getting into a parent's accounts. It's 18% of posts, and 108 of 147 writers care for a parent (4 a spouse). Value is High (over the 15% line); effort proxy is High (only Everplans and MyChart partly cover it). Suggested quadrant: 2, high priority. A note is on the audience page under "Prioritize use cases"; the matrix itself was not changed.
- Checked, not added: "Answers from doctors and hospitals" is 7% on Reddit, still under the 15% line.
- Competitive analysis: for coordination, families' real alternative is everyday tools, not the apps in our table. For safety, Life Alert and Apple Watch come up more than any company in our table. A note is next to the competitive analysis in the Current Set section.
- Feature analysis gaps: 1 (relatives' access), 2 (families stitch tools together) and 3 (safety's family side fails) are confirmed. 4 (shared medication info) is confirmed but may be overstated. 5 (records stuck in MyChart) is unclear; the real problem is getting in. New: 6 (documents and POA) and 7 (caregiver support, mostly about people, not tools).

## 6. Limits (say these whenever the report is used)
- People with problems post more than people without them; these are patterns, not rates.
- Claude helpers tagged each post once and no person double-checked. Problem groups come from keyword sorting of short summaries.
- Long posts were cut at 2,500 characters. Documents and support were sampled (120 posts each in the main communities, up to 25 per other community).
- App makers who don't say so may still be in the data. The other 11 communities only cover their newest ~500 posts, mostly from 2026. The condition communities (Parkinson's, MS, COPD, disability) are mostly patients, so they added almost nothing.
- Who the writer cares for was found from words like "my mom" and "my husband".

## 7. Files
- Full report with links: `docs/reddit-caregiver-findings-2026-11-03.md`
- Counts: `reddit-findings.json` (main communities), `reddit-findings-other.json` (other 11), `mention-counts.json` (tools), all in `docs/sources/reddit/arctic-shift-2026-11-03/`
- Re-run: `python3 -I analyze_tags.py main` · `python3 -I analyze_tags.py other` · `python3 -I count_mentions.py`
- Updated docs: `docs/feature-analysis.md` (steps 3 and 4), `docs/usecase-priority.md`, `docs/competitive-analysis.md` (the 2026-11-03 updates)
