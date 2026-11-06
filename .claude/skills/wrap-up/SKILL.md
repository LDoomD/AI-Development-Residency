---
name: wrap-up
description: Closes out a Claude Code session end-to-end for this residency repo — summarizes progress, updates persistent memory, writes the handoff report for the next session, runs the git workflow (one branch and PR per deliverable, a plain-words pre-merge check, then hands the PR to the user with short steps to review and merge it themselves), writes a dated reflection entry to the user's Notion log, and names the next session's starting point. Use whenever the user says "wrap up," signals they're ending a session (e.g. "I have to go," "that's it for today"), or asks what's left open before stopping.
---

# Wrap-up

The user has ADHD and often ends a session mid-thought to go do something else. "Wrap up" means close every loose end now, not "say goodbye." Permission to run the full routine below was already given when this skill was set up — don't ask step-by-step permission each time.

**Edge case — check this before anything else:** if the user says he already wrapped up this session (e.g. "I already did that," "I'm done for today"), don't assume. Ask one question: **"Did you keep working after that, or is there nothing new since then?"**

- **He kept working** → run the full checklist below, steps 1-6, covering only what happened *since* the last wrap-up.
- **Nothing new** → skip the checklist. Just confirm out loud that git is pushed and the last reflection entry is saved, then stop.

Copy this checklist and check items off as you go:

```
Wrap-up progress:
- [ ] 1. Summarize session progress
- [ ] 2. Update persistent memory
- [ ] 3. Write the handoff report (dogfooding-handoff skill)
- [ ] 4. Git: branch → commit → push → PR → pre-merge check → hand the PR to the owner to merge
- [ ] 5. Notion reflection: ask yes/no first; if yes, 4 mandatory questions, one at a time
- [ ] 6. Next-session starting point
```

## 1. Summarize session progress

Short, plain recap: what got done, what's still open. For skimming, not re-reading the transcript.

## 2. Update persistent memory

Save what's load-bearing, not everything that happened. Write a memory entry only for things that fit the memory system's types (user/feedback/project/reference) AND are one of: an explicit correction, a decision, a pattern repeated more than once this session, or something the user directly asked to remember. A single passing detail that won't matter next session doesn't need a memory file — memory bloats and gets harder to trust the same way a CLAUDE.md does when everything gets written to it.

## 3. Write the handoff report

The step 1 summary is for the user to skim now. The handoff report is for the next session: a saved file it can start from without relying on chat memory. Use the **dogfooding-handoff** skill in write mode. It has the template, the check script, and where the file goes. Do this before step 4, so the report is committed and pushed with the rest of the work.

- If nothing changed since the newest handoff report, say so in one line and skip this step.
- If the dogfooding-handoff skill isn't available, say so in one line. Don't write a report from memory instead.

## 4. Git — branch, commit, push, pull request

Do the full git workflow yourself. The user isn't running git commands from this session. These steps follow GitHub flow and GitHub's pull request guidance; sources and the audit behind them: `caregiving-coordinator/docs/reports/wrap-up-github-audit-2026-11-06.md`.

**One deliverable = one branch = one pull request.** Small pull requests are easier to check and safer to merge. Name the branch after the deliverable (for example `feature-analysis-4`). Work that isn't a deliverable (a skill, a fix) follows the same rule: one task, one PR.

- **Deliverable not approved yet:** keep adding to the same branch and PR across sessions. The PR stays open.
- **Deliverable approved:** the PR is ready for review and merge (step 4b). The next deliverable starts a new branch.
- **Not sure if it's approved?** Check the newest handoff report (an **Approved** tag) or ask the owner once: "Is this deliverable approved?"

- **Check where things stand:** `git status`, the current branch, and whether its PR is still open (`gh pr view --json state`).
  - Open PR for the *same* task → keep using it.
  - PR merged or closed, or this session's work is a *different* task → start a new branch from the latest `main` (`git fetch origin` then `git switch -c <task-name> origin/main`). Ask first if the working folder has changes that aren't from this session: other sessions may be using it (see memory: `other-sessions-are-the-user`).
