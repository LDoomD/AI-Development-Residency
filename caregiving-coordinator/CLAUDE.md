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

Each skill's own description says when to use it, and the session-start hook loads the list, so the one-line list of purposes was removed here (2026-11-18).

Hooks in `.claude/settings.json` force this instead of leaving it to
description-matching: `SessionStart` and `SubagentStart` load the skill list
(`.claude/hooks/emit-skills-directive.mjs`), and a `PreToolUse` hook blocks
`git commit` and `gh pr create` when `arch-gate.mjs` fails
(`.claude/hooks/arch-gate-before-commit.mjs`). Tests: `node --test
.claude/skills/judge-arch/test/*.test.mjs`.

## Rules for this folder

- **NEVER MAKE ANYTHING UP (owner's top rule, 2026-11-19: "live or die").**
  Every fact must come from a file, a command result or a source opened in
  this session, and the reply names it. If the handoff report does not mention
  something, do not assume it: look in the report's "Excluded and deferred"
  section, the memory index and git first. If it still is not found, say "I did
  not find this" or "I am guessing." Never present a guess, a gap or a missing
  item as a fact. Read the whole file before saying what it contains or leaves
  out; if only part was read, name the lines. Never judge one week's work
  against another week's requirements without saying so.
  Why: on 2026-11-19 a status message listed "gaps" (database columns, task
  pages for later epics, Foundation pages) that the saved build plan, backlog
  and handoff had marked as deferred on purpose. Only the first 60 of 245 lines
  of the build plan had been read.
  Enforced by hooks: `.claude/hooks/no-invention-rule.mjs` is shown at
  SessionStart and SubagentStart (inside the skills directive) and again on
  every message (`.claude/hooks/no-invention-reminder.mjs`, UserPromptSubmit).
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

- **Start of session:** ask for the latest dog feeding report in
  `../Resources/<week folder>/Dog Feeding Reports/` (newest `dogfood-*.md`) and the saved documents it lists.
  Read them all, then say what you have and what is missing.
  Then find the owner's current week and read its `../Resources/Week_N/MY STEPS - ...md` page (the owner is on Week 4 as of 2026-11-18). Keep the owner on those steps. If a request is not on the page, say so and ask first.
- **Git at the start of a session (Proposed 2026-11-18, not yet approved):** run `git fetch`, switch to `main`, run `git pull --ff-only`, then make a new branch for this task before the first edit. If the folder has uncommitted changes, say so and ask first.
  Why: GitHub merges do not change the local folder, so a stale branch hid Week 6 on 2026-11-18.
- **Where reports go:** save every new dog feeding report or starting brief
  straight into `../Resources/<week folder>/Dog Feeding Reports/` (for example `Week 2_3`),
  organized by the course week. Ask which week if unsure.
- **One part at a time.** Do only the step the user asks, then stop and wait.
  The user makes each choice. Never start the next step or change other work
  unasked.
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
  - **Every decision I ask the owner to make must explain itself (owner,
    2026-11-15).** When a summary or handoff recap lists open decisions, each
    one needs, in plain sentences: what it is, why it matters, the choices, and
    what happens after each choice. Never list a bare label such as "Approve
    box 5" or "Apply the 8 fixes." The owner cannot decide something he was
    not told about. If the owner says "not yet" to an item, leave it off the
    list until he brings it back.
- **Questions get answers, not edits.** When the owner asks a question, answer
  it and stop. Change files only after a clear yes.
- **Deliverable rules moved (2026-11-18):** Rule #1, the handoff report contents list, order of work, earlier-deliverables-lead, search-all-research, audience split, the table-answer rules, superseded-work banner and table rules are now in `docs/deliverables-rules.md`, word for word. Read that file before any market, audience, competitive, feature, positioning or vision-board work. The handoff report format is also in the `dogfooding-handoff` skill.
