# Handoff: Caregiving Coordinator → feature analysis (Feature Analysis 4) (2026-11-06)

Replaces: `dogfood-2026-11-05-handoff-skill-evals-then-feature-analysis.md` (all its steps are done). The full project tables (audience, market, competitive) still live in `dogfood-2026-11-05-handoff-feature-analysis.md`, sections 3A-3C. Read that one for the tables.

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what the feature analysis starts from. Then fill in docs/research-checklist.md for the feature analysis and show it to me before doing anything else. Keep replies short."

## 0. Start here
- Where we are: the three deliverables so far (market analysis, audience segmentation, competitive analysis) are approved and on the clean Figma page 2782:15415. Today we also finished the work habits for the rest of the course: the handoff skill is graded, the wrap-up routine follows GitHub flow, `main` is guarded, and an INVEST skill exists. All of it is merged to `main`.
- The outcome so far, in one sentence: the largest opportunity is helping worn-out caregivers reach relief (`docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`), and the next deliverable must turn that into a feature list the owner chooses.
- Next milestone: the **feature analysis**, built as a new version, Feature Analysis 4, on the clean page. It follows the teacher's format (Figma example 5:823, template 5:3064). After it: unique value proposition and positioning, release vision, then the INVEST backlog.

## 1. Locked outcomes

