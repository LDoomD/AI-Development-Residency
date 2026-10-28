---
name: residency-context
description: Local, verbatim copy of the full 8-week Tech Fleet AI Development Residency syllabus, class working agreements, homework submission process, and every week's coding challenge (Weeks 1-8), plus the weekly class materials that exist so far (Week 1, Week 2&3). Use whenever the user asks about the residency syllabus, a specific week's objectives or homework, class policies, submission requirements, or wants guidance on staying on track with residency deadlines — even if they don't say "syllabus" explicitly, e.g. "what's due this week", "what does week 5 require", "am I on track", "what's the Premium objective for week 6". Do not use for the user's own specialization project's product work (e.g. their app's PRD, architecture, or feature decisions) — only for questions about the residency program itself.
---

# Residency Context

This is a cached, local copy of the residency's Notion content, kept so Claude doesn't need to call the Notion MCP connector (and burn tokens/time) every session just to recall the syllabus. The actual source of truth remains Notion — see "Keeping this in sync" below.

## Rule: always read the file, never answer from memory of a prior turn

Before stating any residency requirement, deadline, deliverable, or policy, **read the relevant file in `reference/`** — don't answer from what you recall saying earlier in the conversation. The file is the answer; re-derivation or guessing from memory is not.

## Files

- `reference/syllabus.md` — full program overview, pricing, the reconciled 8-week curriculum table, skills/tools/outcomes taught, instructor bio.
- `reference/class-working-agreements.md` — how sessions run, teacher/student commitments, psychological safety, "one source of truth" policy.
- `reference/homework-submission-process.md` — general submission process (GitHub folder convention, PR workflow). Each student handles their own actual submission routing each week — this file is for reference/audit only.
- `reference/week-1.md` — Week 1 (How the Web Works) weekly materials + full coding challenge (Week 1 Claude Skills — already completed).
- `reference/week-2-3.md` — Week 2&3 (Product Delivery Management) weekly materials + Week 2 coding challenge (product specs — Premium track builds specs for their own chosen specialization app).
- `reference/week-3-coding-challenge.md` — Week 3 (Network Architecture, Nov 2): build + host the app on Vercel/Supabase/Material UI. Weekly-materials page is blank; this is the coding challenge only.
- `reference/week-4.md` — Week 4 (Data Engineering, Nov 9): AI chatbot for career coaching using O*NET data. **Mandatory same build for Standard and Premium** — not a specialization week.
- `reference/week-5.md` — Week 5 (Information Security, Nov 16): PenTest your Week 3 (or Week 5) app, OWASP/Aikido/WireShark. **Same for both tracks.**
- `reference/week-6.md` — Week 6 (Coding Architecture/QA, Nov 30): enterprise architecture refactor, ADRs, CI/CD gates. **Same for both tracks.**
- `reference/week-7.md` — Week 7 (APIs and Agents, Dec 7): integrate an API library. **Differs by track** — Standard picks from 4 named APIs for the ADHD app; Premium integrates into their own Week 3 app with their own API choice.
- `reference/week-8.md` — Week 8 (SEO/AEO, Dec 14): optimize for search engines and AI answer engines. **Same for both tracks.**
- `reference/recordings-log.md` — meeting-by-meeting log of what was covered, with links to notes/recordings.

## Cross-week pattern: when Premium matches Standard vs. doesn't

This matters for planning — don't assume every week lets a Premium-track student substitute their own specialization app for the Standard track's ADHD budgeting app:

| Week | Standard/Premium relationship |
| --- | --- |
| 2 | Differ — Premium builds specs for their own chosen app, not the ADHD budgeting app |
| 3 | Differ — Premium builds/hosts their own app |
| 4 | **Same** — everyone builds the O*NET career-coaching chatbot, regardless of specialization |
| 5 | **Same** — PenTest exercise, same for both |
| 6 | **Same** — enterprise architecture refactor, same for both |
| 7 | Differ — Standard picks from 4 named APIs for the ADHD app; Premium integrates their own API choice into their own app |
| 8 | **Same** — SEO/AEO optimization, same for both |

