# Research Brief: Context Engineering for LLM Agents — Current Best Practices

**Date:** 2026-08-10
**Prepared for:** ADHD-Learning-System (Claude Code–based agentic learning system: skills, subagents, MCP tools)
**Scope:** What goes into an agent's context window, how it is curated/structured/compressed/retrieved, and how it is managed across long-running multi-turn sessions. Explicitly *not* a prompt-wording guide.
**Method:** Multi-source pass prioritizing primary vendor documentation (Anthropic engineering blog, Claude Platform docs, Claude Code docs, OpenAI API docs, LangChain) over practitioner writeups, and practitioner writeups over SEO content. Where a number is cited, the model and benchmark it came from are named, because threshold numbers in this field are routinely over-generalized.

---

## Evidence Grading Key

Used throughout, matching this repo's convention:

- **[High — Official]** Primary vendor documentation or vendor engineering blog with implementation detail (Anthropic, OpenAI, Google, LangChain).
- **[High — Measured]** Peer-reviewed or preprint research with a stated method and numbers, or a vendor-published benchmark with methodology.
- **[Moderate — Practitioner consensus]** The same claim appears independently across multiple credible practitioner sources building real systems.
- **[Low — Single source]** One blog/writeup, plausible but unreplicated.
- **[Unverified / Hype]** Asserted without method, numbers, or replication; often SEO content or vendor marketing.

---

## Executive Summary

**1. The term is real, the framing is mostly accurate, and one part of the popular narrative is hype.** Anthropic defines context engineering as "curating and maintaining the optimal set of tokens during LLM inference" and positions it explicitly as *the natural progression of* prompt engineering — a superset, not a replacement. The genuine driver is that in an agentic loop nobody authors the context; it *accumulates* from tool results, sub-agent returns, retrieved files and the agent's own reasoning. "Prompt engineering is dead" is the content-mill version and is contradicted by the vendors themselves.

**2. The empirical foundation is solid, unlike most of what this field publishes.** Three independent, measured effects underwrite everything else: *context rot* (Chroma, 18 frontier models — all degrade as input grows, non-uniformly), *lost-in-the-middle* (Liu et al., U-shaped recall with a 20–30 point mid-context trough), and *context confusion* from tool-count bloat (a model failing with 46 tools and succeeding with 19). Drew Breunig's four failure modes — poisoning, distraction, confusion, clash — each carry a named study. This is not a vibes discipline at its core. It *is* a vibes discipline at its periphery, where fixed token budgets, optimal chunk sizes and universal thresholds circulate without method.

**3. LangChain's Write / Select / Compress / Isolate is the shared vocabulary, and it's framework-agnostic.** Everything in this brief maps onto those four operations regardless of whether you're using LangGraph, the Claude Agent SDK, or a raw API loop.

**4. The 2026 shift that matters most: retrieval moved from pre-computed to just-in-time, and instruction moved from explicit to minimal.** Anthropic now recommends keeping *pointers* (file paths, queries, links) in context and loading payloads at the moment of use — with Claude Code itself as the reference implementation (`CLAUDE.md` loaded up front, `glob`/`grep` for everything else). Separately, Anthropic removed **over 80% of Claude Code's system prompt** for Claude 5–generation models "with no measurable loss" on their coding evals, and documented two concrete harms of over-instruction: over-verification and delegation inflation. **This is the most quotable and most over-generalized finding in the field** — it is scoped to frontier models on coding tasks, and Anthropic's own skills documentation says the same instruction that over-explains for Opus may be necessary for Haiku.

**5. Compaction has become default infrastructure at both major vendors, and it is lossy in a specific, predictable way.** Anthropic ships auto-compaction plus tool-result clearing; OpenAI ships server-side compaction in the Responses API with a `compact_threshold`, and Codex depends on it. Both frame it as a standing primitive rather than an emergency measure. The known loss is *abandoned explorations* — which means a compacted agent will cheerfully re-attempt a dead end it already ruled out. The mitigation is to Write dead ends to a file before compacting, not to trust the summary.

**6. Sub-agent isolation is the highest-leverage single technique for this project, and Anthropic quantifies it.** In Anthropic's own worked session, a subagent read 6,100 tokens of files and returned 420 tokens. At scale the ratio is "tens of thousands explored → 1,000–2,000 returned." The cost is real: multi-agent setups burn up to ~15× the tokens of chat. The 2026 consensus shape — converged on independently by Anthropic, Cognition, OpenAI, Microsoft and LangChain — is **one orchestrator owning the conversation, spawning ephemeral isolated subagents that return compressed summaries**, with **writes single-threaded and reads parallel**.

