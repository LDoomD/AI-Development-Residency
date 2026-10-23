# Research Brief: How a Person Should Actually Use AI to Learn — Evidence Review

**Prepared for:** jose.castillo@giant.cos.edu
**Date:** 2026-08-10
**Scope:** The *learner's* personal usage habits, not tutoring-system design.
**Builds on (does not re-litigate):** `2026-08-09_10x-learning-claims-audit.md`,
`2026-08-09_ai-tutor-landscape-2026.md`, `2026-08-09_agentic-tutoring-workflow-design.md`,
`2026-08-08_prior-art.md`, and `DECISIONS.md` §6, §8, §11.
**Status:** Draft for review. Proposes additions to the Queued list, no changes to Locked items.

---

## Executive Summary

The single most reproducible finding in the 2024–2026 literature on personal AI use for
learning is a **dissociation between performance and learning**. When a learner uses a
general-purpose chatbot while working, the *artefact they produce* gets measurably better —
higher essay scores, more correct exercises, faster completion — and the *knowledge they
walk away with* does not. Four independent studies using different materials, populations,
and outcome measures (Fan et al. 2025, BJET; Kreijkes et al. 2025, *Computers & Education*;
Bassner et al. 2026, *Computers & Education: AI*; Rismanchian et al. 2026, preprint)
converge on this shape. This is the same failure mode as Bastani et al. (PNAS 2025), already
locked in `DECISIONS.md` §8, arriving from four more directions.

The second most reproducible finding is worse, because it's the one a self-directed learner
cannot self-correct: **learners systematically prefer the method that teaches them less.**
In the largest and best-designed study in this set — a pre-registered RCT with 405 secondary
students and a three-day delayed test — the LLM-only condition lost to note-taking on both
comprehension and retention, while *most students rated the LLM as more helpful* (Kreijkes
et al. 2025). Subjective helpfulness is anti-correlated with the outcome that matters. For a
solo learner with no external assessment, that is the whole problem in one sentence.

The headline "AI improves learning" meta-analytic claims should be treated as **not yet
established**. The most-cited one — Wang & Fan (2025), *Humanities and Social Sciences
Communications*, reporting g = 0.867 for learning performance — was **retracted on 2026-04-22**
for pooling studies too heterogeneous and too low-quality to combine. Surviving
meta-analyses (Liu 2025, g = 0.577; Deng et al. 2025) report their largest effects in the
smallest samples, a textbook small-study/publication-bias signature, and — critically —
mostly measure performance *with the AI present*, which the primary RCTs above show is the
wrong dependent variable.

The one genuinely positive rigorous result (Kestin et al. 2025, *Scientific Reports*, Harvard
physics, ~194 students, AI tutor beat an active-learning class) is **not evidence for
chatting with ChatGPT.** It used a purpose-built tutor explicitly constrained to release one
step at a time and never a full solution, and the outcome was an immediate post-test. It is
evidence that *guardrails*, not *AI*, are the active ingredient — the exact position
`DECISIONS.md` §8 already holds.

On ADHD and dyslexia: **there is still no study measuring learning or retention outcomes for
AI-assisted study in ADHD or dyslexic adults.** What exists is (a) qualitative analysis of
what neurodivergent people say on Reddit about using LLMs, (b) evaluations of what LLMs *say*
about ADHD/dyslexia, and (c) one dyslexia writing-support study that measured engagement and
motivation, not learning. The gap this repo's prior-art brief documented is unchanged.

---

## 1. What Happens When the Learner Drives

### 1.1 The core result: the work improves, the learner doesn't

**Fan, Tang, Le, Shen, Tan, Zhao, Shen, Li & Gašević (2025)**, "Beware of metacognitive
laziness: Effects of generative artificial intelligence on learning motivation, processes,
and performance," *British Journal of Educational Technology* 56(2), 489–530.
<https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544>

Randomised experiment comparing four support conditions on a writing task: ChatGPT, a human
expert, writing-analytics tools, and no extra tool. Result: *"ChatGPT group outperformed in
the essay score improvement but their knowledge gain and transfer were not significantly
different."* The authors name the mechanism **metacognitive laziness** — offloading
goal-setting, error monitoring, and strategic reflection to the AI rather than doing them.

This is the cleanest statement of the problem available. The output improved; the person
did not.

**Grade: Moderate–High.** Randomised, published in a strong venue, mechanism-specific.
Docked from High because it is a single task in a single domain (writing) with a single
session.

---

**Kreijkes, Kewenig, Kuvalja, Lee, Vitello, Hofman, Sellen, Rintel, Goldstein, Rothschild,
Tankelevitch & Oates (2025)**, "Effects of LLM use and note-taking on reading comprehension
and memory: A randomised experiment in secondary schools," *Computers & Education*.
<https://www.sciencedirect.com/science/article/pii/S0360131525002829> ·
preprint: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5095149> ·
<https://www.microsoft.com/en-us/research/publication/effects-of-llm-use-and-note-taking-on-reading-comprehension-and-memory-a-randomised-experiment-in-secondary-schools/>

Pre-registered RCT, 405 students aged 14–15, seven schools in England, two text passages,
**comprehension and retention tested three days later**. Conditions: LLM only, note-taking
only, both.

Findings, in the authors' framing:
- Note-taking alone **and** note-taking combined with the LLM both produced significantly
  better retention and comprehension than **LLM alone**.
- **Most students preferred the LLM and perceived it as more helpful.**
- Qualitatively: students valued the LLM for making hard material accessible and reducing
  cognitive load; they valued note-taking for cognitive engagement and durable retention —
  i.e. they could articulate the tradeoff and still chose the worse option.

**Grade: High.** Pre-registered, RCT, real classrooms, adequately powered, and — the part
almost no AI-education study has — a **delayed** outcome measure. This is the best single
citation in the whole brief.

*Caveat I could not verify this pass:* I did not confirm whether the paper reports a
moderator effect for lower-attaining students. That would be the most directly relevant
subgroup for this project and should be checked against the full text before anything is
built on it. **Do not assume it exists.**

---

