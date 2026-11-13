# Week 1 - Introduction Lecture Notes
- Source copy: https://app.notion.com/p/1ed9219a469182dca2b701f3dd13723d
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:09:28.626Z
- Not saved: images (wk1-definitions.png, wk1-how-to-build.png, wk1-brain.png, wk1-what-you-need.png, wk1-lifecycle.png, wk1-agile-philosophies.png, wk1-building-with-agile.png, wk1-agile-vs-waterfall.png, wk1-release-cycles.png, wk1-network-architecture.png, wk1-how-the-web-works.png, wk1-how-ai-works.png); the FigJam board and Google NotebookLM links were not followed. Linked transcript saved separately as "Week 1 AI Dev Residency Lecture Transcript (Notion copy 2026-11-13).md"

---

> Extracted from the FigJam board "Fall 2026 AI Development Residency – Class Lecture and Working Sessions." Faithful transcription of every Week 1 section, in board order. Checklists are also provided as clean PNG files; board memes/diagrams are described inline.

# AI Dev Residency Notebook

Use AI to crunch through the lecture content, transcript, and notes.

[notebook.google.com](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab?authuser=1)

# Transcript

Week 1 AI Dev Residency Lecture Transcript

# FigJam Board

[https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=4-2269&t=XS6vaekeSphGWjfU-1](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=4-2269&t=XS6vaekeSphGWjfU-1)

# Definitions — Vibe Coding vs Enterprise Coding

[video/file not saved: wk1-definitions.png]

**Let's get this straight: What is Vibe Coding? And how is it different from Enterprise Coding?**

### Vibe Coding (verb)

Publishing code by typing a prompt into AI tools and letting the AI build the whole thing without your guidance, relying on the decisions the AI makes itself.

- **Risks:** Hackable applications; exposed user data; bugs that make the app unusable; deplorable experience for users; lost revenue, going out of business; exposed private data.
- **Common tasks:** Building AI prompts for instructions to design or code; refining the result with a prompt based on what you see; evaluating the result produced.
- **Common tools:** Lovable; Replit; Chat GPT; Claude Code; Claude Design.
- **NOT good for:** Building a product that many people use; scaling a business; making a product people pay for.
- **Good for:** Rapid prototypes; concept testing; ideation.

### Enterprise AI Development (noun)

Publishing code with AI agent coding that follows the rigors of what makes applications scale to millions of users, perform well, and be secure.

- **Risks:** More rigorous workflows; more time to produce the right product; costs a lot more credits than Vibe Coding.
- **Common tasks:** Selecting software patterns; requirements specifications; technical architecture; secure feature coding; data engineering; building network architecture; security testing.
- **Common tools:** Human knowledge; security testing tools; database server tools; web hosting tools; API libraries; AI agent tools.
- **NOT good for:** Building testable concepts.
- **Good for:** Software used by millions; bug-free code; supporting teams of multiple developers and product people; meeting data-privacy regulations; building automation into business workflows.

*Board images: four memes — "VIBE CODED APPS GOING TO PRODUCTION (0 VULNERABILITIES)" (dishwasher); "vibe coders be like"; "VIBE CODING / VULNERABILITY AS A SERVICE"; a melting sandcastle labeled "VIBE CODING."*

## How to Build and Launch Products

[video/file not saved: wk1-how-to-build.png]

You have to manage the product to build and ship it. This takes both **user experience** and **product management**.

**The future of our work is way more multi-disciplinary — UX and Product Management are still at the heart of successfully making businesses that thrive:**

- Saving time performing tasks
- Doing more kinds of work than we were trained in
- Handling requirements, strategy, and operations
- Doing more relationship building and influence
- Delivering end-to-end experiences
- More business problem-solving
- More knowledge of full-stack development
- More automation
- Different kinds of UX (conversational, multi-modal, systems)

**You will learn all of the "green circles" in this class** — two overlapping skill families:

- *User Experience:* Interaction Design; Information Architecture; UX Writing; Customer Experience Design; Interface Design; Evaluative Research; Universal Design; Accessibility; Human-computer interaction; Voice Interface Design; UX Operations; UX Strategy; Generative Research; UX of AI Agents; Conversation Design; Systems Design.
- *Product Management:* Product Strategy; Requirements; Project Management; Roadmaps; Customer Segmentation; Development Operations; Quality Engineering; Price Modeling; Technical Architecture; Go-To-Market; Network Security; Data Analysis; Product Operations; Data Engineering; User Experience; Development; Information Security; Business Models; Network Technology.