**The project** (full detail in `dogfood-2026-11-05-handoff-feature-analysis.md`):
- Two audiences: adult children caring for a parent, and spouses or partners. **Approved** (`caregiving-coordinator/CLAUDE.md`, Rule #1).
- Largest opportunity: helping worn-out caregivers get relief. **Approved** 2026-11-05 (`docs/clean-deliverables/market-analysis-clean-page-2026-11-05.md`).
- The break research is merged into use case 1 for both audiences. **Approved** (`docs/clean-deliverables/audience-review-2026-11-05.md`).
- Competitive analysis: 9 competitors, 5 needs, 5 business questions, 4 gaps. **Approved** (`docs/clean-deliverables/competitive-preview-2026-11-05.md`).
- MVP and MMP scoring, "prioritize use cases" and the who-pays research wait for release vision. **Approved**.
- The feature list is **Proposed** only: the owner chooses the features and fills the OUR COMPANY row (`dogfood-2026-11-05-handoff-feature-analysis.md`, section 6).

**Work habits and tools** (all merged to `main` on 2026-11-06 through pull requests 23 to 26 on `LDoomD/AI-Development-Residency`):
- **Handoff skill** `dogfooding-handoff`, with a check script and a hook. **Approved** (`.claude/skills/dogfooding-handoff/`).
- **Handoff hook narrowed:** fires only on specific phrases (dog feeding report, handoff report, "before I compact", "before I clear", "wrap up"). It ignores quoted lines, helper-agent messages and talk about the wrap-up skill. **Approved** (`.claude/hooks/dogfood-handoff-trigger.mjs`). Missed phrases go in `.claude/hooks/dogfood-handoff-misses.md`.
- **wrap-up skill:** writes the handoff report, follows GitHub flow, and runs in **learner mode**. **Approved** (`.claude/skills/wrap-up/SKILL.md`, steps 3, 4 and 4b).
  - **Learner mode:** Claude opens and checks the PR, then gives the owner 6 short steps. **The owner reviews and clicks merge.** Claude does not run `gh pr merge`. If the owner asks, Claude reminds once, then follows their answer.
  - **One deliverable = one branch = one PR.** The PR stays open until the deliverable is approved.
- **Main-branch guard:** a local hook blocks Claude from committing on or pushing to `main`. **Approved** (`.claude/hooks/protect-main.mjs`, registered in `~/.claude/settings.json`; backup `~/.claude/settings.json.bak-2026-11-06`).
- **`CLAUDE.md` reminders:** at deliverable approval, open its PR. Before the next deliverable, check the last PR is merged. **Approved** (`caregiving-coordinator/CLAUDE.md`, "Remind the user" list).
- **INVEST skill** `invest-task-scoping`. **Approved** (`.claude/skills/invest-task-scoping/`). The minimal version is merged (PR 26). The owner then asked for the full build, made on 2026-11-06 and merged in PR 27: a rewritten `SKILL.md`, a worked example, a sources page, a check script, a trigger hook (`.claude/hooks/invest-trigger.mjs`, **switched on 2026-11-06** by the owner's yes: linked into `~/.claude/hooks/` and registered under UserPromptSubmit in `~/.claude/settings.json` with a guard that does nothing if the file is missing; settings backup `~/.claude/settings.json.bak-2026-11-06b`), tests and evals. It grades the 6 letters, splits work over 2 weeks, writes the course task template with Given/When/Then, ends with a receipt and waits for the owner's yes. The owner chose: use for homework and code, "small" means up to 2 weeks, outcomes not solutions.
- **Short replies and owner-first (owner, 2026-11-06):** say only what the owner needs to act or decide; name which result or file you mean; never repeat the report's "Paste to start" line in chat. When the owner asks for something different from the report's first steps, do that first. **Approved**, merged in PR 28 (`caregiving-coordinator/CLAUDE.md`, "Short replies, and say what you mean"; handoff skill step 7 and receive step 3).
- **wrap-up PR hand-off shortened** to about 40 words in chat (link, "all 9 checks passed", 3 actions); the full check table goes in the PR description. **Approved**, merged in PR 29 (`.claude/skills/wrap-up/SKILL.md`, step 4b).
- **Repo settings:** the repo stays **private** (the owner's decision). The plan is GitHub Free, so branch protection is not available on a private repo (`docs/sources/github-practices/github-plans.md`, line 47). Dependabot alerts were turned on. **Approved**.

**Proposed, not decided:** a reminder when a deliverable is approved, a start-of-session alert, and the two INVEST modes (full stories for code, grades and checks only for homework analyses). The modes are built into the skill but the owner hasn't confirmed them.

## 2. Key findings and data

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Handoff skill quality test, with vs without the skill (12 reports, 2 projects, 3 models) | 94% vs 80% pass rate | `.claude/skills/dogfooding-handoff-workspace/iteration-1/bench/benchmark.json`; viewer `Dog Feeding Docs/Week 2_3/handoff-skill-test-results-2026-11-06.html` | Credible secondary (one run each; the format check favors the skill) |
| Fresh readers answering 4 questions from each report | All 6 with-skill reports passed; 1 of 6 without-skill reports missed the two audiences | same folder, `grading.json` in each run folder | Credible secondary |
| Hook tests | 30 of 30 pass | `node --test .claude/hooks/dogfood-handoff-trigger.test.mjs` | Authoritative |
| Handoff skill unit tests | 9 of 9 pass | `python3 -m unittest discover -s tests` in `.claude/skills/dogfooding-handoff/` | Authoritative |
| Casual phrasings the narrowed hook alone misses | 5 of 16 in the test set; the skill description alone loaded the skill for 5 of the 6 phrases it missed at the time | `.claude/skills/dogfooding-handoff-workspace/trigger-results-description-only-after-narrowing.json` | Estimate (2 runs each) |
| INVEST skill trigger test | 3 of 3 right prompts fired, 0 of 3 wrong | `.claude/skills/invest-task-scoping-workspace/trigger-results-invest-first-test.json` | Estimate (1 run each) |
| INVEST skill output length on a real run | About 4,600 characters for the minimal version; 3,305 for the full build (54 lines, still above the 30-line target) | chat only (one run each) | Estimate |
| INVEST check-script tests | 13 of 13 pass | `python3 -m unittest discover -s tests` in `.claude/skills/invest-task-scoping/` | Authoritative |
| INVEST hook tests | 25 of 25 pass | `node --test .claude/hooks/invest-trigger.test.mjs` | Authoritative |
| INVEST live trigger test (hook on, 1 run each) | 7 of 12 right phrases loaded the skill (3 of the 5 misses are "offer" phrases the test can't score), 0 of 12 wrong | `.claude/skills/invest-task-scoping/evals/trigger-results-full-build-hook-on.json` | Estimate |
| INVEST hook alone on the 24 test phrases | Fires on 11 of 12 right phrases, 0 of 12 wrong; the missed one ("this story feels too big") is left to the skill description | `.claude/skills/invest-task-scoping/evals/trigger-eval.json` run through the hook | Estimate |
| Size of the last 6 PRs before the new rules | 5 to 591 files each; PR 23 had 407 files | `caregiving-coordinator/docs/reports/wrap-up-github-audit-2026-11-06.md` | Authoritative (read with `gh`) |
| Owner's usage when this was written | 5-hour limit 83% (resets 20:49 UTC), weekly 48% | chat only, read from the app's usage tool | Estimate |

**Facts about the course (from the owner's NotebookLM, a secondary summary of the course files; verify before relying on them):**
- Week 2 submission: the Notion Product Specs page, plus a folder `Week 2 Coding Challenge` in the repo holding `submission.md` and markdown copies of the specs. Push it on a branch, open a PR, **merge it**, then email the instructor the links.
- **The owner writes "What I Did" and "What I Learned" (2+ paragraphs each) with no AI.** Claude never drafts or edits them.
- Instructor wording: "small" = "one week or two weeks"; no exact INVEST prompt exists; he never lists when NOT to use INVEST.
- The schedule file quotes Week 2 as due Nov 2, which looks like the schedule before the extension. The owner says Week 2 was extended and the instructor doesn't mind lateness. The new date is not known.
- Source of record: `docs/sources/usage-tools/` and `docs/sources/github-practices/` hold saved copies of the pages used today (indexed in `docs/sources/INDEX.md`, partly uncommitted, see section 8).

## 3. Excluded and deferred
- **Parked until release vision (deliverable #3):** MVP and MMP scoring (Figma 2598:11009), prioritize use cases (2378:7243), who-pays research (employers, Medicare GUIDE, families).
- **The week's remaining deliverables** (not started): feature analysis, positioning, vision boards, INVEST backlog, build plan, Kanban, pitch deck, the submission folder.
- **Dropped:**
  - putting the syllabus into wrap-up (advised against; the `residency-context` skill already holds it, and may be out of date)
  - a usage display in the app (the owner dismissed it; the research is in `docs/sources/usage-tools/`)
  - making the repo public (the owner said no)
- **Not required for Week 2:** the JSON receipt log (`docs/skill-receipts/log.jsonl`). NotebookLM places it in the Week 1 enterprise skills readme, enforced in Week 6. The INVEST skill uses a simple receipt block.
- **Live evals of the full INVEST skill:** the 24-phrase trigger test (1 run each, hook on) is done: **7 of 12 right phrases loaded the skill, 0 of 12 wrong ones did** (`.claude/skills/invest-task-scoping/evals/trigger-results-full-build-hook-on.json`, added in the records PR). Of the 5 misses, 3 are the start-of-deliverable phrases, where the hook only tells Claude to *offer* INVEST, so the test (which counts only the skill loading) can't score them; check the reply text for an offer instead. The 2 real misses: "this story feels too big. is it small enough?" and "turn this feature into stories with acceptance criteria" (the second may be noise, 1 run). Next: add "too big" wording to the description and hook, rerun those two with 2 runs each. Still to run after the owner's usage resets: the 6 quality prompts in `.claude/skills/invest-task-scoping/evals/evals.json` (with vs without the skill, graded with `scripts/check_invest.py`). Then tune the description once if it misses.
- **Later:** share the skills with another student. Set up and test first, then write setup steps. Hooks and settings do not travel with a skill. Wrap-up needs a clean copy first (it holds Notion links and personal rules).
- **If "help applying for programs" becomes a feature:** read posts about qualifying for all programs, starting from `docs/sources/competitive-analysis-3/va-check/research-checklist-va-2026-11-05.md`.

## 4. Open decisions
The next session must not decide these alone.
- **The feature list, and what goes in the OUR COMPANY row.** The owner's.
- **Who pays.** Needed before positioning.
- **The new Week 2 due date.** Unknown. Ask NotebookLM: "Quote the lecture note where the instructor extends Week 2. What is the new date?"
- **Should INVEST run on homework analyses,** or only on backlog tasks? NotebookLM says the instructor never says. The owner has not decided.
- **The duplicate audience section 2061:543 in FigJam,** and keep or remove the Feature Analysis 3 gaps rewrite.
- **The Week 2-3 NotebookLM slides** (need the owner's sign-in or a PDF).
- **The instructor's repo invite is still pending** (`mdenner1234`, write access, sent 2026-10-22). The owner must make sure it is accepted. Check with `gh api repos/LDoomD/AI-Development-Residency/invitations`.
- **Wrap-up in the app repo:** it lives only in the homework repo. Decide whether to copy it to the app repo when that exists.
- **Confirm the two INVEST modes** (backlog and homework).
- **Merge the records pull request** (this report, the research sources, the test results page and the INVEST trigger result). The owner merges.
- **The owner's new plan:** their Max plan ended 2026-11-06 and they move to a Tech Fleet enterprise plan. The type is unknown. Usage-based Enterprise has no plan limits; seat-based has. Settings → Usage shows it either way (`docs/sources/usage-tools/usage-tools-research-2026-11-06.md`).

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The 4 competitive gaps | The feature list | Features should fill the gaps (`docs/clean-deliverables/competitive-preview-2026-11-05.md`) |
| The 9 competitors | The ✅/🚫 table, one row each | Only the approved 9 are rows by default |
| Use case 1 scenarios for both audiences | Candidate features | Each feature must say which audience it serves |
| Feature Analysis 3 (Figma 2584:10359, `docs/feature-analysis-3.md`) | A banner, then kept | Its how-well evidence table and "relatives join rarely works" finding are still useful |
| The research checklist (`docs/research-checklist.md`, now says 9 competitors and 4 gaps) | The first step | Rule #1: nothing starts until it is filled in and shown |
| INVEST skill and task template | Deliverable #4, the backlog | Epics, features and tasks, up to 2 weeks each |
| Learner mode and one PR per deliverable | How this deliverable is saved | The feature analysis gets its own branch and PR |

### The approved results it builds on (copied 2026-11-06 from `dogfood-2026-11-05-handoff-feature-analysis.md`, section 3C; record: `docs/clean-deliverables/competitive-preview-2026-11-05.md`)

**The 5 caregiver needs** each competitor was scored on: (1) understand what's happening and what to do next; (2) real relief for the caregiver; (3) the parent's money, papers and accounts; (4) works when the parent refuses help; (5) relatives share the work.

**The 9 competitors** (Y = yes, P = partly, N = no):

| Competitor | Type | 1. Understand | 2. Relief | 3. Money and accounts | 4. Parent refuses | 5. Relatives share |
|---|---|---|---|---|---|---|
| Caring Village | Direct (app) | P | P | P | N | P |
| Everplans | Direct (vault) | N | N | Y, if the parent filled it in | N | P |
| Cariloop | Direct (employer-paid coach) | Y | P | Y | P | P |
| A Place for Mom | Direct (free; senior living pays referral fees) | P | P | P | N | N |
| Geriatric care managers | Direct (paid by the hour) | Y | Y, for a price | P | P | P |
| Group texts and notebooks | Indirect (free workaround) | P | N | P | P | P |
| Area Agencies on Aging | Indirect (free government program) | P | P | P | N | N |
| Respite and adult day services | Indirect (local care; mostly families pay) | P | Y, when families can get it | N | N | N |
| VA caregiver programs | Indirect (government; veterans only) | P | Y, if approved | P | N | P |

Prices and counts are in the source file; they are left out here on purpose.

**The 4 gaps** (the unique value opportunities):
1. **No one handles a parent who refuses help, or gets relatives to share the work.** Opening: help that works around a refusing parent and splits real tasks among relatives.
2. **Personal, ongoing guidance is locked behind an employer or a big hourly bill.** Opening: coach-level guidance at an affordable price, or sold through employers.
3. **Help with money and accounts works only if the parent prepared ahead.** Opening: getting caregivers into accounts after the parent can't set it up. Risk: health data and consent.
4. **Relief exists, but caregivers can't reach it.** Opening: help caregivers find, qualify for, pay for and use relief. This is the approved market opportunity.

## 6. First steps
1. **Confirm in a few lines** where we are, and read the results block at the end of section 5. Check the owner's usage first (`mcp__ccd_session_mgmt__get_usage`): if the 5-hour limit is near full, say so before any research. If the INVEST full build is still uncommitted (section 8), offer to save it as one PR first.
2. **Fill in `docs/research-checklist.md` for the feature analysis and show it. Stop and wait.** It must list the inputs, split by audience, and name the questions.
3. **Search saved docs for feature topics** (relief, respite, eligibility, refusing parent, accounts) and show the inputs table: each input, used or left out, and why.
4. **Propose the feature list** from the gaps, needs and scenarios (the examples are in `dogfood-2026-11-05-handoff-feature-analysis.md`, section 6, step 3). The owner chooses.
5. **Mark ✅/🚫 per competitor from saved sources only** (`docs/sources/competitors-4/` and the competitive cells). If something is missing, research it, cite it, save it.
6. **Preview in markdown first.** Then build Feature Analysis 4 on the clean page and put a big yellow banner on Feature Analysis 3.
7. **Save it the new way:** work on a new branch from `main` named for the deliverable (for example `feature-analysis-4`). When the owner approves it, open the PR, run the checks, and hand it over in learner mode. Don't merge.
8. **Then:** unique value proposition and positioning (one statement per audience), then release vision.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. The ones most likely to be broken next:
- One part at a time. Questions get answers, not edits. Wait for a clear yes.
- **Short replies** (rule in `CLAUDE.md`): answer first, a small table or a few bullets, no walls of text. Name which result or file you mean. Never repeat the report's "Paste to start" line in chat. If the owner asks for something different from the first steps, do that first.
- **The owner merges their own PRs.** Never run `gh pr merge` in learner mode. Use the short hand-off format in the wrap-up skill (about 40 words), link the key files with working links, and remember the repo is private (they must be signed in to GitHub).
- **Never write or edit the owner's homework summary** ("What I Did" and "What I Learned").
- Cite every claim, save copies of sources in `docs/sources/` with an `INDEX.md` entry. For course facts, ask the owner to query NotebookLM, and end the question with "quote the source file and exact words."
- Ask before using the owner's browser or the Chrome extension. Don't change `~/.claude/settings.json` without a yes.
- Commit or push only when asked. Never commit on `main` (the guard blocks it).
- Never delete deliverables. Mark replaced ones with a big yellow banner.
- No RuFlo or claude-flow. Never suggest caregiver interviews.

## 8. Where things live
- **Clean Figma page:** 2782:15415 (file HcDDdEGAnikTImO8v7UPMp). Market analysis 2808:13693, 2812:14373, 2813:14661, 2815:15035. Audience 2834:2844, 2834:2867, 2834:16750. Competitive 2843:15117.
- **Records of the clean work:** `caregiving-coordinator/docs/clean-deliverables/`.
- **Skills (repo `.claude/skills/`):** `dogfooding-handoff`, `invest-task-scoping`, `wrap-up`, `residency-context`. The first two are linked into `~/.claude/skills/`, so they load in every project. `wrap-up` is only in this repo.
- **Hooks (repo `.claude/hooks/`):** `dogfood-handoff-trigger.mjs` (+ test, + misses list) and `protect-main.mjs`, both linked or registered through `~/.claude/`.
- **Test results (git-ignored `-workspace` folders):** `.claude/skills/dogfooding-handoff-workspace/` and `.claude/skills/invest-task-scoping-workspace/`.
- **Audit report:** `caregiving-coordinator/docs/reports/wrap-up-github-audit-2026-11-06.md`.
- **Git:** pull requests 23 to 29 are merged, so `main` has everything except the records PR. The working copy is on branch `records-2026-11-06`. Pull requests 23 to 26 are merged. Eight older local branches remain (they look merged, not touched).
- **INVEST full build** (merged in PR 27): `.claude/skills/invest-task-scoping/` (`SKILL.md`, `references/` with worked example, sources and misses list, `scripts/check_invest.py`, `tests/`, `evals/`), `.claude/hooks/invest-trigger.mjs` and its test, and `caregiving-coordinator/docs/sources/invest/` (4 saved sources, indexed in `docs/sources/INDEX.md`).
- **In the records PR** (open when this was written):
  - `.claude/skills/invest-task-scoping/evals/trigger-results-full-build-hook-on.json`
  - `caregiving-coordinator/docs/sources/INDEX.md` (edited)
  - `docs/sources/github-practices/` (5 new files: `about-pr-reviews.md` and 4 `skills-*.md`)
  - `docs/sources/usage-tools/` (2 files)
  - `Dog Feeding Docs/Week 2_3/handoff-skill-test-results-2026-11-06.html` and this report
  - the owner's `dogfood-2026-11-05-audit-and.textClipping` (leave it alone)

## 9. Verification receipt
- Outcomes and where each came from: sections 1-2 name a file or command for each item. PR states, branch state, test counts and the invite status were read from `gh`, `git` and the test commands on 2026-11-06.
- Checks run: `check_handoff.py` on this report; hook tests (30 of 30); handoff unit tests (9 of 9); the benchmark file re-read for 94% and 80%.
- Not checked: the owner's usage numbers are live and will change. The full INVEST skill's live trigger and quality evals (only one live run was done). The INVEST hook is on, but it was only pipe-tested and only the trigger batch was started live. Whether the desktop app shows a status line. The Week 2 submission list and the course dates (NotebookLM summaries, not the original files). The new Week 2 due date. Whether the instructor can currently see the repo. Whether learner mode works well over several real PRs (it has run on PR 25 and 26 only).
- How this prevents drift: decisions are tagged Approved or Proposed, parked items list where they come back, the first step is the research checklist shown to the owner before any research, and the course facts name their source.
