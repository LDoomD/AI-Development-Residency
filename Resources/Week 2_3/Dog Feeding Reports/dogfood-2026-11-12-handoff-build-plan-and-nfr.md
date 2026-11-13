# Handoff: Caregiving Coordinator → Build plan and non-functional requirements (2026-11-12)

> **Replaced by** `dogfood-2026-11-12-handoff-build-plan-week-4-fixes.md` (2026-11-12, evening).

Replaces: `dogfood-2026-11-11-handoff-requirements.md`. Everything in it still holds. This report adds what was found and decided on 2026-11-12. Older reports stay replaced too: `dogfood-2026-11-11-handoff-epics-features-tasks.md`, `dogfood-2026-11-10-handoff-positioning-statements.md`, `dogfood-2026-11-10-handoff-vision-and-scope-part-3.md`.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few lines where we are. Then check whether the laws and consent research (run wf_328460b2-5ee) finished, and show me its findings as a short table before doing anything else. Keep replies short, one thing at a time. Suggest only verified data (Approved or Fact)."

## 0. Start here
- **Where we are:** Discovery, Vision and Scope, epics, the roadmap and the first 2 weeks of the backlog are done (PRs 43 to 48, all merged). The **Requirements** milestone started on 2026-11-12. The owner says this is **Week 4** of the residency.
- **The outcome so far, in one sentence:** the next deliverable is the **build plan with the non-functional requirements**. Before drafting it, the owner chose to fix the risk profile and research the laws, consent and security rules first.
- **Next milestone:** the build plan and the non-functional requirements.
  - **Template:** the instructor's lecture board section "Non-Functional Requirements and Build Plan" (board `mqryoCyR9mAw3v6kyDlmes`, node 576:5825).
  - **Definition of done:** coding challenge requirement 6. That means a build plan for a three-tier app with stored data: Vercel to host, Supabase for the database, GitHub for the code, and user accounts with secured data.
