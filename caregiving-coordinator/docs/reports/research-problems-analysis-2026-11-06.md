# Why the research keeps going back: analysis of the problems (2026-11-06)

> **Superseded.** The shorter `working-with-claude-analysis-2026-11-06.md` replaces this draft. The owner stopped the report work on 2026-11-06. Lines below that say audits or helpers are "still running" or "in progress" are out of date: all research and audits are finished, and the history helper was stopped.

**Who wrote this:** Claude (the AI assistant), at the owner's request, from the project's own records. It is an analysis of what went wrong. It is **not** the owner's "What I Did" or "What I Learned" summary, which the owner writes alone.

## 1. The short version

- The three deliverables (market analysis, audience segmentation, competitive analysis) were finished and approved, but starting the next deliverable, the feature comparison table, exposed new gaps each time.
- **Most errors in the record were Claude's, not unclear prompts.** The most common one: Claude worked from incomplete, stale or guessed sources and said more than it had read or checked.
- **A second cause is the way the work was set up.** Deliverables were updated after later work had started. Figma and the repo copies drifted apart. Checks came the next day, not before. Some key definitions were never written down (who counts as a caregiver, what a ✅ means).
- **A third cause is the data.** Reddit posts were saved without replies, some sites block crawlers, and one research tool (NotebookLM) could not be reproduced.
- **What helped:** independent audits, script-checked quotes, and the owner catching real problems early.

## 2. What happened, in order

