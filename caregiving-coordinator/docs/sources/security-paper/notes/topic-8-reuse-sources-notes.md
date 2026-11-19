# Notes: Topic 8 reuse sources (batch 6): Supabase RLS and shared responsibility, FTC Health Breach Notification Rule, HHS health apps page, the risk profile and tasks T4.1 to T4.3

- **Read on 2026-11-18, by me directly in this chat (no helper agent).** Retrieval date for the saved copies is the date each file says it was fetched (2026-11-12 or earlier, see each source). Pages are cited by heading because web pages have no page numbers.
- **Label:** Supabase pages are vendor documentation (what Supabase says its product does). The FTC and HHS pages are U.S. government guidance, tier 1. None of this is legal advice. Nothing here says the proposed caregiving coordinator is "compliant" or "secure."
- **Recheck on 2026-11-18** (plain `curl -L`, no faked headers): the two Supabase pages loaded. The HHS and FTC pages returned HTTP 403 to curl and were **not rechecked**; I did not work around the block. The saved copies from 2026-11-12 are what was read.

## Source 1: Supabase, Row Level Security guide
- **Reference (APA 7, ready):** Supabase. (2026, November 3). *Row Level Security*. Supabase Docs. https://supabase.com/docs/guides/database/postgres/row-level-security
- **Local copy:** `caregiving-coordinator/docs/sources/build-plan-2026-11-12/06-supabase-rls.html` (page says "Updated Nov 3, 2026"). **Recheck:** the live page's modified date is still 2026-11-03.
- **Read:** the whole page text (about 5,700 words including SQL samples and the test file examples).

