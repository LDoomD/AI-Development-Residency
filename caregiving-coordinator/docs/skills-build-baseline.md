# Skills build: baseline and plan

Recorded Sat 2026-10-31, about 12:50 PM PDT, **before any new skills or hooks are added**.
Purpose: have a "before" number so we can say what the build cost, then run one test round at the end.

## 1. Baseline measurements (before the build)

| What | Value | How measured |
|---|---|---|
| Prompt size on the first real request of this session | **about 41,370 tokens** (16,276 newly cached + 25,091 read from cache + 2 uncached) | `usage` fields on the first billed assistant message in this session's transcript (`c54fa91f...jsonl`, 2026-10-31 19:17 UTC) |
| Same measure, the previous session (resumed, so larger) | about 84,140 tokens | first billed message in `44fcca21...jsonl` |
| Project skills present | **6** (`accessibility-check`, `engineering-quality-check`, `project-prd-brainstorm`, `security-review`, `ux-ui-design-review`, `writing-security-tests`) | `ls .claude/skills/*/SKILL.md`. `security-review-workspace` is test material, not a skill |
| Project skill descriptions (always loaded) | about 3,600 characters, roughly 900 tokens | character count of the `description:` lines, divided by about 4 (rough estimate, not a tokenizer count) |
| Project skill bodies (load only when a skill triggers) | about 31,500 characters, roughly 8,000 tokens if every one loaded | `wc -c` on the six `SKILL.md` files, divided by about 4 (estimate) |
| User-level skills turned off | **95 off** (set to `"off"` in `~/.claude/settings.json`); 106 entries in `~/.claude/skills` | count of `skillOverrides` |
| Hooks | 1: `.claude/hooks/emit-skills-directive.mjs` (SessionStart, reminds only, enforces nothing) | file listing |
| CI | none (`.github` does not exist) | directory check |

**Limits of these numbers**
- The 41k figure is the whole first prompt: system prompt, tool names, memory, hook output and the first message. It is not the skills alone.
- It is one reading. The two sessions differ a lot, so treat it as a rough baseline and not a precise one.
- The 112-skills Doctor report was from Oct 29. The saving from turning 95 off has not been measured separately.
- Earlier pilot (Oct 29): one skill ran at about 50,594 tokens with the skill vs about 42,306 without, roughly 20% more, with assertions passing 100% vs 83%. One skill, one test.

## 2. Where the skills stand

- **Built:** the six skills above, plus the always-on SessionStart hook.
- **Not built (decided Oct 29, blocked once on a permissions issue, never retried):** `judge-arch`, `architectural-decision-records`, `skeptical-audit`, `enterprise-architecture-standards`, `owasp-secure-coding-bdd`. Also the receipt log and a `pre-done-gate` orchestrator.
- **Confirmed gap:** none of the review skills have a script behind them. All are LLM judgment. There is no arch-gate and no CI.
- **Rejected:** RuFlo / claude-flow.

## 3. What the community comments added (Simon Scrapes Agentic Academy post)

- **Rick Campbell:** use deterministic code instead of spending tokens on checks (accessibility testing was his example). Look at harness engineering, software factories, and Dave Farley on BDD.
- **Usman Mohammed:**
  - Anything with a pass/fail answer should be a script the skill runs, with the model only reading the result.
  - Description triggering alone is not reliable for gates. Call them explicitly with `/skill-name`, or use a hook so they fire whether Claude remembers or not.
  - Run each reviewer as a subagent that writes findings to a file, so the orchestrator only reads verdicts.
  - Asked which step in the chain uses the most tokens. No per-step measurement exists yet.
- **Testing guide (the "#5" Usman meant, from a Simon Scrapes resource):** three test types before shipping a skill: trigger tests, functional tests, quality comparison.

## 4. Plan (agreed order, widened 2026-10-31, nothing built yet)

**Decisions made (2026-10-31)**
- These skills are for building future enterprise-ready products, not only the caregiving app. Product-specific rules (health data, shared credentials) go in a config file or the project CLAUDE.md, not in the skill bodies. `security-review` currently has caregiving-specific "Extra categories" built in, so those move out.
- The approach is a mix: update an existing skill where the new check fits it (for example, `engineering-quality-check` runs the scripts), and add a new skill only where nothing existing covers the job.
- Skills are written fresh. Nothing is copied from Morgan's repo. Morgan's repo is a design model only, and the user said crediting it is not needed.
- Reviewer subagents: use fresh-context reviewer subagents for high-value checks only (for example architecture review before a PR). Anthropic's docs and independent tests say subagents cost extra tokens, so ask for short summaries back, consider a cheaper model for simple reviews, and measure the cost. The "subagent writes findings to a file the orchestrator reads" pattern is Usman's own practice only and is unverified, so it is not part of the plan yet. Morgan's `judge-arch` also mandates a fresh-context subagent review and a committed review log.
- Correctness and safety come before token cost. Morgan runs this style of setup on the $20 plan per the user.

**Order**
1. Record the baseline. Done: this file.
2. Build the mechanical parts first:
   - An arch-gate script that reads a config of forbidden patterns per folder, with expiring waivers. The app has no code yet, so it starts with a config to fill in as the architecture forms and is untested against real code.
   - A hook that forces the important checks to run, not only a reminder.
3. Add skills, written fresh and reusable across products, kept separate from the existing ones unless the mix rule says to extend one:
   - Architecture and decisions: `judge-arch` (review only), `architectural-decision-records`, `enterprise-architecture-standards`.
   - Evidence: `skeptical-audit`.
   - Security: `owasp-secure-coding-bdd`. It overlaps `security-review`, so its description must state the difference.
   - Added in the widening: test strategy, operations readiness (monitoring, alerts, recovery), release and deployment safety (rollback, staged deploys), and data lifecycle and compliance (collection, retention, deletion).
