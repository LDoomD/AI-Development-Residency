# NotebookLM Alternatives — Self-Hostable / Automatable, and What Reddit Actually Says

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-10
> **Scope:** open-source or self-hostable tools that turn documents into audio overviews
> and/or source-grounded Q&A, evaluated against three non-negotiable filters (automatable via
> CLI/script/API; real security & maintenance signal; fits inside the "Gemini/AI helps you
> learn it, Claude decides whether you know it" boundary without trying to replace Anki/
> Obsidian/Claude). **Does not reopen** `DECISIONS.md` §4's rejection of automating the real
> Google NotebookLM product — that's settled. This is the alternative-tool search the
> rejection implied should happen next.
> **Method:** WebSearch (search-engine summaries) + direct GitHub REST API calls (stars,
> forks, commit dates, contributor counts, license, security advisories pulled as raw JSON,
> not paraphrased) + WebFetch against GitHub-hosted docs.

---

## Reddit: could not be fetched — same failure as `2026-08-10_claude-code-obsidian-learning-workflows.md`

**This environment cannot fetch reddit.com in any form.** Tried and confirmed dead:
`www.reddit.com` (direct), `old.reddit.com/…/search.json` (the JSON API endpoint), and two
reddit-mirror front ends (`libreddit.privacyredirect.com`, which redirects to a bare domain
with no reddit content; the redirect target 404s). No workaround exists in this environment.

`site:reddit.com` search-engine queries were run four different ways (general NotebookLM
alternative phrasing, r/LocalLLaMA-scoped, r/selfhosted-scoped, tool-name-scoped). **None
returned an actual reddit.com URL in the result set.** Every query silently substituted
GitHub repos, blog posts, and aggregator pages (dev.to, xda-developers, alternativeto.net)
and then narrated them as if answering the Reddit question. This is the identical failure
shape the prior brief flagged and refused to report as "Reddit says X" — applying the same
discipline here:

> **No claim below is attributed to Reddit. There is no verified Reddit thread, quote, or
> vote count in this brief. Anywhere a source-summary mentions "the community" or "users
> report," that traces to a blog/aggregator, not a fetched forum thread — flagged inline.**

This is a gap worth naming plainly: the task asked specifically for r/LocalLLaMA, r/ObsidianMD,
r/artificial, r/selfhosted, r/PKMS, r/productivity discussion, and it could not be produced at
the standard this project's other briefs hold themselves to. What follows is GitHub-primary
and blog-secondary evidence only.

---

## The candidate that clears all three filters: `lfnovo/open-notebook`

**Verified directly via GitHub API (raw JSON, not a search summary), 2026-08-10:**

| Signal | Value |
|---|---|
| Stars / forks | 36,662 / 4,204 |
| License | MIT |
| Created | 2024-10-21 (~22 months old) |
| Last push | 2026-08-06 — **4 days before this search** |
| Latest commit | 2026-08-01, `fix: include source content in Source Chat context (#1226)` |
| Release cadence | v1.10.0 → v1.14.0, 2026-06-18 through 2026-07-21 — roughly weekly |
| Contributors | 70 (top non-maintainer contributor: `kwp3`, 21 commits — real bus factor, not a one-person repo) |
| Open issues | 124 |
| Topics (self-tagged) | `assistant`, `learning`, `note-taking`, `notebook`, `notes-app`, `self-learning` |

**This is the strongest maintenance/security signal of any candidate found** — active weeks
before today, real multi-contributor base, MIT license, and (see below) a track record of
*fixed* rather than *ignored* security reports.

### Filter 1 — actually automatable: yes, real REST API

Confirmed via direct fetch of `docs/7-DEVELOPMENT/api-reference.md` in the repo (not a
summary): a documented REST API at `http://localhost:5055` covering source ingestion
(`POST /sources`, multipart file upload), chat/Q&A (`POST /chat/execute`, and `POST /ask` for
search+synthesis over sources via server-sent events), notebooks, notes, search, and
transformations. Async operations (source processing, **podcast/audio generation**) return a
command ID to poll. Auth is a password header. **No standalone CLI is documented** — automation
is API-only (curl / Python `requests` / any HTTP client), which satisfies the filter (not
"open the web UI and click") but means the audio-overview and Q&A pieces DECISIONS.md §8
assigns to Gemini would need to be re-scripted here, not swapped in for free.

