> **Renumbered 2026-11-13.** This is the old local file `week-8.md` (snapshot 2026-10-28). The live course calls this "Implement an SEO / AEO Strategy." Live course week: **9**, due Jan 5. The text below is **NOT yet re-checked** against the live page (a fresh copy is in Notion under "Tech Fleet course copies 2026-11-13" but not saved to `Resources/` yet, by the owner's choice). Treat dates and details as unverified. The original is in `reference/_superseded-2026-10-28/week-8.md`.

---

# Week 8 — SEO and AEO (Dec 14)

**Weekly-materials page** (`Week 9 - SEO and AEO - Weekly Class Materials` — note the source page is titled "Week 9", another numbering artifact; it covers reconciled Week 8) **is blank** — not yet populated by the instructor as of 2026-10-28.

---

# Week 8 Coding Challenge — Implement an SEO / AEO Strategy

## How to Submit

Email your teacher the link to your Github repository: mdenner@techfleet.org

## Summary

How will your app survive if people can never find it on their own? This is where optimizing for search engines comes in. Before AI came around, search engines like Google were the primary way that people found information on the web. The page results on the search engine were ranked based on some secret recipe that the company barely shared. People spent their entire careers (SEO specialists) honing their craft to engineer how to get websites to the top of the first search results page. Now, with AI chatbots everywhere, the main way people search (NOTE: not the only way!) is an AI model itself. And so, "Ask Engine" Optimization was born. The way we optimize sites for AI Chat Bots to read is similar to how we optimize for search engines, with added steps. In this exercise you will identify the key areas for SEO Optimization and AEO Optimization, and build the fixes into your Week 3 repository.

## Standard Residency Objective

Optimize your codebase for AEO and SEO. Do the research to learn what you need to do using Claude. Update your Week 3 repository with the new results.

## Premium Residency Objective

**You are doing the same assignment as the standard residency students.**

## Tools

Claude, Notion, Pagespeed Insights measurement tool, Google Analytics, Microsoft Clarity, WAVE web accessibility measurement tool

## Requirements

1. Document new ADR's with the AEO and SEO decisions and add them to the Week 3 repo.
2. Test your website for accessibility using WAVE, document the fixes that need to be fixed, and code the fixes.
3. Deploy any accessibility fixes to Github Week 3 repo with new CI/CD checks that ensure all future code changes include the accessibility standards that they need in order to rank high on SEO and AEO.
4. Add the proper schema to your website so that AI bots can crawl the site.
5. Set the proper settings on Cloudflare to allow AI bot traffic.
6. Also thwart malicious bots using Cloudflare.
7. Make new CI/CD checks for every new piece of code to ensure that it's optimizing for SEO and AEO so that it doesn't hurt your search rankings.
8. Add your website to Google Search Console and Google Analytics.
9. Write a one page summary (NOT USING AI) of what you did and what you learned when you submit the work to me.

## To Submit

USE THE PREVIOUS GITHUB REPOSITORY FROM WEEK 3: "AI DEVELOPMENT RESIDENCY - WEEK 3 - APP"

Use the submission template.

Produce a "Summary of Changes" report with all of the decisions that were made. Push all of the NEW code, report doc, and the submission template files you produce into the WEEK 3 repository through a merge.

Email the instructor the following:
1. The link to the Github repository

---

**Note:** this week explicitly addresses a "login-gated app + SEO" tension — the summary itself asks "how will your app survive if people can never find it" and targets fixes into the Week 3 repo, implying SEO/AEO work applies to whatever public-facing surface exists (landing/marketing pages), not necessarily the authenticated app interior. Worth confirming with the instructor if your app's public surface is thin.

**Source:** https://app.notion.com/p/tech-fleet-community-dao/Week-8-Coding-Challenge-Implement-an-SEO-AEO-Strategy-b841a3bddce58301831081536ed37cf7. **Copied verbatim:** 2026-10-28, via logged-in browser session, scroll-verified in full.
