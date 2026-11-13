# MVP #1 Requirements (Handoff)
- Source copy: https://app.notion.com/p/12f9219a4691838b9ecf01bcb9866efa
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:16.765Z
- Not saved: none

---

> 🧭 Current design (updated 2026-11-01). Sections 5 and 6.6 below describe the original client-only, local-save plan and are kept for history; where they conflict, this and the repo ADRs win (see the Architecture Decision Records page).
>
> - Three-tier app: Next.js + Material UI on Vercel; a server decode route holds the OpenRouter key; Supabase holds the framework only; the browser never touches the database (ADR-0006).
> - The framework is stored as versioned JSONB with build-time snapshot slices served from the CDN (ADR-0022); row-level security on.
> - Matching is a line-scoped keyword matcher (exact / alias / similar) unioned with a grounded, validated LLM; a reviewed translator table built from 934 real postings supplies the aliases (ADR-0007, 0010, 0014, 0020). The framework is the source of truth; the LLM decides nothing.
> - A posting that names an activity or deliverable means the poster is Responsible for it, so it rolls up to the Responsible hat (ADR-0021).
> - State is session-only (HTML5 sessionStorage): no accounts, no device save, no saved history (ADR-0011). This supersedes the local-save requirements below.
> - Scoring (ADR-0039, 2026-11-04): a hat is scored by the share of its work the posting names (matched activities + deliverables ÷ the hat's total activities + deliverables) and classified full (25% or more), partial (above 0, under 25%), or none; tools no longer confer a hat and the "everyone" duty is excluded. The title-honesty verdict uses Formula D over the title's standard hats (full × 1 + partial × 0.5 ÷ all standard hats); the strong / partial / mismatch thresholds are unchanged. This supersedes the three-set boolean in section 3 and FR-1.3's overlap wording below; code is owed (T-prop-1 to T-prop-4) and nothing is built yet.

> 🔒 MVP 1 scope, LOCKED (decided by Morgan, 2026-10-31)
>
> MVP 1 decodes ONE pasted job posting and explains THE JOB. It never asks the person anything about themselves and gives no candidate-specific advice. This section governs: where any priority tag or line below conflicts with it, this wins. The matching record is ADR-0005 in the repo.
>
> **In MVP 1 (about the job):** resolve the title to a job function, handling ambiguous and not-covered honestly; the three hat sets (written-expected, written-not-expected, unwritten-expected); match score and title-honesty verdict; over-scope and under-scope flags; plain-language meaning per hat; role-generic resume highlights (skills, tools, deliverables), hidden hats first, then matched, then non-standard (ADR-0024); all relevant evidence quotes for every claim (the complete breakdown per hat, not just one example); resume and application prep with cover letter and interview points (ADR-0024); no account, session-only state with no saved history (ADR-0011).
>
> **Not in MVP 1 (deferred, not dropped):** anything about the candidate, which means personal fit, go / stretch / no-go for the person, which gaps to close first, comparing the posting to the seeker's level, and "which skills I already have" (MVP 1 collects no experience or profile); a true seniority read from duties (needs a seniority model the framework does not have); a shortlist or comparison of several postings (MVP 1 is one posting at a time); and interview practice, feedback, and generated question lists. Role-generic interview points are in MVP 1 (ADR-0024, amended 2026-11-01).
>
> **Privacy wording changed:** MVP 1 now sends the pasted posting to our server and to an AI service (OpenRouter) to analyze it. The earlier "nothing leaves your device" claim in section 5 below no longer holds. The person is told before they submit.

**Prepared for:** coding agent / build team · **Prepared by:** Morgan · **Date:** 2026-10-18 · **Status:** Ready to build, MVP #1

## 1. One-line summary

A browser app that reads a job description against the **Tech Fleet Skills & Practices Framework**, tells the user which role responsibilities ("RACI hats") the posting really expects, including the ones hidden or mismatched, and shows them how to prove those hats on their resume.

## 2. Product vision & the problem

Job seekers can't tell, before applying, whether they truly fit a role, because job titles are inconsistent and job descriptions are vague or incomplete. The same title means different work at different companies. Generic resume and interview tools optimize keywords or give generic practice. None tell a candidate **what the role actually expects, what the posting left out, and how to prove they can do it.**

This app closes that gap by grounding every answer in a shared, open standard (the Skills & Practices Framework) instead of guessing.

### Target users (all served by one product)

1. **Career changers:** moving into a new field; need to see how their experience maps to a new role.
2. **Experienced professionals:** want the right level and pay; need to judge true seniority and title honesty.
3. **New graduates:** first job seekers; need plain-language help understanding what a role wants.

## 3. Core concept: "RACI hats" = framework Duties

- A **"hat"** is a framework **Duty**: a set of commitments accountable for work. Each Duty carries **RACI tasks**: `Responsible Tasks`, `Accountable Tasks`, `Consulted Tasks`, `Informed Tasks`.
- A **job title** maps to a framework **Job Function**. Each Job Function has a standard set of **Associated Duties** (the hats expected for that title), plus standard Skills, Practices, and Possible Specializations.
- Each Duty links to the proof material a resume needs: **Activities, Responsible Deliverables, Skills Required, Foundational Skills, Unique Required Tools**, plus plain-language fields (`Duty Description`, `Why Is This Duty Important`, `What Does It Take To Succeed`, `First Step to Learn`).
- Each Duty lists **`Job Titles in the World`**, used to resolve a user's real-world title to the standard Job Function/Duties.

### The engine, in plain terms

1. User enters a **job title** and pastes a **job description (JD)**.
2. App resolves the title → **Job Function** → its **standard hats** (Associated Duties).
3. App reads the JD and identifies the **hats it actually describes** (matching described responsibilities to framework tasks and their parent duties).
4. App produces three sets:
   - **Expected but missing:** hats standard for the title, absent from the JD.
   - **Present but non-standard:** hats in the JD, not standard for that title.
   - **Matched:** hats in both.
5. For shown and hidden hats, the app surfaces each hat's activities, skills, deliverables, and tools, compares them to the user's entered experience, and shows **what to highlight on the resume**.

## 4. Data source & integration

**Source:** Tech Fleet Skills & Practices Framework (open data, no key, static JSON over HTTPS).

- Manifest: `https://techfleetworks.github.io/skills-and-practices-framework/data/json/manifest.json`
- Dataset files: `https://techfleetworks.github.io/skills-and-practices-framework/data/json/framework-data/<entity>.json`
- OpenAPI spec: `https://techfleetworks.github.io/skills-and-practices-framework/openapi/openapi.json`
- Browsable docs: [techfleetworks.github.io/skills-and-practices-framework/api](https://techfleetworks.github.io/skills-and-practices-framework/api/)

**Key datasets for MVP #1:**

| Entity | File | Why it's needed |
| --- | --- | --- |
| Job Functions (11) | `job-functions.json` | Title → standard hats, skills, practices, specializations |
| Duties (18) | `duties.json` | The hats: RACI tasks, activities, deliverables, skills, tools, plain-language fields, real-world titles |
| Skills (115) | `skills.json` | Skill detail for fit + resume matching |
| Activities (100) | `activities.json` | Proof material per hat |
| Deliverables (104) | `deliverables.json` | Proof material per hat |
| Specializations (23) | `specializations.json` | Sub-role nuance |
| Tools (17) | `tools.json` | Tools expected per hat |
| Career-transition guides (8) | `career-transitioning/*.json` | Transferable-skills guidance for career changers |

**Integration requirements**

- Read the framework data (bundle a cached snapshot and/or fetch at runtime). Do **not** fork or alter the data's meaning.
- Records relate by `slug`. Resolve relationships by slug, not display label.
- Treat first-version data as current truth. Where data does not cover something, say so rather than guess.

**Role coverage limitation:** the framework currently covers **digital product & tech team roles** (UX Design, UX Research, UX Writing, Product Management, Product Ownership, Business Analysis, Agile Coaching, Software Engineering; 11 job functions, 18 duties). Launch scoped to these roles and clearly tell users when a title falls outside coverage.

**Licensing (must-do):**

- App code is released under the **MIT license**.
- Framework **data is CC BY 4.0**; attribution is **required** wherever the data is shown. Credit line: _"The Skills & Practices Framework by Tech Fleet, licensed under CC BY 4.0. _[_https://github.com/techfleetworks/skills-and-practices-framework_](https://github.com/techfleetworks/skills-and-practices-framework)_"_. MIT on the app does not remove this obligation.

## 5. Non-functional requirements

- **No accounts.** No sign-up, login, email, or server-side user records. Fully usable on first visit.
- **Local persistence only.** All user data (profile, pasted JDs, scans, resume notes, prep plans) saved in the browser (localStorage / IndexedDB). Nothing leaves the device.
- **Data loss is acceptable for MVP #1.** No backup/export/sync. If the browser is cleared, the user re-enters.
- **Privacy as a feature.** "No account, your data never leaves your device" is visible to the user.
- **Platform:** responsive web app on current Chrome, Safari, Firefox, Edge; usable at ≥360px with no horizontal scroll.
- **Accessibility:** WCAG 2.2 AA target; keyboard navigable, sufficient contrast, labeled inputs.
- **Performance:** a scan returns in a few seconds; framework data cached after first load.
- **Tone / reading level:** plain language, \~8th-grade reading level.
- **Integrity:** no "stealth" or live in-interview assistance. All guidance is for honest preparation.

## 6. Functional requirements (by epic)

Priority uses MoSCoW for MVP #1 (**M** = Must, **S** = Should, **C** = Could).

### 6.1 Understand the Job Through the Framework

**FR-1.1 Map the title to its standard hats**

- Enter a job title and see the standard hats expected for it. **\[M\]**
  - AC: given a supported title, show the Job Function's Associated Duties. Unsupported titles: see 6.6.
- Understand each hat in plain language: what it is, why it matters, what it takes. **\[M\]**
  - AC: each hat shows its Duty Description, "why important," and "what it takes to succeed."
- See the skills and practices expected for that title. **\[S\]**

**FR-1.2 Read the hats in the job description**

- Paste a JD and see which standard hats it describes. **\[M\]**
  - AC: returns a list of matched hats, each with all the JD phrases that triggered it (the complete breakdown, not one example per hat), plus each hat's share and match level — full / partial / none (ADR-0039); a tool mention no longer makes a hat match.
- See which hats are expected for the title but missing from the JD. **\[M\]**
  - AC: lists hats in the standard set not found in the JD.
- See which hats appear in the JD but are not standard for the title. **\[M\]**
  - AC: lists hats found in the JD that are not in the standard set.

**FR-1.3 Title & role reality check**

- Learn whether the title honestly matches the work. **\[M\]**
  - AC: a plain verdict (strong match / partial / mismatch) computed by Formula D over the title's standard hats — each full hat counts 1, each partial 0.5, divided by all standard hats (ADR-0039); strong at 60% or more, partial at 25% or more, mismatch below 25%.
- Learn the true seniority a role implies. **\[S\]**
- Be warned when a title looks inflated or under-leveled. **\[C\]**

### 6.2 Know If You Fit the Role

**FR-2.1 Match experience to the hats**

- See the activities, skills, deliverables, and tools tied to each shown or hidden hat. **\[M\]**
- See which of those they already have and which they are missing. **\[M\]**
- See which past-field skills transfer to the role's hats. **\[S\]** (uses career-transition datasets)
- Map education and projects to the role's hats and deliverables. **\[S\]**

**FR-2.2 Apply-or-not decision**

- Get a clear go / stretch / no-go call based on hat coverage. **\[M\]**
- See which gaps to close first. **\[S\]**
- Compare several postings for the same title. **\[C\]**

### 6.3 Prepare the Resume for the Real Role

- See which experiences, deliverables, and skills to highlight to prove each hat. **\[M\]**
- Prioritize highlighting the hidden hats most likely to be overlooked. **\[M\]**
- Tell the story of growth behind each hat. **\[S\]**
- See how well the current resume covers the role's hats. **\[S\]**
- Reframe real experience toward the hats the posting values most. **\[S\]**

### 6.4 Get Ready for the Interview (Phase 2, fast follow)

- See likely questions based on hats and tasks. **\[C\]**
- Understand what each hat means the interview will probe, and why. **\[C\]**
- Follow a prep checklist built from the role's hats. **\[C\]**
- Practice answers and receive feedback. **\[Phase 2\]**
- See improvement across practice sessions. **\[Phase 2\]**

### 6.5 Track Readiness & Build Confidence (Phase 2)

- See a readiness score before applying. **\[S\]**
- Track progress as gaps close. **\[Phase 2\]**
- Prepare openly, with no hidden in-interview help. **\[M, principle, applies throughout\]**

### 6.6 Foundations: Local Save & Framework Data (no account)

- Use the full app right away, no sign-up or login. **\[M\]**
- Keep profile (experience, skills, target roles) on own device. **\[M\]**
- Keep saved roles, scans, resume notes, prep plans between visits. **\[M\]**
- Return and pick up where they left off on the same device. **\[M\]**
- Clear or delete all saved data at any time. **\[M\]**
- See which job families are supported today and what is coming. **\[M\]**
- Be told clearly when a title or duty is not covered, instead of a guess. **\[M\]**
- Credit the framework (CC BY 4.0) wherever its data is shown; release under MIT. **\[M\]**
- View the app license (MIT) and framework attribution in one place. **\[M\]**

## 7. Primary user flow

1. Landing: short explainer + "no account needed, your data stays on your device."
2. Enter/confirm a **target job title** (picker suggests supported titles).
3. Paste a **job description**.
4. (Optional, recommended) Enter/edit **experience, skills, projects** (saved locally).
5. **Results view:** matched / missing / non-standard hats in plain language; title-honesty verdict; fit summary + go / stretch / no-go.
6. **Resume prep view:** for each hat, the activities/skills/deliverables to highlight, flagged by what the user has vs is missing.
7. Everything persists locally; user can return or clear data.

## 8. MVP #1 scope

**In scope (Must/Should):** Epics 6.1, 6.2, 6.3, and 6.6: the hat-matching engine, fit verdict, resume-prep guidance, and the no-account/local-save foundation with licensing. Scoped to currently supported roles.

**Out of scope (Phase 2):** interview question generation, mock practice + feedback, progress tracking, multi-posting comparison, export/import/sync, any server or account features, uncovered roles.

## 9. Assumptions & open questions

- **Resume input:** paste-only for MVP, or resume file upload too?
- **Title → Job Function resolution:** suggest the closest supported Job Function, or only accept from a supported list?
- **JD → hat matching confidence:** is keyword/phrase-to-task matching enough for MVP, or is LLM-based matching expected? (Either must stay grounded in framework data and say so when unsure.)
- **Hosting:** static site is sufficient (no backend). Confirm preferred host.
- **Branding/name:** TBD.

## 10. Definition of done (MVP #1)

- With no account, a user enters a supported title + JD and receives matched / missing / non-standard hats in plain language, a title-honesty verdict, a fit call, and resume-highlight guidance, all grounded in framework data.
- Unsupported titles are handled honestly (no guessing).
- All user data persists locally and can be cleared.
- MIT license and CC BY 4.0 attribution are present and correct.
- Works responsively on current browsers at \~8th-grade reading level, meeting WCAG 2.2 AA basics.

> Source: `Handoff_Requirements_MVP1.md`