4. Update existing skills per the mix rule: `engineering-quality-check` runs the scripted checks, and `security-review` has its caregiving-specific categories moved out to config.
5. One test round over all skills: trigger tests, functional tests, quality comparison, and the same token measure as section 1, including a with-subagent versus without comparison for the reviewer.
6. Reply to Usman later, with real numbers.

**Coverage map (what an enterprise-ready product needs vs what exists)**

| Area | Exists | Planned |
|---|---|---|
| Security | `security-review`, `writing-security-tests` | scripted check, `owasp-secure-coding-bdd` |
| Correctness | `engineering-quality-check` | test strategy, arch-gate, `judge-arch` |
| Usability and accessibility | `ux-ui-design-review`, `accessibility-check` | scripted accessibility check later, once there are screens |
| Planning | `project-prd-brainstorm` | none |
| Operations | none | operations readiness |
| Release safety | none | release and deployment safety |
| Data lifecycle and compliance | none | data lifecycle and compliance |
| Architecture decisions | none | ADRs, architecture standards |

**Not in scope yet:** Farley-style BDD and harness engineering (background reading), community skills from search results (nothing installed).

**Open items:** which step uses the most tokens is unmeasured. Whether the existing hook also reaches subagents has not been checked.

## 5. Sources

- Morgan's `enterprise-software-AI-skills` repo (MIT, "with credit"): https://github.com/techfleetworks/enterprise-software-AI-skills. Read at a shallow clone in the session scratchpad. Nothing copied into this project.
- `lispking/harness-skills` and a community skill built on a Dave Farley talk: looked at via web pages only, nothing installed.
- Earlier research report from the Oct 29 session: `skills-research-report.md` (session scratchpad).
- Simon Scrapes Agentic Academy post and the two replies, pasted by the user on 2026-10-31.

## 6. Test round results (2026-10-31, after the build)

Three test types on the 9 new skills plus `security-review` and `engineering-quality-check` (11 skills). Raw files are in each skill's `<skill>-workspace/` folder (`trigger-eval.json`, `iteration-1/` or `iteration-2/` for security-review, with `benchmark.json`).

**1. Trigger tests (does the skill load?)**
- Description only (skill-creator's `run_eval`, empty scratch project plus the other skills, 12 queries x 3 runs per skill): the skills fired on **10 of 198** should-trigger runs and **0 of 198** wrong runs. Descriptions alone almost never trigger these skills in a one-shot prompt.
- With the real project setup (CLAUDE.md, SessionStart hook, all 15 skills; one run per query, 66 should-trigger queries): **56 of 66 fired (85%)**, and **0 of 66** negative queries fired the target skill. The forcing layer is what makes skills load, which supports the "hook, not a reminder" decision.
- Missed (10): casual wording with no keyword for `judge-arch` (2), and one each for ADR, architecture standards, skeptical-audit, test-strategy, operational-readiness, data-lifecycle, and `engineering-quality-check` (2).

**2. Quality comparison (with skill vs without, 2 tasks per skill, 1 run each)**
- Mean pass rate **98% with vs 76% without**. Mean tokens **48,475 vs 45,622 per run (+2,853, +6%)**.
- Biggest gaps: `enterprise-architecture-standards` 100% vs 25%, `owasp-secure-coding-bdd` 100% vs 62%. No gap: `judge-arch` (100% vs 100%). `release-deployment-safety` 75% vs 75%.

**3. Functional checks**
- Script and hook tests: 18 of 18 pass (`node --test .claude/skills/judge-arch/test/*.test.mjs`).

**Limits of this evidence**
- The assertions were written from each skill's own rules, so they favor the skill. Graders reported many assertions that both configs passed trivially. The gaps are mostly in process and format (evidence labels, "not checked" lists, proposed status, asking before assuming).
- One run per task, no repeats. Subagents were told to read the skill, so the quality test measures content, not triggering.
- `release-deployment-safety`: both configs failed the under-250-words check (the prompt allowed 300, so the check was stricter than the instruction) and both gave no concrete rollback steps.
- The hook blocking a real commit and SubagentStart delivery inside a real session are still untested.
- Trigger tests ran `claude -p`, close to but not identical to an interactive session.

## 7. Description fix for missed triggers (2026-10-31)

Added generic casual phrases (no product-specific wording) to 8 skill descriptions: judge-arch, architectural-decision-records, enterprise-architecture-standards, skeptical-audit, test-strategy, operational-readiness, data-lifecycle-compliance, engineering-quality-check.
- Fresh general queries (other kinds of products), real project setup, 1 run each: 26 of 34 fired (76%), 0 of 48 wrong fires.
- Same queries, 1 run each: 38/48 before and 38/48 after. Single runs were noisy.
- Old vs new wording, 3 runs per query, 3 skills: judge-arch 1/18 -> 9/18, skeptical-audit 13/18 -> 13/18, engineering-quality-check 6/18 -> 7/18, no wrong fires. New wording kept.
- Still weak: judge-arch (50%) and engineering-quality-check (39%). skeptical-audit misses on questions like "how do you know that" are partly a test artifact (one-shot prompts have no earlier answer to audit).
- Not re-tested after the edit: operational-readiness, data-lifecycle-compliance, test-strategy, architectural-decision-records and enterprise-architecture-standards beyond the single-run checks above.