| Date | Deliverable | What had to be redone | Why (from the record) |
|---|---|---|---|
| Nov 2 | Market, audience | Swapped theme counts, a quote that didn't match its page, a wrong review match | Small data slips (commit messages "Fix two swapped theme counts," "Fix one quote," "Fix Lotsa review match") |
| Nov 3 | Feature Analysis 2 | Built on 8 competitors that later changed | Competitor list changed afterward |
| Nov 4 | Competitive Analysis 2 | Every cell rebuilt | Cells held one quote each, and some "gap" text was auto-generated filler (`competitive-analysis-2-change-report-2026-11-04.md`) |
| Nov 4 | Feature Analysis 3 | Built on Competitive Analysis 2's 10 competitors; only 3 overlap with today's 9 | The upstream deliverable changed again |
| Nov 4 | Competitive Analysis 3 | Competitors picked from "handy saved pages," exhaustion (the #1 problem) left out, cells too long, mixed entities | Claude read only the files a report listed (`competitive-analysis-3-change-report-2026-11-04b.md`) |
| Nov 4 | All | The session changed analyses without being asked | Recorded in `session-overview-2026-11-04.md`: "the user was upset" |
| Nov 5 | All three | A six-agent audit found 18 problems | Overstated verdicts, wrong page numbers, repo and Figma copies not matching (`audit-2026-11-05-results.md`) |
| Nov 5 | Market | Statement "segments 11 and 12 were never researched" was wrong | The repo copies were older than the Figma board (`update-inventory-2026-11-05.md`) |
| Nov 6 | Feature table | New research for 9 companies x 9 features, then the competitor list found missing the main kinds of relief | The competitive analysis scored 5 needs, not features. See section 4. |

**Count:** the competitive analysis is on its fourth version and the feature analysis on its fourth, within about a week. At least 7 commits since Nov 1 are explicit corrections to deliverables.

## 3. Errors by cause

**Documented before today:** 4 in the first Competitive Analysis 3 report, 7 in the second, and 18 found by the audit. That is 29 itemized errors, plus the whole of Competitive Analysis 2.

**Today (Nov 6):** 19 errors, listed in `docs/reports/feature-analysis-4-change-report-2026-11-06.md` and in later messages. My classification (a judgment, not a measurement):

| Cause | Count | Examples |
|---|---|---|
| Claimed or assumed more than was read or checked | 9 | Summarized Figma without proof. Called raw name counts "data-driven." Wrote "unpaid caregivers" with no source. Read a failed search as "no matches." |
| Communication Claude could not follow up on | 5 | Shorthand like "Figma says can't be made to do that." "Ordinary caregiver." Grading jargon ("Independent: fail," "homework mode"). Vague multi-part questions. |
| Acted without asking | 2 | Created a branch and file before telling the owner. Drafted a skill and rules before the owner took part. |
| A gap in how the deliverables were defined | 2 | The competitive analysis scored 5 needs, not the 9 features. The teacher's ✅ or 🚫 format has no way to show "offered only to some people." |
| Process or tool | 1 | A helper read pages from a site whose robots.txt blocks Claude's crawler. |

**Where an unclear owner prompt was the cause:** in the records I could read, I found none where the owner's instruction alone caused the error. Two came from definitions that were never written down (rows "design gap" and "assumed unpaid" above). Limit: I cannot see the owner's prompts from earlier sessions, only what those sessions saved.

## 4. The root causes

1. **Working from incomplete or stale sources (most common).** The Nov 4 report says: "I worked from what was in front of me, not from the saved earlier deliverables." The Nov 5 inventory shows the repo copies were older than the Figma board. Today, a helper was first told to use a saved copy of the competitive table, not Figma.
2. **Saying more than the evidence shows.** Examples: "the biggest need has no competitor" never flagged as a trade-off (Nov 4), verdicts the audit downgraded (Nov 5), and raw counts presented as findings (today). The raw count for Home Instead was 53 but only 12 posts were real.
3. **No fixed, versioned source of truth.** Figma and the repo both held "the" deliverable. Upstream deliverables were edited after downstream ones were built, so each downstream version went stale.
4. **Checks came after, not before.** Problems were found the next day by audit. Today's three-pass method (read, add sources, independent audit) caught errors in earlier helper work before any result was shown. One audit listed 39 corrections and another 35.
5. **Missing definitions.** Nobody had written down whether paid or professional caregivers were in the audience, what a ✅ means for a limited offer, or how much evidence is "enough."
6. **Backward planning was missing.** The feature table needs a list of features and competitors that offer them. The competitive analysis answered a different question (5 needs). So the last deliverable exposed gaps in the one before it.
7. **Data limits.** The saved Reddit archive holds posts and no replies. The bulk download was stopped early after repeated timeouts (49 of 53 log lines are timeouts in `log.txt`). Several sites block crawlers. NotebookLM's theme ranking could not be reproduced in a second pass (`community-voice-findings.md`).

## 5. What worked

- **Independent audits:** six agents on Nov 5 and three more on Nov 6 (two others still running) found real errors every time.
- **Script-checked quotes:** more than 1,000 quotes checked this week, with almost no made-up ones. The few misses were wrong file paths or paraphrases.
- **The owner's own checks:** the owner caught the exhaustion gap, the wrong competitor set, the missing paid-caregiver question, the source-of-truth problem and the jargon.
- **Honest reporting:** every error above is in a saved report.

## 6. What the owner can do in prompts

Based on the record, these changes would have prevented or caught errors earlier. They are not criticisms of the prompts so far.

1. **Open each research request with a short brief:**
   - Goal and the question.
   - Source of truth: the exact Figma node or file, and its date.
   - What counts as evidence, and what does not.
   - How much is "enough" (for example 15 or more independent reports).
   - When to stop.
   - What to leave out.
2. **Write the definitions once, in one place:** who is in and out of the audience (paid, unpaid, registered or not), and what ✅ and 🚫 mean.
3. **Ask for proof before work starts:** "Show me which nodes or files you read and what you are assuming."
4. **Date-stamp each approved deliverable** and keep a short list of what each depends on. When one changes, list every downstream deliverable it changes first.
5. **Plan backward:** before starting a deliverable, read the teacher's template for the next one and check that the current deliverable answers its questions.
6. **Decide open questions early.** The Nov 6 handoff lists nine open decisions, and several blocked work later.
7. **Name the tools for the job:** Arctic Shift for posts and replies by post id, Firecrawl for pages that allow crawlers, no NotebookLM.

## 7. What Claude is changing

- Read the owner's deliverables live and say which nodes or files were read.
- Never present a raw count as a finding. Read and sort every item first.
- Find candidates from the data, not from a guess list.
- Three passes before showing a conclusion.
- Explain every term in plain words, and ask one question at a time.
- Do not create or edit rules, skills or files that change how work is done without the owner taking part.
- A draft of these rules is in `docs/drafts/research-gate-skill-DRAFT.md`. It is **not active** and waits for the owner's review.

## 8. Where things stand today

- The feature table's evidence is finished (nine companies, three passes). The grid itself is not built.
- The competitive analysis needs an update: 20 cells in the existing rows (draft in `docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`) and new rows for the kinds of relief caregivers use. Reading and audits for those rows are in progress.
- The market analysis and audience segmentation need no change from this research.
- Nothing from today is committed.

## 9. Sources and limits

| Claim | Source | Limit |
|---|---|---|
| 29 earlier itemized errors | `docs/reports/competitive-analysis-3-change-report-2026-11-04.md`, `...04b.md`, `audit-2026-11-05-results.md` | Counted by rows in those reports |
| 19 errors today | `docs/reports/feature-analysis-4-change-report-2026-11-06.md` plus this session's messages | Classification is Claude's judgment |
| Versions and commit counts | `git log main`, `docs/competitive-analysis*.md`, `docs/feature-analysis*.md` | Dates of the oldest versions not checked |
| Repo copies older than the board | `docs/reports/update-inventory-2026-11-05.md` | Figma edit times are approximate |
| Arctic Shift timeouts | `docs/sources/reddit/arctic-shift-2026-11-03/log.txt` | Counts lines, not requests |
| NotebookLM not reproducible | `docs/community-voice-findings.md` | Says relative weights were not reproduced, not that every run failed |
| Raw counts misleading | `docs/sources/competitive-analysis-4/paid-help-and-therapists/SYNTHESIS.md` | One reader, spot-checked |

**Not checked:** the owner's prompts from sessions I cannot see, whether every earlier error is in a saved report, and anything the independent audits of the new competitor rows may still change.
