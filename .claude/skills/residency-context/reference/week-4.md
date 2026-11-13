# Week 4: Code and Launch a Web App (host on Vercel and Supabase)

> **Current copy, 2026-11-13.** Built from the owner's fresh Notion copies of the live Tech Fleet pages (word for word). Live course week number: **4**. Due: Nov 16.
> Full saved pages (lecture notes, templates, transcripts) are in `Resources/`; paths at the bottom.
> Sources: `Resources/Week_4/`
> Older local files called this assignment "Week 3 - Host a Web App." The page itself still says "Week 3" in the repo name and "Week 3 lecture board."

---

## Table of contents (line numbers are for this file)

**Reading rule:** read this whole file, top to bottom, before answering any question about this week. This list only shows what is in the file. Never use it to skip a section.

  - line 51: Coding challenge
  - line 55: Video: Code and Launch
  - line 58: How to Submit
  - line 63: What are we doing?
  - line 66: Summary
  - line 69: Standard Residency Objective
  - line 72: Premium Residency Objective
  - line 75: Before You Start
  - line 81: BASIC HOMEWORK
  - line 100: ADVANCED HOMEWORK
  - line 110: Deliverables Templates
  - line 121: Tools
  - line 129: How To's
  - line 134: Deliverables
  - line 140: Requirements
  - line 154: Lecture Resources
  - line 164: To Submit
    - line 174: Expand for Submission Template (toggle)
  - line 191: Before You Submit, Check These
  - line 199: Getting Help
  - line 207: Weekly class materials
- line 209: Overview
- line 213: Objectives
- line 221: Work You’ll Do
- line 232: Bonus Work
- line 240: Estimated Workload
- line 248: Class Lecture
- line 256: Class Learning Materials
- line 263: Examples
- line 267: Homework
  - line 269: Instructions
  - line 273: What Does Good Homework Look Like?
  - line 286: Full saved files (all in `Resources/Week_4/`)

---


## Coding challenge

**Copy this page, and add your deliverables to the page:** Week 4 Coding Challenge - Build and Launch Templates (sub-page)

## Video: Code and Launch
*(video, not saved)*

## How to Submit
Email your teacher the Submission Template with your links filled in to mdenner@techfleet.org

**Due date:** Nov 16

## What are we doing?
This week you are going to build and launch the **app that lets people with ADHD budget wisely and effectively.** You will turn the product specifications you wrote in Week 2 into a real, working web app that anyone can open on the internet. Every student builds the entire MVP #1 this week.

## Summary
Now it's time to build and ship! Your product requirements from Week 2 Coding Challenge - Develop Product Specifications for the ADHD Budgeting App are going to become a reality with Claude Code. You will build a three-tier web app. The screens are built with Next.js and Material UI. The server code runs on Vercel. The database runs on Supabase. You do not have to build or run your own servers. Vercel and Supabase host them for you.

## Standard Residency Objective
Take the product specifications you made in Week 2, and build the ADHD Budgeting App with Claude Code. Use Next.js with the Material UI design system for your screens. Host the app on Vercel. Store the data in Supabase.

## Premium Residency Objective
You are not building an app for people with ADHD to budget, you are building the app you chose based on your specialization. Build that using these same tools and the product specifications you made.

## Before You Start
1. Your Week 2 product specifications and backlog are ready. If you did not finish Week 2, finish the vision, scope, and epics, features, and tasks first. You need them to tell Claude what to build.
2. You have the GitHub repository you made in Week 2, called "Week 3 - ADHD Budgeting App." Use this same repository. Do not make a new one.
3. Claude Code and GitHub work on your computer. You set these up in Week 1.
4. You have free accounts on Vercel and Supabase. Step 1 of the Build and Launch Checklist shows you how.

## BASIC HOMEWORK
Every student builds the entire MVP #1 this week. That is the basic homework. The app must be fully functioning. A screen that only looks right, but does not work, does not count.

1. The entire MVP #1 is built and fully functioning. Every epic, feature, and task in your Week 2 MVP #1 scope works in your live app.
2. Every screen, button, link, and form works. Nothing is fake, empty, or "coming soon." The app shows no errors.
3. A working database in Supabase. Your live app saves information to it and reads it back. If you log out and log back in, your information is still there.
4. Every MVP #1 ticket on your Backlog Kanban Board is in Done.
5. A Next.js app that uses Material UI, saved in your GitHub repository
6. Implemented Material UI design system
7. People can sign up and log in
8. Every feature saves its information to Supabase and shows it again
9. Each person can see only their own information
10. At least three ADRs in `docs/adr`: one each for Next.js with Material UI, Vercel, and Supabase
11. A new ADR for every other big choice you make while you build
12. A database diagram
13. The app is live on Vercel
14. The app is published at a web address from Vercel so that visitors around the world can get to the website. The free your-app.vercel.app address is fine. You do not need to buy a domain.
15. A filled-out Submission Template

## ADVANCED HOMEWORK
Everything in basic PLUS:

