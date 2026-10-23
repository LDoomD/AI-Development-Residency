# Obsidian Community Plugins for ADHD Study — TTS, AI Chat, Flashcards, Mind Maps, NotebookLM Gap Analysis

> ## ⚠️ SUPERSEDED IN PART — read this before acting on anything below
>
> **Added 2026-08-10, same day.** This brief was written **without first checking
> `specs/DECISIONS.md`**, and several of its recommendations conflict with locked decisions:
>
> - **Spaced-repetition and quiz-generator plugins: do not adopt.** `DECISIONS.md` §1 locks the
>   review queue to **Anki** (`.apkg` / FSRS). An in-Obsidian SRS plugin duplicates it.
> - **"Chat with your notes" plugins (Copilot, Smart Connections): use for search only, never
>   for explanation.** `DECISIONS.md` §8 locks the boundary *"Gemini helps you learn it, Claude
>   decides whether you know it"* — grounded in Bastani et al. (PNAS 2025), where unguarded AI
>   tutoring raised in-session scores while **eroding unassisted performance**.
> - **TTS is real but modest**, not a headline feature: d ≈ 0.35 per Wood et al. (2018), see
>   `2026-08-09_dyslexia-cognitive-science.md` §4. This brief oversold it.
>
> **What still stands:** the TTS and focus/reading-mode picks, and the NotebookLM gap analysis.
>
> **The bigger point this brief missed:** the highest-leverage dyslexia intervention is not a
> plugin at all — it is morphology-first glossing and chunking **written into the lesson
> Markdown itself** (`DECISIONS.md` §7). No plugin does that.
>
> See also `2026-08-10_examples-mode-tooling-search.md`, which found that **Anki's native
> Filtered Decks** already covers the EXAMPLES-mode gap this brief left open.

> **RESEARCH TIER.** Date: 2026-08-10.
> Requested to answer: "does Obsidian have plugin equivalents to NotebookLM's audio overview,
> source-grounded chat, auto-summary, mind maps, and study-guide/flashcard generation?" — plus
> a general "everything that could help me learn better" sweep for an ADHD learner studying
> dense F&I (finance & insurance) regulatory/product material.
> Sources: Obsidian community plugin directory (obsidian.md/plugins, community.obsidian.md),
> obsidianstats.com (download counts, last-update dates), plugin GitHub repos, and general web
> search. Every plugin below was checked against a live source; nothing here is from model memory
> of "plugins that probably exist."

---

## Summary table