## Known inconsistencies in the source material (preserved, not silently fixed)

These are genuine artifacts in the instructor's own Notion content, confirmed by direct inspection — not copy errors on our end. Flag them if they become relevant rather than guessing which version is "right":

- **Repo naming drifts across weeks.** Week 2 says create a repo named "Week 3 - ADHD Budgeting App"; Week 3's own page gives two different names in different sections ("Week 3 Web App" vs "AI DEVELOPMENT RESIDENCY - WEEK 3 - APP"); Week 6 gives three different names across its own sections. Weeks 5, 7, 8 all say to reuse "the previous GitHub repository from Week 3" using the "AI DEVELOPMENT RESIDENCY - WEEK 3 - APP" name specifically. **Practical takeaway: one running repo from Week 3 onward, named "AI DEVELOPMENT RESIDENCY - WEEK 3 - APP" (or close to it), reused and merged into each week — the exact naming inconsistencies in the instructions don't change that underlying pattern.**
- **Week 2&3's weekly-materials page has a "Homework" section at the bottom that's a verbatim copy of Week 1's homework block** (same "Week 1 folder" reference, same checklist) — almost certainly a copy-paste template artifact, not real Week 2 homework. The real Week 2 homework is the separate Coding Challenge content. See the flag inside `week-2-3.md`.
- **Week 7's Premium objective text** reuses a phrase from the Standard objective ("usable for people who experience ADHD") that doesn't make sense for Premium's own-app track — likely another un-updated template copy. Preserved verbatim, flagged inline.
- A generic **"Submission Guidelines"** page says submit via "the Tech Fleet Network Platform under your weekly module," while every individual week's Coding Challenge page says "email the instructor the link." Each student handles this individually — not something this skill should resolve or act on.

## Known gaps (don't invent content for these)

- Weekly-materials pages for Weeks 3–8 (the lecture/objectives/learning-materials pages, as opposed to the coding challenges) are **blank** on the instructor's side as of 2026-10-28 — not yet taught/published. Only Week 1 and Week 2&3 have real weekly-materials content. Re-check these as each week approaches; don't assume they'll stay blank.
- The 6 Week 2 deliverable templates (audience segmentation, market/competitor/feature analysis, release vision/scope, epics/features/tasks, Kanban board, pitch deck) are titles only — their actual template content lives in the instructor's master Notion workspace and isn't accessible even via logged-in browser guest access.
- The Recordings Log has several session rows the instructor hasn't filled in yet (marked "not yet filled in by instructor") — that's the instructor's gap, not a copy error.

## Flagged, not acted on

Week 1's coding challenge page says: "CHANGE THE AI MODEL TO CLAUDE 4.8 - MEDIUM EFFORT... Always use 4.8 in this class." This is preserved verbatim in `reference/week-1.md`. No model setting has been changed based on it — it may predate the models actually available now. Surface this to the student if it becomes relevant again; don't silently comply or silently ignore it.

## Keeping this in sync

These files are a snapshot from 2026-10-28. If something seems off, outdated, or a week's blank weekly-materials page needs re-checking:

1. Check your own synced copy of the instructor's Notion content first via the Notion MCP connector, if you keep one.
2. If Notion's content itself changed (not just this local copy going stale), the original master pages live in the instructor's separate `tech-fleet-community-dao` workspace and may need a logged-in Chrome session (via the claude-in-chrome extension) to read, since the Notion connector may not have direct access there.
3. Update both your Notion copy and this local file together — don't let them drift apart silently.

No automatic re-sync is set up on purpose — handle updates when they come up rather than building automation for it.

## Verification note (2026-10-28)

All 8 weeks' coding challenges were pulled and scroll-verified in full after discovering that a single `get_page_text` call can silently truncate long pages (caught concretely on Week 3, Week 6, and Week 7 — each was missing whole sections on first pass, since corrected). Every file above reflects the scroll-verified, complete version. The one remaining unverified-from-scratch area is the 6 deliverable-template pages linked from Week 2 (inaccessible entirely, titles only).
