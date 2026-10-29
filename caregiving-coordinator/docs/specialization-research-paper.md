# Research Paper v2 — Agentic Workflows and AI Automation (Jose Castillo, Week 2 Premium)

**Local cached copy.** Source of truth is the live Google Doc:
https://docs.google.com/document/d/1GYrhCw27y_LJdjBb03EN9KgD4inojMQ21TpzX-wJrLc/edit
**Pulled into this project:** 2026-10-28. Written originally for the `adhd-learning-app` project;
Sections 1-7 and 9 (the specialization field itself) transfer as-is. Section 8 ("The Application
I Will Build") and the short illustrative example in Section 1.2 are still about the ADHD
learning app and need to be rewritten for caregiving-coordinator — see the review notes at the
bottom of this file, added when this copy was pulled in.

---

# **Agentic Workflows and AI Automation: How Software Learned to Decide, and Why UX Designers Need to Understand It**

**Author:** Jose Castillo

**Course:** Tech Fleet AI Development Residency, Fall/Winter 2026 (Premium Track)

**Instructor:** Morgan Denner

**Date:** October 2026

**Specialization areas:** AI Automation + Advanced Agentic Workflows (combined)

## -----

## **Abstract**

This paper explains what agentic workflows and AI automation are, how they work, and what a person needs to learn to build with them. AI automation is the work that finishes without a person doing it. Agentic workflows are the main method people use to reach that goal today.

My argument is that the hard part of this field is no longer getting software to act on its own. The hard part is deciding how much the software should be allowed to decide by itself, and then proving it can be trusted with that much. The paper ends by applying these ideas to the application I am building for this residency.

## -----

## **A short glossary first**

This field is full of jargon, and most of it sounds more complicated than it is. These are the words I use in this paper, in plain terms.

| Term | What it means |
| :-- | :-- |
| **LLM** (large language model) | An AI program that produces text by predicting what word should come next. It learned how to do that from an enormous amount of writing. Claude and ChatGPT are LLMs. |
| **Training** | The process that builds a model, by showing it huge amounts of text and adjusting it until its predictions get good. It happens once, before anyone uses the model, and it is expensive. |
| **Model weights** | The numbers inside a finished model. Training is what sets those numbers, so the weights are everything the model learned. Copy the weights and you have copied the model. |
| **Open-weight model** | A model whose company published the weights file, so anyone can download it and run the model themselves. The opposite is a closed model, which you can only use by sending requests to the company's servers. |
| **Local model** | A model running on hardware you control, like your own laptop or a server you rent, instead of running on the model company's servers. |
| **Inference** | Using a finished model. Training is when the model learns. Inference is every time after that, when you give it input and it gives you output. |
| **Tool** | One specific action you give a model permission to take, like "look up this order number" or "send this email." On its own a model can only produce text. A tool is how it gets to make something happen. |
| **Tool use** | When a model answers a request by calling one of its tools instead of just writing a reply. |
| **MCP** (Model Context Protocol) | A shared format for describing tools, so any model that speaks it can connect to any tool that speaks it. The tool is the action. MCP is the standard plug. Before MCP, every pairing of a model and a tool needed its own custom code. |
| **Workflow** | A system where a person wrote down the steps ahead of time. The model does one defined job inside a step, but it does not get to change the order or skip ahead. |
| **Agent** | A system where you give the model a goal instead of steps, and it picks its own steps while it runs. |
| **Orchestration** | The code that coordinates the steps, tools, and models, so they run in the right order and hand information to each other correctly. |
| **Eval** (evaluation) | A test that measures whether an AI system's output is any good. Normal software tests check right against wrong. Evals have to handle output where quality is a judgment call. |
| **Guardrail** | A hard limit built into the system that blocks an action no matter what the model decides. |
| **Human in the loop** | A design where the software stops and waits for a person to approve something before it continues. |
| **VPS** (virtual private server) | A computer you rent in someone else's data center and run yourself. |
| **API** | A published list of requests a company's software will accept, so other software can ask it for data or ask it to do something. |

## -----

## **1. Introduction to the Subject**

### **1.1 Automations are not new**

People have been writing scripts to handle boring work for years. The old kind had one defining limit that couldn't understand anything. Picture a script that emails you a sales report every Monday. A person decides what belongs in that report, and the script repeats that decision forever. If something odd turns up in the data, like a strange refund or a currency nobody planned for, the script does not react. It was never built to react. It does the one thing it was told to do. That made old automation extremely predictable. You always knew what it would do, because somebody wrote down every step in advance. This system made automations very vulnerable to problems because the moment reality stopped matching the plan, it either broke or produced nonsense.

### **1.2 What changed when models could use tools**

LLMs broke that limit. An LLM can read material it has never encountered before and respond sensibly to it, and once you give it tools, it can search a database, read a file, or call an API, and something genuinely new becomes possible. You can stop handing the software a procedure and begin handing it a goal instead. Anthropic (2024a) defines two ways of building on that capability. Workflows, in their account, are "systems where LLMs and tools are orchestrated through predefined code paths," whereas agents are "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." The practical difference comes down to who sequences the work. In a workflow the developer decides the steps and the model fills in the blanks, while in an agent the model determines its own steps as it runs.

The application I am developing for this residency (described in full in Section 8) is a coordination tool for family caregivers managing a parent's health. A family member records a doctor's visit on their phone, and the application converts that recording into a structured note — what the doctor said, recommended, or warned about — stored in one place every sibling can read.

Built as a workflow, that conversion would run as a fixed sequence defined in advance: transcribe the audio, pull out any sentence containing a medication name, format the result into a template. The model would contribute only the transcription and the sentence extraction, and the order of operations would never vary. Built as an agent, the system reads the whole conversation and decides for itself what was actually important enough to record, the way a person listening in the room would. The behavior is far less predictable, but it is also the only version capable of noticing something a fixed template never anticipated — a new diagnosis mentioned in passing, or a warning about a drug interaction that was not on the day's agenda.

### **1.3 The trade this creates**

The agent version is more flexible. It handles the strange email that the workflow would have mangled. But look at what you gave up. You no longer know what your software is going to do. A system that picks its own steps can pick a step you never considered, including a wrong one, a wasteful one, or a harmful one.

That is the trade at the center of this specialization. More freedom means the system copes with more situations and gives you fewer guarantees about its behavior. Every genuinely hard question in this field comes out of that one trade.

So the useful question is almost never "can the AI do this?" Increasingly it can. The useful question is how much it should be allowed to do by itself, and how anyone would find out if you got that wrong.

### **1.4 Why I combined the two specializations**

AI automation is the outcome, meaning work that gets finished without a person doing it. Agentic workflows are the method that currently gets you there on tasks too messy to script in advance.

Study the method without the outcome and you get a clever demo nobody uses. Chase the outcome without understanding the method and you get a system that passes testing, then does something expensive and surprising in production. Gartner has forecast that more than 40% of agentic AI projects will be cancelled by the end of 2027, pointing to rising costs, unclear business value, and weak risk controls.[1] Two of those three causes have nothing to do with the technology. They are planning failures.

## -----**2. Why This Is Relevant to My Career**

I am a UX designer. I have been upskilling in AI, starting with automation and moving into the deeper layers: agentic systems, LLMs, local models, virtual private servers, and MCP. I am taking this residency because I want to build enterprise-ready products, not prototypes. The reason is simple. UX designers now have to know how to build.

That is not a prediction. It is already happening, and the evidence comes from my own field's research.

### **2.1 My field already adopted these tools**

Nielsen Norman Group surveyed 841 UX professionals in July and August of 2023. They found that "92% of the respondents claimed they had used at least one generative AI tool," and among those using AI for work, 63% used it at least several times a week (Liu, Zhang, & Budiu, 2023).

That was three years ago, before agents were practical. Adoption in my field was effectively total before the technology even got interesting. For a designer today the question is not whether to use AI. It is whether to understand what you are using.

### **2.2 The handoff is disappearing, and that is the real change**

UX has always worked through a handoff. A designer figures out what should exist and describes it. An engineer builds it. The description was the designer's deliverable, and the gap between describing and building is why two roles existed in the first place.

Agentic tooling is closing that gap. Someone who can describe intent precisely enough can increasingly produce the working thing. This does not mean engineering knowledge stops mattering. It means engineering knowledge stops being optional for designers. If I can build what I design, the limit on my work is no longer whether anyone has capacity to build it. The limit is whether I understand what I am asking for well enough to be responsible for it.

### **2.3 What I bring that is actually scarce here**

The hardest part of this field is not writing the code. It is deciding what the software should be allowed to decide, and designing the moments where it stops and asks a person.

That is a design problem. Where does the approval step go? How do you show someone a decision the AI made, in a form they can judge and argue with? How much friction protects the user, and how much friction only makes the tool annoying enough to abandon? Those are questions about human judgment under uncertainty, and UX research is the discipline built to study them.

A system nobody can understand cannot be trusted. A system nobody trusts does not get to run on its own. So explainability is not a nice feature added at the end. It is the thing that decides how much automation you are allowed to have. That puts design inside the engineering rather than on top of it.

### **2.4 What I want to be able to do by the end**

I want to take a product from nothing to something real people use. Specify it, build it, deploy it, secure it, and judge honestly whether it works. Not a mockup, and not a demo that falls apart on real data. The specific test I care about is building something that handles real money or real customer data, and being able to defend the decisions inside it to someone technical who disagrees with me.

## -----**3. Background About the Specialization**

How the field got here, in four steps.

### **3.1 Scripts that followed orders**

Classic automation. A person wrote down every step. Reliable and brittle, as described in §1.1. It is still the right answer for a great many problems, which is worth remembering later.

### **3.2 Models that could read and write**

LLMs arrived and could handle language they had never seen before. Early on, though, they were sealed off from everything. A model could write a good summary of a sales report you pasted in, and had no way to go fetch that report itself. It could think without acting.

### **3.3 Tools, and the integration problem**

Then models were given tools. That was the real unlock. A model that can pick a tool and read the result can be handed a goal instead of a procedure.

It also created a grubby practical problem. Every tool needed its own custom glue code. Connecting a model to a database, then Slack, then Google Drive meant writing three separate integrations, and everybody building agents was writing the same glue over and over. Anthropic (2024b) described models as "trapped behind information silos and legacy systems."

### **3.4 One standard instead of custom glue**

The Model Context Protocol, released 25 November 2024, proposed a single standard way to plug tools and data into AI systems. Anthropic (2024b) called it "a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments." Instead of custom glue for every connection, you implement the protocol once.

Something important follows. Once connecting things got easy, the leftover hard problem became whether to connect them at all, and how much authority to grant once connected. Fixing the plumbing exposed the governance question underneath, and that question is where the field sits right now.

One caution from my own research. A standard way to connect is not the same as having something worth connecting to. While scoping an earlier version of this project I checked five commerce platforms and found that none of their official MCP servers exposed the sales or ad spend data I actually needed. The standard existing and the data being available are two separate facts, and you have to check both.

### **3.5 What the field learned along the way**

Anthropic (2024a) documents five reusable patterns for building these systems: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. They report that the teams who succeeded used simple composable patterns rather than heavy frameworks, and they advise adding complexity "*only* when it demonstrably improves outcomes," because agentic systems "often trade latency and cost for better task performance."

That advice deserves attention for an odd reason. The company selling the models is telling developers to use less autonomy than they probably think they need. When a vendor's advice cuts against their own sales incentive, it is usually worth taking seriously.

A safety and governance literature grew alongside the technical work. NIST published the *Artificial Intelligence Risk Management Framework* on 26 January 2023, built around four functions, Govern, Map, Measure, and Manage, for voluntary use (NIST, 2023). It predates the agent wave but saw the central issue early. You cannot judge whether an AI system is safe by looking at the model alone, because the danger depends on what the system is wired up to do.

## -----**4. How It Works When Building Products**

### **4.1 The first decision: workflow or agent?**

This is the choice you make most often, and the most common mistake is making it once for the whole product. Real systems are mixed. You choose per piece.

A rough rule. Use a workflow when you already know the steps and being predictable matters more than being flexible. Use an agent when you cannot write down the steps in advance, because the inputs vary too much.

And one rule that saves a lot of pain. If a task has exactly one correct answer, do not use an LLM for it. Arithmetic is the clearest case. If you need revenue minus costs, write the subtraction. An LLM can do arithmetic, but it introduces the possibility of variation into something with a single right answer, and you get nothing in exchange. Anthropic's (2024a) advice about only adding complexity where it demonstrably helps applies directly.

### **4.2 The second decision: how much can it do without asking?**

Once you have an agent, you have to decide what it may do on its own, what it must get approved, and what it may never touch.

The useful question is not how smart the model is. It is whether you can undo what it did.

Compare two mistakes. In the first, the AI mislabels a support ticket. Somebody notices and fixes it, and the cost is a few minutes. In the second, the AI spends $4,000 of a client's ad budget on the wrong campaign. That money is gone, and the only way to fix it is to spend more money.

The first mistake is reversible and the second is not. You can clean up reversible mistakes after they happen. Irreversible ones have to be stopped before they happen.

So the design rule is to put the brakes where actions cannot be undone, not where the task is hard. An easy action that spends money needs a stricter gate than a hard action that produces a draft for review.

Anthropic (2024a) describes the mechanisms: "extensive testing in sandboxed environments, along with the appropriate guardrails," having agents "pause for human feedback at checkpoints or when encountering blockers," and setting "stopping conditions (such as a maximum number of iterations) to maintain control."

One more thing about this limit matters a great deal and is easy to miss. It does not get looser as models improve. A better model is wrong less often. It is not wrong less expensively. If spending the wrong $4,000 is unacceptable, it stays unacceptable no matter how good the model gets. Waiting for the next model release does not solve this category of problem.

### **4.3 The third decision: how do you know it works?**

You cannot responsibly give a system freedom if you cannot measure whether it uses that freedom well. That is what evals are for.

Husain (2024) argues that failed AI products share "a failure to create robust evaluation systems," and lays out three levels:

1. **Unit tests.** Fast, cheap checks on specific cases, run constantly.
2. **Human and model evaluation.** Log what the system actually did, have people review it, then train an automated judge and check that judge against the human verdicts.
3. **A/B testing.** Compare real user outcomes, once the product is mature.

He also makes a point that reorders how you work. Error analysis comes first. Looking at real failures is what tells you which tests are worth writing. You do not start by guessing what might break. You start by seeing what did break.

The practical consequence is that you cannot grant more autonomy than your evals can verify. A team without that measurement has no idea where its limit sits, so it cannot know whether it has crossed it.

### **4.4 The limit engineering cannot move**

There is one more constraint, and it surprises people because it is not technical at all.

When your system runs on top of someone else's platform, whether that is Google, Meta, Amazon, or Shopify, that platform's terms of service decide what you are allowed to do. Those terms are written by them, can change without your agreement, and sometimes forbid things that are both easy to build and perfectly reasonable.

No amount of good engineering raises this limit.

A real example from my own project research. Google's Required Minimum Functionality policy sorts tools into categories, and tools that fully manage advertiser accounts have to provide a long list of features whether or not those features fit the product's concept (Google, n.d.). A product can be forced to grow in scope by policy rather than by choice.

I raise this in a paper about method because it changes how you sequence work. Platform rules have to be read during design, not after building. Discovering them late can invalidate the architecture you already built.

## -----**5. What the Specialization Includes**

Seven areas of competence.

### **5.1 Choosing the architecture**

Deciding, piece by piece, what is a workflow and what is an agent (§4.1), and using the five known patterns instead of inventing structure from scratch (Anthropic, 2024a).

### **5.2 Models: cloud or local**

Most people start with a model running on someone else's servers, reached through an API. That is the fastest path and usually the cheapest at low volume.

You can also run models on your own hardware. Open-weight models can be downloaded and run locally. The project that made this practical on ordinary computers is llama.cpp, whose stated goal is "to enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware, locally and in the cloud" (ggml-org, n.d.).

Three honest reasons to run a model locally:

1. **Privacy.** The data never leaves your machine. For regulated data, or a client who will not allow their records sent to a third party, this can be the only acceptable option.
2. **Cost at volume.** No per-token bill. For light use a cloud API is cheaper. At high steady volume, owning the hardware can win.
3. **Working offline, and not depending on a vendor.** Nobody can change your pricing, deprecate your model, or rate-limit you.

The trade-off is real. Local models are usually less capable than the best cloud models, and you take on running the infrastructure yourself. Licences also vary between model families and need reading before commercial use.

### **5.3 Connecting to the outside world**

Tool use, MCP, direct APIs, and authentication. The unglamorous part is handling things going wrong: rate limits, data formats that change without warning, credentials expiring. In production those are normal conditions rather than rare exceptions, and a system that assumes the happy path will fail constantly.

### **5.4 Deploying and running it**

An agent that only runs on your laptop is not a product. This is where VPSes, hosting platforms, databases, and scheduled jobs come in. Agentic systems add a wrinkle to ordinary deployment. They run unattended, they cost money per run, and they can loop. So you need spend limits, timeouts, and logs that record not only what happened but why the system chose it.

### **5.5 Evaluation**

Building the measurement described in §4.3, with error analysis first (Husain, 2024).

### **5.6 Guardrails and human-in-the-loop design**

Building the brakes: approval steps, sandboxes, stopping conditions, spend caps, and previews of anything that cannot be undone. This is a safety problem and a usability problem at the same time, because a gate placed badly either fails to prevent the costly mistake or annoys the user into working around it.

### **5.7 Governance and documentation**

Reading platform terms against what you plan to build. Writing down autonomy decisions so they can be reviewed later. NIST's (2023) Govern, Map, Measure, Manage structure gives a frame for this. In a system where the software makes decisions, the written record of which decisions you delegated, and why, is primary documentation rather than paperwork.

## -----**6. What Teams Actually Do in This Specialization**

This work is unusually cross-functional, for a structural reason. The limits on autonomy are owned by different parts of an organization. Engineering knows what the system can do. The business knows what a mistake costs. Legal knows what the platforms permit. No single role can set the boundary alone, so a team without a shared forum for it ends up setting it by accident.

**Setting the autonomy boundary.** A recurring meeting that produces a written decision: what the system does automatically, what needs approval, what it must never do. Writing down the reasoning matters as much as the decision, because the reasoning is what you re-examine when a platform changes its rules.

**Error analysis sessions.** Going through logs of what the system actually did and finding the failure patterns. Husain (2024) treats this as the activity that determines which evals are worth building. It needs people who know the subject, not only engineers, because spotting a wrong answer in a specialized domain requires knowing the domain.

**Capturing expert judgment.** Sitting with someone who knows what good looks like and getting their standard into a form precise enough to automate, then checking the automated judge against real human verdicts. That is interviewing before it is engineering, which makes it a UX research skill.

**Reading platform terms.** Checking the rules against what you plan to build and writing down a determination. Genuinely unclear cases go to a lawyer rather than a developer's best guess.

**Incident review.** When the system does something wrong, fixing the immediate bug and also revisiting whether it should have had that much freedom. Gartner has forecast that by 2027, 40% of enterprises will demote or shut down autonomous agents because of governance gaps found only after something went wrong in production.[1] "Found only after" describes a team that never held the boundary conversation up front.

**Designing the human moments.** Building the screens where a person reviews what the AI decided, and making the reasoning legible enough to argue with. That is design work, and it gates how much automation the product is permitted to have.

## -----**7. Tools and Skills to Learn**

### **7.1 Tools**

| Category | Tools | What it is for |
| :-- | :-- | :-- |
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

### **7.2 Skills**

**Technical**

- Reading API documentation carefully, including the boring parts about rate limits and errors.
- Designing data that can represent "we don't know." A system that stores zero when it means unknown will state a confident wrong answer, which is worse than admitting a gap.
- Handling credentials and authentication for software talking to software, where there is no person available to click "allow."
- Writing evals.
- Logging decisions so you can reconstruct why the system did what it did.

**Analytical**

- Asking whether something can be undone before asking whether it can be automated.
- Reading terms of service adversarially. What does this clause forbid, not what did the author probably mean.
- Telling the difference between a problem that needs an agent and a problem that needs twenty lines of ordinary code.

**Communication**

- Explaining a system's decision to someone non-technical in terms they can actually push back on. As argued in §2.3, that is a functional requirement rather than politeness.

**Dispositional**

- Restraint. Anthropic's (2024a) advice to add complexity only where it demonstrably helps is a habit before it is a technique, and it runs against the natural pull toward building the most autonomous thing you can.

## -----**8. The Application I Will Build**

### **8.1 The problem**

I have been my father's primary caregiver for three years, after he had open-heart surgery for a torn valve. The hardest problem was never any single task. It was that the information about his care lived in a different place depending on who you asked. I recorded his doctor visits myself and sent the audio to my sisters. I kept his current and discontinued medications in a Google Sheet. Appointments got arranged over text, and lost in it just as often. When he felt off in some way that lasted for a year, figuring out whether it was a medication side effect meant reconstructing his drug history from memory and a spreadsheet, under time pressure, because the next appointment was already on the calendar.

I tried to fix this myself before this residency. I built a shared Google account for my father with his medication list and a calendar my siblings could all see. Almost nobody used it. Updating the medication list felt like too much friction to the people who were not the one managing it day to day, so the work quietly reverted to me, and eventually I stopped maintaining parts of it too. That failure is the actual starting point for this project, not a hypothetical risk. A coordination tool that requires everyone to remember to log in and update something will get used by exactly one person until that person burns out, which is precisely what already happened.

### **8.2 What the system does**

A family member records a doctor's visit on their phone. The system turns that recording into a structured note — what the doctor said, recommended, or warned about — and adds it to one shared record every family member can read, with a notification that something new was added.

Everything else is built around that shared record:

1. **Medication timeline.** Every medication mentioned in a visit note, with dosage, instructions, the date it started, and the date it was discontinued if it was. Not just a current list — a history, because the history is what let me previously figure out that a side effect lasting months lined up with a drug my father had started around the same time.
2. **Tasks, not just a calendar.** A follow-up appointment mentioned in a visit note becomes an open task, not a line on a calendar nobody checks. Any sibling can claim it. If whoever claimed it has to cancel, they do that in the app and it reopens for someone else, with a text and an email going out either way.
3. **Vitals.** For families using a device like an Apple Watch, baseline readings sync automatically. If something falls outside a set range, the family is notified to check in.
4. **Shared health literacy.** Short, AI-curated explanations of what to watch for, specific to the parent's actual diagnosis, each one linked to the real source it came from, with a simple mark-as-read per person so the family can see who has actually gone through it.

### **8.3 How the specialization shows up in it**

This is where the ideas from §4 turn into concrete design decisions, the same way the old version of this section did for a learning app — the application changed, but the four decisions did not.

**The parts that must not be agents.** Task state, reminders, and vitals thresholds are plain rules, not model judgment, for the same reason the old version of this paper kept its scheduler deterministic (§4.1): there is a defensible correct answer, and putting an LLM there adds variation and buys nothing. "Has this task been claimed," "is this reading outside the set range," and "has the reminder window passed" are all questions with one right answer, computed the same way every time.

**The parts that must be agents.** Turning an unstructured recording into a structured note is judgment that resists being written down in advance, exactly like the old paper's note-placement problem in §1.2's new version. So is drafting a short list of questions to bring to an upcoming appointment based on what has happened since the last one, and curating which health-literacy topics actually matter for this specific diagnosis.

**Where the "can we undo it?" rule bites, and why it is worse here than in the old version.** The old paper's sharpest example of an irreversible mistake was an agent spending $4,000 of someone else's ad budget. This project's version is not better. If the note-extraction agent drops or misstates something a doctor actually said, and a family member repeats that misstatement to another provider, the mistake does not have a clean undo the way a refunded ad spend does.

This is not a hypothetical risk I am inventing for the paper. A 2026 narrative review of ambient AI scribes in clinical settings found error rates as high as 70% of AI-generated notes containing at least one error, with 10.5% of all errors being outright fabrications — content the AI added that nobody actually said (Razaghi et al., 2026). The same review is explicit that "the responsibility for the final accuracy and safety of the medical record remains non-negotiably with the clinician" (Razaghi et al., 2026) — in this product, with the family member who reviews it, not the model.

It gets harder than that. A 2026 study on auditing AI clinical notes found that automated judges are much better at catching content that was added and should not have been than at catching content that was left out: 0.79-0.94 discrimination on fabrications, but only 0.50-0.63 on omissions (Fox, Markham, Lail, & Karotsieris, 2026). An omission in a caregiving context is not a minor gap. A missed mention of a drug interaction warning is exactly the kind of thing that matters most and is hardest to catch automatically. The design response has to follow Husain's (2024) point directly: error analysis, meaning real review of what the system actually missed, has to come before deciding the eval is good enough, and the eval itself has to be built to specifically check for completeness, not only accuracy.

**Where the vitals-alert brake bites.** The equivalent risk on the vitals side is not fabrication, it is being ignored. Hospital alarm systems are extensively documented to produce non-actionable alerts more than 70% of the time, and the well-established finding across that literature is that clinicians become desensitized and start missing real events buried in the noise (Chromik et al., 2022). A family is not clinically trained and has far less patience for false alarms than a hospital staff does. A vitals feature that alerts too often will be tuned out exactly the way hospital staff tune out hospital alarms, and the first real event it correctly flags is the one nobody will believe. This makes alert precision a harder requirement here than almost anywhere else in the product, not a tuning detail to improve later.

**Where platform rules bite.** Vitals data from a device like an Apple Watch runs through Apple's HealthKit, and Apple's own App Review Guidelines restrict what an app may do with that data: health, fitness, and medical data obtained through HealthKit may not be used for advertising, marketing, or other data-mining purposes, and an app that behaves like a medical device triggers a stricter review (Apple Inc., n.d.). None of that is a problem for this product's actual design, since nothing here is advertising-funded or diagnostic, but it does mean the vitals feature has to be built and described carefully enough to not read as a medical device to begin with, which affects how the alert feature is worded in the product itself, not only in a store listing. The same caution applies to insurance and pharmacy portal access: those portals' own terms of service govern what any integration may do, and I have not yet verified what any of them actually allow, which is an open question for the build, not a settled one.

### **8.4 Why this app fits the specialization**

It forces the same four decisions the old version of this paper made for a learning app, and in every case the caregiving version raises the stakes rather than lowering them. The task/vitals-threshold logic has to be deterministic and the note-extraction has to be agentic, so §4.1 is unavoidable. The cost of an unreviewed mistake is a family acting on a wrong or incomplete medical note, which is a harder brake to design than a spending cap, so §4.2 is unavoidable. The central claim, that the extracted note is accurate and complete, is specifically the thing current research shows automated checking is worst at verifying, so §4.3 is unavoidable. And the vitals and credential-sharing features sit on top of Apple's and third parties' own rules, so §4.4 is unavoidable.

It also needs the design skill I already have, for the same reason as before. A family that does not understand why the system flagged something, or why it did not, will either over-trust it or abandon it the first time it is wrong. The explanation of what the system is and is not confident about is not a feature added on top. It is the product.

## -----**9. Conclusion**

The skill that defines this specialization is not making software that acts on its own. That has become the easy part.

The skill is deciding how much the software is allowed to decide, and being able to show why that amount is right. That decision rests on three things: whether you can measure that the system does the job well, whether a mistake can be undone, and whether the platforms you depend on even permit it.

Two of those do not improve with better technology. A stronger model makes costly mistakes rarer, not cheaper, so wherever an action cannot be reversed the brake stays. And no model, however good, changes what Google's or Meta's terms allow. Both are permanent parts of the design problem rather than temporary limits waiting on the next release.

Gartner's forecast that over 40% of agentic projects will be cancelled by the end of 2027 blames unclear business value and weak risk controls far more than weak models.[1] If that is right, then the bottleneck in this field is not what AI can do. It is whether the people building it thought carefully enough about what it should be allowed to do, which is, in the end, a design question.

## -----

## **Notes**

**[1] Source verification note (updated 2026-10-28).** Gartner's newsroom still returns HTTP 403 to automated retrieval, so the original press releases could not be read directly. However, each of the three figures is now corroborated by multiple independent outlets reporting on a specific, named, dated Gartner release: "40% of enterprise apps will feature task-specific AI agents by 2026, up from less than 5% in 2025" (Gartner press release, 2025-08-26); "over 40% of agentic AI projects will be canceled by end of 2027," attributed to rising costs, unclear business value, and weak risk controls (Gartner press release, 2025-06-25); and "40% of enterprises will demote or decommission autonomous AI agents by 2027" due to governance gaps found only after production incidents (Gartner press release, 2026-05-26). The figures are reasonably well-supported as real, dated Gartner predictions, though still not independently confirmed against Gartner's own page text.

## -----**References**

Anthropic. (2024a, December 19). *Building effective AI agents*. https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024b, November 25). *Introducing the Model Context Protocol*. https://www.anthropic.com/news/model-context-protocol