**7. For a Claude Code project specifically, the operational levers are concrete and mostly under-used:** keep `CLAUDE.md` under 200 lines (official), keep `SKILL.md` bodies under 500 lines with reference files exactly one level deep (official — nested references cause silent partial reads), let deferred tool loading keep MCP schemas out of context until needed, mark side-effecting skills `disable-model-invocation: true` so they cost zero, and know that **the skill index is the one startup item that does *not* survive `/compact`** — a long post-compaction session quietly loses the ability to discover skills it never invoked.

---

## 1. What "Context Engineering" Means in 2026

**Anthropic's definition [High — Official]:** context engineering is "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference," positioned as *the natural progression of prompt engineering* rather than a replacement. Prompt engineering = "writing and organizing LLM instructions"; context engineering = managing the whole token budget: system instructions, tools, MCP servers, external data, message history, memory.
Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Sept 29, 2025)

The framing shift Anthropic states directly: building with LLMs is "less about finding the right words and phrases for prompts, and more about answering the broader question of *what configuration of context is most likely to generate our model's desired behavior*."

**Characterization of the "broader discipline" claim.** The industry narrative that context engineering *contains* prompt engineering is accurate as vendors use it, but it is worth being precise about *why* the term appeared, because the popular version is slightly inflated:

- The real driver is **agentic loops**, not a discovery that prompts don't matter. A single-turn chat completion has one author of its context (you). An agent running 50 turns has many authors: tool results, sub-agent returns, retrieved files, its own prior reasoning. Nobody is "writing" that context — it *accumulates*. Context engineering is the discipline of governing accumulation. [Moderate — Practitioner consensus]
- The prompt is now a *component* of context, and in 2026 vendor guidance it is a shrinking component (see §5 on Anthropic removing >80% of Claude Code's system prompt). [High — Official]
- **Hype flag:** "prompt engineering is dead, context engineering replaced it" is the SEO version and is wrong. Anthropic explicitly frames it as progression/superset, and system-prompt "altitude" guidance is still prompt engineering. Treat any source that declares prompt engineering obsolete as content marketing. [Unverified / Hype]

**Working definition for this project:** context engineering is *budget management under an attention constraint*. Every token in the window costs attention that is not spent on the tokens that matter.

---

## 2. The Physical Basis: Why Context Is Finite Beyond the Token Limit

This is the load-bearing empirical claim of the whole field, and it is well-supported.

**Attention budget [High — Official]:** Anthropic: "LLMs have an *attention budget* that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount." Architectural reason given: transformers compute n² pairwise relationships for n tokens, so "as context length increases, a model's ability to capture these pairwise relationships gets stretched thin"; additionally models have seen fewer long-sequence training examples, so have "fewer specialized parameters" for long-range dependency.

**Context rot [High — Measured]:** Chroma's 2025 study tested 18 frontier models (incl. GPT-4.1, Claude Opus 4, Gemini 2.5) and found *every* model degrades as input length grows, at every increment tested — and degrades **non-uniformly**, not linearly. The practical consequence: you cannot reason about "I'm only at 60% of the window so I'm fine."

**Lost-in-the-middle [High — Measured]:** Liu et al. (Stanford, TACL) — retrieval accuracy follows a U-shape by position: strong at the start and end of context, 20–30 points lower in the middle. Mechanistic account attributes it partly to RoPE long-term decay reducing attention weight on distant token pairs.

> **Practical corollary, widely replicated:** put the *task* and the *current state* at the **end** of the context, and stable instructions at the **start**. The middle is where information goes to be ignored. Manus operationalizes this by having the agent continually rewrite a `todo.md` and keep it at the end of context specifically "to bias the model's attention towards its global plan." [Moderate — Practitioner consensus]

---

## 3. Core Techniques

### 3.1 The four-operation framework: Write / Select / Compress / Isolate

LangChain's taxonomy (Jul 2, 2025) is now the de facto shared vocabulary; it is framework-agnostic and applies equally to LangGraph, the Claude Agent SDK, or a raw API loop. [High — Official (LangChain) + Moderate — consensus on adoption]
Source: https://www.langchain.com/blog/context-engineering-for-agents

| Operation | Meaning | Concrete mechanisms |
|---|---|---|
| **Write** | Persist context *outside* the window so it survives | scratchpads, `todo.md`/plan files, memory files, session state |
| **Select** | Pull the right thing in at the right moment | file reads, grep/glob, RAG, tool-description retrieval, memory recall |
| **Compress** | Reduce what's already in-window to what still matters | summarization/compaction, trimming, tool-result clearing |
| **Isolate** | Split work into separate windows so noise doesn't cross-contaminate | sub-agents, sandboxed code execution, state schemas |

### 3.2 Curation / minimization

**The governing rule [High — Official]:** "Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome." (Anthropic)

Sub-rules from the same source:
- System prompts should hit the **"right altitude"** — specific enough to guide, flexible enough to leave heuristics to the model. Both failure modes are named: hardcoded brittle if-else logic, and vague guidance that assumes shared context that doesn't exist.
- Structure prompts with **explicit sections** (`<background_information>`, `<instructions>`) via XML tags or Markdown headers.
- **Examples over rules:** curate "a set of diverse, canonical examples" rather than "a laundry list of edge cases." "For an LLM, examples are the 'pictures' worth a thousand words."
- Start minimal on the best available model, then add only in response to observed failure modes.

### 3.3 Retrieval: RAG vs. just-in-time ("agentic search")

This is the most genuinely contested area, and the 2026 position has moved.

**Anthropic's stated shift [High — Official]:** from embedding-based *pre-inference* retrieval toward **just-in-time context** — the agent "maintains lightweight identifiers (file paths, stored queries, web links)" and loads data at runtime via tools. Rationale given: mirrors human cognition (we don't memorize corpora, we keep pointers); enables **progressive disclosure** where the agent incrementally discovers relevance; metadata like folder structure, naming conventions and timestamps carries real signal.

