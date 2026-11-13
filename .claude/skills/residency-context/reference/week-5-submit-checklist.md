# Submit checklist for week-5: word-for-word extract

> **How this file was made (2026-11-13):** a script copied the sections below, unchanged, from `week-5.md` (the challenge page). Nothing was rewritten or shortened. It is a shortcut for "what do I build and what do I submit?"
> **If a question touches anything that is not in this file, read the full `week-5.md` first.** Sections copied: How to Submit, Standard Residency Objective, Premium Residency Objective, Before You Start, BASIC HOMEWORK, Deliverables, Requirements, To Submit, Links, Documents, What I Did, What I Learned, Before You Submit, Check These.

---

# How to Submit

Email your teacher the Submission Template with your links filled in to [mdenner@techfleet.org](mailto:mdenner@techfleet.org)

**Due date:** Nov 23

# Standard Residency Objective

Set up a CI/CD pipeline on GitHub Actions for the ADHD Budgeting App you built in Week 4. The automatic checks come from your own MVP requirements, built from the use cases and BDD scenarios you wrote. Gate-check the Claude Skills you made in Week 1 so they run on every push. Then write two test case scenarios and run them by hand on your live app.

# Premium Residency Objective

You are not working on the ADHD budgeting app, you are working on the app you chose based on your specialization. Do the same work on that app: set up the CI/CD pipeline on GitHub Actions, gate-check your Week 1 Claude Skills, and write and run two manual test case scenarios, all based on your own MVP requirements.

# Before You Start

1. Your app from Week 4 is built and live on Vercel, in the GitHub repository you have been using. You will add the pipeline to this same repository.
2. Your MVP requirements from Week 2 are ready, including your use cases and BDD scenarios. You need them to decide what the automatic checks should test.
3. The Claude Skills you made in Week 1 are ready. You will gate-check these on every push.
4. Claude Code and GitHub work on your computer. You set these up in Week 1.

# BASIC HOMEWORK

Every student sets up CI/CD and runs manual QA on the app they already built. The pipeline must really run on every push, and a check that should fail must actually fail.

1. A CI/CD pipeline on GitHub Actions in your repository, that runs automatically on every code push.
2. The automatic checks come from your own MVP requirements, built from the use cases and BDD scenarios you wrote.
3. The Claude Skills you made in Week 1 are gate-checked on every push, so a push that breaks them does not pass.
4. Two test case scenarios, written and run by hand on your live app, with the results written down: pre-conditions, steps to follow, expected results, and what actually happened.
5. You do not need branch protection, because you are on GitHub's free plan.
6. A filled-out Submission Template.

# Deliverables

1. Your GitHub repository, with the CI/CD pipeline (the GitHub Actions workflow) and the checks that run on every push.
2. Your two test case scenarios and their written-down results.
3. Your Submission Template, saved in your repository and sent in your email.

# Requirements

Work with Claude. Follow the How to Create a CI / CD Pipeline on GitHub guide.

1. Take the use cases and BDD scenarios from your Week 2 MVP requirements, and decide what the automatic checks should test.
2. Set up a CI/CD pipeline on GitHub Actions. Make the checks run on every push.
3. Gate-check the Claude Skills you made in Week 1, so they run on every push and a push that breaks them does not pass.
4. Write two test case scenarios for your app. Run them by hand on your live app, and write down the results: pre-conditions, steps to follow, expected results, and what actually happened.
5. You do not need to turn on branch protection, because you are on GitHub's free plan.
6. Fill out the Submission Template **(NOT USING AI)**.

# To Submit

1. Save the Submission Template in your repository as `Week 5 Coding Challenge/SUBMISSION.md`. Keep it separate from your code.
2. Ask Claude to put your changes on a new branch, and open a pull request on GitHub.
3. Merge the pull request into the main branch.
4. Open your live app and check that it still works.
5. Email [mdenner@techfleet.org](mailto:mdenner@techfleet.org) with the Submission Template. Include:

   1. The link to your GitHub repository

**Expand for Submission Template**

### Links

1. Drop your link to the Github Repository here
2. Drop your link to your hosted Vercel app here
3. Drop your link to your database diagram here

### Documents

1. Drop any Notion Document links here
2. Drop any other document links here

### What I Did

Write what you did in no less than 2 paragraphs. Provide full technical detail so that anyone reading it can understand what exactly you did. DO NOT use AI for this! I will check!

### What I Learned

Write what you learned in no less than 2 paragraphs. Describe the full details of what you learned, what you will do differently next time, and how the lessons from this exercise will help you in project team work in the future. DO NOT use AI for this! I will check!

# Before You Submit, Check These

- [ ] Push a change to your repository and watch the checks run on GitHub Actions.
- [ ] Break something on purpose, push it, and confirm the pipeline catches it. A check that should fail does fail.
- [ ] You have at least 3 new CI checks on your Github repository that holds the application code.
- [ ] The Claude Skills you made in Week 1 are checked on every push.
- [ ] You ran both test case scenarios by hand on your live app and wrote down the results.
- [ ] Your live app still works after your changes.
