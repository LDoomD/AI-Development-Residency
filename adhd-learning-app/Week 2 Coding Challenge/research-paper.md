# Agentic Workflows and AI Automation: How Software Learned to Decide, and Why UX Designers Need to Understand It

**Author:** [YOUR NAME]
**Course:** Tech Fleet AI Development Residency, Fall/Winter 2026 (Premium Track)
**Instructor:** Morgan Denner
**Date:** October 2026
**Specialization areas:** AI Automation + Advanced Agentic Workflows (combined)

---

## Abstract

This paper explains what agentic workflows and AI automation are, how they
work, and what a person needs to learn to build with them. The two subjects are
treated together on purpose: AI automation is the goal, which is work that
finishes without a person doing it, and agentic workflows are the main method
people use to reach that goal today.

The paper's main argument is that the hard part of this field is not getting
software to act on its own. That part is now fairly easy. The hard part is
deciding how much the software should be allowed to decide by itself, and
proving it can be trusted with that much. The paper ends by applying these
ideas to the application being built for this residency.

---

## A short glossary first

This field is full of jargon, and most of it sounds more complicated than it
is. Here are the words used in this paper, in plain terms.

| Term | What it means |
|---|---|
| **LLM** (large language model) | A program trained on huge amounts of text that predicts what words come next. It is the "brain" in all of this. Claude and GPT are LLMs. |
| **Model weights** | The numbers inside a trained model. The weights *are* the model. |
| **Open-weight model** | A model whose weights you can download and run yourself. |
| **Local model** | An LLM running on your own computer instead of someone else's server. |
| **Inference** | Running a model to get an answer out of it. |
| **Tool** | Something an LLM can use to act on the world: search a database, send an email, read a file. |
| **Tool use** | When an LLM decides to call a tool instead of just writing text. |
| **Workflow** | A system where a human decided the steps in advance, and software runs them in that order. |
| **Agent** | A system where the LLM decides the steps itself, while it is running. |
| **Orchestration** | Managing how multiple steps, tools, or models work together. |
| **MCP** (Model Context Protocol) | A shared standard for connecting an LLM to tools and data, so you don't write custom glue code for every single connection. |
| **Eval** (evaluation) | A test that measures whether an AI system's output is actually good. |
| **Guardrail** | A limit built into a system that stops it from doing something harmful. |
| **Human in the loop** | A design where the software stops and asks a person before continuing. |
| **VPS** (virtual private server) | A computer you rent in a data center and control yourself. |
| **API** | A door a company opens so other software can ask its systems questions. |

---

## 1. Introduction to the Subject

### 1.1 Automation used to be dumb, and that was fine

Automation is not new. People have been writing scripts to do boring work for
fifty years.

But old automation had one defining trait: **it could not think.** Imagine a
script that emails you a sales report every Monday. A person decided what goes
in that report. The script just repeats that decision forever. If something
strange shows up in the sales data — a weird refund, a currency that wasn't
expected — the script doesn't notice. It wasn't built to notice. It does the
one thing it was told to do.

This made old automation very predictable. You always knew exactly what it
would do, because somebody wrote down every step ahead of time. It also made it
brittle. The moment reality didn't match the plan, it broke or produced
nonsense.

### 1.2 Then the thing being automated started making choices

LLMs changed this. An LLM can read something it has never seen before and
respond sensibly. When you also give it **tools** — the ability to search a
database, read a file, call an API — something new becomes possible. You can
stop giving the software a *procedure* and start giving it a *goal*.

Anthropic (2024a) named the two designs that result, and this distinction
organizes the whole field:

> "Workflows are systems where LLMs and tools are orchestrated through
> predefined code paths" while agents are "systems where LLMs dynamically
> direct their own processes and tool usage, maintaining control over how they
> accomplish tasks."

In plainer words:

- In a **workflow**, *you* decided the steps. The LLM fills in the blanks.
- In an **agent**, *the LLM* decides the steps while it is running.

Here is a concrete comparison. Say you want to answer customer emails.

**As a workflow**, you write the steps: read the email → sort it into one of
five categories → look up the customer's order → pick the matching reply
template → fill in the details → send. The LLM does the sorting and the filling
in. But the path is fixed. You know exactly what will happen.

