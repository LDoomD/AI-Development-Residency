# Week 8: Integrate Apps Together (APIs and Agents)

> **Current copy of the challenge page: 2026-11-13** (read through the Notion connector 2026-11-17; this file written 2026-11-18). Live course week: **8**. Class: Dec 7. Due: **Dec 14**.
> **The Week 8 Lecture Notes and Weekly Class Materials pages were blank in the 2026-11-13 copy and have not been re-checked.** The child pages "Architectural Decision Records" and "PenTest Security Report" were blank or link lists only. This week has not started, so expect the challenge page to change. Before quoting a rule or date, say the copy date and offer to refresh.
> The old text from 2026-10-28 is kept in `reference/_superseded-2026-10-28/week-7.md`.
> Saved pages: `Resources/Week_8/` (see the end of this file).

---

## Reading rule
Read this whole file before answering any question about this week.

## For the owner's project (facts, not decisions)
- The Premium Residency Objective: integrate an API library into the app built earlier, choose one that fits that app, and make the app agentic with OpenRouter. This is the week where an outside AI service could enter the caregiving app. MVP #1 uses none, so any choice here is a new decision for the owner (and likely MVP #2). Do not assume it.
- The page says to use "the same repo from Week 3" (old label for the Week 4 app repository, see `course-map.md`).
- It asks for a PenTest Security Report and ADRs, so the Week 6 PenTest and the ADR habit carry forward.
- The page has leftover wording: "To Submit" appears twice, and it asks for a "Summary of Changes" report.

---

## The challenge page, word for word

Source: `Resources/Week_8/Week 8 Coding Challenge - Integrate Apps Together (Notion copy 2026-11-13).md` (text below the header line, unchanged).

# How to Submit

Email your teacher the link to your Github repository mdenner@techfleet.org

# Summary

Now it’s time to make your app talk with different apps! API integrations are a common way to pull data from other apps and present the data in a way you need to customize. In this challenge you will take your existing Week 3 repo and integrate an API library into the code, and build an elegant experience around it.

# Standard Residency Objective

Choose of of the following API Libraries below and implement it into your ADHD Budgeting App however you see fit. Make sure that the experience you build is valuable, feasible, and usable for people who experience ADHD. Document your architectural decisions in ADR’s, and complete a PenTest Report.

1. [Nilearn ADHD API](https://nilearn.github.io/dev/modules/description/adhd.html) - integrate lessons about ADHD
2. [Google Chat API](https://developers.google.com/workspace/chat/api/reference/rest) - integrate a user-to-user chat function
3. [Financial Budgeting API](https://www.fiskil.com/grow/banking-api/personal-finance/budget-tracking) - integrate more nuanced financial budgeting features
4. [OpenRouter API](https://openrouter.ai/) - make your application agentic somehow

# Premium Residency Objective

You did not build an ADHD budgeting app, but you need to make an integration with the app you built in Week 3. Choose an API library that suits your app and meets an unmet need. Implement it into your App however you see fit. Make sure that the experience you build is valuable, feasible, and usable for people who experience ADHD. Document your architectural decisions in ADR’s, and complete a PenTest Report.

1. Find an API library on your own and integrate it
2. [OpenRouter API](https://openrouter.ai/) - make your application agentic somehow

# Deliverables

1. Your Github repository
2. Your Vercel link with the live app
3. Architectural Decision Records (child page: https://app.notion.com/p/a5f9219a46918370bf818191f4c35aca)
4. PenTest Security Report (child page: https://app.notion.com/p/cfa9219a46918387b22f819c5881c3fe, blank in the copy)
5. CI/CD Gate Checks

# Tools

1. Notion
2. OpenRouter
3. Vercel
4. Github
5. Supabase
6. API library

# Requirements

1. Make new product requirements (only vision and scope and technical requirements) for this work. Use the Week 2 templates for guidance on what to write. Put it in a Notion document.
2. Add the specifications to your kanban board and put the ticket into the proper status.
3. Serve user needs somehow by integrating data from other apps using an open API library.
4. Write full product requirements so that we understand the problems, goals, and scenarios to support with the new feature. Add the specifications to your kanban board.
5. Document the architecture standards for your APIs and add them to the repo.
6. Use the same repo from Week 3 to develop.
7. Build a CI / CD check in Github to ensure that whenever new code drops, it never regresses and always follows the architectural decisions you decided on.
8. Write a one page summary **(NOT USING AI)** of what you did and what you learned when you submit the work to me.

# To Submit

# To Submit

USE THE PREVIOUS GITHUB REPOSITORY FROM WEEK 3: “AI DEVELOPMENT RESIDENCY - WEEK 3 - APP”

Use the submission template

<details>
<summary>Expand</summary>

# Links

1. Drop your link to the Github Repository here
2. Drop your link to your hosted Vercel app here

# Documents

1. Drop any Notion Document links here
2. Drop any other document links here

# What I Did

Write what you did in no less than 2 paragraphs. Provide full technical detail so that anyone reading it can understand what exactly you did. DO NOT use AI for this! I will check!

# What I Learned

Write what you learned in no less than 2 paragraphs. Describe the full details of what you learned, what you will do differently next time, and how the lessons from this exercise will help you in project team work in the future. DO NOT use AI for this! I will check!

</details>

Produce a “Summary of Changes” report with all of the decisions that were made. Push all of the NEW code, report doc, and the submission template files you produce into the WEEK 3 repository through a merge.

Email the instructor the following:

1. The link to the Github repository

---

## Still changing, and how to refresh

| Item | Status on 2026-11-18 | How to refresh |
|---|---|---|
| Week 8 - APIs Lecture Notes (id f6b9219a46918337985981ccba2a0a54) | Blank in the 2026-11-13 copy; not re-checked | Re-copy after class (Dec 7) |
| Week 8 - APIs and Agents - Weekly Class Materials (id d7d9219a4691838aa6bb81f4fa222e92) | Blank in the 2026-11-13 copy; not re-checked | Re-copy |
| Child pages: Architectural Decision Records, PenTest Security Report | Blank or link lists | Re-copy |
| Challenge page | Copied 2026-11-13 | Re-copy at the start of the week |

Refresh method (needs the owner's yes, because it uses Claude in Chrome): see `week-6.md`, section 5.

## Where the saved files are
- `Resources/Week_8/Week 8 Coding Challenge - Integrate Apps Together (Notion copy 2026-11-13).md`
- `Resources/Week_8/Week 8 - blank pages in the 2026-11-13 copy.md`
