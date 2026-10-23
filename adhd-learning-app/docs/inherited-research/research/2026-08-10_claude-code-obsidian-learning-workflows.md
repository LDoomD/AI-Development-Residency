# Claude Code + Obsidian as a Personal Learning System — What Other People Actually Do

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-10
> **Scope:** people using Claude Code (the CLI agent) with an Obsidian vault for *personal
> learning* — studying, retention, retrieval practice, study-note management. Explicitly
> **not** software-engineering usage, and **not** generic "AI note-taking."
> **Method:** GitHub API (stars/forks/commit counts/issue bodies pulled directly, not from
> search summaries), primary READMEs, issue threads, first-person practitioner blogs, the
> official Obsidian skills repo, **Obsidian forum threads, and YouTube — 16 videos with view
> counts, like counts, publish dates and full descriptions scraped from the page JSON rather
> than taken from search summaries** (§7). **Already-decided ground deliberately skipped:**
> Anki `.apkg` generation and Gemini Notebook audio (see `specs/DECISIONS.md` §1, §8) —
> except where a *materially different* mechanism turned up, which it did (§7.3).

---

## The one-paragraph answer

**The Claude Code + Obsidian combination is enormous and almost none of it is about
learning.** The category is dominated by *agent-memory* and *capture-and-organize* systems —
making the AI remember your projects, not making you remember your material. Across the top
~25 repos by stars, exactly **two** are learning-specific, and both are weak: one is a
1,083-star skill pack that was **abandoned six days after launch (4 commits total)**, and the
other doesn't actually use Obsidian despite its reputation. There is **no documented case
anywhere** of someone running a Claude Code + Obsidian study loop with a real spaced-repetition
engine, a mastery gate, and a retention measurement. The patterns that *do* recur across many
independent people are all **vault-hygiene conventions**, not learning mechanisms.

> **The whitespace this repo is building into is real. But the vault-plumbing conventions
> other people converged on are worth stealing, and this repo is currently hand-rolling at
> least one thing (JSON Canvas) that Obsidian's own team ships as an official skill.**

**The social-media pass (§7) did not change that conclusion — it hardened it, and produced
the brief's best source.** YouTube holds ~640,000 views on this topic across sixteen videos;
**fifteen are the same "second brain" video**, and every large one is a funnel into a paid
Skool community, so the genre has no way to report failure. But following the one genuinely
learning-focused video (57k views — which **drops Obsidian entirely** and pairs Claude Code
with Anki) led to the **Memory Machines benchmark: Claude Sonnet 5 produces unusable
spaced-repetition prompts 42% of the time, GPT-5.2 36%** — and models are *worst* at detecting
the defect that quietly destroys retention. **That single finding is the most decision-relevant
thing in this brief, and it argues against automating card generation, not for it.**

---

## Source inventory and grades

Grades follow the repo convention: what *kind* of evidence is this, not whether I liked it.

### Tier A — primary artifacts with real, independently verifiable usage

