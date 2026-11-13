# Week 5 Coding Challenge - Build a CI / CD Pipeline
- Source copy: https://app.notion.com/p/6099219a469183b091870125db5a712c
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:10.294Z
- Not saved: none (child pages saved as separate files: How to Create a CI / CD Pipeline on GitHub; Test Case Scenario Template)

---

# How to Submit

Email your teacher the Submission Template with your links filled in to [mdenner@techfleet.org](mailto:mdenner@techfleet.org)

**Due date:** Nov 23

# What are we doing?

This week you are going to add quality assurance to the app you built and launched in Week 4. You will set up a CI/CD pipeline on GitHub so that automatic checks run every time you push code, and you will run a short round of manual testing on your live app. Every student does this on the app they already built.

# Summary

In Week 4 you built and launched your app. Now you make sure it keeps working as you keep changing it. You will turn the use cases and BDD scenarios from your MVP requirements into automatic checks that run on GitHub Actions on every push. You will also gate-check the Claude Skills you made in Week 1, so a push that breaks them does not pass. On top of the automatic checks, you will write two test case scenarios and run them by hand on your live app, and write down the results. You are on the free plan, so you do not need branch protection.

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

# Deliverables Templates

Test Case Scenario Template

# Tools

1. GitHub
2. GitHub Actions
3. Claude Code

# How To's

How to Create a CI / CD Pipeline on GitHub

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

# Lecture Resources

These sections on the [Week 5 lecture board](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions) show you how to do this homework:

1. [CI / CD](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3642-12561)
2. [DevOps for Product Teams](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3611-10597)
3. [Anatomy of a Test Case](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3604-9982)
4. [How Do Requirements Affect the Success of Quality Assurance?](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3604-9428)
5. [Types of QA Testing](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3582-6147)

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

# Getting Help

1. Ask Claude to break it down in the way you need.
2. Bring your questions to the working sessions this week.
3. If a GitHub Actions check fails, open the run log and give it to Claude Code. Ask it to explain the problem before it fixes it.
