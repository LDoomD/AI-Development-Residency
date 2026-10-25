# Agentic Workflows and AI Automation: How Software Learned to Decide, and Why UX Designers Need to Understand It

**Author:** Jose Castillo
**Course:** Tech Fleet AI Development Residency, Fall/Winter 2026 (Premium Track)
**Instructor:** Morgan Denner
**Date:** October 2026
**Specialization areas:** AI Automation + Advanced Agentic Workflows (combined)

---

## Abstract

This paper explains what agentic workflows and AI automation are, how they
work, and what a person needs to learn in order to build with them. AI
automation is work that finishes without a person doing it, and agentic
workflows are the method most people use to reach that result today.

My argument is that the hard part of this field is no longer getting software
to act on its own. The hard part is deciding how much the software should be
allowed to decide by itself, and then proving it can be trusted with that much.
The paper closes by applying these ideas to the application I am building for
this residency.

---

## A short glossary first

This field is full of jargon, and most of it sounds more complicated than it
is. These are the words I use in this paper, in plain terms.

| Term | What it means |
|---|---|
| **LLM** (large language model) | An AI program that produces text by predicting what word should come next. It learned how to do that from an enormous amount of writing. Claude and ChatGPT are LLMs. |
| **Training** | The process that builds a model by showing it huge amounts of text and adjusting it until its predictions get good. It happens once, before anyone uses the model, and it is expensive. |
| **Model weights** | The numbers inside a finished model. Training is what sets those numbers, so the weights are everything the model learned. Copy the weights and you have copied the model. |
| **Open-weight model** | A model whose company published the weights file, so anyone can download it and run the model themselves. The opposite is a closed model, which you can only use by sending requests to the company's servers. |
| **Local model** | A model running on hardware you control, such as your own laptop or a server you rent, rather than on the model company's servers. |
| **Inference** | Using a finished model. Training is when the model learns, and inference is every time afterward that you give it input and it gives you output. |
| **Tool** | One specific action you give a model permission to take, such as looking up an order number or sending an email. On its own a model can only produce text, and a tool is how it gets to make something happen. |
| **Tool use** | When a model answers a request by calling one of its tools instead of writing a reply. |
| **MCP** (Model Context Protocol) | A shared format for describing tools, so that any model speaking it can connect to any tool speaking it. The tool is the action and MCP is the standard plug. Before MCP, every pairing of a model and a tool needed its own custom code. |
| **Workflow** | A system where a person wrote down the steps ahead of time. The model does one defined job inside a step, but it cannot change the order or skip ahead. |
| **Agent** | A system where you give the model a goal instead of steps, and it picks its own steps while it runs. |
| **Orchestration** | The code that coordinates the steps, tools, and models so they run in the right order and hand information to each other correctly. |
| **Eval** (evaluation) | A test that measures whether an AI system's output is any good. Ordinary software tests check right against wrong, while evals have to handle output where quality is a judgment call. |
| **Guardrail** | A hard limit built into the system that blocks an action no matter what the model decides. |
| **Human in the loop** | A design where the software stops and waits for a person to approve something before it continues. |
| **VPS** (virtual private server) | A computer you rent in someone else's data center and run yourself. |
| **API** | A published list of requests a company's software will accept, so that other software can ask it for data or ask it to do something. |

---

## 1. Introduction to the Subject

### 1.1 Automations are not new

People have been writing scripts to handle boring work for years. The old kind
had one defining limit, which is that it could not understand anything. Picture
a script that emails you a sales report every Monday. A person decides what
belongs in that report, and the script repeats that decision forever. If
something odd turns up in the data, such as a strange refund or a currency
nobody planned for, the script does not react, because it was never built to
react. It does the one thing it was told to do. That made old automation
extremely predictable, since somebody wrote down every step in advance and you
always knew what the system would do. It also left those systems badly exposed,
because the moment reality stopped matching the plan they either broke or
produced nonsense.

### 1.2 What changed when models could use tools

LLMs broke that limit. An LLM can read material it has never encountered before
and respond sensibly to it, and once you give it tools so that it can search a
database, read a file, or call an API, something genuinely new becomes possible.
You can stop handing the software a procedure and begin handing it a goal
instead. Anthropic (2024a) defines two ways of building on that capability.
Workflows, in their account, are "systems where LLMs and tools are orchestrated
through predefined code paths," whereas agents are "systems where LLMs
dynamically direct their own processes and tool usage, maintaining control over
how they accomplish tasks." The practical difference comes down to who
sequences the work. In a workflow the developer decides the steps and the model
fills in the blanks, while in an agent the model determines its own steps as it
runs.