**As an agent**, you say: "Answer this customer's email correctly. Here are
your tools: the order database, the refund system, the shipping tracker." The
LLM decides what to look up, in what order, and when it has enough to reply.
Maybe it checks shipping first. Maybe it checks the order twice. You don't know
in advance.

### 1.3 Why this one difference creates every hard problem in the field

The agent version is more flexible. It handles the weird email the workflow
would have mangled.

But look at what you gave up. **You no longer know what your software is going
to do.** A system that picks its own steps can pick a step you never thought
about — including a wrong one, a wasteful one, or a harmful one.

This is the trade at the center of the specialization. More freedom means the
system handles more situations, and also means fewer guarantees about its
behavior. Every genuinely difficult question in this field comes out of that
single trade.

So the real question is never *"can the AI do this?"* Increasingly, it can. The
real question is: **how much should it be allowed to do by itself, and how
would we know if we got that wrong?**

### 1.4 Why these two specializations belong together

**AI automation** is the outcome: work that gets done without a person doing
it. **Agentic workflows** are the method that currently gets you there for
tasks that are too messy to script in advance.

Studying the method without the outcome gives you a clever demo that nobody
uses. Chasing the outcome without understanding the method gives you a system
that works in testing and then does something expensive and surprising in
production. Gartner has forecast that more than 40% of agentic AI projects will
be cancelled by the end of 2027, pointing to rising costs, unclear business
value, and weak risk controls.[^gartner-note] Two of those three causes have
nothing to do with the technology. They are planning failures.

---

## 2. Why This Is Relevant to My Career

I am a UX designer. I have been upskilling in AI — automation first, and now
the deeper layers: agentic systems, LLMs, local AI models, virtual private
servers, and MCP. I am taking this residency because I want to build
enterprise-ready products, not prototypes. The reason is simple: **UX designers
now have to know how to build.**

That is not a prediction. It is already happening, and the data comes from the
UX field's own research body.

### 2.1 My field already adopted these tools

Nielsen Norman Group surveyed 841 UX professionals in July and August of 2023.
They found that "92% of the respondents claimed they had used at least one
generative AI tool," and among those using AI for work, 63% used it at least
several times a week (Liu, Zhang, & Budiu, 2023).

That was three years ago, before agents were practical. Adoption in my field
was effectively total before the technology even got interesting. The question
for a designer today is not whether to use AI. It is whether to understand what
you are using.

### 2.2 The handoff is disappearing, and that is the real change

UX has always worked through a handoff. A designer figures out what should
exist and describes it. An engineer builds it. The description was the
designer's deliverable, and the gap between describing and building was the
reason two roles existed.

Agentic tooling is closing that gap. A person who can describe intent precisely
enough can increasingly produce the working thing. This does not mean
engineering knowledge stops mattering — it means it stops being optional for
designers. If I can build what I design, the limit on my work is no longer
whether someone has capacity to build it. The limit is whether I understand
what I am asking for well enough to be responsible for it.

### 2.3 What I bring that is actually scarce here

The part of this field that is hardest is not writing the code. It is deciding
what the software should be allowed to decide, and designing the moments where
it stops and asks a human.

That is a design problem. Where do you put the approval step? How do you show
someone a decision the AI made so they can judge it and push back? How much
friction protects the user, and how much friction just makes the tool annoying
enough to abandon? These are questions about human judgment under uncertainty,
and UX research is the discipline that studies exactly that.

A system nobody can understand cannot be trusted. A system nobody trusts does
not get to run on its own. So **explainability is not a nice feature added at
the end — it is the thing that decides how much automation you are allowed to
have.** That makes design central to the engineering, not decoration applied
afterward.

### 2.4 What I want to be able to do by the end

I want to take a product from nothing to something real people use: specify it,
build it, deploy it, secure it, and judge honestly whether it works. Not a
mockup, and not a demo that collapses under real data. The specific test I care
about is being able to build something that handles real money or real customer
data, and being able to defend the decisions inside it to someone technical who
disagrees with me.

---

## 3. Background About the Specialization

How the field got here, in four steps.

### 3.1 Step one: scripts that could not think

