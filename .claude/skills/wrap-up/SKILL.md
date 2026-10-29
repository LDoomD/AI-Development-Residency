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

Destination: **"Case Study Documentation, Reflections & Research Log"** page, inside the "TechFleet: AI Residency Resource Hub" workspace (`https://app.notion.com/p/4069219a4691803a8b23d9c753cb86e2`). Append a new dated entry — don't overwrite existing entries.

**Voice rule — this is the part most likely to get missed, so it's called out separately:** the entry must read like the user wrote it himself. That means:
- First person ("I decided...", "I realized...", "I ran into...") — not "the user" or "Claude did X."
- Built from what the user *actually said* this session (his own words/inputs), not from narrating the tool calls Claude made. If the user didn't say something close to it, it doesn't belong in the entry framed as his realization.
- Concise and well organized — this user has ADHD. Short paragraphs or bullets, clear headers, no dense walls of text. Skimmable over complete.

Keep the page's existing structure (dated entries, newest on top, tagged to the Preamble/Rags/Journey/Riches/Sequel story arc, a "What changed / Why / Challenges / Discoveries / Sources" shape) — just write the content in the user's voice going forward, not the AI-narrator voice used in earlier entries.

**Always surface the Notion page link in the wrap-up message itself** — don't make the user go hunting for it. State it even if nothing else about this step changes.

Note: the user may sometimes want to write the entry himself instead of having it drafted for him (said 2026-10-28, right after this skill was created) — if he says he's writing it himself for a given session, skip drafting it and just confirm the page link so he can go write it.

## 5. Set the next-session starting point

End with one short, explicit line: "Next session, start with: ___." Pull this from whatever was left open — don't invent a new direction.

## Notes

- This skill was created 2026-10-28 because no wrap-up routine existed in memory yet — the user had to explain it from scratch once. It should not need re-explaining again; if something about this process changes, update this file directly rather than re-deriving it from a conversation.
- RuFlo is not part of this — do not reintroduce it for any part of this routine (see memory: `ruflo-removed`).
