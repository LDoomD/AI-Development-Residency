# A NotebookLM Alternative That Can Be Automated Safely — The Search, and Why It Came Back Empty

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-10
> **Scope:** open-source or self-hostable tools that turn documents into **audio overviews**
> and/or **source-grounded Q&A**, and that can be driven by a CLI, script, or documented API.
> This is the alternative-tool search that `DECISIONS.md` §4's rejection implied should happen
> next. It does **not** reopen that rejection.
> **Method:** three independent passes — a GitHub/PyPI-primary pass, a first-person
> practitioner-writeup pass, and an adversarial verification pass whose only job was to try to
> break the first two. Every star count, license, commit date, contributor split, advisory
> field and PyPI ownership record below was pulled from the GitHub REST API or the PyPI JSON
> API as raw JSON, not from a search-engine summary. **Load-bearing figures were re-pulled a
> third time while writing this brief** (see *Verification stamp*, end of §2).
> **Companion briefs, not repeated here:**
> `2026-08-10_notebooklm-alternatives-reddit.md` (the raw GitHub audit),
> `2026-08-10_notebooklm-alternative-practitioner-writeups.md` (first-person accounts),
> `2026-08-10_claude-code-obsidian-learning-workflows.md` (a different angle entirely).

---

## Why this search exists

`DECISIONS.md` §4 rejected **"NotebookLM MCP / browser automation / burner Google account"** —
no public API (enterprise-gated only), Patchright-style stealth automation is a ToS and
fragility problem, and it is unnecessary because the already-paid Google AI Pro subscription
gives first-party access. §1 keeps **Gemini Notebook** as the locked reading-accommodation
layer, and §8 fences its role: *audio overviews and grounded Q&A over dense primary sources —
it does not decide mastery, write the study plan, or generate cards.*

That rejection closed a door without answering the question behind it. The wanted capability —
**push a document in, get an audio overview and source-grounded Q&A out, on a schedule, without
a human clicking** — is still wanted. So the question this brief answers is narrow:

> **Does an open-source or self-hostable tool exist that does the Gemini Notebook slice and can
> be automated through a real CLI, script, or documented API — without stealth-automating
> anybody's product?**

Three non-negotiable filters, applied without exception:

1. **Actually automatable** — CLI, script, or documented API. Not "open the web UI and click."
2. **Real security/maintenance signal** — recent commits, a real license, a nontrivial
   contributor base, no unaddressed security history. A 12-star repo dead for a year is a risk
   to flag, not a tool to recommend.
3. **Stays in its lane** — `DECISIONS.md` §1 already assigns Anki the review queue, Obsidian
   the storage, and Claude the mastery gate. A candidate that wants to become a second SRS
   engine or a grading engine is out of scope. Only the audio-overview / source-Q&A slice.

---

## The one-paragraph answer

**Something exists. Nothing is safe to adopt.** Twenty-eight distinct repos were examined; five
were audited by direct repo inspection. Every candidate that genuinely clears filter 1 fails
filter 2 in a way you would have to *actively decide to accept*. The two most-recommended tools
in this category are `lfnovo/open-notebook` — which has a **CVSS 9.9 remote-code-execution
advisory reported by CERT-EU's Offensive Security Team**, four advisories with **no
machine-readable patched version**, and a critical path running through **five more repos by
the same single author** — and `souzatharsis/podcastfy`, which is not "slow" but **abandoned**:
last commit touching library code 2025-12-09, last GitHub release 2024-11-16, and four
contributor PRs from July 2026 sitting with zero maintainer comments. The best-shaped candidate
on maintenance grounds, `Local-NotebookLM`, is effectively one person with no external review.

> **Recommendation: adopt nothing. `DECISIONS.md` §4 and §1 both stand unchanged. Gemini
> Notebook stays.** It is $0 incremental, has zero self-hosted attack surface, and the problem
> a replacement would solve — automation — was never logged as a pain point. §12.3 (the
> Gemini→vault export seam) is the *only* thing that should ever reopen this, and none of these
> tools fix it; they relocate it.

