# Build and Launch Checklist
- Source copy: https://app.notion.com/p/7b19219a469183899c040148cd01d130
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:24.246Z
- Not saved: none

---

> 📍 These are the same 14 steps from the lecture board section "In This Class, This Is How You Launch." Check off each step as you finish it.

# Set up your accounts and tools

- [ ] **1. Make your free Vercel and Supabase accounts.** Sign up for each one with your GitHub account. Pick the free plan on each one. You already set up Claude Code and GitHub in Week 1.
- [ ] **2. Check that your computer is ready.** Open Claude Code in the folder for this project. Ask Claude: "Check that Node.js is installed. If it is not, help me install it, and explain what it does."
- [ ] **3. Gather your saved documents.** Get your vision, scope, requirements, and build plan from Week 2. You will give these to Claude at the start of every new chat.

# Build the app on your computer

- [ ] **4. Make the project.** Ask Claude to make a new Next.js app that uses Material UI. Put it in the GitHub repository you made in Week 2, called "Week 3 - ADHD Budgeting App." Push the first version.
- [ ] **5. Architect the app.** Plan the screens (tier 1), the server code (tier 2), and the database (tier 3). Ask Claude to write the plan in a document and save it in your repository before you write any code.
- [ ] **6. Write down your big decisions as ADRs.** Use the Architecture Decision Record Template. Make a folder called `docs/adr`. Write one ADR for each big choice, like Next.js with Material UI, Vercel, and Supabase.
- [ ] **7. Design your database tables.** Use the Database Design Template. Ask Claude to save the tables as a migration file and to turn on access rules for every table.
- [ ] **8. Connect the app to Supabase.** Make a new project on the Supabase website. Pick the free plan. Run the SQL one of two ways:
  - Way 1: Copy the SQL from Claude. Paste it into the SQL Editor in Supabase, and click Run.
  - Way 2: Connect Claude Code to your Supabase project. Ask Claude to show you what it will change before it runs anything.
  - Either way, save the SQL as a migration file in your repository.
  - Put your Supabase keys in a file called `.env.local`. Use the Keep Your App Safe Checklist.
- [ ] **9. Build one feature at a time.** Start with sign-up and log-in. Then build the next feature in your build plan. Keep going until every feature in your MVP #1 scope is built. If you make a new big choice, write a new ADR first.
- [ ] **10. Run and test the app on your computer.** Click through every screen. Make two test accounts. Check that one person cannot see the other person's information.

# Launch it on the internet

- [ ] **11. Connect your GitHub repository to Vercel.** In Vercel, import your repository. Add your Supabase keys in Vercel's environment variable settings.
- [ ] **12. Push your code and let Vercel publish it.** Each push to the main branch puts a new version of your app online. If the build fails, copy the build log and give it to Claude.
- [ ] **13. Test the live app.** Open your Vercel web address. Sign up as a new person and test every MVP #1 feature against your Week 2 epics, features, and tasks. Open it on your phone too.
- [ ] **14. Save what you learned.** Ask Claude to write down what you built and what you decided. Save it in your repository. Then fill out the Submission Template yourself, without AI.

# Move your tickets as you work

- [ ] Open the Backlog Kanban Board you made in Week 2.
- [ ] When you start a ticket, move it to In Progress.
- [ ] When the feature works on your live app, move it to Done.
- [ ] You are finished when every MVP #1 ticket is in Done.