Classic automation. A human wrote down every step. Reliable and brittle, as
described in §1.1. This is still the right answer for a great many problems,
which is a point worth remembering later.

### 3.2 Step two: models that could read and write

LLMs arrived and could handle language they had never seen before. But early on
they were sealed off. A model could write a beautiful summary of a sales report
you pasted in, and had no way to go get the sales report itself. It could think
but not act.

### 3.3 Step three: tools, and the integration mess

Then models were given tools. This was the real unlock: a model that can both
pick a tool and read the result can be handed a goal instead of a procedure.

But it created a grubby practical problem. Every tool needed custom glue code.
Connecting a model to a database, then Slack, then Google Drive meant writing
three separate integrations, and everyone building agents was writing the same
glue over and over. Anthropic (2024b) described models as "trapped behind
information silos and legacy systems."

### 3.4 Step four: a shared standard

The Model Context Protocol, released 25 November 2024, proposed one standard
way to plug tools and data into AI systems — "a new standard for connecting AI
assistants to the systems where data lives, including content repositories,
business tools, and development environments" (Anthropic, 2024b). Instead of
custom glue per connection, you implement the protocol once.

Something important follows from this. Once connecting things got easy, the
leftover hard problem became **whether** to connect them, and how much
authority to grant once connected. Solving the plumbing exposed the governance
question underneath. That question is where the field sits right now.

One caution from my own research on this project: a standard way to connect is
not the same as having something worth connecting to. I checked five commerce
platforms for this product and found that none of their official MCP servers
exposed the sales or ad-spend data I actually needed. The standard existing and
the data being available are two separate facts, and you have to check both.

### 3.5 What people learned along the way

Anthropic (2024a) documents five reusable patterns for building these systems —
prompt chaining, routing, parallelization, orchestrator-workers, and
evaluator-optimizer — and reports that the teams who succeeded used simple
composable patterns rather than heavy frameworks. Their advice is to add
complexity "*only* when it demonstrably improves outcomes," because agentic
systems "often trade latency and cost for better task performance."

That is worth pausing on. The company selling the models is telling developers
to use *less* autonomy than they probably think they need. When a vendor's
advice cuts against their own sales incentive, it is usually worth taking
seriously.

Alongside the technical work, a safety and governance literature grew. NIST
published the *Artificial Intelligence Risk Management Framework* on 26 January
2023, built around four functions — Govern, Map, Measure, and Manage — for
voluntary use (NIST, 2023). It came before the agent wave but saw the main
issue early: you cannot judge whether an AI system is safe by looking at the
model alone, because the danger depends on what the system is wired up to do.

---

## 4. How It Works When Building Products

### 4.1 The first decision: workflow or agent?

This is the choice you make most often, and the most common mistake is making
it once for the whole product. Real systems are **mixed.** You choose per
piece.

A rough rule:

- **Use a workflow** when you already know the steps, and being predictable
  matters more than being flexible.
- **Use an agent** when you cannot write down the steps in advance, because the
  inputs are too varied.

And a rule that saves a lot of pain: **if the task has exactly one correct
answer, do not use an LLM for it.** Arithmetic is the clearest case. If you
need revenue minus costs, write the subtraction. An LLM can do arithmetic, but
it introduces the possibility of variation into something that has a single
right answer, and you get nothing in exchange. Anthropic's (2024a) advice about
only adding complexity where it demonstrably helps applies directly here.

### 4.2 The second decision: how much can it do without asking?

Once you have an agent, you must decide what it may do on its own, what it must
get approved, and what it may never touch.

The useful question is not "how smart is the model?" It is: **can we undo it?**

Think about the difference between these two mistakes:

- The AI mislabels a support ticket. Someone notices and fixes it. Cost: a few
  minutes.
- The AI spends $4,000 of a client's ad budget on the wrong campaign. The money
  is gone. The only way to fix it is to spend more money.

The first mistake is *reversible*. The second is not. You can clean up
reversible mistakes after they happen. Irreversible ones have to be stopped
before they happen.

So the design rule is: **put the brakes where actions cannot be undone, not
where the task is hard.** An easy action that spends money needs a stricter
gate than a hard action that produces a draft for review.

