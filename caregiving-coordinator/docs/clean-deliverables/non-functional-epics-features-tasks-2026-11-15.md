# Non-functional epics, features and tasks, T1 to T4 (approved 2026-11-15)

**What this is:** the non-functional list for MVP #1, in the same numbered shape as Morgan's and Lucy's boards (T1, T1.1, T1.1.1). Every line comes from `docs/build-plan-nfr-draft-2026-11-12.md`, boxes 1 to 4, which the owner approved on 2026-11-12. This file is the master copy. Figma must say "same as this file, [date]" and match it word for word, except that the † marks below appear only in this file.

**What † means:** the build plan tags that row "Proposed" inside an approved box. On 2026-11-15 the owner said to include those rows. They are in the Figma list without the mark. Open items about them stay in the build plan file.

**Why the groups are in this order:** the lecture's build plan lists the non-functional parts as tool selection, database architecture, system architecture, security protocol, development operations and quality engineering (Week 2 lecture, about 45:40 to 48:09; lecture notes, "Non-Functional Requirements and Build Plan"). T1 to T4 are the first four. T5 and T6 are left out until the owner approves box 5 (a Proposed draft) and box 6 (not written yet). Morgan's and Lucy's lists are grouped differently (by technical area and by requirement area). The lecture does not say how to shape this list, so the instructor's order is used.

**Why a "Grounded in" line:** Lucy's board has a traceability table that says where each area comes from. Each group below ends with one line that does the same.

---

## T1. Tools and hosting
**T1.1 The tool set**
- T1.1.1 The code is written and checked with Claude Code and held in GitHub, with one branch and one pull request per piece of work.
- T1.1.2 The web app and its server code are hosted on Vercel.
- T1.1.3 All app data is stored in a Supabase Postgres database.
- T1.1.4 Screens are built with Material UI.
- T1.1.5 † Caregivers and invited relatives sign in with Supabase Auth.
- T1.1.6 Sign-in and invite emails are sent by an outside email service, which is not chosen yet.

**T1.2 Plans and regions**
- T1.2.1 † The Supabase project is in a US region (us-east-1), and Vercel functions run in Washington, D.C. (iad1).
- T1.2.2 Week 4 uses the Supabase Free plan with fake data only, and the Pro plan is turned on before any real caregiver data. (The Free plan part is a course requirement. The Pro plan part is †.)
- T1.2.3 † The app stays on Vercel Hobby while building and is rechecked before launch.

**T1.3 Left out of MVP #1**
- T1.3.1 No ad or analytics trackers, no integrations that pull data in, no outside AI service and no payment tools are used.

*Grounded in: build plan box 1; Week 2 and Week 3 coding challenges (tools); the Week 4 page (free plan, fake data); the risk profile (trackers, integrations, AI service).*

## T2. Database
**T2.1 Tables**
- T2.1.1 The foundation tables hold caregiver accounts, care circles, the cared-for person, circle members and roles, consent records and an access log.
- T2.1.2 Care notes and care tasks are added with Epic 3, and money, benefits and coverage records with Epics 5 and 6.

**T2.2 Rules every table follows**
- T2.2.1 Row-level security is on for every table, so members see only their own circle.
- T2.2.2 Data is typed in by people only, and no table is fed by an outside integration.
- T2.2.3 Deleting a cared-for person or a caregiver also deletes the health data entered about that person.
- T2.2.4 † Health notes cannot be shared with a member until the sharing consent record exists.
- T2.2.5 The database diagram is saved in the `docs` folder of the repository in Week 4.

*Grounded in: build plan box 2; the risk profile (consent, deletion, row-level security, no data feeds); the Week 4 page (database diagram).*

## T3. System architecture
**T3.1 The parts**
- T3.1.1 The browser talks only to the web server, over HTTPS.
- T3.1.2 † The web server is a Next.js app on Vercel that reads and writes data through Supabase with the signed-in person's session.
- T3.1.3 † Sign-in uses Supabase Auth with the session kept in cookies, checked on every request.
- T3.1.4 The database checks every read and write against the signed-in person with row-level security.
- T3.1.5 † An outside email service connected to Supabase Auth sends sign-in and invite emails, set up before the first relative is invited.

**T3.2 What does not connect**
- T3.2.1 No ad, analytics or tracking scripts run in the browser.
- T3.2.2 No outside data feeds into the database.
- T3.2.3 No AI service is used.

*Grounded in: build plan box 3; the saved Vercel and Supabase vendor pages; the risk profile (trackers, data feeds).*

## T4. Security protocol
**T4.1 Access and consent**
- T4.1.1 Members see only their own circle, and role changes are visible to the circle.
- T4.1.2 No health note is saved without a collect consent, and none is shared without a separate share consent.
- T4.1.3 An access log records who viewed or changed which health note and when, and no one can edit it.

**T4.2 Keys and data**
- T4.2.1 † The Supabase admin key stays only on the web server as a Vercel environment setting, never in the browser or in GitHub, and `.env.local` is listed in `.gitignore`.
- T4.2.2 If a secret key ever reaches GitHub, a new key is made in Supabase right away, because deleting the file is not enough.
- T4.2.3 Only fake data is used while building in Week 4.
- T4.2.4 Data is encrypted in transit and at rest, which the vendors provide.

**T4.3 Safe code**
- T4.3.1 † Errors show a plain message and never show data or keys, and a failed check denies access.
- T4.3.2 † Package versions are locked, and `npm audit` runs before each merge.
- T4.3.3 † A breach plan says who checks and how people are told within 60 days, before any real caregiver data.

*Grounded in: build plan box 4; the risk profile (consent, access control, FTC breach rule); the OWASP Top 10:2025 list; the Week 4 page and its safety checklist (keys, fake data); the Vision and Scope barrier "Health data and consent are a risk."*

---

## Not in this file
- **T5 Development operations** and **T6 Quality engineering:** waiting on boxes 5 and 6.
- **Accessibility, plain language and browser support:** in Morgan's and Lucy's lists, but not in the Vision and Scope or the build plan. New content the owner has not decided.

## Known limits
- The † rows are Proposed in the build plan. They were included by the owner's decision on 2026-11-15, which is not the same as the owner approving each row separately.
- Vendor facts (regions, plans, encryption) come from the saved vendor pages and may change.
- Nothing here is legal advice or says the product is "compliant."
