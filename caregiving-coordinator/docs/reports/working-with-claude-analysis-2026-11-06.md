# How the work with Claude went, and what to change (2026-11-06)

**Who wrote this:** Claude, from the saved record, at the owner's request. It describes patterns in how the work went. It is not a diagnosis, and it is **not** the owner's "What I Did" and "What I Learned," which the owner writes alone. Replaces the longer draft `research-problems-analysis-2026-11-06.md`, which stays for reference.

## 1. The short answer

- The problem did not start with the competitive analysis. It started in the first week, when rules, sources and definitions were still moving and checks happened by hand.
- Most of the errors in the record were Claude's (29 itemized in the Nov 4 to 5 reports and 19 on Nov 6, plus the 48 events logged through Nov 4): working from stale or partial sources, saying more than it had checked, and acting before being asked.
- The owner's way of working added two things: short messages that depended on shared context, and the owner being the only checker.
- Some of this was learning in progress. The dog feeding method was added to the project rules on **2026-11-04**, after about 11 of 13 sessions had already happened.
- The owner caught errors from the first week. What changed on Nov 4 to 5 is that checking became systematic: cell by cell, then six independent audits.

## 2. What happened, in phases

| Phase | Dates | What went wrong | Who caught it | What changed |
|---|---|---|---|---|
| Setup and pivot | Oct 14–28 | A first project was dropped (Oct 23). The wrap-up skill was rewritten 13 times in 2 hours. | Owner | Homework restarted for the caregiving idea |
| Discovery research | Oct 29–Nov 1 | Chat-AI counts invented numbers. Claude filled gaps with a solution and an assumption. A claim was stated as fact. The full AARP report was not read. | Owner (and Claude, on counts) | Rules: no solution framing, cite sources, Claude counts itself |
| Tables rebuilt | Nov 2–3 | Unsourced figures, empty columns, labels like "Mixed" that said nothing | Owner and review | The owner asked for "observable evidence" (Nov 2) |
| The big rebuild | Nov 4 | One quote per cell, competitors picked from "handy" saved pages, the #1 problem (exhaustion) left out, changes made without being asked | Owner | Dog feeding method, cell rules and "questions get answers, not edits" added to the rules |
| Audit | Nov 5 | 18 problems: stale repo copies, overstated verdicts, wrong page numbers | Six independent agents | A clean Figma page and handoff reports |
| Feature table | Nov 6 | The competitive analysis scored 5 needs, not features. The competitor set missed the main kinds of relief. 19 more errors. | Owner and independent audits | Three-pass research and a retired set of tools |

Sources: `docs/sources/research-history/EVENT-LOG.md` (48 events through Nov 4; the history helper was stopped at the owner's request, so Nov 5 to 6 are not logged), the change reports in `docs/reports/`, and `docs/reports/feature-analysis-4-change-report-2026-11-06.md`.

## 3. Sessions

About 13 conversation sessions from Oct 29 to Nov 6, about 54 active hours, about 1,000 owner messages. The longest ran 49 hours (Nov 4 to 6, 338 messages). Nine of the 13 opened with "pick up where we left off." Three started at the same minute on Nov 3. Source: a script over the saved transcripts. The Oct 28 session's transcript was not found.

## 4. Patterns in how the work was done

These are observations, labeled as such.

| Pattern | Evidence | What it caused |
|---|---|---|
| **Short messages that need shared context.** Examples: "pick up where we left off," "Yes," "If you choose only those communities and maybe not Facebook?" | The owner's own messages in the saved transcripts | Claude filled the gaps with guesses, or answered the wrong part of a multi-part question |
| **Strong checking instinct, used after the fact.** The owner asked for citations on Nov 2, compared work to the instructions on Nov 3 ("ten competitors at least"), and asked "did you make sure you didn't make anything up?" | Same | Many errors were caught, but late, and by the owner alone |
| **Rules added after each incident.** Rules went into `CLAUDE.md` and memory after each mistake. Several were broken again later. For example, "questions get answers, not edits" was added Nov 4, and Claude still created files and a branch unasked on Nov 6. | `docs/sources/research-history/EVENT-LOG.md` (E47 and later), Nov 6 change report | Rules piled up without changing how the work started |
| **Sessions began from memory, not a fixed starting page.** | Nine of 13 sessions opened with "pick up where we left off" | Each session rebuilt its context from whatever files it found, including stale copies |
| **Open decisions piled up.** The Nov 6 handoff listed nine. | `Dog Feeding Docs/Week 2_3/` handoff reports | Later work stalled on questions nobody had settled |
| **Strong direction, fast.** The owner saw that the competitor set missed exhaustion relief, that "paid" and "unpaid" was undefined, and that source of truth must be Figma. | Same transcripts | Most of the useful corrections came from these |
| **Frustration rose when the same error came back.** Corrective words show up on 26 to 39% of the owner's messages every day, with no drop after rules were added. | A rough keyword count over the transcripts (not a precise measure) | Trust wore down. Longer, more emotional messages followed. |

## 5. What to do differently

1. **Start each session with three lines:** the one task, the source of truth (a Figma node or file), and what "done" looks like. This replaces "pick up where we left off."
2. **Ask Claude to show what it read and what it assumes, before it works.** The owner already does this when upset. Make it standing.
3. **Write the definitions once:** who is in the audience, what ✅ and 🚫 mean, how much evidence is "enough."
4. **Have Claude run its checks first.** Ask it to show scripts and an independent audit result before you review. Keep your review for judgment, not hunting for slips.
5. **Settle decisions as they come,** one at a time, with two choices each.
6. **Keep sessions short,** one deliverable each, and end each with a handoff report.
7. **Ask for plain words.** Every term explained, short table titles, one question at a time.

## 6. Evidence and limits

- **Sources:** git history (176 commits since Oct 14), `docs/reports/`, `Dog Feeding Docs/`, the owner's memory notes, and this computer's saved transcripts.
- **Checked:** session and message counts were computed by a script. Event log rows carry commit hashes or file paths, and its quotes are script-checked by the helper.
- **Not checked:** the history helper was stopped at the owner's request, so Nov 5 to 6 events are only partly logged. The keyword count is rough. The owner's earlier chats outside this project's folder, and the Oct 28 transcript, were not read. This describes patterns in the record and says nothing about intentions or personality.