Anthropic (2024a) describes the mechanisms: "extensive testing in sandboxed
environments, along with the appropriate guardrails," having agents "pause for
human feedback at checkpoints or when encountering blockers," and setting
"stopping conditions (such as a maximum number of iterations) to maintain
control."

There is one more thing about this limit that matters a lot, and it is easy to
miss. **It does not get looser as models get better.** A better model is wrong
less often. It is not wrong *less expensively*. If spending the wrong $4,000 is
unacceptable, it stays unacceptable no matter how good the model gets. "Wait
for the next model" does not solve this category of problem.

### 4.3 The third decision: how do you know it works?

You cannot responsibly give a system freedom if you cannot measure whether it
uses that freedom well. This is what evals are for.

Husain (2024) argues that failed AI products share "a failure to create robust
evaluation systems," and lays out three levels:

1. **Unit tests** — fast, cheap checks on specific cases, run constantly.
2. **Human and model evaluation** — logging what the system actually did,
   having people review it, then training an automated judge and checking that
   judge against the human verdicts.
3. **A/B testing** — comparing real user outcomes, once the product is mature.

He also makes a point that reorders how you work: **error analysis comes
first.** Looking at real failures is what tells you which tests are worth
writing. You do not start by guessing what might break; you start by seeing
what did break.

The practical consequence: **you cannot grant more autonomy than your evals can
verify.** A team without this measurement has no idea where its limit is, so it
cannot know whether it has crossed it.

### 4.4 A fourth limit that no amount of engineering can move

There is one more constraint, and it surprises people because it is not
technical at all.

When your system works on top of someone else's platform — Google, Meta,
Amazon, Shopify — that platform's terms of service decide what you are allowed
to do. Those terms are written by them, can change without your agreement, and
sometimes forbid things that are both easy to build and perfectly reasonable.

No amount of good engineering raises this limit.

A real example from my own project research: Google's Required Minimum
Functionality policy sorts tools into categories, and tools that fully manage
advertiser accounts must provide a long list of features — whether or not those
features fit the product's concept (Google, n.d.). So a product can be forced
to grow scope by *policy* rather than by choice.

The reason I raise this in a paper about method is that it changes how you
sequence work. The platform rules have to be read during design, not after
building, because discovering them late can invalidate the architecture you
already built.

---

## 5. What the Specialization Includes

Seven areas of competence.

### 5.1 Choosing the architecture

Deciding, piece by piece, what is a workflow and what is an agent (§4.1), and
using the five known patterns rather than inventing structure from scratch
(Anthropic, 2024a).

### 5.2 Models: cloud or local

Most people start with a model running on someone else's servers, reached
through an API. That is the fastest path and usually the cheapest at low volume.

But you can also run models on your own hardware. **Open-weight** models can be
downloaded and run locally. The main project that made this practical on normal
computers is `llama.cpp`, whose stated goal is "to enable LLM (and VLM)
inference with minimal setup and state-of-the-art performance on a wide range
of hardware — locally and in the cloud" (ggml-org, n.d.).

Three honest reasons to run a model locally:

1. **Privacy.** The data never leaves your machine. For regulated data or a
   client who will not allow their records sent to a third party, this can be
   the only acceptable option.
2. **Cost at volume.** No per-token bill. For light use, a cloud API is
   cheaper; at high steady volume, owning the hardware can win.
3. **Working offline, and not being dependent on a vendor.** Nobody can change
   your pricing, deprecate your model, or rate-limit you.

The trade-off is real: local models are usually less capable than the best
cloud models, and you take on running the infrastructure yourself. Licences
also vary between model families and need reading before commercial use.

### 5.3 Connecting to the outside world

Tool use, MCP, direct APIs, and authentication. The unglamorous part is
handling things going wrong: rate limits, data formats that change without
warning, credentials expiring. In production these are normal conditions, not
rare exceptions, and a system that assumes the happy path will fail constantly.

### 5.4 Deploying and running it

An agent that only runs on your laptop is not a product. This is where VPSes,
hosting platforms, databases, and scheduled jobs come in. Agentic systems add a
wrinkle to ordinary deployment: they run unattended, they cost money per run,
and they can loop. So you need spend limits, timeouts, and logs that record not
only what happened but *why the system chose it*.

