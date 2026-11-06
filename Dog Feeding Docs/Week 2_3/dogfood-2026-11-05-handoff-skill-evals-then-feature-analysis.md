# Handoff: Caregiving Coordinator → finish the dogfooding-handoff skill tests, then the feature analysis (2026-11-05)

Replaces: `dogfood-2026-11-05-handoff-feature-analysis.md` (its project outcomes are still correct and are summarized here; read it for the full tables)

> Paste to start: "Read this handoff report. Confirm in a few lines where we are. Then finish step 1 (grade the skill tests) and show me the results before doing anything else. Don't start the feature analysis until I say."

## 0. Start here
- Where we are: all three Week 2 deliverables so far are done, approved and on the clean Figma page: market analysis, audience segmentation and competitive analysis. Page 2782:15415 (`Dog Feeding Docs/Week 2_3/dogfood-2026-11-05-handoff-feature-analysis.md`, sections 1-3). After that, we built a new user-level skill, **dogfooding-handoff**, so every handoff report is written the same way. Its tests are half done.
- The outcome so far, in one sentence: the largest opportunity is helping worn-out caregivers reach relief (segments 11 and 12; `docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`). The handoff skill is built and triggers well, but its quality test isn't graded yet.
- Next milestones, in order:
  1. Finish the skill tests: grade the quality comparison and read the last trigger run.
  2. Then the feature analysis (homework deliverable #2, part 3), when the owner says.

## 1. Locked outcomes

**The project** (full detail in the replaced handoff, sections 3A-3C):
- Two audiences: adult children caring for a parent, and spouses or partners. **Approved** (`CLAUDE.md`, Rule #1).
- Largest opportunity: helping worn-out caregivers get relief. **Approved** 2026-11-05 (`docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`).
- The break research was merged into use case 1 for both audiences. **Approved** (`docs/clean-deliverables/audience-review-2026-11-05.md`).
- Competitive analysis: 9 competitors, 5 needs, 5 business questions, 4 gaps. **Approved** (`docs/clean-deliverables/competitive-preview-2026-11-05.md`).
- MVP scoring, "prioritize use cases" and the who-pays research wait for release vision. **Approved**.

**The skill:**
- A dog feeding report is a **handoff report**. The next session must be able to start the next milestone from it alone. **Approved** (`CLAUDE.md`, "A dog feeding report is a handoff report").
- Build it as a reusable, user-level skill for any project, with a check script, a hook and evals, following the earlier skill research. **Approved** (owner said "Yes, build it"; research in `docs/skills-build-baseline.md`).
- Files built: `~/.claude/skills/dogfooding-handoff/SKILL.md`, `references/report-template.md`, `scripts/check_handoff.py`, `tests/test_check_handoff.py`; hook `~/.claude/hooks/dogfood-handoff-trigger.mjs`, registered in `~/.claude/settings.json` under UserPromptSubmit. A backup of the settings is at `~/.claude/settings.json.bak-2026-11-05`. **Approved** (built on the owner's yes).
- Fixes to the hook and skill after the tests: **Proposed**, not yet approved (section 4).

## 2. Key findings and data

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Check script tests | 9 of 9 pass | `python3 -m unittest discover -s tests` in `~/.claude/skills/dogfooding-handoff/` | Authoritative |
| Trigger test, this project, with the hook | 24 of 24 fired; 0 of 20 wrong fires | `~/.claude/skills/dogfooding-handoff-workspace/trigger-results-real-project-hook.json` | Credible secondary (2 runs per query) |
| Trigger test, small code project, with the hook | 23 of 24 fired; 0 of 20 wrong fires | `trigger-results-code-project-hook.json` (same folder) | Credible secondary |
| Trigger test, this project, with no hooks (description only) | Still running when this was written | Will be saved as `trigger-results-real-project-nohook.json` | Not checked |
| Quality test reports written | 12 of 12 (2 tasks × with/without skill × Haiku, Sonnet, Opus) | `~/.claude/skills/dogfooding-handoff-workspace/iteration-1/<task>/<config>-<model>/report.md` | Authoritative (files exist) |
| Test agents blocked from saving their own file | 8 of 12; the orchestrator saved their text word for word (from the agent's message or transcript) | `timing.json` notes in each run folder | Authoritative |
| Earlier skill research: description alone vs with a hook | About 5% vs 98% trigger rate | `docs/skills-build-baseline.md`, sections 6 and 8 | Credible secondary |

## 3. Excluded and deferred
- **The feature analysis** is deferred until the skill tests are graded and the owner says go.
- **Skill-creator's `run_eval` tool** was not used for trigger tests. It tests a temporary copy of the description, and the real installed skill would get in the way. A custom runner was used instead: `run_trigger_eval.py` in the workspace.
- **The description optimization loop** (`run_loop`) is deferred until after grading.
- **Committing the skill:** not done. The skill lives in `~/.claude/skills/`, outside the repo. Whether to copy it into a repo is the owner's call.

## 4. Open decisions
- **The hook fires on subagent messages too**, not just the owner's own messages. It matched the word "handoff" in subagent reports. Proposed fix: skip prompts that start with an agent-message or system frame. Needs the owner's yes.
- **Where the skill lives long term:** user-level only, or also a copy in the project's `.claude/skills/` or a plugin, so it's backed up in git.
- **Update `docs/research-checklist.md`:** it still says "7 competitors" and "3 gaps" (should be 9 and 4). Flagged by 3 test agents. Change only with the owner's yes.
- **Section 4 of the market analysis:** a test agent read the record file and reported old to-do phrases still open. They were actually removed on Figma on 2026-11-05. The record file's "Still open" list is out of date. Fix that note with the owner's yes.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The 12 reports and `iteration-1/answer-key.json` | Grading: a fresh-agent test per report, plus `check_handoff.py` | Measures whether a new session can start from each report |
| The trigger results | The skill results summary for the owner | Shows the skill loads when it should, and only then |
| The test findings (hook false trigger, write blocks) | Skill fixes, iteration 2 | Fix, then rerun the tests |
| The replaced handoff (project outcomes) | The feature analysis | Inputs for the feature analysis research checklist |

## 6. First steps
1. **Grade the quality test.** For each of the 12 reports:
   1. Run `python3 ~/.claude/skills/dogfooding-handoff/scripts/check_handoff.py <report>`.
   2. Give a fresh subagent **only** the report and ask the 4 questions in `iteration-1/answer-key.json`.
   3. Score the answers against the key (assertions A1-A6).

   Save `grading.json` in each run folder. Then build `benchmark.json` with skill-creator's `aggregate_benchmark` (from `~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/skill-creator`), and show the owner the viewer (`eval-viewer/generate_review.py`).
2. **Read** `trigger-results-real-project-nohook.json` to see how much the hook adds compared with the description alone.
3. **Show the owner a short results summary** and the proposed fixes (section 4). Stop and wait.
4. **After the owner's go:** apply the fixes, rerun the tests as iteration 2, then write a new handoff.
5. **Then the feature analysis,** starting from `dogfood-2026-11-05-handoff-feature-analysis.md`, section 6.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. The ones most likely to be broken next:
- One part at a time. Questions get answers, not edits. Wait for a clear yes.
- Write for the owner: 8th-grade English, short replies, meaning first.
- Commit or push only when asked. Don't mention routine checks unless they find a problem.
- Don't change `~/.claude/settings.json` again without the owner's yes.
- Never present Claude's reading as the owner's decision.

## 8. Where things live
- **Skill:** `~/.claude/skills/dogfooding-handoff/` (SKILL.md, references/, scripts/, tests/).
- **Hook:** `~/.claude/hooks/dogfood-handoff-trigger.mjs`, set in `~/.claude/settings.json` (backup: `settings.json.bak-2026-11-05`).
- **Tests:** `~/.claude/skills/dogfooding-handoff-workspace/`:
  - `trigger-eval.json` (22 queries)
  - `run_trigger_eval.py`
  - `trigger-results-*.json`
  - `iteration-1/` (12 reports, `answer-key.json`, `timing.json` files)
- **Test projects:** a code project with decisions, a perf file and failing tests, in the session scratchpad (`.../scratchpad/shop-app2`). It may be cleaned up with the session.
- **Project:** clean Figma page 2782:15415; records in `caregiving-coordinator/docs/clean-deliverables/`; project handoff `Dog Feeding Docs/Week 2_3/dogfood-2026-11-05-handoff-feature-analysis.md`.
- **Git:** branch `feature-analysis`, PR LDoomD/AI-Development-Residency#23, last commit fcf84e1. This report is not committed. The skill files are outside the repo.

## 9. Verification receipt
- Outcomes and where each came from: sections 1-2 name a file for each item. Trigger numbers were read from the results files today. The unit test count comes from running the tests today.
- Checks run: `check_handoff.py` on this report; unit tests (9 pass); a pipe-test of the hook (fires on handoff wording, silent on others); `jq` validation of `settings.json`.
- Not checked: the no-hook trigger run (still running); the quality grading (not started); whether the new hook works in a fresh interactive session (only `claude -p` runs and this session were seen); the shop-app2 test folder surviving after the session.
- How this prevents drift: decisions are tagged Approved or Proposed. The feature analysis is explicitly deferred. The first step is to grade and show results before any fix or new work.