**Bassner, Lenk-Ostendorf, Beinstingel, Wasner & Krusche (2026)**, "Less stress, better
scores, same learning: The dissociation of performance and learning in AI-supported
programming education," *Computers and Education: Artificial Intelligence* 10.
<https://www.sciencedirect.com/science/article/pii/S2666920X25001778> ·
<https://www.edtech.tum.de/the-dissociation-of-performance-and-learning-in-ai-supported-programming-education/>

Three-arm RCT, N = 275, introductory Python course at TU Munich. Scaffolded LLM tutor
(graduated four-tier hints) vs. unrestricted AI vs. TA support. Both AI groups scored
significantly higher on the programming exercises; **neither showed greater conceptual
learning or code comprehension.** AI users reported lower frustration and lower cognitive
load. Only the *scaffolded* tutor raised intrinsic motivation; unrestricted AI produced what
the authors call a **"comfort trap."**

**Grade: Moderate–High.** RCT, decent N, and it directly tests the scaffolded-vs-unrestricted
contrast this project cares about. Note the finding cuts both ways: scaffolding helped
motivation and stress, but *did not rescue conceptual learning either*. Guardrails are
necessary, not sufficient.

---

**Rismanchian, Uzun, Matayoshi, Cosyn & Kurd-Misto (2026)**, "Faster Completion, Less
Learning: Generative AI Reduced Study Time on Math Problems and the Knowledge They Build,"
arXiv:2605.21629. <https://arxiv.org/abs/2605.21629>

Same shape in maths: AI access sharply reduced time-on-problem and also reduced knowledge
built.

**Grade: Low–Moderate.** Preprint, not peer-reviewed at time of writing; I could not confirm
sample size or design details from the accessible text. Included as *corroborating direction*
only — do not quote a number from it.

---

**Darvishi, Khosravi, Sadiq, Gašević & Siemens (2024)**, "Impact of AI assistance on student
agency," *Computers & Education* 210, 104967.
<https://www.sciencedirect.com/science/article/pii/S0360131523002440>

Large-scale study of AI scaffolding in a peer-review platform. Reported pattern: AI
assistance produced reduced self-regulatory monitoring and increased dependence.

**Grade: Moderate, with an access caveat.** Full text was paywalled to this research pass;
the finding is reported second-hand from abstracts and citing literature. The commonly cited
"performance dropped when the AI was withdrawn" framing is **not independently verified here**
— treat that specific claim as unconfirmed and rely on Bastani et al. (already locked) for
the withdrawal effect.

---

### 1.2 The one strong positive result, and why it doesn't say what people think

**Kestin, Miller, Klales, Milbourne & Ponti (2025)**, *Scientific Reports* — Harvard
Physical Sciences 2, ~194 students, within-subject crossover: each student learned one topic
in a highly refined active-learning class and another at home with a custom tutor ("PS2 Pal").
Students learned roughly twice as much with the AI tutor, in less time.
<https://hechingerreport.org/proof-points-ai-tutor-harvard-physics/> ·
<https://news.harvard.edu/gazette/story/2024/09/professor-tailored-ai-tutor-to-physics-course-engagement-doubled/>

Read the design before the headline. The tutor was:
- constrained to a few sentences per turn, explicitly to avoid cognitive overload;
- instructed to give **one step at a time** and **never the full solution**;
- built on expert-authored scaffolds against a specific, well-mapped curriculum;
- evaluated on an **immediate post-test**, with no delayed retention measure reported.

**Grade: Moderate** for the claim *"a tightly guardrailed, curriculum-specific AI tutor can
beat classroom time on an immediate post-test."*
**Grade: Not supported** for the claim *"using ChatGPT helps you learn."* Those are different
interventions. The active ingredient tested here is the constraint set, not the model.

This is the strongest available empirical support for the rule already locked in
`DECISIONS.md` §8 — hints, one step, never the answer.

---

### 1.3 The meta-analyses: treat with hostility

| Source | Headline | Status |
|---|---|---|
| **Wang & Fan (2025)**, *Humanit Soc Sci Commun* 12:621 — 51 studies, g = 0.867 learning performance, 0.456 perception, 0.457 higher-order thinking | "Large positive effect" | **RETRACTED 2026-04-22.** Retraction note: <https://www.nature.com/articles/s41599-026-07310-z>. Reasons reported: discrepancies in the meta-analysis; pooling of studies too different in method and sample to combine; implausible that dozens of high-quality studies existed in the covered window. Authors did not respond. Coverage: <https://www.govtech.com/education/nature-retracts-oft-cited-paper-on-positive-impact-of-chatgpt>, <https://www.plagiarismtoday.com/2026/07/15/study-claiming-ai-helps-students-learn-retracted/> |
| **Liu et al. (2025)**, *J Computer Assisted Learning* 41(4):e70096 — 37 studies, g = 0.577 | "Moderate positive effect" | Live, but: largest effects found at **n = 21–40** — the classic small-study/publication-bias signature; larger effects for *declarative* than procedural knowledge; 5–10 week interventions strongest. <https://onlinelibrary.wiley.com/doi/10.1111/jcal.70096> |
| **Deng, Jiang, Yu, Lu & Liu (2025)**, *Computers & Education* 227:105224 — 69 experimental studies | "Strong positive effects on achievement, affect, higher-order thinking"; weak/inconsistent for self-efficacy and mental effort | Live. Same structural problem as the others. |

**The structural problem all three share:** the pooled outcome is overwhelmingly *performance
measured while, or immediately after, the AI was available.* The primary RCTs in §1.1 show
that measure is exactly the one that inflates while learning doesn't move. A meta-analysis of
the wrong dependent variable produces a confident number about nothing.

**Grade for "AI use improves learning, g ≈ 0.6–0.9": Low.** Not because the studies are
fraudulent, but because the construct is mis-measured and the flagship synthesis was
retracted for methodological failure. This is the same *citation-laundering* pattern the 10x
audit already named — real effect sizes, wrong boundary conditions, stacked into a headline.

### 1.4 Two widely circulated results that should NOT be leaned on

**Kosmyna, Hauptmann, Yuan, Situ, Liao, Beresnitzky, Braunstein & Maes (2025)**, "Your Brain
on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing
Task," arXiv:2506.08872. <https://arxiv.org/abs/2506.08872> ·
<https://www.media.mit.edu/publications/your-brain-on-chatgpt/>