- **Never commit to `main` or push to it.** A local guard hook (`.claude/hooks/protect-main.mjs`) blocks this, because GitHub Free can't protect `main` on a private repo. If the guard blocks a command, follow its message; never work around it.
- **Branch name:** short and descriptive, about the task (e.g. `caregiving-feature-analysis-4`, `fix-login-timeout`), not "wrap-up".
- **Commits:** one commit per separate change, so any one change can be undone on its own. For example, the skill fix in one commit and the research notes in another. Commit message follows the repo's style (see `git log`). Only stage files from this session's work; never `git add -A` blindly.
- **Run the project's tests before pushing,** if it has any (for example `npm test`, `node --test`, `pytest`). Save the command and its result for the 4b table. If there are no tests, say so.
- **Push the branch,** then open the PR (`gh pr create`) with a description that has three short parts:
  - **What changed:** a few bullets.
  - **Why:** the problem it solves.
  - **Where to look:** the most important files, and anything risky.

### 4b. Hand the PR to the owner (learner mode)

The owner is new to GitHub and is learning to review and merge, so **the owner does the merge**. You open the PR, check it, and guide. **Don't run `gh pr merge`.** If the owner asks you to merge, remind them once that they chose to merge it themselves while learning, and merge only if they still say yes.

Only do this when the deliverable (or task) is approved. If it isn't, say "PR #N stays open until the deliverable is approved", give the link, and stop.