The application I am developing for this residency, described in full in
Section 8, is a study tool for adults enrolled in courses. A user uploads the
syllabus for a course, writes notes as the course progresses, and the
application converts those notes into practice questions and schedules them for
review. Notes enter at one end and practice material comes out the other.

Built as a workflow, that conversion would run as a fixed sequence defined in
advance. The system would read an incoming note, match it against whichever
topic comes next on the syllabus, load the lesson template for that topic,
generate ten questions from the note, and add the result to the review queue.
The model would contribute only two things to the chain, namely deciding which
topic the note belongs to and writing the questions themselves, and the order
of operations would never vary. The behavior of the system would therefore be
fully known before it ever ran.

A sequence of that kind breaks as soon as it meets real notes, which is why the
same conversion has to be built as an agent instead. Students do not take notes
in syllabus order. A person records whatever held their attention during class,
and the result may cover three topics at once, jump ahead to material the course
has not yet reached, or consist of a question rather than a fact. The system
therefore receives a goal and a set of tools rather than a sequence. It is given
the user's course profile, the new note, and the instruction to produce practice
material appropriate to where that user actually stands in the course. The model
then determines how many topics the note touches, whether the content calls for
memorization or for conceptual mapping, and whether the note is usable at all or
should wait in the inbox until related material arrives. None of those
determinations can be specified ahead of time, because each one depends on a
note that nobody has seen yet.

### 1.3 The trade this creates

The agent version is more flexible, and it handles the disordered note that the
fixed sequence would have mangled. What it gives up is knowledge of what the
software is going to do. A system that picks its own steps can pick a step you
never considered, including a wrong one, a wasteful one, or a harmful one.

That is the trade at the center of this specialization. More freedom means the
system copes with more situations while offering fewer guarantees about its
behavior, and every genuinely hard question in the field comes out of that one
trade. The useful question is therefore almost never whether the AI can do
something, since increasingly it can. The useful question is how much it should
be allowed to do by itself, and how anyone would find out if you got that
amount wrong.

### 1.4 Why I combined the two specializations

AI automation is the outcome, meaning work that gets finished without a person
doing it, and agentic workflows are the method that currently gets you there on
tasks too messy to script in advance. Studying the method without the outcome
produces a clever demo nobody uses, while chasing the outcome without
understanding the method produces a system that passes testing and then does
something expensive and surprising in production. Gartner has forecast that more
than 40% of agentic AI projects will be cancelled by the end of 2027, pointing
to rising costs, unclear business value, and weak risk controls.[^gartner-note]
Two of those three causes have nothing to do with the technology, since they are
planning failures.

---

## 2. Why This Is Relevant to My Career

I am a UX designer, and I have been upskilling in AI, starting with automation
and moving into the deeper layers of agentic systems, LLMs, local models,
virtual private servers, and MCP. I am taking this residency because I want to
build enterprise-ready products rather than prototypes, and the reason is
simple. UX designers now have to know how to build. That is not a prediction,
since it is already happening, and the evidence comes from my own field's
research.

### 2.1 My field already adopted these tools

Nielsen Norman Group surveyed 841 UX professionals in July and August of 2023.
They found that "92% of the respondents claimed they had used at least one
generative AI tool," and that among those using AI for work, 63% used it at
least several times a week (Liu, Zhang, & Budiu, 2023).

That survey is three years old now and predates practical agents, which means
adoption in my field was effectively total before the technology even got
interesting. For a designer today the question is no longer whether to use AI
but whether to understand what they are using.

### 2.2 The handoff is disappearing, and that is the real change

UX has always worked through a handoff. A designer figures out what should exist
and describes it, and an engineer builds it. The description was the designer's
deliverable, and the gap between describing and building is why two roles
existed in the first place.

Agentic tooling is closing that gap, because someone who can describe intent
precisely enough can increasingly produce the working thing. This does not mean
engineering knowledge stops mattering. It means engineering knowledge stops
being optional for designers. If I can build what I design, the limit on my
work is no longer whether anyone has capacity to build it, but whether I
understand what I am asking for well enough to be responsible for it.

### 2.3 What I bring that is actually scarce here

The hardest part of this field is not writing the code. It is deciding what the
software should be allowed to decide, and then designing the moments where it
stops and asks a person.

That is a design problem. Where does the approval step go, and how do you show
someone a decision the AI made in a form they can judge and argue with? How
much friction protects the user, and how much friction only makes the tool
annoying enough to abandon? Those are questions about human judgment under
uncertainty, and UX research is the discipline built to study them.

