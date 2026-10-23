# NotebookLM-Alternative Pipelines and Learning Automation — Practitioner Writeups (Substack / dev.to / Medium)

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-10
> **Scope:** first-person practitioner accounts (Substack, personal blogs, dev.to, Medium) of
> building or using a NotebookLM-alternative pipeline, or any automated document→audio/podcast
> or source-grounded-Q&A pipeline. Distinguishes genuine practitioner writeups from
> content-marketing repackaging of the same "AI second brain" pitch. Also logs any interesting
> agentic-AI-for-learning tool/technique noticed along the way, NotebookLM-shaped or not.
> **Does not repeat** `2026-08-10_notebooklm-alternatives-reddit.md`, which already did the
> GitHub-primary security/maintenance audit of `lfnovo/open-notebook` and ranked it the one
> candidate clearing all three filters. This brief adds first-person usage evidence for that
> same tool, plus a separate finding that materially affects `DECISIONS.md` §4 and is the most
> important thing in this brief — see §1.
> **Method:** WebSearch + WebFetch against individual posts. Several Substack posts were
> paywalled past the first section; graded accordingly, not treated as unreachable.

---

## 1. Important finding: "notebooklm-py" / "NotebookLM MCP" is the exact thing §4 already rejected, just repackaged

`DECISIONS.md` §4 rejected "NotebookLM MCP / browser automation / burner Google account" with
the reasoning: *no public API (enterprise-gated only); Patchright stealth automation is a ToS +
fragility problem.* Two of the practitioner posts found in this search (`buildtolaunch.substack.com`,
`prosperinai.substack.com`) recommend exactly this, under a name that sounds official but isn't:

- **`teng-lin/notebooklm-py`** (verified via GitHub/PyPI) — its own README states plainly: *"Unofficial
  Python client for Google NotebookLM that uses undocumented RPC APIs."* It works via Google's
  internal `batchexecute` RPC protocol with **obfuscated, undocumented method IDs that Google can
  change at any time** — not a public API, not enterprise-gated access, a reverse-engineered
  private-endpoint wrapper. It ships a Claude Code skill/CLI, which is exactly why it shows up in
  "Claude Code + NotebookLM" workflow posts looking like sanctioned tooling.
