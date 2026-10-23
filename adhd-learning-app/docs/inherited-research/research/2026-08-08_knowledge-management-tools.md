# Knowledge-Management / Note-Taking Tools — Verified Survey

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.** Second half of research question 6 — see
> `2026-08-08_adhd-tools-landscape.md` for the ADHD-productivity-app half (Focusmate, Tiimo,
> Sunsama, Structured, Llama Life, Goblin Tools). Not repeated here.
> **Date:** 2026-08-08 · **~28 candidate sources discarded for failing verification** (see per-section
> counts) · Prices read from vendor pricing pages / official App Store listings, not aggregators.
> Roam Research's own pricing page could not be rendered (SPA); its figures are UNVERIFIED.

## Headline: **the walled-garden pattern breaks here.** Logseq and Anki are real open source (AGPL-3.0); Excalidraw is MIT. Roam ships a vendor-official AI-agent read/write API — nobody in the ADHD-productivity survey had that. But the core evidence question is a clean **"not covered"**: no controlled study of any specific PKM tool improving learning outcomes exists, and this project's own prior FSRS grade was too optimistic — **verified and corrected down** below.

---

## Pricing (verified from vendor page unless flagged)

| Tool | Price | Free tier | Verification |
|---|---|---|---|
| **Obsidian** | Core app **free**, Sync $4/mo (annual) / $5/mo, Publish $8/mo (annual) / $10/mo, Catalyst $25 one-time, Commercial $50/user/yr | ✅ Full core app, no paywall | ✅ vendor page fetched |
| **Logseq** | Core app **free**, no feature gating | ✅ Unlimited, local-first | ✅ core confirmed; Sync price **UNVERIFIED** — vendor's own blog describes $5/$15 as *beta Open Collective donation tiers*, explicitly not yet a finalized public price |
| **RemNote** | Free $0/mo; Pro **$8/mo ($96/yr)**; Pro+AI **$18/mo ($216/yr)** | ✅ Unlimited notes/flashcards, 100 AI credits/mo | ✅ vendor page fetched |
| **Heptabase** | Pro **$8.99/mo**; Premium **$17.99/mo**; Premium+ **$53.99/mo** | ❌ No free tier | ✅ vendor page fetched |
| **Roam Research** | ~$15/mo or $165/yr; "Believer" $500/5yr (converged secondary figures only) | ❌ (per all sources) | ⚠️ **UNVERIFIED** — vendor SPA unrenderable, /pricing 404s, archive.org unreachable |
| **Anki** desktop | **Free**, AGPL-3.0-or-later | ✅ Full app | ✅ LICENSE file fetched |
| **AnkiMobile** (iOS) | **$24.99 one-time** | — | ✅ live App Store listing |
| **AnkiDroid / AnkiWeb sync** | Free | ✅ | ⚠️ Moderate — not independently re-fetched |
| **CmapTools** | Free to use (incl. commercial, per current beta terms) | ✅ | ✅ IHMC license page fetched |
| **Excalidraw** | Free, MIT OSS core; Excalidraw+ is separate paid SaaS | ✅ | ✅ LICENSE fetched |
| **tldraw** | Free for hobby/dev (watermarked); commercial license required for production, reportedly **~$6,000/yr/team** | ⚠️ Restricted, not unrestricted free | License mechanics ✅ verified; price figure ⚠️ UNVERIFIED (secondary source, not tldraw's own pricing page) |

---

## Mechanisms worth stealing

### 🏆 Roam Research — the only vendor-official AI-agent read/write surface found
`Roam-Research/roam-tools` ships an **official MCP server + CLI**, explicitly built so Claude/Cursor can read and write a user's graph: search (incl. semantic), Datalog queries, create/update/delete blocks and pages, append to daily notes, move blocks, upload files. The repo's own docs carry a blunt warning: *"This MCP server gives Claude full read and write access to your Roam graph... Changes may be difficult or impossible to undo."* Nothing else in this survey — or the prior ADHD-productivity survey — has a vendor-shipped agent API this direct. **The stealable part isn't Roam the app; it's the fact a vendor built and shipped this integration pattern at all** — proof an agent-driven write path into a PKM graph is a solved, productized problem, not a research question.

### Obsidian — local-first plain files + a spun-out open format
Every note is a `.md` file on disk in a folder ("vault") — no DB, no cloud dependency to function. Plugin API (`obsidianmd/obsidian-api`, MIT) exposes `Vault` (file I/O), `MetadataCache` (parsed links/tags/embeds), `Workspace`. Canvas data is **JSON Canvas** — an open MIT-licensed spec (`nodes`/`edges` arrays) Obsidian deliberately released as implementation-agnostic (jsoncanvas.org, v1.0 March 2024) so other tools can read/write `.canvas` files without Obsidian itself. **The stealable part: the format was decoupled from the app on purpose.**

### Logseq — block-addressable outliner + native SRS, no export step
Every bullet is a block with a persistent UUID — the addressable unit, not the file. Two distinct link primitives: **block reference** (window — can't edit source from it) vs. **block embed** (portal — can edit source through it). A `#card` tag turns any block into a spaced-repetition flashcard reviewed in-app; no export to a separate SRS tool. Data is plain Markdown/Org-mode on local disk.

### RemNote — the fused notes+flashcard document, now on FSRS
Any "Rem" (bullet) can be marked a flashcard inline (`::` concealment syntax) and reviewed without leaving the document — no Notion→Anki export step. Since **RemNote 1.16** FSRS is the default scheduler, replacing a custom SM-2 variant (the community's `fsrs4remnote` plugin was archived specifically because FSRS became native). Documented plugin SDK (`plugins.remnote.com`, `@remnote/plugin-sdk`) with a real Rem-object read/write API — but storage is cloud-sync-primary, not local files; a user feature request for Logseq-style local Markdown storage is still open.

### Heptabase — cards as single objects placed on multiple canvases
A card (atomic note) can be spatially arranged on several different whiteboards **without duplication** — one source of truth, many spatial contexts. Cards retain provenance links back to source PDFs/YouTube transcripts rather than becoming free-floating quotes. Local storage is on-device with AWS sync when enabled (closer to local-first than RemNote) — but **no official public API was found**, only an unofficial community scraper (`draJiang/heptabase-api`).

### Anki — SQLite + a de facto community REST API
`collection.anki2` is a plain **SQLite** database; `.apkg` exports are zip-wrapped SQLite + media — trivially readable/writable by any external tool with a SQLite library, no vendor API required. **AnkiConnect** (third-party add-on, not core) exposes a local JSON-RPC HTTP server (`127.0.0.1:8765`) for programmatic card/deck CRUD — this is the de facto standard integration path used by tools like Yomitan. Note-type/template/card separation (fields × template × instantiation) is a genuinely reusable data-modeling pattern for generating many card variants from one fact.

### Excalidraw / tldraw — open JSON scene formats built for programmatic writes
Excalidraw's `.excalidraw` JSON schema (elements array, appState) is documented and versioned (docs.excalidraw.com) — an agent can write valid scene JSON directly, no UI interaction needed. tldraw has a comparable Editor API (tldraw.dev) but changed licensing at SDK v4.0 (2025) from permissive OSS to a proprietary "tldraw SDK License" — free only for hobby/dev use (watermarked), commercial deployment requires a paid license.

---

## Open source? (the previous survey found **zero** in the ADHD-productivity category — does that hold here?)

**No — it does not hold here.** Real OSS appears repeatedly in this category:

| Tool | License | Repo | Verification |
|---|---|---|---|
| **Logseq** | **AGPL-3.0** | github.com/logseq/logseq | ✅ LICENSE.md fetched directly |
| **Anki** desktop | **AGPL-3.0-or-later** (+ BSD-3 contributed portions) | github.com/ankitects/anki | ✅ LICENSE fetched directly |
| **AnkiDroid** | Free/open (GPL-family reported) | — | ⚠️ Moderate — not independently fetched |
| **Excalidraw** core | **MIT** | github.com/excalidraw/excalidraw | ✅ LICENSE fetched directly |
| **Mnemosyne** | GPL-lineage, exact variant **contradicted across sources** (GPLv3+ vs. AGPLv3 core/LGPLv3 sync client) | github.com/mnemosyne-proj/mnemosyne | ⚠️ Extrapolated — primary LICENSE file 404'd; contradiction flagged, not resolved |
| **tldraw** | Was permissive OSS; **as of SDK v4.0 (2025), proprietary "tldraw SDK License"** — source-available, commercial-use gated | github.com/tldraw/tldraw | ✅ LICENSE.md fetched directly |
| **Obsidian** core app | **Proprietary**, closed source (auxiliary API/format repos are MIT) | — | ✅ confirmed absent from `obsidianmd` org; forum-confirmed |
| **RemNote** core app | **Proprietary** (plugin examples repo is open, core is not) | — | ⚠️ Moderate — no positive vendor statement found, inferred from repo-org structure |
| **Heptabase** | **Proprietary** | — | ⚠️ Moderate — search-synthesized, not a direct vendor statement |
| **Roam Research** | **Proprietary** (official `roam-tools` MCP/CLI repo is open, core app is not) | — | ⚠️ Moderate — vendor page unfetchable; independent OSS clones (Athens, Logseq, org-roam) exist specifically because Roam itself is closed, which corroborates |
| **CmapTools** | Free to use, **not open source** — IHMC states code/structure are proprietary trade secrets | — | ✅ IHMC license page fetched directly |

---

## Public API / plugin surface / local data format — build vs. buy vs. compose

| Tool | Vendor-official programmatic write path? | Local-first storage? | Verdict |
|---|---|---|---|
| **Roam Research** | ✅ **Yes** — official MCP server + CLI, built for AI agents | Cloud-based; local desktop caching reported, not vendor-confirmed | **Compose** — best integration path in the whole survey, but proprietary core and unverified pricing |
| **Obsidian** | ✅ Documented plugin API (MIT); no official REST API (community plugin only) | ✅ Plain `.md` files on disk | **Compose** — plain files mean an agent doesn't even need the plugin API to read/write; it can write Markdown directly to the vault folder |
| **Logseq** | Plugin system exists, but its API surface wasn't independently confirmed this pass (docs page unfetchable) | ✅ Plain Markdown/Org-mode files on disk | **Compose** — same file-level argument as Obsidian, plus it's OSS so the app itself is forkable |
| **Anki** | ⚠️ Not vendor-official — AnkiConnect is a third-party add-on; alternative is direct SQLite/`.apkg` write | Local SQLite DB | **Compose** — no vendor API needed; SQLite/`.apkg` generation is a fully viable programmatic path |
| **RemNote** | ✅ Documented plugin SDK + Rem API | ❌ Cloud-sync primary | **Compose, with a dependency on their cloud** |
| **Heptabase** | ❌ No official API; only an unofficial scraper | ⚠️ Partial (local cache + AWS sync) | **Buy or skip** — no real integration path found |
| **Excalidraw** | ✅ Open, documented `.excalidraw` JSON schema + embeddable API | ✅ Open JSON format | **Compose** — agent can write scene JSON with no runtime dependency on Excalidraw at all |
| **tldraw** | ✅ Editor API, but commercial license required for production use | — | **Buy** (license) **or avoid** for a shipped product |
| **CmapTools** | ❌ No public API | — | **Skip** |

**Build-vs-buy-vs-compose answer to the brief's Q3:** for a `specs/` + `src/` + `system/` agent-driven system, **Obsidian and Logseq are the strongest programmatic-write targets** — both store data as plain Markdown files, so an agent can write directly to the vault folder with zero API dependency, zero vendor lock-in, and (for Logseq) a forkable OSS core if the vendor ever disappears. **Roam is the most *sophisticated* integration** (a real agent-facing MCP server) but trades that for a closed, unverified-pricing, cloud-only core. **Anki is the strongest target specifically for the SRS/review-queue piece** — SQLite + `.apkg` generation is dependency-free and the format is stable and documented.

---

## Q1 — FSRS: the correction is **verified, not refuted**

Pulled directly from the primary source (`open-spaced-repetition/srs-benchmark` README, raw-fetched, not a search snippet):

| Algorithm | Params | Log Loss ↓ (no same-day) | RMSE(bins) ↓ | AUC ↑ |
|---|---|---|---|---|
| **MOVING-AVG** (outputs the user's recent average retention — an "algorithm" with **zero learned parameters**) | **0** | **0.3369** | **0.0592** | 0.7001 |
| FSRS-7 (current) | 35 | 0.3437 | 0.0655 | 0.7069 |
| FSRS-6 (Anki's shipped default) | 21 | 0.3460 | 0.0653 | 0.7034 |
| FSRS-5 | 19 | 0.3560 | 0.0741 | 0.7011 |
| FSRS-4.5 | 17 | 0.3624 | 0.0764 | 0.6893 |

- **What the benchmark measures:** the vendor's own README states its purpose verbatim: *"to assess the predictive accuracy of various algorithms."* It's a **calibration-only** benchmark — log loss / RMSE / AUC on next-review recall prediction against ~350–520M held-out real Anki reviews. It contains **no controlled trial** comparing actual learning outcomes (retention, exam performance, time-to-mastery) between FSRS-scheduled and SM-2-scheduled learners. Grade: **High — rely on as-is** for what it measures.
- **The zero-parameter baseline claim:** verified, and **understated** if anything — the 0-parameter MOVING-AVG baseline **beats every FSRS version shown, including FSRS-6 (Anki's current shipped default) and FSRS-7**, on both Log Loss and RMSE. FSRS only wins clearly on AUC (discrimination, not calibration). Grade: **High — rely on as-is**.
- **Learning-outcome evidence for FSRS vs. SM-2:** none found. No RCT of FSRS-scheduled vs. SM-2-scheduled human learners' retention/exam performance exists in the `open-spaced-repetition` org's own materials or elsewhere searched. Grade: **Not covered.**
- **Academic paper citation:** a claimed formal FSRS publication could not be resolved to a real DOI/arXiv ID this pass — **discarded**, not cited.

**Corrected grade:** "FSRS predicts recall probability better than SM-2" → **Moderate — directional** (real edge on AUC, but a free baseline matches or beats it on the benchmark's own headline calibration metrics). "FSRS produces better learning outcomes than SM-2" → **Not covered.** Do not restore the old optimistic grade.

## Q2 — Any controlled study of a PKM tool improving learning outcomes?

**Not covered — a well-supported negative.** Two independent research passes ran 12+ differently-angled queries (general web + PubMed-domain-restricted, e.g. `site:pubmed.ncbi.nlm.nih.gov Obsidian OR Roam OR Logseq note-taking tool`, which returned **zero** PubMed hits for any of those three tool names by name) and found **no controlled trial, with a control group and an objective outcome measure, naming a specific PKM tool** (Obsidian, Roam, Logseq, RemNote, Heptabase, Notion) as the tested intervention.

What exists instead, explicitly **not** conflated with tool-specific evidence:
- **Note-taking as an activity, not software:** Mueller & Oppenheimer 2014 ("The Pen Is Mightier Than the Keyboard," PMID 24760141) — longhand vs. laptop, and later multi-lab replications shrank the effect to small/nonsignificant.
- **Concept mapping as a technique, not software:** Schroeder/Nesbit/Anguiano/Adesope 2017 meta-analysis (*Educ. Psychol. Rev.*, DOI 10.1007/s10648-017-9403-9) and a 2025 STEM meta-analysis (DOI 10.1186/s40594-025-00554-2) show moderate-large effects (g≈0.58–0.63) for the *activity* of concept mapping — not an evaluation of CmapTools/Excalidraw/tldraw specifically.
- **Spaced repetition as a technique, not software:** solid controlled-trial evidence it beats conventional study (e.g. PMC11186069, PMC12343689, both real peer-reviewed education RCTs) — but these test the technique, not RemNote or Anki as products.
- **One flagged near-hit, not fully verifiable:** Malashenko et al. 2023, "A Digital Model of Full-Cycle Training Based on the Zettelkasten and Interval Repetition System," *Emerging Science Journal* 7, DOI 10.28991/ESJ-2023-SIED2-01 (DOI resolves live). Reportedly a two-group achievement-test comparison favoring a "Zettelkasten + interval-repetition digital model." **Not fully verified** — full text was unreadable (garbled OCR / socket errors on two fetch attempts), so sample size, randomization, and effect size are unconfirmed, and it's unclear whether "Zettelkasten" means a named app or a bespoke research tool. Grade: **Extrapolated — tune by feel.** Flagged, not relied on.

## Q3 — see the "build vs. buy vs. compose" table above.

## Q4 — Retention-vs-adherence: social/commitment mechanisms in these tools?

**None found.** Every mechanism surfaced across all four research passes is either a solo data-structure feature (block references, spatial canvases, flashcard scheduling) or a solo review ritual (Anki reviews, Logseq `#card`). **No social or commitment mechanism** — no team competition, no accountability partner, no reputation score, no shared-streak feature — was found in Obsidian, Logseq, RemNote, Heptabase, Roam, or Anki. (Compare the ADHD-productivity survey: Focusmate's reputation-score/account-freeze commitment device was the standout mechanism there, and none of it has an analog in this category.) This is a **gap, not a finding to build on** — the PKM/SRS category is uniformly solitary-use, unlike the productivity-app category which had at least one strong commitment-device example.

---

## Not covered / unverified

- Logseq Sync current public price (vendor's own post frames the $5/$15 figures as beta donation tiers, not finalized pricing)
- Roam Research pricing and full plugin/local-storage architecture (vendor SPA unrenderable this pass)
- Heptabase's exact license-status statement from the vendor itself (inferred, not a direct quote)
- Mnemosyne's exact license variant (GPLv3+ vs. AGPLv3+LGPLv3 — sources contradict, primary LICENSE file 404'd)
- Logseq's exact SRS algorithm variant ("SM-5" — secondary-sourced only)
- AnkiDroid's exact license and AnkiWeb sync free-tier limits (not independently re-verified)
- tldraw's reported $6,000/yr commercial price (secondary source, not tldraw's own pricing page)
- Whether Anki's FSRS became the *default* (vs. merely available) scheduler, and in which exact version — the native-availability version (23.10, Oct 2023) is confirmed; the default-on version is not
- The Malashenko et al. 2023 Zettelkasten study's methodology (see Q2)

**Total candidate sources discarded across all four passes for failing citation verification: ~28** — 5 general spaced-repetition RCTs (real, resolvable, but not tool-specific, so not used as tool evidence), ~12 secondary pricing-aggregator sites, 5 Anki/FSRS-adjacent blog posts and one unresolvable academic-paper claim, and ~6 marketing/blog "evidence" claims for graph-view or spatial-canvas learning benefits.

---

## Implications

1. **The open-source gap from the productivity-app survey does not repeat here.** Logseq (AGPL-3.0), Anki (AGPL-3.0), and Excalidraw (MIT) are real, forkable OSS — a genuine build option exists in this category that didn't exist in the last one.
2. **Plain-file storage (Obsidian, Logseq) is the actual integration answer to "can an agent write into this."** No API is even required — write Markdown to the vault folder. This beats every cloud-native competitor (RemNote, Heptabase, Roam) on build-vs-buy grounds regardless of their feature depth.
3. **FSRS's evidence was over-graded before; the corrected grade is Moderate at best, and only for calibration — not learning outcomes.** A free, zero-parameter moving average matches or beats it on the benchmark's own headline metric. Don't cite FSRS as a settled win when picking a scheduler.
4. **No controlled study of any PKM tool improving learning outcomes exists, searched two ways.** Anything built on top of Obsidian/Logseq/Anki/etc. inherits zero outcome evidence from the platform choice — the evidence, if any, will have to come from this project's own design, not from borrowing credibility off these tools.
5. **This category has no commitment-device analog to Focusmate's reputation score.** If the design doc wants the compounding social-adherence mechanism from the adherence review, it will not come from a PKM tool integration — it has to be built separately, on top of whichever storage layer (Obsidian/Logseq) is chosen for content.
6. **Anki's SQLite/`.apkg` format is the cleanest SRS target for programmatic card generation** — no vendor API dependency, stable and documented format, real community precedent (AnkiConnect) for the alternative live-write path.