### Reference: Skills & Practices Framework

| Area | What is it? | Example Deliverables |
| --- | --- | --- |
| User Experience | Making products easy, useful, pleasant; brings together research, design, content. | Wireframes; prototypes; research reports; design systems; journey maps |
| UX Writing | The words inside a product (buttons, menus, errors) — clear, friendly, consistent. | Style guide; voice & tone guide; UI copy; content inventory |
| UX of AI Agents | How people work with AI assistants so it feels natural and trustworthy. | AI prompt designs; conversation/task flows; prototypes; CX maps |
| Information Architecture | Organizing and labeling content so people can find things. | Site maps; card sorting; content inventory; navigation structure |
| Customer Experience Design | Shaping every interaction so the journey feels smooth. | Journey map; CX maps; service blueprints; personas |
| Interface Design | The screens people see and touch — layout, buttons, colors, icons. | UI kit; components; mockups; icons/logos; prototypes |
| Interaction Design | How a person and product respond to each other. | Wireframes; storyboards; clickable prototypes; task flows |
| Voice Interface Design | Products controlled by talking. | Voice flows; dialog scripts; voice prompts; prototypes |
| UX Operations | Tools/processes/standards that keep a UX team running. | Design-system governance; playbooks; working agreements; research ops |
| Accessibility | Products that work for everyone, including people with disabilities. | Accessibility audit; WCAG report; dev annotations; remediation checklist |
| Universal Design | Usable by as many people as possible without a special version. | Inclusive design guidelines; checklists; standards; principles |
| Generative Research | Early research to discover real needs before building. | Interview findings; personas; journey map; research plan; diary studies |
| Evaluative Research | Testing designs with real people. | Usability report; heuristics analysis; A/B results; UAT results |
| Human-computer interaction | How people and computers work together. | Interaction models; task analysis; study reports; findings |
| Conversational Design | The back-and-forth with chatbots/assistants. | Conversation flows; dialog scripts; chatbot prompts; task flows |
| UX Strategy | Big-picture plan for the experience. | UX vision/strategy; roadmap; feature vision; storyboards |
| Product Management | Deciding what to build and why, guiding idea → launch. | Roadmap; vision/strategy; release plan; epics/features; user stories |
| Data Engineering | Systems that collect, move, store data. | Data pipelines; schemas; data models; ETL |
| Go-To-Market | How a product reaches customers and lands at launch. | GTM strategy; marketing plan; positioning; buyer personas |
| Requirements | Capturing what a product needs to do. | Requirements docs; user stories; acceptance criteria; use cases |
| Product Strategy | Direction: what it's for, who it serves, how it wins. | Vision boards; vision/strategy; competitive analysis; positioning |
| Data Analysis | Turning data into insights. | Analytics reports; dashboards; stats summaries; insights |
| Roadmaps | What a product delivers over time. | Product roadmap; release plan |
| Product Operations | Tools/processes keeping the product team aligned. | Working agreements; backlogs; sprint plans; client intake; risk analysis |
| Quality Engineering | Making sure it works before customers get it. | QA test plan; test cases; automated tests; bug reports |
| Project Management | Coordinating people, time, tasks. | Project plan; schedule; status reports; risk log |
| Customer Segmentation | Grouping customers by needs/behaviors. | Segments; buyer personas; proto personas; market research |
| Business Models | How value is created and monetized. | Business plan; business model canvas; value props; revenue models |
| Price Modeling | What to charge and whether it works. | Pricing models; price testing; competitive pricing |
| Development Operations | Build/test/release smoothly and often. | CI/CD pipelines; deployment plans; automated tests; env configs |
| Information Security | Keeping data safe from hackers and leaks. | Security audit; threat model; protocols; pen-test report |
| Network Security | Protecting networks/connections. | Firewall configs; policies; pen-test report; incident response plan |
| Technical Architecture | The technical blueprint of the system. | Architecture diagram; architecture doc; ER diagrams; tech decisions |
| Development | Building the actual software. | Working code; REST APIs; documented code; deployed features |

## You Must Promise You Will Not Replace Your Brain With AI Tools — You Need Your Brain!

[video/file not saved: wk1-brain.png]

**DON'T DO THIS:**

- Don't replace your brain smarts with AI
- Don't trust AI's judgment
- Don't trust the output
- Don't stop giving it your own data
- Don't let it make the decisions for you
- Don't stop learning the fundamentals

**DO THIS INSTEAD:**

