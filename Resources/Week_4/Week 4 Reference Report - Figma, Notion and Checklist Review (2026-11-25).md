# Week 4 Reference Report: what the course expects, and where we are (2026-11-25)

**Read this at the start of every Week 4 session**, together with the newest dog feeding report in `Resources/Week_4/Dog Feeding Reports/` and `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`.

Made by Claude on 2026-11-25 from the sources listed in section 1. Every fact names its source. Where I did not read something or am guessing, this report says so (section 9). **If this report and the course page ever disagree, the course page wins.**

## 0. The short version

- **What Week 4 is:** build and launch the whole MVP #1 of the caregiving coordinator as a three-tier web app. Screens: Next.js with Material UI. Server code: Vercel. Database and sign-in: Supabase. (Course page, "What are we doing?" and "Summary"; Premium objective.)
- **The owner's role (lecture):** the owner is the technical architect and makes each choice. Claude is the developer. (Lecture notes, "You and Claude are the Head Chefs.")
- **The order of work is the 14-step Build and Launch Checklist.** The Figma board, the Notion lecture notes and the owner's steps page all list the same 14 steps in the same order.
- **Where we are (2026-11-25):** checklist steps 2 and 3 are done. Step 1 is done except possibly the Vercel account (see section 2). Step 4, making the Next.js app, has not started. All of Part A (GitHub) of the "How to Set Up GitHub and Vercel" guide is done.
- **The Vercel import belongs at checklist step 11**, after the app and database exist. Do not deploy before then.

## 1. Sources read, and how much of each

| Source | Where | What I read |
|---|---|---|
| Figma board, Week 4 section ("Section 35", node 3089:14568) | https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/Orlandos-AI-Dev-Residency-Work?node-id=3089-14568 | All 2,738 lines of text and structure returned by the Figma tool. **No pictures viewed.** |
| Notion: Week 4 - Web Coding Lecture Notes | https://app.notion.com/p/7eb9219a469182888be281b0505f49c8 (page last edited 2026-11-13) | All 2,387 lines of text, start to finish. **No pictures viewed** (about 25 `wk4-*.png` files). Local copy: `Resources/Week_4/Week 4 - Web Coding Lecture Notes (Notion copy 2026-11-13).md` (2,399 lines, not compared line by line). |
| Notion: Build and Launch Checklist | https://app.notion.com/p/7b19219a469183899c040148cd01d130 | All of it, plus the local copy. |
| Notion: Week 4 Coding Challenge (course page) | https://app.notion.com/p/1169219a469182f2991f8174d94f2e4a | All of it, plus the local copy. |
| Notion: How to Set Up GitHub and Vercel | https://app.notion.com/p/c239219a46918329916781bb84cafff4 | All of it, plus the local copy. No comments on the page. |
| Owner's steps page | `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md` | All 62 lines. |
| NotebookLM answer pasted by the owner | chat, 2026-11-25 | Read in full and checked against the files above (section 7). |

The Notion lecture notes say they are a word-for-word copy of the Figma board's Week 4 row (line 9 of the local copy). They agree with the Figma on everything I compared, and the Notion page has a few sections the Figma text lacked (section 6).

## 2. Where we are (as of 2026-11-25)