- A parallel ecosystem of **at least seven** "NotebookLM MCP server" GitHub repos (`kkaminsk`,
  `PleasePrompto`, `m4yk3ldev`, `alfredang`, `moodRobotics`, `Pantheon-Security`,
  `set2374`/`notebooklm-mcp-cli`) exists, all wrapping the same undocumented surface — several via
  outright **browser automation** (`kkaminsk`'s explicitly says "browser automation"), one
  advertising "17 security hardening layers" (a strange thing to need for a personal research tool,
  and itself a signal the underlying surface is fragile/adversarial).

**Why this matters for this project specifically:** the `buildtolaunch.substack.com` post ("Claude
Code + NotebookLM: 9 Workflows I Run Weekly") explicitly told readers it uses "a free MCP server
(NotebookLM's)" — phrasing that reads as Google-provided. It is not. `prosperinai.substack.com`
("NotebookLM Is Now Gemini Notebook. Here's What I Built Instead") uses `notebooklm-py` directly
as its automation layer for a Claude-Code-driven study pipeline that otherwise looks a lot like
what §8 already locks (Gemini grounds, Claude organizes/grades).

**Recommendation:** no change to §4 — it already correctly rejected this category, this just
confirms the rejection is still current and names the specific tool ecosystem to keep avoiding if
"just use the MCP server" comes up again, since it will keep resurfacing under official-sounding
names. Treat any post recommending `notebooklm-py` or a "NotebookLM MCP server" as recommending
ToS-violating reverse-engineered API access, full stop, regardless of how the post itself frames it.

---

## 2. `lfnovo/open-notebook` — independent first-person usage confirms the prior brief's read

Three separate practitioner accounts (not the maintainer, not each other) converge on the same
verdict as the 2026-08-10 GitHub-primary audit:

**`dev.to/andrew-ooo` — real hands-on review, most technically substantive of the three.**
Ran it on a Hetzner CX22 (4GB/2vCPU) and a 16GB M2 MacBook Air — i.e., actually deployed it, not
just read the README. Built a working example: a three-speaker "VC pitch debate" podcast profile
(skeptic/optimist/moderator, distinct ElevenLabs voice IDs, JSON-configured personality prompts and
template variables) fed a startup's pitch deck + an HN thread + a CrunchBase page, producing a
14-minute episode. Reports real cost data (~$0.20–0.40 per 12-minute episode on ElevenLabs Flash
v2) and real friction: SurrealDB OOMs below 4GB RAM, citations are "basic... not NotebookLM-grade,"
UI is "utilitarian," and the Episode Profile docs were thin enough he had to read the source. Also
confirms the REST API supports real automation — his stated use case was "auto-generate a weekly
podcast from starred articles." This is a genuine practitioner account, not marketing.

**Other dev.to posts** (`vigoss_luke_...`, `lightningdev123`, xda-developers, makeuseof) repeat
largely the same shape (self-hosted, podcast generation, REST API) with less first-person technical
detail — closer to well-informed reviews than build logs, but not contradicting andrew-ooo's account.

**Net effect on the prior brief's recommendation: unchanged, and now better supported.** The
security-advisory history (Critical RCE, three High findings, all patched) stands; the "run it
localhost-only, keep it updated" posture is corroborated by a real deployment story rather than
just docs review. Still: **queued, not locked** — nothing here shows the Gemini Notebook → vault
export friction has actually become painful enough to justify the added self-hosting burden.

---

## 3. `blog.dailydoseofds.com` — a real, different open-source pipeline, not Open Notebook

**"[Hands-on] Build a 100% open-source alternative to NotebookLM!"** is a distinct build from Open
Notebook, worth logging as a second reference architecture:

| Layer | Tool |
|---|---|
| Vector DB | Milvus |
| Conversation memory | Zep |
| Web/YouTube scraping | Firecrawl |
| Speech-to-text | AssemblyAI |
| Text-to-speech (podcast) | Kokoro 82M — fully open-source, runs locally |

Reads as real, runnable code (a Lightning AI Studio link is provided for a reproducible
environment), not a marketing post. Weaker than the Open Notebook writeups on one count: no CLI/API
automation detail was retrievable from the fetched content, so **filter 1 (actually automatable)
is unconfirmed for this specific pipeline** — it may well have one, but it wasn't verifiable in
this pass. Notable mainly as evidence that Milvus + Zep + Firecrawl + Kokoro is a live, working
combination people are actually assembling, independent of the Open Notebook project. Not a
recommendation — a second data point that the "roll your own NotebookLM" pattern is real and
repeatable, not one project's idiosyncratic choice.

---

## 4. Two Medium posts that are the most directly relevant finds in this whole search

**`encryptorium.medium.com`, "How I Turned Claude Code into a Study Operating System"** (Andreas
Renz) — **the single most relevant practitioner account found**, and not because of NotebookLM.
This person independently built a Claude-Code-centric study system with strong structural overlap
to this project's own locked architecture, for real exam prep (CISSP, TOGAF, post-quantum crypto):

- A **scaffold repo** (reusable workflows/tools/templates) plus **per-topic repos**, each with
  `workflows/`, `app/`, `data/`, `tools/`, and a `CLAUDE.md` — directly analogous to this project's
  `tracker.md`-as-sole-durable-state pattern (`DECISIONS.md` §9), independently arrived at.
  Flat-JSON state files (`session-log.json`, `flashcard-scores.json`, `practice-scores.json`,
  `user-progress.json`) fill the same role `tracker.md` fills here.
  - **A "personified Examiner agent" for rote memorization** — the same *word*, the same *role
    boundary concept* (a distinct agent that grades/quizzes rather than teaches), independently
    named and built by someone with no connection to this project. This is not evidence the design
    is correct — it's one more anecdote, not a study — but it is a genuine, unprompted convergence
    worth noting as a sanity check on the architecture, not as validation of it.
  - A **screenshot → vision-classification → flashcard-generation → next-session-quiz-seeding**
    pipeline (ShareX screenshots of missed questions get turned into scheduled review material) —
    a concrete, different-from-anything-in-this-repo technique for capturing errors as they happen
    rather than after the fact. Possibly relevant to the still-open Q2 (study-session trigger /
    capture) in `DECISIONS.md` §11.
  - **No mention of NotebookLM, audio overviews, or source-grounded Q&A anywhere in the piece** —
    it solves a different slice (retrieval practice + tracking), not the reading-accommodation
    slice.
  - Reads as genuinely first-person: admits the classifier mislabels sometimes, states plainly "it
    is not a replacement for studying," documents maintenance overhead. No promotional tone, no
    product being sold.

**`actuallymaybe.com/blog/agentic-ai-anki-flashcard-creation`** (Micheál Reilly) — a real, narrow,
useful practitioner account of **Claude Code + AnkiConnect** (the long-standing local Anki HTTP
API add-on) to generate cards directly into a live Anki deck instead of copy-pasting. Concrete
examples given: trigonometric-identity cloze variations with derivation cards, and Polish noun
declension drills with contextualized case-form cards. Directly corroborates `DECISIONS.md`'s
already-locked "card generation via scripts, mandatory human review" line (§11 item 6, and the
`anki-llm`/`pdf2anki` row in §1) — this is a second, independent person doing the same
AnkiConnect-based pattern successfully, for a similarly memorization-heavy domain (grammar/formula
drills, not unlike F&I terminology). Worth naming as a concrete implementation reference if/when
this project builds its own AnkiConnect script, since it confirms the friction point
("without AnkiConnect you're stuck copy-pasting, which defeats the purpose") and the fix.

---

## 5. Content-marketing pattern, confirmed again

As expected from the prior briefs' skepticism, most of what search engines surface under "built a
NotebookLM alternative" is SEO listicle content, not practitioner writeups: `storyflow.so`,
`atlasworkspace.ai`, `articlecast.ai`, `podcastify.io`, `medevel.com`'s "12 Free Self-hosted
Alternatives" roundup, `notelyn.com`, `studycardsai.com`, `flica.app`, `notefren.app`. All follow
the same shape this project's other research already flagged: generic "AI second brain" framing,
no first-person build detail, often thinly disguised advertising for the SEO site's own paid
product (StudyCards AI, NoteFren, Notelyn all pitch themselves inside their own "how AI helps
studying" posts). None added information beyond what §§1–4 above already cover. Not itemized
further — naming the pattern once, per this project's existing discipline, is enough.

**One from this batch is worth a specific callout:** `growwithaiguide.substack.com`, "These 8
Extensions Make NotebookLM 10x Better," and `techysurgeon.substack.com`'s "Learner Pack" tutorial
both use "10x" framing on an unmeasured claim — the exact pattern
`2026-08-09_10x-learning-claims-audit.md` already named and retired. Skipped, not fetched in
depth, on the strength of that prior finding alone.

---

## 6. Other agentic-AI-for-learning tools/techniques noticed, not NotebookLM-shaped

- **`ad2969/obsidian-auto-anki`** (GitHub, surfaced in search, not deep-audited here) — an Obsidian
  plugin that uses AI to auto-generate Anki cards from vault notes. Directly adjacent to this
  project's stack (Obsidian + Anki, both already locked) but **not evaluated against the three
  filters in this pass** — flagging its existence only, since a plugin that touches both locked
  tools at once is exactly the kind of thing worth a real look before Phase 4 (`.apkg` generation)
  is built, not recommending it yet.
- **The screenshot-to-flashcard capture pipeline** from the Encryptorium post (§4) — a genuinely
  novel-to-this-project technique for turning an in-the-moment mistake into a scheduled review item
  automatically, worth remembering against the still-open capture/trigger question in
  `DECISIONS.md` §11 item 2, even though it has nothing to do with NotebookLM.
- **AnkiConnect as the concrete integration point** for any future Claude-Code-driven card
  generation (§4) — confirms the mechanism, not just the intent, behind the already-locked
  `anki-llm`/`pdf2anki` line in `DECISIONS.md` §1.

---

## Bottom line

1. **No change to any Locked decision.** §4's rejection of NotebookLM automation is reconfirmed,
   now with the specific tool names (`notebooklm-py` and its MCP-server ecosystem) to recognize and
   decline if they resurface under official-sounding branding.
2. **§4/§8 recommendation from the prior brief stands unchanged:** `lfnovo/open-notebook` remains
   the one real alternative-tool candidate, now with independent first-person deployment evidence
   (not just docs/GitHub-metadata) backing the same "queued, not worth displacing Gemini Notebook
   yet" call.
3. **The most useful find in this search wasn't NotebookLM-shaped at all** — the Encryptorium
   Claude-Code study-OS post, independently converging on a similarly-named "Examiner" role and a
   `tracker.md`-equivalent state file, plus a screenshot-capture-to-flashcard pipeline worth
   remembering for the open capture-trigger question.
4. **AnkiConnect-based card generation has a second independent practitioner confirming it works**
   as a real automation mechanism for the already-locked card-generation line.
