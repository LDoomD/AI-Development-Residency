# Vision and Scope - Hat Check
- Source copy: https://app.notion.com/p/3d59219a469182d09f0701b9add32085
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:13.266Z
- Not saved: none (a link-preview block for the Scope database view has no text; child pages saved as their own files)

---

# Scope

(link preview: https://app.notion.com/p/3d59219a469182d09f0701b9add32085#3009219a4691820ca35a01ab4e0caab3)

- Release Level Scope
- Job Seeker Use Cases
- MVP #1 Requirements (Handoff)

# MVP #1 Vision Board — Hat Check

## 🔭 Vision Statement

Hat Check cuts through the noise of the job market.

## 👤 Audience

Job Seekers

## ❓ User Problems & Business Problems

- A lot of job postings do not share all the details of what's expected.
- People may not have the advantage or privilege to work with someone who can pay close attention to their needs and prepare their story for interviews. Most people can't afford a dedicated career coach.
- There are hidden details that interviewers expect you to discuss that are never posted in the description ("other duties as needed").
- Companies make their own definitions of jobs, deviating from what people expect to be doing in a role (for example, a product manager also required to do research and design).
- People training for roles don't know what they don't know, and rely on other information to coach them — which may be conflicting and scattered.

## 🎯 Business Goals

- We want people to know before applying whether a role truly fits; to stop wasting effort on wrong-fit roles; to focus where they can win; to apply with confidence.
- We want people to see the real role behind the title; understand true seniority; avoid under- or over-applying; negotiate from accurate information.
- We want people to understand a post in plain language; see the real day-to-day work; feel confident they grasp the role.
- We want people to see the hidden expectations for free; walk in without blind spots; have the insider knowledge coaches charge for.
- We want people to highlight the right experience; prove they can do the real duties; raise their interview rate honestly.
- We want people to prep for the actual role; reduce interview anxiety; perform at their true ability.

## 💎 Value For Each Problem

- **Give every job seeker the insight of a personal career coach — for free.** (Because today postings hide what's really expected, and most people can't afford a dedicated coach to prepare their story.)
- **Make the unwritten expectations of a role visible before the interview.** (Because today interviewers expect duties they never post, and seekers get blindsided by "other duties as needed.")
- **Reveal the true shape of a role behind its title.** (Because today companies redefine jobs and inflate titles, and seekers can't tell a standard role from an off-script one — like a PM also expected to do research and design.)
- **Replace scattered, conflicting advice with one trustworthy standard.** (Because today people training for roles don't know what they don't know, and the guidance they find is fragmented and contradictory.)

## 🏆 Competitive Advantage (Unique Value)

- Unlike other companies, we measure a posting against the real standard for the role — not just the words on the page.
- Unlike other companies, we reveal the expected and the hidden, unwritten duties for free — the insider knowledge career coaches charge for.
- Unlike other companies, we give an honest title-fit and seniority read, and flag duties that go beyond the role's normal scope.
- Unlike other companies, we ground every answer in an open, shared standard (the Skills & Practices Framework) instead of opaque AI guesses.
- Unlike other companies, we are free, open source, and account-free — the user's data never leaves their device.
- Unlike other companies, we turn the decode into resume and interview prep for that exact role, all in one flow.
- Unlike other companies, we prepare people honestly and transparently — no stealth, nothing to hide from an employer.

## 🚧 Barriers to Product Success

- Framework currently covers mostly tech/digital-product roles → limited audience at launch.
- Dependency on an external dataset for coverage, accuracy, and updates.
- Accurately matching messy, non-standard job-description text to standard duties (NLP/parsing risk).
- Getting users to trust AI-generated role analysis; a confident wrong answer erodes trust fast.
- No accounts = no persistent data to learn from or re-engage users by email.
- Awareness/discovery with no built-in network effects and no paid acquisition budget.
- Competitors (JobDecode, Revarta, [gothired.ai](http://gothired.ai)) adding their own baseline comparison.
- Sustainability of a free + open-source model — funding the build and ongoing upkeep.
- Browser-only storage limits stickiness across devices (accepted for MVP, but a growth ceiling).

## 💰 Costs

- Developer time to build the JD-to-framework matching engine and UI.
- LLM/API costs for parsing and matching job descriptions (if LLM-based).
- Design, UX, and accessibility work.
- Static hosting + domain (low, but ongoing).
- Prompt engineering and tuning the match against the framework.
- Testing, QA, and user testing with real job seekers.
- Ongoing maintenance to sync with framework updates and expand role coverage.
- Legal review for MIT license + CC BY 4.0 attribution compliance.
- Marketing / awareness effort (no paid acquisition built in).
- Open-source community upkeep (issues, contributions, docs).

## 📊 Key Performance Indicators

- **Grow adoption among job seekers:** monthly unique users; number of job descriptions decoded; return (repeat) visitors; shares / referrals (word-of-mouth rate).
- **Help users fully decode a role and apply with confidence:** % who complete a full decode (title + JD → results); % who open the hidden/expected-duties section; average decodes per user; % who use the resume/interview prep after a decode.
- **Improve job-search outcomes:** % reporting the app changed which jobs they applied to; % reporting they landed an interview (self-report); self-reported confidence lift (before vs. after); % saying hidden duties helped them prepare.
- **Become a trusted, free alternative to career coaches:** satisfaction / NPS; % who say they'd otherwise have paid a coach; user-rated accuracy/trust of the analysis; qualitative testimonials collected.

## 🧭 Use Cases to Support (MVP #1)

- Show role fit and what's expected that's missing; give a clear go / stretch / no-go call; recommend which gaps to close first; prioritize a shortlist of winnable roles.
- Score how closely the post matches the standard for that title; detect title inflation or under-leveling; read true seniority from the duties; compare the post to the seeker's level.
- Translate jargon into plain English and its implications; show the expected deliverables, tools, activities, and skills; surface the real day-to-day expectations.
- Reveal duties expected for the title but absent from the post; flag extra responsibilities beyond the normal scope; explain why each hidden duty matters.
- Show which experiences, skills, and deliverables to highlight for each expected duty; prioritize must-haves vs nice-to-haves; flag hidden duties worth proving.
- Generate likely questions from the role's real duties; show what the post will probe and why; provide a role-specific prep checklist; suggest questions to ask the employer.

---

# 📐 Scope — Value → Problem → Outcomes

### Give every job seeker the insight of a personal career coach — for free

**Associated problem:** Postings don't share all the details, and most people can't afford a career coach.

**Outcomes to achieve:**

- Job seekers can see the full set of responsibilities a role typically requires, beyond what the posting lists.
- Job seekers understand what "good" looks like for the role without paying an expert.
- Job seekers can tell how complete or incomplete a given posting is.
- Job seekers receive coach-level insight regardless of budget or network.
- Job seekers feel confident they understand the role before investing time applying.
- Job seekers can prepare their story for the role without one-on-one coaching.

### Make the unwritten expectations of a role visible before the interview

**Associated problem:** Interviewers expect duties that are never posted ("other duties as needed").

**Outcomes to achieve:**

- Job seekers can see the duties expected for the role but absent from the posting.
- Job seekers know which hidden expectations are most likely to come up in an interview.
- Job seekers are no longer blindsided by responsibilities that weren't advertised.
- Job seekers understand why each hidden expectation matters to the role.
- Job seekers can prepare for the unwritten parts of the job, not just the written ones.

### Reveal the true shape of a role behind its title

**Associated problem:** Companies redefine jobs, so the title deviates from the real work.

**Outcomes to achieve:**

- Job seekers can tell how closely a posting matches the standard expectations for its title.
- Job seekers can see which duties in a posting fall outside the normal scope of the title.
- Job seekers understand the true seniority a role implies from its duties.
- Job seekers can recognize when a role is really two jobs in one.
- Job seekers can judge whether the title honestly reflects the work.
- Job seekers can weigh a posting against a trusted baseline for the role.

### Create a trustworthy standard for job fit

**Associated problem:** People don't know what they don't know, and rely on scattered, conflicting info.

**Outcomes to achieve:**

- Job seekers can rely on one consistent, trusted source of what a role requires.
- Job seekers can see the gaps between what they already have and what the role expects.
- Job seekers know what to learn or show to become ready for the role.
- Job seekers can trust the guidance is grounded in a real standard, not opinion.
- Job seekers spend less time reconciling conflicting advice from many sources.
- Less-experienced job seekers understand the expectations experts take for granted.

### Help job seekers apply with confidence to roles

**Associated problem:** Across all the above, seekers waste effort on wrong-fit or mislabeled roles and struggle to present themselves well.

**Outcomes to achieve:**

- Job seekers can decide whether a role is worth applying to before investing the effort.
- Job seekers can focus their energy on roles they can realistically win.
- Job seekers know which experiences, skills, and results to highlight for the role.
- Job seekers can prepare for the specific interview that role implies.
- Job seekers apply feeling informed and in control rather than guessing.
- Job seekers can revisit and build on their understanding of a role over time.

---