| Item | Status | Source |
|---|---|---|
| App repository | `LDoomD/Week_4_Caregiving-Coordinator`, private, cloned to `/Users/landodoom/Desktop/Week_4_Caregiving-Coordinator`. | `gh pr list`, `git status` on 2026-11-25 |
| Starting layout (72 files: README, CLAUDE.md, .gitignore, `.claude/` with 14 skills and hooks, 2 arch-gate files, `docs/risk-profile.md`, 12 spec copies in `docs/specs/`) | **Approved** by the owner ("I think the layout of the GitHub looks fine ... I already confirmed it"). Merged as pull request 1 on 2026-11-19. | chat 2026-11-25; `git ls-tree origin/main` |
| GitHub Actions check | **Done.** Pull request 2 added `.github/workflows/ci.yml` (runs the architecture gate and the 21 hook and gate tests on every pull request into `main` and every push to `main`). Merged 2026-11-25 20:25 UTC. The check, named `checks`, passed on the pull request and on `main`. | `gh run list` |
| Branch protection on `main` | **Done.** GitHub accepted: the check `checks` must pass before merging. Strict mode off, enforce for admins off, force pushes off, deletions off. The owner's GitHub plan was never found; GitHub accepted the rule anyway. Not tested with a failing check. | `gh api` answer, 2026-11-25 |
| Checklist step 1, accounts | **Supabase:** owner said "Done." **Vercel:** the owner reached Vercel's import screen and chose the Next.js preset, so an account exists. I do not know if a half-finished Vercel project was saved. The owner was told not to click Deploy. | chat 2026-11-25 |
| Checklist step 2, Node.js | **Done.** `node --version` printed v26.4.0, `npm --version` printed 11.17.0. | command output 2026-11-25 |
| Checklist step 3, saved documents | **Done.** The 13 files were listed to the owner. They are in the app repository (`docs/specs/` and `docs/risk-profile.md`). | chat 2026-11-25 |
| Checklist step 4, the Next.js app with Material UI | **Not started.** | |
| Local app folder | After pull request 2 was merged, I did not switch the local app folder back to `main`. It was on branch `add-ci-checks`. **Check with `git status` and run `git switch main` and `git pull --ff-only` first.** | I did not check after the merge |
| Deadline | The course page says due Nov 16. **The owner said there is no deadline for them.** Treat as settled; do not raise it. | course page line 20; chat 2026-11-25 |
| Course repository | Has uncommitted changes that are not from this Week 4 work (`caregiving-coordinator/docs/sources/INDEX.md` modified, and an untracked folder `immigrant-data-security-2026-11-20/`). The owner did not recognize it as part of this project. I did not open them. Leave alone. | `git status` at session start |

## 3. What the course page requires (the rubric)

Source: course page (`Week 4 Coding Challenge - Code and Launch a Web App (Notion copy 2026-11-13).md`) and the Notion version, read 2026-11-25.

**Basic homework (all 15):**
1. The entire MVP #1 is built and fully working. Every epic, feature and task in the Week 2 MVP #1 scope works in the live app.
2. Every screen, button, link and form works. Nothing fake, empty or "coming soon." No errors shown.
3. A working Supabase database. The live app saves and reads information. Log out, log in, and it is still there.
4. Every MVP #1 ticket on the Backlog Kanban Board is Done.
5. A Next.js app that uses Material UI, saved in the GitHub repository.
6. The Material UI design system is implemented.
7. People can sign up and log in.
8. Every feature saves its information to Supabase and shows it again.
9. Each person sees only their own information.
10. At least three ADRs in `docs/adr`: Next.js with Material UI, Vercel, Supabase.
11. A new ADR for every other big choice made while building.
12. A database diagram.
13. The app is live on Vercel.
14. Published at a free `your-app.vercel.app` address. No domain purchase needed.
15. A filled-out Submission Template.

**Advanced homework (optional, only if the owner chooses it):** test with 1 to 2 real people thinking aloud (Usability Test Plan and Script Template), write a research report (Usability Test Results and Analysis Template), write new user and technical requirements, feed them to Claude, code a new version, launch it.

**Deliverables:** (1) the GitHub repository with code, ADRs in `docs/adr` and migration files; (2) the Vercel link with the whole MVP #1 working; (3) the database diagram, saved in the repository's `docs` folder; (4) the Submission Template, saved in the repository and sent by email.

**Requirements (10):** build MVP #1 one feature at a time; move tickets on the Backlog Kanban Board (In Progress when started, Done when working on the live app); build in the Week 2 repository; write an ADR for each big decision; design tables with the Database Design Template, make them in Supabase, and save the SQL as a migration file; turn on Row Level Security for every table; keep secret keys out of GitHub (Keep Your App Safe Checklist) and use fake data; use Material UI; host on Vercel; fill out the Submission Template **with no AI**.

**To submit (in order):** (1) save the Submission Template as `Week 4 Coding Challenge/SUBMISSION.md`, separate from the code; (2) ask Claude to put changes on a new branch and open a pull request; (3) merge into `main` so Vercel publishes; (4) open the live app and check it; (5) email mdenner@techfleet.org with the template and three links: the repository, the live Vercel app, the database diagram.

**Submission Template:** Links (repo, Vercel app, database diagram); Documents (Notion and other links); **What I Did** (at least 2 paragraphs, full technical detail); **What I Learned** (at least 2 paragraphs, including what to do differently and how it helps in team work). The course says "DO NOT use AI for this! I will check!" **Claude never writes or edits those two sections.**