- **The research run on laws, consent and security finished** on 2026-11-12. It ran 104 agents with 0 errors. Run ID `wf_328460b2-5ee`.
  - Its output is saved in `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/`: `research-run-result.txt` (the report) and `research-run-journal.jsonl` (every agent's result).
  - **It hasn't been reviewed yet.** The sources aren't saved, the dates aren't checked, and the owner hasn't seen it.
  - **Its headline (unreviewed):** HHS says HIPAA is "not likely" to apply to an app consumers use directly, but it depends on the facts. The FTC Act and the FTC Health Breach Notification Rule (2024) can still apply. Washington's and Nevada's laws require opt-in consent before collecting health data and separate consent before sharing it. Whose consent counts when a caregiver enters another person's data needs a lawyer.

## 1. Locked outcomes

### Earlier milestones (unchanged, all Approved)
- Positioning (PR 44): `caregiving-coordinator/docs/clean-deliverables/positioning-statements-2026-11-11.md`.
- Epics, features and tasks (PR 45): `epics-features-tasks-2026-11-11.md`. **6 epics, 10 features, 27 tasks.**
- Release roadmap (PR 46): `release-roadmap-2026-11-11.md`. **Order:** Epic 3 (Nov 16 to 20), Epic 1 (Nov 23 to 27), Epic 4 (Nov 30 to Dec 4), Epics 5 and 6 (Dec 7 to 11), Epic 2 (Dec 14 to 18).
- Notion backlog (PR 47): `notion-backlog-2026-11-11.md`. **11 tasks** (Epic 3, then Epic 1) in the [Backlog Kanban Board](https://app.notion.com/p/0579219a469182f1954401f71214631a).
- Requirements handoff: PR 48, merged (source: `gh pr list --state all`, run 2026-11-12).
- Vision and scope boards (PR 43): `vision-and-scope-boards-2026-11-10.md`.
- The full tables are in `dogfood-2026-11-11-handoff-requirements.md`, section 1.

### Decided on 2026-11-12
- **Every Week 2 and 3 step is guided by the Week 2&3 overview, the coding challenge and the lecture transcript, cited by timestamp.** Approved (owner's request). Saved as the memory note `week-2-3-guides-every-step.md`.
- **The order of work:** risk profile review, then the research on laws, consent and security, then the build plan and the non-functional requirements. Approved (owner picked "Review risk profile first," then "Yes, start it").
- **The research run's 5 angles:** Approved (owner, "Yeah, let's start it"):
  1. Does HIPAA apply? What do HHS's own health-app guidance and the "personal representative" rule say?
  2. The FTC Health Breach Notification Rule (2024 update) and FTC enforcement on health apps.
  3. State health-data laws (Washington's My Health My Data Act, Nevada, Connecticut, California's CCPA/CPRA and CMIA).
  4. Consent when a caregiver enters data about another person and shares it with relatives (power of attorney, healthcare proxy).
  5. The security these rules require, and whether Vercel and Supabase support it (HIPAA agreements, data region).
- **Owner's rules for the research:** it must be up to date as of 2026, every claim must cite its source, and nothing may be made up. Use every tool available (Firecrawl, others). **Ask the owner before using Arctic Shift (Reddit) or the Chrome extension.**
- **Laws aren't left out.** The owner pushed back on dropping HIPAA. Approved: research both, consent first.

## 2. Key findings and data

### What the course says about this step
| Finding | Detail | Source | Confidence |
|---|---|---|---|
| Non-functional work comes first | "We have to build that stuff first before we get into the functional requirements" | Lecture 44:13 to 44:20 | Authoritative (course) |
| What a build plan is | "A list of the prioritized order of epics," non-functional first, then functional | Lecture board 576:5725 | Authoritative (course) |
| Dependencies | "Work piece A before work piece B" | Lecture 45:16 to 45:35 | Authoritative (course) |
| How the instructor built one | Claude sorted the epics into work, then the foundation piece went first | Lecture 1:44:12 to 1:45:31 | Authoritative (course) |
| Depth this week | Name each part and its build order. Detail comes in later weeks. | Board 576:5725; lecture 48:21 to 48:43 | Authoritative (course) |
| Scope of the technical requirements | "For whatever is your first piece of work, feature work." For us, that's Epic 3. | Lecture 1:20:22 to 1:20:43 | Authoritative (course) |
| The tools are already chosen | Vercel, Supabase, GitHub, user accounts with secured data | Coding challenge, requirement 6 ([Student Space copy](https://app.notion.com/p/4069219a469180269b11dbba1ae2555e), edited 2026-11-05; matches the [public page](https://tech-fleet-community-dao.notion.site/Week-2-Coding-Challenge-Develop-Product-Specifications-for-the-ADHD-Budgeting-App-30d1a3bddce5824b87d88176985ad522) word for word, checked 2026-11-12) | Authoritative (course) |
| The Week 2&3 overview is current | Last edited 2026-10-27; matches the local copy | [Notion](https://app.notion.com/p/4689219a469182d7aa6f0144146b1e79); `.claude/skills/residency-context/reference/week-2-3.md` | Authoritative (course) |

### The template's 12 boxes (board 576:5824)
| Non-functional (build first) | Functional (build after) |
|---|---|
| Tool selection | Prototypes |
| Database architecture | Design system |
| System architecture decisions | Task-level acceptance criteria |
| Security protocol | Use case scenarios |
| Development operations | Flow charts |
| Quality engineering architecture | BDD scenarios |

When each part is taught in depth (source: lecture 48:21 to 48:43): tool selection and system architecture in Week 3, database in Week 4, security in Week 5, dev operations and quality in Week 6.

### Risk profile review (Proposed, waiting on the owner's yes)
The current `docs/risk-profile.md` is a draft the owner never approved, and most of it predates the research.

| Profile item | Verdict | Source |
|---|---|---|
| Doctor-visit recordings and transcripts | Out of MVP #1 | Market master report, row 8: "Open but unproven. No one asked for it."; competitive master report, line 123 |
| AI-generated visit notes | Out of MVP #1 | Same |
| Medication lists and refills | Not backed by the data | Competitive master report, line 122: "medicines isn't one of the 5 needs" |
| Stored portal logins | Out of MVP #1 | Vision and scope, line 95; competitive master report, line 119 |
| Family member accounts and permissions | Keep | Epic 2; Epic 3 task "Settling who handles care tasks and money"; board barrier, line 59; coding challenge, requirement 6 |
| **Add:** health and behavior details caregivers type in | New (Proposed) | Epic 3 and Epic 4 tasks |
| **Add:** money, benefits and coverage details | New (Proposed) | Epic 5 and Epic 6 tasks |
| **Add:** who can see what about the parent or partner (consent) | New (Proposed) | Board barrier, line 59 |
| HIPAA question | Keep as an open question | Our data doesn't settle it. The research run covers it. |

- **Owner's point (2026-11-12):** an AI that records doctor visits would also be a risk. Add it as a note on why recording stays out of MVP #1, since an outside AI service would hold health data. That reasoning is general knowledge, not from our research.

### Which open items matter before the build plan (Proposed, partly Approved)
| Open item | Source | Verdict |
|---|---|---|
| Consent: who can see what | Board barrier, line 59; competitive master report, line 206 | Look into it first. It shapes accounts, permissions and the database. Right now it rests on only 2 competitor examples. |
| Laws (HIPAA, FTC, state) | `risk-profile.md`, open question | Look into it second. **Approved:** the research run is going. |
| Who pays | Board barriers 1 and 2; market master report, finding 8 | Not now. There are no payment tools in the build plan. |
| The evidence leans toward hard moments | Board barrier 8 | Not now. It's a known limit. |

## 3. Excluded and deferred
- **Fleety's "Project Plan / Release Plan" framing:** it doesn't match the instructor's build plan (it adds pricing and launch marketing). Left out. Fleety's second answer (the 6 non-functional parts, "Prioritized Backlog Tasks") does match the board and can be used. That answer is chat only, not saved.
- **Morgan's example:** not found. Nodes 4162:5427, 4162:5437 and 4165:6061 aren't on the vision board or the lecture board as of 2026-11-12. It comes back if the owner finds the link.
- **The lecture board's "Agile Methods" section (544:10467):** not read. Read it only if a step needs it.
- **Visit recordings, AI visit notes, medication lists and stored portal logins:** out of MVP #1 (sources in section 2).
- **Who pays:** stays an open barrier. It comes back with the pitch deck or a later release.
- **Reddit or Arctic Shift for the laws research:** not needed. It comes back only for a consent pass on caregiver posts, and only with the owner's OK.
- **The pitch deck:** last. It's requirement 8 and on the bonus list, not the basic list. The lecture never mentions it. Course template: [Pitch deck](https://tech-fleet-community-dao.notion.site/p/4281a3bddce582a39b56810e8a046acf?pvs=25), not opened yet.
- **INVEST:** not used for this step (it isn't task splitting).

## 4. Open decisions
The next session must not decide these alone.
- **Approve the risk profile changes** in section 2? The owner was asked and hasn't answered.
- **A consent pass on the saved caregiver posts** (412 Reddit posts and 141 forum threads; market master report, gaps table)? It's Proposed, and needs a research checklist shown first.
- **Week 4 links:** the owner said they'd send them. Week 4 covers database architecture, which may add to the build plan. Local copy: `week-4.md`, from 2026-10-28.
- **The empty public GitHub repo** ("Week 3 - ADHD Budgeting App," adapted to this product) is core homework (requirement 5). It isn't made yet. Its name is the owner's call.
- **Where the build plan lives:** markdown first, then Notion or FigJam. The owner picks which.

## 5. Bridge to the next milestone

| This output | Goes into | Why |
|---|---|---|
| The research run's verified findings | Risk profile, then the security protocol box | The laws set what the security must do |
| The approved risk profile | Security protocol and database architecture | Health data, money data and consent are this product's risks |
| Coding challenge requirement 6 | Tool selection and system architecture | The course already chose the tools |
| The roadmap's epic order | The build plan's functional order | Order of value; then dependencies are added |
| Epic 3 tasks (5 in Notion) | Technical requirements, acceptance criteria and BDD for the first piece of work | Lecture 1:20:22 to 1:20:43 |
| The 6 non-functional boxes (576:5824) | The sections of the non-functional requirements | That's the instructor's template |

## 6. First steps
1. **Confirm where we are** in a few lines. Run `gh pr list --state open`.
2. **Read the research results.** It finished; the output is in `docs/sources/laws-consent-research-2026-11-12/research-run-result.txt`. The findings are JSON inside the text. Some findings are rated "medium" because their case pages weren't fetched (for example the FTC's GoodRx, BetterHelp and Flo cases).
3. **Before showing results**, do what was promised to the owner:
   - Save a copy of each cited source in `caregiving-coordinator/docs/sources/` and log it in `docs/sources/INDEX.md`.
   - Record each source's date.
   - Search each rule for 2025 to 2026 changes, and mark anything unconfirmed "may be out of date."
   - Label general knowledge as such, or leave it out.
4. **Show a short table:** rule, might it apply, what it requires, source, and where a lawyer is needed. Never say "compliant." Wait.
5. **Ask about the risk profile changes** (section 2 plus the research findings). Edit only after a yes.
6. **Then the build plan:** show the inputs table first, then draft one part at a time.

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md` and the memory files (`week-2-3-guides-every-step.md`, `only-verified-suggestions.md`, `confirm-before-changing.md`, `cite-sources-not-assumptions.md`). The ones most likely to be broken next:
- **Data-driven only.** Every line comes from an earlier deliverable or a cited source. Tag each Approved, Fact or Proposed.
- **Research checklist before any research.** `docs/research-checklist.md` is shown to the owner first.
- **Ask first** before using Arctic Shift, the Chrome extension, or writing to Notion or FigJam.
- **Laws: never conclude.** Report what each rule covers, and flag where a lawyer is needed.
- **Check the lecture and board first** for each step, and cite the timestamp or node.
- **Questions get answers, not edits.** Short replies, one thing at a time.
- **One deliverable = one branch = one PR**, from `main`. The owner merges.
- **Never write the owner's homework summary.**

## 8. Where things live
- **Records:** `caregiving-coordinator/docs/clean-deliverables/` (the 5 files listed in section 1).
- **Risk profile (draft, not approved):** `caregiving-coordinator/docs/risk-profile.md`.
- **Research checklist template:** `caregiving-coordinator/docs/research-checklist.md`.
- **Master reports:** `Resources/Week 2_3/Week 2 & 3_Course Overview_Docs/`.
- **Lecture:** `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`. It's the only transcript, and there's no Week 3 one yet.
- **Course pages:**
  - Week 2&3 overview: `.claude/skills/residency-context/reference/week-2-3.md`.
  - Week 3 challenge: `week-3-coding-challenge.md`.
  - Week 4: `week-4.md`.
- **Instructor's lecture board** `mqryoCyR9mAw3v6kyDlmes`:
  - Non-Functional Requirements and Build Plan: 576:5825.
  - Task-Level User Stories and Acceptance Criteria: 548:11166.
  - Deliverables for Product Requirements: 550:11450.
  - Agile Methods: 544:10467.
- **Vision board** `PQFzfyqTUQhAgEEe1P6ygs`: Notion steps 2001:1620 (step 12 = "Task-Level Acceptance Criteria Template").
- **Research run:** ID `wf_328460b2-5ee`. Transcripts: `~/.claude/projects/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/7e2ae3a4-c777-44ff-aec4-38025428dd86/subagents/workflows/wf_328460b2-5ee`.
- **Git (2026-11-12):**
  - No open PRs. PRs 43 to 48 are merged. `origin/main` is at `70670d7`.
  - Local branch: `handoff-requirements` (already merged).
  - This report isn't committed.
  - Left uncommitted on purpose: `docs/sources/competitive-analysis-4/live-pages/raw/il.html` and `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-05-audit-and.textClipping`.

## 9. Verification receipt
- **Outcomes and where each came from:** see sections 1 and 2. The owner's decisions on 2026-11-12 were made in chat; the quoted button choices are recorded in section 1.
- **Checks run:**
  - `gh pr list` (no open PRs); `git log origin/main` (the 2026-11-11 handoff is on main and matches the local copy).
  - Notion fetches: the overview (edited 2026-10-27) and the coding challenge (edited 2026-11-05). Firecrawl scrape of the public coding challenge page, which matched word for word.
  - FigJam reads: lecture board 576:5825 and the 6 sections to its right; vision board 2001:1620.
  - Lecture transcript keyword map and readings: 41:20 to 53:20, 1:19:50 to 1:22:10, 1:44:05 to 1:48:10.
  - The risk profile was checked line by line against the clean deliverables and the master reports with grep.
  - `check_handoff.py` on this report (result in chat).
- **Not checked:**
  - The research run's results (still running).
  - Lecture board sections 544:10467 (Agile Methods) and 544:9145 weren't read in full. Some long text boxes in 548:11166 were cut at about 700 characters.
  - The course pitch deck template and the Week 4 links weren't opened.
  - Notion and FigJam weren't written to today.
- **How this prevents drift:** owner decisions are tagged Approved, and the risk profile changes are Proposed. The research angles and the owner's rules for it are written out. First step 4 stops for the owner before any edit.