n = 54 across sessions 1–3, **n = 18** in the critical session 4. EEG showed weaker
distributed connectivity in the LLM group; essays were judged homogeneous and "soulless."

**Grade: Low.** Preprint, tiny critical-session sample, and — the important part — **EEG
connectivity is not a learning outcome.** "Less brain connectivity" is not the same claim as
"learned less," and the term "cognitive debt" is the authors' coinage, not a measured
construct. This paper went viral precisely because its framing is quotable. Its *direction*
agrees with the better studies above; its *evidence* should not be cited as support for
anything. Do not put it in the design doc.

**Gerlich (2025)**, "AI Tools in Society: Impacts on Cognitive Offloading and the Future of
Critical Thinking," *Societies* 15(1):6. <https://doi.org/10.3390/soc15010006>

n = 666, survey + interviews. Negative correlation between AI tool use and critical-thinking
scores, mediated by self-reported cognitive offloading.

**Grade: Low.** Cross-sectional, correlational, self-report on both sides of the
relationship, no causal identification, and a **published Correction** exists
(<https://www.researchgate.net/publication/395511406>). Reverse causation (people with weaker
critical-thinking habits use AI more) is entirely unexcluded. Widely cited on LinkedIn as
proof AI makes you stupid. It is not that.

---

## 2. What Scholars Actually Recommend for Personal Use

Ranked by how much the evidence behind them is *AI-specific* versus *borrowed from general
learning science and extrapolated*. That distinction is the whole point of this section.

### 2.1 Take notes *alongside* the AI, never instead of it — **High**

The only personal-usage practice in this brief with a direct, pre-registered RCT behind it.
Kreijkes et al. (2025): note-taking + LLM matched note-taking alone and both beat LLM alone
at a three-day delay. The AI is allowed to make the passage comprehensible; the note is what
makes it yours. This is a *generation* requirement bolted onto a *comprehension* tool.

**Applies to this build directly:** it is the missing operating rule for Gemini Notebook.
`DECISIONS.md` §8 says what Gemini may do; it does not yet say what *you* must do while it
does it.

### 2.2 Attempt first, ask second — **High** (principle), **Moderate** (AI-specific)

Retrieval practice and the generation effect are already the universal layer of this system
(Dunlosky et al. 2013 — locked). The AI-specific application is: produce your own answer,
prediction, or explanation *before* opening the chat, then use the AI to check it. Bastani
et al. (PNAS 2025) and Kestin et al. (2025) both show the guardrail that makes AI help work
is *withholding the answer until the learner has committed to one*.

The extrapolation step — that a learner can reliably impose this on themselves without an
external system — is **untested**. Which is the argument for the Examiner existing at all.

### 2.3 Use AI to generate *questions*, not *explanations* — **Moderate**

The underlying technique (retrieval practice) is the highest-graded thing in this project's
evidence base. The AI's role here is generation-at-scale, not teaching, and the failure mode
is quality rather than dependency.

Direct evidence is thin: **Xu et al. (2025)**, "Enhancing Student Learning with LLM-Generated
Retrieval Practice Questions," arXiv:2507.05629 <https://arxiv.org/abs/2507.05629>, reports
89% vs. 73% retention accuracy in weeks with vs. without LLM-generated MCQs in data-science
courses — but this is a within-course week-to-week comparison, not a randomised design, and
the authors themselves state instructors **must manually verify and revise** generated
questions before release.

**Grade: Moderate** for the practice; **Low** for the specific 89%/73% figures. This directly
supports `DECISIONS.md` §11 item 6 (LLM card generation *with mandatory human review*) — the
mandatory-review clause is not bureaucratic caution, it is the finding.

### 2.4 Explain it back closed-book, then let the AI grade the explanation — **Moderate**

Self-explanation is a well-established effect in its own right (Chi's work; Bisra et al. 2018
meta-analysis, g ≈ 0.55) and this project already mandates verbal explain-back as the
integration gate (`DECISIONS.md` §3). The AI-as-checker variant is a natural fit and is what
the Examiner is.

**Honest labelling: the AI-as-grader-of-self-explanation configuration has no efficacy RCT.**
It is a well-motivated extrapolation from two solid literatures, not a validated practice.
The evidence-before-verdict structure in §9 is a hedge against the known failure mode
(lenient grading), not proof the configuration works.

### 2.5 Test yourself unassisted, at a delay — **High** (principle), **untested** (as habit)

Every study in §1.1 that found a null did so because it measured at a delay, without the tool.
Every study that found a large effect measured immediately, with it. The practical corollary
for a solo learner: **any self-assessment made during or right after an AI session is
uninformative.** The only signal that means anything is unassisted recall days later.

This is the same logic that already makes 30-day retention one of the two honest metrics in
`DECISIONS.md` §6. It now has an additional, AI-specific reason to exist.

### 2.6 Do not rely on "being aware of the risk" as the safeguard — **Moderate**

