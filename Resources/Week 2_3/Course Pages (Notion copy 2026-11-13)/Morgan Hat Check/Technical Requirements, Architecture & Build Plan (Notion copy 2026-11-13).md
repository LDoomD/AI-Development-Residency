# 🏗️ Technical Requirements, Architecture & Build Plan
- Source copy: https://app.notion.com/p/b229219a4691834eb5d101656ec867c8
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:21.457Z
- Not saved: the table-of-contents block (child of "Technical Architecture - Hat Check"); toggles are rendered as bold lines followed by their contents

---

> 🧭 Current architecture (updated 2026-11-01). The sections below are the original client-only plan, kept for history; where they conflict, this callout and the repo ADRs win. The canonical decision log is the Architecture Decision Records page, mirroring docs/adr/ in the repo.
>
> - Three-tier app (ADR-0006): Next.js + Material UI static on Vercel's CDN; a tier-2 decode route holds the OpenRouter key and owns the Hat Check logic; Supabase holds the framework only. The browser never touches the database. This supersedes the client-only ADR-001/ADR-003 below.
> - Data model (ADR-0022, revising ADR-0008): the framework is versioned JSONB in Supabase (spf\_release + spf\_record, keyed by (release, entity, slug)); a build step emits a title index + per-function snapshot slices to the CDN as the read model (CQRS). Nothing queries Supabase at request time.
> - Matching (ADR-0007, 0010, 0014): a line-scoped keyword matcher with exact / alias / similar tiers, unioned with a grounded, validated LLM recognizer. The framework is the source of truth; the LLM recognizes wording only and decides nothing; every match is validated (item in the framework, quote in the posting). This supersedes the on-device embedding plan in ADR-003 below.
> - Translator table (ADR-0020): a reviewed term-to-SPF table built from a 934-posting corpus (Greenhouse, Lever, Ashby) plus domain knowledge supplies the matcher's aliases; it lives in eval/translator-table.csv. Distinct leaf items matched across the corpus rose from 88 to 141 of 221; a real test posting went from 7 to 15 matches.
> - Roll-up (ADR-0021): a posting that names an activity or deliverable means the poster is Responsible for it, so it rolls up to the Responsible duty only (not Accountable/Consulted/Informed). Non-standard hats on the real posting dropped from 8 to 3.
> - State (ADR-0011): session-only (HTML5 sessionStorage); no accounts, no device save, no saved history. This supersedes the local-save sections below.
> - Accuracy (ADR-0019): a dependency-free eval harness (eval/ in the repo) measures precision and recall against labeled postings and picks the model; a coverage audit accounts for every posting line (100% line-accountability, distinct from matching accuracy).
> - Matching scope and AI quotes (ADR-0025): the matcher compares a posting against every framework item, so non-standard hats can appear; an AI match needs a verbatim quote and counts as similar. v1 audit: see the page v1 Audit: Requirements vs Prototype (2026-11-01).
> - Evidence (ADR-0023): every hat shows all of its relevant quotes, not one example.
> - Resume and application prep (ADR-0024): skills, activities and deliverables with outcome templates, ATS keywords, cover letter points, and interview points, built from the hats with no AI-written text. Added to MVP 1 on 2026-11-01 (T16).
> - **Scoring (ADR-0039, 2026-11-04):** a hat is scored by the share of its work the posting names (matched activities + deliverables ÷ the hat's total activities + deliverables); its match level is full (25% or more), partial (above 0, under 25%), or none. Tools do not confer a hat and the "everyone" duty is excluded. The overall title-fit uses Formula D over the title's standard hats: (full × 1 + partial × 0.5) ÷ all standard hats, with the verdict thresholds unchanged. This supersedes the one-item "covered" rule; code is owed and nothing is built yet.

> 🔒 MVP 1 scope, LOCKED (decided by Morgan, 2026-10-31)
>
> MVP 1 decodes ONE pasted job posting and explains THE JOB. It never asks the person anything about themselves and gives no candidate-specific advice. This section governs: where any requirement or priority below conflicts with it, this wins. The matching record is ADR-0005 in the repo.
>
> **In MVP 1 (about the job):** resolve the title to a job function, handling ambiguous and not-covered honestly; the three hat sets; match score and title-honesty verdict; over-scope and under-scope flags; plain-language meaning per hat; role-generic resume highlights, hidden hats first, then matched, then non-standard (ADR-0024); all relevant evidence quotes for every claim (the complete breakdown per hat, not just one example); resume and application prep including role-generic interview points (ADR-0024); no account, session-only state (ADR-0011).
>
> **Not in MVP 1 (deferred, not dropped):** anything about the candidate (personal fit, go / stretch / no-go for the person, gaps to close first, compare to the seeker's level, "which skills I already have") since MVP 1 collects no experience; a true seniority read (needs a seniority model); a shortlist or comparison of several postings (one at a time in MVP 1); interview practice, feedback, and generated question lists (FR-11 and the interview item in build Phase 3 below). Role-generic interview points and cover letter points moved into MVP 1 on 2026-11-01 (ADR-0024).
>
> **Note on NFR-1 below:** MVP 1 now sends the pasted posting to our server and to an AI service (OpenRouter). The earlier "nothing leaves the device" wording is superseded; this is a three-tier app, and the matching approach and hosting will be recorded in their own ADRs that supersede ADR-0001 and ADR-0004.

**Product:** Hat Check · **Prepared for:** engineering / coding agent + ADR authoring · **Date:** October 2026 · **Scope:** MVP #1, client-only web app, job-seeker audience, roles the Skills & Practices Framework currently covers.

> ⚠️ **Decision (2026-10-31): interview prep is Phase 2, not MVP #1.** FR-11 and the interview-prep item in build Phase 3 below are kept as written in the source, but are out of MVP #1 scope. **Amended 2026-11-01:** role-generic interview points and cover letter points are now in MVP 1 (ADR-0024, T16); practice, feedback, and generated question lists stay Phase 2.

[table of contents block, not saved]

## 1. Context & scope

Hat Check decodes a single job description against a **standard baseline for the role**, drawn from Tech Fleet's **Skills & Practices Framework**. The engine ("Hat Check") maps the posting's duties ("hats") to the framework, compares them to what the title *should* require, and returns: a match percentage, the written / unwritten / out-of-scope hats, evidence quoted from the posting, and resume + interview guidance.

**In scope (MVP #1):** one JD + title at a time; the framework's current role coverage (digital-product/tech roles, \~11 Job Functions, \~18 Duties); client-only execution; no accounts; local persistence.

**Out of scope (MVP #1):** accounts/auth, server-side user data, mock-interview practice with feedback, salary benchmarking, multi-JD comparison dashboards, roles the framework does not yet cover, seniority scoring.

### The Hat Check pipeline

1. **Input:** user provides JD text and the job title.
2. **Parse:** extract the posting's stated responsibilities, activities, skills, tools.
3. **Title resolution:** map the user's title to a framework **Job Function** (synonym translation across companies).
4. **Vocabulary normalization:** translate the JD's terms and jargon to the framework's vocabulary (skills, activities, duties).
5. **Hat matching:** match the JD's activities/tasks to framework tasks → their parent **Duties (hats)**.
6. **Hat classification:** produce three sets:
   - **Written & expected:** hats in the JD that are standard for the title.
   - **Written & not expected:** hats in the JD that are not standard for the title (out of scope / "two jobs in one").
   - **Unwritten but expected:** hats standard for the title that are absent from the JD (the hidden expectations).
7. **Match score:** how closely the JD matches the title's standard baseline.
8. **Evidence:** quote **all** the relevant JD lines that justify each hat (the complete breakdown, not a single example), and name what's implied or left unsaid.
9. **Outputs:** breakdown view + resume highlights (skills/tools/tasks/deliverables per hat) + interview questions + prep strategy.

## 2. Architecture overview

**Shape:** a single-page application that runs the entire Hat Check pipeline **in the browser**, against a **bundled, versioned snapshot** of the framework data, and persists results to **browser storage**. No application backend, no user accounts, no user data leaving the device.

### Components (logical)

| Component | Responsibility |
| --- | --- |
| Framework Data Module | Loads/validates the bundled JSON snapshot; exposes slug-indexed lookups and the title-synonym index |
| Title Resolver | Resolves free-text title → Job Function via exact + synonym match ("Job Titles in the World"), with confidence and an "unsupported" path |
| JD Parser | Segments the posting into candidate responsibility / skill / tool phrases |
| Vocabulary Normalizer | Maps JD phrases to framework terms (synonyms → canonical slugs) |
| Hat Matcher | Links normalized phrases to framework tasks → parent duties, each with a confidence |
| Hat Classifier | Computes the three hat sets against the title's standard duty set |
| Scorer | Computes the match percentage from hat coverage |
| Evidence Extractor | Ties each hat/implication back to quoted JD spans |
| Output Composer | Assembles breakdown, resume highlights, and interview prep from each hat's framework fields |
| Local Store | Persists inputs, results, profile to HTML5 storage; supports clear/delete |
| UI Layer | Input, results, evidence, and prep views; accessibility baseline |

> 📌 The central open decision is **how matching (steps 4 to 6) is implemented**: deterministic/embedding vs LLM, and whether it can stay on-device. This is ADR-003 and the biggest driver of accuracy, cost, and the privacy promise. **Decided 2026-10-31:** server-side grounded AI recognition unioned with a keyword matcher, validated against the framework (ADR-0007, ADR-0010, ADR-0014, ADR-0020).

## 3. Non-functional requirements (build these first)

**NFR-1 Privacy & data handling** (highest priority, it's the brand)

- No user account, login, email capture, or server-side user record.
- JD text, title, profile, and results are processed and stored **only on the user's device**. *(If ADR-003 selects an external inference API, this NFR must be explicitly renegotiated.)*
- No third-party analytics carrying user content; any metrics are anonymous, aggregate, content-free (NFR-10).
- A single action clears all stored data.

**NFR-2 Availability & offline**

- After first load and snapshot cache, a decode needs no network.
- Static hosting; no server runtime required; target 99.9% static availability.

**NFR-3 Performance**

- A decode returns in ≤ 3s on a mid-range laptop for a typical (≤ 1,500-word) JD.
- Initial load (app + snapshot) ≤ 5s on broadband; snapshot cached thereafter.
- If a local model is used (ADR-003), first-run download shows progress and is cached.

**NFR-4 Accuracy & trustworthiness**

- Every asserted hat is **traceable to evidence**: all relevant quoted JD spans (written hats) or a named framework rule (unwritten / out-of-scope hats).
- **Never fabricate** a duty, skill, or title mapping not in the framework; say so when confidence is low or coverage is missing.
- A labeled evaluation set of real JDs with expected classifications exists, with a target accuracy threshold agreed before launch (ADR-010).

**NFR-5 Accessibility:** WCAG 2.2 AA (keyboard, visible focus, labeled inputs, contrast, screen-reader-correct structure); \~8th-grade reading level.

**NFR-6 Compatibility & responsiveness:** current Chrome, Safari, Firefox, Edge; usable from 360px with no horizontal scroll.

**NFR-7 Security**

- No secrets in the client; no user content in URLs/query strings.
- Sanitize and safely render pasted JD text (untrusted data; no HTML injection).
- Strict Content-Security-Policy; dependencies pinned and auditable.

**NFR-8 Maintainability & data freshness**

- Framework data is a **versioned snapshot** with a documented refresh procedure; every result records the framework version.
- Matching rules/thresholds are configurable and tested, not hard-coded.

**NFR-9 Licensing & compliance:** app code MIT; framework data CC BY 4.0 with attribution wherever data is shown; one in-app place for license + attribution.

**NFR-10 Observability (privacy-safe):** optional, content-free, opt-in telemetry only (counts, error rates). Never JD text, title, or profile.

**NFR-11 Scalability & cost:** static delivery via CDN at near-zero marginal cost; no per-user compute on the critical path.

## 4. Architecture Decision Records (ADRs)

> 🧩 Updated 2026-11-01. The decisions of record are ADR-0001 to ADR-0024 in the repo (`docs/adr/`), listed with their status on the Architecture Decision Records page (https://app.notion.com/p/8d49219a469182c09fa0812e2b540489). That page is the one list; this section does not keep a second copy.
>
> The ten proposals below are the original October plan, kept for history. Each heading now says what replaced or confirmed it.

Format: MADR-lite (Context · Decision · Status · Consequences · Alternatives). Each becomes its own file under `docs/adr/`, committed with the code.

### ADR-001: Client-only architecture, no backend, no accounts (superseded by ADR-0006 three-tier and ADR-0011 session-only)

- **Context:** privacy-first, free, open-source product; no need to store user data server-side.
- **Decision:** ship as a static SPA that runs the pipeline in the browser and persists locally. No application server, no auth.
- **Status:** Proposed (recommended).
- **Consequences:** removes server cost and attack surface and delivers the privacy promise; limits matching to what runs client-side (ADR-003); no cross-device sync; limited server-side analytics.
- **Alternatives:** thin backend for heavier inference (rejected for MVP: breaks privacy promise and adds cost).

### ADR-002: Framework data as a bundled, versioned snapshot (accepted as ADR-0002; storage revised by ADR-0022)

- **Context:** the framework is open JSON over HTTPS, updated over time; the app must work offline and cite a version.
- **Decision:** bundle a pinned snapshot of the needed datasets; record the framework version in every result; document a refresh/rebuild step.
- **Status:** Proposed.
- **Consequences:** deterministic, offline-capable, reproducible results; needs a periodic update process.
- **Alternatives:** live fetch at runtime (rejected for MVP: network dependency, versioning ambiguity, upstream is not a guaranteed-uptime API).

### ADR-003: Matching approach (decided: ADR-0007, 0010, 0014, 0020; on-device embedding plan not used)

- **Context:** steps 4 to 6 need semantic matching of messy JD language to framework vocabulary. Three options trade accuracy vs privacy vs cost.
- **Decision (recommended):** **on-device, framework-grounded matching**. Deterministic normalization (synonym dictionaries from framework labels + "Job Titles in the World") plus a **local embedding model** (WASM / transformers.js) for semantic similarity, all on-device. Keep an abstraction boundary so the matcher can be swapped.
- **Status:** Proposed. **Needs Morgan's decision** (governs NFR-1 and NFR-4).
- **Consequences:** keeps the privacy promise and zero per-decode cost; accuracy depends on embedding quality; larger first load; needs the eval harness (ADR-010).
- **Alternatives:**
  - *External LLM API:* highest semantic accuracy, but sends the JD off device (breaks NFR-1 as written) and adds per-call cost. Only acceptable as an explicit opt-in "enhanced" mode with clear consent.
  - *Pure deterministic/keyword:* fully private and cheapest, lowest accuracy on paraphrased duties.

### ADR-004: Title → Job Function resolution via synonyms (replaced by ADR-0012: direct, no confidence, no picking; shared-title tie-break open)

- **Context:** the same role is titled differently across companies; the framework stores real-world titles on each Duty and canonical Job Function names.
- **Decision:** build a title-synonym index from Job Function names + duty title lists; resolve to the best Job Function with a confidence; expose an explicit "title not recognized" path.
- **Status:** Proposed.
- **Consequences:** handles title variance; needs fallback UX when unmatched (FR-13).
- **Alternatives:** require users to pick from a fixed list (worse UX, but a safe fallback to offer alongside).

### ADR-005: Local persistence with accepted data-loss stance (superseded by ADR-0011 session-only)

- **Context:** no accounts; MVP accepts that clearing the browser loses data.
- **Decision:** persist inputs/results/profile in HTML5 storage; provide clear/delete; **no** export/import/sync in MVP.
- **Status:** Proposed.
- **Consequences:** simple, private, device-bound; no cross-device continuity (accepted).
- **Alternatives:** export/import (deferred).

### ADR-006: Technology stack (decided in ADR-0006 and ADR-0013: Next.js + Material UI on Vercel, Supabase, OpenRouter)

- **Context:** static, client-only, accessible SPA with a swappable matching module.
- **Decision:** a mainstream, well-supported SPA framework + TypeScript, static build, CDN hosting; matching isolated behind an interface. Specific framework left to the team; prefer boring, long-term-supported choices.
- **Status:** Proposed. Team to confirm specifics.
- **Consequences:** easy hiring/maintenance; engine testable in isolation.
- **Alternatives:** hand-rolled vanilla (more effort) or heavy meta-framework (unnecessary without a backend).

### ADR-007: Evidence traceability is mandatory (accepted as ADR-0014 and ADR-0023)

- **Context:** trust is the product; users must see *why* a hat was flagged.
- **Decision:** every written hat links to **all** its relevant quoted JD spans (the complete breakdown, not one example); every unwritten / out-of-scope hat links to the framework rule (the title's standard duty set). No claim ships without a trace.
- **Status:** Proposed.
- **Consequences:** the matcher must return spans/rationales, not just labels; strengthens trust (NFR-4).

### ADR-008: Role coverage boundary & honest gaps (accepted in ADR-0008 and ADR-0012)

- **Context:** the framework covers limited roles today; guessing erodes trust.
- **Decision:** detect unsupported titles/duties and tell the user plainly; never fabricate a baseline for an uncovered role.
- **Status:** Proposed.
- **Consequences:** narrower launch audience, higher trust; needs clear "not covered yet" UX.

### ADR-009: Licensing: MIT code + CC BY 4.0 data attribution (still in force; built in backlog T15; no repo ADR file yet)

- **Context:** two licenses apply; obligations differ.
- **Decision:** release the app under MIT; attribute the framework (CC BY 4.0) wherever data is shown; one consolidated license/attribution screen.
- **Status:** Accepted (non-negotiable obligation).
- **Consequences:** compliant; a small, permanent UI/credit requirement.

### ADR-010: Accuracy evaluation strategy (accepted as ADR-0019; harness built; threshold and labels still open)

- **Context:** matching quality must be provable, not assumed (NFR-4).
- **Decision:** build a labeled fixture set of real JDs with expected hat classifications; measure precision/recall of the three hat sets and the score; set a launch threshold; run it in CI.
- **Status:** Proposed. **Needs an agreed threshold + a source of ground-truth labels.**
- **Consequences:** a go/no-go quality gate; needs upfront labeling effort.

## 5. Functional requirements

| ID | Requirement | Acceptance criteria |
| --- | --- | --- |
| FR-1 | Capture input: accept pasted JD text and a job title | Empty/oversized input handled gracefully; input retained locally |
| FR-2 | Resolve title to a Job Function via synonyms, with confidence | Known synonyms resolve correctly; unknown titles route to FR-13; resolved function and confidence are shown |
| FR-3 | Parse JD into candidate responsibility / skill / tool phrases | Bulleted and prose JDs both segment; original character spans preserved for evidence (ADR-007) |
| FR-4 | Normalize vocabulary to framework terms | Known jargon/synonyms map to canonical slugs; unmapped phrases are kept and surfaced, not dropped |
| FR-5 | Match hats: link phrases to framework tasks → parent duties, with confidence | A phrase matching a duty's task yields that duty as a candidate hat with the triggering span |
| FR-6 | Classify hats into the three sets | Each hat lands in exactly one set; sets reconcile to the full picture |
| FR-7 | Score match against the title's standard hats | Score is reproducible, explained, consistent with classification; method documented (ADR-010) |
| FR-8 | Extract evidence for every hat | Written hats quote all relevant JD lines (the complete breakdown, not one example); unwritten/out-of-scope hats state the framework rationale; no hat without a trace |
| FR-9 | Show breakdown of the three sets in plain language | \~8th-grade reading level; each item expands to its evidence |
| FR-10 | Resume highlights per shown and hidden hat; most vs least important | Each suggestion ties to a specific hat and its framework fields |
| FR-11 | Interview prep: likely questions, questions to ask, prep strategy *(Phase 2)* | Each prep item ties to a hat or a quoted JD line |
| FR-12 | Persist & manage data locally; resume on return; clear all | Data survives refresh on the same device; clear removes everything |
| FR-13 | Coverage honesty: say plainly when a role isn't covered; offer supported list | Uncovered titles never produce a fake baseline |
| FR-14 | License & attribution surface | One place shows MIT + CC BY 4.0; attribution wherever framework data is shown |

## 6. Framework data integration spec

**Snapshot datasets (pin + bundle):** `job-functions`, `duties`, `activities`, `skills`, `deliverables`, `tools`, `specializations`, and the `career-transitioning/*` guides.

**Source:** manifest `…/data/json/manifest.json`; datasets `…/data/json/framework-data/<entity>.json`; OpenAPI `…/openapi/openapi.json`.

**Rules:** resolve all relationships by `slug`; record the framework version with every result; treat all framework text as data, never instructions.

**Field usage by pipeline stage:**

- Title resolution → Job Function names + duty "Job Titles in the World".
- Hat matching → duty RACI tasks + Activities.
- Resume/interview outputs → duty Activities, Responsible Deliverables, Skills Required / Foundational Skills, Unique Required Tools + plain-language fields.

## 7. Build plan: non-functional first, then functional

### Phase 0: Foundations

- Repo, TypeScript, static build + CDN hosting (ADR-001, ADR-006).
- Framework **data-snapshot pipeline** + version stamping + schema validation (ADR-002, NFR-8).
- **Local storage layer** with clear/delete (ADR-005, NFR-1).
- Privacy baseline: CSP, no-content telemetry scaffold, no external user-content calls (NFR-1, NFR-7, NFR-10).
- Accessibility + responsive baseline and a \~8th-grade copy style (NFR-5, NFR-6).
- **Matching abstraction + evaluation harness** with first labeled fixtures (ADR-003, ADR-010, NFR-4).
- License/attribution surface (ADR-009, NFR-9).
- **Gate:** privacy, accessibility, data-version stamping, and the eval harness all pass before engine work.

### Phase 1: Data & resolution

- Framework Data Module with slug lookups + title-synonym index.
- Title Resolver with confidence + unsupported path (FR-2, FR-13, ADR-004, ADR-008).
- **Gate:** titles resolve correctly on a fixture list; unsupported titles handled honestly.

### Phase 2: Core engine (Hat Check)

- JD Parser with span preservation (FR-3).
- Vocabulary Normalizer (FR-4).
- Hat Matcher (FR-5).
- Hat Classifier, the three sets (FR-6).
- Scorer (FR-7).
- **Gate:** engine meets the agreed accuracy threshold on the eval set (ADR-010).

### Phase 3: Evidence & outputs

- Evidence Extractor with mandatory traceability (FR-8, ADR-007).
- Breakdown view (FR-9).
- Resume highlights (FR-10).
- ~~Interview prep (FR-11)~~ moved to product Phase 2.
- **Gate:** every shipped claim has a trace; outputs read at target level.

### Phase 4: Persistence, honesty, polish

- Save/resume/clear end to end (FR-12).
- Coverage-honesty UX finalized (FR-13).
- Accessibility audit, performance pass (NFR-3, NFR-5), licensing/attribution check (NFR-9).
- **Gate:** definition of done.

### Definition of done (MVP #1)

A job seeker can, with no account, submit a JD + title for a supported role and receive: a match score, the written / unwritten / out-of-scope hats, evidence quoted from the posting, and resume guidance. All traceable, all on-device, honest about coverage, correctly licensed and attributed, meeting the accuracy threshold and WCAG 2.2 AA.

## 8. Open decisions needed from Morgan

> ✅ Updated 2026-11-01. All five decisions in the original list below have been made: matching (ADR-0007), stack (ADR-0006), data freshness (ADR-0022: pinned commit, manual sync for MVP 1), and the scoring method (now ADR-0039, 2026-11-04: a proportional per-hat score with full / partial / none match levels at the 25% line, tools excluded; overall title-fit by Formula D over the standard hats with the verdict thresholds unchanged — superseding the earlier ADR-0018 step 11 "covered hats divided by standard hats"). The accuracy threshold is still open.
>
> **Open now:**
>
> 1. ~~Title override list (ADR-0012, T02).~~ Decided and approved 2026-11-01.
> 2. The accuracy threshold, and who labels the test postings (ADR-0019, T12).
> 3. Approval of the resume prep ranking rules (ADR-0024, T16).

### Original list (October plan)

1. **ADR-003 matching approach:** on-device only (keeps the privacy promise, more R&D on accuracy) vs allowing an external LLM (higher accuracy, breaks "data never leaves device" unless opt-in). *The biggest one.*
2. **ADR-010 accuracy:** what precision/recall threshold is good enough, and where do ground-truth labels come from?
3. **ADR-006 stack:** any preference, or leave to the team?
4. **ADR-002 data freshness:** bundled snapshot (recommended) vs live fetch, and how often to refresh.
5. **Scoring method (FR-7):** how the match percentage weights written vs missing hats. A product decision, not just technical.

## 9. Next steps

- Done: the five original decisions were made (see section 8). Next: settle the three decisions still open in section 8.
- Done in part: ADRs 0001 to 0024 exist as files under `docs/adr/`. ADRs 0005 to 0018 are on branch `docs/adr-0005-mvp1-scope` (not merged); 0019 to 0024 are not yet committed. Commit and merge them with the code.
- Begin Phase 0; do not start engine work until the Phase 0 gate passes.

> Source: `Hat_Check_Technical_Requirements_and_Build_Plan.md`
