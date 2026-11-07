# Handoff: Caregiving Coordinator → competitive analysis update, then the feature table (2026-11-06, evening)

Replaces: `dogfood-2026-11-06-handoff-feature-analysis.md` (its first steps were done; its tables about the 9 competitors, 5 needs and 4 gaps still stand and are not repeated here). The project tables are still in `dogfood-2026-11-05-handoff-feature-analysis.md`, sections 3A to 3C.

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what is next. Show me the final competitor candidate table with plain-word explanations of every name before doing anything else. Keep replies short, plain, and one question at a time."

## 0. Start here
- **Where we are:** the three deliverables (market analysis, audience segmentation, competitive analysis) are approved and live in Figma on page 2782:15415. Today we researched the 9 existing competitors on 9 features in three passes, and researched new competitor candidates for the kinds of relief caregivers actually use. Nothing from today is committed.
- **The outcome so far, in one sentence:** none of the 9 competitors gives an ordinary family caregiver a strong, open way to reach relief; relatives sharing the work, account access and a parent who refuses are almost always limited or missing (`docs/sources/feature-analysis-4/*/AUDIT-PASS3.md`).
- **UPDATE (owner, later on 2026-11-06): the report work is STOPPED.** The owner said "Let's just stop this already. I don't need this anymore." A short report exists (`docs/reports/working-with-claude-analysis-2026-11-06.md`) and a longer earlier draft (`research-problems-analysis-2026-11-06.md`). Do not extend either, and do not rerun the history helper unless the owner asks. The partial event log is in `docs/sources/research-history/` (48 events through Nov 4). Skip step 1 and step 2 below; start at step 3.
- **Two tasks were first, in this order (now stopped; only the second continues):**
  1. **The report for the owner's teacher meeting (tomorrow, 2026-11-07):** an analysis of why the three deliverables keep being redone, built from the full history since Oct 14. Draft exists. It is the owner's "last report from Claude."
  2. **Update the competitive analysis,** then build the feature table sample for review, then put it in Figma.

## 1. Locked outcomes
**Approved by the owner this session (2026-11-06):**
- The Figma deliverables are the source of truth. Feature Analysis 3 and the teacher's example are format only. **Approved.**
- Order of work: update the competitive analysis first, then build the feature comparison table, show a sample for review, then put it in Figma. **Approved.**
- Include all the differences between the new evidence and the competitive analysis (the draft now has 20 cells, in `docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`). **Approved** ("No" to leaving any out).
- Delete the 23 pages saved from aplaceformom.com (its robots.txt blocks ClaudeBot). **Approved and done.** That company's page-based verdicts count as "verify."
- The audience is "anybody": any caregiver, paid or unpaid, registered or not. **Approved.** The research did not split paid from unpaid (see section 4).
- NotebookLM is out for research, forever. **Approved** (memory `notebooklm-out-of-research.md`).
- Do not run the INVEST skill on analysis work. **Approved** (memory `invest-not-for-feature-analysis.md`).
- Never create or change rules or skills without the owner taking part. **Approved.** A rules draft was moved to `docs/drafts/research-gate-skill-DRAFT.md` and is not active.
- A ✅ means the product offers the feature and a 🚫 means it does not. **Approved** ("The checkmark just means yes"). How to show a limited offer is unresolved (section 4).
- Facebook and WhatsApp are not part of the "group texts and notebooks" competitor. **Approved.** Online caregiver communities may be a separate row.

**Proposed, not decided:** the competitor candidates (section 2), the 20 changed cells (`docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`), and the research rules draft (`docs/drafts/research-gate-skill-DRAFT.md`).

## 2. Key findings and data

**Final audited verdicts for the 9 existing competitors** (Y = yes, L = limited to some people, N = no, V = verify). Source: the `AUDIT-PASS3.md` in each company's folder under `docs/sources/feature-analysis-4/`. Confidence: Credible secondary (three passes, quotes script-checked; "independent" means a different post, not a proven different person).

| Company | Relief finder | Eligibility | Paying | Refusing parent | Relatives cover | Accounts | Guidance | Behavior/talks | People |
|---|---|---|---|---|---|---|---|---|---|
| Caring Village | L | N | L | N | L | N | L | L | N |
| Everplans | N | N | N | N | N | L | N | L | N |
| Group texts, notebooks | N | N | N | N | L | L | N | N | V |
| Cariloop | L | L | L | V | L | V | L | L | L |
| A Place for Mom (pages withdrawn) | L | L | L | V | N | N | L | V | L |
| Geriatric care managers | Y | L | L | L | L | L | Y | L | V |
| Area Agencies on Aging | L | L | L | N | L | L | L | L | L |
| Respite and adult day | Y find / L get | L | Y info / L pay | N | L | N | L | L / V | V |
| VA caregiver programs | L | L | L | L | L | N | L | L | L |