### 5.5 Evaluation

Building the measurement described in §4.3, with error analysis first
(Husain, 2024).

### 5.6 Guardrails and human-in-the-loop design

Building the brakes: approval steps, sandboxes, stopping conditions, spend
caps, and previews of anything that cannot be undone. This is both a safety
problem and a usability problem, because a gate placed badly either fails to
prevent the costly mistake or annoys the user into working around it.

### 5.7 Governance and documentation

Reading platform terms against what you plan to build. Writing down autonomy
decisions so they can be reviewed later. NIST's (2023) Govern-Map-Measure-Manage
structure gives a frame for this. In a system where the *software* makes
decisions, the written record of which decisions you delegated — and why — is
primary documentation, not paperwork.

---

## 6. What Teams Actually Do in This Specialization

This work is unusually cross-functional, for a structural reason: the limits on
autonomy are owned by different parts of an organization. Engineering knows
what the system can do. The business knows what a mistake costs. Legal knows
what the platforms permit. No single role can set the boundary alone — so a team
without a shared forum for this ends up setting it by accident.

**Setting the autonomy boundary.** A recurring meeting that produces a written
decision: what the system does automatically, what needs approval, what it must
never do. Writing down the *reasoning* matters as much as the decision, because
the reasoning is what you re-examine when a platform changes its rules.

**Error analysis sessions.** Going through logs of what the system actually did
and finding the failure patterns. Husain (2024) treats this as the activity that
determines which evals are worth building. It needs people who know the
subject, not just engineers, because spotting a wrong answer in a specialized
domain requires knowing the domain.

**Capturing expert judgment.** Sitting with someone who knows what "good" looks
like and getting their standard into a form precise enough to automate, then
checking the automated judge against real human verdicts. This is interviewing
before it is engineering — which is, notably, a UX research skill.

**Reading platform terms.** Checking the rules against what you plan to build
and writing down a determination. Genuinely unclear cases go to a lawyer rather
than a developer's best guess.

**Incident review.** When the system does something wrong, fixing the immediate
bug *and* revisiting whether it should have had that much freedom. Gartner has
forecast that by 2027, 40% of enterprises will demote or shut down autonomous
agents because of governance gaps found only after something went wrong in
production.[^gartner-note] "Found only after" describes a team that never held
the boundary conversation up front.

**Designing the human moments.** Building the screens where a person reviews
what the AI decided, and making the reasoning legible enough to argue with.
This is straightforwardly design work, and it gates how much automation the
product is permitted to have.

---

## 7. Tools and Skills to Learn

### 7.1 Tools

| Category | Tools | What it is for |
|---|---|---|
| Agentic development | Claude Code | Building and running agentic systems |
| Connection standard | MCP (Anthropic, 2024b) | Standard way to attach tools and data |
| Model routing | OpenRouter | Comparing and switching between models |
| Local models | llama.cpp, Ollama | Running open-weight models on your own hardware |
| Platform data | REST and GraphQL APIs | Getting real data where no standard connector exists |
| Database and auth | Supabase | Stored data, user accounts, row-level security |
| Hosting | Vercel, VPS | Getting it running where others can use it |
| Security | OWASP, Cloudflare, Aikido | Finding and blocking vulnerabilities |
| Evaluation | Trace logging, LLM-as-judge | Measuring whether output is good |
| Documentation | Architectural Decision Records | Recording why decisions were made |
| Version control | Git, GitHub | History and review |

### 7.2 Skills

**Technical**

- Reading API documentation carefully, including the boring parts about rate
  limits and errors.
- Designing data that can represent *"we don't know."* If a system stores zero
  when it means unknown, it will state a confident wrong answer, which is worse
  than admitting a gap.
- Handling credentials and authentication for software talking to software,
  where there is no human to click "allow."
- Writing evals.
- Logging decisions so you can reconstruct why the system did what it did.

**Analytical**

- Asking "can this be undone?" before "can this be automated?"
- Reading terms of service adversarially — what does this clause *forbid*, not
  what did the author probably mean.
- Telling the difference between a problem that needs an agent and one that
  needs twenty lines of ordinary code.

