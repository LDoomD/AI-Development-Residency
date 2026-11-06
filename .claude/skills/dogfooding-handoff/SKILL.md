---
name: dogfooding-handoff
description: "Writes and reads handoff reports for dog feeding: one saved markdown file that lets a fresh session, or the same session after a compact, continue a project from checked documents instead of chat memory. Write mode: use when the user asks for a report, a handoff, something to paste into a new chat, a recap before compacting or ending a session, or when a deliverable or milestone was just approved and the next one is about to start. Receive mode: use when the user pastes or points to a handoff, dogfood or session report and wants to pick up where they left off. Also use for casual asks like 'wrap this up so I can start fresh', 'write something I can feed you tomorrow', 'save where we are before I compact', or 'here's my report, read it first', even if the user never says 'handoff'. Do not use for status updates written for other people, release notes, changelogs, decision records, meeting notes, or summaries of an outside article."
---

# Dogfooding handoff

Dog feeding means every new piece of work is made from saved, checked documents, not from chat memory. A new chat starts empty, and a long chat slowly drifts from what was decided. The handoff report is the bridge between sessions: **the next session should be able to start the next milestone from this one file**, without the owner re-explaining anything.

This skill has two modes: **write** a handoff, and **receive** one.

## Ground rules (why they matter)

1. **Outcome first.** Before writing, name the next milestone and what it needs. Every section must help the next session start it correctly. A diary of what happened doesn't, so leave it out.
2. **From files, not memory.** Pull every outcome, number and decision from a saved file, and put the file path or link next to it. Chat memory is where numbers drift. If something only exists in the chat, save it first, or mark it "chat only, not saved."
3. **Owner decisions vs proposals.** Tag each outcome **Approved** (the owner decided) or **Proposed** (suggested, not decided). Otherwise a suggestion reads as a decision, and the next session builds on it.
4. **Actual results, not just links.** Include the key tables, verdicts, answers and numbers the next milestone needs. Links are for checking, not for re-reading everything.
5. **Say what's excluded or deferred, and when it comes back.** This is what stops the next session from reopening settled questions or bringing back work that was set aside.
6. **Project rules live in the project.** Point to the project's rule files (CLAUDE.md, AGENTS.md, README) and list only the rules most likely to be broken next. Don't copy them all.
7. **Never overwrite an older report.** Write a new file, say which reports it replaces, and add a one-line "Replaced by" note to the old ones.
8. **Plain words.** Follow the project's writing rules. If there are none, write so a newcomer understands on first read.

## Write mode

1. **Gather:** read the project's rule files, the newest earlier handoff (so you know what this one replaces), and the files of record for each finished milestone.
2. **Name the next milestone** and what it needs (its template, homework or definition of done). If it's unclear, ask the owner one question.
3. **Fill in `references/report-template.md`** section by section. Read it now; it shows what each section holds, with examples.
4. **Check:** run `python3 scripts/check_handoff.py <report-path>` (the path to `scripts/` is relative to this skill's folder) and fix every failure. The script checks what can be checked mechanically: required sections, the "Replaces" line, sources next to numbers, Approved/Proposed tags, and a "Not checked" list.
5. **Fresh-session test:** reread the report as if you knew nothing. Can you answer these four questions from the report alone?
   - Where are we?
   - What was decided?
   - What's excluded?
   - What's the first step?

   If not, fix it. For an important milestone, if subagents are available, give a fresh subagent only the report and ask it those four questions.
6. **Save** where the project's rules say. If they say nothing, use `docs/handoffs/`. Name it `<YYYY-MM-DD>-handoff-<next-milestone>.md`, unless the project has its own naming rule. Add the "Replaced by" note to the older reports.
7. **Tell the owner** in a few lines: where it's saved, what it replaces, and the paste-to-start line. Commit or push only if the owner or the project rules say to.

## Receive mode

1. **Read the whole report,** then every file it lists under "Where things live" or "Files to read."
2. **Reply briefly:**
   - where we are, in 1-2 lines
   - the next milestone
   - which files are present and which are missing
   - any conflicts between the report and the files: files win, but flag it to the owner
3. **Follow the report's first steps.** If they say to show something before starting (a checklist, a plan), show it and stop.
4. **Treat Approved outcomes and exclusions as settled.** Don't reopen them unless the owner asks. Treat Proposed items as open.

The same steps apply when a report is fed back in the same session after a compact.

## Length

Most handoffs run 150 to 400 lines. Detail the next milestone doesn't need stays in the linked files.