**Before you submit, check:** the Vercel link works in a private window and you can sign up as a new person; every MVP #1 feature works on the live app; click every screen, button, link and form; add something, log out, log in, find it again, then find the new row in Supabase's Table Editor; if the app stopped, open Supabase and click "Resume project" (free projects pause after 7 days of low activity); no secret keys in the repository.

**Templates on the course page:** Build and Launch Checklist, ADR Template, Database Design Template, Keep Your App Safe Checklist, Submission Template, and (Advanced) the two usability templates. Copies are in `Resources/Week_4/`. **I have not re-read the ADR Template, Database Design Template, Keep Your App Safe Checklist or Supabase migration guide in this review.**

**Getting help:** Fleety (the Tech Fleet helper bot), the working sessions, and, if the Vercel build fails, copy the build log to Claude and ask it to explain the problem before fixing it.

## 4. The 14-step order, with our status

Source: Build and Launch Checklist (Notion, read 2026-11-25), Figma block "In This Class, This Is How You Launch," lecture notes "How to Launch."

| Step | What it is | Status |
|---|---|---|
| 1 | Free Vercel and Supabase accounts, signed up with GitHub, free plan | See section 2 |
| 2 | Check Node.js | Done |
| 3 | Gather saved Week 2 documents (vision, scope, requirements, build plan) | Done |
| 4 | Make a new Next.js app with Material UI in the Week 2 repository and push the first version | **Next** |
| 5 | Architect the app: plan the screens (tier 1), server code (tier 2), database (tier 3). Save the plan in the repository before any code | Later |
| 6 | Write ADRs: make `docs/adr`, add the ADR line to `CLAUDE.md`, one ADR per big choice (at least Next.js with Material UI, Vercel, Supabase) | Later |
| 7 | Design the database tables (Database Design Template). Save as a migration file. Turn on access rules for every table | Later |
| 8 | Connect the app to Supabase: make the Supabase project, run the SQL (paste in the SQL Editor, or connect Claude Code and ask it to show changes first), save migrations, keys in `.env.local` | Later |
| 9 | Build one feature at a time. Start with sign-up and log-in. New big choice means a new ADR first | Later |
| 10 | Run and test on the computer. Two test accounts. One person must not see the other's information | Later |
| 11 | Connect the GitHub repository to Vercel (import it) and add the Supabase keys in Vercel's environment variables | Later |
| 12 | Push to `main`; Vercel publishes. If the build fails, give Claude the build log | Later |
| 13 | Test the live app: private window, new sign-up, every MVP #1 feature, phone | Later |
| 14 | Claude saves what was built and decided in the repository. **The owner fills in the Submission Template alone, no AI** | Later |

Tickets (all along): on the Week 2 Backlog Kanban Board move a ticket to In Progress when started and Done when it works on the live app. Finished when every MVP #1 ticket is Done.

**Two numbering systems cause confusion.** The How-To guide has its own Part A (GitHub, steps 1 to 5) and Part B (Vercel, steps 6 to 10). The checklist has 14 steps. Always say which list a step number belongs to.

## 5. The lecture, in detail

Source: Notion lecture notes (all lines) and the Figma board. Paraphrased; read the originals for exact wording.

### 5.1 Roles and the restaurant metaphor
- Raw ingredients = the programming languages (SQL, JavaScript, HTML, CSS, PHP, Python, design components, flow charts, requirements). Mixed ingredients = software patterns. Type of meal = data architecture. Head chef = technical architect. Restaurant owner = product manager. Line chefs = developer and UX designer. Restaurant manager = product owner. Ovens = database server and web server. Delivery van = the HTTP request and response. The cake = the finished user experience, which is the presentation layer.
- **In this class:** the owner is the technical architect, Claude is the developer. Both wear the architect hat, only Claude wears the developer hat. Duties and Milestones are explained in Tech Fleet's Skills and Practices Framework; Fleety (techfleet.network/tal-9000) knows that data and Claude does not.
- The technical architect decides: servers and dev tools; languages (for speed, performance, security); how to design code for speed and security; how many developers work on the same code safely; the standards for QA, coding and security.
- **Enterprise ready** means four promises: reliable, scalable, maintainable, secure. They are planned from day one.
- Week focus (green circles): Development Operations, Network Technology, Technical Architecture, Development.