Notes (sources: the nine `AUDIT-PASS3.md` files named above): A Place for Mom's row rests on Reddit, BBB and older pages only. Everplans account access works only on the paid plan and after a death. Cariloop works only through an employer or insurer. About 1,000 quotes were checked in total, with almost no invented ones.

**Competitive analysis changes drafted:** 20 cells in `docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`. Four rest on pages saved in `docs/sources/competitive-analysis-4/live-pages/` (New York memo 26-TAM-01, Illinois and Massachusetts money management programs, VA Veteran Directed Care; ARCH only partly supported). Confidence: Credible secondary.

**New competitor candidates, after reading and independent audit** (`docs/sources/competitive-analysis-4/<folder>/SYNTHESIS.md` and `AUDIT.md`). Raw counts were wrong in meaning: "Home Instead 53" was mostly "at home instead of."

| Candidate | Independent reports | Verdict | Confidence | Source |
|---|---|---|---|---|
| Care.com (marketplace for paid caregivers) | 52 posts, 13 with a result, 18 users | Enough to include | Credible secondary | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |
| Medicaid and state paid-family-caregiver programs (IHSS 77, PACE 41, hospice respite 32 or more) | 78 | Enough | Credible secondary | `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| VA caregiver programs | 19 or more new | Already a row | Estimate | `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| Alzheimer's Association groups and helpline | 19 (10 from Reddit only; 9 from its own forum) | Enough, with a caution | Estimate | `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| Support groups (any) | 37 read of 114 or more | Enough | Credible secondary | `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| Facebook caregiver groups | 21 (mostly negative) | Enough as a workaround row | Estimate | `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| Therapist (as a type, not a brand) | 123 (27 worked, 10 mixed, 23 did not, 63 none) | Include as a type | Credible secondary | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |
| Aide paid by the family (type) | 84 (12/17/19/36) | Include as a type | Estimate | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |
| Aide paid by a program (type) | 41 (6/11/11/13) | Include as a type | Estimate | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |
| Visiting Angels, Home Instead, BetterHelp | 13 (4 used), 8 (3 used), 4 | Not enough | Estimate | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |
| Papa, Talkspace, Headway, Wellthy, Lotsa, Cozi, CaringBridge, Meal Train, Teepa Snow, NAMI | 0 to 6 each | Leave out | Estimate | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` and `docs/sources/competitive-analysis-4/support-government-community/AUDIT.md` |
| CareYaya | 6 asking, 0 users | Not enough | Estimate | `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md` |

Also found (source: `docs/sources/competitive-analysis-4/paid-help-and-therapists/AUDIT.md`): 39 paid-aide posts name a refusing parent, and only 3 worked. Most paid-help failures are "could not get it" (waitlists, minimum hours, eligibility, cost), not "it was bad." Meals on Wheels has about 45 real mentions but meets a food need, not relief.

**Research tools** (evidence: `docs/sources/reddit/arctic-shift-2026-11-03/log*.txt`, helper reports): Arctic Shift saved posts work, but the bulk download was cut short (49 of 53 log lines were timeouts) and replies came only by post id; Firecrawl works on allowed company, government and PDF pages and not on Reddit, BBB or Trustpilot; saved forums work (ALZConnected is the Alzheimer's Association's own forum); NotebookLM rankings could not be reproduced and are retired.

**Session record** (transcripts in `~/.claude/projects/...-caregiving-coordinator/`; times Pacific; active = gaps under 15 minutes): about 13 conversation sessions from Oct 29 to Nov 6, about 54 active hours, about 1,000 owner messages. 9 of the 13 opened with a version of "pick up where we left off." The longest ran Nov 4 11:11 to Nov 6 12:20 (49 hours wall, 20 active, 338 messages). Three sessions started at 16:25 on Nov 3. The Oct 28 session that began market research is listed but its transcript was not found. Confidence: Estimate.

## 3. Excluded and deferred
- **Feature Analysis 3 as a content source.** It stays only as a format reference and gets a yellow banner in Figma at the end.
- **MVP and MMP scoring, prioritize use cases, who-pays research:** still parked until the release vision deliverable (from the earlier handoff).
- **Raw name counts as evidence.** Retired.
- **The research rules and skill draft:** deferred until the owner and Claude review it together.
- **A Place for Mom's own website:** off limits (robots.txt).
- **Clubhouse-style live audio rooms for caregivers:** the owner's idea, noted as a possible feature or competitor type, not researched.

## 4. Open decisions
The next session must not decide these alone.
- **Limited offers:** Cariloop offers coaching, but only if an employer pays. Should that cell be ✅ (it offers it) or 🚫 (most caregivers cannot use it)? The owner said both "✅ with limits is not okay" and "the checkmark just means yes." Unanswered. The data keeps four states (YES, LIMITED, NO, VERIFY) so this converts in one step.
- **Hard talks:** does help with hard talks alone earn a ✅ in "behavior and hard talks help," or only if both parts are offered? Unanswered.
- **Which competitors to add** to the competitive analysis. The owner has not seen the final corrected table of candidates (section 2) and has not chosen.
- **Paid and professional caregivers:** the owner said "anybody." The deliverables center on family caregivers and set paid workers aside in the relief research. Decide whether to say so in the audience page (optional).
- **The 20 changed cells:** approve each Yes, Partly or No change, especially Yes to Partly (Everplans, Cariloop), No to Partly (A Place for Mom, Area Agencies, respite, VA) and Partly to No (group texts).
- **The rules and skill draft:** review together before anything is wired in.
- **NotebookLM for course facts:** the owner said never again for research. Ask once whether that also covers course-fact lookups.
- **Still open from the earlier handoff** (`dogfood-2026-11-06-handoff-feature-analysis.md`, section 4): the new Week 2 due date, the instructor repo invite (`mdenner1234`), the duplicate audience section 2061:543, wrap-up in the app repo, the owner's new enterprise plan type.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The audited verdict grid | The feature table (✅/🚫 after the owner's rule on limited offers) | It is the evidence for each cell |
| The 20 changed cells | The updated competitive analysis | Figma and the new evidence differ |
| The candidate table | New rows in the competitive analysis, then the feature table | The competitor set lacked paid aides, therapists and support groups |
| Care.com, programs, communities scored on the 5 needs | The competitive analysis rows | Each chosen candidate still needs scoring with evidence |
| The history analysis | The report for the teacher | The owner needs dates, sessions and where problems occurred |

## 6. First steps
1. **Check the history helper's output:** `docs/sources/research-history/EVENT-LOG.md` and `ANALYSIS.md`. If absent, it did not finish. Rerun it (brief: rebuild every redo event from Oct 14, with date, deliverable, trigger, who found it, cause category, evidence; first occurrence and repeats of each cause; rules broken again). Do not trust it until a script checks its commit hashes and quotes.
2. **Finish `docs/reports/research-problems-analysis-2026-11-06.md`** (the draft exists):
   - Go back to the start: dates, times, number of sessions, lengths, and where problems occurred (sessions table in section 2).
   - Five lenses, each with evidence: data analyst (themes, counts, who caught each error: the owner caught about 12 of today's 19, checks about 7), UX designer (the research journey and pain points), psychologist (the error, correction, apology, repeat loop; mental load from jargon, multi-part questions and open decisions; label everything as observation or hypothesis, no diagnosis), linguist (the owner's prompts and Claude's replies: pronouns like "this" and "it," words with several senses like "research," "update," "enough," "caregiver," three rating scales for one idea, before-and-after prompt rewrites), systems thinking (the redo loop, delays, where one change helps most).
   - Three passes: (1) draft, (2) a script confirms every cited file exists and every number matches its source, (3) a fresh helper tries to find unsupported claims.
   - **Owner's own finding (stated 2026-11-06, reported, not yet tested):** early on the owner was not verifying Claude's outputs as closely, and the errors surfaced once the owner started checking. Test this against the history helper's "who found it" tally by date, and include it in the report as shared responsibility without blame: the checking step was missing from the process, not from any one person.
   - Leave out personal details such as reading needs. It is Claude's analysis, not the owner's "What I Did" and "What I Learned." Optionally add a short list of questions to ask the teacher.
   - Show it to the owner before anything else. It is the last report the owner wants.
3. **Show the owner the final candidate table** (section 2) with plain-word explanations of every name, and ask which to add.
4. **Score each chosen candidate on the 5 needs** with evidence, add them to the competitive draft, and show the whole updated competitive analysis in one piece. Then put it in Figma, as its own pull request.
5. **Build the feature table as a markdown sample for review** (teacher's layout, blank OUR COMPANY row, an evidence row under each question, ✅/🚫 per the owner's rule, "verify" where unsettled), then put it in Figma, then add a yellow banner on Feature Analysis 3.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files. Most likely to be broken next:
- **Read the owner's Figma deliverables live** before any research, and say which node was read.
- **A raw count is not a finding.** Read and sort every item. Never call anything data-driven from a count.
- **Candidates come from the data,** never from Claude's own list.
- **Never assume facts about the audience** or add words the owner didn't say (paid, unpaid, registered).
- **Plain words:** explain every name and term. Table column titles are short titles ("Description," "Evidence"). Full sentences. One question at a time. No shorthand like "Figma says can't be made to do that" without naming the cell.
- **Questions get answers, not edits.** Do not create files, branches, rules or skills the owner hasn't approved.
- **Respect robots.txt,** including a ClaudeBot block. Never work around it.
- **Three passes** (read, add sources, fresh blind audit that tries to disprove) before showing a conclusion.
- **The owner merges their own pull requests.** One deliverable, one branch, one pull request.
- **Never write or edit the owner's homework summary.** Never use NotebookLM or INVEST for this work.
- **Keep replies short.** The owner also compacts before 60% context; check usage with `get_usage` and warn early.

## 8. Where things live
- **Figma:** file `HcDDdEGAnikTImO8v7UPMp`, clean page 2782:15415. Market 2808:13693, 2812:14373, 2813:14661, 2815:15035. Audience 2834:2844, 2834:2867, 2834:16750. Competitive 2843:15117. The teacher's feature table example is node 5:638.
- **Repo:** `/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator` (note the space before the slash in "Residency /").
- **Research evidence:** `docs/sources/feature-analysis-4/<company>/` (EVIDENCE, PASS1, PASS2, AUDIT-PASS3 per company, about 244 files); `docs/sources/competitive-analysis-4/` (`live-pages/`, `paid-help-and-therapists/`, `support-government-community/`); `docs/sources/research-history/` (history helper, may be incomplete).
- **Drafts and reports:** `docs/clean-deliverables/competitive-analysis-4-changes-draft-2026-11-06.md`; `docs/reports/feature-analysis-4-change-report-2026-11-06.md` (13 errors; needs the three-pass results added); `docs/reports/research-problems-analysis-2026-11-06.md` (draft report for the teacher); `docs/research-checklist-feature-analysis-4-2026-11-06.md`; `docs/drafts/research-gate-skill-DRAFT.md` (inactive).
- **Memory:** `/Users/landodoom/.claude/projects/-Users-landodoom-Desktop-AI-Developer-Residency-/memory/` (new: `invest-not-for-feature-analysis.md`, `notebooklm-out-of-research.md`).
- **Git:** branch `competitive-analysis-4`, last commit `49a5baf` (PR 30, merged), 0 commits ahead of `main`. Branch `feature-analysis-4` exists locally, empty. No open pull requests. **Everything from today is uncommitted:** `docs/sources/INDEX.md` is modified (entries added for `feature-analysis-4/` and `competitive-analysis-4/live-pages/`; entries still missing for the reading folders and `research-history/`), and the folders and files above are untracked. Plan: pull request A on `feature-analysis-4` (research evidence, change report, checklist, table), pull request B on `competitive-analysis-4` (draft, saved pages, reading research), merged A then B by the owner, with `INDEX.md` split between them. Commit only when the owner asks. The commit gate hook may run on commit.
- **Usage when written:** 5-hour limit 53% (resets 04:49 UTC), weekly 56%, context 61% (chat only, read from the usage tool).

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2 name a file or Figma node for each item. The verdict grid is copied from the final tables in the nine `AUDIT-PASS3.md` files. Candidate numbers come from the two `AUDIT.md` files under `docs/sources/competitive-analysis-4/`. Session numbers come from a script over the saved transcripts and the app's session list.
- **Checks run:** quotes machine-checked in every research file (about 1,000, all but a few matched); independent audits of all three company groups and both candidate groups; git and PR state read with `git` and `gh`.
- **Not checked:** the history helper's output (it was still running); whether every change in the 20-cell draft matches the audits exactly (taken from the audit summaries); ConsumerAffairs invited-review status; real use of any product; replies on Reddit beyond the threads fetched; the Oct 28 session transcript; whether Figma changed after today.
- **How this prevents drift:** each decision is tagged Approved or Proposed, the open decisions are listed, the first step is to finish the report and show it, and the owner's rules are in section 7.
