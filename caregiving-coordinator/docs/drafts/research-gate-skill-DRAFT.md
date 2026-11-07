---
name: research-gate
description: Gate for any research, competitor or candidate list, market or audience summary, count, or recommendation drawn from saved or new data. Makes sure the owner's approved deliverables are read first, raw counts are never presented as findings, candidates come from the data and not from guesses, claims are read and synthesized in three passes, terms are explained in plain words, and nothing about people or audiences is assumed. Use before starting any research pass, before showing any list or table built from data, before saying anything is "data-driven", and when briefing a subagent to research. Also use for casual asks like "is this enough data", "what do we know", "where did that come from", "did you actually read it", or "what are the competitors". Do not use for code review, architecture, or writing code.
---

# Research gate

Born from 2026-11-06, when the owner lost hours to the same mistakes: conclusions built on raw counts, candidate lists from my own guesses, assumptions about the audience, jargon, and results shown without proof. Every rule below stops one of those.

## The rules

1. **The owner's approved deliverables come first.** Read them live (Figma node ids, or the newest file in `docs/clean-deliverables/`) before any research. Saved copies can be out of date. Say what was read, by node or file, and what was not.
2. **A raw count is not a finding.** A name count, a keyword hit count or a post count is only a filter. Label it "raw, not read." Never rank, recommend, or call anything "data-driven" from it. A finding needs every item read, sorted (used it / considering it / recommends or warns / vendor or ad / passing mention), with the outcome, the audience, and an exact quote checked by a script.
3. **Candidates come from the data.** Run a discovery pass over the coded or relevant posts and list every name a caregiver gives. Say where each name came from. Never present my own guess list as the list.
4. **Three passes before a conclusion.** Pass 1: read and sort the saved data. Pass 2: fill the thin spots from new sources. Pass 3: a fresh helper re-counts blind, checks every quote, and tries to disprove each finding. Say which passes ran.
5. **Define "enough" before looking, then say plainly if it is not met.** Default: 15 or more independent reports per item. If fewer exist, say what was searched and how many were found. Thin data means getting more data, not softer wording.
6. **Never assume facts about people, audiences or terms.** If it is not in a file, say "this is not in your files" and ask in one full sentence. Never add qualifiers the owner did not say (for example paid or unpaid caregivers).
7. **Plain words, always.** Explain every name and term the first time, in one sentence. Say "a break" before "respite." Table column titles are short titles ("Description," "Evidence"), never sentences. No codes, IDs or research jargon in cells.
8. **Conflicts are listed, never settled silently.** Where evidence differs from the owner's deliverable, list both sides with their sources. The owner decides. Never edit a deliverable without being asked.
9. **Respect robots.txt.** Read it first. Skip a page if it is disallowed for everyone or for ClaudeBot. Do not work around it. Log what was blocked.
10. **Tag every claim** with a state (proven, observed, inferred, documented, reported, not-assessed), a source, and a limit (use `skeptical-audit`).

## Before showing any result: 6 yes/no checks

- Did I read the owner's deliverable for this topic, and say which?
- Is every number either read-and-sorted, or labeled "raw, not read"?
- Does every name in the list say where it came from?
- Did three passes run, or do I say which did not?
- Is every term explained, and every column title a short title?
- Did I list the assumptions I made, or write "none"?

If any answer is no, fix it before showing anything.

## Brief for a research helper (paste into every subagent prompt)

> Read the owner's approved deliverables first (file or node named by me). Raw counts are not findings: read every item, sort it (used / considering / recommends or warns / vendor or ad / passing), record outcome, audience and an exact quote (20 words or fewer) that a script checks against the saved text. Find candidates from the data, not from a list I gave you. Report how many independent reports each item has; aim for 15 or more and say plainly if fewer. Respect robots.txt and never work around it. Tag every claim with state, source and limit. List conflicts with the owner's deliverable. Do not assume anything about the audience. Do not commit or edit existing files.

## Related

`skeptical-audit` (tagging claims), `docs/research-checklist.md` (shown before research starts), `CLAUDE.md` dog feeding rules (one part at a time, inputs table, plain writing).

---

# DRAFT ONLY. Not approved, not a skill, not wired into anything.

This file is a draft for the owner and Claude to review together. It was moved out of `.claude/skills/` on 2026-11-06 at the owner's request. Nothing here is active.

## Proposed CLAUDE.md additions (not applied)

1. Skills count line: "Fifteen project skills", plus a bullet for `research-gate`.
2. A "Research gate" rule block under "Rules for this folder" with the 8 short rules from the draft above.
3. In `.claude/hooks/emit-skills-directive.mjs`: one line in the SKILLS list and one line in the WHEN list, so subagents also get the rule.
