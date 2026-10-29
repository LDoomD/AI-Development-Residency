---
name: wrap-up
description: Closes out a Claude Code session end-to-end for this residency repo — summarizes progress, updates persistent memory, runs the full git workflow (branch/commit/push/PR), writes a dated reflection entry to the user's Notion log, and names the next session's starting point. Use whenever the user says "wrap up," signals they're ending a session (e.g. "I have to go," "that's it for today"), or asks what's left open before stopping.
---

# Wrap-up

The user has ADHD and often ends a session mid-thought to go do something else. "Wrap up" means close every loose end now, not "say goodbye." Permission to run the full routine below was already given when this skill was set up — don't ask step-by-step permission each time.

Copy this checklist and check items off as you go:

```
Wrap-up progress:
- [ ] 1. Summarize session progress
- [ ] 2. Update persistent memory
- [ ] 3. Git: branch → commit → push → PR
- [ ] 4. Notion reflection entry (ask opt-in question first)
- [ ] 5. Next-session starting point
```

## 1. Summarize session progress

Short, plain recap: what got done, what's still open. For skimming, not re-reading the transcript.

## 2. Update persistent memory

Save what's load-bearing, not everything that happened. Write a memory entry only for things that fit the memory system's types (user/feedback/project/reference) AND are one of: an explicit correction, a decision, a pattern repeated more than once this session, or something the user directly asked to remember. A single passing detail that won't matter next session doesn't need a memory file — memory bloats and gets harder to trust the same way a CLAUDE.md does when everything gets written to it.

## 3. Git — commit and push (the user works in VS Code, not this CLI)

Do the full git workflow yourself — the user isn't running git commands from this session:

- Check `git status` for anything changed this session.
- Follow the existing repo convention (see memory: `github-org-convention`): **feature branch → commit → push → open a PR**, never a direct commit to `main`.
- Branch name describes the session's work, not just "wrap-up" (e.g. `caregiving-market-research-segments`).
- Commit message follows the repo's existing style (see `git log` for examples).
- After pushing, open the PR (`gh pr create`) so it's ready for the user to review/merge — don't merge it yourself.
- Tell the user the PR link at the end.

## 4. Write the session's Notion reflection entry

**Destinations:**
- Hub page (overview + table view, sorted newest-first): `https://app.notion.com/p/4069219a4691803a8b23d9c753cb86e2`
- Database ("Reflections & Learnings Log"): `collection://ddf9e7b6-c36f-4324-8c3a-7f7317017785`

Create a **new page in the database** for the session (not an append to the hub page body). Properties: `Entry` (title, format `YYYY-MM-DD — short description`), `Date`, `Story Arc` (one or more of Preamble/Rags/Journey/Riches/Sequel), `Project`.

**First, ask a yes/no opt-in question** — don't skip straight to the guided Q&A: *"Want to write this session's reflection yourself, or should I draft it from our conversation?"*

**If yes (he's writing it):** ask the guided questions below, one at a time or as a short batch, and wait for him to actually type his own answers. Do not draft answers for him and ask him to approve them — that defeats the point. If his answer is short or rough, leave it that way; don't polish it into something he didn't say.

1. **What changed this session?** — what you actually did or decided.
2. **Why?** — what prompted that call, in your own words.
3. **What frustrated you or went wrong?** — challenges, friction, corrections you had to make.
4. **What did you realize or learn?** — the actual "aha," not a feature list.
5. **What's next?**
6. **Which story arc stage fits?** — Preamble / Rags / Journey / Riches / Sequel (can be more than one; give him the one-line definitions from the hub page if unsure).

Your job here is only to format his literal answers into the entry's shape and add sources/links/citations for anything factual that came up this session — he isn't expected to cite things from memory.

**If no (he doesn't have time to document):** write the entry yourself, drawing on the session's actual conversation history — not invented content. **Mark it as AI-drafted, visibly, every time:** open the entry with a callout stating Claude wrote this one from the session transcript because the user opted out, so anyone reading later (including him) knows it isn't his own words. Never let an AI-drafted entry pass as if he wrote it.

**Voice rule (for user-written entries only):** first person, his actual words from the Q&A — not a paraphrase, not an AI-narrator summary. Concise, skimmable, short bullets over dense prose.

**Always surface the Notion page link in the wrap-up message itself** — don't make him go hunting for it.

## 5. Set the next-session starting point

End with one short, explicit line: "Next session, start with: ___." Pull this from whatever was left open — don't invent a new direction.

## Changelog

- 2026-10-28: Skill created — no wrap-up routine existed in memory before this.
- 2026-10-29: Reflection log moved from a flat Notion page to a database (one page per session, filterable). Reflection step made a mandatory guided Q&A by default.
- 2026-10-29: Added the yes/no opt-out — if the user doesn't have time to write the reflection himself, Claude drafts it from session history instead, visibly marked as AI-drafted. Rewrote description to third person per Anthropic's skill-authoring guidance, added the step checklist, and capped memory writes to load-bearing items only (confidence-filtering idea borrowed from the `claude-wrap-up` community skill).

## Notes

- RuFlo is not part of this — do not reintroduce it for any part of this routine (see memory: `ruflo-removed`).