**Stated trade-off, not glossed over:** "Runtime exploration is slower than retrieving pre-computed data." It also risks the agent "wasting context by misusing tools, chasing dead-ends."

**The hybrid is the actual recommendation [High — Official]:** Anthropic cites Claude Code itself as the reference implementation — `CLAUDE.md` is "naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time."

**Counter-position worth keeping [Moderate]:** RAG is not dead; it's demoted from "the architecture" to "one Select mechanism." For large static corpora with no filesystem-like structure, pre-computed retrieval still wins on latency and cost. Production systems reportedly layer several: Windsurf is cited as using AST parsing, semantic chunking, grep/file search, knowledge graphs, and re-ranking together.

**Tool retrieval [Low — Single source, notable]:** LangChain cites a result that applying RAG *to tool descriptions* improves tool-selection accuracy ~3×. Directionally consistent with the context-confusion evidence in §4, but the specific 3× figure traces to a single paper — treat as directional, not a benchmark.

### 3.4 Compaction / summarization for long sessions

**Definition [High — Official]:** "Taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary." (Anthropic)

- Claude Code's compaction is tuned to **preserve architectural decisions, unresolved bugs, and implementation details** while **discarding redundant tool outputs**. Auto-compact historically triggered after exceeding ~95% of the window.
- **Tuning method [High — Official]:** "Start by maximizing recall to ensure your compaction prompt captures every relevant piece of information from the trace, then iterate to improve precision." I.e. tune for over-inclusion first, then trim. This is a concrete, testable procedure — most advice in this space isn't.
- **Cheapest safe win [High — Official]:** **tool-result clearing** — dropping old tool outputs while keeping the calls — is called "one of the safest, lightest-touch forms of compaction," and shipped as a Claude Developer Platform feature.
- **OpenAI has converged on the same primitive [High — Official]:** server-side compaction in the Responses API via `context_management` with a `compact_threshold`; the server compacts when rendered token count crosses the threshold. Codex relies on it for long-running coding tasks — i.e. it's load-bearing infrastructure, not a fallback. Positioned as a **default long-run primitive**, not an emergency measure.
  Source: https://developers.openai.com/api/docs/guides/compaction
- **Honest limitation [Moderate — consensus]:** compaction is *lossy*. Nuance becomes bullets, tool outputs become references, and abandoned explorations are usually discarded entirely — which means the agent can re-attempt a dead end it already ruled out. Mitigation is to Write dead-ends to a durable file before compaction, not to trust the summary to keep them.

### 3.5 Structured note-taking / external memory

**[High — Official]** The agent periodically writes notes to durable storage outside the window and pulls them back later. Anthropic's cited example: Claude playing Pokémon maintaining tallies across *thousands* of steps ("for the last 1,234 steps I've been training my Pokémon in Route 1"). Anthropic shipped a **memory tool** (public beta, Sonnet 4.5 launch) for exactly this.

**Manus's version [Moderate — Practitioner, detailed]:** treat **the file system as unlimited external context**. Key discipline: compression must be **restorable** — you may drop a file's contents from context as long as the *path* remains, because the content can be re-read. Irreversible compression is the thing to avoid.
Source: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus

**Recitation [Moderate — Practitioner]:** Manus has the agent constantly *rewrite* its `todo.md`, keeping goals and progress at the end of context. This is both a Write and an anti-lost-in-the-middle measure.