1. **Test the app with 1 - 2 real people.** Watch them use the app and tell them to think aloud as they use the app. Capture their reactions and perspectives. Use the Usability Test Plan and Script Template.
2. **Document** the confusion, effectiveness, or problems that people faced in a research report. Use the Usability Test Results and Analysis Template.
3. **Create user requirements and technical requirements** for the changes based on the research report.
4. **Feed the requirements** from testing back into Claude
5. **Code** a new version of the app.
6. **Launch** the new version on GitHub, Vercel, and Supabase

## Deliverables Templates
Go to these links to get the templates to use with Claude

1. Build and Launch Checklist
2. Architecture Decision Record (ADR) Template
3. Database Design Template
4. Keep Your App Safe Checklist
5. Submission Template
6. Usability Test Plan and Script Template (Advanced Homework)
7. Usability Test Results and Analysis Template (Advanced Homework)

## Tools
1. Claude Code
2. GitHub
3. [Next.js](https://nextjs.org/)
4. [Material UI](https://mui.com/material-ui/)
5. [Vercel](https://vercel.com/) (free plan)
6. [Supabase](https://supabase.com/) (free plan)

## How To's
- Week 4 Coding Challenge - Build and Launch Templates
- How to Set Up GitHub and Vercel
- How to Run Your First Supabase Migration

## Deliverables
1. Your GitHub repository, with your code, your ADRs in `docs/adr`, and your database migration files
2. Your Vercel link with the live app, with the entire MVP #1 working
3. Your database diagram, saved in the `docs` folder of your repository
4. Your Submission Template, saved in your repository and sent in your email

## Requirements
Work with Claude AND Fleety the Tech Fleet Helper Bot to learn how to do each step. Follow the Build and Launch Checklist. It has the same 14 steps as the lecture.

1. Take your product requirements from Week 2 homework and give them to Claude Code. Build every feature in your MVP #1 scope, one feature at a time.
2. Move your tickets across your Week 2 Backlog Kanban Board as you work. Move a ticket to In Progress when you start it, and to Done when it works on your live app.
3. Build the app in the GitHub repository you made in Week 2, called "Week 3 - ADHD Budgeting App."
4. Write an ADR for each big decision, using the ADR Template. Save them in `docs/adr`.
5. Design your database tables with the Database Design Template. Then make the tables in Supabase. Either paste Claude's SQL into the Supabase SQL Editor, or connect Claude Code to Supabase. Either way, save the SQL as a migration file in your repository.
6. Turn on access rules (Row Level Security) for every table, so each person sees only their own information.
7. Keep your secret keys out of GitHub. Follow the Keep Your App Safe Checklist. Use fake data only.
8. Use Material UI for the interface design components.
9. Host the app on Vercel.
10. Fill out the Submission Template **(NOT USING AI)**.

## Lecture Resources
These sections on the Week 3 lecture board (Figma board `mqryoCyR9mAw3v6kyDlmes`) show you how to do this homework:

1. In This Class, This Is How You Launch (node 2490-6455)
2. Architectural Decision Records (node 2501-5349)
3. Design Systems (node 2536-7815)
4. Web Servers and Database Servers (node 2485-6149)
5. Types of Apps (node 2540-5447)
6. Dogfooding Claude (node 2443-9074)

## To Submit
1. Save the Submission Template in your repository as `Week 4 Coding Challenge/SUBMISSION.md`. Keep it separate from your code.
2. Ask Claude to put your changes on a new branch, and open a pull request on GitHub.
3. Merge the pull request into the main branch. Vercel publishes the new version of your app.
4. Open your live app and check that it still works.
5. Email mdenner@techfleet.org with the Submission Template. Include:
   1. The link to your GitHub repository
   2. The link to your live Vercel app
   3. The link to your database diagram

### Expand for Submission Template (toggle)

**Links**
1. Drop your link to the Github Repository here
2. Drop your link to your hosted Vercel app here
3. Drop your link to your database diagram here

**Documents**
1. Drop any Notion Document links here
2. Drop any other document links here

**What I Did**
Write what you did in no less than 2 paragraphs. Provide full technical detail so that anyone reading it can understand what exactly you did. DO NOT use AI for this! I will check!

**What I Learned**
Write what you learned in no less than 2 paragraphs. Describe the full details of what you learned, what you will do differently next time, and how the lessons from this exercise will help you in project team work in the future. DO NOT use AI for this! I will check!

## Before You Submit, Check These
- [ ] Open your Vercel link in a private browser window. It works, and you can sign up as a new person.
- [ ] Every feature in your MVP #1 scope works on the live app. Check each one against your Week 2 epics, features, and tasks.
- [ ] Click every screen, button, link, and form on the live app. Nothing is broken, fake, or "coming soon."
- [ ] Your database works. Add something in your live app, log out, log back in, and check that it is still there. Then open the Table Editor in Supabase and find the new row.
- [ ] Supabase pauses free projects after 7 days of low activity. If your app stopped working, open your Supabase project and click "Resume project."
- [ ] No secret keys are in your GitHub repository.

## Getting Help
1. Ask Fleety the Tech Fleet Helper Bot.
2. Bring your questions to the working sessions this week.
3. If the Vercel build fails, copy the build log and give it to Claude Code. Ask it to explain the problem before it fixes it.


---

## Weekly class materials

# Overview

Week 4 focuses on technical architecture and web hosting: deciding how an app is built so it stays reliable, fast, easy to change, and secure as more people use it. You take on the role of technical architect, the head chef of the kitchen, while Claude does the cooking as the developer. The class explains how a three-tier web app works, with the screens in the browser, the server code on Vercel, and the database on Supabase, and how a request travels between them. It covers layers, software patterns, and the three ways to organize business rules, and how to write down every big decision in an Architecture Decision Record. It also covers design systems with Material UI, the types of apps you can build, and the step-by-step way to build, launch, and fix a live web app. The goal is to build and launch the entire MVP #1 of your app as a fully working three-tier web app.

# Objectives

1. Explain what a technical architect does, and what "enterprise ready" means: reliability, scalability, maintainability, and security.
2. Describe how a three-tier web app works, and how a request moves from the browser to the web server, to the database server, and back.
3. Explain the layers of software architecture, and choose software patterns and an approach to business rules that fit your app.
4. Write Architecture Decision Records that save each big decision and why it was made, in your GitHub repository.
5. Use a design system to build your screens, launch a working app on Vercel with a Supabase database, and find and fix problems when something breaks.

# Work You’ll Do

1. Build and launch the entire MVP #1 of the ADHD budgeting app (or your specialization):
   1. A fully functioning Next.js app that uses the Material UI design system
   2. A working database in Supabase
   3. Sign up and log in, where each person sees only their own information
   4. Architecture Decision Records in your repository
   5. A database diagram
   6. The live app published on Vercel
2. Move every MVP #1 ticket on your backlog to Done

# Bonus Work

1. Test your live app with 1 to 2 real people, and turn what you learn into a new version:
   1. Usability test plan and script
   2. Research report of the problems people faced
   3. User requirements and technical requirements for the changes
   4. A new version of the app, launched on GitHub, Vercel, and Supabase

# Estimated Workload

1. 5 hours in class
2. Core homework
   1. 5 hours in homework
3. Bonus homework
   1. 8 hours in homework

# Class Lecture

1. [Text Lecture Content](https://app.notion.com/p/0869219a469183dfa3ab018af8813128) (saved as its own file: Week 4 - Web Coding Lecture Notes, copy of page 0869219a469183dfa3ab018af8813128)
2. [FigJam Lecture Content](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=2192-3744)
3. [Lecture Recording](https://app.notion.com/p/05c9219a4691824ea94201ea2c5eba3b) (saved as its own file: Fall 2026 - AI Dev Residency Recordings)
4. Lecture Transcript
5. [Lecture Slides](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/c68496d5-5c55-4e11-b79c-b28abe33ada6?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

# Class Learning Materials

1. [Gemini Notebook](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab?authuser=1)
2. [Week 4 Podcast](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/a88fa154-ab7f-473d-b416-ff16578bcd9e?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)
3. [Week 4 quiz](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/a799a055-584a-4799-8077-0f9313207e9d?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)
4. [Week 4 flash cards](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/89c94e67-3059-43ca-bd83-36ab0616e700?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

# Examples

1. https://github.com/techfleetworks/job-decoder

# Homework

## Instructions

1. Week 4 Coding Challenge - Code and Launch a Web App for People with ADHD to Budget (https://app.notion.com/p/1969219a4691834995c7818bb02e7974)

## What Does Good Homework Look Like?

1. The entire MVP #1 is built and fully functioning. Every epic, feature, and task in the student’s Week 2 MVP #1 scope works in the live app, and nothing is fake, empty, or "coming soon."
2. The app has a working Supabase database. Information is saved and is still there after the person logs out and logs back in.
3. People can sign up and log in, and each person can see only their own information.
4. The app is built with Next.js and the Material UI design system, and is live on a Vercel web address.
5. The repository has ADRs in `docs/adr` for every big decision, the database migration files, and a database diagram. No secret keys are in the repository.
6. Every MVP #1 ticket on the backlog is in Done.
7. The student has written the submission summary about what they did and learned, without using AI, and has emailed the instructor the links.


---

## Full saved files (all in `Resources/Week_4/`)
- Templates: Build and Launch Checklist, ADR Template, Database Design Template, Keep Your App Safe Checklist, Submission Template, Usability Test Plan and Results templates (titled "Rapid Prototype Test ..." in Notion)
- How-To: How to Set Up GitHub and Vercel; How to Run Your First Supabase Migration
- Lecture notes (no transcript exists; the page says "Add the transcript link here after class")
- Morgan's Week 4 example (Vision and Scope, Epics, Architecture, ADRs 0001 to 0004)