### 5.2 Idea to ship (7 steps)
1 Build specs (functional and non-functional requirements). 2 Decide the technical architecture. 3 Document it in ADRs. 4 Set up the database server. 5 Code. 6 Push code and database changes to the servers. 7 Ship at a web address.

### 5.3 The Language of Change applied to architecture (9 steps)
1 What is happening now that needs to change (problem scenarios; produce problem statements). 2 Expected outcomes (goals and needs, including speed, privacy, many users, change). 3 How we will know we succeeded (success measurements). 4 Choose software patterns (ADR for each). 5 Architect the domain layer (ADR). 6 Architect the data source layer (ADR). 7 Architect the presentation layer (ADR). 8 Architect the network (ADR). 9 Plan for real use and write down why (save all ADRs in `docs/adr`).
- Step 4 helpers: one job with many ways to do it, use Strategy; talking to an outside service, use Adapter; something that moves through stages, use State Machine. Choose the simplest fit, or no pattern on purpose.
- Step 5: simple rules, Transaction Scripts; in-between rules on table-based tools, Table Modules; complex or growing rules, Domain Model. Add a thin Service Layer only if needed.
- Step 6 matches step 5: Transaction Scripts with Gateways; Table Modules with Table Data Gateway; simple Domain Model with Active Record; complex Domain Model with Data Mapper.
- Step 7: keep business rules out of screens, build for speed, never let a screen talk to the database directly.
- Step 8: the screens run in the browser, the server code on Vercel, the database on Supabase. Draw how a request travels. Use HTTPS. Keep secret keys on the server. Put server and database in the same region. Decide timeouts and failure handling. Produce a diagram and an ADR.
- Step 9: decide what happens when two people edit the same thing; keep the app in one place unless forced to split; treat each decision as an assumption and test the riskiest first; one decision per ADR; when a decision changes, write a new ADR and never erase the old one.

### 5.4 Layers
Presentation (what people see; UI, styles, brand, front-end code, pictures), Service (one front door per action, API routes, checks who is asking, saves every step or none), Domain (business rules), Data source (reads and writes the database), and the Database itself (tables, records, keys, access rules). Golden rule: the domain and data layers never depend on the presentation layer. Test: if you would have to copy a rule to add a phone app, the rule is in the wrong layer. A layer is code organization, not a machine; a tier is usually a machine. Five DON'Ts: rules in screens; rules or data depending on screens; more servers than needed; the same rule in two places; the screen talking to the database directly.

### 5.5 Software patterns (15 cards)
Core (1 to 7): Monolith, Modular Monolith, Microservices, Event-Driven, Serverless (the note says "close to our budgeting app on Vercel"), Layered, Hexagonal. Advanced (8 on): SOA, CQRS, Event Sourcing, Domain-Driven Design, Space-Based, Pipeline, Microkernel, Cell-Based. Each card has: the problem, when to use, the risks, and a real example. Fowler's lessons: write down the why; the data is what makes enterprise software hard; split into layers; protect the business rules; architecture is the hard-to-change decisions; every choice is a trade-off; start simple and earn complexity; do not distribute objects; measure, do not guess; guard shared data from day one.

### 5.6 Business logic: three approaches
Transaction Script (one procedure per action; fastest; rules get copied and drift), Table Module (one piece of code per table; fits table-based tools; falls back to if-this-then-that), Domain Model (objects with their own rules; grows by adding pieces; takes months to feel natural). Start simple. Moving from Transaction Script to Domain Model later is painful; going the other way is rarely worth it. All examples in the notes use the ADHD budgeting app, not the caregiving app.

### 5.7 ADRs
One short file per big decision, in `docs/adr`, numbered like `0001-use-nextjs-with-material-ui.md`. Parts: title; date and status (Proposed, Accepted, Deprecated, Superseded); context (facts, not opinions); options with good and bad parts; decision (starts "We will"); consequences (good and bad). Never erase an old ADR; write a new one that replaces it and mark the old one "replaced by." Do not keep the only copy in a chat, Notion, Google Docs, FigJam or only on a computer. **Add to `CLAUDE.md`:** "Read every ADR in docs/adr before making changes, and write a new ADR for every big decision." The example ADR notes that Material UI's theme file needs a "use client" line at the top.