| What the page says (my words) | Heading |
|---|---|
| A table in an exposed schema with row level security (RLS) off can be read and written by any role that has a grant on it. The guide says to turn RLS on for every such table. | Intro |
| Postgres runs two checks: grants decide whether a role may do an operation at all, and policies decide which rows. Both must be set. Adding policies does not remove default grants, so a table protected only by policies can still hand `anon` an insert path. | Grants and policies |
| A policy works like an extra WHERE clause on every query. | What a policy does |
| `anon` is a request with no signed-in user; `authenticated` is a signed-in user. `service_role` skips RLS, so it must stay on the server. | Authenticated and unauthenticated roles |
| Views skip RLS by default. A view over a protected table can hand out every row. On Postgres 15 and above, `security_invoker = true` makes a view obey the table's policies. | Views and RLS; Expose a view safely |
| The procedure for every table: turn RLS on, set grants, write one policy per operation, write a test file that checks allow and deny for each operation and for `anon` and `authenticated`, then run `supabase test db`. "Until the suite passes, you don't know whether the policies do what you intended." (paraphrase of the guide's own sentence) | Secure a table with RLS |
| A denied write that matches zero rows raises no error, so a test must also check the target row is unchanged. `lives_ok` must not be used to prove an allowed write. | Policy tests |
| `auth.uid()` returns null when nobody is signed in, so a policy that only compares it to a column silently fails for signed-out users; check for null on purpose. | RLS reference, `auth.uid()` |
| Do not base policies on `user_metadata`, because signed-in users can change it. `app_metadata` cannot be changed by the user. A JWT is not always current: removing a user from a team is not seen until their token refreshes. | RLS reference, `auth.jwt()` |
| `security definer` functions run with their creator's rights and can skip RLS, so pin `search_path` and never put one in an exposed schema. | Use security definer functions |
| Two tables whose policies read each other fail with an "infinite recursion" error. Sharing features (lists and members) produce exactly this shape; the guide shows a `security definer` helper in a private schema as the fix. | Avoid recursive policies |
| A secret key bypasses RLS only when the request carries no user token. Never use it in the browser. | Bypassing Row Level Security |

## Source 2: Supabase, Shared responsibility model
- **Reference (APA 7, ready):** Supabase. (2026, October 6). *Shared responsibility model*. Supabase Docs. https://supabase.com/docs/guides/deployment/shared-responsibility-model
- **Local copy:** `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/17-supabase-shared-responsibility.html` (says "Updated Oct 6, 2026"). **Recheck:** the live page's modified date is now **2026-11-16**, so the page changed after the saved copy. The saved text was read; the new text was not diffed. Batch 5 notes (`caregiving-coordinator/docs/sources/security-paper/notes/upguard-supabase-and-rls-notes.md`) say the live wording was the same as the repository's copy, with only the date changed.
- **Read:** the whole page text (about 1,400 words).

| What the page says (my words) | Heading |
|---|---|
| The customer is always responsible for their Supabase account, access management, their data and applying security controls. | Top summary |
| Supabase gives full access to the database. If access is shared with team members or the public, the customer must manage the access levels. The customer also owns table access for sensitive data and the safe storage of database secrets and API keys. | You share the security responsibility |
| Supabase "recommended that you always apply Row Level Security" and sends alerts through the Security Advisor; applying the advice is the customer's job. | Same section |
| The customer is responsible for their own architecture, for third-party services they connect (sign-in providers, email and SMS senders, outside API calls), and for tuning and sizing their database. | Next sections |
| Supabase says its environment is SOC 2 compliant and points to a SOC 2 responsibilities document. This is the vendor's own claim. | SOC 2 and compliance |
| For health data (PHI): the customer must sign a Business Associate Agreement (a HIPAA add-on, on the Team Plan or higher), mark projects as HIPAA projects, turn on multi-factor sign-in for all accounts, turn on point-in-time recovery, SSL enforcement and network restrictions, keep connection logging on, and not keep PHI in public storage buckets. Data is encrypted at rest and in transit by Supabase. | Managing healthcare data |

## Source 3: FTC, Health Breach Notification Rule (rule page and Federal Register notice page)
- **References (APA 7, ready):** Federal Trade Commission. (2024, May 30). *16 CFR Part 318: Health Breach Notification Rule*. https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-318-health-breach-notification-rule . Federal Trade Commission. (n.d.). *Health Breach Notification Rule*. https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule
- **Local copies:** `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/44-ftc-hbnr-rule-page.md` (fetched 2026-11-12; page metadata modified 2026-09-09) and `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/03-ftc-hbnr-final-rule-fr-notice.md` (page dated May 30, 2024, matter number P205405). **Recheck:** blocked (HTTP 403), not rechecked.
- **Read:** both files in full. The rule page is a summary and a list of links; the rule text itself is at ecfr.gov (`caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/23-ecfr-16-cfr-318.html`, **not read in this batch**).

| What the pages say (my words) | Page |
|---|---|
| The rule requires vendors of personal health records and related entities to tell consumers after a breach of unsecured information. A service provider who has a breach must tell the entity, which tells consumers. The rule sets the timing, method and content of notice, and requires notice to the media for certain breaches of 500 or more people. | Rule page, Rule Summary |
| The page lists a September 9, 2026 FTC press release, "FTC Withdraws Obsolete Policy Statement." That release is not read. | Rule page, Press Releases |
| The Federal Register notice page holds only a title, date, tags and a link to the rule text. | Notice page |

## Source 4: FTC business guidance, "Complying with FTC's Health Breach Notification Rule"
- **Reference (APA 7, ready):** Federal Trade Commission. (2024, July). *Complying with FTC's Health Breach Notification Rule*. https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0
- **Local copy:** `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/04-ftc-complying-with-hbnr.md` (fetched 2026-11-12; page dated July 2024; a note says it was edited January 2025 for penalty amounts). **Recheck:** blocked (HTTP 403), not rechecked.
- **Read:** the whole file (about 3,900 words).

| What the page says (my words) | Heading |
|---|---|
| Many companies that collect health information (fitness trackers, diet apps) are not covered by HIPAA. The FTC enforces the rule for businesses and nonprofits not covered by HIPAA. The July 2024 amendments make clear that makers of health apps and connected devices must comply. | Intro |
| The rule covers vendors of personal health records, "PHR related entities" and third-party service providers. A personal health record is an electronic record of health information that can draw information from multiple sources and is managed by or for the person. A health app that collects consumer information and can sync with a fitness tracker is probably a vendor of personal health records. | Who's covered |
| The trigger is an "unauthorized acquisition" of unsecured, identifiable health information. A breach is not limited to hacking: sharing health information without the person's authorization is also a breach. Information counts as identifiable if it could reasonably identify someone even without a name. | What triggers the notification requirement |
| Where there was unauthorized access, unauthorized acquisition is presumed unless the company can show it did not or could not reasonably have happened (for example a policy that employees who open a record by mistake must not read it, must log out and must report it). | Answers to questions |
| Notice goes to each affected person without unreasonable delay and within 60 calendar days of discovery, to the FTC (for 500 or more people at the same time; for fewer, within 60 days after year end) and to the media when at least 500 residents of one state are affected. | What to do if a breach occurs |
| Notice to people must be clear, and email notice must also be paired with a text, in-app message or banner. The notice must say what happened, what information was involved, steps people can take, what the company is doing, and two or more ways to contact it. | How to notify; What information to include |
| A company that is only a HIPAA business associate is outside this rule. One that is also a consumer health record service may face both the FTC rule and the HHS rule. | Answers to questions |
| Penalty: "up to $53,088 per violation" (amount as edited January 2025). | Answers to questions |

## Source 5: HHS, "Resources for Mobile Health Apps Developers"
- **Reference (APA 7, ready):** U.S. Department of Health and Human Services, Office for Civil Rights. (2026, April 22). *Resources for mobile health apps developers*. https://www.hhs.gov/hipaa/for-professionals/special-topics/health-apps/index.html
- **Local copy:** `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/02-hhs-health-apps.md` (fetched 2026-11-12; "Content last reviewed April 22, 2026"). **Recheck:** blocked (HTTP 403), not rechecked.
- **Read:** the whole file (about 380 words). It is a list of links with one-line descriptions.

| What the page says (my words) | Heading |
|---|---|
| Privacy and security protections are sometimes required by federal and state laws, including the HIPAA Privacy, Security and Breach Notification Rules. | Intro |
| The FTC, with HHS, ONC and the FDA, offers a Mobile Health Apps Interactive Tool that asks about an app's function, data and services and points to laws that might apply (FTC Act, the Health Breach Notification Rule, HIPAA, the FD&C Act, COPPA, the Cures Act). | First link |
| A separate HHS guide ("Health App Use Scenarios and HIPAA," 2016 PDF) explains when an app developer may be a business associate. It is **not read in this batch** (saved as `caregiving-coordinator/docs/sources/laws-consent-research-2026-11-12/sources/01-hhs-app-developer-scenarios-2016.md`). | Second link |

## Source 6: the proposed coordinator's own files
Read in full: `caregiving-coordinator/docs/risk-profile.md` (Approved by the owner 2026-11-12) and tasks T4 in `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md` (T4.1 to T4.3, lines 62 to 80). **Not read in this batch:** the sections of `caregiving-coordinator/docs/build-plan-nfr-draft-2026-11-12.md` those tasks cite.

| Link between a source and the proposed coordinator | Where |
|---|---|
| Risk profile: "Row-level security on every table with health, money or consent data." It cites the Supabase shared responsibility page as the reason. The Supabase RLS guide says the same and adds grants, tests, views and recursion traps (Source 1). | `caregiving-coordinator/docs/risk-profile.md`, "Risks to check on every relevant change" |
| Risk profile: under the FTC rule, unauthorized sharing counts as a breach needing notice within 60 days; the rule covers "personal health record" apps; a data-pulling feature can make the product one; adding one is "a High finding." This matches Source 4. | Same section |
| Risk profile open question 3: HIPAA is "probably not covered"; an app serving consumers directly is "not likely" covered, but it depends on the facts and changes if work starts for a doctor, hospital or health plan. Source 5 is the HHS page about this, but it only links to the scenarios guide, which was not read in this batch. | `caregiving-coordinator/docs/risk-profile.md`, "Open questions" 3 |
| T4.1.1 (members see only their own circle) and T4.1.3 (an access log nobody can edit): these are what RLS policies and the Supabase checks in Source 1 would enforce; the guide's sharing and recursion section matches the care-circle shape. | `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`, T4.1 |
| T4.2.1 and T4.2.2 (admin key on the server only; replace a leaked key): Source 1 says a secret key skips RLS and must never be in the browser; Source 2 says the customer must store keys safely. | Same file, T4.2 |
| T4.2.4 says data is encrypted at rest and in transit "which the vendors provide." Source 2 says Supabase encrypts at rest and in transit and suggests the customer "can consider" encrypting at the application layer. | Same file, T4.2.4 |
| T4.3.3 (a breach plan with a 60-day notice before any real caregiver data) matches the 60-day rule in Source 4. | Same file, T4.3.3 |

## Useful for the paper (topic 8)
- Supabase's own page puts access to tables and keys on the customer, so the proposed coordinator needs its own row-level security, tests and key handling. It does not get them automatically.
- The FTC guidance supports a clear breach plan and shows that sharing health data without permission can itself be a breach.
- Supabase's HIPAA section lists what a customer must do to store PHI there (BAA, Team Plan, MFA and more). Whether HIPAA applies to the proposed coordinator at all is an open question in the risk profile.

## Limits and cautions
- Not legal advice. The risk profile itself says open questions need a lawyer.
- The Supabase pages are the vendor's description of its product. Supabase's SOC 2 and "HIPAA" statements are vendor claims, not our claims.
- The HHS and FTC pages could not be rechecked on 2026-11-18 (HTTP 403 to curl). The FTC page's September 9, 2026 withdrawal press release and the rule text at ecfr.gov were not read.
- The Supabase shared responsibility page changed on 2026-11-16, after the saved copy.

## Not read
The ecfr.gov rule text, the Federal Register rule (files 38 and 39), the HHS 2016 scenarios guide (file 01), the FTC press and case files, and the build plan sections cited by T4. The other laws research files (state laws and cases) were not part of this batch.