**Communication**

- Explaining a system's decision to someone non-technical in terms they can
  actually push back on. As argued in §2.3, this is a functional requirement,
  not politeness.

**Dispositional**

- Restraint. Anthropic's (2024a) advice to add complexity only where it
  demonstrably helps is a habit before it is a technique, and it runs against
  the natural pull toward building the most autonomous thing you can.

---

## 8. The Application I Will Build

### 8.1 The problem

A business that sells in more than one place — its own website plus
marketplaces — and buys ads on several platforms usually cannot tell you which
channel actually makes money.

Here is why. Each ad platform reports on its own ads, using its own rules, and
each one tends to take credit for sales it merely influenced. One customer who
saw a Meta ad, then searched on Google, then bought, can show up as a win in
both places. Add the platform reports together and you get more sales than
really happened.[^vendor-note] Meanwhile the fees, shipping, and cost of goods
live somewhere else entirely, usually a spreadsheet.

So the seller knows total revenue and total ad spend, but not which channel
made a profit after everything is subtracted. And then they make decisions on
that missing information — moving budget toward whichever platform brags
loudest, which can mean defunding the channel that was actually working.

### 8.2 What the system does

**Phase one — reconciliation.** Pull in orders and ad spend from each connected
platform. Subtract that channel's fees, shipping, and cost of goods. Work out
real profit per channel. Track what a customer from each channel is worth over
time. Then say the answer in plain language instead of metric names.

**Phase two — generation.** Use those real numbers to build and manage the ads,
and preview anything that spends money before it spends it.

### 8.3 How the specialization shows up in it

This is where the ideas from §4 become concrete design decisions.

**The parts that must NOT be agents.** Scheduled data collection and the profit
math itself are plain workflows. Revenue minus costs has one right answer, so
per §4.1 an LLM here would add variation and buy nothing. This is a case where
knowing when *not* to use the fancy approach is the skill.

**The parts that must be agents.** Three pieces cannot be scripted in advance.
Deciding which channel deserves credit when several claim the same sale needs
judgment that resists being fully written down. Turning numbers into an
explanation a seller can act on is generative by nature. Writing ad copy is
open-ended.

**Where the "can we undo it?" rule bites.** Phase two spends real client money,
and that cannot be reversed. So the rule for this product is firm: **nothing
that spends money runs without a human approving it, no matter how accurate the
model turns out to be.** The agent can build the whole campaign and show it.
It cannot launch it. Per §4.2, this does not loosen as models improve, because
better models reduce how often you are wrong, not how much it costs.

Phase one is different. Its output is a number on a screen. A wrong number is
embarrassing but fixable. So more of it can run unattended — and that is a real
reason to build reconciliation before ad generation, not just a convenient
order.

**Where measurement bites.** The attribution judgment is the system's boldest
claim and the one a user can least easily check. Until I have Husain's (2024)
Level 1 and Level 2 evals — tests on cases where I know the right answer, plus
human review of logged decisions with someone who knows the business — the
honest design shows attribution as an assumption with its reasoning visible,
not as a fact. And per §7.2, *"we don't know"* has to be a real state the
system can store and display. Printing zero where it means unknown would be the
worst possible failure for this product, because the entire value proposition
is telling someone the truth about their money.

**Where platform rules bite.** Two things from my research constrain this
directly. Google's Required Minimum Functionality policy may force a long list
of extra features onto the product once it starts managing campaigns in phase
two (Google, n.d.) — so that question needs a written answer from Google before
phase two starts, not a guess from me. Separately, Meta's developer policies
restrict how their ad data may be combined with other platforms' data, which
may conflict with cross-channel reconciliation. That one needs a legal reading.
Both are recorded as open risks rather than quietly assumed away.

### 8.4 Why this app fits the specialization

It forces every lesson in this paper into a real decision. It has pieces that
must be deterministic and pieces that must be agentic, so I cannot avoid §4.1.
It spends money, so I cannot avoid §4.2. Its central claim is hard to verify,
so I cannot avoid §4.3. It lives on other companies' platforms, so I cannot
avoid §4.4.