A system nobody can understand cannot be trusted, and a system nobody trusts
does not get to run on its own. Explainability is therefore not a feature added
at the end but the thing that decides how much automation a product is allowed
to have, which puts design inside the engineering rather than on top of it.

### 2.4 What I want to be able to do by the end

I want to take a product from nothing to something real people use, which means
specifying it, building it, deploying it, securing it, and judging honestly
whether it works. Not a mockup, and not a demo that falls apart on real data.
The specific test I care about is building something that handles real money or
real customer data, and then being able to defend the decisions inside it to
someone technical who disagrees with me.

---

## 3. Background About the Specialization

The field arrived at its current position in four steps, and each step created
the problem that the next one solved.

### 3.1 Scripts that followed orders

The first step was classic automation, in which a person wrote down every step
and the software repeated it. Those systems were reliable and brittle for the
reasons described in §1.1, and they remain the right answer for a great many
problems, which is worth remembering later in this paper.

### 3.2 Models that could read and write

The second step came when LLMs arrived and could handle language they had never
seen before. Early on they were sealed off from everything around them. A model
could write a good summary of a sales report you pasted in, and had no way to
go fetch that report itself, so it could think without acting.

### 3.3 Tools, and the integration problem

The third step was giving models tools, and that was the real unlock, because a
model that can pick a tool and read the result can be handed a goal instead of
a procedure. It also created a grubby practical problem, since every tool needed
its own custom glue code. Connecting a model to a database, then to Slack, then
to Google Drive meant writing three separate integrations, and everybody
building agents was writing the same glue over and over. Anthropic (2024b)
described models in that period as "trapped behind information silos and legacy
systems."

### 3.4 One standard instead of custom glue

The fourth step was the Model Context Protocol, released 25 November 2024, which
proposed a single standard way to plug tools and data into AI systems.
Anthropic (2024b) called it "a new standard for connecting AI assistants to the
systems where data lives, including content repositories, business tools, and
development environments." Instead of writing custom glue for every connection,
a developer implements the protocol once.

Something important follows from that. Once connecting things became easy, the
leftover hard problem became whether to connect them at all, and how much
authority to grant once connected. Fixing the plumbing exposed the governance
question underneath it, and that question is where the field sits right now.

My own research on this project produced one caution worth adding, which is
that a standard way to connect is not the same as a standard that fits your
situation. I expected to read a user's notes out of Notion or Google Docs
through MCP, and found that MCP is designed for a model client running on
someone's own machine rather than for a web application running on a server
with many users. The protocol existing and the protocol suiting the
architecture are two separate facts, and both have to be checked before the
design depends on either.

### 3.5 What the field learned along the way

Anthropic (2024a) documents five reusable patterns for building these systems,
which are prompt chaining, routing, parallelization, orchestrator-workers, and
evaluator-optimizer. They report that the teams who succeeded used simple
composable patterns rather than heavy frameworks, and they advise adding
complexity "*only* when it demonstrably improves outcomes," because agentic
systems "often trade latency and cost for better task performance."

That advice deserves attention for an unusual reason. The company selling the
models is telling developers to use less autonomy than they probably think they
need, and when a vendor's advice cuts against its own sales incentive it is
usually worth taking seriously.

A safety and governance literature grew alongside the technical work. NIST
published the *Artificial Intelligence Risk Management Framework* on 26 January
2023, built around four functions named Govern, Map, Measure, and Manage, for
voluntary use (NIST, 2023). It predates the agent wave but identified the
central issue early, which is that you cannot judge whether an AI system is
safe by looking at the model alone, because the danger depends on what the
system is wired up to do.

---

## 4. How It Works When Building Products

### 4.1 The first decision, workflow or agent

This is the choice a developer makes most often, and the most common mistake is
making it once for the whole product. Real systems are mixed, and the decision
has to be made piece by piece.

The rough rule is to use a workflow when you already know the steps and
predictability matters more than flexibility, and to use an agent when you
cannot write the steps down in advance because the inputs vary too much. A
second rule saves a great deal of pain, which is that a task with exactly one
correct answer should not go to an LLM at all. Arithmetic is the clearest case.
If you need revenue minus costs, write the subtraction. An LLM can do
arithmetic, but it introduces the possibility of variation into something that
has a single right answer, and nothing is gained in exchange. Anthropic's
(2024a) advice about adding complexity only where it demonstrably helps applies
directly to that case.

### 4.2 The second decision, how much it can do without asking

Once a system includes an agent, a developer has to decide what it may do on its
own, what it must get approved, and what it may never touch. The useful question
is not how smart the model is but whether its actions can be undone.

