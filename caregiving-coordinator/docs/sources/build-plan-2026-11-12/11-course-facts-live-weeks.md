# Course facts used for the 8 build plan fixes (saved 2026-11-15)

Each quote below was copied word for word from a saved copy of the live course pages. The copies were read through the Notion connector on 2026-11-13. Line numbers are in the saved copy named next to each quote. The skill folder is `.claude/skills/residency-context/reference/` in the repository root (the folder above `caregiving-coordinator`). The "Keep Your App Safe Checklist" copy is in `Resources/Week_4/`.

## Fix 1: Week 4 builds the student's own app. The chatbot with OpenRouter is Week 7.
- `week-4.md` line 73, Premium Residency Objective: "You are not building an app for people with ADHD to budget, you are building the app you chose based on your specialization. Build that using these same tools and the product specifications you made."
- `week-4.md` line 1: "# Week 4: Code and Launch a Web App (host on Vercel and Supabase)". The Tools list (lines 122 to 127) names Claude Code, GitHub, Next.js, Material UI, Vercel and Supabase. It does not name OpenRouter.
- `week-7.md` line 1, a note written when the skill was rebuilt on 2026-11-13: "The live Week 7 page (read 2026-11-13) is this AI chatbot challenge: O*NET data, Vercel, Supabase, OpenRouter; Premium builds the same thing."
- Limit: the body text of `week-7.md` was not re-checked against the live page. Only the note on line 1 records the live Week 7 page.

## Fix 2: Week 4 uses free plans and fake data
- `week-4.md` lines 126 and 127, Tools: "5. [Vercel](https://vercel.com/) (free plan)" and "6. [Supabase](https://supabase.com/) (free plan)".
- `week-4.md` line 79, Before You Start: "You have free accounts on Vercel and Supabase."
- Pro pricing and the missing backups on Free are from Supabase pages already saved as sources 57 and 58 (see `INDEX.md`). They are not changed by this fix.

## Fix 3: The database diagram is a Week 4 deliverable, saved in `docs`
- `week-4.md` line 137, Deliverables: "3. Your database diagram, saved in the `docs` folder of your repository"
- `week-4.md` line 95, Basic Homework: "12. A database diagram"

## Fix 4: A new public repository for the app, empty until Week 4, then used in Week 4
- `week-2-3.md` line 125, requirement 5: "Create a new Github repository called “Week 3 - ADHD Budgeting App” under your own Github account. But DO NOT put any code in it yet. Make it public. This is the repo we will merge code into in the following weeks."
- `week-4.md` line 77, Before You Start: "You have the GitHub repository you made in Week 2, called "Week 3 - ADHD Budgeting App." Use this same repository. Do not make a new one."
- The course name is the ADHD budgeting example's name. That the owner picks the name for the caregiving app is from the owner's decision on 2026-11-12 (Premium track, "premium-track-own-app" memory). The name itself is still open.

## Fix 5: GitHub Actions is the course's choice for automatic checks
- `week-5.md` line 85: "1. A CI/CD pipeline on GitHub Actions in your repository, that runs automatically on every code push."
- `week-5.md` line 89: "5. You do not need branch protection, because you are on GitHub's free plan."
- `week-5.md` line 72, Premium objective: "Do the same work on that app: set up the CI/CD pipeline on GitHub Actions, gate-check your Week 1 Claude Skills, and write and run two manual test case scenarios, all based on your own MVP requirements."

## Fixes 6, 7 and 8: the Keep Your App Safe Checklist (`Resources/Week_4/Keep Your App Safe Checklist (Notion copy 2026-11-13).md`)
- Line 10: "> ⚠️ Your GitHub repository is public. Anyone on the internet can read every file in it. Check every item on this list before you push."
- Line 14: "- [ ] My Supabase keys are in a file called `.env.local`, not in my code."
- Line 15: "- [ ] My `.gitignore` file lists `.env.local`, so Git never uploads it."
- Line 18: "- [ ] If a secret key ever went to GitHub, I made a new key in Supabase right away. Deleting the file is not enough, because GitHub keeps the history."
- Lines 27 to 28, under "Use fake data only": "- [ ] I use made-up names, numbers, and money amounts when I test." and "- [ ] I never type my real bank or card information into my app."
- `week-4.md` line 149, requirement 7: "Keep your secret keys out of GitHub. Follow the Keep Your App Safe Checklist. Use fake data only."