Apple Inc. (n.d.). *App Review Guidelines*. Apple Developer. Retrieved October 28, 2026, from https://developer.apple.com/app-store/review/guidelines/

Chromik, J., Klopfenstein, S. A. I., Pfitzner, B., Sinno, Z.-C., Arnrich, B., Balzer, F., & Poncette, A.-S. (2022). Computational approaches to alleviate alarm fatigue in intensive care medicine: A systematic literature review. *Frontiers in Digital Health, 4*, Article 843747. https://doi.org/10.3389/fdgth.2022.843747

Fox, S., Markham, L., Lail, R., & Karotsieris, M. (2026). *LLM judges verify presence, not absence: Omission blindness in AI clinical notes and what recovers it*. arXiv. https://arxiv.org/abs/2608.31016

ggml-org. (n.d.). *llama.cpp* [Computer software]. GitHub. Retrieved October 23, 2026, from https://github.com/ggml-org/llama.cpp

Google. (n.d.). *Required Minimum Functionality (RMF)*. Google Ads API documentation. Retrieved October 23, 2026, from https://developers.google.com/google-ads/api/docs/api-policy/rmf

Husain, H. (2024, March 29). *Your AI product needs evals*. https://hamel.dev/blog/posts/evals/

Liu, F., Zhang, M., & Budiu, R. (2023, October 27). *AI as a UX assistant*. Nielsen Norman Group. https://www.nngroup.com/articles/ai-roles-ux/

