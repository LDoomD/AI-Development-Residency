# Week 4 - Web Coding Lecture Notes
- Source copy: https://app.notion.com/p/7eb9219a469182888be281b0505f49c8
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:09:25.313Z
- Not saved: 25 board picture blocks (images) not saved, marked [image not saved]; the page's Transcript section only says "Add the transcript link here after class." (no transcript text exists on the page); linked page f4b1a3bddce583c1a1ed0161a0078312 (Homework mention at the end) is not accessible through the connector

---

> Extracted from the FigJam board "Fall 2026 AI Development Residency, Class Lecture and Working Sessions." This is a word-for-word transcription of every section in the Week 4 (Technical Architecture) row of the board, in board order. Each heading is the label shown on the board. Each section has a picture of the board, followed by its exact text.

# AI Dev Residency Notebook

Use AI to crunch through the lecture content, transcript, and notes.

[notebook.google.com](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab?authuser=1)

# Transcript

Add the transcript link here after class.

# FigJam Link

[https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=2192-3744](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=2192-3744)

# Lecture Content

## Week 3: Hosting Three-Tier Architecture Websites

[image not saved]

USER EXPERIENCE

Customer Experience Design

Accessibility

AI User Expereince

UX Writing

Universal Design

Human-computer interaction

Information Architecture

Interface Design

Generative Research

Conversation Design

Systems Design

Interaction Design

Voice Interface Design

UX Strategy

UX Operations

Evaluative Research

**WE ARE COVERING THE GREEN CIRCLES THIS WEEK**

PRODUCT MANAGEMENT

Data Engineering

Project Management

Information Security

Customer Segmentation

Go-To-Market

Data Analysis

Business Models

Network Security

Requirements

Backlog Management

Product Operations

Price Modeling

Technical Architecture

Product Strategy

Development Operations

Development

Quality Engineering

User Experience

Network Technology

Table Reference from

Skills and Practices Framework

| Area | What is it? | Examples of Deliverables |
| --- | --- | --- |
| Development Operations | Setting up the tools and processes that let software be built, tested, and released smoothly and often, with fewer mistakes. | CI/CD pipelines; deployment plans; automated tests; environment configurations |
| Network Technology | Building the three tier architecture for a digital product: the web servers, the database servers, and the foundation for a website to communicate with the servers inside the three-tier architecture | Web server; database server |
| Technical Architecture | The overall technical blueprint of a system: how the pieces are organized and connected so everything works together and can grow. | System architecture diagram; technical architecture document; entity relationship diagrams; technology decisions; database architecture; use case diagrams |
| Development | Building the actual software that makes a product work, writing and shipping the code behind the features. | Code; APIs; documentation |

## Cake Metaphor for Week 3

[image not saved]

### If Enterprise Software Architecture were a restaurant...

**RAW INGREDIENTS ARE...**

**The programming languages**

- SQL
- Javascript
- HTML
- CSS
- PHP
- Python
- Design components
- Flow charts
- Requirements

**What purpose do the ingredients serve?**

1. The programming languages execute the logic of what you are building
2. Each programming language serves a different purpose:
3. Querying and extracting data (SQL)
4. Presenting things in the browser (HTML / CSS)
5. Performing logic functions based on clicks or hover behavior (Javscript)
6. Performing actions on the web server (PHP, Python, JavaScript, TypeScript)

**THE MIXED INGREDIENTS ARE...**

**The Software Patterns**

**What purpose does it serve?**

1. The code scripts are actual files that get stored, and reused. When code runs, the file actually loads in order for it to run.
2. Software needs to be architected just like a UI design so that it can be speedy, secure, and efficiently run over time. This is done through patterns.

**THE TYPE OF MEAL BEING PREPARED IS...**

**The Data Architecture**

**What purpose does it serve?**

1. The data architecture is designed to fit the needs of the business and the logic of the application.
2. The data architecture decides where each piece of information is stored, so every fact lives in one place and the app always shows the same answer.
3. The data architecture is used to secure the data, so only the right people can see or change it, and nothing is lost if something breaks.

**THE HEAD CHEF IS....**

**The technical architect**

**What purpose does it serve?**

1. The Technical Architect designs the architecture of the entire structure. They decide:
2. What servers and dev tools to use
3. What programming languages make the most sense based on the desired speed, performance, and security of the system itself
4. How to design the code for speed
5. How to design the code for security
6. How to get multiple developers to work on the same code at the same time without blowing up the end product
7. The standard operations for QA testing, coding, and security

**THE RESTAURANT OWNER IS....**

**The product MANAGER**

**What purpose does it serve?**

1. The Product Manager orchestrates the direction of the entire product itself
2. The Product Manager sets the long-term vision of what features are actually going to the market for millions of people

**THE LINE CHEFS ARE...**

**The developer**

**The UX designer**

**What purpose does it serve?**

1. The developer and UX designer are the producers of the work
2. They work with the business analyst to operate based on the specific requirements
3. They follow the priorities set by the product owner and product manager

**THE RESTAURANT MANAGER  IS....**

**The product OWNER**

**What purpose does it serve?**

1. The Product Owner runs the team that delivers the work
2. The Product Owner prioritizes features, delivers the Product Manager’s roadmap, and sets the Product Operations with the team

**THE WAIT STAFF IS....**

**The Business Analyst**

**What purpose does it serve?**

1. The Business Analyst gathers all of the information from the people who make the request
2. The Business Analyst studies how customers work in their world, what they desire, how they face problems, and what their goals are. They relay this to the product owner and product manager to make important product decisions
3. The Business Analyst communicates the needs of the business and the needs of the customer to the product team, and balances both
4. The Business Analyst writes “requirements” that specify the need, the goals, the problem, and the scope of work to do

**THE OVENS ARE...**

**The database server**

**The web server**

**What purpose does it serve?**

Web Server

1. The web server stores the code script files
2. PHP
3. Python
4. SQL
5. HTML
6. CSS
7. Images
8. Javascript
9. TypeScript
10. The web server takes requests from other sources to send over the files and perform operations of the website itself

Database Server

1. The database server stores the database
2. The database server takes requests from the web server to send over the results of Queries for data

**THE DELIVERY VAN IS....**

**The HTTP request and response between a person’s computer and the web server**

**What purpose does it serve?**

1. The HTTP request carries the customer’s ask from their computer to the web server.
2. The HTTP response carries the files and the data back to the customer’s computer. The data comes from the database server, but it always goes through the web server first.

**Cakes R Us**

**THE CAKE IS...**

**The resulting user experience; everything put together! Code, design, structure, everything**

**What purpose does it serve?**

1. The “Presentation” layer is what the customer sees at the end: the website, functioning buttons, running scripts and seeing images that come from the “behind the scenes” crews

## Who is the Head Chef?

[image not saved]

### You and Claude are the Head Chefs; Claude Makes the Cake

As a human AI Developer, you are taking on the role of technical architect, and Claude helps you by consulting to help assist in decisions. Claude is the developer itself. So, you both wear the Tech Architect hat, but only one of you wears the Dev hat

Product Owner

Product Operations

Info Security Analyst

Business Analyst

Technical Architect

QA Specialist

Product Manager

**You, in this class**

Info Security Analyst

Business Analyst

Technical architect

Technical architect

Developer

- Other humans
- Claude
- ChatGPT
- Codex
- Visual Studio
- Lovable
- Gemini
- Qwen
- WHATEVER OTHER AI

UX Designer

- You
- AI bot
- Other humans

UX Researcher

- You
- Other humans

**Pro tip!**

Want to know more about these “hats”? They are called “Duties”. You can learn all about them in the Skills and Practices framework that Tech Fleet made to explain it in lay terms.

- The skills and practices website
- The skills and practices Github repo

EVEN BETTER: If you go to the Tech Fleet Platform, and go talk to Fleety, Fleety has all of this framework data in its brain, and Claude does not. So go talk to Fleety and Fleety will teach you everything about any kind of “Hat” you want to know about!

