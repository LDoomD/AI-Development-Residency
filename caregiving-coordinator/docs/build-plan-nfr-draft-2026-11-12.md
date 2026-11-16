# Build plan and non-functional requirements (draft, 2026-11-12)

Template: the instructor's lecture board, "Non-Functional Requirements and Build Plan" (board `mqryoCyR9mAw3v6kyDlmes`, node 576:5824). The 6 non-functional boxes come first, then the 6 functional ones (lecture 44:13 to 44:20). This week each part is only named and put in order. Detail comes in later weeks (lecture 48:21 to 48:43).

Tags:
- **Fact:** from a course page or a vendor page.
- **Approved:** decided by the owner.
- **Proposed:** waiting on the owner.

---

## 1. Tool selection (Approved by the owner, 2026-11-12)

What the course asks for: "give me the tool selection. Give me the servers you want to use. Give me the database... other tools that we need to buy and set up" (lecture 45:37 to 45:55). Tools can be swapped later: "If they don't work out... you just swap them out and migrate to another tool" (lecture 46:17 to 46:22). Taught in depth in Week 3 (lecture 48:33).

### Tools we use
| Tool | What it does for us | Source | Tag |
|---|---|---|---|
| Claude Code | Writes and checks the code | Week 3 coding challenge, Tools | Fact |
| GitHub | Holds the code. One branch and one PR per piece of work. | Week 2 coding challenge, requirement 6; Week 3 coding challenge | Fact |
| Vercel | Hosts the web app and runs its server code | Week 2 requirement 6; Week 3 Tools | Fact |
| Supabase (Postgres database) | Stores all app data, with row-level security on every table | Week 2 requirement 6; risk profile | Fact |
| Supabase Auth | User accounts and sign-in for caregivers and invited relatives | Week 2 requirement 6 ("user accounts with secured data") | Proposed |
| Material UI | Ready-made screen parts (buttons, forms, tables) | Week 3 Tools | Fact |
| An outside email service (added with box 3) | Sends sign-in and invite emails to relatives. The service is not chosen yet. | Supabase custom SMTP page (`build-plan-2026-11-12/01`) | Approved 2026-11-12 (box 3) |

### Settings and plans
| Choice | Why | Source | Tag |
|---|---|---|---|
| Supabase project in a US region (us-east-1) | The data stays in the chosen region, and the region can't be changed later without a new project | Supabase regions, SOC 2 and change-region pages (sources 56, 59, 60) | Proposed |
| Vercel functions in Washington, D.C. (iad1), the default | It sits near us-east-1. That reason is general knowledge, not from our research. | Vercel function regions (source 62) | Proposed |
| Supabase Free plan in Week 4, with fake data only; Pro ($25 a month) later, before any real caregiver data | The live Week 4 page lists "Supabase (free plan)" and requires fake data only. Free has no automatic backups. Pro keeps 7 days. | Week 4 Tools and requirement 7 (source 11); Supabase backups and pricing (sources 57, 58); risk profile, "Backups" | Free in Week 4: Fact. Pro later: Proposed |
| Vercel Hobby ($0) while building | Pro is $20 a month. Whether Hobby allows a real launch wasn't found on Vercel's pages. | Vercel pricing (source 63) | Proposed: recheck before launch |
| No HIPAA add-ons (Supabase Team $599 a month; Vercel $350 a month) | HIPAA probably doesn't apply. Recheck if we ever work with a doctor or health plan. | Risk profile, open question 3 and recheck triggers | Proposed |

### Tools we leave out of MVP #1
| Tool type | Why it's out | Source |
|---|---|---|
| Ad and analytics trackers (pixels, ad SDKs) | Every Washington lawsuit and FTC health-app case found is about these | Risk profile, "No ad or analytics trackers" |
| Integrations that pull data in (calendar, health portals, devices) | One working integration can put us under the FTC breach rule | Risk profile, FTC rule |
| An outside AI service | Visit recordings and AI notes are out of MVP #1, and an AI service would hold health data | Risk profile, "Out of MVP #1" |
| Payment tools | "Who pays" stays open | Handoff 2026-11-12, section 3 |

