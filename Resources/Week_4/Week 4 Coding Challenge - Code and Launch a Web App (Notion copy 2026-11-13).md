# Week 4 Coding Challenge - Code and Launch a Web App for People with ADHD to Budget

- **Source (live):** [Week 4 Coding Challenge](https://tech-fleet-community-dao.notion.site/Week-4-Coding-Challenge-Code-and-Launch-a-Web-App-for-People-with-ADHD-to-Budget-f4b1a3bddce583c1a1ed0161a0078312)
- **Read from:** the owner's fresh Notion copy of the live Homework page, made 2026-11-13 22:08 (`app.notion.com/p/1169219a469182f2991f8174d94f2e4a`, inside "Tech Fleet course copies 2026-11-13").
- **How faithful:** text is word for word, in the page's order. The video block ("Week 4: Code and Launch", an .mp4) was left out. Sub-pages (the templates and How-To pages) are in the Notion copy but **not saved here yet**.
- **Checked against live:** due date Nov 16 and the homework-table row match the live homework index page read on 2026-11-13. The earlier live read of this page (Firecrawl, 2026-11-12) lists the same repo rule, stack, 3 ADRs, database template, safety rule and submission steps.
- **Week numbering:** this is the course's **Week 4**. Older local copies called the same assignment "Week 3 - Host a Web App." The page itself still says "Week 3 lecture board" and names the repo "Week 3 - ADHD Budgeting App."
- **Owner's track:** Premium (own app, the caregiving coordinator).

---

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