- Ask it to compare your results to authoritative literature
- Focus on defining the outcomes you want to achieve
- Provide context about content and structure
- Ask it for observable proof based on what it's telling you
- Ask it to teach you the steps and the knowledge
- Ask it to skeptically audit its own results

*Board image: a cartoon brain with a speech bubble — "Can haz neurons plz?"*

## What You Need Regardless of AI

[video/file not saved: wk1-what-you-need.png]

- **A solid foundation** about Engineering, Security, Operations
- **Problem-solving skills and critical thinking skills**
- **A specification system** that you track
- **Good organization** of your work
- **An agile mindset** to orchestrate your work
- **Great people skills** to build influence and collaborate

## What You Learn In This Class — Agile Product & Service Development Lifecycle

[video/file not saved: wk1-lifecycle.png]

The product lifecycle is how products and services get built in the world. Both types of research are required to produce products that meet user needs and solve problems. This class focuses on the parts that evaluate assumptions or evaluate solutions already made. Agile says deliver early and often. Evaluating solutions early and often is key to changing direction and delivering the right thing. Agile research focuses on **pattern analysis** — talking to smaller samples, forming patterns, each round quick, always building on the last.

**Lifecycle flow:** Project Goals → Success Measures → Kickoff → Hypotheses → Research → Analysis → (repeat) → Release Vision → Release Scope → Epics/Features/Tasks → Acceptance Criteria → Refinement → Plan → (in parallel) UX Research / UX Design / Development / Content → User Acceptance → QA → Feedback Collection → (repeat).

**Milestone meanings:** Project Goals (define high-level goals); Success Measures (define success); Kickoff (start with team/client); Hypotheses (form hypotheses for the work ahead); Research (research the hypotheses); Analysis (analyze, form problem-statement assumptions); Release Vision (near- and long-term problems in a release); Release Scope (outcomes per release); Epics/Features/Tasks (organize the backlog); Acceptance Criteria (instructions for delivery); Refinement (review with teammates/clients); Plan (when features/tasks get built); do Research/Design/Dev/Content in parallel; User Acceptance (review WIP with clients/users); QA (test for bugs); Feedback Collection (gather feedback and changes).

**Deliverables taught, by milestone:** Discovery/Kickoff — Team Ice Breakers, Project Plan, RACI Charts, KPIs, Client Intake, Team Process Definition, Stakeholder Interviews, Working Agreements, Case Study Outline. Research/CX — Audience Personas, Empathy Maps, CX Strategy, User Journey Map, Future & Current CX Maps, Generative Research, Evaluative Research, Product Positioning, UVP, Problem Statements, Discovery Research Backlog. Vision/Scope — MMP/MVP Vision Boards, Release-Level Use Cases, MMP/MVP Release Scope, Release Roadmap, Epic & Feature Definition. Requirements — Acceptance Criteria/User Stories, Task Flows, Use Case/BDD Scenarios, Backlog, Architecture Decision Records, Software Architecture, Secure Coding Specs, Data Engineering. Design/Dev — Brand Assets/Identity, Editorial Style Guide, Prototypes, Site Map, Interaction Design, Design Annotations, Low/High Fidelity Prototypes, Copywriting, Design System, Technical Architecture, Coding, Web Hosting, CI/CD. Acceptance/QA — QA Test Scenarios, AI Agent Evals, Evaluative UX Research.

## Agile Philosophies

[video/file not saved: wk1-agile-philosophies.png]

**How to release in iterations (MVP → MMP):** (1) Define long-term vision (MMP); (2) Define first release (MVP); (3) Deliver MVP; (4) Gather feedback and adjust; (5) Repeat — create new MVPs and repeat 2–4; (6) Eventually you hit MMP.