Two mistakes illustrate the difference. In the first, the AI mislabels a support
ticket, somebody notices, somebody fixes it, and the cost is a few minutes. In
the second, the AI sends an email to every customer on a company's list, and
that email is wrong. The first mistake is reversible and the second is not. A
reversible mistake can be cleaned up after it happens, while an irreversible one
has to be stopped before it happens.

The design rule that follows is to put the brakes where actions cannot be
undone, rather than where the task is hard. An easy action that reaches
customers, moves money, or deletes data needs a stricter gate than a difficult
action that produces a draft for somebody to review. Anthropic (2024a)
describes the mechanisms for building those brakes, recommending "extensive
testing in sandboxed environments, along with the appropriate guardrails,"
having agents "pause for human feedback at checkpoints or when encountering
blockers," and setting "stopping conditions (such as a maximum number of
iterations) to maintain control."

One further point about this limit matters a great deal and is easy to miss,
which is that it does not get looser as models improve. A better model is wrong
less often, but it is not wrong less expensively. If sending that email to every
customer is unacceptable, it stays unacceptable no matter how good the model
gets, and waiting for the next model release does not solve this category of
problem.

### 4.3 The third decision, how you know it works

A developer cannot responsibly give a system freedom without being able to
measure whether it uses that freedom well, and measuring that is what evals are
for. Husain (2024) argues that failed AI products share "a failure to create
robust evaluation systems," and lays out three levels of evaluation. The first
level is unit tests, meaning fast and cheap checks on specific cases that run
constantly. The second is human and model evaluation, which means logging what
the system actually did, having people review those logs, then training an
automated judge and checking that judge against the human verdicts. The third
is A/B testing, which compares real user outcomes once the product is mature.

Husain also makes a point that reorders how the work gets done, which is that
error analysis comes first. Looking at real failures is what tells you which
tests are worth writing, so you do not start by guessing what might break but
by seeing what did break. The practical consequence is that a team cannot grant
more autonomy than its evals can verify. A team without that measurement has no
idea where its limit sits, and therefore cannot know whether it has crossed it.

### 4.4 The limit engineering cannot move

One more constraint shapes this work, and it surprises people because it is not
technical at all. When a system runs on top of someone else's platform, whether
that is Google, Meta, Amazon, or Shopify, the platform's terms of service decide
what the developer is allowed to do. Those terms are written by the platform,
can change without the developer's agreement, and sometimes forbid things that
are both easy to build and perfectly reasonable. No amount of good engineering
raises that limit.

My own project research produced a concrete example. An earlier version of my
residency project was an advertising and sales tool, and while scoping it I
found that Google's Required Minimum Functionality policy sorts tools into
categories, and that tools which fully manage advertiser accounts have to
provide a long list of features whether or not those features fit the product's
concept (Google, n.d.). A product can therefore be forced to grow in scope by
policy rather than by choice.

I raise this in a paper about method because it changes how the work gets
sequenced. Platform rules have to be read during design rather than after
building, since discovering them late can invalidate an architecture that is
already finished.

---

## 5. What the Specialization Includes

The specialization covers seven areas of competence, and the sections below
describe each one.

### 5.1 Choosing the architecture

The first competence is deciding, piece by piece, what should be a workflow and
what should be an agent, as described in §4.1, and then using the five
documented patterns instead of inventing structure from scratch (Anthropic,
2024a).

### 5.2 Models, cloud or local

Most developers start with a model running on someone else's servers and
reached through an API, which is the fastest path and usually the cheapest at
low volume. Models can also run on hardware the developer owns, since
open-weight models can be downloaded and run locally. The project that made
this practical on ordinary computers is `llama.cpp`, whose stated goal is "to
enable LLM (and VLM) inference with minimal setup and state-of-the-art
performance on a wide range of hardware, locally and in the cloud" (ggml-org,
n.d.).

There are three honest reasons to run a model locally. The first is privacy,
because the data never leaves the machine, and for regulated data or a client
who will not allow records to be sent to a third party this can be the only
acceptable option. The second is cost at volume, since there is no per-token
bill, and while a cloud API is cheaper for light use, owning the hardware can
win at high steady volume. The third is independence, because a local model
works offline and nobody can change the pricing, deprecate the model, or
rate-limit the developer.

The trade-off is real. Local models are usually less capable than the best cloud
models, and the developer takes on running the infrastructure. Licences also
vary between model families and need reading before any commercial use.

### 5.3 Connecting to the outside world

The third competence covers tool use, MCP, direct APIs, and authentication. The
unglamorous part is handling the ways things go wrong, including rate limits,
data formats that change without warning, and credentials that expire. In
production those are normal conditions rather than rare exceptions, and a system
built on the assumption that everything works will fail constantly.