And it needs the design skill I already have, because a seller who cannot
understand why the system says Google lost money will not trust it, and will
not let it near their budget. The explanation is not a feature on top of the
product. It is the product.

---

## 9. Conclusion

The skill that defines this specialization is not making software that acts on
its own. That has become the easy part.

The skill is deciding how much the software is allowed to decide, and being able
to show why that amount is right. That decision rests on three things: whether
you can measure that the system does the job well, whether a mistake can be
undone, and whether the platforms you depend on even permit it.

Two of those do not improve with better technology. A stronger model makes
costly mistakes rarer, not cheaper — so wherever an action cannot be reversed,
the brake stays. And no model, however good, changes what Google's or Meta's
terms allow. Both are permanent parts of the design problem rather than
temporary limits waiting for the next release.

Gartner's forecast that over 40% of agentic projects will be cancelled by the
end of 2027 blames unclear business value and weak risk controls far more than
weak models.[^gartner-note] If that is right, then the bottleneck in this field
is not what AI can do. It is whether the people building it thought carefully
enough about what it should be allowed to do — which is, in the end, a design
question.

---

## Notes

[^gartner-note]: **Source verification note.** The Gartner figures here come
from search-result metadata, including titles and dates in the press-release
URLs. Gartner's newsroom returned HTTP 403 to automated retrieval, so I could
not read the full releases myself. The figures — 40% of enterprise apps having
task-specific AI agents by end of 2026; over 40% of agentic projects cancelled
by end of 2027; 40% of enterprises demoting or shutting down agents by 2027 —
should be confirmed against the releases directly before being relied on. They
are used here to describe a general pattern, not as exact measurements.

[^vendor-note]: **Source quality note.** Published figures on cross-platform
conversion over-counting come mostly from companies selling attribution
software, who benefit from the problem looking large. The direction of the claim
is consistent across independent vendors and matches how platform attribution
works mechanically, so I treat the pattern as real and the specific numbers as
vendor claims rather than measurements.

---

## References

Anthropic. (2024a, December 19). *Building effective AI agents*.
https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024b, November 25). *Introducing the Model Context Protocol*.
https://www.anthropic.com/news/model-context-protocol

ggml-org. (n.d.). *llama.cpp* [Computer software]. GitHub. Retrieved October
23, 2026, from https://github.com/ggml-org/llama.cpp

Google. (n.d.). *Google Ads developer policies*. Advertising Policies Help.
Retrieved October 23, 2026, from
https://support.google.com/adspolicy/answer/6169371

Husain, H. (2024, March 29). *Your AI product needs evals*.
https://hamel.dev/blog/posts/evals/

Liu, F., Zhang, M., & Budiu, R. (2023, October 27). *AI as a UX assistant*.
Nielsen Norman Group. https://www.nngroup.com/articles/ai-roles-ux/

National Institute of Standards and Technology. (2023, January 26).
*Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI
100-1). U.S. Department of Commerce.
https://www.nist.gov/itl/ai-risk-management-framework

---

### Notes for the author

1. **Section 2 is built from what you told me** — UX designer, upskilling in
   automation, agentics, LLMs, local models, VPSes and MCP, taking the
   residency to build enterprise-ready products. Read it and make it sound like
   you. §2.4 in particular should be your own words; I wrote a version of what
   you said, but it is the most personal paragraph in the paper.

2. **Anthropic authorship.** The agents post lists "Erik S. and Barry Zhang."
   Because the first author has no full surname, I used APA's corporate-author
   form, which is the normal fix. Don't invent a surname.

3. **Undated sources.** The Google and llama.cpp entries are living pages with
   no publication date, so APA's `n.d.` plus a retrieval date is correct.

4. **The NN/g survey is from 2023.** That's three years old. I've said so in
   the text rather than implying it's current — and the age actually helps the
   argument, since adoption was already near-total before agents were usable.

5. **Check every link before you submit.** I opened and read all seven sources
   on 23 October 2026. Re-check them; a dead citation makes an instructor doubt
   the rest.

6. **The "can we undo it?" framing is my synthesis**, not a named framework you
   can point to in the literature. The sources support each piece, but the way
   it's assembled is the paper's own argument. Be ready to defend it as yours,
   because you may be asked.
