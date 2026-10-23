# Week 2 deliverables plan — due Oct 26, 2026

**Course:** Tech Fleet AI Development Residency, Fall/Winter 2026 (Premium track)
**Instructor:** Morgan Denner — mdenner@techfleet.org
**Written:** 2026-10-23 · **3 days to deadline** · course budgets 8 hrs/week homework

**Specialization:** AI Automation **+** Advanced agentic workflows, combined —
framed as *agentic workflows applied to adaptive learning systems*. Agents are
the method; learning is the domain.
⚠️ Needs instructor approval. See "Do today".

**Project:** this app. It replaced `growth-ads-system` on 2026-10-23 — see
[`../STATUS.md`](../STATUS.md) for why.

---

## Residency schedule

| Wk | Class | Topic | Tools | HW due |
|---|---|---|---|---|
| 1 | Oct 12 | How the Web Works | Claude Code, GitHub | Oct 19 |
| **2** | **Oct 19** | **Product Delivery Management** | **Notion** | **Oct 26** |
| 3 | Oct 26 | Network Architecture | Vercel, Material UI | Nov 2 |
| 4 | Nov 2 | Data Engineering | Supabase, O*NET | Nov 9 |
| 5 | Nov 9 | Information Security | OWASP, Cloudflare, Aikido | Nov 16 |
| 6 | Nov 16 | Coding Architecture & QA | ADRs, CI/CD, AI Evals | Nov 30 |
| — | Nov 23 | *holiday, no class* | — | — |
| 7 | Nov 30 | APIs and Agents | OpenRouter | Dec 14 |
| 8 | Dec 7 | SEO / AEO | PageSpeed, GA, WAVE | Dec 21 |
| 9–16 | Jan 1 – Feb 28 | Real client team project, 15–20 hrs/wk | — | — |

**The Week 3 app is reused in Weeks 5, 6, 7, and 8.** Whatever ships by Nov 2
is what the rest of the residency builds on.

---

## Do today — unblockers, not deliverables

| # | Action | Why |
|---|---|---|
| 1 | Message Morgan: specialization choice + application subject | **Was due Oct 19.** Overdue. |
| 2 | Same message: is the combined specialization approved? | Syllabus requires instructor approval of specialization topics |
| 3 | Same message: **repo naming is contradictory.** Week 1 says one repo `AI Development Residency` with a folder per week; Weeks 3–8 say a separate repo per week. Which? | Determines how the project is structured — blocks repo creation |
| 4 | Same message: **does Week 4 use my app or the O*NET chatbot?** Week 4's premium section is the only one naming a specific app instead of the student's own. | Changes whether the app carries 5 or 6 of 6 build weeks |
| 5 | Same message: Notion or Word docs? | Syllabus says "document your homework in word docs"; Week 2 page says Notion + email a Notion link |
| 6 | Create the **public** GitHub repo once naming is settled | Course mandates public repos |
| 7 | Copy the Notion template page into your own space | Template page says do not edit it directly |

---

## Assignment A — research paper (Premium only)

**Status: drafted.** See [`../Week 2 Coding Challenge/research-paper.md`](../Week%202%20Coding%20Challenge/research-paper.md)

Write about **the specialization field**, not the product. The product appears
only in section 8. Eight required sections: introduction · career relevance ·
background · how it works when building products · what it includes · team
activities · tools and skills · the app you'll build.

APA style, inline citations, bibliography, no plagiarism. May be written with
Claude but must be polished and evaluated.

**Outstanding:**
- [ ] **Section 8 must be rewritten** for this project. It currently describes
      the ads reconciliation panel. Sections 1–7 stand — the specialization
      did not change.
- [ ] §2.4 ("what I want to be able to do") should be in your own words
- [ ] Re-verify all 7 source links before sending

**Submit:** email the paper to Morgan + fill out the Google Form on the
Week 2 PREMIUM Notion page.

---

## Assignment B — product specifications

Five Notion templates, plus a build plan, backlog, and deck.

### B1. Market Research — *substantially covered by inherited research*

`docs/inherited-research/research/` already contains the substance:

