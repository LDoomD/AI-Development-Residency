# Week 4 - Web Hosting - Weekly Class Materials
- Source copy: https://app.notion.com/p/e889219a4691828b8c4a812b47b3295e
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:09:48.973Z
- Not saved: none (Lecture Transcript item is plain text with no link; NotebookLM/Gemini notebook, podcast, quiz, flash card and slide links are external and not followed)

---

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