National Institute of Standards and Technology. (2023, January 26). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). U.S. Department of Commerce. https://www.nist.gov/itl/ai-risk-management-framework

Razaghi, M., Hafez, A., Farina, J. M., Scalia, I. G., Pereyra, M., Abdelfattah, F. E., Sheashaa, H., Awad, K., Lester, S. J., Ayoub, C., & Arsanjani, R. (2026). Transforming clinical documentation with ambient artificial intelligence (AI) scribes: A narrative review of technology, impact, and implementation. *Cardiovascular Diagnosis and Therapy, 16*(1), 11. https://doi.org/10.21037/cdt-2025-454

---

## Review notes (added 2026-10-28, when this copy was pulled into caregiving-coordinator)

**What's strong and did not change:** Sections 1 (minus the §1.2 illustrative paragraph), 2, 3, 4,
5, 6, 7, and 9 are about the specialization field itself, not about any specific app. They were
already well-sourced and adversarially fact-checked (per the deleted author's-notes section), and
carried over to caregiving-coordinator without modification.

**What was rewritten (done 2026-10-28):**

1. **§1.2's illustrative paragraph** — replaced the old notes→practice-questions example with a
   caregiving-coordinator one: a recorded doctor's visit → structured note extraction → shared
   family record, consistent with the rewritten §8.
2. **All of §8** — fully rewritten for caregiving-coordinator, applying the same four decisions
   (§4.1-§4.4): the task/vitals-threshold logic stays deterministic (same reasoning as the old
   paper's scheduler); visit-note extraction, visit-prep drafting, and health-literacy curation
   are the genuinely agentic pieces; the "can we undo it?" brake is argued as *worse* here than
   the old paper's $4,000 ad-spend example, not just equivalent, since an inaccurate medical note
   repeated to another provider has no clean undo; and the platform-risk section covers Apple's
   HealthKit data-use restrictions and medical-device review trigger, plus the open question of
   what insurance/pharmacy portal terms of service actually allow.
3. **The learning-specific citations in the old §8.3** (metacognitive laziness, the Paas 1992
   cognitive-load scale, spaced-repetition adherence stats) were removed — they didn't transfer.
   Replaced with real, verified sources for the two caregiving-specific risks: a 2026 peer-reviewed
   review of AI clinical-scribe hallucination/omission rates (Razaghi et al., 2026), a 2026 paper
   on automated judges being much worse at catching omissions than fabrications in clinical notes
   (Fox et al., 2026), and a systematic review of alarm fatigue in clinical monitoring (Chromik et
   al., 2022) for the vitals-alert risk. Apple's own App Review Guidelines (Apple Inc., n.d.) were
   added for the platform-risk section, the same way the original paper cited Google's policy page
   directly rather than an academic source.
4. **Not yet verified:** what insurance and pharmacy portal terms of service actually permit for
   a credential-sharing or access-tracking feature — flagged as an open question in §8.3, not
   invented.
5. **Still needs doing before submission:** the original Google Doc has a "Notes for the author:
   DELETE THIS SECTION BEFORE YOU SEND IT TO MORGAN" section at the very end, containing internal
   editorial notes. It was never included in this local copy — confirm it's also removed from the
   live Google Doc, and copy this rewritten §1.2/§8 and the updated reference list back into the
   Doc before submitting.
