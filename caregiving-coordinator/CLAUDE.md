# Caregiving Coordinator

Week 2+ project for the Tech Fleet AI Development Residency. See `README.md`
for the problem and feature scope once written.

## Skills to use

Fourteen project skills live in `.claude/skills/` in this folder. Four carried
over from Week 1, `writing-security-tests` was added later, and nine were added
2026-10-31 for enterprise readiness. `project-prd-brainstorm` was removed
2026-11-01 (it does not fit the agile method this residency uses), and the old
`week-1-claude-skills/` folder was removed because all its skills already live
here (git tag `week-1-skills-as-submitted` keeps the original). The skills are
written to be reusable across products. This
product's specific risks (health data, shared credentials, multi-user access)
live in `docs/risk-profile.md`, which the skills read.

- `ux-ui-design-review`: reviewing screens, flows, forms, dashboards, or
  data tables for usability.
- `accessibility-check`: checking a UI against WCAG 2.2 level AA.
- `security-review`: checking code against the OWASP Top 10:2025, plus the
  risks in `docs/risk-profile.md`. Use whenever the user is about to commit, push, or share code
  containing a key, token, password, or secret, even when the question looks
  simple.
- `writing-security-tests`: after a `security-review` finding, write one
  real, runnable test proving the fix for that finding, in whatever test
  framework the project already uses. Confirm what's being tested with the
  user before writing it. No Gherkin, no CI/feature-index assumption — a
  test that can't actually run isn't done.
- `engineering-quality-check`: before calling work done, ready to merge, or
  ready for a pull request. Runs the arch-gate script.
- `judge-arch`: fresh-context architecture review of a change, with the
  `arch-gate.mjs` script. Findings only.
- `architectural-decision-records`: write a short ADR in `docs/adr/` when a
  decision others must follow is made.
- `enterprise-architecture-standards`: decide and document layers, data
  ownership, and dependency rules in `docs/architecture.md`.
- `skeptical-audit`: tag each factual claim in a report with evidence state,
  source, and limit.
- `owasp-secure-coding-bdd`: write secure-behavior scenarios before building a
  feature that handles input, data, or access.
- `test-strategy`: plan what to test, at what level, and which checks run as
  scripts.
- `operational-readiness`: monitoring, alerts, backups, and recovery before
  launch.
- `release-deployment-safety`: rollback, migrations, and rollout before a
  release.
- `data-lifecycle-compliance`: inventory personal data and find gaps in how it
  is kept, shared, and deleted. Never says "compliant".

Hooks in `.claude/settings.json` force this instead of leaving it to
description-matching: `SessionStart` and `SubagentStart` load the skill list
(`.claude/hooks/emit-skills-directive.mjs`), and a `PreToolUse` hook blocks
`git commit` and `gh pr create` when `arch-gate.mjs` fails
(`.claude/hooks/arch-gate-before-commit.mjs`). Tests: `node --test
.claude/skills/judge-arch/test/*.test.mjs`.

## Rules for this folder

- The review skills report findings first. Do not edit code until the user
  asks for fixes.
- Never say code is "secure", "accessible", or "tests pass" without evidence.
  Show the command and result, or say what was not checked.
- Never silently fall back to base knowledge when a skill above applies, and
  never silently skip a relevant skill. If one is judged not relevant to a
  task, say so explicitly rather than defaulting to not using it.
- Research must be auditable. Read the full primary source (the report
  itself, never only a news or blog summary), cite every claim with a link and
  a page number, and save a copy of each cited source in `docs/sources/` with an
  entry in `docs/sources/INDEX.md` so the user can open it right away. List the
  sources in the chat reply. Never offer "I did not read the full report" as a
  limit: fetch and read it. If a source cannot be fetched, say what was tried
  and ask for the file.
- Ask before using the user's browser or the Chrome extension.
- Never write or edit the user's homework summary. They write it themselves.
- No RuFlo/claude-flow — removed from this residency's tooling; see memory.

## Dog feeding (how every session works, added 2026-11-04)