Worth stating because it is the most common piece of advice given. The offloading literature
(Fan et al. 2025; and the metacognitive-laziness measurement work, **Dizon, Mendoza, Gasevic
& Ganotice, 2026**, "Assessing AI-Driven Metacognitive Offloading," <https://journals.sagepub.com/doi/10.1177/20965311261450994>)
converges on the view that **fostering metacognitive awareness is not by itself a sufficient
safeguard** — the failure is motivational and structural, not informational. Knowing that
asking for the answer will hurt you does not stop you from asking for the answer at 9pm when
you're tired.

Structural constraints beat good intentions. That is an argument for the tool boundary being
enforced by *which app you open*, not by willpower inside one chat window.

---

## 3. ADHD, Dyslexia, and Executive-Function Constraints: The Gap Is Still Open

**Verdict: Not covered.** There is no controlled study measuring learning or retention
outcomes for AI-assisted studying in ADHD or dyslexic adults. This confirms, rather than
updates, `2026-08-08_prior-art.md`.

What actually exists, and what each one is *not*:

| Study | What it is | What it does not show |
|---|---|---|
| **Carik, Ping, Ding & Rho (2025)**, "Exploring Large Language Models Through a Neurodivergent Lens," *ACM GROUP 2025*, arXiv:2410.06336 <https://arxiv.org/abs/2410.06336> | Qualitative thematic analysis of 1,653 coded Reddit data points across 61 neurodivergent subreddits (autism, ADHD, social anxiety, dyslexia), Nov 2022 – Jan 2024, κ = 0.82 | **No learning outcomes measured.** Self-reported perception and usage only |
| **Fung et al. (2026)**, ChatGPT-assisted writing system ("CHATTING") for students with dyslexia, *ECNU Review of Education* <https://journals.sagepub.com/doi/10.1177/20965311251358269> | n = 101, experimental vs. traditional class; improved behavioural/emotional engagement and intrinsic motivation | **Engagement and motivation, not learning or retention.** Children, writing task, L2 context |
| **ADHD-education LLM comparisons** (ChatGPT-5 vs DeepSeek V3 vs Grok 4), *PLOS One* 2025 <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335335> | Evaluates the *accuracy of model output* about ADHD against DSM-5 | Says nothing about whether an ADHD learner using the model learns anything |
| **Dyslexia/dyscalculia Q&A quality**, *Psychiatric Quarterly* 2025 <https://link.springer.com/article/10.1007/s11126-025-10170-6> | Rates answer quality/reliability | Same — output quality, not learner outcome |

Two findings from Carik et al. that are genuinely useful *as design input* (not as evidence
of efficacy):

- **Text-centric interaction was the dominant dyslexia complaint (72.7% of dyslexia-related
  challenges).** One quoted user: *"We still need to read responses from ChatGPT, so I am not
  sure if it is helpful."* A chatbot that answers in prose hands a dyslexic reader a
  decoding task as the reward for asking a question. This is a real, specific,
  population-relevant friction that generic AI-learning advice never mentions — and it is a
  strong argument for the audio-overview accommodation already locked in `DECISIONS.md` §7.
- **Prompting frustration was the top ADHD complaint (52% of ADHD discussions).** The
  overhead of composing a good prompt is itself an executive-function tax. A saved,
  pre-written Examiner invocation removes a barrier that the general literature doesn't know
  exists.

### The extrapolation trap — both directions are speculative

Two plausible, opposite arguments exist and **neither has evidence**:

1. *"AI should help ADHD/dyslexic learners more"* — because it reduces extraneous cognitive
   load and decoding burden, and both channels are impaired (verbal WM d ≈ 0.55, visuospatial
   d ≈ 0.49, already in `DECISIONS.md` §3).
2. *"AI should hurt ADHD learners more"* — because the offloading failure is a
   self-regulation failure, and this is a population with a documented self-regulation
   constraint. A tool that removes the effort signal is most dangerous to the learner least
   able to reinstate it.

Both are reasoning-by-analogy. **Do not write either into the design doc as a finding.** The
honest position: the mechanism arguments cut both ways, the population is understudied, and
this system should therefore be built to *measure* which one is true for Orlando specifically
rather than assume.

There is a weak, non-population-specific hint that the second argument deserves the
precedence: the prior-art brief's CSAL AutoTutor finding (n = 252) that **adaptivity without
a floor amplifies the gap for the lowest-skill learners**. That is already locked as the
floor rule. It is consistent with, but not evidence for, the ADHD-specific version.

---

## 4. Documented Failure Modes, With Citations

| # | Failure mode | Evidence | Grade |
|---|---|---|---|
| 1 | **Performance–learning dissociation.** The output improves; the knowledge doesn't | Fan et al. 2025 (essay score ↑, knowledge gain/transfer n.s.); Bassner et al. 2026 (exercise scores ↑, conceptual learning flat); Kreijkes et al. 2025 (LLM-only loses at 3-day delay) | **High** — three independent replications, different domains |
| 2 | **Preference inversion.** Learners prefer and rate as more helpful the method that teaches them less | Kreijkes et al. 2025 (most students preferred the LLM). Precedent outside AI: Deslauriers et al. (PNAS 2019) — students *felt* they learned less in active learning while learning more | **High** |
| 3 | **Metacognitive laziness / offloading of self-regulation.** Goal-setting, error monitoring, and strategy selection get handed to the AI | Fan et al. 2025 (names and measures the construct); Dizon et al. 2026 (scale development); Darvishi et al. 2024 | **Moderate–High** |
| 4 | **Erosion of unassisted performance.** Practice scores rise while the ability to perform without the tool falls | Bastani et al., PNAS 2025 — **already locked, `DECISIONS.md` §8** | **High** |
| 5 | **Fluency illusion.** AI prose is maximally fluent; perceived fluency is a known driver of inflated judgments of learning, independent of actual retention (Bjork/Koriat metamemory work) | Established metamemory literature; the AI-specific application is described but not experimentally isolated in the studies above | **Moderate** (principle High, AI-specific isolation not yet demonstrated) |
| 6 | **Hallucinated material entering the study set.** A wrong flashcard is worse than no flashcard, because spaced repetition will drill it | Xu et al. 2025 explicitly requires manual verification; hallucination rates are covered in this repo's existing tutor-landscape brief | **High** (as a design risk) |
| 7 | **The evidence base itself is unreliable.** The flagship supporting meta-analysis was retracted; surviving ones show small-study bias | Wang & Fan 2025 retraction note (2026-04-22); Liu 2025 moderator pattern | **High** |
| 8 | **The "comfort trap."** Unrestricted AI lowers frustration and cognitive load — which feels like the system working, and is the mechanism of the problem | Bassner et al. 2026 (their term) | **Moderate** |

Note the shape of #8 against this repo's locked architecture: the Paas 7–9 floor exists to
*catch overload*. Nothing currently catches **underload** — the session that felt smooth,
fast, and productive because the AI did the thinking. Both are failure states. Only one is
currently instrumented.

---

## 5. Who to Actually Listen To

### Credible — publish peer-reviewed work specifically on human–AI *learning* interaction

| Person / group | Affiliation | Why they count |
|---|---|---|
| **Dragan Gašević** | Centre for Learning Analytics, Monash | Senior author on the metacognitive-laziness line (Fan et al. 2025) and on Darvishi et al. 2024. Publishes nulls |
| **Yizhou Fan** | Peking University | Lead author, Fan et al. 2025 |
| **Hamsa Bastani & Osbert Bastani** | Wharton / Penn | Bastani et al. PNAS 2025 — the guardrail finding already locked here |
| **Gregory Kestin** | Harvard Physics | Kestin et al. 2025 — designed and RCT'd a constrained tutor; publicly attributes the result to the constraints, not the model |
| **Pia Kreijkes & Tim Oates** (Cambridge Univ Press & Assessment) with **Jake Hofman, Daniel Goldstein, Lev Tankelevitch, Abigail Sellen, Sean Rintel** (Microsoft Research) | — | The 405-student pre-registered RCT. Pre-registration in this field is rare enough to be a credential by itself |
| **Hassan Khosravi** | University of Queensland | Learner agency and AI scaffolding |
| **Ryan S. Baker** | Penn Center for Learning Analytics | Long pre-LLM track record in learning analytics; a check on hype from inside the field |
| **René Kizilcec** | Cornell, Future of Learning Lab | Co-leads the National Tutoring Observatory / Million Tutoring Moves dataset |
| **Kenneth Koedinger** | CMU HCII / LearnLab | Decades of ITS work predating LLMs; the reason "intelligent tutoring" has a real evidence base to compare LLMs against |
| **Robert & Elizabeth Bjork** | UCLA Learning & Forgetting Lab | Desirable difficulties, metamemory, judgments of learning. **Not AI researchers** — but the framework that explains every result in §1 |
| **Michelene Chi** | Arizona State | Self-explanation and the ICAP framework — the theory behind "explain it back" |

### Practitioner-only — real credentials, useful heuristics, no efficacy data

- **Ethan Mollick & Lilach Mollick**, Wharton Generative AI Labs. Their published AI tutor
  and practice-generation prompts are explicitly grounded in learning-science principles and
  are among the most sensible material in circulation. **They have not been tested against
  learning outcomes**, and the Mollicks generally say so themselves. Use as design heuristics.
  Do not cite as evidence.

### Hype — apply the same filter as the 10x audit

Anything whose primary claim is a multiplier ("learn 10x with AI"), any "second brain" prompt
pack, any LinkedIn/YouTube framing that uses "neuroscience" or "how geniuses learn" as a
credential, and any tool citing Wang & Fan (2025) — which is now retracted and will keep
circulating for years. **A retracted g = 0.867 is the highest-quality-looking citation
available to a marketer**, so expect to see it a lot.

The 10x audit's three-part pattern applies unchanged here: (1) a real narrow effect exists
nearby, (2) it is generalised past its boundary conditions, (3) it is restated as a
multiplier. Section 1.3 is that pattern happening inside peer review.

---

## 6. What This Means — For This Build, and For Orlando's Own AI Habits

### 6.1 Nothing here changes a Locked decision. Three get stronger.

- **§8, tool boundary ("Gemini helps you learn it. Claude decides whether you know it.")** —
  now supported by four more studies, not one. The line was drawn on Bastani alone; it now
  has Fan, Bassner, Kreijkes, and Kestin behind it. Keep it exactly as written.
- **§11 item 6, LLM card generation with mandatory human review** — upgrade the framing from
  cautious-practice to research-backed requirement. The one study of LLM-generated retrieval
  questions says the same thing in its own limitations section.
- **§6, the two honest metrics (repetitions-to-criterion and 30-day retention)** — this
  literature is essentially a series of demonstrations that any *other* metric lies. Studies
  measuring immediate/assisted performance find large effects; studies measuring delayed
  unassisted recall find nulls. The metric choice was already right; now it has a second,
  independent justification.

### 6.2 Three things to add to Queued

**Q10 — A "notes alongside" rule for Gemini sessions.** §8 specifies what Gemini may do.
It does not specify what Orlando must do while it does it. Kreijkes et al. is the single
strongest study in this brief and its finding is a *user habit*, not a system feature: an
audio overview or grounded Q&A session must produce a written artefact in the vault, in his
own words, or the session doesn't count as study time. This also happens to fix the known
Gemini→vault export seam (§12 item 3) as a side effect, because the artefact is authored in
the vault rather than exported from Google.

**Q11 — Instrument underload, not just overload.** The Paas 7–9 floor catches "too hard."
Nothing catches "suspiciously easy." Bassner's comfort trap is a session where effort ratings
are low, output is good, and nothing was learned. A one-line prompt at session end — *did I
produce the answer before I saw it?* — is roughly free and targets the only failure mode this
architecture currently can't see.

**Q12 — Delayed unassisted check as a distinct event.** Every null in this literature came
from a delayed, tool-free test. The Examiner currently gates at the end of a learning loop.
Consider a separate, later, tool-free re-check — not a new Anki review (that's recognition
under cue) but a cold explain-back with no vault, no chat, no notes open. This is the only
measurement in the whole system that the research says is trustworthy.

### 6.3 For Orlando's own habits — plain language

1. **Whatever the AI explains, write it down in your own words before you move on.** This is
   the only recommendation in this brief with a pre-registered RCT behind it. Not a summary
   the AI generates — one you generate. This is the single highest-value change.
2. **Answer before you ask.** Say or type your guess first, even a bad one, then open the
   chat. The one Harvard study where AI genuinely beat a good classroom used a tutor that
   was *forbidden* from giving the answer until the student had tried.
3. **Distrust the feeling of a good session.** The clearest finding in this whole literature
   is that the sessions that feel best are the ones that teach least, and that learners can
   describe the tradeoff accurately and still pick wrong. Smooth, fast, and frictionless is a
   warning sign, not a success signal.
4. **Never judge whether you learned something on the same day you learned it.** Assisted or
   same-day self-assessment is uninformative. Days later, closed-book, is the only read that
   means anything.
5. **Use AI to make questions more than to make explanations.** Explanations are where the
   dependency forms. Questions put the work back on you — but check every generated card
   before it enters the queue, because spaced repetition will faithfully drill a wrong one.
6. **Don't rely on knowing all this.** Awareness isn't the safeguard — the research is
   explicit that metacognitive awareness alone doesn't prevent offloading. That's what the
   tool boundary is for: the constraint should live in *which app is open*, not in your
   resolve at 9pm.

### 6.4 What is honestly unknown for this specific profile

- Whether any of the above holds for an ADHD + dyslexic adult. **No study has asked.** The
  mechanism arguments point in opposite directions and neither has been tested.
- Whether reduced decoding load from audio/AI explanation is a net gain for a dyslexic
  learner (load reduction is real, d ≈ 0.35 for TTS per §7) or a net loss (it removes the
  generative work). Genuinely open.
- Whether a self-imposed "answer first" rule is sustainable without external enforcement for
  a learner with an executive-function constraint. This is the assumption the whole Examiner
  design rests on, and it is an assumption.

The correct response to all three is not to guess — it's that this system already logs
repetitions-to-criterion and 30-day retention against Orlando's own baseline. That makes him
an n-of-1 study on exactly the question the literature hasn't answered. That's not a
consolation prize; given the state of the field, it's better data than the field has.

---

## 7. Addendum — Verifying a Specific Claimed Source ("Oxford Researchers Discovered…")

**Trigger:** YouTube video, *"Oxford Researchers Discovered How to Use AI To Learn Like A Genius"*
(channel: Python Programmer), <https://www.youtube.com/watch?v=TPLPpz6dD3A>. A transcript
check flagged that it names no researcher and links no study. This section traces its actual
sources and grades each on the correct tier.

**Bottom line: the underlying Oxford material is real, and it is not research.** It is
institutional student guidance plus one small internal case study reporting student
self-report. Four of the five practices it describes do have real research behind them —
just not *that* research, and with an important correction to one of them. The word
"Discovered" in the title is doing all the work; nothing was discovered.

### 7.1 The Oxford source, correctly identified and tiered

| Page | What it actually is | Tier |
|---|---|---|
| **"Generative AI tools"**, Oxford student academic-skills guidance <https://www.ox.ac.uk/students/academic/guidance/skills/ai-study> | University study-skills advice page for students. Recommends AI to break down complex concepts, organise notes/learning plans, and build custom bots for practice activities; recommends generating **practice questions with sample responses for independent self-assessment** | **Institutional guidance** |
| **"Getting started with AI for students"**, Oxford AI Competency Centre / e-Research Centre <https://oerc.ox.ac.uk/ai-centre/ai-guides/getting-started-with-ai-for-students> | Prompt-recipe guide: transform notes into tables/mind maps/timelines, generate flashcards, extract key concepts by theme, build study timetables. Explicitly warns never to trust AI on numbers, dates, statistics, references, or quotations. **No research citations on the page.** | **Institutional guidance** |
| **"AI for Learning: Helping Foundation Year Students in the Physical Sciences use ChatGPT Effectively"**, Oxford Centre for Teaching and Learning <https://www.ctl.ox.ac.uk/ai-for-learning> (redirects as of this pass; content confirmed via Oxford's own GenAI case-studies index <https://www.ox.ac.uk/gen-ai/case-studies>) | The closest thing to a "study." An Astrophoria Foundation Year cohort used ChatGPT Edu as a **Socratic tutor** — students asked it to guide them step by step and answer questions themselves rather than be given solutions, deliberately mimicking the Oxford tutorial style. Presented at Oxford's AI in Teaching and Learning Knowledge Exchange Forum, Saïd Business School, 2025-07-09 | **Institutional case study / practitioner report** |

**What the CTL case study actually measured:** students reported revision felt "more like a
dialogue than solitary reading," that it gave quick feedback when tutors weren't available,
and that it sustained motivation during long sessions; **all students said they'd want to
keep access.** Those are engagement, motivation, and satisfaction measures.

**Grade: Practitioner-only / institutional.** Small cohort, no control group, no learning or
retention outcome, self-report only. It is *reasonable* guidance from a *credible*
institution — those are both true and worth something. Neither makes it evidence.

And note the trap: "all students would want to keep access" is exactly the metric Kreijkes et
al. (§1.1) showed points the wrong way. Learner-preference data from an AI-tool trial is the
one thing this literature says not to trust. Oxford's guidance page isn't claiming otherwise
— the video is.

**Why the video's framing fails this repo's standard:** "Oxford researchers discovered"
implies a finding, a method, and an author. There is no finding (nothing was measured), no
discovery (Socratic questioning as a tutoring method predates Oxford, let alone LLMs), and no
named researcher. This is the citation-laundering pattern from `2026-08-09_10x-learning-claims-audit.md`
§2, one tier lower: instead of inflating a real effect size, it borrows an institution's
credibility for a page that makes no empirical claim at all. **"Learn Like A Genius" in a
title is a reliable negative signal about sourcing, and it was here.**

### 7.2 The "CLEAR principle" — real, correctly attributed, and modest

**It is real, and it is not Cambridge's.** Original source:

> **Lo, L. S. (2023).** "The CLEAR path: A framework for enhancing information literacy
> through prompt engineering." *The Journal of Academic Librarianship* 49(4), 102720.
> <https://www.sciencedirect.com/science/article/abs/pii/S0099133323000599> ·
> open copy: <https://digitalrepository.unm.edu/ulls_fsp/211/>

Five principles for writing prompts: **C**oncise, **L**ogical, **E**xplicit, **A**daptive,
**R**eflective. Cambridge University Library reproduces it in their LibGuides
(<https://libguides.cam.ac.uk/AI/results>, <https://libguides.cam.ac.uk/wolfsoncollege/academic-ai>),
as do Texas A&M–Corpus Christi and others. So the video's "Cambridge Library resource" exists
— but it's Cambridge *citing Lo*, not Cambridge originating anything.

**Grade: Practitioner framework, peer-reviewed venue, no efficacy data.** It is a *conceptual*
framework published in a library-science journal, not an experiment. Nobody has tested whether
CLEAR-shaped prompts produce better learning than un-shaped ones. Its provenance is clean and
its advice is sensible; it is a writing heuristic, not a learning intervention.

**Worth citing?** Marginally, and only for what it is. This repo already has
`2026-08-10_prompt-engineering-best-practices.md`, which covers the same ground with more
rigour. CLEAR's one genuinely useful contribution here is the **R — Reflective** step
(evaluate the output, iterate), which is the only part that touches learning rather than
output quality. Not worth a decision entry.

### 7.3 The five claimed practices, checked independently

Checked against the literature in §§1–2 of this brief, not against the video's framing. Three
hold up, one holds up with a **significant correction**, and one is weaker than it sounds.

**(1) Socratic questioning — AI asks guiding questions instead of answering. → Supported, and it's the single most important one.**
This is the only practice on the list with converging *experimental* support: Bastani et al.
(PNAS 2025, locked in `DECISIONS.md` §8) and Kestin et al. (2025, §1.2), where the tutor was
explicitly forbidden from giving a full solution and constrained to one step per turn.
Oxford's case study arrived at the same design by intuition and tutorial tradition; the RCTs
are why it's right. **Grade: High.** Note the direction of dependence — the good idea is not
Oxford's, and it doesn't need Oxford to be true.

**(2) Multi-level explanations — have AI explain at child / high-schooler / academic level. → CORRECTION: this is backwards.**
This is the one to be careful about, and the video gets it the wrong way round.

The robust finding is that **you** should generate the explanation, not read one. Bisra, Liu,
Nesbit, Salimi & Winne (2018), "Inducing Self-Explanation: a Meta-Analysis," *Educational
Psychology Review* 30(3) — 64 reports, 69 effect sizes, **g = 0.55**
<https://link.springer.com/article/10.1007/s10648-018-9434-x>. The related, widely reported
contrast in that literature is that **self-explanation often outperforms being given an
explanation**. The learning-by-teaching / protégé literature points the same way (Kobayashi's
meta-analysis of ~39 experiments; not primary-verified this pass) — the gain comes from *the
act of producing the simplified explanation*, which is precisely the work you hand to the
model when you ask it to explain like you're five.

**Reversed, it becomes one of the best practices available:** *you* explain the concept at a
child's level, out loud or in writing, and then ask the AI to find what you got wrong or left
out. That is self-explanation (g = 0.55) plus a checker, and it is exactly the shape of this
project's integration gate (`DECISIONS.md` §3) and Examiner.

**Grade: Low as stated in the video** (AI-generated multi-level explanations are a
comprehension aid, and comprehension aids are what produced the nulls in §1.1).
**Grade: Moderate–High when inverted** (High for the underlying self-explanation effect;
the AI-as-checker layer remains untested).

**(3) AI-generated practice questions with assessment. → Supported, with the review clause.**
Covered in §2.3. Retrieval practice is the highest-graded technique in this project's whole
evidence base; the AI's role is generation-at-scale. Oxford's own page adds the right
refinement — practice questions *with sample responses so students can self-assess*. The
non-negotiable caveat stands: hallucinated questions get faithfully drilled by FSRS, so
mandatory human review (`DECISIONS.md` §11 item 6) is a requirement, not caution.
**Grade: Moderate.**

**(4) Retrieval-practice framing. → Supported, and it isn't Oxford's or AI's.**
Dunlosky et al. (2013) is already the universal layer of this system (`DECISIONS.md` §2). It
predates LLMs by decades. Nothing about AI changes the underlying effect; AI changes only
*who writes the questions*. Presenting retrieval practice as an AI discovery is the "real
narrow effect exists nearby" step of the 10x audit's pattern.
**Grade: High for the technique, not attributable to this source.**

**(5) Structured reading support — concept lists, proposition tables. → Half right, and the half matters.**
There is a real, well-sized literature here, and it contains the exact distinction the video
elides. Schroeder, Nesbit et al. (2018), "Studying and Constructing Concept Maps: a
Meta-Analysis," *Educational Psychology Review* — 142 effect sizes, n = 11,814, overall
**g = 0.58** <https://link.springer.com/article/10.1007/s10648-017-9403-9>.

The moderator result is the useful part:

| Activity | Effect |
|---|---|
| **Constructing** the map yourself | **g = 0.72** |
| **Studying** a map someone else made | **g = 0.43** |

Asking an AI to produce your concept list or proposition table puts you in the **weaker**
condition — you've traded g = 0.72 for g = 0.43 in exchange for saving time. That's not
nothing, and for a learner facing a decoding burden it may be a defensible trade on dense
primary material. But it is a *known, quantified* downgrade, not a free win, and this is the
clearest number in the entire brief for what cognitive offloading costs.

**Grade: High** for the effect and the construct/study split. **Moderate** for the practice as
the video frames it, with the explicit caveat that the AI-generated version is the weaker
half. Practical form: let the AI produce a *skeleton* (headings, term list) and fill in the
relations yourself — the relations are where the g = 0.72 lives.

### 7.4 What this adds to §6

Nothing here changes a decision. Two refinements to Orlando's habit list:

- **Habit 1 gets sharper.** "Write it down in your own words" now has a number attached: for
  structured artefacts specifically, building it yourself is g = 0.72 vs g = 0.43 for reading
  one the AI built. When Gemini produces a summary or concept list from a dense F&I source,
  the version that counts is the one Orlando re-derives into the vault.
- **A new habit 7 — invert the "explain it simply" move.** The popular advice is to ask AI to
  explain like you're five. The research says do the opposite: *you* explain it at a
  five-year-old's level first, then ask the AI what you missed. Same conversation, opposite
  direction of work, and it's the difference between g ≈ 0 and g ≈ 0.55.

### 7.5 Standing filter for sourced-from-a-video claims

This one resolved cleanly because the underlying institution was real. The general test, in
order:

1. **Is there a named researcher?** No name → no study. "Oxford researchers" is not a name.
2. **Is there a paper, or a webpage?** A `.ac.uk` guidance page is institutional advice.
   Credible tier, different tier.
3. **What was measured?** If the outcome is satisfaction, engagement, motivation, or "would
   want to keep access," it is *not a learning finding* — and per Kreijkes et al., those
   measures reliably point away from learning.
4. **Does the title contain a multiplier or a genius claim?** Treat as a negative signal
   about the sourcing beneath it. It was correct here.

Applied to this video: fails (1), reveals (2) as institutional guidance, (3) is satisfaction
data, (4) fails. **Verdict: not a research source.** Four of its five practices are
nonetheless real, because they were real before the video and are documented above from their
actual primary sources.

---

## Sources

- Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., & Gašević, D. (2025). Beware of metacognitive laziness. *BJET* 56(2), 489–530. <https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544> · <https://arxiv.org/abs/2412.09315>
- Kreijkes, P., Kewenig, V., Kuvalja, M., Lee, M., Vitello, S., Hofman, J. M., Sellen, A., Rintel, S., Goldstein, D. G., Rothschild, D. M., Tankelevitch, L., & Oates, T. (2025). Effects of LLM use and note-taking on reading comprehension and memory. *Computers & Education*. <https://www.sciencedirect.com/science/article/pii/S0360131525002829> · <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5095149>
- Bassner, P., Lenk-Ostendorf, B., Beinstingel, R., Wasner, T., & Krusche, S. (2026). Less stress, better scores, same learning. *Computers and Education: AI* 10. <https://www.sciencedirect.com/science/article/pii/S2666920X25001778>
- Darvishi, A., Khosravi, H., Sadiq, S., Gašević, D., & Siemens, G. (2024). Impact of AI assistance on student agency. *Computers & Education* 210, 104967. <https://www.sciencedirect.com/science/article/pii/S0360131523002440>
- Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning. *Scientific Reports*. <https://hechingerreport.org/proof-points-ai-tutor-harvard-physics/>
- Wang, J., & Fan, W. (2025). **RETRACTED.** *Humanit Soc Sci Commun* 12:621. Retraction note (2026-04-22): <https://www.nature.com/articles/s41599-026-07310-z> · original: <https://www.nature.com/articles/s41599-025-04787-y>
- Liu, S. et al. (2025). The Impact of ChatGPT on Students' Academic Achievement: A Meta-Analysis. *JCAL* 41(4):e70096. <https://onlinelibrary.wiley.com/doi/10.1111/jcal.70096>
- Deng, R., Jiang, M., Yu, X., Lu, Y., & Liu, S. (2025). Does ChatGPT enhance student learning? *Computers & Education* 227, 105224.
- Rismanchian, S., Uzun, H., Matayoshi, J., Cosyn, E., & Kurd-Misto, E. (2026). Faster Completion, Less Learning. arXiv:2605.21629. <https://arxiv.org/abs/2605.21629>
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT. arXiv:2506.08872. <https://arxiv.org/abs/2506.08872>
- Gerlich, M. (2025). AI Tools in Society. *Societies* 15(1):6. <https://doi.org/10.3390/soc15010006> (see published Correction)
- Dizon, J. I. W. T., Mendoza, N. B., Gasevic, D., & Ganotice, F. A. (2026). Assessing AI-Driven Metacognitive Offloading. <https://journals.sagepub.com/doi/10.1177/20965311261450994>
- Xu et al. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions. arXiv:2507.05629. <https://arxiv.org/abs/2507.05629>
- Carik, B., Ping, K., Ding, X., & Rho, E. H. (2025). Exploring Large Language Models Through a Neurodivergent Lens. *ACM GROUP 2025*. <https://arxiv.org/abs/2410.06336>
- Fung, K. Y. et al. (2026). A Study on Using ChatGPT to Help Students With Dyslexia. <https://journals.sagepub.com/doi/10.1177/20965311251358269>
- Evaluating LLMs for ADHD Education. *PLOS One* (2025). <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335335>
- LLM quality on dyslexia/dyscalculia questions. *Psychiatric Quarterly* (2025). <https://link.springer.com/article/10.1007/s11126-025-10170-6>
- Retraction coverage: <https://www.govtech.com/education/nature-retracts-oft-cited-paper-on-positive-impact-of-chatgpt> · <https://www.plagiarismtoday.com/2026/07/15/study-claiming-ai-helps-students-learn-retracted/>

**Added for §7 (source verification):**

- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing Self-Explanation: a Meta-Analysis. *Educational Psychology Review* 30(3). 64 reports, 69 effect sizes, **g = 0.55**. <https://link.springer.com/article/10.1007/s10648-018-9434-x>
- Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and Constructing Concept Maps: a Meta-Analysis. *Educational Psychology Review*. 142 effect sizes, n = 11,814; overall **g = 0.58**; constructing **0.72** vs studying **0.43**. <https://link.springer.com/article/10.1007/s10648-017-9403-9>
- Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship* 49(4), 102720. <https://www.sciencedirect.com/science/article/abs/pii/S0099133323000599> · open copy <https://digitalrepository.unm.edu/ulls_fsp/211/> · Cambridge LibGuides reproduction <https://libguides.cam.ac.uk/AI/results>
- University of Oxford, "Generative AI tools" (student academic-skills guidance). <https://www.ox.ac.uk/students/academic/guidance/skills/ai-study>
- University of Oxford AI Competency Centre, "Getting started with AI for students." <https://oerc.ox.ac.uk/ai-centre/ai-guides/getting-started-with-ai-for-students>
- University of Oxford Centre for Teaching and Learning, "AI for Learning: Helping Foundation Year Students in the Physical Sciences use ChatGPT Effectively." <https://www.ctl.ox.ac.uk/ai-for-learning> · index: <https://www.ox.ac.uk/gen-ai/case-studies>
- Video under review (not a source; graded in §7): "Oxford Researchers Discovered How to Use AI To Learn Like A Genius," Python Programmer. <https://www.youtube.com/watch?v=TPLPpz6dD3A>

## Verification notes — read before citing downstream

- **Kreijkes et al.**: exact effect sizes and any lower-attainer moderator were not read from
  the full text this pass. Direction and design are confirmed from the publisher, Microsoft
  Research, and SSRN listings.
- **Darvishi et al. 2024**: paywalled; finding reported second-hand. The "withdrawal" framing
  is **unverified** — use Bastani for that claim.
- **Rismanchian et al.**: preprint, design details unconfirmed. Direction only.
- **Xu et al. 2025**: author list not fully verified; the 89%/73% figures come from a
  non-randomised week-to-week comparison. Do not quote as an effect size.
- **Deng et al. 2025**: cited from reference databases, not the full text.
- **Bisra et al. 2018** self-explanation **g = 0.55** — now verified against the publisher
  record (64 reports, 69 effect sizes). Safe to cite.
- **Schroeder et al. 2018** concept-map figures (g = 0.58 overall; 0.72 construct / 0.43
  study) verified against the publisher record. Safe to cite.
- **Kobayashi** learning-by-teaching meta-analysis (~39 experiments) is cited in §7.3 from
  secondary summaries only. **Not primary-verified** — pin before use.
- **Oxford CTL case study**: the page redirects as of this pass; content was confirmed via
  Oxford's own GenAI case-studies index and search snippets, not the live page. Cohort size
  was not established. Nothing load-bearing rests on it.