### 5.8 Design system (Material UI)
Free, open-source React component library following Material Design 2, 40+ components. One theme file holds colors, fonts and spacing (made with `createTheme`, wrapped with `ThemeProvider`). Breakpoints xs, sm, md, lg, xl. One spacing step is 8 pixels. Prompts to give Claude: set up Material UI in the Next.js app with a theme file; put brand colors and fonts in the theme; use Material UI components instead of building from scratch; ask "Does this use the theme, or did you type a color straight into the code?"; write an ADR for design system choices.

### 5.9 Platforms and tiers
Web, progressive web, desktop, native mobile and Internet of Things apps. This class builds a web app. The server code and database can serve every type later. Material UI pages resize for a phone browser.

### 5.10 How the web works (8 steps)
Type the address; the browser sends an HTTP request; DNS finds the server and the request hops across the internet; it reaches the web server (on Vercel) that holds the files; the web server sends a SQL query to the database server (on Supabase); the database replies with a payload; the web server replies with an HTTP response; the browser loads the files. Two-tier means the client talks straight to the database; three-tier means only the web server does. This app is three-tier.

### 5.11 Your computer, preview and live
Local at `http://localhost:3000` (only you); preview link on Vercel for any branch other than `main` or any pull request (Vercel may ask visitors to log in); live at the main address after a merge into `main` (the link you submit). All three use the same Supabase database if they use the same keys, so test data on the computer also shows on the live app. Use fake data only. Bigger teams use a second Supabase project for testing.

### 5.12 Servers
A web server is always on, holds the files, runs server code, and keeps secret keys out of browsers. A database server stores tables and checks access rules. Vercel runs the web server; Supabase runs the database and handles accounts and sign-in. Hosting with a provider is the least effort and least cost; self-hosting means you maintain everything. Neither is secure or private by default.

### 5.13 Launch step 8 in detail (Supabase)
A migration is a SQL file that makes one change. File names have a number or date so they run in order. To change the database later, add a new migration; never edit one that already ran. Make every database call from server code, never the browser, and keep access rules on as a second lock. Keys go in a local environment file, never in code or GitHub. (The saved Supabase guide `How to Run Your First Supabase Migration (Notion copy 2026-11-13).md` says the migration file is usually in a folder like `supabase/migrations`; I did not re-read it in full.)

### 5.14 When something breaks
Find the exact error message and give it to Claude; copy it, do not retype it. Say what you did, what you expected, what happened, and where. Browser: F12 (Windows) or Cmd + Option + I (Mac); Console for errors; Network for requests; 401 not logged in, 403 not allowed, 404 not found, 500s mean server code broke; try a private window. Vercel: Deployments, build log, Logs page (kept only 1 hour on the free plan), Settings then Environment Variables (every `.env.local` key must be there; redeploy after a change). Supabase: Table Editor, Authentication, Logs; an access rule can hide rows with no error; "Resume project" if paused.

### 5.15 Dogfooding (how to work with Claude)
Claude forgets other chats, so save every approved result as a markdown file and give saved documents to each new chat. Ask Claude to read everything first. Work one part at a time. Ask where each answer came from. Check for mistakes. Ask Claude to teach when stuck. Save each approved result as a new document and repeat.

## 6. What the Notion lecture notes have that the Figma text lacked

- The "Your Computer, Preview, and Live" section (5.11).
- The full body of launch step 8 on Supabase and migrations (5.13). The Figma frame showed only its title.
- Notion labels the wait staff as the Business Analyst and the delivery van as the HTTP request and response. The Figma text labeled the wait staff as "The HTTP Requests and Responses." Small mismatch between the two copies.

## 7. Differences and conflicts to remember