**Keep it short.** The owner has ADHD, so no paragraphs. First run the checks (`gh pr diff --name-only`, `gh pr view`, `gh pr checks`, `git fetch origin` then `git rev-list --count HEAD..origin/main`, and the project's tests). Then show exactly this:

**Your turn: review and merge PR #N**
Link: <url>
What it does: <one line>

| Check | Result | What it means |
|---|---|---|
| The right files | ✅ or ⚠️ | Only files from this task. Name any that don't belong. |
| Small enough to check | ✅ or ⚠️ | Say how many files. Flag mixed, unrelated work. |
| Nothing deleted by mistake | ✅ or ⚠️ | List deleted files, and whether that was intended. |
| No secrets | ✅ or ⚠️ | No passwords, keys or tokens. GitHub doesn't scan this private repo, so this is the only check. |
| No junk | ✅ or ⚠️ | No `.DS_Store`, `.textClipping`, temp or test leftovers. |
| Tests pass | ✅ or ⚠️ | The project's tests ran (show the command), or "no tests yet". |
| Checks pass | ✅ or ⚠️ | GitHub's automatic checks are green, or "no automatic checks on this repo". |
| Up to date with main | ✅ or ⚠️ | Has every commit from `main`. If not, update the branch first. |
| The description matches | ✅ or ⚠️ | What / why / where to look, and it matches the real changes. |

Keep each "What it means" cell under about 8 words in the output.

**Your steps on GitHub (about 5 minutes):**
1. Open the link. Read the description. Does it match what we did?
2. Click **Files changed**.
3. Look at these first: <the 2-3 files that matter most>. Skip `docs/sources/`: those are saved web pages.
4. Tick **Viewed** on each file you've looked at.
5. Confused? Ask me "what is this change in <file>?" before merging.
6. All good? Click the **Conversation** tab, then **Merge pull request**, then **Confirm merge**.

End with: "Tell me 'merged', or tell me what looked wrong."

If any row is ⚠️, say which, and replace step 6 with "Not yet: I'll fix it first."

**After the owner says "merged":**
- Check it: `gh pr view <number> --json state,mergedAt`. Confirm in one line.
- Offer to tidy up locally: switch to `main`, pull, delete the old local branch. Ask first: other sessions may be using this folder.

**If the owner reports a problem:** fix it on the same branch, push, and run the checks again.

**Later:** when the owner says they're ready to hand merging back, switch to the earlier mode: show the table, ask "Merge this PR into main now?", and run `gh pr merge <number> --merge` only on a yes.

## 5. Write the session's Notion reflection entry

**Destinations:**
- Hub page (overview + table view, sorted newest-first): `https://app.notion.com/p/4069219a4691803a8b23d9c753cb86e2`
- Database ("Reflections & Learnings Log"): `collection://ddf9e7b6-c36f-4324-8c3a-7f7317017785`

Create a **new page in the database** for the session (not an append to the hub page body). Properties: `Entry` (title, format `YYYY-MM-DD — short description`), `Date`, `Story Arc` (one or more of Preamble/Rags/Journey/Riches/Sequel), `Project`.

**The gate — ask this first, at every wrap-up (added 2026-10-31):** before any question, ask one yes/no: **"Do you want to document a reflection for this session?"** Use the AskUserQuestion popup with two options ("Yes, document it" / "No, skip it this time"). The answer applies to *this wrap-up only* — never carry it over from an earlier wrap-up, even the same day. He often jumps on and off several times in a day and may want to document the first time, skip the second, and document the third.

- **Yes** → run the questions below.
- **No** → skip this step completely: no Notion page, no questions, no nagging, no AI-drafted substitute. Say in one line that the reflection was skipped for this wrap-up. Steps 1, 2, 3, 4 and 6 still run.
- If two documented wrap-ups land on the same date, make each `Entry` title's short description different so they can be told apart.

His sessions can run up to 4 hours — by wrap-up he may be mentally done — so keep the *effort* per question as low as possible. **Once he answers yes at the gate, all 4 questions are mandatory, no skip** — he decided this explicitly (2026-10-29): the case study needs 8 weeks of real, complete data, and a skippable flow risked ending up thin exactly on the days it mattered most (the hard/exhausting ones). Also still true: **the instructor (Morgan) requires that case-study source data come from the student's own thinking, not AI.** Claude may help him answer faster by pre-filling a guess; Claude may never supply the answer itself.

**One exception (added 2026-10-29):** if he says he already answered these questions — through earlier conversation this session, or any other way — he can skip the formal Q&A for that session. Take his word for it, don't push back, don't re-ask. Everything else in this checklist (summary, memory, git, next-step) still runs regardless.

**Before question 1, say once (don't repeat every question):** "4 quick ones, one at a time — I'll show my best guess for each as a starting point. Confirm it, fix it, or replace it — one word is a completely fine answer, but I do need something from you on each one."

**Ask these 4 questions, one at a time (not all at once), labeled "Question X of 4" so he can see how much is left, and pre-fill each with a draft guess pulled from the session before you ask it — as a prompt to react to, not an answer to accept as-is:**

1. **What did you decide or get done this session, and why that choice over the others?**
2. **Where did the AI get something wrong, or where did you push back on it?**
3. **What was hard or frustrating, and how did it feel?**
4. **What did you learn that you didn't know before?**

(These four come from the field list in the user's `ai-case-study-journal` skill — what changed, why and what else was considered, what the AI did and what he did about it, how it felt, discoveries — rewritten 2026-10-31 in plain words. "What's next" is no longer a question: step 6 ends with the next-session line instead.)

(Story arc tag is *not* a question — classify Preamble/Rags/Journey/Riches/Sequel yourself from the content. That's tagging work, not reflection, and it isn't case-study source data in the way the 4 answers are.)

For each question: show your drafted guess first (1-2 lines, pulled from what actually happened this session) as something to confirm, correct, or replace. If he tries to skip or brush past one, say once that it's required and ask again — don't nag past that, just hold the line that an answer (even one word) is needed before moving to the next question.

**Voice rule:** every answer in this entry must actually be his words — confirmed or edited, never supplied by Claude. There is no skip path inside the questions and no AI-authored fallback in this step. The only ways a session goes unreflected are his "no" at the gate or the already-answered exception above — both are his call, never Claude's.

**Always surface the Notion page link in the wrap-up message itself** — don't make him go hunting for it.

## Setup requirements (before this skill can run at all)

This skill is a plain file in the repo (`.claude/skills/wrap-up/SKILL.md`), so it loads the same way in Claude Code's terminal, the Desktop app, and Claude Code in the browser — skill-loading isn't terminal-specific. But two things are **per-student account/environment setup, not part of the skill file**, and will silently fail step 4 or step 5 if missing:

- **Notion MCP connector must be connected on that student's own Claude account** before step 5 can write anywhere. Verified path (checked live, 2026-10-29): claude.ai → **Settings → Customize → Connectors → Discover tab → search "Notion" → Connect**. This is one account-level toggle — it applies the same whether that student then runs Claude Code from the terminal, Desktop app, or browser, since it's not an app-specific setting. If it's missing, step 5 has nowhere to write.
- **GitHub access for step 4.** Confirmed live in Settings → Claude Code: there's a real split between **local sessions (CLI, Desktop, IDE)** and **cloud sessions (Claude Code in the browser, claude.ai/code)** — cloud sessions have their own PR/branch settings (e.g. "Create pull requests automatically... applies to cloud sessions only"), meaning the browser surface does have real git/PR capability, but it's a separate authorization from local git. A student using only the browser needs their GitHub connected there — local `git`/`gh` config on their machine won't carry over.

**Honesty check on what's actually verified:** the account-level Notion connector setup and the local-vs-cloud-session split are both confirmed live in claude.ai's own settings UI, not assumed. What's still unverified is running this specific skill file end-to-end inside the Desktop app or claude.ai/code — that needs a real session in each, which hasn't happened yet from here. Don't tell students it's "tested on all three" until that's actually done.

## 6. Set the next-session starting point

End with one short, explicit line: "Next session, start with: ___." Pull this from whatever was left open — don't invent a new direction. If a handoff report was written in step 3, name it here and point to its paste-to-start line.

## Changelog

- 2026-10-28: Skill created — no wrap-up routine existed in memory before this.
- 2026-10-29: Reflection log moved from a flat Notion page to a database (one page per session, filterable). Reflection step made a mandatory guided Q&A by default.
- 2026-10-29: Added the yes/no opt-out — if the user doesn't have time to write the reflection himself, Claude drafts it from session history instead, visibly marked as AI-drafted. Rewrote description to third person per Anthropic's skill-authoring guidance, added the step checklist, and capped memory writes to load-bearing items only (confidence-filtering idea borrowed from the `claude-wrap-up` community skill).
- 2026-10-29: Replaced the yes/no gate + 6-question form with 4 questions, asked one at a time, each pre-filled with a drafted answer to confirm/edit/skip (not written from a blank box). Dropped the story-arc question entirely — Claude classifies it, user shouldn't have to. Driven by the user explicitly flagging 4-hour sessions and needing the reflection step to not be mentally exhausting; backed by NN/g's EAS form-design framework (eliminate/automate/simplify) and micro-journaling research on low-effort, skippable reflection.
- 2026-10-29: Removed the "AI fully drafts the entry" fallback entirely. Instructor requirement: case-study source data must come from the student's own thinking, not AI, even when visibly labeled as AI-drafted. Skipped questions now save as "not answered this session" instead of Claude's guess standing in as the recorded answer. Added a Setup requirements section covering Notion MCP connection and GitHub access for Desktop/browser Claude Code — flagged as documented-but-not-live-tested on those two surfaces.
- 2026-10-29: Removed the skip option entirely (including "skip all") — all 4 questions are now mandatory. User's explicit call: an always-skippable flow risked thin data on exactly the sessions that mattered most (the hard/exhausting ones), undermining the whole point of the log. Pre-filled drafts stay as the low-effort mechanism; what changed is that confirming/editing is no longer optional.
- 2026-10-31: Added a yes/no gate at the start of step 4, asked at every wrap-up (never carried over), because the user jumps on and off several times a day and may want a reflection some times and not others. Yes → the 4 mandatory questions as before. No → step 4 skipped entirely, other steps still run. Triggered by the user noticing a wrap-up went straight to the questions with no gate, which was true of the file as it stood after the 2026-10-29 "no skip" change.
- 2026-10-31: Rewrote the 4 questions. The user found "what happened and why" meaningless. The old wording came from merging questions to cut effort, not from journaling research. New questions are drawn from the `ai-case-study-journal` skill's entry fields (decision and why, where the AI was wrong or got pushed back on, what was hard and how it felt, what was learned) and the user approved the wording. "What's next" moved out of the questions into step 5.

- 2026-11-06: Added step 3, the handoff report (dogfooding-handoff skill), before git, so it gets committed. Owner's call after a check showed wrap-up only left a chat summary and a one-line next step, never a saved handoff report.

- 2026-11-06: Rewrote step 4 after a GitHub best-practices audit (docs/reports/wrap-up-github-audit-2026-11-06.md): one branch and one PR per task, one commit per separate change, run tests before pushing, a 3-part PR description, the main-branch guard hook, an up-to-date check, a size check, and local tidy-up after a merge.
- 2026-11-06: Step 4b is now learner mode: the owner reviews and merges the PR themselves, with a short 6-step guide and a check table that says what each line means. One deliverable = one branch = one PR; the PR stays open until the deliverable is approved. Owner asked for this because they are new to GitHub and don't want Claude to have full autonomy over merging.
- 2026-11-06: Added step 4b. Wrap-up now checks the PR (files, deletions, secrets, junk, checks, description), shows the result in plain words, and asks "Merge this PR into main now?". It merges only on a yes. Also checks the PR is still open before adding commits. Owner asked for this because he is new to GitHub and didn't know what to check.

## Notes

- RuFlo is not part of this — do not reintroduce it for any part of this routine (see memory: `ruflo-removed`).