| Source | Signal | Grade |
|---|---|---|
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | **44,691 ★ / 3,191 forks.** Official Obsidian agent skills, authored by Obsidian's CEO. Skills: `obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, `defuddle` | **High** — first-party, canonical |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | **14,683 ★**, pushed 2026-08-10 (active). Embeds Claude Code/Codex *inside* Obsidian | **High** — sustained active development |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | **10,700 ★ / 1,238 forks**, created 2026-04-07, still pushed 2026-08-01. 15 skills | **High** as an artifact; **Moderate** as evidence of *outcomes* |
| [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | **4,308 ★ / 503 forks**, active | High as artifact |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | **3,949 ★ / 494 forks**, active. 45 commands | High as artifact |
| [bevibing/tutor-skills](https://github.com/bevibing/tutor-skills) | **1,083 ★ / 93 forks** — but **4 commits, all between 2026-02-22 and 2026-02-28.** Dead since | **Moderate** — see §4 |
| [hluaguo/learn-faster-kit](https://github.com/hluaguo/learn-faster-kit) | **346 ★ / 37 forks**, created 2025-11-10, pushed 2026-08-04 (**genuinely maintained**) | Moderate |
| [derek-larson14/obsidian-claude-sidebar](https://github.com/derek-larson14/obsidian-claude-sidebar) (441 ★), [RAIT-09/obsidian-agent-client](https://github.com/RAIT-09/obsidian-agent-client) (2,347 ★) | Run agent CLIs inside Obsidian via ACP | High as artifacts |
| [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) | **3,291 ★**. Canvas/Excalidraw/Mermaid generation. Self-described **"public prototype… does not yet cover all input scales and edge cases"** | Moderate, author-caveated |

### Tier B — first-person practitioner accounts (one person each, but real usage)

| Source | Who | Grade |
|---|---|---|
| [Eleanor Konik — "Claude + Obsidian Got a Level Up"](https://www.eleanorkonik.com/p/claude-obsidian-got-a-level-up) | Long-running PKM writer, ~15M-word vault. Runs Claude Code via Obsidian's **Terminal plugin**; Telegram voice capture → vault | **Practitioner-only, but high-credibility** — names her own failures |
| [Theo Stowell — Parazettel, "TL;DR of Claude Code Inside Obsidian"](https://parazettel.com/articles/tldr-claude-code-in-obsidian/) | PKM-focused site, first-person | Practitioner-only |
| [Simon Späti — "Keep AI Out of Your (Obsidian) Vault"](https://www.ssp.sh/brain/using-obsidian-with-ai/) | The main dissenting voice. Cites **no formal research**, self-admitted | Practitioner-only — **but the most useful source here** |

### Tier C — the SEO cluster ⚠️

**This is the pattern this repo's other briefs keep catching, and it is severe here.**

`mindstudio.ai/blog` alone returned **five distinct URLs** on the identical topic
(`build-ai-second-brain-claude-code-obsidian`, `…-obsidian-2`,
`how-to-build-ai-second-brain-obsidian-claude-code`, `ai-second-brain-claude-code-obsidian-architecture`,
`self-evolving-claude-code-memory-obsidian-hooks`). MindStudio is an AI-product company;
this is content marketing, not experience. Alongside it: howtogeek, xda-developers, dev.to
(×3 different authors, near-identical structure), medium (×3), towardsai, buildmvpfast,
whytryai, agenticpm, codecraftsphere, noahvnct.

All of them make the same four claims in the same order: *vault is just markdown → Claude
Code reads the folder → wikilinks are trivial for it → it finds connections you missed.*
Several use the identical anecdote shape ("I threw 3 months of notes at it and it found a
pattern I'd ignored").

> **Grade: Low / aggregator. Treat the "consensus" that this stack is a second brain as
> one idea republished ~15 times, not fifteen people's results.** None of them report a
> retention outcome, a study schedule, or a follow-up after month one.

### Tier D — could not verify

- **Reddit**: `www.reddit.com` is not fetchable from this environment. Search-engine
  summaries claiming to represent r/ObsidianMD threads were returned **without any actual
  Reddit URLs** — the summarizer appears to have synthesized "Reddit-flavored" content from
  blog sources. I am not reporting any Reddit claim as evidence. *(Same failure shape as the
  fabricated citations logged in `2026-08-08_prior-art.md`.)*
- **Hacker News**: the one relevant thread,
  [Show HN: Skill for structured deep research with Claude Code and Obsidian](https://news.ycombinator.com/item?id=47246516),
  has **one comment**. There is no HN discussion to mine.
- **YouTube video transcripts**: player pages do not render through the fetch tool. Titles,
  channels, dates, view counts, like counts and **full descriptions** were recovered from the
  page JSON (§7); spoken content was not. Claims below rest on descriptions and metrics only.

### Tier E — social media ⚠️ (see §7 for the full pass)

**YouTube is where the actual audience is** — the sixteen videos measured total **~640,000
views**, roughly two orders of magnitude more reach than every GitHub repo and blog post in
Tiers A–C combined. It is also the **least trustworthy tier**, because the dominant format is
a lead magnet. Graded individually in §7.1. **X/Twitter and LinkedIn: Low throughout** —
engagement-optimized, largely unverifiable, and in at least one case demonstrably automated
(§7.5).

---

## 1. What the category actually is: agent memory, not human learning

Read the top repos' own descriptions and the theme is unmissable:

- obsidian-mind: *"gives AI coding agents **persistent memory**"*
- obsidian-second-brain: *"**Persistent memory for Claude Code** … Stop re-explaining your projects"*
- claude-code-memory-setup (923 ★): *"**71.5x fewer tokens per session**"*
- claude-obsidian: loop is *"retain the source, ground the claims, connect the knowledge, put it back to work"*

I checked `AgriciDaniel/claude-obsidian` — the 10,700-star flagship — directly for learning
functionality across all 15 skills. **There is none.** No quizzing, no recall, no review
scheduling, no retention metric. Same for obsidian-mind, obsidian-second-brain, and
kepano/obsidian-skills (confirmed: *"No mention exists of flashcards, spaced repetition, or
learning-focused functionality"*).

> **The stated goal of this category is that *the agent* never forgets. This repo's goal is
> that *Orlando* never forgets. Those are different products that happen to share a file
> format.**

**Grade — "Claude Code + Obsidian is widely used as a personal *learning* system":
Not supported.** It is widely used as an agent-memory and capture system.

---

## 2. Patterns that genuinely recur across independent people

These appear in the official Obsidian skills **and** multiple large independent repos **and**
first-person accounts. That triangulation is what makes them real rather than one blogger's
taste.

| Pattern | Where it independently appears | Worth stealing? |
|---|---|---|
| **`CLAUDE.md` at vault root describing the vault's own conventions** | kepano skills, claude-obsidian, obsidian-mind, obsidian-second-brain, Parazettel, Konik | Already have it (`specs/vault-convention.md`) — but see §6.1 |
| **`inbox/` staging separated from processed output** | claude-obsidian (`inbox/` → `wiki/`), obsidian-mind, most templates | **Already locked** — Capture inbox, DECISIONS §3 |
| **Immutable raw source copy (`.raw/`) + provenance ledger** | claude-obsidian's strongest idea; partially in obsidian-second-brain | **Yes — new. See §6.3** |
| **Maps of Content (MOC) as the index primitive** | claude-obsidian, tutor-skills (`00-Dashboard/`), the HN deep-research skill, most templates | Partially — this repo uses Canvas instead |
| **Read-only query mode separated from write mode** | claude-obsidian (`/wiki-query` is explicitly read-only) | **Yes — new. See §6.4** |
| **Explicit save only; never automatic capture** | claude-obsidian states this as a hard limitation-by-design; Späti and Stowell both insist on it independently | **Yes — new. See §6.5** |
| **A lint/hygiene command (dead links, orphans, metadata gaps)** | claude-obsidian `/wiki-lint`, Konik ran metadata cleanup over 15M words overnight | Moderate value |
| **A session-close skill that writes state back before exit** | Parazettel's `/close`, obsidian-second-brain, claude-obsidian | **Already have it** — `tracker.md` as sole durable state (DECISIONS §9) |
| **Agent running *inside* Obsidian rather than a separate terminal** | claudian (14.7k), obsidian-agent-client/ACP (2.3k), obsidian-claude-sidebar (441), Claude Code Skills plugin, Konik via Terminal plugin | **Yes — and it matters for ADHD. See §6.2** |

**Grade — these conventions are a real convergent pattern: Moderate–High.** Multiple
independent implementations, plus first-party endorsement for the file formats.
**Grade — any of them improves learning: Not covered.** Nobody measured anything.

---

## 3. Learning-specific tooling: the two real artifacts

### 3.1 `bevibing/tutor-skills` — the closest prior art that exists

Two skills: `/tutor-setup` (PDF/doc/codebase → structured Obsidian "StudyVault") and
`/tutor` (adaptive quizzing). Structure:

```
StudyVault/
├── 00-Dashboard/     (MOC, Quick Reference, Exam Traps)
├── 01-<Topic>/       (concept notes + practice questions)
└── ...
```

**Its one genuinely good idea — and it converges with this repo's Examiner:**

> **Mastery is tracked at the *concept* level, not the session level.** Wrong answers are
> recorded per-concept, rephrased in a new context on the next drill, and only marked
> resolved once the underlying idea is demonstrated. Proficiency badges 🟥🟨🟩🟦⬜ with
> attempt counts and dates.

**What it does NOT have:** any spaced-repetition algorithm, any Anki integration, any
scheduling. Confirmed by reading the repo directly. "Adaptive" means *within-session
difficulty selection*, not distributed practice.

**⚠️ The abandonment signal.** 1,083 stars, 93 forks — and the GitHub API shows **4 commits
total**, the last on 2026-02-28, six days after launch. It went viral and died. Five and a
half months later there are **five open issues and zero maintainer responses.**

**Grade — as a design reference: Moderate.** The concept-level mastery model is real and
independently arrived-at. **Grade — as evidence the workflow sustains: Low.** The author
stopped using it before anyone could find out.

### 3.2 `hluaguo/learn-faster-kit` — maintained, but misfiled

`/learn [topic]`, `/review`, `/progress`. Created 2025-11-10, **still pushed 2026-08-04** —
the only learning-focused project here with real longevity.

Three problems on inspection:
1. **It does not use Obsidian.** Plain markdown + JSON in a `.learning/` directory. It is
   repeatedly cited in the Claude-Code-plus-Obsidian conversation anyway.
2. **The spaced repetition is undocumented.** A `review_scheduler.py` exists; no algorithm
   is specified. Not FSRS, not SM-2, not stated. This is exactly the "adaptivity" claim shape
   `2026-08-08_prior-art.md` found in ~25 commercial products and verified in two.
3. **⚠️ "2-3x retention vs. passive reading" with zero citation.** Straight into the bucket
   `2026-08-09_10x-learning-claims-audit.md` exists to catch.

**Grade: Low as evidence, Moderate as an existence proof** that a CLI-agent study loop can be
maintained for nine months.

### 3.3 Flashcard generation — the plugin ecosystem adds nothing; AnkiConnect does

Auto Anki, AI-AnkiSync, obsidian-auto-anki, ccmdi/obsidianki (**5 ★**), Flashcard Generator,
plus the Obsidian Spaced Repetition plugin family (st3v3nmw's, updated 2026-02-21, supports
**both FSRS and SM-2**; open-spaced-repetition's `-recall` fork, maintainer publicly asking
for help). These are all **pre-existing plugin-ecosystem tools that predate the Claude Code
era and were not built for it.** Nobody has documented pairing them *with* a Claude Code
agent loop.

**This confirms rather than challenges `DECISIONS.md` §1.** Anki + FSRS remains the only
serious engine; the in-Obsidian alternatives are thinner and less maintained.

**⚠️ One exception, found in the later social-media pass: AnkiConnect** — a live local HTTP
API into the Anki collection, which several agent workflows use instead of `.apkg` files.
That *is* a materially different mechanism and it gets a real comparison in **§7.3**. The
conclusion is still to keep `.apkg`, but for a better reason than "already decided."

---

## 4. Documented failure modes

The most valuable output of this search. These are things people actually hit.

| # | Failure | Source & strength |
|---|---|---|
| 1 | **⚠️ Answer leakage from format examples.** The tutor skill instructed users to *"Reply in this format: 1B 2D 3A 4C"* — with a 4-question quiz, this **leaks the answer key** when it happens to match. Reporter: *"This did happen several times."* | [tutor-skills #4](https://github.com/bevibing/tutor-skills/issues/4) — **specific, reproducible, unfixed.** Highest-value finding in this brief |
| 2 | **Vault corruption under long context.** Claude "loses focus after the first 20% of its context" and overwrites notes — corrupting the source of truth | Reported in the failure-mode discussion; single-source. **Low–Moderate**, but the mechanism is plausible and cheap to defend against |
| 3 | **Deduplication decay.** Same topic across multiple sessions → near-identical entries. Requires a mandatory search-before-save step | Multiple repos build explicit defenses (claude-obsidian `/wiki-lint`, obsidian-second-brain hybrid search). **Convergent → Moderate** |
| 4 | **Maintenance burden exceeds capacity within ~6 months** → people stop linking and abandon the system | Single-source, but **corroborated structurally by tutor-skills itself dying in 6 days** |
| 5 | **Interaction latency kills throughput.** A user who ran the tutor *"more than 3 weeks… more than 10 times everyday"* asked for Python scripts because *"the interaction is cool but slow"* | [tutor-skills #5](https://github.com/bevibing/tutor-skills/issues/5) — **the single best piece of real sustained-usage evidence found.** One person, three weeks, daily, exam-driven |
| 6 | **AI slop poisons retrieval.** Späti: generated summaries become noise that buries personally meaningful notes; *"if you only have your own writing, it's all valuable."* Quoting kepano: **"A summary of a PDF is noise. An insight I had from reading the PDF is signal."** | Practitioner-only, but the reasoning is sound and kepano is first-party |
| 7 | **Cache staleness on large edits** — Konik reports needing restarts after large file changes | Practitioner-only |
| 8 | **⚠️ Vendor spam in the ecosystem.** [tutor-skills #6](https://github.com/bevibing/tutor-skills/issues/6) is a marketing "issue" from `socialistic.ai` with UTM campaign tags (`utm_campaign=20260613-summer-exam-prep-study-tools`), flattering the maintainer's design to route their users to a hosted product | Directly observed. Relevant to how "community interest" gets manufactured |

**Nobody documented:** an ADHD- or dyslexia-specific version of this stack. The ADHD +
Claude Code writing that exists ([chudi.dev](https://chudi.dev/blog/claude-code-skills-adhd-developers),
[dev.to/kairi_outputs](https://dev.to/kairi_outputs/claude-code-as-executive-function-my-adhd-brain-setup-1412),
[iwoszapar](https://www.iwoszapar.com/p/claude-code-adhd-executive-function)) is entirely about
**executive function for software work** — task triage, session resume, time-blindness — with
no Obsidian and no learning content. Consistent with `2026-08-08_prior-art.md`: the
neurodivergent-adult learning category stays empty.

---

## 5. Is there a meaningfully better approach than what this repo built?

**Honest answer: no on architecture, yes on plumbing.**

### Where this repo is clearly ahead

| Dimension | Field | This repo |
|---|---|---|
| **Distributed practice** | **Absent everywhere.** tutor-skills: none. learn-faster-kit: unspecified algorithm. The whole agent-memory category: none | Anki + FSRS, locked (§1) |
| **Evidence base** | Zero citations across every source found. learn-faster-kit asserts "2-3x" uncited | Dunlosky 2013, Brunmair & Richter 2019, Cromley & Chen 2025, Bastani PNAS 2025 |
| **Guarding against the tutor answering** | **Nobody addresses it.** tutor-skills fell into the inverse failure — leaking answers in its own instructions | Tool boundary (§8): *"Gemini helps you learn it. Claude decides whether you know it."* Evidence-before-verdict grading |
| **Adaptivity floor** | Absent. tutor-skills "adapts difficulty" with no floor — the exact CSAL AutoTutor failure shape | The floor, Paas 7–9 → reduce scope (§3) |
| **Material-type sensitivity** | Absent. One universal quiz loop for everything | Subject-type router (§2, built last) |
| **Rejection discipline** | tutor-skills ships proficiency **badges** (🟥🟨🟩🟦⬜) — gamified progress signalling | Streaks/XP/badges explicitly rejected (§4) |

**Nothing found challenges the three-layer architecture.** No competing design in this space
even has two of the three layers.

### Where the field is ahead — six things worth taking

#### 6.1 ⭐ Adopt `kepano/obsidian-skills` `json-canvas` rather than hand-rolling it

**The most actionable finding.** Obsidian's own team ships an official `json-canvas` agent
skill — nodes, edges, groups, connections — at **44,691 stars**, alongside `obsidian-markdown`
and `obsidian-cli`. `DECISIONS.md` §10 puts the Canvas layer at build step 5 and
`specs/vault-convention.md` commits to JSON Canvas.

Writing valid `.canvas` by hand is exactly the fiddly, spec-conformance work a first-party
skill removes. And the one third-party alternative (axtonliu, 3,291 ★) self-describes as *"a
public prototype [that] does not yet cover all input scales and edge cases"* — including
**node-overlap prevention**, which is precisely the part that's annoying.

> **Recommendation: before building step 5, install `kepano/obsidian-skills` and treat
> `json-canvas` as the writer. This does not change any locked decision — it's an
> implementation shortcut on one already locked.**

**Also newly relevant: `obsidian-bases`.** Bases is Obsidian's native structured-query format
(views, filters, formulas). This repo has never evaluated it. `tracker.md` stays the sole
durable state (§9) — **do not move state into Bases** — but a Base could give a *read-only
view* over tracker state without becoming a second source of truth. Worth a look, not a
decision.

#### 6.2 Run the agent inside Obsidian — an ADHD argument, not a convenience one

Four independent, well-starred projects exist purely to eliminate the terminal↔Obsidian
switch: claudian (14.7k), obsidian-agent-client/ACP (2.3k), obsidian-claude-sidebar (441),
the Claude Code Skills community plugin. Konik does it via the plain Terminal plugin.

The current design implies VS Code + terminal + Obsidian + Anki. That is **four context
switches per session**, and switching cost is a named ADHD support target
(`adhd-learning-system-design.md`). The field converging this hard on collapsing that switch
is a signal — and the cheapest version (Obsidian's Terminal plugin, per Konik) needs no new
dependency.

**Caveat, honestly:** the Examiner is a mastery gate. A sidebar that makes the agent
*always present* is in tension with the tool boundary in §8 — the whole point is that Claude
is not a companion you consult mid-thought. **This is a real tradeoff, not a free win.**

#### 6.3 The `.raw/` immutable-source + provenance ledger pattern — fixes a known open seam

`claude-obsidian`'s best idea: raw sources are copied in **content-addressed and immutable**;
processed notes carry a source/claim ledger; high-risk claims require two independent sources.

`DECISIONS.md` §12.3 logs an unresolved problem: **"The Gemini → vault export seam — manual
today, no design yet."** An `.raw/` convention is a partial answer. Material read in Gemini
Notebook lands as an immutable copy in the vault first; anything authored from it carries a
pointer back. It doesn't automate the export, but it stops material accumulating invisibly
outside the system — the exact risk §8 flags.

It also directly mitigates failure mode #2 (an agent that loses focus can't corrupt what it
can't write to) and #6 (generated content is structurally separable from sources and from
your own writing).

#### 6.4 Read-only query mode as a separate command

`/wiki-query` is *"read-only, evidence-based."* Cheap structural defense against #2, and it
rhymes with the mechanism this repo already uses for the Examiner: **make the constraint
structural, not a "be careful" instruction in a prompt** (§9).

#### 6.5 Explicit-save-only, and the anti-slop discipline

Späti, Stowell, and claude-obsidian arrive at the same rule from three directions: **the
agent never writes to the vault unprompted, and generated content is marked as such.** Späti
goes further — a separate vault for AI experiments — which is probably too strict here, since
the Examiner's output (grades, gaps) is legitimately durable state.

But the underlying principle is one this repo's `2026-08-09_book-synthesis-audit.md` would
endorse: **a summary is noise; the thing you produced under retrieval is signal.** Retrieval
practice only counts if *you* generated the answer. A vault filling with agent-written
summaries doesn't just waste space — it degrades the retrieval cue set. That's a learning
argument, not a tidiness one.

#### 6.6 The answer-leakage failure — fix the Examiner before it ships

`tutor-skills` #4 is a gift: a real, reproduced, unfixed bug in the exact component this
repo is building next (§10 build order, step 3 — *"Examiner first"*).

> A quiz prompt that says *"Reply in this format: 1B 2D 3A 4C"* leaks the key whenever the
> example collides with the real answers. On a 4-item quiz that's frequent.

**Concrete rule for the Examiner spec:** format instructions must be *generic* ("reply with
question number and option letter") and the skill must **explicitly forbid worked format
examples containing option letters.** This belongs on the **never-list** (Queued §11 item 5)
alongside streaks and timers — it's the same class of guard.

---

## 7. Social media pass — YouTube, forums, X/LinkedIn

Added after the first draft under-covered video. **This turned out to be where the strongest
single piece of evidence in the entire brief was hiding** (§7.4) — and also where the
promotional distortion is worst.

### 7.1 The sixteen videos, measured

View/like counts and dates scraped from page JSON on 2026-08-10.

| Views | Date | Channel | Title | About learning? |
|---:|---|---|---|---|
| 217,437 | 2026-04-10 | KJ Rainey | How To Build The ULTIMATE AI Second Brain | No |
| 123,836 | 2026-04-16 | Productive Dude | Claude Code + Obsidian is INSANE! | No |
| 93,765 | 2026-03-15 | Mark Kashef | Claude Code Turned Obsidian Into My Dream Second Brain | No |
| 75,022 | 2026-04-06 | Eric Tech | The Second Brain Setup That Actually Works | No |
| **57,398** | **2026-06-08** | **Automata Learning Lab** | **How I Use Claude Code + Anki to Memorize Anything** | **YES** |
| 18,187 | 2026-03-04 | Noah Vincent | Build Your AI Second Brain (Free Setup) | No |
| 13,561 | 2026-06-24 | Ritesh Verma | AI Second Brain OS | No |
| 12,371 | 2026-07-02 | Eric Michaud | Obsidian AI Second Brain that ACTUALLY Works! | No |
| 9,059 | 2026-05-14 | Julian Goldie SEO | Claude Obsidian is INSANE! 🤯 | No |
| 6,734 | 2026-04-28 | Nuno Tavares | Build a Second Brain That Actually Learns | No |
| 4,279 | 2026-06-20 | Luke J Byrne | Build a Second Brain | No |
| 3,761 | 2026-04-23 | NextWork | Karpathy method pt 2 | No |
| 3,210 | 2026-05-06 | Duke Pan | Build Your Second Brain With AI | No |
| 561 | 2026-05-08 | Incubyte | Second Brain (conference talk) | No |
| 343 | 2026-04-28 | Frank | AI-Powered Spaced Repetition | Partly, no Claude Code |
| 22 | 2026-07-19 | Claude Daily | Claude AI for Students | No (AI-spun) |

**Fifteen of sixteen are the same video.** Same title grammar ("second brain," "ACTUALLY
works," "INSANE"), same March–July 2026 window, same structure. This is the video-format twin
of the Tier C SEO cluster — and it confirms that cluster is **a genuine content-marketing
wave, not fifteen independent practitioners**.

> **Note the title of the 6,734-view video: "Build a Second Brain That *Actually Learns*."
> The subject of the verb "learns" is the vault, not the person.** That is the category in
> one phrase.

### 7.2 ⚠️ The funnel pattern — the single most important grading fact here

I pulled the full descriptions. **Every one of the four largest videos routes to a paid
product**, and the pattern is uniform:

| Channel | Views | Monetization in the description |
|---|---:|---|
| KJ Rainey | 217k | `skool.com/useful-ai` community + "my free AI courses" + `seven80labs.com` ("work with me") + affiliate tool links |
| Productive Dude | 124k | `skool.com/ai-foundations` — *"The full blueprint with all skill files and ingestion patterns is available inside AI Foundations"* + `aifoundations.io/apply` ("done for you") |
| Mark Kashef | 94k | `skool.com/earlyaidopters` masterclass + Gumroad kit + `promptadvisers.com` + Calendly consultation |
| Eric Tech | 75k | `skool.com/erictech` + `surething.io` **affiliate link with UTM tracking** |

**Productive Dude's is the tell: the actual system is deliberately withheld from the video
and sold.** The video is an advertisement for the artifact, so it is structurally incapable
of reporting that the artifact failed.

> **Grade — YouTube "Claude Code + Obsidian" content as evidence of working practice: Low.**
> Not because creators are lying, but because **the genre has no failure branch.** A video
> published 1–7 days after a setup, monetized by a community selling that setup, cannot tell
> you what happened in month three. **Zero of the sixteen report a follow-up, a retention
> outcome, or an abandonment.**

**One honest moment, worth recording.** Mark Kashef (94k views) opens by naming the exact
failure mode §4 catalogues, in the first person:

> *"I tried Obsidian five times. Every time: set it up, used it for a week, forgot it
> existed. The sixth attempt worked because I added Claude Code."*

The first sentence is well-evidenced by everything else in this brief. The second is a claim
made in a video advertising a Skool community, five months ago, with no follow-up.
**Grade: the confession is credible; the resolution is unverified.** He does ship a real
public repo ([earlyaidopters/second-brain](https://github.com/earlyaidopters/second-brain),
183 ★ / 57 forks) — but it is **dead after 8 days** (created 2026-03-09, last push
2026-03-17), the same viral-then-abandoned shape as tutor-skills (§3.1).

### 7.3 ⭐ The one on-target video — and a genuinely new mechanism

**[Automata Learning Lab — "How I Use Claude Code + Anki to Memorize Anything (My Agentic
Learning System)"](https://www.youtube.com/watch?v=RocA3wA3QjU)** — 57,398 views, 2,490 likes,
2026-06-08. Creator: Lucas Soares, who also
[wrote it up on Medium](https://lucas-soares.medium.com/i-think-i-found-the-perfect-formula-for-learning-anki-claude-code-db47f0a72117)
and sells an [Anki + AI course](https://www.automatalearninglab.com/courses/Anki-AI-course)
(so: funnel-adjacent, but a real practitioner with a written artifact).

**This is the only creator in the entire corpus who paired a CLI agent with a real SRS
engine.** Notably, he **skipped Obsidian entirely** — the vault plays no part. The chapter
list describes: bulk card generation from PDFs, quizzing via vibe-coded HTML apps, extracting
timestamped highlights from YouTube, and **"Automating Card Creation Directly Into Anki's
Database."**

**⚠️ The new mechanism: AnkiConnect.** Multiple independent sources
([actuallymaybe.com](https://actuallymaybe.com/blog/agentic-ai-anki-flashcard-creation/),
[MCP Market's Anki skill](https://mcpmarket.com/tools/skills/anki-flashcard-manager),
[Clanki](https://mcpmarket.com/server/clanki)) converge on it: an Anki add-on exposing a
**local HTTP API** so an agent can create decks, add cards, and **check for duplicates before
inserting** against the live collection.

**This is materially different from `DECISIONS.md` §1's `.apkg` path and deserves an honest
comparison rather than a reflexive "already decided":**

| | `.apkg` generation (locked) | AnkiConnect (new) |
|---|---|---|
| Coupling | File handoff, offline, Anki closed | Live API, Anki must be running |
| Duplicate detection | None — you re-import and dedupe by hand | **Agent queries the collection first** |
| Blast radius on a bad run | A bad import file you can discard | **Writes straight into the live collection** |
| Human review gate | Natural — the file is inspectable before import | **Easy to skip; that's the selling point** |
| FSRS scheduling | Untouched | Untouched via the API; **at risk if writing the DB directly** |

**Assessment: adopt the duplicate-check idea, not the write path.** Duplicate accumulation is
independently reported as a top failure mode (§4 #3). But AnkiConnect's advantage is
*removing the friction of a human looking at the cards*, and §7.4 is about to explain why
that friction is the most valuable part of the whole pipeline. **`.apkg` stays. The
inspectable-file step is a feature, not overhead.** And the video's "directly into Anki's
database" framing — bypassing even the API — is a collection-corruption risk this repo should
not take with the one component holding the FSRS scheduling state.

### 7.4 ⭐⭐ The strongest evidence in this brief, reached via a social-media trail

Following the AI-flashcard-quality thread led to a real benchmark — **[Memory Machines,
Ozzie Kirkby & Andy Matuschak (2026)](https://memory-machines.com/report)**. Matuschak is a
serious name in spaced repetition; this is not a blog claim.

**Method:** ~1,500 labeled prompts across 93 sources; **20 models**; models generate
spaced-repetition prompts from reader highlights; four-tier usability taxonomy (T3 ready ·
T2 minor polish · T1 needs structural refactoring · T0 off-target); human–model agreement
**κ = 0.61**.

**Unusable rate (T0 + T1):**

| Model | Unusable |
|---|---:|
| GPT-5.2 | **36%** |
| **Claude Sonnet 5** | **42%** |
| OpenAI o3 | 46% |
| Gemini 2.5 Pro | 48% |
| Claude Opus 4.5 | 50% |
| GPT-4o | 71% |

> **Even the best frontier model produces an unusable spaced-repetition prompt more than a
> third of the time. The model this repo's stack runs on scores 42%.**

The failure analysis is the part that matters most:

- Models are **good** at spotting off-target prompts (T0) and **bad** at distinguishing T1
  (structurally broken) from T2 (fine) — *"models are best at judging criteria that are
  apparent without review… weakest at judging"* what only shows up after repeated use.
- Worst-detected failure: **"solicits multiple valid responses" (F1 0.32–0.50)** — the exact
  defect that silently wrecks long-run retention.
- Framing: a memory prompt *"must cue the same retrieval over time: today, then again in
  three months, then again in a year."* A card can look perfect and still fail in month four.

**Grade: High.** Real benchmark, real scale, published methodology, named authors,
reported inter-rater agreement. **This is the highest-grade source in the brief and it
argues against automation, not for it.**

**Corroborated independently** by
[Eva Keiffenheim](https://evakeiffenheim.substack.com/p/when-ai-flashcards-pollute-your-anki)
(*"It took me less than a minute to mess up my Anki deck"*; cites Pan et al. 2022 on
user-generated vs. premade cards) and by
[**Li et al. (2026), *SmartFlash*, arXiv:2602.14431**](https://arxiv.org/abs/2602.14431) —
formative study, **n = 6** students, think-aloud + interview. Verbatim from the abstract:
students *"value automation for addressing the overwhelming preparation burden, yet require
transparent, editable AI outputs to maintain **cognitive ownership, which is essential for
self-regulation**"*; they conceptualized AI as *"a collaborative partner demanding verifiable
reasoning rather than an autonomous agent."* **Grade: Low–Moderate** — n=6, formative, no
learning outcomes — **but it points the same direction as the benchmark.**

### 7.5 X / LinkedIn — Low, and partly automated

- A widely-shared [X post](https://x.com/cyrilXBT/status/2086388265318310264) about *"a
  27-year-old [who] connected Claude Code to more than 4,000 Obsidian notes and woke up to…
  an AI teammate"* — anonymous subject, no artifact, no outcome. **Pure engagement bait.**
- [Prajwal Tomar](https://x.com/PrajwalTomar_/status/2076668274306318468) on kepano's skills
  — *"41K stars"*; the API says **44,691** today. Directionally right, illustrative of the
  precision available on this channel.
- LinkedIn: *"Andrej Karpathy just 10x'd everyone's Claude…"* — **the exact "10x" claim shape
  `2026-08-09_10x-learning-claims-audit.md` exists to reject.**
- ⚠️ **Some of this "organic" social content is machine-generated.**
  [yamz8/x-thread-skill](https://github.com/yamz8/x-thread-skill) is a Claude Code skill that
  turns a project into *"a viral X/Twitter thread that actually sounds human"* — explicitly
  coaching lowercase tone and no em-dashes to defeat AI-detection heuristics. The 22-view
  "Claude Daily" video is the same phenomenon on YouTube.

> **Treat volume of social agreement on this topic as evidence of nothing.** A measurable
> share of it is generated by tooling built to manufacture exactly that appearance.

**One genuine attribution does survive:** the "raw folder + wiki folder" structure that
recurs across the big repos (§2) traces to **Andrej Karpathy's LLM Wiki pattern**, cited by
name in claude-obsidian, [qhuang20/obsidian-skills](https://github.com/qhuang20/obsidian-skills),
NextWork, and swarmvault. Convergence here is **one idea with a famous origin**, not
independent discovery — which *lowers* its evidentiary weight while explaining the uniformity.

### 7.6 Obsidian forum — small but real

Ten-plus threads on embedding agents in the vault: [Agent Client](https://forum.obsidian.md/t/new-plugin-agent-client-bring-claude-code-codex-gemini-cli-inside-obsidian/108448),
[Cortex](https://forum.obsidian.md/t/plugin-cortex-an-ai-obsidian-vault-agent-powered-by-claude-code/112430),
[Blackglass](https://forum.obsidian.md/t/plugin-blackglass-real-embedded-claude-code-terminal-with-built-in-vault-mcp-server/114734),
[Claude Code from the Sidebar](https://forum.obsidian.md/t/claude-code-from-the-sidebar/109634).
Reply counts are low (single digits) — these are announcement posts, not discussions.
**Independently corroborates §6.2**: the field really is converging on collapsing the
terminal↔vault switch. Not one thread is about studying.

**One concretely useful thread:**
[*"Open-source agent skill for Obsidian CLI — prevents 13 silent failures"*](https://forum.obsidian.md/t/open-source-agent-skill-for-obsidian-cli-prevents-13-silent-failures/111169)
— **13 silent failures across 57 test scenarios (22.8%)** where the Obsidian CLI returns
plausible-but-wrong results to an agent: `tasks todo` returns 0 results (needs `tasks all
todo`), `tags counts` reports "No tags found" (needs `tags all counts`), `properties
format=json` returns YAML, `create` pops the GUI without a `silent` flag. **Grade: Moderate**
— a second commenter (`lilsizzle`) independently re-tested on v1.12.1 against an 18,876-file
vault and reported the failures now surface as explicit errors. **Directly relevant to §6.1:
if this repo drives the Obsidian CLI, silent wrong answers are a real class of bug, and the
version matters.**

---

## Cross-cutting grades

| Claim | Grade |
|---|---|
| Claude Code + Obsidian is a large, active, real ecosystem | **High** — 44.7k / 14.7k / 10.7k ★, sustained commits |
| That ecosystem is about agent memory and capture, not human learning | **High** — verified by reading the top repos directly |
| A convergent set of vault conventions exists (inbox, MOC, CLAUDE.md, session-close, lint) | **Moderate–High** — multiple independent implementations |
| Any of those conventions improves learning or retention | **Not covered** — nobody measured anything |
| Concept-level (not session-level) mastery tracking is an independently-arrived-at design | **Moderate** — one implementation, but it converges with this repo's Examiner |
| Nobody pairs a Claude Code study loop with a real SRS engine | **High** — searched directly; the gap is total |
| The "second brain" consensus is a genuine multi-person finding | **Rejected** — ~15 near-identical posts (≥5 from one content-marketing domain) **plus 15 near-identical videos**; the shared structure traces to one Karpathy post |
| **LLM-generated spaced-repetition cards are frequently unusable (36% GPT-5.2, 42% Claude Sonnet 5)** | **High** — Kirkby & Matuschak, 20 models, ~1,500 labeled prompts, κ=0.61 |
| Models are worst at detecting the failure that matters most ("solicits multiple valid responses", F1 0.32–0.50) | **High** — same benchmark |
| Learners need editable, transparent AI output to retain cognitive ownership | **Low–Moderate** — SmartFlash, n=6, formative, no learning outcomes |
| YouTube "Claude Code + Obsidian" content is evidence of sustained working practice | **Rejected** — ~640k views across 16 videos; every large one is a funnel to a paid community; zero follow-ups |
| AnkiConnect is a viable live-API alternative to `.apkg` | **Moderate** — several independent implementations; **but see §7.3, the friction it removes is the friction §7.4 says you need** |
| The Obsidian CLI can return silently wrong results to an agent | **Moderate** — 13/57 scenarios, one independent re-test, version-dependent |
| Answer-leakage via format examples is a real tutor-agent failure | **Moderate** — one detailed reproduced report, unfixed |
| Long-running agent sessions can corrupt a vault | **Low–Moderate** — single-source, plausible mechanism |
| Anyone has run this stack for personal learning >3 weeks and reported results | **Not covered** — the longest documented usage is one GitHub issue |
| An ADHD/dyslexia-specific version of this stack exists | **Not covered** — the category is empty, consistent with `2026-08-08_prior-art.md` |

---

## What this means for THIS build

1. **Nothing here justifies changing the architecture.** The three-layer design
   (`DECISIONS.md` §2) has no competitor in this space with even two of its three layers. Every
   learning-adjacent project found is a single within-session quiz loop with no distributed
   practice, no evidence base, and no floor. **Keep the build order in §10 as-is.**

2. **Install `kepano/obsidian-skills` before build step 5.** Use the official `json-canvas`
   skill as the Canvas writer rather than hand-rolling `.canvas` emission. Implementation
   detail, not a decision change — but it removes the fiddliest part of the layer most likely
   to need iteration.

3. **Add the answer-leakage guard to the Examiner spec now**, while it is still being
   designed (§10 step 3). Generic reply-format instructions only; **no worked examples
   containing option letters.** File it on the never-list (Queued §11 item 5). This is the
   single most concrete transferable finding in the brief.

4. **Adopt `.raw/` immutable sources + a provenance pointer as part of the vault
   convention.** It's a partial, cheap answer to the Gemini→vault seam logged as open in
   §12.3, and it hardens against the two most-reported failure modes at once.

5. **Adopt explicit-save-only and mark generated content.** Not tidiness — a retrieval
   argument. Agent-written summaries degrade the cue set that retrieval practice depends on
   (§3, universal layer). This should be written into `specs/vault-convention.md`.

6. **Treat "run the agent inside Obsidian" as an open question, not an adoption.** Four
   independent projects say the context switch is worth killing, and switching cost is a
   named ADHD target. But an always-present sidebar cuts against the tool boundary in §8.
   **Log it in §11 Queued; don't act yet.** If tested, test the zero-dependency version
   (Obsidian's Terminal plugin) first.

7. **Design for the latency ceiling early.** The one person with three weeks of daily usage
   quit over speed, not quality — running ~10 questions per session and asking for scripts.
   `DECISIONS.md` §10 step 4 already puts `.apkg` generation right after the Examiner, which
   is the correct instinct: **the high-volume drilling belongs in Anki, and the Examiner
   should stay low-volume and gate-shaped.** This brief is evidence for that split, not
   against it.

8. **The abandonment pattern is the real warning, and it is this repo's actual risk.**
   tutor-skills: 1,083 stars, dead in six days. The maintenance-burden reports converge on
   ~6 months. This system's defense is already correct in principle — `tracker.md` as the
   sole durable state, capture with no structure required, a floor that reduces scope instead
   of pressing on. **But it is untested.** The honest metric from §6 — repetitions-to-criterion
   and 30-day retention against your own baseline — is worth nothing if the system is
   abandoned in week three. **Adherence is the binding constraint here, not pedagogy**, and
   nobody in this corpus has solved it either.

9. **Do not let the SEO/video cluster set expectations.** Fifteen posts and fifteen videos
   (~640k views) promise a second brain that surfaces connections you missed. Not one reports
   what happened in month two, and the largest are advertisements for paid communities. This
   repo's standing caveat in §1 — *"no controlled study shows any notes/PKM tool improves
   learning outcomes… any evidence this system has will come from its own design"* — applies
   to everything in this brief without exception.

10. **⭐ Promote Queued item 6 (`DECISIONS.md` §11) from "prototype with mandatory human
    review" to a hard, non-negotiable mechanism (§3).** This is the biggest change the social
    pass produced, and the evidence is the strongest in the brief:
    **Claude Sonnet 5 generates unusable spaced-repetition prompts 42% of the time**
    (Kirkby & Matuschak, §7.4). Human review of generated cards is not a cautious first-pass
    policy to relax once the prompt improves — **at a ~2-in-5 defect rate it is load-bearing
    forever.** Two specifics worth carrying into the card-generation spec:
    - The dominant undetectable defect is **"solicits multiple valid responses."** A card that
      admits two right answers trains nothing and fails silently months later. Review should
      target this explicitly, because the model cannot (F1 0.32–0.50).
    - Card defects are **latent**: T1 cards look like T2 cards on the day they are written.
      This is an argument for reviewing cards *at first review*, when the defect surfaces —
      not only at generation.

11. **Reject AnkiConnect as the write path; steal only its duplicate check (§7.3).** It is the
    one genuinely new mechanism the social pass surfaced against `DECISIONS.md` §1, so it got
    a real comparison rather than a dismissal. It loses on the merits: its selling point is
    removing the human-inspection step, and §7.4 establishes that step as the highest-value
    part of the pipeline. **`.apkg` stays locked** — an inspectable file before import is now
    better-justified than when it was chosen. Do borrow *query-before-insert* to fight the
    duplicate decay in §4 #3. And **do not write to Anki's database directly**, as the
    highest-reach learning video demonstrates; that is the one store holding FSRS state.

12. **If the build drives the Obsidian CLI (§6.1), pin and test the version.** 13 of 57
    scenarios returned silently wrong results to an agent (§7.6) — zero results rather than
    an error. An agent that believes "no tasks found" will make confident wrong decisions, and
    a mastery gate fed bad vault state is worse than no gate.
