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
- [ ] 4. Notion reflection entry (4 pre-filled questions, one at a time, each skippable)
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

His sessions can run up to 4 hours — by wrap-up he may be mentally done. Don't hand him a blank 6-item form. Instead:

**Before question 1, say once (don't repeat every question):** "4 quick ones, one at a time — I'll show my best guess for each, you can confirm, edit, or say 'skip.' Say 'skip all' any time to bail out of the whole thing and I'll just draft the entry." That escape hatch matters — without it, someone who wants out has to sit through 4 separate skips instead of 1.

**Ask these 4 questions, one at a time (not all at once), labeled "Question X of 4" so he can see how much is left, and pre-fill each with a draft answer pulled from the session before you ask it:**

1. **What happened and why?** — merge "what changed" + "why" into one question; they're always answered together anyway.
2. **What frustrated you or went wrong?**
3. **What did you realize or learn?**
4. **What's next?**

(Story arc tag is *not* a question — classify Preamble/Rags/Journey/Riches/Sequel yourself from the content. That's tagging work, not reflection, and he shouldn't have to do it.)

For each question: show your drafted guess first (1-2 lines, pulled from what actually happened this session), then ask him to confirm it, edit it, replace it, or say "skip." Make it explicit up front that one word or "yep, that's right" is a completely fine answer — don't make him feel like he owes you paragraphs.

- **He confirms or edits →** that question's answer is his, in his voice.
- **He skips a question →** your drafted guess stands for just that one section, and that section (and only that section) gets a small inline note that it's Claude's draft, not his words. The rest of the entry stays unaffected.
- **He skips all 4 →** the whole entry is AI-drafted — open it with a visible callout saying Claude wrote it from the session transcript because he opted out. Never let an AI-drafted entry pass as his own words.

**Voice rule:** anything attributed to him must actually be his words (confirmed or edited), not a paraphrase and not an AI-narrator summary. Concise, skimmable, short bullets over dense prose.

**Always surface the Notion page link in the wrap-up message itself** — don't make him go hunting for it.

## 5. Set the next-session starting point

End with one short, explicit line: "Next session, start with: ___." Pull this from whatever was left open — don't invent a new direction.

## Changelog

- 2026-10-28: Skill created — no wrap-up routine existed in memory before this.
- 2026-10-29: Reflection log moved from a flat Notion page to a database (one page per session, filterable). Reflection step made a mandatory guided Q&A by default.
- 2026-10-29: Added the yes/no opt-out — if the user doesn't have time to write the reflection himself, Claude drafts it from session history instead, visibly marked as AI-drafted. Rewrote description to third person per Anthropic's skill-authoring guidance, added the step checklist, and capped memory writes to load-bearing items only (confidence-filtering idea borrowed from the `claude-wrap-up` community skill).
- 2026-10-29: Replaced the yes/no gate + 6-question form with 4 questions, asked one at a time, each pre-filled with a drafted answer to confirm/edit/skip (not written from a blank box). Dropped the story-arc question entirely — Claude classifies it, user shouldn't have to. Driven by the user explicitly flagging 4-hour sessions and needing the reflection step to not be mentally exhausting; backed by NN/g's EAS form-design framework (eliminate/automate/simplify) and micro-journaling research on low-effort, skippable reflection.

## Notes

- RuFlo is not part of this — do not reintroduce it for any part of this routine (see memory: `ruflo-removed`).