**Counterintuitive one worth flagging [Low — Single source]:** Manus deliberately **leaves failed actions and error observations in context**, arguing it implicitly updates the model's beliefs and prevents repeating the failure. This directly tensions with "minimize context" and with compaction's habit of discarding dead ends. Unreplicated by vendor docs. Treat as a hypothesis to test, not a rule.

### 3.6 Structured context: tools, schemas, sub-agent boundaries

**Tool design [High — Official]:** tools must be "self-contained, robust to error, and extremely clear with respect to their intended use." Anthropic names the most common failure mode as **bloated tool sets** with ambiguous decision points, and gives a usable heuristic:

> "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better."

**Sub-agent isolation [High — Official]:** specialized sub-agents work in clean windows; a sub-agent "might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000–2,000 tokens)." The main agent holds the plan; detail stays quarantined.

**Cost of isolation [High — Official, LangChain]:** multi-agent architectures use **up to ~15× more tokens than chat**. Isolation buys context cleanliness with tokens.

### 3.7 Caching and how it interacts with context structure

**[Moderate — Practitioner, with vendor-grounded numbers]** Manus reports KV-cache hit rate is "the most important metric for production-stage AI agents," because the input:output token ratio in an agent is roughly **100:1** — nearly all cost is *reading* context, not generating. With Claude Sonnet pricing cited at the time, cached input was ~$0.30/MTok vs ~$3/MTok uncached — **10×**.

The structural implication is the important part and is not obvious:

- **Keep the prefix stable.** Because generation is autoregressive, a single differing token invalidates the cache *from that token onward*. A timestamp, a randomized tool order, or a non-deterministic JSON key order at the top of your prompt destroys the cache for the whole rest of the window.
- **Append-only context.** Don't edit or re-order past actions/observations; append.
- **This creates a real tension with compaction and with dynamic tool loading** — both change the prefix and therefore blow the cache. The practical resolution is to make prefix changes *rare and batched* (compact once at a threshold) rather than continuous (trimming a message every turn).

---

## 4. Failure Modes: What's Documented vs. What's Folklore

Drew Breunig's four-mode taxonomy (Jun 2025) is the standard reference and, unusually for this space, each mode is backed by a citation.
Source: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html

| Mode | Definition | Evidence | Grade |
|---|---|---|---|
| **Context poisoning** | A hallucination/error enters context and is then repeatedly referenced as fact | DeepMind's own Gemini 2.5 technical report: the Pokémon agent wrote a hallucinated game state into its tracked *goals*; because goals are re-read every turn, the false belief self-validated and the agent pursued an impossible objective for dozens of turns | **High — Measured (vendor technical report)** |
| **Context distraction** | Context grows so long the model over-weights its own history and under-weights training | Gemini 2.5 Pro favored repeating actions from history beyond ~100k tokens; Databricks found correctness declining around ~32k for Llama 3.1 405B | **High — Measured** |
| **Context confusion** | Superfluous content (esp. too many tools) degrades response quality | Berkeley Function-Calling Leaderboard: all models perform worse as tool count rises. GeoEngine: Llama 3.1 8B failed with 46 tools, succeeded with 19 | **High — Measured** |
| **Context clash** | Later information contradicts earlier information in the same window | Microsoft/Salesforce sharded-prompt study: ~39% average performance drop when one prompt is split across turns; o3 fell 98.1 → 64.1. Cause: models commit to assumptions in early turns and over-rely on premature answers | **High — Measured** |

**Assessment of what's real vs. folklore:**

- **Real and well-evidenced:** poisoning, distraction, confusion, clash, lost-in-the-middle, context rot. All four Breunig modes have named studies. Lost-in-the-middle and context rot have controlled studies with numbers.
- **Real but the *thresholds* are folklore:** "degrade after 32k," "keep under 50% of the window," "auto-compact at 95%." These are true *of specific models on specific benchmarks* and get repeated as universal laws. The Databricks 32k figure is Llama 3.1 405B on one task. Don't port a threshold across models. [Flagging as commonly-repeated but over-generalized]
- **Folklore / unverified:** the whole genre of "10 context engineering hacks" listicles asserting fixed token budgets, "optimal chunk size = 512," or percentage splits between instruction/retrieval/history. None of the sources surveyed with actual method support fixed universal ratios. [Unverified / Hype]
- **"Stale context" is real but under-documented.** It's a genuine failure (an agent acting on a file it read 40 turns ago that has since changed), and it's the *mechanism* behind a lot of what gets labeled poisoning. But it doesn't have a dedicated benchmark in the sources surveyed — it's practitioner-reported. [Moderate — Practitioner consensus]

---

## 5. Anthropic / Claude Code–Specific Guidance

This project runs on Claude Code, so this section is the operationally important one.