| Deliverable | Inherited source |
|---|---|
| Market analysis | `2026-08-09_ai-tutor-landscape-2026.md` (3,285 words, tool-by-tool) |
| Competitive analysis | `2026-08-08_adhd-tools-landscape.md` (verified pricing, "every tool surveyed is proprietary") |
| Unique positioning | `2026-08-08_prior-art.md` → **"THE WHITESPACE"** section |
| Feature analysis | `2026-08-08_spaced-repetition-tools-and-adherence.md` ("mechanisms worth stealing") |

- [ ] Reformat into the Notion template's structure
- [ ] Write explicit positioning statements
- [ ] **Check dates** — this research is from August 2026. Spot-check that no
      major competitor launched since.

### B2. Product Release Vision and Scope — *empty*

11 fields, **twice** — once for MVP #1, once for MMP: Audiences · Problems per
audience (up to 3) · Business goals · Value · Unique value proposition ·
Barriers to success · Release-level costs · KPIs · Use cases · Release-level
scope table (Value / Problem / Scope of Outcomes).

⚠️ **Decision required: personal tool or multi-user product?**
The predecessor's `CLAUDE.md` stated "a personal learning system for one user,
not a general product." This template demands *audiences*, plural, and Weeks
3 and 5 demand user accounts with secured data. Pick one and defend it. Cannot
be skipped.

### B3. Epics and Features — *empty*
Template shape: **4 epics × 5 features**, each with a feature-level user story
and use case scenarios.

Natural epic candidates: content and lesson authoring · the subject-type
router · the review scheduler · the safety mechanisms (floor, escape hatch,
integration gate).

### B4. Build plan — *empty*
Must assume a **three-tier network architecture with stored data**:
- [ ] Vercel for hosting
- [ ] Supabase for the database
- [ ] GitHub for the repo
- [ ] User accounts, so user data must be secured

⚠️ **Note the re-platform.** The inherited design assumed a local toolchain —
Obsidian for content, Anki for scheduling, NotebookLM for Q&A. None of that
survives into a hosted web app. The *mechanisms* carry over (plain-text
content, spaced-repetition scheduling); the *tools* do not. Say this
explicitly in the build plan rather than leaving the contradiction implicit.

### B5. Backlog Kanban Board — *empty*
Populate from the epics/features/tasks list using the Notion template.

### B6. Product Pitch Deck — *empty*
Summarise all of the above.

### B7. One-page summary — **USER WRITES THIS, NO AI**
Instructor states: *"DO NOT use AI for this! I will check!"* for both the
"What I Did" and "What I Learned" sections (2+ paragraphs each).
**Claude must not draft these.** Claude may supply a factual list of actions
taken as raw material; the writing must be the user's own.

---

## Submission mechanics

1. Folder named `Week 2 Coding Challenge` in the repo, submission doc inside
2. Open a pull request, then merge it
3. Upload on the Tech Fleet Network Platform → weekly module under Courses
4. Email Morgan the filled submission template

Template fields: GitHub repo link · Vercel app link (n/a this week) · Notion
document links · other document links · What I Did · What I Learned

---

## Scope for Week 3 — decided, recorded here so specs match it

**Subject domain:** automation and agentics. This decides what seed content
sits in the database, nothing more. The app is not being used as a live study
tool during the residency.

**Modes:** all four present. Router plus MAP, DRILL, and EXAMPLES fully
working. **REPS deliberately thin** — record and self-rate, no AI judging —
until Week 7, whose assignment is literally "make your application agentic
somehow."

⚠️ **Open conflict:** `inherited-research/subjects.md` tags subject #3
"Agentic engineering" as **MAP + REPS only**, and #2 "Vibe / agentic marketing
& growth hacking" as MAP + EXAMPLES + REPS. Neither has DRILL. That collides
with demonstrating four modes. Revising the tagging looks defensible — agentic
engineering plainly has DRILL material (API signatures, CLI flags, framework
patterns) and EXAMPLES material (good agent code vs. bad) — but the August
tagging was considered, so change it deliberately and write down why.

---

## Explicitly NOT this week

- **No application code.** Week 2 is specifications. Building starts Week 3.
- **No REPS audio evaluation.** That is Week 7.
- **No learning-effectiveness claims.** The app will have no live user during
  the residency, so retention cannot be validated. The research supports the
  *design*; it is not evidence this build works.