Podcast generation specifically: multi-speaker (1–4, vs. NotebookLM's fixed 2), takes 10+
minutes for a 30-minute episode per the docs, runs against any of 16+ configured providers
(OpenAI/Anthropic/Google/Groq/Mistral/OpenRouter/Vertex AI/local Ollama) — meaning it could in
principle run entirely local with zero new subscription cost, which is the one place it beats
the locked Gemini Notebook choice on cost/privacy, at the expense of setup complexity.

### Filter 2 — security/maintenance signal: active, but with real disclosed vulnerabilities

**Four GitHub security advisories, pulled directly from the repo's advisories page:**

| ID | Severity | Published | Description |
|---|---|---|---|
| GHSA-f35w-wx37-26q7 | **Critical** | 2026-04-09 | RCE via unsandboxed Jinja2 server-side template injection in user-created transformation prompts |
| GHSA-842v-h4cj-r646 | High | 2026-04-09 | Arbitrary file read via local file inclusion in source creation |
| GHSA-x4q2-89g5-594v | High | 2026-04-09 | Arbitrary file write via path traversal in file upload |
| GHSA-5wj9-f8q5-8f9c | High | 2026-04-07 | SurrealDB injection via unsanitized `order_by` param, CSRF-exploitable |

One search summary (unverified against the advisory itself, flagged as such) additionally
described the RCE as reported by **CERT-EU's Offensive Security Team via coordinated
disclosure**, with the fix landing by bumping the `ai-prompter` dependency to a version using
a `SandboxedEnvironment`, and the injection fixed via parameterized query binding.

**How to read this against the filter, honestly:** a Critical RCE and three High-severity
bugs in one project is a real red flag on its face — this is not "12 stars and no commits,"
it's the opposite failure mode: enough real-world usage to attract professional security
researchers, and vulnerabilities serious enough that they did. What makes it not disqualifying:
all four were reported through coordinated disclosure (not found exploited in the wild, as far
as this search turned up) and **all four are fixed in releases that predate today by four
months**, with the release cadence since showing no gap in maintenance. The honest
recommendation: **treat this as self-hosted-and-firewalled software, not internet-facing
software** — run it on localhost or a LAN-only Docker instance, never expose it publicly,
and don't skip version upgrades. That's a usable posture for this project's single-user,
local-machine use case; it would not be an acceptable posture for anything multi-tenant.

### Filter 3 — fits the role boundary: yes, same slice as Gemini Notebook, no mastery-grading ambition

Nothing in the docs or feature list positions Open Notebook as a quiz/spaced-repetition/
mastery tool — it's a research/reading tool (chat over sources, podcast generation, notes),
the same slice DECISIONS.md §8 already carves out for Gemini Notebook. It would not compete
with Anki or the Examiner if adopted; it would only be a candidate to *sit alongside or
replace* Gemini Notebook specifically. Whether that swap is worth the added self-hosting
security posture is a cost/benefit call, not a scope violation.

---

## Other candidates checked, weaker on the same three filters

| Candidate | Stars/license | Last push | Verdict |
|---|---|---|---|
| `theaiautomators/insights-lm-public` (InsightsLM) | 654 ★, MIT | **2026-01-16** — 7 months stale as of this search | Real REST/N8N-based automation surface, audio summaries, but activity has visibly dropped off relative to Open Notebook. Moderate risk on filter 2 |
| `run-llama/notebookllama` | 1,961 ★, (Apache-family, LlamaCloud-backed) | **2026-03-02** — 5+ months stale | Backed by a well-known org (LlamaIndex/run-llama), but commit activity has gone quiet. Flag, don't recommend, until it shows renewed activity |
| `blinkospace/blinko` | 10,857 ★, GPL-3.0 | 2026-08-03 (active) | Actively maintained, but it's a **note-taking tool with RAG bolted on**, not a document→audio-overview tool — closer to Obsidian's territory than Gemini Notebook's. Out of scope for this specific slice, noted because search engines keep surfacing it as a "NotebookLM alternative" |
| Meta's "NotebookLlama" (the actual Meta org repo could not be found — `meta-llama/notebookllama` returns 404; the real one is `run-llama/notebookllama`, above) | — | — | **Search-summary attribution error, corrected here.** Multiple blog posts describe this as a Meta project; it is a `run-llama` (LlamaIndex) project that uses LlamaCloud as a backend. Do not repeat the "Meta ships a NotebookLM alternative" claim — it traces to sloppy blog headlines, not to Meta's own GitHub org |
| KnowNote, Scholarly.so, and similar | — | — | Surfaced repeatedly in search results but are **not open-source/self-hostable** (Scholarly.so is a hosted SaaS; KnowNote's licensing/hosting model wasn't independently verified) — fail filter 1/3 by definition and are not recommended |

---

## Agentic-AI learning tools noticed that are NOT NotebookLM-related

Nothing surfaced in this specific search that wasn't already covered by
`2026-08-10_claude-code-obsidian-learning-workflows.md` (`bevibing/tutor-skills`,
`hluaguo/learn-faster-kit`) or `2026-08-10_ai-assisted-learning-practices.md`. No new
genuinely useful agentic learning tool turned up in this pass beyond what those two briefs
already logged — worth stating plainly rather than padding the list with SEO-cluster hits
(Scholarly.so, "10 Best AI Study Tools" listicles) that don't meet this project's bar.

---

## Bottom line for DECISIONS.md §4 / §8 (not a decision — a recommendation for sign-off)

1. **`lfnovo/open-notebook` is the one real candidate.** It clears all three filters, with the
   security-advisory history as an explicit, disclosed caveat rather than a silent one.
2. **It is not obviously worth displacing the locked Gemini Notebook choice.** Gemini Notebook
   is $0 incremental (already-paid Google AI Pro), zero self-hosting/security-posture burden,
   and already locked with a defined role boundary. Open Notebook's advantages — real API
   automation, local-model option, multi-speaker podcasts — are real but solve a problem
   (automation, self-hosting) that DECISIONS.md never flagged as a pain point with Gemini
   Notebook. The actual open problem it could help with is §12.3, the **Gemini → vault export
   seam** — but Open Notebook doesn't fix that either; it would just relocate the seam.
3. **Recommend: log as Queued, not Locked.** If the Gemini → vault export friction becomes
   painful in practice, Open Notebook's REST API is the concrete automation path — script
   ingestion + `/ask` + podcast generation, land the output as `.raw/`-style immutable copies
   (the pattern from `2026-08-10_claude-code-obsidian-learning-workflows.md` §6.3) — but there
   is no evidence yet that today's manual export is actually a bottleneck, and adopting it
   pre-emptively adds a self-hosted-RCE-history service to the stack for a problem that
   hasn't materialized.
4. **The Reddit gap should be logged, not silently dropped.** If real user-experience
   validation of Open Notebook (or any alternative) is needed later, it requires either a
   different fetch path than this environment has, or manual review by Orlando directly.