- [https://techfleet.network/tal-9000](https://techfleet.network/tal-9000)

## Deliverables This Week

[image not saved]

**We are here**

**Intake Milestone**

Project Goals

Define the high-level project goals.

Success Measures

Define the measures of success for the project.

Kickoff

Start work with the team and client.

**DELIVERABLES IN MILESTONE**

Team Ice Breakers (Team Kickoff Party Workshop)

Project Plan (Project Plan Workshop)

Team RACI Charts (RACI Hats Workshop)

KPI’s (Success Measures Workshop)

Client Intake (Client Intake Workshop)

Team Process Definition (Team Process Mapping Workshop)

Stakeholder Interviews

Working Agreements (Working Agreements Workshop)

Case Study Outline (Case Study Preparation Workshop)

**Discovery Milestone**

Hypotheses

Start forming hypotheses for the most important work ahead.

Research

Perform research based on hypotheses.

Analysis

Analyze results and form problem statement assumptions for future work.

**DELIVERABLES IN MILESTONE**

Audience personas (Audience Personas Workshop)

Empathy Maps (Empathy Map Workshop)

Customer Experience Strategy (CX Strategy Workshop)

User Journey Map (User Journey Map Workshop)

Future Customer Experience Map (Customer Experience Map Workshop)

Current Customer Experience Map (Customer Experience Map Workshop)

Generative Research (Research Test Plan Workshop) (Research Analysis Workshop)

Evaluative Research (Research Test Plan Workshop) (Research Analysis Workshop)

Product Positioning (Competitive Analysis Workshop)

Unique Value Proposition (Competitive Analysis Workshop)

Problem Statements (Problem Solving Workshop)

Discovery Research Backlog (Research Prioritization Workshop)

**Vision Milestone**

Release Vision

Form a near-term and long-term vision of problems within a release.

**DELIVERABLES IN MILESTONE**

MMP Vision Board (Vision/Scope/Roadmap Workshop)

MVP Vision Boards (Vision/Scope/Roadmap Workshop)

Release-Level Use Cases (Vision/Scope/Roadmap Workshop)

**Scope Milestone**

Release Scope

Form a list of outcomes to achieve per release.

**DELIVERABLES IN MILESTONE**

MMP Release Scope (Vision/Scope/Roadmap Workshop)

MVP Release Scope (Vision/Scope/Roadmap Workshop)

Release Roadmap (Vision/Scope/Roadmap Workshop)

Epic and Feature Definition (Vision/Scope/Roadmap Workshop)

**Requirements Milestone**

Epics, Features, Tasks

Organize the backlog based on the release vision and scope.

Acceptance Criteria

Create details that provide the instructions for delivery in research, design, and development.

Refinement

Review the documented requirements with teammates and clients to refine details.

Plan

Decide when features and tasks will be built toward the release.

**DELIVERABLES IN MILESTONE**

Acceptance Criteria / User Stories

Task Flows

Use Case Scenarios / BDD Scenarios

Backlog

Architecture Decision Records (Week 3)

Database Architecture (Week 3)

Software Patterns (Week 3)

Security Test Report

Data Engineering

Secure Coding Specifications

**Implement Milestone**

UX Research

UX Design

Development

Content

Do the research, design, content, and development work in parallel.

**DELIVERABLES IN MILESTONE**

Brand Assets

Brand Identity (Brand Identity Workshop)

Editorial Style Guide

Prototypes (Page Layout Workshop)

Site Map (Site Map Design Workshop)

Interaction Design (Interaction Design Workshop)

Design Annotations

Low Fidelity Prototypes

High Fidelity Prototypes

Copywriting Documents

Design System (Week 3)

Coding (Week 3)

Web Hosting (Week 3)

CI / CD

Generative Research (Research Test Plan Workshop) (Research Analysis Workshop)

Evaluative Research (Research Test Plan Workshop) (Research Analysis Workshop)

**Acceptance Testing Milestone**

User Acceptance

Review the work in progress with clients and users to evaluate the result and the direction of the release.

QA

Test the functionality to ensure it works well and doesn’t have bugs.

Feedback Collection

Collect feedback from users and from clients related to the release features and gather information about changes.

**DELIVERABLES IN MILESTONE**

QA Test Scenarios

AI Agent Evals

Evaluative UX Research

**Pro tip!**

Want to know more about these things? They are called “Milestones”. You can learn all about them in the Skills and Practices framework that Tech Fleet made to explain it in lay terms.

- The skills and practices website
- The skills and practices Github repo

EVEN BETTER: If you go to the Tech Fleet Platform, and go talk to Fleety, Fleety has all of this framework data in its brain, and Claude does not. So go talk to Fleety and Fleety will teach you everything about any kind of “Milestones” you want to know about!

- [https://techfleet.network/tal-9000](https://techfleet.network/tal-9000)

## How to Be a 0 to 1 Enterprise Shipper

[image not saved]

### How to Get from Idea To Ship

Step 1: Build your specs: functional and non-functional requirements

Step 2: Decide your technical architecture

Step 3: Document your technical architecture in ADRs

Step 4: Set up the database server

Step 5: Code

Step 6: Push your code and database changes to the servers

Step 7: SHIP IT. Publish it at a web address

## UX People CAN Be Enterprise Architects

[image not saved]

### How to Architect an App Without Being a Technical Expert

You may think you need to be very technical to be a great Technical Architect. After all, “Technical” is in the title!

Nope. UX people and social scientists can be as effective, if not more effective, at architecting applications when we tackle the problems and don’t worry about the solutions first.

Everything relates to the outcomes being achieved and the problems being solved. To architect a great app, you don’t need to know computer engineering. You need to solve the right problems and solve the problems correctly. The technology is the solution to the problems. The code is the solution to the problems. Technical architecture is problem-solving. Use your problem-solving chops.

As problem-solvers, we can apply the **Language of Change: Criteria, Commit, Collaborate, Change.**

1. What’s happening right now that needs to change?
2. What are the outcomes we need to achieve?
3. How do we know we will have succeeded?
4. What are we going to commit to first?

This is linguistics. Words are established first, and shared understanding is formed, before any solutions are developed. When you are learning how to architect applications, you need to apply the Language of Change as well. Do not jump right ot the solution. Develop the Language of Change first, and then your team (humans, Claude) will build the right solution to the right problems.

### The Language of Change from ProblemOps Applied to Technical Architecture

Step 1: What’s happening right now that needs to change? Describe the problems as scenarios

Step 2: What are the expected outcomes? Agree on goals and needs

Step 3: How do we know we’ll have succeeded? Set success measurements

**What should we commit to now and later?**

Step 4: Choose the appropriate software patterns. Write an ADR for each choice

Step 5: Architect the domain layer. Write an ADR for this choice

Step 6: Architect the data source layer. Write an ADR for this choice

Step 7: Architect the presentation layer. Write an ADR for this choice

Step 8: Architect the network. Write an ADR for this choice

Step 9: Plan for real use and write down why. Save all ADRs in docs/adr

### Architect Apps with the Language of Change

**1. What’s happening right now that needs to change?**

- Describe what people go through today, as scenarios.
- Describe the problem, not a solution or a feature.
- List every group of people and every situation they face.

**What you produce: **problem statements

**2. What are the outcomes we need to achieve?**

- Agree on what people want to achieve. These are their goals.
- Agree on what must be in place for them. These are their needs.
- Write down the needs about speed, privacy, many users, and change. These drive the architecture.

**What you produce: **user goals, business goals, user needs, business needs

**3. How do we know we will have succeeded?**

- Turn each important need into something you can check.
- Agree on what measurements count as success before anything is built.

**What you produce: **success measurements

**Steps 4 to 9: What should we commit to first, and later?**

Turn your answers to steps 1 to 3 into decisions. First learn how to choose a pattern. Then architect one layer at a time and connect the layers. Write an ADR for each decision.

**4. Choose the appropriate software patterns**

- Use these steps every time you pick a pattern, starting with the layers in steps 5 to 7.
- Name each problem that comes up again and again before you pick a fix.
- Write down what the fix must handle: what will change often, what must stay safe, and what must be fast.
- Pick the pattern that fits the problem, or choose no pattern on purpose.
- Pick the simplest choice that meets the needs. A pattern that does not fit makes the code harder to change.
- Write down what the pattern prevents, what it costs, and how you will check that it works.

Some common problems inside the code, and the patterns that fit them:

**One job, many ways to do it** → Strategy

**Talking to an outside service** → Adapter

**Something that moves through stages** → State Machine

**What you produce: **a list of the patterns you chose, the problem each one solves, and an ADR for each choice.

**5. Architect the domain layer**

- Add a thin Service Layer on top only if a need calls for it.
- Judge how complex the business rules are, then pick one

**Simple rules** → Transaction Scripts

**In-between rules on table-based tools** → Table Modules

**Complex or growing rules** → Domain Model

**What you produce: **how the business rules are organized, and an ADR for this choice.

**6. Architect the data source layer**

Match it to your step 5 choice:

**Transaction Scripts** → Gateways

**Table Modules** → Table Data Gateway

**Simple Domain Model** → Active Record

**Complex Domain Model** → Data Mapper

**What you produce: **how the app reaches the database, and an ADR for this choice.

**7. Architect the presentation layer**

- Keep business rules out of the screens.
- Build for speed and performance
- Never let the screen talk to the database directly.

**What you produce: **Technical requirements for the logic of the presentation layer, and an ADR for this choice.

**8. Architect the network**

- Decide where each layer runs. In our app, the screens show in the browser, the server code runs on Vercel, and the database runs on Supabase.
- Draw how a request moves from the browser to the server, to the database, and back.
- Send every request over HTTPS.
- Keep secret keys on the server. Never send them to the browser.
- Put the server and the database in the same region, close to your users.
- Decide how long to wait for an answer, and what to do when a call fails.

**What you produce: **a diagram of where each layer runs and how the layers talk to each other, and an ADR for this choice.

**9. Plan for real use and write down why**

- Decide what happens when two people edit the same thing.
- Keep the app in one place unless a need forces a split.
- Treat each decision as an assumption, and test the riskiest first.
- Write down what you chose and why, one decision per ADR.
- Save each decision as its own ADR in the docs/adr folder of your repository.
- When a decision changes, write a new ADR that replaces the old one. Never erase the old one.

**What you produce: **Architectural decision records

## Dev Glossary

[image not saved]

### Let’s talk “Developer”

**“Front-End”**

The code that lives on the “client”, which is a computer browser or mobile phone. For instance: HTML, CSS, Javascript, React, etc.

**“Back-End”**

The code that lives on web servers and database servers. These are coding languages that handle scripts that perform server actions. PHP, Python, Java, Ruby, Perl, Bash, etc.

**“Middle Layer”**

The code that sends HTTP Requests over the internet from computer to computer. This happens through a variety of front-end scripting languages or back-end programming languages. These calls are either started on a computer / phone or on the servers.

**“Full Stack”**

A term that means “all of it”! When a coder says they are “full stack”, they code the front-end, the middle layer, and the back-end. So.... Claude is a full-stack developer!

## DOGFOODING CLAUDE

[image not saved]

### Here’s how to get Claude to make any deliverable with quality, over and over and over

**What is dogfooding in software corporate speak?**

- The name comes from the saying “eat your own dog food.”
- It means a team uses the product they made every day, just like their customers do.
- For example, the people who make an email app use that app for their own email.
- This helps them find problems before their customers do.

**What is dogfooding in our class with Claude Code?**

- You give Claude something it made before, so it can make the next thing.
- First, Claude helps you make a research report. You check it and save it.
- Next, you give that report to Claude to make the vision.
- Then you give the vision to Claude to make the scope, and so on.
- Each new document is made from the ones before it.

**How does it work with Claude Code?**

- Claude does not remember your other chats. Each new chat starts empty.
- Claude only remembers what is in the chat you are using right now. This is called context.
- So you save your work in documents. Then you give those documents to each new chat.
- The first time, you only have an idea. You ask Claude to help you make your first document.
- The steps below show the whole process from start to finish.

**Why does it work?**

- Each new document is made from one you already checked. You never have to start over.
- Claude uses your documents instead of guessing or searching the internet. This also uses fewer tokens.
- Saved documents keep Claude from slowly changing what you already decided. This slow change is called drift.
- You stay in charge. If you ask Claude to make everything in one step, you will not understand your own product.
- When you go one part at a time, you make every choice and you know why you made it.

### Steps to Produce Literally Anything with Claude Code and Dogfooding

**Get ready**

**1. Write your idea in your own words.**

- You do not need anything else to start.
- Write what you want to make or what problem you want to solve. A few sentences is enough.

**2. Ask Claude where to start.**

- Say: “Here is my idea. I don’t know where to start. What should we make first?”
- Most of the time, the first thing to make is research about the problem and the people who have it.

**3. Make your first document and save it.**

- Make it with Claude. Then read it yourself and fix anything that is wrong.
- Save it as a markdown file. Do not leave important work only in a chat.

**Work together**

**4. Open a new chat and give it your saved documents.**

- Give it every document you have saved so far.
- If you have a template or instructions for the next thing, give it those too.

**5. Ask Claude to read everything first.**

- Say: “Read these files. Tell me when you have what you need. I don’t know how to do this, so let’s do it together.”

**6. Work on one part at a time.**

- Go through the template one box at a time.
- You make each choice, so you understand what you are building.

**7. Ask Claude where each answer came from.**

- Ask: “How did you decide that? What did you use?”
- The answer should come from your documents, not from the internet.

**8. Find mistakes and fix them.**

- Do not trust Claude without checking. Tell it what is wrong and what is right.
- Ask it to use plain words that you understand.

**9. When you are stuck, ask Claude to teach you.**

- Ask: “What do I need to know to decide this? Explain it like I’m 5.”
- Claude gives you the facts. You make the choice.

**Save and repeat**

**10. Approve the work and save it as a new document.**

- Ask Claude for the finished work as a markdown file.
- Save every version so you can look back at it later.

**11. Give the new document to Claude and start again.**

- The new document is now one of your saved documents.
- Go back to step 4 and use it to make the next thing.

## Technical Architecture

[image not saved]

### What does a Technical Architect do?

**THE HEAD CHEF IS....**

**The technical architect**

**What purpose does it serve?**

1. The Technical Architect designs the architecture of the entire structure. They decide:
2. What servers and dev tools to use
3. What programming languages make the most sense based on the desired speed, performance, and security of the system itself
4. How to design the code for speed
5. How to design the code for security
6. How to get multiple developers to work on the same code at the same time without blowing up the end product
7. The standard operations for QA testing, coding, and security

**THE HEAD CHEF DOES....**

The Technical Architect is the head chef. They do not cook dishes. They themselves are not developing. Their job is to decide how the whole kitchen works so that every dish comes out right, every time, for everyone in the restaurant.

A technical architect is the person who plans and designs how an app is built before the building starts, and keeps it on track while it is being built. They make the big choices about the shape of the thing. The line chefs (the developers, the UX designer, and the AI) do the cooking. The Tech Architect tastes every plate before it goes out.

You do not need to code to do this job. You need to understand the ingredients well enough to make good calls and to check the work. A great head chef can taste a sauce and know what is wrong with it, even if a line chef stirred the pot.

## What does “Enterprise ready” mean to the Technical Architect?

[image not saved]

### What does “Enterprise ready” mean?

You can make a sloppy plate for yourself and nobody cares. But the moment a dish goes out to 300 people at once, every weakness shows. “Enterprise ready” is that jump. It means the app is built to serve a whole room of real people, for a long time, not just to work once on your own screen. As the head chef, your job is not to prove the app can run. It is to make sure it keeps running right when it is busy, when something breaks, and when the recipe needs to change next month.

In plain terms, enterprise ready means the app keeps four promises:

1. It does not fall apart when one small thing goes wrong (reliability), so a single bad ingredient never ruins the whole plate.
2. It serves everyone well, even at the busiest moment and even the last table (scalability), so you measure your slowest rush, not your easy average.
3. It stays easy and safe to change later (maintainability), so a new cook can walk into the kitchen, understand how it works, and fix or add something without blowing up the rest.
4. It keeps people’s data private and only in the right hands (security).

None of this is extra polish you add at the end. It is the plan you make from the first day, and the standard you taste against before anything leaves the kitchen.

**Where does it live?**

An app lives in three places at once: on the customer's screen, on a server that does the work, and in a database that stores anything that must still be there tomorrow. The technical architect decides which work happens in each place, and chooses where those servers run. Almost always they are rented from a hosting company (the cloud), not owned.

**What is the app built on?**

The app is built from raw parts and ready-made ones. The raw parts are the programming languages and the design pieces. The ready-made parts are libraries and APIs: prebuilt chunks of code, and services from other companies that you plug in instead of building from scratch. The technical architect picks the languages, the database type, and the ready-made parts that best fit the kind of app being built.

**How do the pieces fit together?**

The technical architect decides how the parts talk to each other: the screen the customer sees, the server that does the work, and the database that stores the data. A request travels from the screen to the server, the server asks the database for what it needs, and the answer travels back. Each part has one clear job and connects through known openings, instead of reaching into another part.

**Why did we build it this way?**

Every real choice costs something and rules something else out. The technical architect writes down why each important choice was made: what the options were, which one they picked, and the trade-offs. These notes are kept on record so future teammates understand the reasons, and nobody re-argues or quietly undoes a decision. The rule: never erase an old note. If the choice changes, write a new one.

**How might we build it reliably, securely, and scalably?**

The technical architect makes software and hardware choices that keep three of the four promises. Reliable: one small failure never takes down the whole app. Scalable: it still runs well at the busiest moment, not just on a quiet day. Secure: people's data stays private, and only the right person can reach it. These are planned from the start, not patched on at the end.

**How can we efficiently maintain this when there are 1,000,000 users?**

Maintain means keeping the app easy and safe to change later, since most of an app's life is spent changing it. On the software side: every fact has one home, each part has one job, there is one way to do each thing, and dead code gets deleted. On the team side: the shared code home (GitHub) is set up to enforce standards and let every developer work together cleanly. If one developer can build smoothly but another cannot, the team has a problem.

## Deliverables

[image not saved]

### Technical Architecture Deliverables

The technical architect’s job is to ensure that over time, with more and more users using the software at once, the application remains stable. This is a very real threat to software. If a developer, or many developers, just jump in to code and deliver chunks of code on top of each other, things start getting really messy. Messy code structure leads to more bugs. Not only more problems, but problems that will be impossible to track or resolve quickly over time. The more that time passes with messy coding practices, the more the system becomes slow, buggy, insecure, and really hard to use.

At the very beginning, the technical architect invests time and energy in their teams properly building a rigorous foundation that is the right job for the application being built. Once the foundation is built, the rest of the system can handle a lot of traffic, is speedy, is usable, and is secure. But this does not happen with the snap of someone’s fingers. The deliverables for technical architecture require energy and attention.

**CHOOSING PROGRAMMING LANGUAGES**

- SQL
- NoSQL
- Javascript
- HTML
- CSS
- PHP
- Python
- Ruby
- Perl
- Java

**What purpose do the ingredients serve?**

1. The programming languages execute the logic of what you are building
2. Each programming language serves a different purpose:
3. Querying and extracting data (SQL)
4. Presenting things in the browser (HTML / CSS)
5. Performing logic functions based on clicks or hover behavior (Javscript)
6. Performing actions on the web server (PHP, Python, JavaScript, TypeScript)

**Decision for Choosing “Ingredients” - Programming Languages**

- The type of programming language you use for front-end, middle layer, and back-end will depend on the type of performance, security, and reliability, and function you want
- Pick the programming languages that fit the purpose of what you are doing
- Are the programming languages you’ve chosen maintainable over time? Are they easy for new developers to start coing on, or have you picked an impossible coding language to code with? How accessible is the programming language for developers? Some languages have higher accessibility for developers than others
- If you need a database, you are going to need to vet specific backend scripting languages (the files that call to the database) to ensure that they uphold the proper architecture and reliability / performance / security over time.

**THE DATABASE SERVER AND WEB SERVER**

**What purpose does it serve?**

Web Server

1. The web server stores the code script files
2. PHP
3. Python
4. SQL
5. HTML
6. CSS
7. Images
8. Javascript
9. TypeScript
10. The web server takes requests from other sources to send over the files and perform operations of the website itself

Database Server

1. The database server stores the database
2. The database server takes requests from the web server to send over the results of Queries for data

**Decision for Choosing Databases**

- The purpose of the data will drive the type of database you use.
- There are “Relational” databases and “non-relational” databases. Each of them have a completely different architecture from each other.
- If you have neatly structured data that connects together and must stay accurate, like people, their budgets, and each budget's transactions, you want a relational database
- If you expect your data to be loosely shaped or to change often, or you need to store large piles of flexible records fast and the strict links between them do not matter, you want a non-relational database
- You need to host the database on a server. Either you build the server yourself, or you host it on another tool. In this class we’re going to use Supabase which is a relational database server that’s hosted for you with tools that you can use to easily build and maintain the database server without it being too manual. But there are reasons to build a database from scratch! More security, more control over the data, 100% self ownership of the data (it’s not stored on someone else’s data center computer), performance standards (maybe you need to build a beefy supped up database for performance of the app).

**THE SOFTWARE PATTERNS**

**What purpose does it serve?**

1. The code scripts are actual files that get stored, and reused. When code runs, the file actually loads in order for it to run.
2. Software needs to be architected just like a UI design so that it can be speedy, secure, and efficiently run over time. This is called software patterns.

**Decisions for Software Architecture**

- Choosing the type of programming language is one thing, but technical architects must also design the way that the apps are coded. This is called “Software Patterns”
- Software Patterns are repeatable ways to architect code. Just like a design pattern is a repeatable pattern for the UX.
- There are software patterns that will lead to way more efficient and speedy performance of the app itself because of the sequence of the coding execution. This gets really complicated when there are a lot of pieces to connect: the front end, middle layer, and backend.

**THE HTTP CALLS AND CONNECTIONS TO OTHER PIECES**

**Cakes R Us**

**What purpose does it serve?**

1. The HTTP request carries the customer’s ask from their computer to the web server.
2. The HTTP response carries the files and the data back to the customer’s computer. The data comes from the database server, but it always goes through the web server first.

**The big lessons about enterprise architecture from Martin Fowler's Patterns of Enterprise Application Architecture.**

**Write down the why.**

Record the important decisions and the forces behind them. A pattern is a starting point to adapt to your situation, not a recipe to copy. This is done through Architectural Decision Records that are stored, maintained, and checked against when new lines of code ship to production.

**What makes enterprise software hard is the data, not the size.**

Enterprise apps hold a lot of long-lived business data, are touched by many people at once, and must fit together with other systems. That mix, not clever algorithms or raw size, is what makes them hard.

**Split the system into layers.**

Separate what the user sees (presentation), the business rules that decide things (domain), and how data is stored and fetched (data source). The most important rule: the domain and data layers must never depend on the presentation layer.

**Protect the business rules above all.**

The domain logic is the crown jewel. Keep it free of the screen, the web, and the database so it can be tested and reused. Code you can only run by faking a web request is code you cannot trust.

**Architecture is the decisions that are hard to change.**

Fowler treats architecture as the shared understanding of the important, hard-to-reverse decisions. Spend your care there, and make everything else easy to change later.

**There is no free lunch. Every choice is a trade-off.**

No arrangement wins on every measure. Scalability costs operational complexity; testability costs indirection. Name the forces in your situation, then pick the option whose strengths match them.

**Start simple. Earn complexity.**

Use the simplest thing that works (one program, a simple script, an optimistic lock) until a concrete force pushes you to the richer option. Complexity should be earned, not paid for up front.

**Bridging objects and tables is most of the work.**

In-memory objects and database tables are shaped differently. Moving data cleanly between them is a huge part of enterprise apps, and it is exactly what an ORM tool does for you.

**Do not distribute your objects.**

Fowler's First Law of Distributed Object Design. Every call across a network is slow and can fail. Keep the app in one process when you can; when you must cross a network, do it with few, large calls, not many small ones.

**Measure performance, do not guess.**

Learn the words (response time, throughput, latency, load, scaling up versus out) and watch your slowest, busiest moment, not the average. Never optimize without measuring first.

**Guard shared data from day one.**

Whenever many people touch the same data, you risk one edit erasing another and half-finished reads. Choose how you handle it (optimistic or pessimistic locking) on purpose, not by accident.

## Platforms for Apps

[image not saved]

### Platforms for App Development

**What is an app?**

- An app is a program that people use to get something done.
- Apps can run in a web browser, on a computer, on a phone, or inside a device like a smart thermostat.
- Where the app runs changes how you build it, how people get it, and how you update it.
- There are four main types of apps. They are web apps, desktop apps, native mobile apps, and Internet of Things apps.

**Web apps** (picture: a browser window at [www.myapp.com](http://www.myapp.com))

- A web app runs inside a web browser, like Chrome or Safari.
- People open it with a link. They do not install anything.
- Examples are Gmail, Google Docs, and YouTube.

**Desktop apps** (picture: a computer screen showing "My App")

- A desktop app is installed on a Windows or Mac computer.
- People download it once, then open it from their computer.
- Examples are Microsoft Word, Photoshop, and the Claude desktop app.

**Native mobile apps** (picture: a phone)

- A native mobile app is installed on an iPhone or Android phone.
- People download it from the Apple App Store or Google Play.
- Examples are Instagram, Uber, and most bank apps.

**Internet of Things apps** (picture: a smart thermostat showing 72°)

- An Internet of Things app runs on a device that is not a computer or a phone, and that connects to the internet.
- It usually comes with a phone app or web app that controls it.
- Examples are smart thermostats, smart doorbells, fitness watches, and smart speakers.

**How the five types are different**

| Question | Web app | Progressive Web App | Desktop apps | Native mobile apps | Internet of Things apps |
| --- | --- | --- | --- | --- | --- |
| What’s the difference between the others? | It’s an app that runs in an internet browser and opens from a link. It requires the internet to be connected to the computer. Nothing is installed on a device. | It is a web app that acts like a native mobile app. People can add it to their home screen, and it can work offline. It still runs in the browser. | It is installed on a computer. It can use the computer's files and work offline. It does not run on phones. It does not require the internet to function, unless it’s making calls to servers on the internet. | It is an application that is specifically built for iPhone or Android and installed from an app store. It can use the phone parts, like Face ID or Geolocation sensors or cameras on the phone. | It runs on a physical device, not a screen you browse. It senses or controls something in the real world. |
| What kind of programming languages does it require to build? | “Web” programming languages:
HTML
CSS
Javascript
Next.js
React
PHP | “Web” programming languages:
HTML
CSS
Javascript
Next.js
React
PHP | “Native Desktop” programming languages:
Windows: C#, C++, Java, .NET
Apple: Swift, Objective-C, Java
Linux: Perl, C++, Python
All three: JavaScript with a tool called Electron | “Native Mobile” programming languages:
Android: Java, Kotlin
Apple: Swift, Objective-C
Both: JavaScript with React Native, or Dart with Flutter | C++, C, and MicroPython (a small version of Python)
Plus web or mobile languages for the app that controls the device |
| Where does it run? | It runs in a web browser, either on a desktop, a laptop, or a mobile phone. | It runs in a web browser. Once it is added to a phone or computer, it opens in its own window like a regular app. | It runs on a Windows or Mac computer. | It runs on an iPhone or Android phone as a stored application that you download | It runs on a small computer inside a device. |
| How do people get it? | They open a link on an internet browser | They open a link. Then they tap "Add to Home Screen" or "Install." No app store is needed. | They download it from an internet source and install it. | They download it from an app store. | It comes on the device. People often set it up with a phone app. It could be installed on an IoT device through a USB drive too. |
| How do you send an update? | You publish new code. Everyone gets it the next time they open the page. | You publish new code. The app gets the new version the next time it opens. | People download a new version, or the app updates itself. | You send a new version to the app store. People update the app. | The company sends the update to the device over the internet. |
| Does it work without internet? | Most web apps need the internet. | Yes. It can save pages and data on the device so it works without the internet. The developer has to set this up. | Most desktop apps work without the internet. | Many features work without the internet. | Basic features often work. Smart features need the internet. |
| Can it use device parts, like the camera or location? | Yes, some parts, after the person says yes. | Yes, more than a regular web app. It can use alerts, the camera, and location after the person says yes. iPhones allow fewer parts than Android phones. | Yes, it can use files and most computer parts. | Yes, it can use the camera, location, alerts, and Face ID. | Yes. It is built around sensors, like heat, motion, or heart rate. |
| What do people build it with? | HTML, CSS, and JavaScript, often with Next.js or React. | The same tools as a web app, like Next.js. It also needs two extra files: a manifest file and a service worker. | Often web code with a tool called Electron, or a language made for Windows or Mac. | Swift for iPhone, Kotlin for Android, or React Native or Flutter for both. | C or C++ on the device, plus server code and a phone or web app. |
| Who must approve it before people use it? | No one. You publish it when you are ready. | No one. You publish it when you are ready. | No store is needed. Computers may warn people about apps that are not signed. | Apple and Google review it before people can download it. | The device maker. Devices that send radio signals also need government approval. |

**All four types can use the same three tiers**

- The screens are different for each type of app. They can be a web page, a desktop window, a phone screen, or a device with buttons or a small display.
- The server code and the database can stay the same for all of them.
- For example, a smart doorbell, its phone app, and its website can all save to the same database.

Diagram: Web app (tier 1), Desktop app (tier 1), Mobile app (tier 1), and Internet of Things device (tier 1) all connect to Server code (tier 2), which connects to Database (tier 3).

**How to choose the right type**

- Choose a web app if you want people to use it right away from a link, on any device.
- Choose a desktop app if people work with large files or use it all day on a computer.
- Choose a native mobile app if people need it on the go, or need the camera, location, or alerts.
- Choose an Internet of Things app if your product is a physical device that senses or controls something in the real world.
- Many products start as a web app. They add the other types later.

**What we build in this class**

- In this class, you will build a web app with Next.js and Material UI.
- A web app is the fastest way to launch. There is no app store and no download.
- Material UI pages can change size to fit a phone screen. People can use your app on their phone in a browser.
- Later, you could add a mobile app that uses the same server code and database.

**How to ask Claude Code about app types**

- Ask Claude: "Which type of app fits my idea, and why? Give me the pros and cons of each type."
- Ask Claude: "Will my app work on a phone screen? Show me how it looks at phone size."
- Ask Claude: "If I add a mobile app later, what parts of my code can I keep?"

## Architectural Decision Records

[image not saved]

**What are ADRs?**

- ADR stands for Architecture Decision Record.
- An ADR is a short document that writes down one important choice about how your app is built.
- It also writes down why you made that choice.
- Each ADR covers only one decision.
- Important choices are the ones that are hard to change later, like which database to use, which framework to use, or where to host your app.

**Why are they used?**

- They remember your decisions for you. Claude does not remember your other chats, but it can read a saved ADR in every new chat.
- They stop drift. Without a written record, Claude may quietly change a choice you already made.
- They explain the “why.” When someone asks “why did we build it this way?”, the answer is already written down.
- They help new people catch up. A new teammate can read the ADRs and understand the app faster.
- They help you decide well. Writing down your options, and the good and bad parts of each, makes you think before you choose.

**How are they stored over time?**

- Each ADR is its own file in your repository, in a folder like docs/adr.
- Each file gets a number and a short name, like `0001-use-nextjs.md`. The numbers show the order you made the decisions.
- All of your ADRs together are called a decision log.
- You save and push them to GitHub like any other file, so you keep a full history.
- When a decision changes, write a new ADR that replaces the old one. Mark the old one as “replaced by” the new one.
- Some teams add dated notes to an old ADR instead. Either way, never erase what was decided before.

**What goes on them?**

- Title: the decision, in a few words.
- Date and status: when it was decided, and whether it is proposed, accepted, or replaced.
- Context: what was happening, and what problem pushed you to make a choice.
- Options: the choices you looked at, with the good and bad parts of each.
- Decision: what you chose, and why.
- Consequences: what happens because of this choice, both good and bad, and anything you need to do next.

**The 4 main parts of an ADR, and how to write them**

Every ADR starts with a short title that names the decision. Under the title are four main parts. They come from Michael Nygard, who wrote the first ADR template in 2011. Our class template also adds a date and a list of the options you looked at.

**1. Status**

**What it is:** where the decision stands right now.

**How to write it:** use one word: Proposed, Accepted, Deprecated, or Superseded. Add the date.

**What to include:** “Proposed” means the team has not agreed yet. “Accepted” means the team agreed. If a newer ADR replaces this one, mark it “Superseded by” and write the newer ADR’s number.

**Example:** Accepted, October 31, 2026.

**2. Context**

**What it is:** the situation that made you need to decide.

**How to write it:** write facts, not opinions. Write it so someone who was not there can understand it.

**What to include:** the problem, what the app needs, and any limits, like time, money, tools, or skills.

**Example:** We need screens and server code for a three-tier app that runs on Vercel.

**3. Decision**

**What it is:** the choice you made.

**How to write it:** use full sentences, and start with “We will.”

**What to include:** what you chose, and why you chose it over the other options.

**Example:** We will use Next.js with Material UI, because it covers two of our three tiers in one project.

**4. Consequences**

**What it is:** what happens because of the choice.

**How to write it:** list every result, not just the good ones. Be honest about what gets harder.

**What to include:** what gets easier, what gets harder, new risks, and anything the team has to do next.

**Example:** Students learn where code runs, in the browser or on the server. Material UI’s theme file needs a “use client” line at the top.

**Where should ADRs live if they are permanent?**

- Keep them in your GitHub repository, right next to your code, in a folder like docs/adr.
- The decision stays with the code it explains. Anyone who has the code also has the reasons.
- GitHub keeps every version forever, so you can see what changed, when, and who changed it.
- Claude Code reads the files in your repository, so it can check your decisions before it writes code.
- Do not keep the only copy in a chat, in Notion, in Google Docs, in FigJam, or on your own computer. Those copies can get lost or go out of date.

**A simple setup for this class**

1. Make a folder in your repository called docs/adr.
2. Save each decision as its own numbered file, like `0001-use-nextjs-with-material-ui.md`.
3. Commit and push it along with the code it affects.
4. Add this line to your project’s `CLAUDE.md` file: “Read every ADR in docs/adr before making changes, and write a new ADR for every big decision.” Claude Code reads `CLAUDE.md` at the start of every session.

**Example: **`docs/adr/0001-use-nextjs-with-material-ui.md`

Title: Use Next.js with Material UI.

Date and status: October 31, 2026. Accepted.

Context: We need screens and server code for a three-tier app that runs on Vercel.

Options: Plain React, or Next.js. Plain React needs a separate place for server code. Next.js holds the screens and the server code in one project.

Decision: Use Next.js with Material UI, because it covers two of our three tiers in one project.

Consequences: Students learn where code runs, in the browser or on the server. Material UI’s theme file needs a “use client” line at the top.

**HERE IS AN ACTUAL ADR IN THE TECHFLEET NETWORK PLATFORM**

ADR-0001: SPF becomes the single source of truth for the framework data layer

- **Status:** Accepted (2026-08-10)
- **Deciders:** Tech Fleet owner + engineering
- **Related:** ADR-0002, ADR-0003; docs/framework/[open-data-strategy.md](http://open-data-strategy.md)

**Context**

The Skills & Practices Framework (SPF) launched publicly on 2026-08-10 as a versioned open-data product — static JSON on GitHub Pages ([https://techfleetworks.github.io/skills-and-practices-framework](https://techfleetworks.github.io/skills-and-practices-framework), v1, \~29 datasets, generated from Baserow, CC BY 4.0). Per [open-data-strategy.md](http://open-data-strategy.md), **the public Git repo is now the canonical source of truth** for the framework; everything else is a derived read model.

Today the app carries its own copy of the framework in reference\_\* tables + the framework\_entity\_v view + the framework\_edges graph, populated from an earlier CSV ingestion path. These power Fleety (the AI coach's RAG + graph injection), the Journeys section, and search. This local copy predates the public SPF and does **not** contain the handoff-deliverables-map or the career-transitioning datasets, and it can silently drift from the now-canonical public data.

The owner's directive: SPF is to become the **one authoritative source** that Fleety, the Journeys section, the new Hand-Off Production System, and future features all read from — not a per-feature dependency.

**Decision**

Adopt the public SPF v1 API as the **single upstream source of truth** for framework data, consumed into the app as a **documented, versioned, derived snapshot** (spf\_\* schema, see ADR-0002) that is synced from the public API and **version-pinned per consumer read** where reproducibility matters (e.g. each hand-off production run pins the spf\_version it used).

The existing reference\_\* tables + framework\_edges graph are **replaced** by graph structures rebuilt from the SPF snapshot, exposed through a source facade (ADR-0003) so the migration is a strangler-fig cutover, not a big-bang. The local snapshot is a **derived index of an external authoritative source**, not a competing source of truth — its existence and sync mechanism are documented, per [database-architecture.md](http://database-architecture.md).

**Alternatives considered**

1. **New standalone snapshot alongside reference\_\* (no replacement).** Safest for Fleety, but leaves two framework homes that drift — explicitly rejected by the owner, who wants one source of truth for the platform.
2. **Runtime fetch + short cache only (no snapshot tables).** Simplest, but couples production Fleety/Journeys/hand-off generation to GitHub Pages uptime, gives no reproducibility (version pinning), and is not a durable layer future features can build on. Rejected.
3. **Keep reference\_\* as the source; sync SPF into it in place.** Would mutate the live graph Fleety depends on with no clean rollback boundary; the schema shapes differ (SPF has a dedicated handoff map, career-transitioning, slug-based links). Rejected in favor of a parallel snapshot + facade that keeps rollback a flag flip.

**Consequences**

- **Easier:** one authoritative, versioned framework layer; new features (hand-off, career coaching, Journeys) read one contract; framework data can no longer silently drift from the public standard; reproducible hand-off generation via spf\_version pinning.
- **Harder / accepted risk:** the cutover touches Fleety and Journeys, which are live for \~767 users — this is the highest-risk item in the programme. It is mitigated by expand/contract + a source facade + canary + a verified restorable backup, and the destructive drop of reference\_\* is a separate, owner-confirmed release (ADR-0003).
- We take on an **external dependency** on GitHub Pages availability and on SPF v1 schema stability; mitigated by the snapshot (serve last-good), a pinned v1 contract test that fails CI on drift, and graceful degradation (see the resilience decisions in the plan).
- The SPF data is **public, non-personal** (CC BY 4.0), so most privacy obligations do not attach to the snapshot itself; attribution is tracked. Personal data enters only via the hand-off feature's uploads (handled separately).

[image not saved]
Recipe card: the format of an ADR. ADR 0001: Use Next.js with Material UI. Date: October 31, 2026. Status: Accepted, with a red ACCEPTED stamp. Context: We need screens and server code for a three-tier app that runs on Vercel. Plain React needs a separate place for server code. Next.js holds the screens and the server code in one project. Decision: We will use Next.js with Material UI, because it covers two of our three tiers in one project. Consequences: Easier: students learn where code runs, in the browser or on the server. Harder: Material UI’s theme file needs a “use client” line at the top. Saved as docs/adr/[0001-use-nextjs-with-material-ui.md](http://0001-use-nextjs-with-material-ui.md)

## Layers of Software

[image not saved]

### Layers of Software Architecture

**What a layer is**

A layer is a group of code with one job. Each layer uses the layer below it, and the layer below does not even know the layer above exists. Fowler calls layering one of the most common ways to break a complicated system into parts.

**How layers shape enterprise architecture**

Fowler builds his whole book around three layers. The presentation layer is the service you offer the outside world. The domain layer is the real point of the system: the business rules. The data source layer is how you use other systems, mostly the database. Layering lets you understand one layer without the others, swap one layer out without rewriting the rest, and keep the parts from leaning on each other too much. The catch: some changes still ripple through every layer, like a new field that has to show on screen and also be saved.

**Where the service layer fits**

Fowler often splits the domain layer in two. On top sits a thin Service Layer that lists every action the app offers, such as adding a transaction or setting a monthly budget. Underneath sit the business rules themselves. The screen talks only to the Service Layer, and the Service Layer then calls the business rules. This gives the app one clear front door, and one place to check that a person is allowed to do an action and to make sure each action either fully finishes or does not happen at all. It is most useful on top of a Table Module or a Domain Model. An app built only from Transaction Scripts usually does not need one, because each script already acts as the front door for its own action. Fowler's own advice is to keep it as thin as possible and add it only when the app needs it, though he notes that many good designers use richer ones.

**The golden rule**

The domain and data source layers must never depend on the presentation layer. Because the business rules and the data do not rely on the screen, you can change how the app looks many times, or add a phone app next to the website, without breaking the business rules.

**A quick test for rules in the wrong place**

Imagine adding a totally different screen, like a phone app next to the website. Anything you would have to copy over is a business rule hiding in the wrong layer. Move it down into the domain layer so every screen shares one copy.

**Layers are not machines**

A layer is about how code is organized, not where it runs. A tier usually means a separate machine. All three layers can run on one laptop. Fowler's advice: keep everything in one place unless you truly have to split it, because every split across a network adds cost and complexity.

**Why layering caught on**

In the 1990s, many apps buried their business rules inside desktop screens. When the web arrived, those teams had to rewrite everything. Teams that kept a separate domain layer just added a new web screen on top. That one story is the whole payoff of layers.

**A cake cut open to show the four layers**

Each layer of the cake sits on top of the layer below it, just like the layers of an app. The Presentation Layer is on top, where people can see it. The Data Source Layer is on the bottom. The cake sits on a plate, and the plate is the database.

[image not saved]
A cake cut open to show the four layers: Presentation Layer, Service Layer, Domain Layer, and Data Source Layer, sitting on a plate labeled Database

**Presentation Layer**

This is the part of the app that people see and use. It shows information on the screen, like a profile page or a list of messages, and it takes in what people type, tap, or click. It passes those requests down to the domain layer and then shows the results that come back.

What lives here:

- UI
- Styles
- Brand
- Front-end code
- Pictures

**Service Layer**

This layer sits between the screen and the business rules. Every time a person does something in the app, like signing up, saving a form, or sending a message, the screen sends that request here first. Each action the app can do has its own starting point in this layer. In many apps, these starting points are called API routes. Before an action runs, this layer checks who is asking and whether they are allowed to do it. Then it runs every step of the action. If any step fails, it undoes the steps that already ran, so the app never saves half of a change. Fowler treats it as the top part of the domain layer.

What lives here:

- API routes
- Actions like “Sign up”
- “Are you allowed?” checks
- Save every step or none

**Domain Layer**

This is where the app makes its decisions. It holds the business rules, such as working out a total price and deciding when to send a reminder. It does not care what the screen looks like or how the data is stored. Its only job is to get the rules right.

What lives here:

- Web server scripts
- Database server scripts
- Business rules

**Data Source Layer**

This is the part of the app that saves information and gets it back when it is needed. It reads and writes things like accounts, messages, and orders in the database, so nothing is lost between visits. When the domain layer needs data, it asks this layer for it.

What lives here:

- Database architecture

**Database** (where the data actually lives)

What lives here:

- Tables
- Data records
- Keys that link records
- Access rules
- DON’T put the app’s rules in the screens people see
- DON’T let the rules or the data depend on the screens
- DON’T spread the app across more servers than you need
- DON’T write the same rule in two different places
- DON’T let the screen talk to the database directly

## Software Patterns

[image not saved]

### Enterprise Software Architecture Patterns

“A pattern describes a problem that repeatedly appears in software and a solution that has worked in practice.” **Martin Fowler, Patterns of Enterprise Application Architecture**

Patterns are repeatable ways to shape an app's code and parts. Cards 1 to 7 are the core shapes to learn first: how the app is split and shipped, how work flows, and how the code inside is organized. Cards 8 and on are more advanced styles you will meet later. A real app usually mixes several of these.

Source: TechFleet Enterprise Software AI Skills repo, enterprise-architecture-standards / references / [software-architecture-styles.md](http://software-architecture-styles.md) ([https://github.com/techfleetworks/enterprise-software-AI-skills](https://github.com/techfleetworks/enterprise-software-AI-skills)). Patterns, trade-offs, and “use when” guidance drawn from that file.

### Monolith

**One deployable unit**

Diagram: User interface, Business logic, Data access, Database

**What problem does it solve?**

You need to get an app built and launched fast, without juggling lots of separate pieces.

**When to use**

Use this pattern when you are starting a brand new app with a small team. Everything lives in one place, so it is the easiest to build, test, and launch.

**What are the risks**

As it grows, it can turn into one big messy pile that is hard to change. The whole app is a single piece, so one bad change can break all of it at once.

**A real example**

A small local bakery's website where you browse items and place an order. One person builds the whole thing as a single app and ships it in a weekend.

### Modular Monolith

**One deployable unit, clean inner walls**

Diagram: Module A, Module B, Module C, Shared database

**What problem does it solve?**

One app gets messy as it grows, and a change in one area keeps breaking another area.

**When to use**

Use this pattern when you want one app that stays tidy on the inside, but you are not ready to split into many separate apps. A good fit for most teams.

**What are the risks**

You have to keep the inside walls neat on purpose, or it slowly gets messy again. It is still one piece, so you cannot update or grow just one part by itself.

**A real example**

A school portal with grades, attendance, and messages. It is one app, but each area is walled off inside, so a change to messages does not touch grades.

### Microservices

Diagram: Orders and Orders data, Billing and Billing data, Users and Users data

**What problem does it solve?**

Many teams keep waiting on each other, and one part of the app needs to grow much bigger than the rest.

**When to use**

Use this pattern when many teams need to build and launch on their own, or different parts of the app need to grow to very different sizes.

**What are the risks**

Much more work to run. Each small app needs its own setup and watching. The parts talk over the network, so there are more ways to break and problems are harder to find.

**A real example**

A large food-delivery app where one team runs search, another runs payments, and another runs driver tracking, each launching on its own schedule.

### Event-Driven

Diagram: Order placed, Event bus, Inventory, Billing, Notifications

**What problem does it solve?**

One thing happens and many different parts need to react, but you do not want them all tied tightly to each other.

**When to use**

Use this pattern when one thing happens and many parts need to react on their own. For example, “order placed” tells billing, shipping, and email all at once.

**What are the risks**

It can get hard to follow what happened and in what order. Using it for a simple “give me this right now” request just makes things more confusing.

**A real example**

An online store. The moment someone clicks buy, separate parts act on their own: charge the card, email a receipt, and tell the warehouse to ship.

### Serverless (functions)

Diagram: Request or event, Function, Function, Function, Database

**What problem does it solve?**

Your traffic jumps up and down, and you do not want to pay for or babysit a computer that runs all day.

**When to use**

Use this pattern when traffic goes up and down a lot. Small pieces of code run only when they are needed, then stop, so you never manage an always-on server.

**What are the risks**

There can be a short wait while the code wakes up. It is a poor fit for long jobs. It can cost more when it runs a lot, and you depend heavily on one company's tools.

**A real example**

A “contact us” form. A tiny bit of code runs only when someone hits send, emails the message, then goes back to sleep. (Close to our budgeting app on Vercel.)

### Layered

Diagram: Presentation (screens), Business logic, Data access, Database

**What problem does it solve?**

Screen code, business rules, and storage code get tangled together, so nobody can change one without breaking the others.

**When to use**

Use this pattern when you have a simple, steady app. The code is stacked in layers, and each layer only talks to the one right below it. Easy to follow.

**What are the risks**

If you are not careful, the layers get tangled and storage details leak into the wrong place. It keeps code tidy, but it does not help the app handle more people.

**A real example**

A simple to-do list app. The screen shows the tasks, the logic decides what “done” means, and the storage layer saves them, each in its own layer.

### Hexagonal (Ports and Adapters)

Diagram: Core business logic in the center, with Web / UI, Database, Message queue, and Other APIs around it

**What problem does it solve?**

Your most important rules are glued to one screen or one database, so testing them or swapping a tool is painful.

**When to use**

Use this pattern when the real rules of your app matter. The main rules sit in the middle, and screens, databases, and other tools plug in around them.

**What are the risks**

For very simple apps it adds extra steps you do not need. Used everywhere by habit, it just makes easy things harder to read.

**A real example**

A bill-splitting tip calculator. The math sits in the center, so you can swap the screen or change how it saves without touching the math.

### SOA (Service-Oriented Architecture)

Diagram: Client app, Enterprise Service Bus, Service A, Service B, Service C

**What problem does it solve?**

A big company has many separate systems that all need to share information with each other.

**When to use**

Use this pattern when you work in a big, older company where many systems already share one central hub to talk to each other.

**What are the risks**

That shared hub can get overloaded and become the one thing that takes everything down. Lots of rules and approvals slow the work. It is an older way of doing things.

**A real example**

A large bank where the website, the phone app, and the ATM all talk to the same central account system through one shared hub.

### CQRS (Command Query Responsibility Segregation)

Diagram: App, Command (write) to Write database, Query (read) from Read database

**What problem does it solve?**

Reading data and saving data need very different things, and one design cannot do both jobs well.

**When to use**

Use this pattern when reading data and saving data are very different jobs, so you want to handle each one in its own way.

**What are the risks**

The reading side can fall a little behind the saving side, so people may see slightly old info for a moment. It is extra work, and overkill for most simple apps.

**A real example**

A live sports scores app. Millions read the score every second, while only a few referees update it, so reading and writing are handled apart.

### Event Sourcing

Diagram: Command, Event log (append only) with Event 1, Event 2, Event 3, Current state

**What problem does it solve?**

Saving only the latest number loses the story of how you got there, and you need to prove every change.

**When to use**

Use this pattern when you need a full history of every change, like money accounts or orders, so you can see exactly what happened and when.

**What are the risks**

A big jump in difficulty. You keep a growing list of every change forever, and rebuilding the current total from that list takes care. Too much for a simple app.

**A real example**

A bank account that keeps every deposit and withdrawal ever made, not just today's balance, so you can prove exactly how the balance got there.

### Domain-Driven Design (DDD)

**Bounded contexts, each with its own model**

Diagram: Orders context, Billing context, Shipping context

**What problem does it solve?**

The business has lots of complicated rules, and the code keeps mixing up ideas that mean different things to different teams.

**When to use**

Use this pattern when your app has lots of tricky, changing rules. It helps you find the clear lines between the different parts of the business.

**What are the risks**

Too much for a simple app. It only works if you spend real time with the people who know the business, and drawing the lines wrong is costly to fix.

**A real example**

A hospital system with very different worlds: scheduling, billing, and patient records. You map clear boundaries so each area has its own rules.

### Space-Based

Diagram: Processing unit, Processing unit, Processing unit, In-memory data grid, Database (async)

**What problem does it solve?**

So many people show up at once that one database becomes a traffic jam and the app slows to a crawl.

**When to use**

Use this pattern when you expect huge, sudden crowds that one normal database cannot keep up with. The data is kept in fast shared memory instead.

**What are the risks**

Very hard to build and run. Keeping all the copies of the data in step is tricky. It is a rare, special-case choice that is easy to overdo.

**A real example**

A concert ticket site the morning tickets drop. A hundred thousand people hit buy at once, so the data lives in fast shared memory to survive the rush.

### Pipeline (Pipes and Filters)

Diagram: Input, Filter 1, Filter 2, Filter 3, Output

**What problem does it solve?**

Data has to go through many steps in order, and doing it all in one big blob is hard to fix or change.

**When to use**

Use this pattern when work moves through a line of steps, each doing one job and passing it on. Good for cleaning and processing data.

**What are the risks**

Not good for quick back-and-forth with a person. If one step is slow or breaks, the whole line stops. Hard to handle “if this, then that” choices.

**A real example**

A photo upload tool. Each photo flows through steps: shrink it, remove private info, add a watermark, then save it. One step at a time.

### Microkernel (Plugin)

Diagram: Core system with Plugin A, Plugin B, Plugin C, Plugin D

**What problem does it solve?**

You want new features added to your app without changing or risking the core that everything depends on.

**When to use**

Use this pattern when you have a small core and want add-ons that snap on extra features, like add-ons for a web browser.

**What are the risks**

Keeping the add-on rules steady over time is hard. One bad add-on can crash the whole thing. It does not help the app handle more people.

**A real example**

A simple photo editor. The core edits images, and extra filters and tools snap on as add-ons, like plugins.

### Cell-Based

Diagram: Router (splits traffic by user), Cell 1 (own app and data), Cell 2 (own app and data), Cell 3 (own app and data)

**What problem does it solve?**

In a huge app, one breakdown takes down every single user at the same time.

**When to use**

Use this pattern when you run a very large app. You split users into separate sealed groups called cells, so a problem in one cell does not spread to the others.

**What are the risks**

A lot of work to run many copies. Sending each user to the right cell, and sharing anything across cells, is hard. Overkill until you are very big.

**A real example**

A huge chat app used across many countries. Users are split into sealed groups, so an outage for one group never knocks out everyone else.

## Business Logic Design

[image not saved]

### Three Approaches to Architecting Business Logic in the Domain Layer

Every app has business rules. The logic of the application lives in the domain layer. Martin Fowler describes three main ways to organize the code for those rules. They are called Transaction Script, Table Module, and Domain Model. All three can work well. The right one depends mostly on how complex your rules are, and how complex they are likely to become.

**Which approach fits your business logic rules?**

**Simple business logic**

Your rules are simple, and they will stay simple.

ADHD Budget App example: add a transaction, show how much is left in a budget, and start every budget over on the first of the month.

**Usually the best fit:** Transaction Script

**More complex business logic**

Your rules are in between, and the tools you build with are organized around tables of data.

ADHD Budget App example: the same budgeting rules, built with tools where the screens and the code all pass around tables of rows and columns, as many Microsoft .NET tools do.

**Usually the best fit:** Table Module

**Very complex business logic**

Your rules are complex, or they keep growing.

ADHD Budget App example: budgets start over on different schedules, unspent money can roll over to next month, two people can share one budget, and reminders depend on how fast someone is spending.

**Usually the best fit:** Domain Model

Not sure which row you are in? That is normal. Nobody knows how to measure how complex a set of rules is. Experienced people look at what the app needs to do and make a judgment call. If you start simple and your code begins to tangle as the rules grow, that is the signal to move toward a Domain Model.

### Transaction Script

One set of steps for each action a person can take in the app.

Best for simple rules

**What it looks like in the ADHD Budget App**

Each action on the left gets its own list of steps on the right.

**Steps for: Add a transaction**

1. Check what the person typed
2. Work out what is left in the budget
3. Save the transaction to the database
4. Send the answer back to the screen

**Steps for: Show what is left**

1. Load the budget from the database
2. Work out what is left in the budget
3. Send the answer back to the screen

**Steps for: Start a budget over**

1. Load the budget from the database
2. Clear this period's spending
3. Save the budget to the database
4. Send the answer back to the screen

Notice the orange step. The same rule, working out what is left in the budget, is written in two different places. If someone later changes one copy and forgets the other, the app gives two different answers to the same question.

**Good when**

✓  The rules are simple and will stay simple.

✓  You want something quick to build that anyone on the team can follow.

✓  Each action can be handled from start to finish on its own.

**Watch out**

✗  The same rule gets copied into several places.

✗  Copies slowly drift apart and start giving different answers.

✗  Long chains of if-this-then-that checks pile up as the rules grow.

**The full explanation**

With a Transaction Script, you write one procedure for each thing a person can do in the app. A procedure is a list of steps the computer follows from top to bottom. Each procedure takes what the person typed, checks it, does the math, saves the result to the database, and sends an answer back to the screen. Steps that several procedures share can be pulled out into smaller helper procedures, but the main way the code is organized is still one procedure per action.

It is the simplest of the three approaches. Most developers understand it right away, and it is fast to write. Each procedure is also a natural place to start and finish saving to the database, which makes it easy to be sure an action either fully happens or does not happen at all. Fowler says not to dismiss it. Many problems really are simple, and a simple solution gets you running much faster.

The trouble starts as the rules grow. Because each procedure is written on its own, the same rule tends to get copied into several procedures, like the orange step in the picture. Every new kind of budget or special case adds another if-this-then-that check, and those checks end up repeated in every procedure that cares. Over time the code becomes a tangle that is hard to change safely. You can move from Transaction Script to a Domain Model later, but it is painful, so Fowler suggests making the choice early.

**Usually paired with**

Simple database helpers called a Table Data Gateway or a Row Data Gateway. They hold the database commands, so each procedure can ask for the data it needs without writing those commands itself.

### Table Module

One piece of code for each table in the database, which handles every row in that table.

Best for in-between rules

**What it looks like in the ADHD Budget App**

Follow the arrows from top to bottom. Each step is explained on the right.

1. **Database:** The database has a budgets table, with one row for every budget a person has created.
2. **Budgets record set** (ID 12 Groceries \$400; ID 13 Rent \$1,200; ID 14 Fun money \$150): A query copies those rows into a record set. A record set is a temporary copy of rows and columns, shaped just like a table, that the code can work with.
3. **Budgets module, handles every budget row:** There is only one Budgets module, no matter how many budgets there are. To work on one budget, the code passes in that budget's ID. For example: work out what is left for budget 12.
4. **Screen, shows the budgets as a table:** The same record set can go straight to the screen and appear as a table. When someone edits it, the changes go back through the module to be checked before they are saved.

**Good when**

✓  Your rules are in between simple and complex.

✓  Your tools are built around tables of data, like many Microsoft .NET tools.

✓  You want all the logic for one table kept together in one place.

**Watch out**

✗  It cannot give each budget its own rules, so different kinds of budgets fall back to if-this-then-that checks.

✗  Every action on one row needs that row's ID passed in.

✗  Without table-based tools, Fowler would skip it.

**The full explanation**

With a Table Module, you write one piece of code for each table in the database. The ADHD Budget App might have a Budgets module that handles every row in the budgets table, and a Transactions module that handles every row in the transactions table. There is only one Budgets module, no matter how many budgets exist. So whenever the code needs to work on one specific budget, it passes in that budget's ID, the unique number that identifies it.

The data usually arrives as a record set, a temporary copy of rows and columns pulled from the database. Several modules can work on the same record set, and the screen can show that record set directly as a table. That is the main reason to choose it: it fits tools that are built around tables of data. Fowler points to Microsoft .NET as the classic example, where the screens, the data tools, and the business logic all pass the same record sets around. It is also easy to test, because you can build a record set in memory without a real database.

It sits in the middle of the three approaches. It gives more structure than separate procedures, because all the logic for one table lives together, so copied code is easier to spot and remove. But because there is only one module for the whole table, there is no separate piece of code for each individual budget. When different kinds of budgets need different rules, the code falls back to if-this-then-that checks, just like a Transaction Script. For truly complex rules, a Domain Model handles this better.

**Usually paired with**

A Table Data Gateway, a helper that runs the database queries and hands back the record sets for the modules to work on.

### Domain Model

A set of objects that match the real things in the business, where each object holds its own information and its own rules.

Best for complex rules

**What it looks like in the ADHD Budget App**

Each box is one object. Lines show which objects are connected and work together.

**Budget object: Groceries**

- What it knows: Spending limit: \$400. Time period: this week
- What it can do: Work out what is left. Decide when to start over
- Connected to: Transaction object (\$32 at the market), Transaction object (\$18 for lunch), Category object (Food)

**How a budget starts over**

Each schedule is its own small piece. This budget is connected to the one it uses.

- Every Monday (In use by the Groceries budget)
- First of the month
- Never
- \+ Add a new one

To support a new schedule, you add one new piece. Nothing else in the app has to change. Fowler calls these swappable pieces strategies.

**Good when**

✓  Your rules are complex, or you expect them to keep growing.

✓  Different kinds of things need different rules.

✓  You want each rule to live in exactly one place.

**Watch out**

✗  It takes the longest to learn. Fowler says it can take months to feel natural.

✗  At first it can feel like hunting from object to object to find where something happens.

✗  Saving the objects to a database takes extra work, which does not pay off for simple rules.

**The full explanation**

With a Domain Model, you build a set of objects that match the real things in the business. An object is a piece of code that holds both some information and the rules that use that information. The ADHD Budget App might have a Budget object, a Transaction object, and a Category object, with one object for each real budget, transaction, and category. The Groceries budget object knows its spending limit and its time period, and it also knows how to work out how much is left. Instead of one long procedure doing everything, each object does the part of the work that belongs to it and hands the rest to the objects it is connected to.

This is what makes it strong when rules keep growing. Suppose budgets start over on different schedules: groceries every Monday, rent on the first of the month, and a savings goal never. In a Transaction Script, each new schedule adds another if-this-then-that check to every procedure that cares. In a Domain Model, each schedule becomes its own small piece of code, and each budget is connected to the schedule it uses. Adding a new schedule means adding one new piece, and nothing else has to change. Because each rule lives in one place, it is not copied around. The rules also stay separate from the screen and the database, which makes them easier to test and to change.

The cost is effort up front. Fowler says people new to this way of building often need several months before it feels natural, and some developers never get comfortable with it. The logic is spread across many small objects, so at first it can feel like you are hunting from object to object to find where something happens. Saving these objects to a database also takes more work, because objects are not shaped like database tables. For simple rules, that extra cost never pays off, which is why the simpler approaches still have a place.

**Usually paired with**

A simple Domain Model, where each object closely matches one table, can use Active Record, where each object saves itself. A rich Domain Model, with many connected objects and swappable pieces, needs a Data Mapper, a separate layer that moves information between the objects and the database.

### The three side by side

|  | Transaction Script | Table Module | Domain Model |
| --- | --- | --- | --- |
| Organizes the code around | Each action a person can take | Each table in the database | Each real thing in the business |
| Best for | Simple rules | In-between rules, built with table-based tools | Complex or growing rules |
| Effort to get started | Lowest | Low, if your tools are built around tables | Highest |
| As the rules grow | Rules get copied and tangled | Better, but still falls back to if-this-then-that checks | Grows smoothly by adding new pieces |
| Usually paired with | Table Data Gateway or Row Data Gateway | Table Data Gateway | Active Record or Data Mapper |

**Choosing in practice**

- Start with the simplest approach that fits your rules today, while keeping an eye on where the rules are heading.
- You can mix them. It is common to use Transaction Scripts for a few simple parts of an app and a Domain Model for the rest.
- If you start with Transaction Scripts and they begin to tangle, move toward a Domain Model. Going the other way is rarely worth it.
- The team matters. A team that already knows how to build a Domain Model makes it a cheaper choice. Fowler says the better the team, the more he leans toward it.
- A Service Layer can sit on top of a Table Module or a Domain Model to list every action the app offers in one place. You can see it in the Layers of Software Architecture section.

## Design System Code

[image not saved]

### Design Systems 101

**What is a design system?**

- A design system is a set of rules and ready-made pieces that make every screen in an app look and work the same way.
- Designers use it to design screens. Developers use it to build those screens in code.
- When both use the same system, what gets designed is what gets built.
- You do not have to be a designer to use one. It gives you good design choices that are already made.

**What is Material UI?**

- Material UI is a free, open-source library of ready-made React components.
- It follows Google’s Material Design rules. Right now, it follows Material Design 2.
- It has more than 40 components, like Button, Text Field, Table, Alert, and Tooltip.
- In this class, your Next.js app uses Material UI for every screen people see. This is tier 1.
- To see every component, go to [mui.com/material-ui](http://mui.com/material-ui).

**Design words and code words for the same things**

Designers and developers often use different words for the same part of a design system. This table matches them up.

| Part | In design (like Figma) | In code (Material UI) |
| --- | --- | --- |
| Design tokens | Saved styles and variables for colors, fonts, and spacing. | Values saved in one theme file, like the main brand color. |
| Colors | Color styles, like primary, secondary, and error. | The palette in the theme, like palette.primary.main. |
| Typography | Text styles, like Heading 1 and Body. | Typography in the theme, like h1 and body1. |
| Spacing | A spacing scale for gaps and padding. | theme.spacing. One step is 8 pixels by default. |
| Components | Reusable components in a shared library. | React components, like \<Button> and \<TextField>. |
| Variants | Component variants, like filled or outlined. | Props, like variant="contained" or variant="outlined". |
| States | Frames for hover, focus, pressed, and disabled. | Built-in states, plus props like disabled. |
| Screen sizes | Separate frames for phone, tablet, and desktop. | Breakpoints in the theme: xs, sm, md, lg, and xl. |
| Guidelines | Notes on when and how to use each piece. | The documentation page for each component on [mui.com](http://mui.com). |

**What Material UI pieces look like**

These are drawn to match Material UI’s default look. Under each one is the code a developer writes to use it.

- **Button:** SAVE `\<Button variant="contained"\>`, CANCEL `\<Button variant="outlined"\>`, LEARN MORE `\<Button variant="text"\>`
- **Text Field:** Email, [name@example.com](mailto:name@example.com) `\<TextField label="Email" /\>`
- **Alert:** Your changes were saved. `\<Alert severity="success"\>`
- **Chip and Switch:** Budget `\<Chip label="Budget" /\>`, `\<Switch checked /\>`

**How the theme works**

- The theme is one file that holds your design tokens: your colors, fonts, spacing, and screen sizes.
- A developer makes it with createTheme. Then they wrap the app in a ThemeProvider, so every screen uses the same theme.
- If you change a color in the theme, every button and link that uses that color changes too.
- The theme can also set defaults for each component, like making every button outlined.
- Material UI has a light theme and a dark theme. It uses the light theme unless you change it.

**How designers and developers work together**

- Designers choose the tokens: brand colors, fonts, and spacing. Developers put those tokens into the theme.
- Designers use Material UI pieces in their designs, so developers do not have to build new pieces from scratch.
- If a design needs something Material UI does not have, talk about it before anyone builds it.
- When the design and the code use the same tokens and pieces, the app looks the same as the design.

**How to use Material UI with Claude Code**

- Ask Claude: “Set up Material UI in my Next.js app with a theme file.” Claude follows the Material UI steps for Next.js.
- Give Claude your brand colors and fonts. Ask it to put them in the theme.
- Ask Claude to use Material UI components instead of making new ones from scratch.
- Ask Claude: “Does this use the theme, or did you type a color straight into the code?” Colors typed straight into the code break the design system.
- Ask Claude to write an ADR for your design system choices.

## ADHD Budget On the Internet

[image not saved]

### A Reminder About Network Architecture

When you build a product that is hosted on the internet (a web application or a website), you will hear about Two Tier and Three Tier. In Two Tier, the client talks straight to the database server. In Three Tier, only the web server talks to the database server.

**“Two Tier Architecture”**

Client + Database Server

**“Three Tier Architecture”**

Client + Web Server + Database Server

ADHD Budget App is a three-tier network architecture!

### ADHD BUDGET APP on the Internet

Expanded from week 1 lesson and applied to the ADHD Budget App. Here is how the internet works. You must understand this concept in order to properly become an AI developer, because you will be building multiple components o this flow while you build applications!

**YOUR COMPUTER**

**1. Go to an internet browser and type in the URL for ADHD BUDGET APP**

“Let’s budget!” ([www.pliers-vercel-1054.com](http://www.pliers-vercel-1054.com))

**HTTP / API REQUEST**

**2. Your browser creates a request to receive the files from YOUR WEB SERVER THAT HOSTS THE ADHD BUDGET APP**

HTTP packet structure. Credit: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)

What a packet looks like in the browser. Hit F12 key on your internet browser and select the Network Tab to see all different kinds of HTTP requests and responses. Credit: Chrome Dev Tools

**“THE CLOUD” AKA THE INTERNET**

**3. First, DNS finds the server for your web address. Then your request hops across routers on the INTERNET.**

**YOUR WEB SERVER, HOSTED ON VERCEL**

**4. The request is routed to a SERVER specifically hosting YOUR website files. This server has:**

- ADHD Budget App code files
- Image files
- Web Script files
- Database Script files

**YOUR DATABASE SERVER, HOSTED ON SUPABASE**

**5. The WEB SERVER connects to the DATABASE SERVER which holds the database files and scripts, so that you can retrieve your own account information and whatever else is stored on the database for you as a customer. This is done through a language called SQL. The WEB SERVER runs a script that starts a SQL QUERY REQUEST to the DATABASE SERVER.**

**SUPABASE DATABASE SERVER RESPONSE**

**6. The DATABASE SERVER responds with the results, called the “payload”, after the request gets processed from the WEB SERVER. It spits it back to the WEB SERVER in the form of a SQL QUERY RESPONSE.**

**ADHD BUDGET WEB SERVER RESPONSE**

**7. Now that the WEB SERVER has the PAYLOAD from the database and from its own files, the WEB SERVER replies to your request within the same HTTP language called an HTTP RESPONSE, back over the CLOUD**

**YOUR COMPUTER: HTTP / API RESPONSE**

**8. The browser loads all of the files that were sent from the server, and you see the page with the loaded files.**

“Welcome to ADHD Budget Land!”

### Your Computer, Preview, and Live

**Where does your app run while you build it?**

- Your app can run in three places: on your own computer, on a preview link, and on the live site.
- Each place has its own web address.
- When something looks wrong, first check which address you are on.

**1. On your computer (local)**

- The address is [http://localhost:3000](http://localhost:3000).
- Only you can see it. It only runs while the app is started on your computer.
- Changes show up as soon as you save a file.
- Build and test here first, before anyone else sees your work.

→ Push a branch →

**2. Preview (on Vercel)**

- When you push a branch that is not main, or open a pull request, Vercel makes a preview link for it.
- Use it to check your changes on the internet before they go live.
- Your main web address does not change yet.
- Vercel may ask visitors to log in before they can see a preview link.

→ Merge into main →

**3. Live (on Vercel)**

- This is your main web address, like [your-app.vercel.app](http://your-app.vercel.app).
- It updates when you merge your pull request into main.
- Everyone sees this version. This is the link you submit.

**What about the database?**

- All three places use the same Supabase database if they use the same keys.
- That means test data you add on your computer also shows up on the live app.
- Use fake data only while you test.
- Bigger teams make a second Supabase project just for testing, so testing never touches real data.

## Web Servers and Database Servers

[image not saved]

### Web Servers and Database Servers

**Web server**

**What it is**

- A web server is a computer that is always on and connected to the internet.
- It holds your app’s files, like pages, styles, pictures, and scripts.
- It also runs your server code, like API routes.

**What it does**

- It waits for people to visit your web address.
- When a request comes in, it sends back the right files.
- It runs code that must stay private, like code that uses secret keys.
- It asks the database server for information when it needs it.

**Why it is used**

- Your laptop is not always on, and other people cannot reach it.
- A web server lets anyone visit your app at any time of day.
- It keeps secret keys out of people’s browsers, where anyone could see them.

**In this class**

- Vercel runs your web server.
- Each time you push code to GitHub, Vercel puts the new version of your app online.

**Database server**

**What it is**

- A database server is a computer that is always on and saves your app’s information.
- It stores the information in tables. Each table has rows and columns.

**What it does**

- It saves new information, like a new account or a new message.
- It finds information when the app asks for it.
- It changes or deletes information when the app asks.
- It checks access rules, so each person only sees what they are allowed to see.

**Why it is used**

- Without a database, your app forgets everything when the page closes.
- It keeps information in one place, so every person sees the same answer.
- It lets many people save and read information at the same time.

**In this class**

- Supabase runs your database server.
- Supabase also handles accounts and sign-in.

### Where do Servers Live?

**Host It in a Data Center**

**What it means**

- A company runs the server for you. You connect your code or your data to their service.

**What you do**

- You sign up on their website and connect your GitHub repository.
- You choose settings and add your secret keys.

**What they do**

- They keep the server running all day and night.
- They add security updates and fix problems with the machines.
- Many of them make backups for you.

**This is a good choice when**

- You are new to coding.
- You want to spend your time building the app, not running servers.
- You want to start for free and pay more only when your app grows.

**Watch out for**

- Free plans have limits on how much you can use.
- You follow the company’s rules and prices.
- Moving to a different company later takes work.

**Examples**

- Web servers: Vercel and Netlify.
- Database servers: Supabase and Neon.

**Host it Yourself at Your House**

**What it means**

- You run the server. It can be your own computer, or an empty computer that you rent online.

**What you do**

- You install and set up all of the server software yourself.
- You keep it running, add security updates, and make backups.

**What you are responsible for**

- If the server stops at night, you have to fix it.
- If you miss a security update, your app and your data can be at risk.

**This is a good choice when**

- A law or a contract says your data must stay on your own machines.
- You need full control over every setting.
- Someone on your team knows how to run servers.

**Watch out for**

- It takes much more time to learn and set up.
- The work never stops. Servers need care every week.

**Examples**

- Web servers: a rented computer from DigitalOcean or Amazon Web Services, with web server software you install.
- Database servers: PostgreSQL that you install on your own server.

### How To Choose The Right Path

| Factor | Self-Hosting | Hosting Provider |
| --- | --- | --- |
| Effort | Most complex | Least complex |
| Cost | Most expensive | Least expensive |
| Maintenance | You maintain the machines and the code. | They maintain the machines. You still maintain your code and data. |
| Ownership | You own the machines and the code. | You own your code and data. They own the machines. |
| Security | Not secure by default, can make secure | Not secure by default, can make secure |
| Privacy | Not private by default, can make private | Not private by default, can make private |

## How to Launch

[image not saved]

### In This Class, This Is How You Launch

**Set up your accounts and tools**

**1. Make your free Vercel and Supabase accounts.**

- You already set up Claude Code and GitHub in Week 1.
- Sign up for Vercel and Supabase with your GitHub account. Pick the free plan on each one.

**2. Check that your computer is ready.**

- Open Claude Code in a new folder for this project.
- Ask Claude: “Check that Node.js is installed. If it is not, help me install it, and explain what it does like I’m 5.”

**3. Gather your saved documents.**

- Get your vision, scope, requirements, and build order from the last few weeks.
- You will give these to Claude at the start of every new chat.

**Build the app on your computer**

**4. Make the project and a GitHub repository.**

- Ask Claude to make a new Next.js app that uses Material UI.
- Ask Claude to put it in a new GitHub repository and push the first version.

**5. Architect the app.**

- Tier 1 is the screens. Plan each screen people will see and click. You will build them with Material UI.
- Tier 2 is the server code. Plan where your app’s rules will live. This code runs on Vercel.
- Tier 3 is the database. Plan what information your app needs to save. It lives on Supabase.
- Ask Claude to write the plan in a document and save it in your repository before you write any code.

**6. Write down your big decisions as ADRs.**

- Make a folder in your repository called docs/adr. Add a line to your [CLAUDE.md](http://CLAUDE.md) file that tells Claude to read every ADR before it makes changes.
- Ask Claude to write one ADR for each big choice in your plan, like Next.js with Material UI, Vercel, and Supabase.
- Read each ADR and fix anything that is wrong. Then commit and push them to GitHub.

**7. Design your database tables.**

- Ask Claude to design the tables from your requirements and explain each one.
- Ask Claude to save them as a migration file and turn on access rules for every table.

**8. Connect the app to Supabase.**

- Make a new project on the Supabase website. Pick the free plan.
- Claude writes the SQL that makes your tables and access rules. SQL is the language databases use.
- Way 1: Copy the SQL from Claude. Paste it into the SQL Editor in Supabase, and click Run.
- Way 2: Connect Claude Code to your Supabase project. Then Claude can make the tables and run the SQL for you. Ask it to show you what it will change before it runs anything.
- Either way, ask Claude to save the SQL as a migration file in your repository. This keeps a record of every change to your database.
- A migration is a file of SQL that makes one change to your database, like adding a table or a column.
- Each migration file has a number or a date in its name, so the changes run in the right order. Together, the files are the full history of your database.
- To change your database later, add a new migration. Do not edit a migration that already ran.
- Ask Claude to make every database call from your server code, never from the browser. Keep the access rules on too, as a second lock.
- Put your Supabase keys in a local environment file. Never put secret keys in your code or on GitHub

**9. Build one feature at a time.**

- Start with sign-up and sign-in. Then build the next feature in your build order.
- For each feature, build the screen, the server code, and the database part together.
- If you make a new big choice while you build, ask Claude to write a new ADR before it writes the code.

**10. Run and test the app on your computer.**

- Ask Claude how to start the app on your computer. Then click through every screen.
- Check that one person cannot see another person’s information.

**Launch it on the internet**

**11. Connect your GitHub repository to Vercel.**

- In Vercel, import your GitHub repository.
- Add your Supabase keys in Vercel’s environment variable settings.

**12. Push your code and let Vercel publish it.**

- Each push to the main branch puts a new version of your app online.
- If the build fails, copy the build log and give it to Claude.

**13. Test the live app.**

- Open your Vercel web address. Sign up as a new person and test every feature.
- Check the free plan limits. Supabase pauses free projects that are not used for a while.

**14. Save what you learned and keep building.**

- Ask Claude to write down what you built and what you decided. Save it in your repository.
- Give that document to Claude in your next chat to build the next feature.

## When Something Breaks

[image not saved]

### When Something Breaks

**Where to look first**

- Every problem leaves a clue. Your job is to find the error message and give it to Claude.
- If the screen looks wrong, start in the browser.
- If the build failed, start in Vercel.
- If information is missing or will not save, start in Supabase.

**Browser troubleshooting**

- Open the developer tools. Press F12 on Windows, or Cmd + Option + I on a Mac.
- Click the Console tab. Red lines are errors. Copy them and give them to Claude.
- Click the Network tab, then reload the page. Look for requests in red. Click one to see what the server sent back.
- A number in the 400s means the request had a problem. 401 means you are not logged in. 403 means you are not allowed. 404 means it was not found.
- A number in the 500s means the server code broke. Check Vercel next.
- Try a private window. It does not use old saved files, so you see the newest version.

Picture: Chrome Console tab. The red line is an error. Source: Chrome for Developers.

Picture: Chrome Network tab. Each row is one request. Source: Chrome for Developers.

**Vercel troubleshooting**

- Open your project in Vercel and click Deployments.
- If a deployment says Error, the build failed. Open it, copy the build log, and give it to Claude.
- If the build worked but the live app breaks, open the Logs page. It shows errors from your server code.
- Open Settings, then Environment Variables. Every key from your .env.local file must be there too.
- After you change an environment variable, deploy again. The change does not work until you do.
- If the app works on your computer but not on Vercel, check for a missing key first.
- On the free plan, Vercel keeps these logs for only 1 hour. Check them soon after the problem happens.

Picture: Vercel Deployments page. The red dot and the word Error mean the build failed. Source: Vercel docs.

Picture: A build log. Look for the red lines with the word Error. Source: Vercel docs.

Picture: Vercel Logs page. It shows errors from your server code. Source: Vercel docs.

Picture: Vercel Environment Variables settings. Add each key from .env.local here. Source: Vercel docs.

**Supabase troubleshooting**

- Open the Table Editor. Check that the row you saved is really there.
- If your app shows nothing and no error, an access rule may be blocking it. Access rules hide rows without showing an error.
- Open Authentication to see the people who signed up.
- Open the Logs page to see errors from the database.
- If everything stopped working, check if your project is paused. Click “Resume project.”

Picture: Supabase Table Editor. Each row is one saved record. Check here that your data was saved. Source: Supabase.

**How to ask Claude for help**

- Copy the exact error message. Do not retype it.
- Say what you did, what you expected, and what happened instead.
- Say where you saw it: the browser, Vercel, or Supabase.
- Ask Claude to explain the problem in plain words before it fixes it.

# Homework

(linked page https://app.notion.com/p/f4b1a3bddce583c1a1ed0161a0078312, not accessible)