**Yes, researchers and designers should be Agile too.** Reference: the Manifesto for Agile Software Development ([agilemanifesto.org](http://agilemanifesto.org)). Agile always was, is, and always will be **iterative value delivery** — "ship and learn, learn more as you ship." Agile UX Research validates assumptions early and often, 5 days at a time — no more 5-month research efforts (credit: Google Ventures).

*Note: a popular "AI development" meme on the board is called out as describing Vibe Coding only, NOT Enterprise Development.*

## Building Products and Services with Agile

[video/file not saved: wk1-building-with-agile.png]

**Milestones of work toward release launches.** A milestone is a group of completed deliverables representing a significant point of progress; they may be completed multiple times or adjusted as teams move toward release cycles.

**Releasing incremental value with MVPs.** Agile teams deliver increasingly incremental value with each release, building many MVPs on the road to MMP — a judgment call for the product owner/manager functions. (Business Value rises over Time: MVP #1 → #2 → #3 → MMP.)

## Agile vs. Waterfall (Research Ops)

[video/file not saved: wk1-agile-vs-waterfall.png]

Two ways to build through process. **Waterfall** = sequential phases, each complete before the next. **Agile** = flexible, parallel, no phases — continuously delivering to users for feedback.

**Agile Operations:** teams collaborate across functions and break silos; work with customers to find scope/vision as they go; self-organize their process; work across functions in parallel; change the plan when needed; deliver early and often for feedback. *Agile Manifesto:* value individuals and interactions over processes/tools; working software over documentation; customer collaboration over contract negotiation; responding to change over following a plan. *Lifecycle:* client requests work → define high-level goals (days) → gather the most important requirements to deliver now (weeks) → do work and iterate across Product/Research/Design/Dev "hats" → cross-functionally deliver an iteration → gather feedback with users/clients (days) → change the plan? No → continue; Yes → change and continue. Cross-functional teammates float across the lifecycle even if it's not their title.

**Waterfall Operations:** each team siloed, handing off; scope agreed up front and never changed; no feedback until finished; no research in design phase / no design in requirements phase; no process to adjust prior work until the end; no validation with clients/users until the end. *"Waterfall Manifesto" (parody):* values processes/tools over individuals; documentation over working software; contract negotiation over collaboration; following a plan over responding to change. *Lifecycle:* client requests work → create a contract (weeks) → BA gathers requirements (months) → Research (months) → Design (months) → Development (months) → Launch (months) → hand off to client → change needed? No → continue; Yes → start over with "Change Management." Waterfall devs work in a silo, delivering only what was agreed.

## Agile Release Cycles

[video/file not saved: wk1-release-cycles.png]

**What makes up a product release?** A release is many deliverables marked by progress indicators called **milestones** that happen at the same time. Each release runs the same bars: **Intake → Discovery → Vision → Scope → Requirements → Experience Design → Development → Acceptance Testing → MVP Release.** Teams repeat this MVP after MVP; the final cycle produces the **MMP Release.**

## Understanding Network Architecture

[video/file not saved: wk1-network-architecture.png]

When you build a product hosted on the internet, the most common architecture is **Two Tier or Three Tier** — either it has a database or it doesn't.

- **Two Tier:** Client + Web Server.
- **Three Tier:** Client + Web Server + Database Server.

*Discussion: what are common examples of Two Tier and Three Tier products you've used or built?*

## How the Web Works

[video/file not saved: wk1-how-the-web-works.png]

You must understand this to become an AI developer — you'll build multiple components of this flow. The 8 steps (example: buying socks on [amazon.com](http://amazon.com)):

1. **Your Computer:** open a browser and type a URL ([www.amazon.com](http://www.amazon.com)).
2. **HTTP / API Request:** your browser creates a request to receive the files from Amazon.
3. **"The Internet":** the request hops across web servers, warehouse to warehouse.
4. **Amazon Web Server Request:** routed to the server hosting Amazon's files — website code files, image files, script files.
5. **Amazon Database Server Request:** the web server connects to the database server (which holds data + scripts) via SQL, running a SQL QUERY REQUEST to retrieve your account info.
6. **Amazon Database Server Response:** the database returns the results (the "payload") to the web server as a SQL QUERY RESPONSE.
7. **Amazon Web Server Response:** with the payload plus its own files, the web server replies in HTTP (an HTTP RETURN) back over the cloud.
8. **Your Computer: HTTP / API Response:** the browser loads all the files and you see the page.

## How Claude, ChatGPT, and Other AI Tools Work

[video/file not saved: wk1-how-ai-works.png]

When you use an AI agent tool like Claude on your computer, you work from your own computer's files; the app creates a new AI agent each session.

1. **Your Computer:** start the Claude Desktop app (no server — just the client).
2. **Start a session:** hit "+" to start a new AI agent.
3. **Claude AI Agents:** each "+" creates a new agent that operates temporarily, then stops when its job is done.
4. **Claude Skills:** Claude uses files to store memory — you can create them. The most common is a SKILLS file holding instructions Claude reads; you can tell Claude to read skills on every new agent so all agents read them.
5. **Files on your computer:** Claude creates files in the folder you tell it to work in; it doesn't save to the cloud by default.
6. **The Internet:** Claude can look things up online if you tell it to.