### 5.4 Deploying and running it

An agent that only runs on a developer's laptop is not a product, so this
competence covers virtual private servers, hosting platforms, databases, and
scheduled jobs. Agentic systems add a wrinkle to ordinary deployment, because
they run unattended, cost money on every run, and can loop. That means a
deployment needs spend limits, timeouts, and logs that record not only what
happened but why the system chose it.

### 5.5 Evaluation

The fifth competence is building the measurement described in §4.3, beginning
with error analysis rather than with test-writing (Husain, 2024).

### 5.6 Guardrails and human-in-the-loop design

The sixth competence is building the brakes, which includes approval steps,
sandboxes, stopping conditions, spend caps, and previews of anything that cannot
be undone. This is a safety problem and a usability problem at the same time,
because a gate placed badly either fails to prevent the costly mistake or
annoys the user into working around it.

### 5.7 Governance and documentation

The last competence is reading platform terms against what the team plans to
build, and writing down autonomy decisions so they can be reviewed later.
NIST's (2023) Govern, Map, Measure, and Manage structure gives a frame for that
work. In a system where the software makes decisions, the written record of
which decisions were delegated, and why, is primary documentation rather than
paperwork.

---

## 6. What Teams Actually Do in This Specialization

This work is unusually cross-functional for a structural reason, which is that
the limits on autonomy are owned by different parts of an organization.
Engineering knows what the system can do, the business knows what a mistake
costs, and legal knows what the platforms permit. No single role can set the
boundary alone, so a team without a shared forum for the question ends up
setting it by accident.

Setting the autonomy boundary is therefore the first recurring activity, and it
should produce a written decision covering what the system does automatically,
what needs approval, and what it must never do. Writing down the reasoning
matters as much as recording the decision, because the reasoning is what a team
re-examines when a platform changes its rules.

Error analysis sessions are the second activity, and they involve going through
logs of what the system actually did in order to find the failure patterns.
Husain (2024) treats this as the activity that determines which evals are worth
building. It needs people who know the subject rather than engineers alone,
because spotting a wrong answer in a specialized domain requires knowing the
domain.

Capturing expert judgment is the third activity. Someone who knows what good
looks like has to be interviewed until their standard is precise enough to
automate, and the resulting automated judge then has to be checked against real
human verdicts. That is interviewing before it is engineering, which makes it a
UX research skill.

Reading platform terms is the fourth activity, meaning checking the rules
against what the team plans to build and writing down a determination.
Genuinely unclear cases go to a lawyer rather than to a developer's best guess.

Incident review is the fifth activity, and it involves more than fixing the
immediate bug, because the team also has to revisit whether the system should
have had that much freedom in the first place. Gartner has forecast that by
2027, 40% of enterprises will demote or shut down autonomous agents because of
governance gaps found only after something went wrong in
production.[^gartner-note] Finding a gap only after the failure describes a team
that never held the boundary conversation up front.

Designing the human moments is the sixth activity, and it means building the
screens where a person reviews what the AI decided and making the reasoning
legible enough to argue with. That is design work, and it gates how much
automation the product is permitted to have.

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

The technical skills start with reading API documentation carefully, including
the boring parts about rate limits and error codes. Close behind that is
designing data that can represent uncertainty, because a system that stores a
zero when it means unknown will state a confident wrong answer, which is worse
than admitting a gap. A developer also has to handle credentials and
authentication for software talking to software, where no person is available
to click an approval button, and has to be able to write evals and to log
decisions in enough detail to reconstruct why the system did what it did.

The analytical skills are mostly habits of questioning. The first is asking
whether an action can be undone before asking whether it can be automated. The
second is reading terms of service adversarially, which means asking what a
clause forbids rather than what its author probably meant. The third is telling
the difference between a problem that genuinely needs an agent and a problem
that needs twenty lines of ordinary code.

One communication skill matters more than the rest, which is explaining a
system's decision to someone non-technical in terms they can actually push back
on. As argued in §2.3, that is a functional requirement rather than politeness.

Finally the work demands a disposition, and the disposition is restraint.
Anthropic's (2024a) advice to add complexity only where it demonstrably helps is
a habit before it is a technique, and it runs against the natural pull toward
building the most autonomous thing a developer can build.

---

## 8. The Application I Will Build

### 8.1 The problem

An adult taking a demanding course writes notes and then does nothing with them.
The notes are not the problem. The problem is the distance between having notes
and having practice.