The user follows the teacher's dog feeding method (Figma node 2390:7831, "Steps
to Produce Literally Anything"). Each new document is made from saved,
checked documents, never from chat memory.

> **RULE #1: EVERY DELIVERABLE IS PART OF ONE PROJECT (the owner's words, 2026-11-04,
> after repeated mistakes).** Market analysis, audience segmentation, competitive
> analysis, feature analysis, positioning and vision boards are not separate tasks.
> Each one is built on the ones before it and feeds the ones after it. Any research,
> table or step must use the structure the project already set: the two audiences
> (Audience 1 = adult child caring for a parent, Audience 2 = spouse or partner),
> the top caregiver problems, the market segments, the 5 criteria, and the open
> questions (such as who pays). **No research, reading pass or new table starts
> until `docs/research-checklist.md` is filled in and shown to the owner.** When new
> research changes one deliverable, say which other deliverables it changes, and
> update them in order.

- **Start of session:** ask for the latest dog feeding report in
  `../Resources/<week folder>/Dog Feeding Reports/` (newest `dogfood-*.md`) and the saved documents it lists.
  Read them all, then say what you have and what is missing.
- **Where reports go:** save every new dog feeding report or starting brief
  straight into `../Resources/<week folder>/Dog Feeding Reports/` (for example `Week 2_3`),
  organized by the course week. Ask which week if unsure.
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
- **One part at a time.** Do only the step the user asks, then stop and wait.
  The user makes each choice. Never start the next step or change other work
  unasked.
- **Order of work:** market analysis → competitive → feature → positioning →
  vision boards. New research updates the market analysis first.
- **Say where each answer came from** (which saved document or data file).
- **Remind the user to ask for a markdown file or report** at these moments,
  in one line at the end of the reply:
  1. A deliverable was approved: save it as a new markdown version, and open
     its pull request (one deliverable = one branch = one PR) so the owner can
     review and merge it.
  2. Before a new chat or a compact: write a dog feeding report.
  3. Something was redone or went wrong: write a short change report.
  4. Before moving to the next step in the order: check that the last
     deliverable's PR is merged (`gh pr list --state open`, or `gh pr view`). If
     it isn't, say one line: "<Deliverable>'s PR isn't merged yet. Merge it
     first, or keep going?" It's a reminder, not a block: the owner decides.
  5. End of the session.
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
- **Write for the owner (2026-11-05).** Every output (chat, reports, tables,
  Figma) uses UX writing best practices at an 8th-grade reading level: what it
  means first, then the number; full sentences; caregiver words, not research
  jargon ("supply," "coded," "keyword rule"). Test: would the owner understand
  it on first read?
- **Short replies, and say what you mean (owner, 2026-11-06, at 90% usage).**
  The owner has ADHD and reads fast, and every extra word costs usage.
  - Say only what the owner needs to act or decide. Cut recaps, filler and
    anything already saved in a file. Never paste the handoff report's
    "Paste to start" line in chat: it lives inside the report.
  - Never write "the results," "it," "that file" or "the test" without saying
    which one and where it is. The owner doesn't carry every earlier line in
    mind. Name it the first time, then keep it short.
  - Short words, one idea per line, and a small table instead of a paragraph.
- **Complete sentences with context, never shorthand (owner, 2026-11-13: "you
  keep repeating this same problem over and over").** Every sentence must make
  sense to someone who has not read the rest of the chat. Short means fewer
  sentences, not clipped fragments.
  - Never write a phrase that only makes sense if the owner remembers an earlier
    line, such as "link it, don't move it," "those copies," "the Week 2 pages,"
    "the hub," or a bare action word like "linked" or "synced."
  - When proposing or reporting an action, say all three parts in plain
    sentences: what I will do (or did), to which page or file (its name and where
    it lives), and what is different afterwards.
  - If a word could mean two things (for example "link" or "copy"), say which
    one in the sentence.
  - Test before sending: could the owner act on this line if it were the only
    line he read?
- **Questions get answers, not edits.** When the owner asks a question, answer
  it and stop. Change files only after a clear yes.
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
