---
name: wrap-up
description: Run this whenever the user says "wrap up," "let's wrap up," "wrapping up for now," or otherwise signals they're ending a session (e.g. "I have to go," "that's it for today"). Closes out the session end-to-end — don't just summarize and stop.
---

# Wrap-up

The user has ADHD and is often ending a session mid-thought to go do something else (walk the dog, etc.). "Wrap up" means close every loose end now, not "say goodbye." Do these steps in order, every time, without asking permission for each one individually — permission to run the full routine was already given when this skill was set up (2026-10-28).

## 1. Summarize session progress

Short, plain recap: what got done, what's still open. This is for the user to skim, not re-read the transcript.

## 2. Update persistent memory

Save anything from this session that fits the memory system's types (user/feedback/project/reference) per the memory instructions already in context — new facts, corrections, decisions. Don't skip this because it feels redundant with the summary; memory is what survives into the next session, the summary is not.

## 3. Git — commit and push (the user works in VS Code, not this CLI)

The user is not going to run git commands themselves from this session — do the full git workflow:

- Check `git status` for anything changed this session.
- Follow the existing repo convention (see memory: `github-org-convention`): **feature branch → commit → push → open a PR**, never a direct commit to `main`.
- Branch name should describe the session's work, not just "wrap-up" (e.g. `caregiving-market-research-segments`).
- Commit message follows the repo's existing style (see `git log` for examples).
- After pushing, open the PR (`gh pr create`) so it's ready for the user to review/merge from VS Code or GitHub — don't merge it yourself.
- Tell the user the PR link at the end.

## 4. Write the session's Notion reflection entry

As of 2026-10-29, this is a **database**, not a flat page — restructured because Notion's own best practice is database-over-subpages for anything filterable by date/theme, and it gives one real page per day instead of one giant scrolling page ([Atlas Workspace](https://www.atlasworkspace.ai/blog/notion-for-journaling), [AI Tool Pick](https://aitoolpick.org/blog/notion-databases-best-practices-2026/)).

- **Hub page** (overview + linked table view, sorted newest-first): `https://app.notion.com/p/4069219a4691803a8b23d9c753cb86e2`
- **Database** itself ("Reflections & Learnings Log"): `collection://ddf9e7b6-c36f-4324-8c3a-7f7317017785`

Create a **new page in the database** for the session (not an append to the hub page body). Set properties: `Entry` (title, format `YYYY-MM-DD — short description`), `Date`, `Story Arc` (one or more of Preamble/Rags/Journey/Riches/Sequel), `Project`.

**Mandatory guided Q&A (set 2026-10-29) — he types the answers, every time, no exceptions:** this is the step most likely to get skipped under pressure (he's tired, in a hurry, etc.) — don't let that happen. Ask these questions in the chat, one at a time or as a short batch, and wait for him to actually type his own answers before writing anything to Notion:

1. **What changed this session?** — what you actually did or decided.
2. **Why?** — what prompted that call, in your own words.
3. **What frustrated you or went wrong?** — challenges, friction, corrections you had to make.
4. **What did you realize or learn?** — the actual "aha," not a feature list.
5. **What's next?**
6. **Which story arc stage fits?** — Preamble / Rags / Journey / Riches / Sequel (can be more than one; give him the one-line definitions from the hub page if he's not sure).

Do not draft answers for him and ask him to approve them — that defeats the point. If he gives a short or rough answer, that's fine; don't pad it into something more polished-sounding than what he actually said. **Your job is only:** format his literal answers into the entry's shape, and add sources/links/citations for anything factual that came up this session (market data, APIs, research, etc.) — he won't have those memorized and isn't expected to cite them himself.

**Voice rule:** the entry must read like he wrote it himself — first person, his actual words from the Q&A, not a paraphrase and not an AI-narrator summary of what Claude did. Concise, skimmable, short bullets over dense prose — he has ADHD.

**Always surface the Notion page link in the wrap-up message itself** — don't make him go hunting for it.

If he explicitly says he wants to write the whole entry himself instead of doing the guided Q&A for a given session, skip the questions and just hand him the database link.

## 5. Set the next-session starting point

End with one short, explicit line: "Next session, start with: ___." Pull this from whatever was left open — don't invent a new direction.

## Notes

- This skill was created 2026-10-28 because no wrap-up routine existed in memory yet — the user had to explain it from scratch once. It should not need re-explaining again; if something about this process changes, update this file directly rather than re-deriving it from a conversation.
- RuFlo is not part of this — do not reintroduce it for any part of this routine (see memory: `ruflo-removed`).