Turning a page of notes into something a person can be tested on is slow, boring
work, and it has to happen before any learning does. For an adult with ADHD that
ordering is fatal, because the task with the highest startup cost sits directly
in front of the task with the payoff. So the notes pile up, the material never
gets retrieved, and the course ends with a folder of writing nobody ever quizzed
themselves on.

The tools that exist do not close this gap. Flashcard apps assume the cards are
already made, note apps assume the user will come back and study them, and chat
assistants will answer a question without scheduling the next one. My own
competitive research found that every tool surveyed in this space is
proprietary, and that none of them take raw notes in one end and produce a
practice schedule out the other.

A second and harder problem sits underneath the first one, which is that even
the people who do build the cards mostly stop using them. Adherence research on
spaced-repetition tools shows that roughly 20 to 30 percent of users never start
at all, and that around 80 percent of those who do have stopped within a year
once no exam is forcing them.[^adherence-note] A system that only generates
material and then sends reminders has therefore already failed, and the real
design target is the drop-off rather than the generation.

### 8.2 What the system does

The user signs in, and for each course they go through a short intake in which
they upload the syllabus and answer a few questions. The system reads the
syllabus and builds a course profile holding the topics, the sequence, and the
real deadlines.

After that the user simply captures notes, in whatever shape they already write
in, whether that is one line or ten pages. There is no template, no tagging,
and no formatting requirement, because the moment a format is required the work
has been put back in front of the payoff and the original problem has been
recreated.

Everything else runs behind that single action. First the system reads each note
and places it against the course profile, determining which topic it belongs
to, where it sits in the sequence, and whether it is material the syllabus
announced or something unexpected. Second it decides what kind of practice the
material actually supports, choosing between four modes, which are MAP for
structure, DRILL for facts and syntax, EXAMPLES for reading good work against
bad, and REPS for procedures. A list of API flags calls for DRILL, while a
conceptual overview calls for MAP. Third it writes the lesson in the chosen
mode. Fourth a spaced-repetition scheduler decides when that lesson comes back,
weighted by the deadlines recorded in the syllabus. Fifth, after each session
the user rates mental effort on a 9-point scale (Paas, 1992), and a reading of 7
to 9 means the system reduces scope and adds scaffolding rather than pressing
on.

### 8.3 How the specialization shows up in it

The ideas in §4 turn into concrete design decisions once applied to this
product.

Some parts of the system must not be agents at all. The scheduler is a plain
algorithm rather than a model, because the question of when an item should come
back has a defensible deterministic answer, and putting an LLM there would add
variation while buying nothing. That is exactly the §4.1 mistake. The same
reasoning covers storing notes, tracking streaks, and computing what is due, and
knowing where not to put the model is half the job.

A second reason applies specifically to this product. The failure mode that
kills adherence in existing tools is an item that keeps coming back no matter
how well the user performs on it. That is a bug in scheduling logic, and it gets
fixed with a circuit breaker in code, meaning a rule that retires an item after
a set number of failures, rather than by asking a model to be reasonable about
it.

Other parts must be agents, because three pieces of the work cannot be scripted
in advance. Reading an arbitrary note and placing it against a course profile is
judgment that resists being written down. Choosing the practice mode is a
classification over material nobody has seen yet. Writing the lesson is
generative by nature. The intake conversation is open-ended as well, since the
system cannot know in advance what a given course looks like to the person
taking it.

The question of reversibility from §4.2 lands somewhere less obvious in this
product, because nothing here spends money. It lands on the user's own
self-regulation. My research names the risk directly. Metacognitive laziness is
the handing of goal-setting, error-monitoring, and strategy selection over to
the AI instead of doing those things yourself (Fan et al., 2025; Dizon et al.,
2026), and my own review grades it a moderate to high risk. Strategy selection
is exactly what my effort rule performs, because when the system quietly shrinks
a lesson in response to a rating of 8, it has just made a learning-strategy
decision on the user's behalf. Do that silently and often enough and the result
is a tool that improves today's session while removing the skill the user came
for.

The rule for this product is therefore that the system never decides the user is
overloaded. The user's rating decides that. The system only decides what to cut,
and it says so out loud. The cut happens immediately, because stopping to
deliberate mid-session is its own kind of load, and the trade-off gets surfaced
at review time when there is room to think about it.

This is also the place where the brake is designed to move over time, which is
the opposite of the right answer for a product with money on the line. Bounded
autonomy is the mechanism. Salah et al. (2026) define it as limiting the scope,
timing, transparency, contestability, and duration of an AI's intervention
according to how much regulatory capacity the learner has actually developed.
Early on the system explains the trade-off, later it only asks, and later still
it only records the user's own call.