1. **New repository vs the Week 2 repository.** Figma launch step 4, the lecture notes and the Figma "Deliverables for Code and Launch" all say "new GitHub repository." The course page says to use the Week 2 repository and not make a new one ("Before You Start" item 2). **Decision: follow the course page and the owner. The app lives in `Week_4_Caregiving-Coordinator`.**
2. **The old name.** The steps page line 11 still names `LDoomD/Week-3---Caregiving-Coordinator`. The repository is now `Week_4_Caregiving-Coordinator` (the owner confirmed). The steps page is out of date on that line (not yet fixed).
3. **Public or private.** The steps page line 12 says the course says the repository is public. I searched the three Week 4 course files for "public" and found no such statement. The How-To says to choose Public or Private. The app repository is private.
4. **"Week 3" labels.** The lecture notes call the section "Week 3" and label some deliverables "(Week 3)." The course page (line 7) explains the course renumbered the weeks. These notes are for the current Week 4.
5. **Deliverables on the Figma that are not on the course page.** The Figma lists "Software layer design" and "Software pattern design" under Architecture. The course page and checklist do not list them by those names. The 9-step architecture method in 5.3 is where they would come from.
6. **The 3 ADRs.** The steps page names three required ADRs. The lecture's 9-step method creates more. The course page says "at least three" plus an ADR for every other big choice.
7. **NotebookLM's answer (pasted 2026-11-25).** Its 7-step roadmap, its Week 3 title, and its `CLAUDE.md` ADR line match the lecture notes. Its "Claude 4.8, Medium effort" tip is not in the lecture notes I read (the source is unknown). Its "Week 5 chatbot" claim was not checked. It told the owner to make a new public repository, which conflicts with item 1 above. It leaves out the Database Design Template, the Keep Your App Safe Checklist, Kanban ticket moving and the pull request steps. **Use the course page and checklist, not NotebookLM, as the source.**
8. **Vercel guide order.** The How-To's step 6 says to import the repo right after signing in. The checklist and the Figma put the import at step 11. The guide assumes an app and a database already exist (its step 8 asks for database keys before the first deploy). **Decision: import at checklist step 11.**

## 8. Decisions and open items

**Approved by the owner (settled; do not reopen):**
- The app repository and its starting layout (merged pull request 1).
- No deadline pressure for Week 4 ("There's no deadline. We just have to start week four").
- Do GitHub Part A steps 4 and 5 (done; the owner said these are part of the homework).
- Follow the Notion checklist as the order of work.

**Open (Proposed, not decided):**
- **Where the Next.js app goes.** My proposal: the top level of the repository (matches Vercel's Root Directory `./`), with no `src/` folder. The Next.js doc saved at `caregiving-coordinator/docs/sources/week-4-repo-setup-2026-11-19/nextjs-project-structure.md` says `src/` is optional and to pick a layout and stay consistent. The Figma and lecture notes give no folder layout.
- **How big step 5 is.** The lecture's 9-step method suggests several ADRs. The owner decides how much to cover.
- **Business-logic approach** (Transaction Script, Table Module or Domain Model) for the caregiving app: decide at checklist step 5.
- **Add the ADR line to the app's `CLAUDE.md`:** planned for checklist step 6, with the owner's yes.
- **Fix steps page line 11** (old repository name): waiting for the owner's yes.
- **Whether to do the Advanced homework:** the owner has not asked.

## 9. Not read, not verified

- Pictures in the Notion lecture notes and the Figma board (not viewed).
- Other parts of the Figma file outside node 3089:14568.
- The ADR Template, Database Design Template, Keep Your App Safe Checklist, Submission Template, usability templates, "Week 4 - Web Hosting - Weekly Class Materials," the recordings page and the "WEEK 4 Example" pages in `Resources/Week_4/` (not re-read in this review).
- Whether Vercel kept a half-finished project, whether Vercel's free plan accepts a deploy from a private repository, and whether commits must match the Vercel account's email (research file `vercel-troubleshoot-collab.txt` says the commit author must be the Hobby team owner, matched by email; not tested).
- Whether GitHub Actions is free for this private repository (not found in the saved research).
- The local app folder's current branch after the pull request 2 merge.
- The NotebookLM sources.

## 10. Working rules for Week 4 sessions

Full rules are in `caregiving-coordinator/CLAUDE.md` and the app repository's `CLAUDE.md`.
- **Never make anything up.** Name the file or command behind every fact. If not found, say "I did not find this" or "I am guessing."
- **One step at a time.** Do only the step asked, then stop and wait. The owner makes each choice. Questions get answers, not edits.
- **Say what each step number belongs to** (checklist, How-To part, or steps page).
- **Every task gets a new branch and a pull request.** The owner merges. Claude never runs `gh pr merge` and never commits to `main`.
- **Plain words, complete sentences, short replies.** Explain every folder or term the first time. Say real repository names.
- **Ask before** Firecrawl, Chrome or the browser pane, before changing GitHub settings, and before creating files or branches the owner did not ask for.
- **The owner writes "What I Did" and "What I Learned."** Claude never writes or edits them.
- **Fake data only. No secret keys in the repository.**