| Plugin | What it does | Free/Paid (API needed?) | Fit for ADHD study of dense material | Vault-convention risk (proprietary syntax?) |
|---|---|---|---|---|
| **Text to Speech** (`obsidian-tts`, joethei) | Reads notes/selections aloud using the OS's native TTS (macOS/Windows/iOS; no Android). Start/pause/resume from status bar. | Free, no API key — uses OS voices | Good baseline: zero-cost audio pass over dense text while doing something else (driving, chores). Voice quality is robotic (system voice), which can undercut engagement for long F&I regulatory passages. | None — reads plain markdown, writes nothing back |
| **Aloud** | Real-time TTS with sentence-level streaming + active-sentence highlighting, using OpenAI/Gemini/ElevenLabs/Azure/Polly voices | Free plugin, **paid API** (per-provider) | The sentence highlighting is a genuine ADHD win — following along visually while listening improves sustained attention more than audio alone. | None — reads plain markdown, writes nothing back |
| **Voice** | Turns notes into an "audiobook" experience: sidebar player, chapter-style playback across multiple notes, podcast-style transport controls, MP3 export for offline listening | Free plugin, **paid API** (AWS Polly/ElevenLabs/Google/Azure/OpenAI/MiniMax — pick one) | Closest thing on this list to a NotebookLM "audio overview" for a single subject's lesson set — press play and get sequential playback of a whole `learning/f-and-i/` folder like chapters. Not generative narration (no two-host script, no synthesized commentary) — it reads your existing text verbatim. | None — reads plain markdown, writes nothing back |
| **Smart Connections** | Local (on-device) semantic search + "chat with your vault" — surfaces related notes and answers questions grounded in your own notes | Free core, **no API key required** (ships a local embedding model); paid "Connections Pro" tier adds extras | Strong fit: source-grounded Q&A over your F&I notes without sending study material to a cloud API by default, and no per-query cost. Good for "what did I already write about GAP insurance" style recall during review. | Low — UI layer over plain markdown; suggested links are inserted as standard `[[wikilinks]]` if you choose to accept them, not a proprietary block format |
| **Copilot** | Full chat interface inside Obsidian, grounded in vault content ("bring your own model") — closer to a real conversational tutor than Smart Connections | Free tier + **API key required** (OpenAI/Anthropic/Gemini/OpenRouter/Cohere, or self-hosted/local model); paid "Believer" tier for agent mode etc. | Best fit for actual **Socratic Q&A practice** over F&I material — you can ask it to quiz you, explain a term back, or push on a weak spot, using your own notes as ground truth. Needs an API key (cost is usage-based, typically cents per session for a personal vault). | None — standard markdown, chat happens in a side pane, doesn't rewrite notes |
| **AI-Vault** | Chat with OpenAI/Anthropic/local models with vault-aware context (canvases, files, selections) | Free plugin, **API key required** | Similar niche to Copilot; smaller install base, less battle-tested. Only worth it if Copilot's UX doesn't fit. | None — chat-only |
| **AI Summarize** | Summarizes selected text or a whole note via OpenAI; output can replace selection, insert below, go to frontmatter, or create a new note | Free plugin, **requires OpenAI API key** (paid usage) | Direct NotebookLM "auto-generated summary" equivalent — condensing a dense F&I lesson into a study-guide-style abstract. Small install base (~3K downloads) vs. alternatives, so less battle-tested; output format is plain markdown either way, so low risk to try. | Low — inserts plain text/markdown, no locked-in formatting; but *can* write into the note itself (frontmatter/inline), so review before accepting if you care about `learning/` staying gate-controlled per vault rule 5 |
| **Quiz Generator** (ECuiDev) | Generates exam-style questions (true/false, multiple choice, matching, fill-in-blank, short/long answer) from a note, with a built-in quiz-taking UI | Free plugin, **API key required** (OpenAI/Gemini/Anthropic/Perplexity/Mistral/Cohere, or **Ollama for local/free**) | Strong NotebookLM "study guide" analog — turns an F&I lesson into a self-test instead of passive re-reading, which is a much better retention strategy for ADHD than rereading notes. Actively maintained (340+ commits). | **Low** — output can be saved as plain inline/multiline cards compatible with Spaced Repetition plugin syntax, or as markdown callouts. Uses the same `Question::Answer` convention as Spaced Repetition below (see that row for the syntax tradeoff) |
| **Obsidian Spaced Repetition** | Anki-style SM-2 spaced repetition, reviewed inside Obsidian; supports single-line (`Q::A`), reversed, multi-line, and cloze (`==...==`, `{{...}}`) cards | Free, **no API key** | The best-established, most battle-tested tool on this list (548K+ downloads, updated 2 months ago) for what ADHD learners need most: forced, scheduled active recall instead of re-reading. Directly suited to F&I product-term drilling (VSC vs. GAP vs. tire-and-wheel definitions, compliance thresholds). | **Real risk, flagged per your rule 3.** Card syntax (`Question::Answer`, `??`, cloze `{{}}`) is plugin-specific. It still renders as plain text outside Obsidian (nothing breaks visually), but the *spaced-repetition behavior* only exists inside this plugin — so a card written this way "degrades gracefully" to inert text elsewhere, which is a softer violation than binary/proprietary formats but still worth being deliberate about where you put it (see recommendation below) |
| **Flashcards LLM / Spaced Repetition AI / Gated Notes** | Various plugins that auto-generate flashcards from note text via LLM, then hand them to spaced-repetition review | Free plugin, **API key required** (varies) | Same idea as Quiz Generator but smaller communities / less vetted. Not recommended as a first pick — Quiz Generator + Spaced Repetition already covers this need with a bigger user base. | Same syntax risk as Spaced Repetition, since most target its card format |
| **Obsidian Canvas** (built-in, JSON Canvas) | Native visual board for arranging notes, images, and free text spatially | Free, built-in, no API | Already your vault's convention (`canvas/` folder, rule 4) — genuinely good for building a visual schema of, e.g., how the menu's three pages relate, without touching prose notes. Not auto-generated from notes; you build it by hand (or with an agent's help). | **None by design** — Canvas files are separate `.canvas` JSON files, never mixed into `learning/` markdown, which is exactly the "addition, never a replacement" pattern rule 4 already establishes |
| **ExcaliBrain** | Auto-generates an interactive mind-map view of your vault's actual links/tags/dataview fields (requires Excalidraw + Dataview) | Free, no API | Automatic (not hand-built) mind map from your existing note graph — closest thing to a NotebookLM-style auto mind map. Requires two other plugins installed as dependencies, adding fragility. | Low risk to your notes (it *reads* links/tags, doesn't require special syntax beyond normal `[[links]]` and tags you'd use anyway) but the visualization itself only exists as an Excalidraw view, not a portable artifact |
| **Canvas Mindmap / Mind Map Visual** | Manual or semi-automatic mind-mapping via Canvas or a dedicated mind-map editor | Free, no API | Useful for structuring a single lesson's concept map (e.g., product lineup taxonomy) but manual effort, not auto-summary from source. | Canvas-based ones are as safe as native Canvas; the dedicated "Mind Map Visual" plugin stores its own file format alongside markdown, so check before using it inside `learning/` |
| **Focus and Highlight / Zen / Fullscreen Focus Mode** | Distraction-reduction reading/writing modes — dim everything except the active heading/paragraph, remove UI chrome | Free, no API | Directly useful for ADHD sustained attention during long F&I lesson reads — reduces visual noise without changing content. | None — pure display-layer plugins, don't touch file content at all |
| **PomoBar** | Pomodoro timer in the status bar (25/15/5-minute presets) | Free, no API | Standard external-scaffolding tool for ADHD time-on-task; not learning-specific but commonly paired with study plugins. | None |

---

## Recommended starter set

1. **Copilot** — the single highest-leverage pick: source-grounded chat over your own F&i notes lets you *ask* to be quizzed or challenged instead of passively rereading, which is the core "explain-back" mechanic this vault's gate design already values. Needs an API key, but usage cost for a personal study vault is trivial (cents per session).
2. **Obsidian Spaced Repetition** — the most proven, most-used plugin in this whole space (548K downloads, actively maintained) for the actual retention mechanism ADHD learners need most: scheduled forced recall instead of rereading. Use it deliberately, in a place you're comfortable holding plugin-specific syntax (see caveat below).
3. **Quiz Generator** — auto-generates real study-guide-style self-tests from a lesson, which is the most direct NotebookLM "study guide" equivalent found, and it can output in Spaced Repetition-compatible syntax so the two plugins chain together.
4. **Voice** — closest available analog to a NotebookLM "audio overview": queue up a whole F&I lesson folder and listen to it back-to-back, hands-free, while commuting or doing chores. Requires picking a paid TTS provider (ElevenLabs or OpenAI voices sound far better than the free system-voice plugin).
5. **Focus and Highlight** (or Zen) — free, zero-risk, pure UI dimming that reduces visual noise while reading dense regulatory text. Costs nothing to try and nothing to undo.

**Syntax caveat for #2 and #3:** Spaced Repetition's card syntax (`Q::A`, cloze `{{}}`) is plugin-specific, but it degrades to plain (if slightly odd-looking) text outside Obsidian rather than breaking the file. Given rule 3's "near-zero exit cost" goal, consider keeping generated flashcards in a dedicated file (e.g. a `flashcards.md` per subject, separate from the narrative lesson prose) rather than embedding review syntax directly inside `learning/<subject>/NN-*.md` lesson files — that way the lesson files themselves stay 100% portable, and only a clearly-labeled review file carries the plugin dependency.

---

## NotebookLM gap analysis

| NotebookLM feature | Real Obsidian equivalent today? | Verdict |
|---|---|---|
| **Audio overview** (generated two-host podcast script from source material) | **No direct equivalent.** TTS plugins (Voice, Aloud, obsidian-tts) read your *existing* text aloud — they narrate, they don't write a script, invent dialogue, or synthesize a discussion between two "hosts." Multiple independent sources confirm no Obsidian plugin currently does script-generation-then-TTS in one step. | **Gap.** Closest workaround: use an AI plugin (Copilot/AI Summarize) to draft a "podcast script" summary of a lesson as a new markdown note, then feed that note to Voice/Aloud for narration — two manual steps, no plugin glues them. |
| **Source-grounded chat / Q&A over your notes** | **Yes, real equivalent(s).** Smart Connections (local, free, no API key) and Copilot (API-based, more conversational) both do vault-grounded chat today, and are both mature (1M+ and 1.6M+ downloads respectively, updated within the last 3 months). | **Covered.** This is the strongest match to NotebookLM of anything researched. |
| **Auto-generated summary** | **Yes, but thinner.** AI Summarize and similar plugins will summarize a note or selection via API call. It's a single-note (or selected-notes) summarizer, not NotebookLM's whole-notebook synthesis across many sources at once — you'd have to select/combine notes yourself first. | **Partially covered.** Works for one lesson at a time; multi-source synthesis needs manual assembly first. |
| **Study guide / flashcards generated from source material** | **Yes, and arguably better-suited to spaced repetition than NotebookLM's own study guides.** Quiz Generator and Flashcards LLM generate questions directly from note text via API, and Quiz Generator's output plugs straight into the well-established Spaced Repetition plugin for scheduled review — something NotebookLM doesn't do natively. | **Covered, and arguably an upgrade** once chained with Spaced Repetition. |
| **Mind map from notes** | **Partially.** ExcaliBrain auto-generates a mind-map view from your vault's actual link/tag graph (not from prose content directly), and requires Excalidraw + Dataview as dependencies. Obsidian's built-in graph view does a cruder version of this natively, free, no plugins. Neither reads dense prose and extracts a concept hierarchy the way NotebookLM's mind map does. | **Gap, partially bridged.** Best available today is graph-of-links, not content-derived concept extraction. Your existing canvas/ convention (hand-built diagrams matching a lesson) is actually a more deliberate substitute already in use in this vault. |

**Bottom line:** two of four NotebookLM standout features (source-grounded chat, study-guide/flashcard generation) have solid, mature Obsidian plugin equivalents today — arguably *better* suited to spaced, ADHD-friendly review than NotebookLM's own versions once chained together. The other two (generative audio-overview scripting, and content-derived mind-mapping) don't exist as single plugins; each requires gluing 2+ tools together manually, with a real quality gap versus what NotebookLM ships natively.
