# Use case prioritization (2nd version, 2026-11-02)

Placed on the effort and value matrix in the audience workshop board ("Prioritize Use Cases"). **Draft for the owner to move; prioritizing is the owner's judgment call.** This replaces the first version, where effort was my guess (kept in git history, commit `9deb9c6`).

**Value rule (from the research):** high if the problem came up in 8 or more of that audience's forum threads (about 15% or more), low if fewer. This measures how common it is, not how much it matters to the person. Counts: `docs/sources/forum-relevance/usecase-themes-final.json`.

**Effort rule (a proxy from our competitor data, not a measure of build time):** low only if a tool in our ten competitor rows already covers the use case. High if only part is covered or none is. Source: `docs/competitive-analysis.md`. "No tool in our ten" does not prove no tool exists.

**Evidence behind each use case** (forums, AARP report with pages, caregiving-only app reviews, competitors): `docs/usecase-evidence-table.md`.

**Borderline:** Audience 1 "Medicines, eating, personal care" (8 threads) and Audience 2 "Aides, hospice, trusting others" (8 threads) sit exactly at the value line. Several "partly covered" calls (Medisafe for medicines, Everplans for money, Epic MyChart for doctors) change quadrant if "partly" is counted as low effort.

| Quadrant | Audience | Use case | Threads | Value | Competitor coverage | Effort (proxy) |
|---|---|---|---|---|---|---|
| 1 Top priority (low effort, high value) | Audience 1 | Relatives do not help, or block each other | 10 of 55 | High | Yes | Low |
| 1 Top priority (low effort, high value) | Audience 2 | Safety when alone or out | 9 of 54 | High | Yes | Low |
| 2 High priority (high effort, high value) | Audience 1 | Exhaustion, guilt, no life of their own | 23 of 55 | High | None | High |
| 2 High priority (high effort, high value) | Audience 2 | Exhaustion, loneliness, own health | 22 of 54 | High | None | High |
| 2 High priority (high effort, high value) | Audience 2 | Dementia behavior, hard conversations | 18 of 54 | High | None | High |
| 2 High priority (high effort, high value) | Audience 1 | Dementia behavior, hard conversations | 14 of 55 | High | None | High |
| 2 High priority (high effort, high value) | Audience 2 | Personal care and medicines | 12 of 54 | High | Partly | High |
| 2 High priority (high effort, high value) | Audience 1 | Money, legal papers, facility bills | 11 of 55 | High | Partly | High |
| 2 High priority (high effort, high value) | Audience 1 | Medicines, eating, personal care | 8 of 55 | High | Partly | High |
| 2 High priority (high effort, high value) | Audience 2 | Aides, hospice, trusting others | 8 of 54 | High | None | High |
| 3 Medium priority (low effort, low value) | Audience 1 | Staying safe at home | 6 of 55 | Low | Yes | Low |
| 3 Medium priority (low effort, low value) | Audience 2 | Relatives and others not helping | 3 of 54 | Low | Yes | Low |
| 4 Low priority (high effort, low value) | Audience 2 | Placing them and care costs | 7 of 54 | Low | None | High |
| 4 Low priority (high effort, low value) | Audience 1 | Choosing and arranging a place | 6 of 55 | Low | None | High |
| 4 Low priority (high effort, low value) | Audience 2 | Money, scams and bills | 6 of 54 | Low | Partly | High |
| 4 Low priority (high effort, low value) | Audience 1 | Answers from doctors and hospitals | 4 of 55 | Low | Partly | High |
| 4 Low priority (high effort, low value) | Audience 2 | Diagnosis and doctor delays | 4 of 54 | Low | Partly | High |
| 4 Low priority (high effort, low value) | Audience 1 | Far away, not knowing what is happening | 2 of 55 | Low | Partly | High |

Audience 1 = adult child caring for a parent (55 threads). Audience 2 = spouse or partner caring for a husband, wife or partner (54 threads). Themes are worded slightly differently for each audience.

**Limits:** forums skew to dementia caregivers (AgingCare, ALZConnected). Counts are minimums. The effort proxy says what exists today, not how hard anything is to build.

## Update 2026-11-03: one new use case from Reddit (added; the existing rows are unchanged)

**Getting into a parent's accounts (banks, insurers, patient portals, passwords): Audience 1.**
- **Evidence:** 147 of 825 caregiver posts on Reddit (18%). Of those, 108 are by someone caring for a parent, 4 by someone caring for a spouse, 9 both, and 26 unclear, so it belongs to Audience 1.
- **What goes wrong:** banks, insurers or agencies won't deal with the caregiver, even with a POA (52); the parent's passwords are lost, forgotten, hidden or on scraps of paper (35); sign-in codes go to the parent's phone or email (23).
- **In their words:**
  - "Can't get a code because it gets sent to my moms phone." ([r/CaregiverSupport, 2026-01-02](https://www.reddit.com/r/CaregiverSupport/comments/1q1q82k/))
  - "They write it down on daily mail, random sheets of paper, and occassionally type it in a word doc." ([r/AgingParents, 2024-08-05](https://www.reddit.com/r/AgingParents/comments/1el0weu/))
- **Value: High.** 18% is above the 15% line, though this is a different base (Reddit posts, not forum threads).
- **Effort (proxy): High.** Coverage is partial: Everplans shares accounts (Premium, no caregiver reviews found) and MyChart has proxy access (Mixed, 17 of 36), but neither helps with banks or other sign-ins.
- **Quadrant: 2, high priority (high effort, high value).**
- **Why it's new:** the forum read folded this into "Money, legal papers, facility bills". Reddit shows it's mostly about logins and institutions refusing the caregiver, not the papers themselves.

**Checked but not added:** "Answers from doctors and hospitals" came up in 58 of 825 Reddit posts (7%, doctors not sharing with family plus portal problems). That's still under the 15% line, so it stays Low.

Sources: `docs/reddit-caregiver-findings-2026-11-03.md`; counts in `docs/sources/reddit/arctic-shift-2026-11-03/mention-counts.json` and `reddit-findings*.json` (`count_mentions.py`, `analyze_tags.py`). Limits: tagged once by Claude helpers; who the writer cares for was found by words like "my mom" and "my husband".