The reason to fade that scaffold rather than keep it is that nobody has
demonstrated the skill survives its removal. Salah et al. frame transfer to
unsupported tasks, meaning whether regulatory capability remains once the AI
support is gone, as an open question to be tested rather than a settled result.
A permanent scaffold is therefore a design that can never be checked, which is
reason enough to prefer one that withdraws on a schedule.

Measurement bites hardest on the system's boldest claim, which is that the
practice it generates is good practice, and that happens to be the claim a user
can least easily check. A lesson can read well and teach nothing. The gap
between performance and learning is the best-replicated finding in my review,
with three independent studies showing output scores rise while knowledge gain
and transfer stay flat, so a lesson looking right is not evidence that it works.
Until I have Husain's (2024) first and second levels of evaluation, meaning
tests on notes where I already know the correct mode and the correct questions,
plus human review of logged mode decisions, the honest design treats mode
selection as a visible assumption the user can override rather than as a
verdict. Following the point in §7.2, an admission that the system does not know
what a note is has to be a real state it can store and display. A note the
system cannot place should sit in the inbox saying so, rather than get forced
into a lesson that teaches the wrong thing.

Adherence needs the same discipline. The research is explicit that adherence
must never be measured by asking, which means it has to come from logged
behavior, and that makes the instrumentation part of the build rather than an
afterthought.

Platform rules are the constraint that changed most when I changed projects, and
the honest account is that the constraint shrank rather than vanished. The
earlier version of this project could not display anything at all until Google,
Meta, Shopify, and Amazon had each granted access, which is a §4.4 problem in
its purest form and the reason I switched. No amount of good engineering
shortens someone else's review queue, and the course deadline does not move.

What remains is smaller and still worth naming. The system depends on a model
provider, which makes that provider's terms, pricing, and rate limits a real
dependency rather than a detail. If I later let users pull notes directly out of
Notion or Google Docs instead of uploading files, that reintroduces the exact
gate I escaped, since a public Notion integration needs Notion's review and
reading a user's Google Docs needs a sensitive-scope verification that has been
reported taking well over a month. File upload is therefore the first version on
purpose, and the integration becomes a later decision made with its approval
cost visible rather than a convenience assumed into the architecture.

### 8.4 Why this app fits the specialization

This application forces every lesson in the paper into a real decision. The
scheduler has to be deterministic while the note reading has to be agentic, so I
cannot avoid §4.1. The system makes strategy decisions for a user whose own
judgment is the thing being built, so I cannot avoid §4.2, and the right answer
there is a brake that fades on purpose, which is a harder design than a brake
that stays fixed. Its central claim is hard to verify and easy to fake, so I
cannot avoid §4.3. It still sits on top of someone else's platform, so I cannot
avoid §4.4 either.

It also needs the design skill I already have. A user who does not understand
why the system cut their lesson in half will read that cut as the software
deciding they are not capable. The explanation is not a feature sitting on top
of the product. It is the product.

---

## 9. Conclusion

The skill that defines this specialization is not making software that acts on
its own, since that has become the easy part. The skill is deciding how much the
software is allowed to decide, and being able to show why that amount is right.
That decision rests on three things, which are whether the team can measure that
the system does its job well, whether a mistake can be undone, and whether the
platforms the system depends on even permit the behavior.

Two of those three do not improve with better technology. A stronger model makes
costly mistakes rarer rather than cheaper, so wherever an action cannot be
reversed the brake stays. And no model, however good, changes what the companies
a product depends on allow it to do. Both are permanent parts of the design
problem rather than temporary limits waiting on the next release.

Gartner's forecast that over 40% of agentic projects will be cancelled by the
end of 2027 blames unclear business value and weak risk controls far more than
weak models.[^gartner-note] If that is right, then the bottleneck in this field
is not what AI can do. It is whether the people building it thought carefully
enough about what it should be allowed to do, which is, in the end, a design
question.

---

## Notes

[^gartner-note]: **Source verification note.** The Gartner figures in this paper
come from search-result metadata, including titles and dates in the
press-release URLs. Gartner's newsroom returned HTTP 403 to automated
retrieval, so I could not read the full releases myself. The figures, meaning
40% of enterprise apps having task-specific AI agents by end of 2026, over 40%
of agentic projects cancelled by end of 2027, and 40% of enterprises demoting
or shutting down agents by 2027, should be confirmed against the releases
directly before being relied on. They are used here to describe a general
pattern rather than as exact measurements.

[^adherence-note]: **Source quality note.** The spaced-repetition adherence
figures in §8.1 come from studies of medical students and residents, a
population under board-exam pressure. Reported standard deviations exceed the
means, so these figures are better read as a ceiling for a user with no external
deadline than as a prediction. The direction of the finding is consistent across
the studies, while the specific percentages are not precise measurements.

