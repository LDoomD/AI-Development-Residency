# MY STEPS - Week 4: Build and launch the app

- Made by Claude on 2026-11-18 from the course page copied on 2026-11-13. **If this page and the course page ever disagree, the course page wins.** The course page is `Week 4 Coding Challenge - Code and Launch a Web App (Notion copy 2026-11-13).md` in this folder.
- Course due date: **Nov 16**. I don't know if you have extra time. Ask Morgan.
- You are on the Premium track: you build **your own app** (the caregiving app), not the ADHD budgeting app.
- **Stay on track rule:** if a task is not on this page, it is not Week 4. Claude says so and asks before starting it.

**[Claude]** = Claude does it. **[You]** = only you can do it. **[Both]** = Claude does it, you check it.

## Decided (owner, 2026-11-18)
**The app lives in `LDoomD/Week-3---Caregiving-Coordinator`.** It is the repository you made in Week 2, and it is empty today. Your research and documents stay in `AI-Development-Residency`.
The course says this repository is public, so **no secret keys and fake data only.**
When Claude sets up the folders in step 4, it follows best practices for the folder design and shows you the layout first.

## Part 1: Accounts and tools
- [ ] **1. [You]** Make free Vercel and Supabase accounts. Sign up with your GitHub login and pick the free plan. Claude cannot make accounts for you.
- [ ] **2. [Claude]** Check that Node.js is installed, and help install it if not.
- [ ] **3. [Claude]** List your saved Week 2 documents (vision, scope, requirements, build plan) and show you the list. Claude reads these at the start of every new chat.

## Part 2: Build the app on your computer
- [ ] **4. [Claude]** Make a new Next.js app that uses Material UI, in the repository you picked. Push the first version on a new branch.
- [ ] **5. [Both]** Claude writes the plan for the screens, the server code and the database, and saves it before any code. You read it and say yes.
- [ ] **6. [Claude]** Write ADRs in `docs/adr`. You need at least three: Next.js with Material UI, Vercel, and Supabase. Write a new ADR for every other big choice.
- [ ] **7. [Both]** Design the database tables with the Database Design Template. Claude saves them as a migration file and turns on access rules (Row Level Security) for every table. You check it.
- [ ] **8. [You then Claude]** You make the Supabase project (free plan). Claude runs the SQL one of two ways: paste into the Supabase SQL Editor, or connect Claude Code. Claude shows you what will change before running anything. Keys go in `.env.local`, never in the code.
- [ ] **9. [Both]** Build one feature at a time. Start with sign-up and log-in, then the next feature in your build plan, until all of MVP #1 works. Claude writes a new ADR before any new big choice.
- [ ] **10. [Both]** Test on your computer. Make two test accounts and check that one person cannot see the other person's information.

## Part 3: Launch on the internet
- [ ] **11. [You]** Connect your repository to Vercel (import it) and add your Supabase keys in Vercel's settings. Claude walks you through it.
- [ ] **12. [Claude]** Push to `main` through a pull request. Vercel publishes it. If the build fails, give Claude the build log.
- [ ] **13. [You]** Test the live app in a private browser window and on your phone. Sign up as a new person. Check every MVP #1 feature.
- [ ] **14. [Claude then You]** Claude writes down what you built and decided and saves it in the repository. **You** fill in the Submission Template yourself. No AI.

## Tickets (all along)
- [ ] **[You]** On your Backlog Kanban Board, move a ticket to In Progress when you start it and to Done when it works on the live app. You are finished when every MVP #1 ticket is Done.

## Before you submit (all must be true)
- [ ] Your Vercel link works in a private window, and you can sign up as a new person.
- [ ] Every MVP #1 feature works on the live app.
- [ ] Every screen, button, link and form works. Nothing is fake or "coming soon."
- [ ] Add something, log out, log back in: it is still there. It is also in the Supabase Table Editor.
- [ ] If the app stopped, open Supabase and click "Resume project." Free projects pause after 7 days of low activity.
- [ ] No secret keys are in the repository.
- [ ] The database diagram is saved in the `docs` folder.

## Submit (in this order)
1. **[Claude]** Save the Submission Template as `Week 4 Coding Challenge/SUBMISSION.md`, separate from the code.
2. **[Claude]** Put the changes on a new branch and open a pull request.
3. **[You]** Merge the pull request into `main`. Vercel publishes the new version.
4. **[You]** Open the live app and check that it still works.
5. **[You]** Email mdenner@techfleet.org with the Submission Template and three links: the repository, the live Vercel app, and the database diagram.

## Extra, only if you choose it (course "Advanced homework")
Test the app with 1 to 2 real people while they think aloud. Write a results report with the Usability Test Results and Analysis Template. Turn what you learn into new requirements, build a new version, and launch it. **Tell me if you want this. It is not required for the basic homework.**

## Parked until Week 4 is done
The Premium research paper, repository cleanup, and all later weeks.