**Two namespace facts belong in the record regardless of adoption, because both are traps a
future session will otherwise walk into:** `open-notebook-mcp` on PyPI is **not** the
open-notebook maintainer's package, and `pip install open-notebook` installs **NIST's unrelated
software**. Both independently re-verified while writing this brief. Details in §2.3 and §2.4.

---

## 1. Candidates

Twenty-eight distinct repos/tools survived dedupe across the three passes. The table below
carries every one that got past a title-level read. **Disqualified-on-sight** tools — the eight
that automate Google's real product, and the six that are already-owned roles — are listed
after the table rather than given rows they don't deserve.

| Tool | What it does | Automatable how | Security / maintenance signal | Verdict |
|---|---|---|---|---|
| **`Goekdeniz-Guelmez/Local-NotebookLM`** 981★ Apache-2.0 | PDF/doc → multi-speaker audio overview, fully local | `python -m local_notebooklm.make_audio` + Python API + a FastAPI server. **No `[project.scripts]` entry point** — "real CLI" oversells it, but fully scriptable | **Weak.** 2 contributors, one a single drive-by commit. Last push 2026-05-08 (3 mo). 0 advisories — and 0 external review. 18 lifetime issues on a 981★ repo | ⚠️ **Least-unsafe, not safe.** Smallest attack surface of anything still moving. Read the source before running it |
| **`lfnovo/open-notebook`** 36,663★ MIT | Full NotebookLM analogue: sources, chat/Q&A over sources, notes, podcast generation | Documented REST API on `localhost:5055` (`POST /sources`, `/chat/execute`, `/ask` via SSE, async podcast jobs). **MCP path is third-party — do not use** | **Worst in the set.** CVSS 9.9 RCE (CERT-EU), 3 more High advisories, all four with `first_patched_version: null`. 78% single-author. 3 solo-maintainer repos on the critical path | ⚠️ **Queued, not Locked.** The only candidate with real deployment evidence *and* the only one with a Critical-RCE history |
| **`souzatharsis/podcastfy`** 6,491★ Apache-2.0 | Text/URL/PDF → conversational two-speaker audio | Best-shaped of all: `pip install`, real CLI, no service to firewall | **Fails filter 2 outright.** Library code frozen since 2025-12-09; last release **v0.4.0, 2024-11-16 (21 months)**; 119 open issues; July 2026 PRs unanswered | ❌ **Do not adopt.** Ideal shape, dead project. Vendor a fork if you must; never depend on it |
| `nazdridoy/kokoro-tts` 1,774★ MIT | TTS only — the voice engine. EPUB/PDF input directly | Real CLI | 3 contributors, last push 2026-04-08 | 🔧 **Component, not a tool.** This is what makes any of the above $0. **Vendor and pin — never a live dependency** |
| `mozilla-ai/document-to-podcast` 180★ | Document → podcast, clean reference implementation | Clean CLI | **Dead.** `pushed_at` reads today, but every recent `main` commit is `pre-commit-ci[bot]` / `dependabot`. **Last human commit 2025-03-19 (~17 months).** Release 1.4.5 from 2025-02-12 | ❌ Read as a reference implementation. Do not run |
| `MODSetter/SurfSense` 15,875★ | Research assistant / RAG over sources, active development | API surface exists | Active — but `LICENSE` carves out `surfsense_backend/app/proprietary/` as **BSL-1.1** (rest Apache-2.0), and the directory exists. Pivoting toward scraper-for-agents | ❌ **Rejected.** Open-core bait-and-switch risk as a *core* dependency, plus a §4-shaped scraping posture |
| `run-llama/notebookllama` 1,961★ | NotebookLM analogue, LlamaCloud-backed | LlamaIndex tooling | Last push 2026-03-02 — 5+ months quiet. **Not a Meta project** despite widespread blog claims | ❌ Flag, don't recommend |
| `theaiautomators/insights-lm-public` 654★ MIT | Audio summaries + notebook UI | REST / n8n | Last push 2026-01-16 — 7 months stale | ❌ Fails filter 2 |
| `blinkospace/blinko` 10,857★ GPL-3.0 | Note-taking with RAG bolted on | API | Active (2026-08-03) | ❌ **Out of slice** — this is Obsidian's territory (§1), not Gemini Notebook's |
| `CaviraOSS/PageLM`, `MrSibe/KnowNote`, `smallnest/notex`, `open-biz/OpenBookLM`, `RecursiveIntell/Gloss`, `robzilla1738/Memorwise`, `PndaMan/cortex`, `earlyaidopters/notebooklmreimagined` | Various NotebookLM-alikes | Mixed / unverified | Sub-50★ cluster or unverified hosting model; several are hosted SaaS wearing an open-source costume | ❌ All fail ≥1 filter. Flagged so they aren't re-found |
| "Deta Surf" | Surfaced repeatedly in aggregator content | — | **Never verified to exist as claimed** | ❌ Dropped — see §5 |
| Milvus + Zep + Firecrawl + AssemblyAI + Kokoro pipeline | DIY reference architecture | — | **A blog post, not a repo.** No CLI/API automation detail retrievable | ℹ️ Logged as evidence the DIY pattern is repeatable. Not a candidate |