### 5.1 What actually occupies a Claude Code context window

Anthropic ships an interactive breakdown of a real session. Approximate startup costs from that official simulation (200k window): [High — Official]

| Component | ~Tokens | Notes |
|---|---|---|
| System prompt | 4,200 | always first, never visible |
| Auto memory (`MEMORY.md`) | 680 | first 200 lines or 25 KB, whichever first |
| Environment info | 280 | cwd, platform, git state |
| MCP tools (deferred) | 120 | **names only** — schemas load on demand |
| Skill descriptions | 450 | one line per skill; full body loads only on use |
| `~/.claude/CLAUDE.md` | 320 | global |
| Project `CLAUDE.md` | 1,800 | the biggest controllable startup item |
| *Your first prompt* | 45 | — |
| *One file read* | 1,100–2,400 | **file reads dominate** |

Source: https://code.claude.com/docs/en/context-window

The headline lesson from the official numbers is blunt: **your prompt is noise; file reads are the budget.** A single source file costs 25–50× your prompt. Anthropic's own inline tip: "File reads dominate context usage. Be specific in prompts... For research-heavy tasks, use a subagent."

### 5.2 `CLAUDE.md`

- **Official sizing guidance: keep it under 200 lines.** "Move reference content to skills or path-scoped rules so it only loads when needed." [High — Official]
- Anthropic's 2026 guidance explicitly moves memory *out* of `CLAUDE.md` and into auto-memory features, and reframes `CLAUDE.md` as **repo-specific gotchas, not general instruction**. [High — Official]
  Source: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models (Jul 24, 2026)
- The useful editing test, from a practitioner writeup but consistent with official framing: **"Would a strong model behave worse without this line?"** If not, delete it. Content that duplicates the model's existing competence is pure tax. [Moderate — Practitioner, consistent with official]
- Four categories that *do* earn always-loaded status: operator opinions/preferences, project facts that surprise (gotchas, generated files), routing rules with real thresholds, named integrations (services, env vars, endpoints).

### 5.3 The Claude 5 shift: less instruction, better interfaces

This is the single most important 2026 update and it inverts a lot of 2025 advice. Anthropic removed **over 80% of Claude Code's system prompt** for Claude Opus 5 / Fable 5 "with no measurable loss on our coding evaluations." [High — Official]

Their own before/after table:

| Old advice (2025) | New advice (2026) |
|---|---|
| Give Claude explicit rules | Let Claude use judgment |
| Provide usage examples for tools | Design better tool interfaces |
| Front-load all context upfront | Use progressive disclosure |
| Repeat instructions throughout | Simple tool descriptions |
| Store memory in `CLAUDE.md` | Use auto-memory features |
| Basic markdown specifications | Rich references (code, HTML, rubrics) |

Two specific documented harms from over-instruction on Opus 5: **over-verification** (explicit verification instructions cause the model to waste tokens re-checking) and **delegation inflation** (excessive subagent spawning). Deterministic gates — build, tests, typecheck — stay; motivational instruction goes. [High — Official / Moderate on the specific numbers]

Anthropic also shipped `/doctor` (`claude doctor`) to rightsize skills and `CLAUDE.md` files automatically. [High — Official]