---

## References

Anthropic. (2024a, December 19). *Building effective AI agents*.
https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024b, November 25). *Introducing the Model Context Protocol*.
https://www.anthropic.com/news/model-context-protocol

Dizon, J. I. W. T., Mendoza, N. B., Gašević, D., & Ganotice, F. A. (2026).
Assessing AI-driven metacognitive offloading: Initial development and
validation of the Metacognitive Laziness Scale. *ECNU Review of Education,
9*(2). https://doi.org/10.1177/20965311261450994

Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., &
Gašević, D. (2025). Beware of metacognitive laziness: Effects of generative
artificial intelligence on learning motivation, processes, and performance.
*British Journal of Educational Technology, 56*(2), 489–530.
https://doi.org/10.1111/bjet.13544

ggml-org. (n.d.). *llama.cpp* [Computer software]. GitHub. Retrieved October
23, 2026, from https://github.com/ggml-org/llama.cpp

Google. (n.d.). *Required Minimum Functionality (RMF)*. Google Ads API
documentation. Retrieved October 23, 2026, from
https://developers.google.com/google-ads/api/docs/api-policy/rmf

Husain, H. (2024, March 29). *Your AI product needs evals*.
https://hamel.dev/blog/posts/evals/

Liu, F., Zhang, M., & Budiu, R. (2023, October 27). *AI as a UX assistant*.
Nielsen Norman Group. https://www.nngroup.com/articles/ai-roles-ux/

National Institute of Standards and Technology. (2023, January 26).
*Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI
100-1). U.S. Department of Commerce.
https://www.nist.gov/itl/ai-risk-management-framework

Paas, F. G. W. C. (1992). Training strategies for attaining transfer of
problem-solving skill in statistics: A cognitive-load approach. *Journal of
Educational Psychology, 84*(4), 429–434.
https://doi.org/10.1037/0022-0663.84.4.429

Salah, M., Al-Busaidi, R., Al-Ghawi, A., & Shawky, W. (2026). The regulation
paradox: Agentic AI, bounded autonomy, and self-regulated learning in higher
education. *Frontiers in Education, 11*, Article 1902833.
https://doi.org/10.3389/feduc.2026.1902833

---

### Notes for the author, delete this section before you send it to Morgan

1. **Section 2 is built from what you told me.** UX designer, upskilling in
   automation, agentics, LLMs, local models, VPSes and MCP, taking the
   residency to build enterprise-ready products. Read it and make sure it
   sounds like you. §2.4 in particular should be your own words, since I wrote
   a version of what you said and it is the most personal paragraph in the
   paper.

2. **Anthropic authorship.** The agents post lists "Erik S. and Barry Zhang."
   Because the first author has no full surname, I used APA's corporate-author
   form, which is the normal fix. Don't invent a surname.

3. **Undated sources.** The Google and llama.cpp entries are living pages with
   no publication date, so APA's n.d. plus a retrieval date is correct.

4. **The NN/g survey is from 2023.** That is three years old, and I say so in
   the text rather than implying it is current. The age actually helps the
   argument, since adoption was already near-total before agents were usable.

5. **Links re-checked 23 October 2026.** All eleven resolve. The Wiley and SAGE
   links block automated checking but open fine in a browser, and both were
   confirmed against Crossref. The old Google Ads policy link was dead and has
   been replaced with the Google Ads API RMF documentation page, which is the
   more precise source anyway.

6. **Section 8 was rewritten on 23 October 2026** for the learning-system
   project. Sections 1 through 7 and 9 were originally written for the earlier
   ads project but are about the specialization field rather than the product,
   so they still stand. Read §8 against §4 and make sure you can defend the
   connections as yours.

7. **The reversibility framing is my synthesis**, not a named framework you can
   point to in the literature. The sources support each piece, but the way it
   is assembled is the paper's own argument. Be ready to defend it as yours,
   because you may be asked.

8. **What changed in this pass.** Every em dash, arrow, and sentence-level
   colon is gone. Fragments that stood alone as paragraphs have been folded
   into real paragraphs. The bulleted lists in §4.3, §5.2, §7.2, and §8.2 are
   now prose. The ad-budget example in §4.2 became a customer-email example
   that needs no ads context. The commerce-platform aside in §3.4 became the
   MCP finding from this project, which is both true and relevant. §4.4 and
   §8.3 now state plainly that the earlier version of the project was an ads
   tool, so the Google policy reference has context. The conclusion no longer
   names Google and Meta.
