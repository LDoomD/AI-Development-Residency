# MY STEPS - Week 5: Build a CI/CD pipeline

- Made by Claude on 2026-11-18 from the course page copied on 2026-11-13. **If this page and the course page disagree, the course page wins.** The course page is `Week 5 Coding Challenge - Build a CI - CD Pipeline (Notion copy 2026-11-13).md` in this folder.
- Course due date: **Nov 23**. Do not start this week until Week 4 is submitted.
- Premium track: you do this on **your own app**, using your own MVP requirements.
- **Stay on track rule:** if a task is not on this page, it is not Week 5. Claude says so and asks before starting it.

**[Claude]** = Claude does it. **[You]** = only you can do it. **[Both]** = Claude does it, you check it.

## Before you start (all must be true)
- [ ] Your Week 4 app is built and live on Vercel, in the repository you use.
- [ ] Your Week 2 MVP requirements are ready, with your use cases and BDD scenarios.
- [ ] Your Week 1 Claude Skills are ready. **They must be in the same repository as the app code**, because the pipeline checks them on every push. The app repository is `Week-3---Caregiving-Coordinator` (decided 2026-11-18), so **[Claude]** copies the skills over from `AI-Development-Residency`. Claude keeps them well organized (one folder per skill with a `SKILL.md`), follows best practices for the folder layout, and shows you the layout before pushing.

## Steps
- [ ] **1. [Both]** Pick what the automatic checks should test, using your use cases and BDD scenarios.
- [ ] **2. [Claude]** Set up a pipeline on GitHub Actions that runs on every push. You need **at least 3 new checks**.
- [ ] **3. [Claude]** Check your Week 1 skills on every push, so a push that breaks them does not pass.
- [ ] **4. [Both]** Claude writes two test case scenarios. **You run them by hand on your live app** and write down: the starting conditions, the steps, what you expected, and what actually happened.
- [ ] **5.** You do **not** need branch protection, because you are on GitHub's free plan.
- [ ] **6. [You]** Fill in the Submission Template yourself. No AI.

## Before you submit (all must be true)
- [ ] You pushed a change and watched the checks run on GitHub Actions.
- [ ] You broke something on purpose, pushed it, and the pipeline caught it.
- [ ] There are at least 3 new CI checks in the repository that holds the app code.
- [ ] Your Week 1 skills are checked on every push.
- [ ] You ran both test case scenarios by hand and wrote down the results.
- [ ] Your live app still works after your changes.

## Submit (in this order)
1. **[Claude]** Save the Submission Template as `Week 5 Coding Challenge/SUBMISSION.md`, separate from the code.
2. **[Claude]** Put the changes on a new branch and open a pull request.
3. **[You]** Merge the pull request into `main`.
4. **[You]** Open the live app and check that it still works.
5. **[You]** Email mdenner@techfleet.org with the Submission Template and the link to your GitHub repository. The template also has spots for your live app link and your database diagram link.

## Parked until Week 5 is done
Everything not on this page.