### Open items for this box
- **Email for inviting relatives.** Epic 3's task "Settling who handles care tasks and money" brings in other people. Supabase Auth's built-in invite emails may be enough. That is general knowledge, not checked; check it in the Week 3 system architecture step.
- **Week 4 builds this product, and OpenRouter is not part of it.** The live Week 4 page tells Premium students: "you are building the app you chose based on your specialization. Build that using these same tools and the product specifications you made." Its tool list has no OpenRouter. The career chatbot that uses OpenRouter is Week 7 (source `11-course-facts-live-weeks.md`). (Corrected 2026-11-15. The earlier text used the course's old week numbers and called Week 4 a separate chatbot.)
- **The web framework** (for example, which React framework runs on Vercel) is decided in the system architecture box, taught in Week 3.

---

## 2. Database architecture (Approved by the owner, 2026-11-12)

What the course asks for: "You have to design the data. It's called database architecture. You have to architect the database just like you architect screens" (lecture 46:30 to 46:39). Taught in depth in Week 4 (lecture 48:21). This week it only names the main tables and their build order. Columns and the diagram come in Week 4.

### The main tables
| Table | What it holds | Why it exists (source) | When it's built |
|---|---|---|---|
| Caregiver accounts | One row per person who signs in (Supabase Auth) | Coding challenge, requirement 6; tool selection box | Foundation |
| Care circles | One per parent or partner being cared for. It links everyone in that family's care. | Epic 2; Epic 3 task "Settling who handles care tasks and money" | Foundation |
| Cared-for person | The parent or partner, with no account of their own, labeled parent or spouse or partner | Risk profile, product facts (the person often never signs up); audience labels (Audience 1 and 2) | Foundation |
| Circle members and roles | Who is in the circle (main caregiver, invited relative) and what each can see or change | Risk profile, multi-user access control | Foundation |
| Consent records | One record to collect health data, a separate one to share it, with who agreed and when | Risk profile, "Two separate consents" (RCW 19.373.030; NRS 603A.500) | Foundation |
| Access log (added 2026-11-12 with box 4) | Who viewed or changed which health note, and when. No one can edit it. | Box 4, access log rule (owner decision) | Foundation |
| Care notes | Health and behavior notes caregivers type in | Risk profile, data table row 1; Epic 3 and 4 tasks | Epic 3 (Nov 16 to 20) |
| Care tasks and owners | Who handles which care task or money task | Epic 3 task "Settling who handles care tasks and money"; Epic 2 task "Having relatives agree and follow through" | Epic 3 |
| Money, benefits and coverage records | Bills, benefits and coverage details | Risk profile, data table row 2; Epic 5 and 6 tasks | Epic 5 and 6 (Dec 7 to 11) |

### Rules every table follows
| Rule | Source | Tag |
|---|---|---|
| Row-level security is on for every table, so members see only their own circle | Risk profile; Supabase shared responsibility page (source 17) | Fact (rule) |
| Data is typed in by people only, with no tables fed by outside integrations | Risk profile, FTC rule | Approved (risk profile) |
| Deleting a cared-for person or a caregiver also deletes the health data entered about that person | Risk profile, "Deletion" (RCW 19.373.040; NRS 603A) | Approved (risk profile) |
| Health notes can't be shared with a member until the sharing consent record exists | Risk profile, "Two separate consents" | Proposed |
| The project lives in the US region chosen in box 1 | Tool selection box; sources 56, 59 | Approved |

### Build order
1. **Foundation first:** accounts, care circles, the cared-for person, members and roles, and consent records. Every epic needs them, Epic 3 included.
2. **Epic 3:** care notes, care tasks and owners.
3. **Epics 5 and 6:** money, benefits and coverage records.

The roadmap puts Epic 2 last. Its circle and member tables are built in the foundation anyway, because Epic 3 and the consent rules need them first.

### Open items for this box
- **Consent for a person who never signs up** (risk profile, open question 1). The consent records table holds whatever answer a lawyer gives. Until then, the table design records who agreed and in what role, and doesn't decide whose consent is valid.
- ~~An access log~~ Decided in box 4: added to the foundation (owner, 2026-11-12).
- **The database diagram is a Week 4 deliverable.** The live Week 4 page lists it under Deliverables: "Your database diagram, saved in the `docs` folder of your repository." It is made once the tables exist in Supabase (source `11-course-facts-live-weeks.md`). (Corrected 2026-11-15. The earlier text called it a Week 3 deliverable, which was the course's old numbering.)

---

## 3. System architecture (Approved by the owner, 2026-11-12)

What the course asks for: "System architecture is how do the servers talk to each other? ... my own web server, database server, email server?" (lecture 47:23 to 47:32). Week 3 asks for "a web server, a database server, and the code to make the app a reality" (`week-3-coding-challenge.md`). Taught in depth in Week 3 (lecture 48:29). New sources for this box are saved in `docs/sources/build-plan-2026-11-12/` and logged in `INDEX.md`.

### The parts and how they talk
| Part | What it is | How it talks to the others | Source | Tag |
|---|---|---|---|---|
| Browser | The caregiver's or relative's screen, built with Material UI | Talks only to the web server, over HTTPS | Week 3 challenge (Material UI); Vercel compliance (TLS, source 19) | Fact |
| Web server | A Next.js app on Vercel, in Washington, D.C. (iad1) | Signs people in and reads and writes data through Supabase, sending the signed-in person's session with each request | Vercel: "Next.js is a fullstack React framework for the web, maintained by Vercel... deploying to Vercel is zero-configuration" (04); Supabase SSR guide (03) | Proposed |
| Sign-in | Supabase Auth, with the session kept in cookies | The web server checks the session on each request | Supabase SSR guide: SSR "requires cookie-based session storage" (03) | Proposed |
| Database server | Supabase Postgres, US region (us-east-1) | Row-level security checks every read and write against the signed-in person | Supabase RLS: "Enable RLS on every table in an exposed schema" (06); box 2 | Fact (rule) |
| Email server | An outside email service connected to Supabase Auth (custom SMTP) | Sends sign-in and invite emails to relatives | Supabase: the built-in server "is not meant for production use" and refuses addresses "not part of the project's team" (01) | Proposed: which service is open |
| Screen kit | Material UI, set up for the Next.js App Router | Runs inside the web server's pages | MUI Next.js guide (05) | Fact (course tool) |

### What does not talk to anything
- No ad, analytics or tracking scripts in the browser (risk profile).
- No outside data feeds into the database, such as calendars, portals or devices (risk profile, FTC rule).
- No AI service (box 1).

### Build order
1. The web server on Vercel and the Supabase project in the US region, connected.
2. Sign-in with cookie sessions.
3. The email service, before the first relative invite (Epic 3, "Settling who handles care tasks and money").
4. Then the foundation tables from box 2, with row-level security on.

### Open items for this box
- **Which email service.** Box 1 had no email tool. This adds one to tool selection. Pick a service, and check its plan and where it stores data, before inviting real relatives.
- **The admin key.** Supabase's invite step is an admin action ("Sends an invite link to an email address," source 02). The admin key must stay on the web server and never reach the browser. That is a security protocol item for box 4.
- **The GitHub repo.** Week 2 requirement 5 asks for a new public GitHub repository with no code in it yet. Week 4 then says to build in that same repository and not make a new one (source `11-course-facts-live-weeks.md`). The course's example name belongs to the ADHD budgeting app. The owner picks the name for the caregiving app, and it is still open. (Corrected 2026-11-15. The earlier text listed two names from an old page.)

---

## 4. Security protocol (Approved by the owner, 2026-11-12)

What the course asks for: "rules that you have to put in place called security protocol that could protect user data or it could protect the application from getting hacked" (lecture 48:06 to 48:18). Taught in depth in Week 5 (lecture 48:37). This box names each rule, why we need it, and when it's built. Sources:
- the approved risk profile (`docs/risk-profile.md`)
- the OWASP Top 10:2025 list in the project's `security-review` skill (`references/owasp-top-10-2025-checklist.md`)
- the vendor pages saved for boxes 1 and 3

### The rules
| Rule | What it protects against | Source | When it's built | Tag |
|---|---|---|---|---|
| Row-level security on every table. Members see only their own circle, and role changes are visible to the circle. | One family seeing another's data, or a relative quietly changing someone's access | Risk profile, multi-user access control; OWASP A01 Broken Access Control; Supabase RLS page | Foundation | Approved (risk profile) |
| No health note is saved without a collect consent, and none is shared without a separate share consent | Breaking the Washington, Nevada and Connecticut consent rules | Risk profile, "Two separate consents" | Foundation | Approved (risk profile) |
| The Supabase admin key stays only on the web server, as a Vercel environment setting. It's never in the browser or in GitHub, and the file that holds keys, `.env.local`, is listed in `.gitignore`. | Anyone with the key could read or change all data, bypassing row-level security | Supabase invite step is an admin action (`build-plan-2026-11-12/02`); OWASP A02 Security Misconfiguration; `security-review` skill, step 1; Keep Your App Safe Checklist (source 11) | Foundation, before the first deploy | Proposed |
| If a secret key ever reaches GitHub, make a new key in Supabase right away. Deleting the file is not enough, because GitHub keeps the history. (Added 2026-11-15) | The repository is public, so a leaked key can be read by anyone, and it stays in the history | Keep Your App Safe Checklist (source 11) | Always | Fact (course checklist) |
| Use fake data only while building in Week 4: made-up names, numbers and notes. (Added 2026-11-15) | Real health information must not reach a public project or a free plan with no backups | Week 4 requirement 7; Keep Your App Safe Checklist, "Use fake data only" (source 11) | Week 4 | Fact (course requirement) |
| No ad, analytics or tracking scripts on any page | Health data reaching ad companies, which every lawsuit and FTC case found is about | Risk profile | Always | Approved (risk profile) |
| Sign-in through Supabase Auth with cookie sessions, checked by the web server on every request | Someone using another person's account | Box 3; OWASP A07 Authentication Failures | Foundation | Approved (box 3) |
| HTTPS everywhere, and data encrypted at rest | Data read in transit or from disk | Vercel: AES-256 at rest, TLS 1.3 in transit (source 19); Supabase: AES-256 at rest and TLS in transit (source 61) | Provided by the vendors | Fact |
| Deleting a person deletes the health data entered about them | Keeping data the law says must be deleted on request | Risk profile, "Deletion" | Foundation | Approved (risk profile) |
| Errors show a plain message and never show data or keys. When a check fails, access is denied, not allowed. | Leaks through error messages, and checks that fail open | OWASP A09 and A10; `security-review` skill, step 8 | Every feature | Proposed |
| Package versions are locked, and `npm audit` runs before each merge | A bad or hacked package | OWASP A03 Software Supply Chain Failures; `security-review` skill, step 4 | Foundation | Proposed |
| An access log: who viewed or changed which health note, and when. Members can't edit it. | Not knowing who saw a parent's health data, or being unable to check after a breach | OWASP A09 Security Logging and Alerting Failures; the earlier draft risk profile's audit trail. Owner decision, 2026-11-12. | Foundation | Approved (owner, 2026-11-12) |
| A breach plan: who checks, and how people are told within 60 days | Missing the FTC notice deadline if health data is shared without permission | Risk profile, FTC rule (16 CFR 318) | Before real caregiver data | Proposed |

### How each rule is checked (project skills)
| When | Skill | What it does |
|---|---|---|
| Before building a feature that takes input or health data | `owasp-secure-coding-bdd` | Writes secure-behavior scenarios (Given/When/Then) for that feature |
| Before each commit or PR | `security-review`, and the `arch-gate` commit hook | Checks the code against OWASP 2025 and the risk profile |
| After a security finding | `writing-security-tests` | Writes one real test that proves the fix |
| Before launch | `data-lifecycle-compliance` | Lists the personal data and finds gaps in keeping, sharing and deleting it |

### Open items for this box (owner's call)
- **Two-step sign-in** (a code on top of a password) for caregivers. It isn't in the risk profile. Ask in Week 5.
- **The lawyer questions** (whose consent is valid; California's medical privacy law) stay open. The consent rules above are built so a lawyer's answer can be added without a rebuild.

---

## 5. Development operations (Approved by the owner, 2026-11-15, without branch protection)

What the course asks for: "Development operations are the ways that you gate check the cake... That is the quality check that happens without a human. And every time I introduce a new piece of code to the code base... there are checks" (lecture 49:08 to 49:38). The board's template lists "dev operations (CI/CD checks, security, auto testing, etc.)" (board text node 2980:3163). Taught in depth in Week 6 (lecture 48:40). Box 6 says which tests to write. This box says when the checks run and how code reaches users.

### How code reaches users
| Step | What happens | Source | Tag |
|---|---|---|---|
| 1. Branch | Each piece of work gets its own branch from `main` | Project rule: one deliverable = one branch = one PR (`CLAUDE.md`) | Approved (project rule) |
| 2. Checks on every commit | The `arch-gate` hook blocks a commit if the structure check fails. `security-review` runs before code with keys or personal data is committed. | `CLAUDE.md` (hooks in `.claude/settings.json`); box 4 | Fact (already set up) |
| 3. Pull request | Automatic checks run on GitHub: build, tests (box 6) and a package audit (box 4). The owner reads the results before merging. Branch protection (blocking a merge when a check fails) is not used for now. | Lecture 49:24; live Week 5 page: "You do not need branch protection, because you are on GitHub's free plan" (source `11-course-facts-live-weeks.md`) | Approved (owner, 2026-11-15) |
| 4. Preview | Vercel builds a preview copy of the app for every push, to look at before merging | Vercel: "Preview deployments for every push" (source 07) | Fact |
| 5. Merge | The owner merges. Vercel then deploys `main` to the live site. | Vercel: "Production deployments for the most recent changes from the production branch" (07); project rule | Fact / Approved |
| 6. Undo | Roll back to the last good version | Vercel: "Instant rollbacks" (07) | Fact |

### Database changes
| Rule | Why | Source | Tag |
|---|---|---|---|
| Every table change is a migration file kept in GitHub, and is never made by hand in the dashboard | Changes are reviewed in the PR and can be repeated on a new project | Supabase: `supabase migration new` and `supabase db push` (source 09) | Proposed |
| Row-level security rules live in the same migration files | Security rules get reviewed like code | Box 4 | Proposed |
| Supabase Pro backups (7 days) are on before any real caregiver data | Recovery if a change goes wrong | Box 1; Supabase backups (57) | Approved (box 1) |

### Settings and keys
| Rule | Source | Tag |
|---|---|---|
| Keys live in Vercel's environment settings, with separate values for preview and production | Vercel environments page (08); box 4, admin key rule | Proposed |
| Fake data only in every copy of the app while building in Week 4 (local, preview and live). Real caregiver data waits for later. | Week 4 requirement 7 (source 11); risk profile (health data) | Fact (course requirement) |

### Build order
1. GitHub repo and branch rule, then connect Vercel (preview and production).
2. The Supabase project with migrations in the repo.
3. The automatic PR checks, before the first feature PR.
4. Pro backups on, before real caregiver data.

### Open items for this box
- **Where the PR checks run.** GitHub Actions is the course's choice. The live Week 5 page asks for "A CI/CD pipeline on GitHub Actions in your repository, that runs automatically on every code push" (source `11-course-facts-live-weeks.md`). Approved with this box on 2026-11-15. (Updated 2026-11-15. The earlier text said this was general knowledge and not checked.)
- **Branch protection: decided 2026-11-15.** The owner approved box 5 without it. The checks still run on every pull request, and the owner decides when to merge. Revisit if a second person starts merging or a failed check is ever merged by mistake.
- **Watching the live app** (alerts when it breaks) belongs to the `operational-readiness` skill before launch, not to this week.

---

## 6. Quality engineering (Approved by the owner, 2026-11-15, as drafted)

What the course asks for: quality engineering is "the overarching topic." It asks whether a change has broken anything, whether it will break something, and whether it falls back to worse functionality than before (lecture 49:43 to 50:19, `Resources/Week 2_3/Lecture_Transcripts/Week 2_Lecture_Transcript.md`). It is decided in the non-functional requirements before anything is built. The board's box is named "Quality engineering architecture" (board node 3079:14601). Box 5 says when the checks run. This box says what they check and how many tests of each kind to write.

### What the checks try to catch
| What to catch | The course's example | Source | Tag |
|---|---|---|---|
| New bugs | The first time you tap Save, nothing happens. | `Resources/Week_5/Week 5 - Enterprise QA Lecture Notes (Notion copy 2026-11-13).md`, "What You Try to Catch" | Fact |
| Regressions | A new filter breaks the old sort that worked last week. | Same | Fact |
| Drift from the architecture decisions | A screen talks straight to the database when the decision said never to. | Same. The project's `arch-gate` and `judge-arch` already check this (`CLAUDE.md`). | Fact |
| Unexpected behavior, errors and failed links to other systems | Saving an expense sends an email nobody planned. | Same | Fact |
| Confusing steps, poor layout, slow screens | Five taps to add one expense, text cut off on a phone. | Same | Fact |

### How many tests of each kind
| Level | What it checks | How many | Source | Tag |
|---|---|---|---|---|
| Unit | One small piece of code on its own. | The most. They are fast and cheap. | Week 5 lecture notes, "Martin Fowler's Testing Pyramid" | Fact |
| Integration | The connection between one system and another. | Fewer. | Same | Fact |
| End to end | A whole sequence through every layer. | The fewest. Do not automate many, because they slow every push. | Same | Fact |
| Where our rules go | The consent check, care circle access and deletion from the Epic 3 scenarios are checked at the lowest level that can prove them. | | `task-pages-epic-3-2026-11-15.md` | Proposed |

### Who does the checking
| Who | What they do | Source | Tag |
|---|---|---|---|
| Scripts and robots | Unit tests, regression tests, smoke tests and the pull request checks, run automatically. | Week 5 lecture notes, "Who Does QA?" | Fact |
| A person (the owner) | Judgment checks on the live app: confusing screens, layout, phones. | Same | Fact |

### What Week 5 requires from us
| Requirement | Source | Tag |
|---|---|---|
| Automatic checks run on every push, with at least 3 checks. | `Resources/Week_5/Week 5 Coding Challenge - Build a CI - CD Pipeline (Notion copy 2026-11-13).md`, "Before You Submit" | Fact |
| The checks come from our own use cases and BDD scenarios. | Same, Basic Homework item 2 | Fact |
| The Week 1 Claude Skills are checked on every push, so a push that breaks them does not pass. | Same, item 3 | Fact |
| A check that should fail must actually fail. | Same | Fact |
| Two test case scenarios run by hand on the live app, with pre-conditions, steps, expected results and what actually happened. | Same, item 4, and the Test Case Scenario Template | Fact |
| Fake data only in every copy of the app. | Week 4 requirement 7 (source `11-course-facts-live-weeks.md`) | Fact |
| The two scenarios to run by hand: the parent agrees to a safer move (3.1.2, Scenario 1) and consent is not recorded (3.1.2, Scenario 3). | `task-pages-epic-3-2026-11-15.md` | Proposed (owner approved the box as drafted) |

### Build order (the course's seven steps)
1. Build the requirements, functional and non-functional. 2. Write the BDD scenarios, use cases and test cases. 3. Write the code. 4. Run the pull request checks. 5. Run all other kinds of QA testing. 6. Analyze and document the results. 7. Write new requirements for the next changes. (Week 5 lecture notes, "How to Perform Enterprise QA.")

### Open items for this box
- **Which tools run the tests.** The board says not to write technical requirements yourself. The developer role (Claude Code) names the test tools. This box does not.
- **A coverage threshold.** The course says teams often set a line the tests must not drop below. None is set. Ask the developer role before choosing one.
- **The lecture says quality engineering is taught in Week 6.** The course notes cover it in Week 5. The weeks shifted by one, so the Week 5 pages were used.