### Disqualified under §4 — unofficial automation of Google's product

`teng-lin/notebooklm-py` (18,621★, pushed today — real, popular, and **still disqualified**),
`PleasePrompto/notebooklm-mcp`, `PleasePrompto/notebooklm-skill`,
`israelbls/notebooklm-podcast-automator`, `mahlernim/chrome-pdf-to-notebooklm`,
`joeseesun/qiaomu-anything-to-notebooklm`, `zstmfhy/zlibrary-to-notebooklm`,
`proyecto26/notebooklm-ai-plugin`.

> ⚠️ **`notebooklm-py`'s own README says it: *"Unofficial Python client for Google NotebookLM
> that uses undocumented RPC APIs."*** It drives Google's internal `batchexecute` protocol with
> obfuscated method IDs. Its popularity (18.6k stars) and its shipped Claude Code skill are
> exactly what make it keep resurfacing in "Claude Code + NotebookLM" posts **looking
> sanctioned**. It is the precise thing §4 rejected. If "just use the MCP server" comes up
> again, this is what is being proposed.

### Out of slice — roles already owned by §1

`SYuan03/Skill-Anything`, `raine/anki-llm`, `pieralukasz/true-recall`, `ctrlaltwill/LearnKit`,
`TovTechOrg/Tov-learn`, `lfnovo/open-cognition`. These want to be SRS engines, card generators,
or tutors. Anki, Claude and Obsidian already hold those roles.

---

## 2. Where the earlier passes were too optimistic

The first two passes' raw numbers were accurate — every one re-pulled and matched. But four
material readings were wrong, **all in the optimistic direction**. These corrections are the
reason this brief's verdict is harsher than the pass it builds on.

### 2.1 `open-notebook`'s "70 contributors, real bus factor" is false

The GitHub contributor count is 70. The commit distribution is not:

- `lfnovo`: **723 of 923 commits (78%)**
- `dependabot`: 80 (#2 overall)
- `kwp3`, the top human contributor after the owner: **21 (2.3%)**

That is a bus factor of one wearing a crowd costume. And the critical path runs through **five
more repos by the same person**:

| Dependency | Role | Human contributors | Last push |
|---|---|---|---|
| `lfnovo/ai-prompter` | prompt/template rendering | **1** | 2026-04-09 |
| `lfnovo/podcast-creator` | **the actual audio-generation engine** | **1** | 2026-03-03 |
| `lfnovo/surreal-commands` | async job queue behind podcast generation | **1** | 2026-01-31 |
| `lfnovo/content-core` | source ingestion | 4 | 2026-07-30 |
| `lfnovo/esperanto` | 22-provider LLM abstraction | 9 | 2026-07-30 |

`ai-prompter` — one maintainer — is exactly where the CVSS 9.9 RCE lived. **Adopting
open-notebook means adopting six repos from one person, three with a single human contributor
and two untouched for five to seven months.**

### 2.2 The advisories are documented as fixed but are machine-unresolvable

| GHSA | Severity | CVSS | Vulnerable | `first_patched_version` |
|---|---|---|---|---|
| `GHSA-f35w-wx37-26q7` | **Critical** | **9.9** | ≤ 1.8.3 | **null** |
| `GHSA-x4q2-89g5-594v` | High | 8.1 | ≤ 1.8.3 | **null** |
| `GHSA-5wj9-f8q5-8f9c` | High | 8.8 | ≤ 1.8.2 | **null** |
| `GHSA-842v-h4cj-r646` | High | 7.7 | ≤ 1.8.3 | **null** |

The RCE prose says "Fixed in v1.8.4." The structured field is empty on all four — re-confirmed
against the live advisories API while writing this. **Practical consequence: `pip-audit`,
`osv-scanner` and Dependabot cannot certify any version as safe.** You get no automated
regression alarm if a future release reintroduces it.

The reporter matters too. **CERT-EU's Offensive Security Team** found an unsandboxed Jinja2
`Environment` in a user-facing template feature. That is a design-level failure, not a typo, and
no external review has happened since.

> The earlier pass read four disclosed-and-fixed advisories as a *positive* maturity signal —
> "enough real usage to attract professional researchers." That reading is defensible, and it is
> also how you talk yourself into running a 9.9 on your own machine. Both things are true: the
> disclosure process worked, **and** the codebase had a national-CERT-grade RCE in it four
> months ago with no independent review since.

### 2.3 ⚠️ `open-notebook-mcp` is not first-party — the single most important finding

The GitHub pass presented `uvx open-notebook-mcp` as open-notebook's own automation surface.
**It is not.** Verified against the PyPI JSON API at write time:

```
open-notebook-mcp 0.3.0
  Homepage:   https://github.com/Epochal-dev/open-notebook-mcp
  Author:     Piotr Mrzygłowski
```

`Epochal-dev/open-notebook-mcp` is a different org — 41 stars, MIT, last pushed **2025-12-22**.
`lfnovo` owns no MCP repo (all 20+ of his public repos were enumerated).

> **So the "easy automation path" is: run unreviewed code from an unrelated 41-star org, eight
> months stale, against a local service holding your decrypted API keys.** That is the same
> shape as the §4 problem with a different vector. **If open-notebook is ever adopted, use its
> own REST API on `:5055` and nothing else.**

### 2.4 ⚠️ `pip install open-notebook` installs NIST's unrelated package

Also verified at write time:

```
open-notebook 0.2.0
  License:    NIST-PD
  Homepage:   https://github.com/usnistgov/open-notebook
  Docs:       https://pages.nist.gov/open-notebook/
```

This is not a stale abandoned namespace — it is **actively maintained software from the US
National Institute of Standards and Technology that has nothing to do with this project**.
Docker is the only correct distribution path for `lfnovo/open-notebook`. That is a stronger
statement than the earlier pass's "PyPI is a dead end."

### 2.5 `podcastfy` is not stale — it is abandoned, and it is provable

`pushed_at` reads 2026-05-04, and the earlier pass took that at face value. The last three
commits are README book-promo edits. Filtering commits to the library path:

- **Last commit touching `podcastfy/`: 2025-12-09**, by `caiquecober` — *not the owner*.
- **Last GitHub release: v0.4.0, 2024-11-16 — 21 months ago.**
- `souzatharsis`: 182 of 243 commits (75%).
- **119 open issues.**

The decisive signal: four contributor PRs from **July 2026** (#310–#313, including a Gemini TTS
bugfix) sit with **zero comments**, and of the eight most recent issue comments repo-wide, **not
one is from the maintainer**. People are still trying to fix this project and nobody is home.

> **`pushed_at` is a liar.** Three of the candidates in this search — podcastfy,
> document-to-podcast, and to a lesser degree open-notebook's dependency tree — look alive by
> that field and are not. **Any future maintenance check in this repo should filter commits by
> path and exclude bot authors**, or it will produce exactly the reading this pass had to
> correct.

### 2.6 Smaller corrections

- **`document-to-podcast` is deader than reported.** The earlier "last commit 2025-08-26" is
  `pre-commit-ci[bot]`. Verified: the six most recent `main` commits are *all* bots. **Last
  human commit 2025-03-19.**
- **`Local-NotebookLM` has no console-script entry point.** `pyproject.toml` declares no
  `[project.scripts]`; invocation is `python -m local_notebooklm.make_audio`. Filter 1 still
  passes — it is fully scriptable — but calling it "a real CLI" oversells it. Also: v2.0.1
  shipped to PyPI 2026-05-08 with **no matching GitHub release**, and its "0 open issues" is
  low traffic (18 issues in the repo's entire life), not fast triage.
- **SurfSense's open-core carve-out is confirmed verbatim** — `LICENSE` states
  `surfsense_backend/app/proprietary/` is BSL-1.1 while the rest is Apache-2.0, and that
  directory exists.

**Verification stamp.** Re-pulled independently during the writing of this brief, all matching:
open-notebook 36,663★/MIT/pushed 2026-08-06; podcastfy 6,491★/119 open issues/last library
commit 2025-12-09/last release v0.4.0 2024-11-16; Local-NotebookLM 981★/Apache-2.0/pushed
2026-05-08; kokoro-tts 1,774★/MIT/pushed 2026-04-08; all four open-notebook advisories with
`first_patched_version: null`; document-to-podcast's six most recent `main` commits all bots;
the five `lfnovo` dependency push dates in §2.1; and both PyPI ownership records in §2.3–2.4.

---

## 3. Recommendation

**Nothing here is good enough. Adopt none of it. Gemini Notebook stays locked.**

That is the honest answer, and it is not a hedge — it is what falls out of applying the three
filters without flinching:

| | Clears filter 1? | Clears filter 2? | Clears filter 3? |
|---|---|---|---|
| `Local-NotebookLM` | ✅ (module, not CLI) | ⚠️ solo maintainer, zero external review | ✅ |
| `open-notebook` | ✅ REST API | ❌ CVSS 9.9, unresolvable advisories, 6 repos / 1 person | ✅ |
| `podcastfy` | ✅ best-shaped | ❌ abandoned | ✅ |
| everything else | ❌ or ❌ | ❌ | mixed |

**The comparison that ends the argument:** Gemini Notebook is $0 incremental on an already-paid
subscription, has **zero self-hosted attack surface**, and its role is already fenced by §8. The
only thing a replacement buys is automation — and `DECISIONS.md` has never logged automation of
this layer as a bottleneck. Adopting any of these means taking on a real, disclosed security
posture to solve a problem that has not yet been shown to exist.

### The least-bad option, stated precisely, for the day this changes

The single trigger that should reopen this is **§12.3 — the Gemini → vault export seam becoming
a measured bottleneck** (measured, not felt: e.g. a logged count of sources that never made it
into the vault). If that happens:

> **Take the audio slice only. `Local-NotebookLM` driven by `python -m`, with
> `nazdridoy/kokoro-tts` vendored and pinned as the voice engine, running fully local.**
>
> - It touches no third party's ToS, so §4 is not reopened.
> - It has the smallest attack surface of anything in this search that is still moving.
> - It leaves source-grounded Q&A with Gemini, which means §8's boundary is untouched and
>   Claude's mastery-gate role is not competed with.
> - **Read the source before running it.** Two contributors, no external review — this is
>   "least-unsafe," not "safe," and the difference is load-bearing.
> - **Do not** reach for `open-notebook` for the audio slice. Six repos, one person, and a
>   CERT-EU RCE is a materially worse trade for the same capability.

**Explicitly not recommended, at any threshold:** `open-notebook-mcp` (§2.3), `pip install
open-notebook` (§2.4), `podcastfy` as a live dependency, `SurfSense`, and every tool in the §4
disqualified list no matter how many stars it accumulates.

---

## 4. Other agentic-learning ideas worth stealing

**Separate from the NotebookLM question.** These surfaced during the search and have nothing to
do with audio overviews. None is a recommendation to adopt; each is a technique to remember.

### 4.1 ⭐ The screenshot → classify → card → next-session-seed capture pipeline

From the Encryptorium "Claude Code as a Study Operating System" writeup (Andreas Renz, real exam
prep — CISSP, TOGAF, post-quantum crypto). **Missed practice questions get screenshotted at the
moment of failure**, vision-classified, turned into flashcards, and seeded into the next
session's quiz automatically.

This is a different answer to **`DECISIONS.md` §11 item 2** (the study-session trigger) and to
the capture problem generally: it captures *the error*, at the moment it happens, rather than
asking you to remember to write it down later. That is precisely the shape the §3 "capture
inbox" mechanism exists to serve, and this is a more automatic version of it.

⚠️ **Caveat that must travel with it:** this generates cards without a human in the loop, which
collides head-on with `2026-08-10_claude-code-obsidian-learning-workflows.md` §7.4 (Kirkby &
Matuschak: **Claude Sonnet 5 produces unusable spaced-repetition prompts 42% of the time**).
Steal the *capture trigger*, not the *unreviewed generation*. **Grade: Moderate as a technique,
one practitioner, no outcome data.**

### 4.2 An independently-built agent literally called "the Examiner"

The same writeup describes a "personified Examiner agent" for rote memorization — a distinct
agent that quizzes and grades rather than teaches — plus flat-JSON state files
(`session-log.json`, `flashcard-scores.json`, `user-progress.json`) filling exactly the role
`tracker.md` fills here (§9).

**This is not validation.** It is one anecdote, and convergence between two people who read the
same genre of blog post is weak evidence. But an unprompted, independent arrival at the same
role boundary *and the same name* is worth logging as a sanity check on §8. **Grade: anecdote.**

### 4.3 `ad2969/obsidian-auto-anki` — the one tool touching both locked apps

An Obsidian plugin that generates Anki cards from vault notes. It sits directly across two
already-locked tools, which makes it worth a real audit **before build step 4 (`.apkg`
generation)** — not now. **It was not evaluated against the three filters in any pass.** Flagged
as existing; explicitly not recommended.

### 4.4 The DIY reference architecture is real and repeatable

Milvus (vectors) + Zep (memory) + Firecrawl (scraping) + AssemblyAI (STT) + **Kokoro 82M
(local TTS)**. Notable only because Kokoro appears independently in this stack *and* as
`Local-NotebookLM`'s engine *and* as a standalone CLI. **Kokoro is the piece with the most
independent corroboration in this entire search** — which is why §3 recommends vendoring it
rather than any tool that wraps it.

### 4.5 Already covered elsewhere — deliberately not re-litigated

AnkiConnect as a card-write path (a second independent practitioner confirmed it works;
`2026-08-10_claude-code-obsidian-learning-workflows.md` §7.3 already rejected the write path and
kept only the duplicate check) and `bevibing/tutor-skills` / `hluaguo/learn-faster-kit` (covered
in that same brief). Nothing in this search changes either read.

---

## 5. What could not be verified

Stated plainly rather than papered over.

1. **Reddit — no thread, quote, or vote count in this brief is from Reddit.** This environment
   cannot fetch `reddit.com` in any form: direct, `old.reddit.com/…/search.json`, and two mirror
   front ends all fail. Four separate `site:reddit.com` queries returned **zero reddit.com URLs**
   and silently substituted GitHub/blog/aggregator content while narrating it as community
   sentiment. **Real user-experience validation of any tool here therefore does not exist in
   this brief.** It requires a different fetch path or manual review by Orlando directly. Same
   failure shape logged in `2026-08-08_prior-art.md` and the Claude-Code/Obsidian brief.
2. **"Deta Surf"** — surfaced repeatedly in aggregator listings; **never verified to exist as
   described**. Dropped rather than listed as a candidate.
3. **The Milvus/Zep/Firecrawl/Kokoro pipeline's automation surface** — the post reads as real,
   runnable code with a reproducible environment link, but **no CLI or API detail was
   retrievable**, so filter 1 is *unconfirmed*, not passed.
4. **Whether `open-notebook`'s advisories are genuinely remediated in the running code.** The
   prose says v1.8.4; the structured metadata says nothing; **no scanner can confirm it and this
   search did not read the patch**. Treated as unresolved.
5. **Whether the four advisories were ever exploited in the wild.** Nothing found either way.
   Absence of evidence only.
6. **`Local-NotebookLM`'s actual output quality.** 18 lifetime issues, no substantive
   first-person account found. **Nobody has publicly reported using it for anything.** Its
   ranking here rests entirely on *attack surface*, not on evidence it produces usable audio.
7. **`KnowNote`'s licensing and hosting model** — not independently verified. Assumed hosted
   SaaS on indirect signals; not treated as a candidate either way.
8. **Any retention or learning outcome for any tool in this brief.** Zero. Nobody measured
   anything. `DECISIONS.md` §1's standing caveat applies without exception.
9. **The `esperanto` provider claims** (22 LLM providers, local Ollama included) — read from
   documentation, never executed.

---

## 6. Confidence grades

| Claim | Grade |
|---|---|
| A self-hostable NotebookLM-alike category genuinely exists and is active | **High** — 28 repos, several >5k★, verified via API |
| `open-notebook` is the most-used and best-documented of them | **High** — API-verified metrics plus an independent first-person deployment writeup (Hetzner CX22 + M2 MBA, 3-speaker profile, real cost figures) |
| `open-notebook`'s contributor base provides a real bus factor | **Rejected** — 78% single-author; 3 solo repos on the critical path |
| `open-notebook`'s advisories are machine-unresolvable | **High** — `first_patched_version: null` on all four, re-pulled at write time |
| `open-notebook-mcp` is third-party, not the maintainer's | **High** — PyPI metadata names `Epochal-dev`; re-verified at write time |
| `pip install open-notebook` installs NIST's package | **High** — PyPI metadata: `NIST-PD`, `usnistgov` |
| `podcastfy` is abandoned rather than merely quiet | **High** — path-filtered commit history, release dates, unanswered July 2026 PRs |
| `document-to-podcast` is bot-maintained only | **High** — six most recent `main` commits all bots |
| `Local-NotebookLM` is automatable | **Moderate–High** — `python -m` module + Python API confirmed; no console script |
| `Local-NotebookLM` produces usable audio | **Not covered** — no usage evidence found at all |
| Any of these is safe to run on a personal machine today | **Rejected** — every candidate fails filter 2 in a way that must be actively accepted |
| Automating this layer would improve learning outcomes | **Not covered** — no evidence exists for any tool here |
| The §4 rejection of NotebookLM automation is still correct | **High** — `notebooklm-py`'s own README confirms undocumented-RPC access |

---

## 7. What this means for THIS build

1. **No `DECISIONS.md` change. §1 and §4 both stand.** Gemini Notebook remains the locked
   reading-accommodation layer, and §4's rejection is reconfirmed with the specific tool
   ecosystem named so it can be recognized and declined on sight.

2. **Record the two namespace traps in §4's rejection row or alongside it.** `open-notebook-mcp`
   is a third-party 41-star package eight months stale, and `pip install open-notebook` is
   NIST's software. Both are the kind of thing a future session re-derives the hard way.

3. **Keep `open-notebook` Queued, not Locked** — same call as both prior briefs, now on
   materially stronger grounds. It is the only candidate with real usage evidence *and* the only
   one with a Critical-RCE history in a one-maintainer dependency.

4. **The one trigger to reopen this is §12.3, and it must be measured.** "The Gemini→vault
   export feels annoying" is not the trigger. A logged count of material that never reached the
   vault is. None of these tools fixes that seam anyway — they relocate it — so the fix is more
   likely to be the `.raw/` immutable-source convention already proposed in
   `2026-08-10_claude-code-obsidian-learning-workflows.md` §6.3 than a new service.

5. **If the audio slice is ever automated, it is `Local-NotebookLM` + vendored `kokoro-tts`,
   local-only, source read first** — never `open-notebook`, never an MCP wrapper, never a tool
   that also wants to answer questions (which would put a second always-explaining chatbot
   inside the §8 boundary that Bastani et al. 2025 is the reason for).

6. **Adopt `pushed_at` skepticism as a standing research rule.** Three candidates in this search
   looked maintained by that field and were not. Any maintenance claim in a future brief should
   be **path-filtered and bot-excluded**, or it is not a maintenance claim.

7. **The Reddit gap is now logged twice.** Two consecutive briefs have been unable to reach real
   user-experience discussion from this environment. That is a structural limit on what this
   research can conclude about *whether tools actually work in practice*, and it should stop
   being rediscovered per-brief. **Every "works in practice" claim in this repo currently rests
   on GitHub metadata plus a handful of blog posts.**
