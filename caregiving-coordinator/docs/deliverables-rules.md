# Deliverable rules (moved out of CLAUDE.md on 2026-11-18)

These rules were in the "Dog feeding" section of `CLAUDE.md`. They are copied here word for word. They apply to the Week 2 and 3 deliverables (market analysis, audience, competitive analysis, features, positioning, vision boards) and to any research that builds on them. They are not needed for every session, so Claude reads this file when that work starts, instead of loading it every session.

---

> **RULE #1: EVERY DELIVERABLE IS PART OF ONE PROJECT (the owner's words, 2026-11-04,
> after repeated mistakes).** Market analysis, audience segmentation, competitive
> analysis, feature analysis, positioning and vision boards are not separate tasks.
> Each one is built on the ones before it and feeds the ones after it. Any research,
> table or step must use the structure the project already set: the two audiences
> (Audience 1 = adult child caring for a parent, Audience 2 = spouse or partner),
> the top caregiver problems, the market segments, the 5 criteria, and the open
> questions (such as who pays). When new research changes one deliverable, say
> which other deliverables it changes, and update them in order.

- **A dog feeding report is a handoff report (owner, 2026-11-05).** Its outcome:
  the next Claude, in a new session or the same one, can start the next
  deliverable from this file alone. It must hold:
  1. where we are and where to start
  2. all the rules
  3. **the actual outcomes of every finished deliverable**: key tables,
     verdicts, answers and numbers with sources, not just links
  4. what the next deliverable needs (homework and template)
  5. what's out of date and why
  6. exact first steps
  7. open and parked items
  8. where things live
  9. git status

  A list of what happened is not enough. Name it
  `dogfood-<date>-handoff-<next deliverable>.md`, and say which older reports
  it replaces. Example: `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-08-handoff-audience-segmentation-reports.md`.

- **Order of work:** market analysis → competitive → feature → positioning →
  vision boards. New research updates the market analysis first.

- **Earlier deliverables lead the next one (rule added after repeated mistakes,
  2026-11-04).** Start each step from the earlier deliverables' actual tables. For
  example, the competitive analysis takes its competitors from the market
  analysis segment table and its named companies
  (`docs/competitive-analysis-3-inputs.md`). Before giving options, show an
  inputs table: each relevant item, used or left out, and why. Table cells are
  one short sentence that answers the column's question, in the style of the
  owner's earlier tables. Counts and quotes go in the evidence file. One entity
  per row, labeled business, nonprofit, government program or workaround.

- **Search all saved research on a topic first (rule added 2026-11-04, after
  `docs/exhaustion-dementia-research.md` was missed).** Before working on any
  problem, segment or competitor, search every saved document in `docs/` for
  that topic (for example `find docs -name "*.md" -exec grep -l -i -E
  "exhaust|burnout|respite" {} \;`), and list each file found in the inputs
  table as used, or left out and why. Don't rely only on the files a report
  lists. Never filter out the segment for the #1 problem without telling the
  owner plainly that the biggest need will have no competitor. Candidates come
  from the full researched list, never from pages that happen to be saved.
  Mistake log: `docs/reports/competitive-analysis-3-change-report-2026-11-04b.md`.

- **Every research pass splits by audience.** Before any reading starts, the
  instructions must record who the writer cares for, with the market analysis
  labels ("cared_for": parent, spouse or partner, other relative, child,
  client, unclear). Audience 1 = adult child (or child-in-law) caring for a
  parent; Audience 2 = spouse or partner (Figma 2378:7111, 2378:7177).

- **How to answer a table question from data (owner-approved style,
  2026-11-04, after 4 rejected drafts).** Every cell must pass all of these:
  1. **Answer the column's question directly, in the first word.** Don't
     repeat the row's name (the label already says it). Don't lead in.
  2. **No filler.** Cut words that add no fact: "quickly", "overwhelmed",
     "for them", "when a parent completes it ahead of time", "so everyone".
  3. **Concrete examples from the data.** Give several when the data has
     several, as a list of facts. Never vague words like "easy to use" or
     "helpful".
  4. **No quotes, counts, IDs or research words** ("evidence", "mentions",
     "company claim", "no data") in the cell. They go in the evidence file.
  5. **No tags or fragments** that don't answer ("Shows options and some
     prices"). **No long, wordy sentences** either. Two short sentences at most.
  6. **Thin data means getting more data** (BBB, Trustpilot, app stores,
     Reddit through the Arctic Shift archive), never a cell saying it's thin.
  7. **Yes / Partly / No questions** start with that word, then the facts:
     "Partly: stores documents. No help getting into bank, insurer or portal
     accounts."
  - Approved examples: "Lists nearby senior living options with prices and
    books tours." / "Shares families' contact details, causing nonstop sales
    calls. Commission-paid advisors know little about the places." / "Cost
    $150 to $300 an hour, offer unclear services, and sometimes never make
    the agreed care plan."
  - Before showing a table, check every cell against these 7 rules and its
    saved source (for example with a checker script like
    `docs/sources/competitive-analysis-3/grid/build_grid_v2.py`).

- **Superseded work:** a big yellow banner across the top of the section,
  never a small sticky. Never delete.

- **Tables:** follow `docs/sources/market-analysis-3/audience-v2/TABLE-RULES.md`
  (the user has ADHD: short bullets, no IDs or quotes in cells, big text).
