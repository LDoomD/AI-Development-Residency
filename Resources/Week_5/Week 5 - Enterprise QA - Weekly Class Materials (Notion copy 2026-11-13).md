# Week 5 - Enterprise QA - Weekly Class Materials
- Source copy: https://app.notion.com/p/6cb9219a4691834195d90192a069d6c8
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:09:49.287Z
- Not saved: Lecture Recording and Lecture Transcript are empty list items with no link on the page; external links (Figma, Notebook, GitHub) listed but not followed
- Note: "Text Lecture Content" links to page f869219a469183e08dba81f2cbafb799 (saved as separate file). The Homework mention points to page 55f9219a469183f1a0f30197877b06e7 (not fetched; the copy of the challenge is saved as its own file).

---

# Overview

Week 5 focuses on enterprise quality assurance: making sure the app does what it should, and does it well, for every user, before and after it goes live. You learn how to perform manual QA by hand, how to decide which types of tests to run, and how to set up automatic checks so that code which fails cannot reach your users. The class covers the types of QA testing and Martin Fowler's testing pyramid, how clear requirements such as acceptance criteria, use cases, and BDD scenarios are what make good QA possible, and how to turn those into test cases you can run and record. It also covers DevOps, where the people who build the app and the people who run it work as one team, and CI/CD, which is how teams get code from a developer's computer to real users safely and often. The goal is to build a CI/CD pipeline on GitHub for your app, with automatic checks that run on every push and stop code that fails, so quality is built into every step instead of being saved for the end.

# Objectives

1. Explain what quality assurance is, and why enterprise teams build quality in all the way through instead of testing only at the end.
2. Perform manual QA by hand, and decide which types of tests to run, such as unit, integration, browser, smoke, regression, and security, using the testing pyramid.
3. Turn requirements into QA by using acceptance criteria, use cases, and BDD scenarios to write test cases you can run and mark pass or fail.
4. Explain DevOps and CI/CD, and how code moves from a developer's computer to real users safely and often.
5. Build a CI/CD pipeline on GitHub Actions that runs automatic checks on every push and stops code that fails from being merged.

# Work You'll Do

1. Build CI checks on GitHub Actions for the ADHD budgeting app (or your specialization), based on your own MVP requirements:
   1. Turn the BDD scenarios and use cases you already wrote into automatic checks
   2. Set the checks to run on every code push
   3. Gate-check the Claude Skills you made in Week 1, so they run on every push too
   4. You do not need branch protection, because you are on GitHub's free plan
2. Write 2 test case scenarios and run them by hand on your live app, and record the results: pre-conditions, steps to follow, expected results, and what actually happened

# Estimated Workload

1. 5 hours in class
2. Core homework
   1. 3 hours in homework

# Class Lecture

1. [Text Lecture Content](/p/f869219a469183e08dba81f2cbafb799?pvs=25)
2. [FigJam Lecture Content](https://www.figma.com/board/mqryoCyR9mAw3v6kyDlmes/Fall-2026-AI-Development-Residency---Class-Lecture-an-Working-Sessions?node-id=3564-6526)
3. Lecture Recording
4. Lecture Transcript
5. [Lecture Slides](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/be074c92-9177-4a01-9253-c479589c58a3?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

# Class Learning Materials

1. [Gemini Notebook](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab)
2. [Week 5 Podcast](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/fa3174b8-c031-4f99-99ef-e13da941daa2?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)
3. [Week 5 quiz](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/9649ba91-99d8-452d-807c-d909a20a10fc?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)
4. [Week 5 flash cards](https://notebook.google.com/notebook/faa6414c-3395-4831-ba43-15ccc02da3ab/artifact/2e16d696-8fd2-41db-a8b7-a8b4eccd045b?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

# Examples

1. [https://github.com/techfleetworks/job-decoder](https://github.com/techfleetworks/job-decoder)

# Homework

Week 5 Coding Challenge - Build a CI / CD Pipeline

## What Does Good Homework Look Like?

1. Your repository has working CI checks on GitHub Actions that run automatically on every code push.
2. The CI checks come from your own MVP requirements, built from the BDD scenarios and use cases you wrote.
3. The Claude Skills you made in Week 1 are gate-checked on every push, so a push that breaks them does not pass.
4. You ran 2 test case scenarios by hand on your live app and wrote down the results, including pre-conditions, steps to follow, expected results, and what actually happened.
5. The student has written the submission summary about what they did and learned, without using AI, and has emailed the instructor the links to the GitHub repository, the live Vercel app, and the database diagram.