**Skeptical note:** "remove 80% of your prompt" is being repeated as a universal rule. Anthropic's claim is scoped to *Claude Code's* system prompt on *frontier Claude 5 models* against *their coding evals*. On Haiku, or on a domain the model has no priors for (e.g. this repo's F&I compliance material), removed instruction is removed capability. Anthropic's own skills doc says the same: what works for Opus "might need more detail for Haiku." Do not port the 80% figure to a Haiku subagent.

### 5.4 Skills = progressive disclosure as a first-class mechanism

Official three-tier loading model: [High — Official]

1. **Tier 1 — metadata only, always loaded.** `name` + `description` from YAML frontmatter go into the system prompt at startup. Measured median discovery cost ~80 tokens/skill (range ~55–235); Anthropic's own session breakdown shows ~450 tokens for a whole skill index.
2. **Tier 2 — `SKILL.md` body, loaded on trigger.** Official cap: **under 500 lines.** A 19 KB skill costs ~4,800 tokens *every time it fires*, even if a third was needed.
3. **Tier 3 — bundled reference files and scripts, loaded/executed on demand.** "**No context penalty for large files**" — reference material costs zero until read. Scripts executed via bash cost only their *output*, not their source.

Official authoring rules that are really context rules:

- "The context window is a public good." Challenge every line: "Does this paragraph justify its token cost?"
- **Default assumption: Claude is already very smart.** Only add context Claude doesn't have. Their worked example is a 50-token version beating a 150-token version that explained what a PDF is.
- **Keep references one level deep from `SKILL.md`.** Nested references cause partial reads (`head -100`) and incomplete information. This is a concrete, non-obvious failure mode.
- **Reference files over 100 lines need a table of contents at the top**, so a partial read still reveals full scope.
- **Organize reference files by domain**, so a sales question never loads the finance schema.
- **Degrees of freedom should match task fragility:** high freedom (prose heuristics) for open fields, low freedom (exact scripts, "do not modify the command") for narrow bridges with cliffs.
- **Build evaluations before writing documentation** — measure baseline without the skill, write only enough to close the measured gap.

Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

### 5.5 Deferred tool loading

By default in Claude Code, MCP tool **names** are listed (~120 tokens) while **full schemas stay deferred**; the agent fetches schemas via tool search when a task needs them. `ENABLE_TOOL_SEARCH=auto` loads schemas upfront only if they fit within 10% of the context window; `=false` loads everything. [High — Official]

This is the direct engineering answer to the **context confusion** failure mode in §4 (Berkeley FCL / GeoEngine: 46 tools fail, 19 succeed). Large tool surfaces become affordable because they cost nothing until used.

### 5.6 Subagent context isolation

Official framing: use a subagent "when a side task would flood your main conversation with search results, logs, or file contents you won't reference again." Each subagent has **its own context window**, its own (shorter) system prompt, its own tool permissions, and can run on a cheaper model. [High — Official]

Anthropic's worked numbers from the official session walkthrough: **the subagent read 6,100 tokens of files and returned a 420-token result.** That is the context saving, quantified. Anthropic's engineering blog gives the same shape at larger scale: a subagent may burn "tens of thousands of tokens" and return "often 1,000–2,000 tokens." [High — Official]

Non-obvious mechanics worth knowing:

- The subagent **loads its own copy of `CLAUDE.md`** — against its budget, not yours. The built-in `Explore` and `Plan` agents skip this for a smaller footprint.
- The subagent **does not inherit your conversation history or the main session's auto memory.** Anything it needs must be in the task you write for it. This is the #1 cause of subagents doing the wrong work.
- The `Agent` tool is withheld from subagents by default, preventing recursion.

### 5.7 Compaction in Claude Code

- `/compact` replaces conversation with a structured summary; `/context` inspects what's consuming the window; `/clear` starts fresh. [High — Official]
- **After compaction, system prompt, `CLAUDE.md`, memory, and MCP tools all reload automatically. The skill listing is the one exception — only skills you actually invoked are preserved.** [High — Official] This is a genuinely surprising, load-bearing detail: a long post-compaction session silently loses the ability to *discover* skills it never used.
- Anthropic's compaction tuning method (from the engineering blog): maximize recall first, then iterate for precision.
- `disable-model-invocation: true` keeps a skill out of the index entirely — zero context cost until the user types `/name`. Official recommendation: use it for skills with **side effects** (committing, deploying, sending messages). [High — Official]

### 5.8 The multi-agent question, honestly

There is a real, documented disagreement here worth preserving rather than resolving:

- **Cognition, "Don't Build Multi-Agents" (2025):** single-threaded only, with a separate compression model. Argument: **context fragmentation** — parallel agents make conflicting implicit decisions because they don't share the decisions that led to the task split.
- **Cognition, "Multi-Agents: What's Actually Working" (Apr 22, 2026):** a substantial revision. What works is **read/write asymmetry** — many read-only agents contributing *intelligence*, one single-threaded writer contributing *actions*. Parallel writer swarms still fail on conflicting style/edge-case decisions.
- **Counterintuitive finding worth flagging [Low–Moderate — single vendor, but specific]:** a dedicated review agent performs *better* with **no** shared context from the coding phase — clean context beats informed context for review, catching ~2 bugs/PR (58% severe). If true, this contradicts the naive "give agents more context" instinct and supports deliberate context *starvation* for adversarial roles.
- **Convergence claim [Moderate — consensus]:** Anthropic, Cognition, OpenAI, Microsoft Agent Framework and LangChain have all landed on the same shape — one orchestrator owning the full conversation, spawning ephemeral isolated subagents that return compressed summaries. That's exactly what Claude Code's Agent tool implements.

**Cost of the pattern:** LangChain reports multi-agent setups burn **up to ~15× more tokens than chat**. Isolation is bought with tokens, not free.

---

## 6. Actionable Rules

Written to be directly embeddable in an agent's operating instructions.

### Budget

1. **Treat the context window as a per-turn budget, not a bucket.** Do not reason "I'm at 60%, I'm fine" — degradation is non-uniform and starts well before the limit.
2. **Assume file reads are the budget.** One source file ≈ 25–50× a user prompt. Before reading a file, ask whether a `grep` for the specific symbol would answer the question.
3. **Never read a whole file to answer a question about one function.** Grep for the symbol, read the range.
4. **Ask "would a strong model behave worse without this?" before adding any line to an always-loaded file.** If no, delete it.

### Placement

5. **Stable instructions at the top, current task and state at the bottom.** The middle of the context is where information goes to be ignored (U-shaped positional recall, 20–30 point mid-context drop).
6. **Re-state the goal near the end of long sessions.** Rewriting a `todo.md` / plan block late in context is both a Write and a defense against distraction.
7. **Use explicit structure** — XML tags or Markdown headers delimiting `<background>` / `<instructions>` / `<current_state>`. Unstructured concatenation is what makes context clash invisible.

### Retrieval

8. **Default to just-in-time retrieval over pre-loading.** Keep pointers (file paths, queries, URLs) in context; load contents at the moment of use.
9. **Use the hybrid, not a religion:** a small always-loaded index (`CLAUDE.md`, skill descriptions, folder map) + on-demand loading (`grep`, `glob`, file reads, RAG for large static corpora).
10. **Treat folder structure, file names and timestamps as retrieval signal.** Name things so an agent can route on the name alone.

### Compression

11. **Compact on a threshold, not continuously.** Continuous trimming destroys the KV cache prefix every turn; one batched compaction at a threshold pays for itself.
12. **Clear stale tool results first.** Keep the tool *call*, drop the old *output*. Officially "the safest, lightest-touch form of compaction."
13. **Before compacting, Write the things compaction is known to lose** — dead ends already ruled out, unresolved bugs, architectural decisions — to a durable file. Compaction is lossy and discards abandoned explorations by default.
14. **Tune a compaction prompt by maximizing recall first, then trimming for precision.** Not the reverse.
15. **Prefer restorable compression.** Dropping a file's contents is safe while its *path* survives. Never irreversibly summarize something you can cheaply re-read.

### Isolation

16. **Delegate any task whose *intermediate* output you'll never reference again.** Research, log triage, broad search, codebase mapping. The subagent burns the tokens; you get the summary.
17. **Write subagent task prompts as if to a stranger** — the subagent inherits no conversation history and no session memory. Include absolute paths, the actual question, and the required output shape.
18. **Ask subagents to return conclusions, not transcripts.** Target 1–2k tokens back from tens of thousands explored.
19. **Keep writes single-threaded.** Parallelize reading, analysis and review; serialize edits. Parallel writers make conflicting implicit decisions.
20. **Consider deliberately starving adversarial roles of context.** A reviewer with clean context outperforms one carrying the author's rationalizations.

### Tools

21. **If a human engineer can't say definitively which tool applies, neither can the agent.** Merge or delete overlapping tools.
22. **Defer tool schemas.** Names in context, schemas on demand. Tool count degrades performance measurably (46 tools fail where 19 succeed).
23. **Prefer executing a script over generating one.** Executed scripts cost only their output; generated code costs its full source in context, twice.

### Caching

24. **Keep the prefix byte-stable.** No timestamps, no non-deterministic JSON key ordering, no reordered tool arrays at the top of the window. One changed token invalidates everything downstream.
25. **Append, don't edit.** Rewriting history is a cache-invalidating operation with a ~10× cost multiplier on the re-read.
26. **Put cache breakpoints after stable content only** — tools, system prompt, long-lived reference — and leave the volatile query uncached.

### Hygiene

27. **Correct poisoned context explicitly and immediately.** If a hallucinated fact has entered a plan/goal/memory file, delete it at the source — it will otherwise be re-read every turn and self-validate.
28. **Re-read before acting on anything read more than a few turns ago.** A file's content in context is a claim about the past, not the present.
29. **Instrument, don't guess.** Use `/context` (or equivalent token accounting) to see what's actually consuming the window before optimizing.
30. **Don't port thresholds across models.** "Degrades at 32k," "compact at 95%," "80% prompt reduction" are all model- and benchmark-specific. Re-measure.

---

## 7. If I Could Only Keep 10 Rules

The distillation intended to seed a Claude Code skill.

1. **The smallest set of high-signal tokens wins.** Every token you add spends attention that other tokens needed. Adding context is a cost, not a freebie.
2. **File reads are the budget; your prompt is a rounding error.** Grep before you read; read ranges, not files.
3. **Instructions at the top, live state at the bottom, nothing important in the middle.**
4. **Pointers in context, payloads on demand.** Keep paths, queries and an index loaded; load contents just-in-time.
5. **Progressive disclosure everywhere:** one-line description → body under 500 lines → reference files one level deep, loaded only when needed. Bundled files cost zero until read.
6. **Delegate anything whose intermediate output you'll never reference again**, and write the subagent's task as if to a stranger — it has none of your history.
7. **Compact at a threshold, not continuously — and Write what compaction will lose (dead ends, decisions, open bugs) to a file first.** Compaction is lossy by design.
8. **Prefer restorable compression:** drop contents, keep paths.
9. **Keep the prefix byte-stable and append-only.** Editing history costs ~10× on the re-read and blows the cache.
10. **Delete instruction the model doesn't need, but don't port that rule across models or domains.** "Would a strong model behave worse without this line?" — and remember the answer differs for Haiku, and for domains with no training priors.

---

## Caveats and Open Questions

- **The 2026 "less instruction" turn is genuinely new and genuinely scoped.** It is well-evidenced for frontier Claude 5 models on coding evals and much weaker as a general law. This brief has treated it as directional, not universal.
- **Manus's "leave failures in context" advice directly contradicts minimization and compaction defaults.** Unreplicated by vendor docs. Flagged as a hypothesis, not adopted into the rules above.
- **"Stale context" lacks a benchmark.** It is practitioner-reported and mechanically plausible (and is arguably how most context poisoning actually starts), but no controlled study surfaced in this pass.
- **Threshold numbers are the most-abused artifacts in this literature.** Every specific number in this brief is tagged with its model and benchmark for that reason.
- **Not covered:** multimodal context budgeting (images/video are token-expensive and behave differently), context-window pricing arbitrage across providers, and formal evaluation harnesses for context strategies. Worth a follow-up pass if this project starts routing across models.

---

## Sources

**Primary / official:**
- Anthropic Engineering — *Effective context engineering for AI agents* (Sept 29, 2025): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic / Claude — *The new rules of context engineering for Claude 5 generation models* (Jul 24, 2026): https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- Claude Platform Docs — *Skill authoring best practices*: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Claude Platform Docs — *Agent Skills overview*: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code Docs — *Explore the context window* (interactive token breakdown): https://code.claude.com/docs/en/context-window
- Claude Code Docs — *Create custom subagents*: https://code.claude.com/docs/en/subagents
- OpenAI API Docs — *Compaction*: https://developers.openai.com/api/docs/guides/compaction
- OpenAI Cookbook — *Context Engineering: Short-Term Memory Management with Sessions*: https://developers.openai.com/cookbook/examples/agents_sdk/session_memory
- LangChain — *Context Engineering for Agents* (Jul 2, 2025): https://www.langchain.com/blog/context-engineering-for-agents
- LangChain — *How and when to build multi-agent systems*: https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems
- LangChain (repo) — *how_to_fix_your_context*: https://github.com/langchain-ai/how_to_fix_your_context

**Practitioner / vendor engineering writeups:**
- Drew Breunig — *How Long Contexts Fail* (Jun 22, 2025): https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
- Simon Willison on the above: https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/
- Manus — *Context Engineering for AI Agents: Lessons from Building Manus*: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Cognition — *Don't Build Multi-Agents*: https://cognition.com/blog/dont-build-multi-agents
- Cognition — *Multi-Agents: What's Actually Working* (Apr 22, 2026): https://cognition.com/blog/multi-agents-working
- Martin Fowler (Thoughtworks) — *Context Engineering for Coding Agents*: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- Sourcegraph — *Context Engineering: A Practical Guide for AI Agents (2026)*: https://sourcegraph.com/blog/context-engineering
- claudefa.st — *The New Rules of Context Engineering for the Claude 5 Family*: https://claudefa.st/blog/guide/mechanics/claude-5-context-engineering

**Research / measured:**
- Liu et al. — *Lost in the Middle: How Language Models Use Long Contexts* (TACL): https://www.researchgate.net/publication/378284067_Lost_in_the_Middle_How_Language_Models_Use_Long_Contexts
- Chroma — *Context Rot* study (18 frontier models); secondary coverage: https://redis.io/blog/context-rot/
- Lodha, Pahlavikhah Varnosfaderani, Chakraborty & Mithal — *Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents* (arXiv:2606.10209, Jun 10, 2026): https://arxiv.org/pdf/2606.10209
- *Context Engineering 2.0: The Context of Context Engineering* (arXiv:2510.26493): https://arxiv.org/pdf/2510.26493

**Referenced within sources, not independently verified in this pass:** Berkeley Function-Calling Leaderboard (tool-count degradation), GeoEngine benchmark (46 vs 19 tools), Databricks long-context correctness study (Llama 3.1 405B ~32k), Microsoft/Salesforce sharded-prompt study (~39% drop), DeepMind Gemini 2.5 technical report (Pokémon context poisoning).
