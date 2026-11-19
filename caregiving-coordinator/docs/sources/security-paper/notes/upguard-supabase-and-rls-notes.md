# Notes: UpGuard's Supabase study, Wiz on Moltbook, and Supabase's own RLS and key docs

All pages were fetched with plain `curl -L` on 2026-11-18 (retrieval date). The HTML is the saved copy; a `.txt` text extract sits beside each file so you can open it fast. Folder: `caregiving-coordinator/docs/sources/security-paper/upguard-supabase-study/`.

**Page numbers:** these are web pages with no page numbers. I cite the heading instead.

**Product framing:** the coordinator is a proposed product idea, not built. Nothing here says it is secure or compliant.

---

## Source 1: UpGuard study

- **Reference (APA 7):** Pollock, G. (2026, September 23). *Everything everywhere: Systemic data exposure in Supabase apps*. UpGuard. https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps
- **Tier:** vendor research (tier 3). UpGuard sells security ratings and a product that scans for this kind of exposure (it says so in the last lines). Author title on the page: Director of Research and Insights. Listed reading time: 11 minutes.
- **Local copies:** `upguard.html` (325,801 bytes) and `upguard.txt`.
- **What I read:** the whole article text (background, prior research, methodology, all tables, the five case studies, conclusion). **I could not see the interactive 3D map**, because it is drawn by JavaScript. Its tables are in the page HTML, and I read those.

### What the page says (my words)

| What the page says | Source and heading |
|---|---|
| UpGuard found **16,326** Supabase databases "exposing readable tables." It calls this "the largest study of its kind." | Intro; "A City and Its Mirror" |
| How it found them: it fingerprinted sites that use Supabase by looking for Supabase key names and database addresses in public JavaScript files. It used two data sources from other scanners: BuiltWith and the Chrome UX Report dataset on BigQuery. | "Prior Research and Methodology" |
| It gathered about **300,000** unique domains with signs of Supabase use. It then asked each one for a table named "users". The database answered one of three ways: no data (blocked, or database gone), a hint naming a different readable table, or a page of results. | "Prior Research and Methodology" |
| It looked only at standalone sites on their own domains, not apps inside vibe-coding platforms (such as Lovable or Replit), so it would include sites made with Claude Code and Codex. | "Prior Research and Methodology" |
| It did not read every row. It judged data types from the table schemas (column names). It looked at "a handful" of cases more closely and told the owners of the significant ones. | "Distribution of data types"; "Exposed Data" |
| Data types, share of the 16,326 databases: any personal info 55.8% (9,104); person name 42.8% (6,981); email 38.8% (6,329); phone 25.8% (4,216); address 16.0% (2,619); payment system 12.1% (1,974); hard credential 9.7% (1,582); password or PIN 8.2% (1,336); date of birth 3.6% (584). | Table "Types of data exposed" |
| UpGuard says "payment system" means a payment service is hooked up (mostly Stripe or PIX reference IDs and billing data), not card numbers. It says "a very small number" had plausible card data. | Note under that table; "Distribution of data types" |
| Medical and health sites: 558 databases. 53.4% had any personal info, 11.6% had a payment signal, 7.5% had password columns, 10.0% had credential columns. 69.7% served consumers (B2C). | Tables "Audience mix by industry" and "Exposure by industry" |
| Operator region: no country could be tied to 7,794 (47.7%); Europe and Central Asia 2,302 (14.1%); Latin America 1,449 (8.9%); South Asia 1,263 (7.7%); North America 1,226 (7.5%); East and Southeast Asia 887; Africa 784; Middle East 445; Oceania 176. | Table "Exposed databases by operator region" |
| **Cause, in UpGuard's words (my paraphrase):** the exposure comes from configuration mistakes by people or their AI coding agents. It says the simplest form was databases "lacking a control to prevent any user from querying the database" (row-level security off). It also lists policies that exist but do not limit access enough, and public keys used as if they were secret keys. | "Background" |
| UpGuard says Supabase has since made tables created in the Table Editor have RLS on by default. Tables made through the API, "which is how coding agents interact with Supabase," do not get RLS on by default. Having RLS on is not enough; it must be set up and the keys used right. | "Background" |
| UpGuard says "Supabase misconfigurations" and does not call it a Supabase flaw. It does compare Supabase to Amazon S3 and GitHub: products whose easy-to-use defaults led to mass exposure and were later changed. It argues it is "time to rebalance the equation." | "Background"; "Conclusion" |
| It says the exposure rates were about the same for business sites and consumer sites, because the people building them "do not understand their database's configuration." | "Consumer and supply chain risk" |
| Five cases: an Indian adult-content site with 65,467 users in the table (driver's license, passport, payout account details) and over 100,000 private messages; a Philippines OTP service (over 2,000 users, over 100,000 SMS messages); a US valet service (over 100,000 customers); an African consulate (25,000 users, including a field for emergency housing location); a Canadian immigration service (nearly 5,000 records, 884 with a plain-text password). | "Exposed Data" (case headings) |
| Earlier studies it lists: Modern Pentest, 107 Y Combinator startups scanned, 28% exposed personal data; Symbiotic Security, 1,072 apps, 39 with readable tables; Escape, about 1,400 apps, 175 databases leaking personal data; Red Access, 380,000 URLs, 5,000 apps, 2,000 exposing sensitive data. | "Prior Research and Methodology" |
| Dates it gives: Lovable misconfiguration reported March 2025 (CVE-2025-48757); Wiz found Moltbook "in February of 2026"; Supabase valued at $10 billion as of June 2026. | "Background"; "Prior Research and Methodology" |
| **Did Supabase respond?** The article does not say. It does not quote Supabase, and does not say UpGuard contacted Supabase. It says only that UpGuard notified owners of significant exposures. | Whole article (checked for this) |

### Useful for the paper
- Topic 5 (risks): a real, large example of what turning RLS off (or never setting it up) leads to. 55.8% of exposed databases showed personal-info columns; health-site databases are 558 in the study.
- Shows the hole is in the app's setup, which is the point of the project rule "every table with health, money or consent data has RLS turned on."
- Good for a point about AI coding agents: UpGuard says API-made tables do not turn RLS on by default.
- Case studies show harm to vulnerable people (a consulate, immigrants), which matches the caregiving data's sensitivity.

### Limits and cautions
- Vendor research (tier 3). It is self-reported; the method and data are not published for anyone to repeat. UpGuard also sells exposure scanning.
- 16,326 is a **count of exposed databases it found**, not a rate. It does not say how many Supabase projects exist, so you cannot say "X% of Supabase projects are exposed." The article gives no such number.
- It probed for a "users" table, so the personal-info share is skewed upward (the article says so).
- Data types come from column names, not from reading real rows (except a few cases). A column called "password" is not proof of real passwords.
- The cause statement is UpGuard's view. It did not (in this article) test why each owner left RLS off.
- Medical and health databases are a small slice (558 of 16,326). It does not say these were health records of the kind in the proposed coordinator.
- Includes a 2026 date; the article is two months old on the retrieval date.

### Not read / not found
- The interactive 3D map (needs JavaScript). Its data tables were in the page and were read.
- No Supabase response was found in this article. I did not search for one outside it.

---

## Source 2: Wiz on Moltbook

- **Reference (APA 7):** Nagli, G. (2026, February 2). *Hacking Moltbook: The AI social network any human can control*. Wiz. https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys (The browser tab title reads "Hacking Moltbook: AI Social Network Reveals 1.5M API Keys.")
- **Tier:** vendor research (tier 3). Wiz is a cloud security vendor.
- **Local copies:** `wiz-moltbook.html` (488,337 bytes) and `wiz-moltbook.txt`.
- **What I read:** the whole post text, including the disclosure timeline. I did not view the images (screenshots inside the post).

### What the page says (my words)

| What the page says | Source and heading |
|---|---|
| Wiz found a misconfigured Supabase database belonging to Moltbook, with "full read and write access to all platform data." Exposed: 1.5 million API authentication tokens, 35,000 email addresses, and private messages between agents. | Intro; "Executive Summary" |
| Wiz did a "non-intrusive" review by browsing like a normal user. Within minutes it found a Supabase API key in client-side JavaScript that gave anyone, without signing in, access to the production database (read and write, all tables). | "Executive Summary" |
| Wiz says finding the key "does not automatically indicate a security failure." Supabase is designed so some keys are visible to the client. With RLS set up, the public key "is safe to expose" and works like a project identifier. Without RLS policies it gives full database access. | "Discovery of Exposed Supabase Credentials" |
| **Cause, in Wiz's words (my paraphrase):** "this critical line of defense was missing": RLS was not in place. Wiz's lessons section says it "traced back to a single Supabase configuration setting." Wiz does not call it a Supabase product flaw. | "Discovery of Exposed Supabase Credentials"; Lesson 1 |
| Test: a request to the REST API with the public key for the `agents` table returned data (names and API keys) when it should have returned an empty list or an error if RLS had been on. | "Unauthenticated Database Access via Supabase API" |
| Wiz used Supabase's PostgREST error hints and GraphQL introspection to map the tables and found about 4.75 million records. | "Database Enumeration Through PostgREST and GraphQL" |
| Data exposed: every agent's API key and claim token; 17,000+ owner emails; 29,631 more emails in a new `observers` table; 4,060 private message threads, some holding plain-text OpenAI API keys. | "Sensitive Data Exposed in the Moltbook Database" items 1 to 3 |
| Write access: after the first fix blocked reading, writing to public tables stayed open. Wiz edited a post as a test. It says this could allow content changes and prompt injection. | Item 4 "Write Access"; Lesson 4 |
| Moltbook had 1.5 million "agents" but about 17,000 human owners (88 to 1). | "Executive Summary"; Lesson 2 |
| Disclosure timeline (UTC): Jan 31, 2026 21:48 first contact; 22:06 reported the RLS misconfiguration; 23:29 first fix (agents, owners, site_admins); Feb 1 00:13 second fix; 00:31 found write access; 00:44 write access blocked; 00:50 found more tables; 01:00 final fix. The Moltbook team secured it within hours, with Wiz's help. Wiz says all data it accessed was deleted. | Intro; "Disclosure Timeline" |
| Fixing took several rounds, each showing more exposed tables (sensitive tables, then write access, then GraphQL-found tables). | Lesson 5 |
| Wiz says another researcher, Jameson O'Reilly, also found the misconfiguration, reported by 404 Media. Wiz says its post shares its own independent find. | Note near the end |
| Wiz suggests AI assistants that build Supabase backends "can enable RLS by default" and that deployment platforms scan for exposed credentials. | "Closing Thoughts" |

### Useful for the paper
- Topic 5: a named, dated case where a public key plus RLS missing meant the whole database was open, with read and write.
- Shows the difference between a public (publishable) key, which is fine, and a database with no RLS, which is not. This matches the Supabase docs in Source 3.
- The write-access point shows the risk is not only leaks but also changed data (for caregiving, a changed medication note or consent record).
- Timeline shows how fast a fix can happen once someone is told, and that fixes came in rounds.

### Limits and cautions
- Vendor research (tier 3), self-reported. Wiz also markets security products.
- It is one app, not a rate. It is also a social network for AI agents, not a health product.
- Wiz's dates differ slightly from UpGuard's: Wiz reported on Jan 31, 2026 and published Feb 2, 2026; UpGuard says "February of 2026." Use Wiz's own dates.
- The post is partly about hype ("1.5 million agents") and bots; only the Supabase part is relevant.
- The post contains a full publishable key and live URLs. I did not copy them into these notes and the paper should not either.

### Not read / not found
- Images and screenshots in the post were not viewed. The text next to them was read.
- Whether Supabase commented on Moltbook: not in this post.

---

## Source 3: Supabase's own docs

- **Tier:** official documentation from the tool's maker. It tells what the tool does and what Supabase says users should do. It is not an independent test of whether it works, and Supabase is describing its own product.
- **Retrieval:** 2026-11-18, page "Updated" dates are from each page.
- **Reading note:** each page's text was read, but long SQL code blocks and the lint pages for checks not about security (such as slow queries and unused indexes) were skimmed, not studied line by line.

### 3a. Row Level Security guide

- **Reference (APA 7):** Supabase. (2026). *Row Level Security*. Supabase Docs. https://supabase.com/docs/guides/database/postgres/row-level-security (retrieved 2026-11-18)
- **Local:** `supabase-rls.html`, `supabase-rls.txt`. The page shows no update date in the text I extracted.

| What the page says | Source and heading |
|---|---|
| A table in an exposed schema without RLS "is readable and writable by any role with a grant on it." The page says to enable RLS on every table in an exposed schema. | Intro |
| Postgres runs two checks: grants (can the role do this at all) and policies (which rows). Set both. | "Grants and policies" |
| On existing projects a new table in `public` starts with every privilege granted to `anon`, `authenticated` and `service_role`. Adding policies does not remove those grants. Not every project grants these automatically. | "Grants and policies" |
| `service_role` bypasses RLS, so it must stay on the server. | "Grants and policies" table; "Bypassing Row Level Security" |
| Once RLS is on, no data is available through the API with a publishable key until policies are created. | "Enable RLS and set the grants" |
| Four steps for every exposed table: enable RLS and set grants, write a policy per operation, write a test file for allow and deny, run `supabase test db`. "Until the suite passes, you don't know whether the policies do what you intended." | "Secure a table with RLS" |
| Views bypass RLS by default; a view over a protected table can hand out rows its policies were meant to hide. Use `security_invoker = true` (Postgres 15+). | "Views and RLS"; "Expose a view safely" |
| A policy `to anon using (true)` gives every signed-out visitor read access. Use only for public data. | "Authenticated and unauthenticated roles" |
| Do not base policies on `user_metadata`; signed-in users can change it. `app_metadata` cannot be changed by the user. | "auth.jwt()" |
| Secret keys bypass RLS only when the request carries no user token. | "Bypassing Row Level Security" |
| Never create a security definer function in an exposed schema; set `search_path = ''` on those functions. | "Use security definer functions" |
| For tables users share, tests should also check that a non-owner member is allowed and a non-member is denied. | "Policy tests" |

### 3b. Database Advisors (Security Advisor) and the lint list

- **Reference (APA 7):** Supabase. (2026). *Advisors* [Database linter and Security Advisor checks]. Supabase Docs. https://supabase.com/docs/guides/database/database-advisors (page "Updated Oct 2, 2026"; retrieved 2026-11-18)
- **Local:** `supabase-database-advisors.html`, `supabase-database-advisors.txt`. **The lint pages I asked for** (`database-linter?lint=0013_rls_disabled_in_public`, `...0007_policy_exists_rls_disabled`) **return the same single page**: every lint is a section on this one page. I did not save duplicate copies.

| What the page says | Source and heading |
|---|---|
| Advisors are "deterministic checks that ship with the platform." They can be run from Studio, MCP (`get_advisors`), CLI (`supabase db advisors`) or the Management API. | Top of page |
| Some findings may be intentional, so check against the schema and access model. | Top of page |
| Lint **0013, "rls disabled in public"** (level ERROR, "Table publicly accessible"): anyone with the project URL can read, edit and delete all data in the table because RLS is off. Fix: `alter table ... enable row level security`. The page says full public create, read, update and delete is "a critically unsafe configuration." | Section for 0013 |
| Lint **0007, "policy exists rls disabled"** (INFO): a policy exists but does nothing because RLS is not on. The page calls this a common mistake. | Section for 0007 |
| Lint **0008, "rls enabled no policy"** (INFO): RLS is on but no policies, so nothing can be read or written through the API. | Section for 0008 |
| Lint **0023, "sensitive columns exposed"** (ERROR): flags exposed tables with RLS off whose column names match patterns such as password, token, ssn, credit_card, health_record, medical_record, diagnosis. | Section for 0023 |
| Lint **0024, "permissive rls policy"** (WARN): policies like `using (true)` that defeat RLS. | Section for 0024 |
| Lint **0010, "security definer view"** (ERROR) and **0002, "auth users exposed"** (ERROR): views that ignore RLS or expose `auth.users`. Lint **0015, "rls references user metadata"** (ERROR). Lint **0012** warns about anonymous sign-ins sharing a role with permanent users. | Sections for 0010, 0002, 0015, 0012 |

### 3c. Securing your data

- **Reference (APA 7):** Supabase. (2026). *Securing your data*. Supabase Docs. https://supabase.com/docs/guides/database/secure-data (page "Updated Sep 3, 2026"; retrieved 2026-11-18)
- **Local:** `supabase-securing-your-data.html`, `.txt`.
- **URL note:** the address you gave, `/docs/guides/api/securing-your-data`, returns **404**. The page lives at `/docs/guides/database/secure-data`.

| What the page says | Source and heading |
|---|---|
| For front-end access via the Data API, data stays secure "so long as" you turn on RLS with least-privilege policies and use the publishable key. | "Frontend access" |
| The publishable key is "safe to expose with RLS enabled," because row access is checked against policies and the user's JWT. | "Frontend access" |
| Secret and service role keys are "never safe to expose" in the front end because they bypass RLS. Use them only on the backend, as sensitive environment variables. | "Never expose your service role or secret keys on the frontend" |

### 3d. Securing your API

- **Reference (APA 7):** Supabase. (2026). *Securing your API*. Supabase Docs. https://supabase.com/docs/guides/api/securing-your-api (page "Updated Oct 22, 2026"; retrieved 2026-11-18)
- **Local:** `supabase-securing-your-api.html`, `.txt`. (Not on your list; the RLS and data pages point to it, so I read it.)

| What the page says | Source and heading |
|---|---|
| Two layers: grants (which role can reach an object) and RLS (which rows). "Use both controls for every exposed object." | "Grants and RLS" |
| On existing projects, new objects in `public` get default privileges for `anon`, `authenticated`, `service_role`, which makes them reachable through the Data API "even when you don't intend to expose them." You can turn off "Automatically expose new tables." | "Default privileges" |
| "Supabase is changing the platform default to revoke these automatic grants so that exposure becomes opt-in." | "Default privileges" |
| Tables made in the Dashboard have RLS on by default. Tables made in the SQL Editor or other tools need RLS turned on explicitly. | "Enable RLS policies" |
| If an app never uses the Data API, it can be turned off. | "Disable the Data API" |

### 3e. API keys

- **Reference (APA 7):** Supabase. (2026). *API keys*. Supabase Docs. https://supabase.com/docs/guides/api/api-keys (page "Updated Nov 2, 2026"; retrieved 2026-11-18)
- **Local:** `supabase-api-keys.html`, `.txt`.

| What the page says | Source and heading |
|---|---|
| Publishable key (`sb_publishable_...`): low privilege, safe to expose in web pages and apps; it only reaches what RLS allows. Secret key (`sb_secret_...`): bypasses RLS and "must never leave your control." | "Which key do you use?"; "Key types" |
| Supabase is deprecating the `anon` and `service_role` keys "by the end of 2026" in favor of the new keys. | "Changes to API keys" |
| Policies never apply to a secret key, because `service_role` has the BYPASSRLS attribute. | "Postgres roles and Row Level Security" |
| What publishable keys do not protect against: code inspection, network inspector, XSS and CSRF, phishing, man-in-the-middle. For protection, RLS must be on for all tables, policies reviewed for `anon` and `authenticated`, and the Security Advisor findings reviewed. | "What publishable keys don't protect against" |
| Where a secret key must never appear: web page, source control, browser (even localhost), chat, email, URL. Use a separate secret key per backend component, and rotate a leaked key. | "Handling secret keys safely" |
| A secret key does not work in a browser: Supabase returns 401 when the User-Agent looks like a browser. But "an attacker can still use the key from other tools." | "Secret keys and elevated access"; "Limiting the damage of a leak" |

### 3f. Shared responsibility model

- **Reference (APA 7):** Supabase. (2026). *Shared responsibility model*. Supabase Docs. https://supabase.com/docs/guides/deployment/shared-responsibility-model (page "Updated Nov 16, 2026"; retrieved 2026-11-18)
- **Local:** `supabase-shared-responsibility.html`, `.txt`.

| What the page says | Source and heading |
|---|---|
| "You are always responsible for": your Supabase account, access management (account, database, tables), data, and applying security controls. | Top of page |
| The user is responsible for making sure tables with sensitive data have the right access level and for managing secrets and API keys. Supabase "recommended that you always apply" RLS. | "You share the security responsibility" |
| Supabase sends alerts through the Security Advisor, and "applying the recommendations are your responsibility." | "You share the security responsibility" |
| Supabase gives "very few guard-rails" around the database; that gives control but means "you can break things." | "You are in control of your database" |
| For health data (PHI): the user must sign a Business Associate Agreement (Team Plan or higher), mark projects as HIPAA projects and fix advisor findings, enforce MFA, turn on point-in-time recovery, SSL enforcement and network restrictions, keep connection logging on, and not store PHI in public Storage buckets. | "Managing healthcare data" |

### Overlap with files already in the repo
- `docs/sources/laws-consent-research-2026-11-12/sources/17-supabase-shared-responsibility.html` is the same page. Its text shows "Updated Oct 6, 2026"; today's copy shows "Updated Nov 16, 2026." I compared the body text (headings aside) and found **no difference in the wording**. Only the page date changed.
- `18-supabase-hipaa-projects.html` and `61-supabase-security-page.html` are about HIPAA projects and the security page; I did not compare them. The RLS guide, Advisors, Securing your data/API and API keys pages were **not** in the repo before.

### Useful for the paper
- Topic 5 and 8: Supabase's own pages agree with UpGuard and Wiz on one point: a table in `public` without RLS is open to anyone with the project URL. They say turning RLS on and writing policies is the user's job (shared responsibility page). This supports the project rule.
- The "publishable key is fine, RLS is what protects data" point explains why the Wiz key was not itself the failure.
- Advisor lint 0013 (RLS off), 0023 (sensitive-looking columns) and 0024 (always-true policies) are named checks that could be run on the proposed coordinator's tables. The lint 0023 pattern list includes health words (health_record, medical_record, diagnosis).
- The policy-test steps (`supabase test db`) show how to test RLS, which fits a Topic 7/8 point about testing access rules.
- Tables made through the SQL Editor or other tools do not get RLS on by default, per Supabase and UpGuard. A migration-based project (as a Next.js plus Supabase project often is) must turn it on in the migration.
- The key-handling rules (secret key only on the server, never in the browser) fit the Next.js plus Vercel setup (the page's own `.env` example uses `NEXT_PUBLIC_` for the publishable key only).

### Limits and cautions
- Official docs describe the vendor's tool and advice. They do not prove any project is protected, and the advisor is a set of checks, not a full audit. The page itself says findings may be intentional and must be checked.
- Docs change often. These pages have different "Updated" dates (Sep 3 to Nov 16, 2026). Cite the retrieval date.
- The docs say the default grants differ by project age ("Not every project grants these automatically"). I did not check what a brand-new project does today.
- The shared responsibility page lists HIPAA duties for Supabase customers. It does not say a project is HIPAA compliant, and the paper must not say so either.
- A count of exposed databases in UpGuard is not a rate of all Supabase projects, and Supabase's docs do not give any such rate.
- UpGuard and Supabase agree on the default for API-made tables; I did not independently test it.

### Not read / not found
- Not read line by line: long SQL code samples and test-file code in the RLS guide and Advisors page, and the Advisors sections about slow queries, indexes, bloat and error rates. I read the section headings and Level, Summary and Ramification lines for all lints, and the rationale and fix text for 0007, 0013 and 0023, plus the first part of 0024 (the always-true patterns). For 0008, 0010, 0002, 0012 and 0015 I read only the Level, Summary and Ramification lines.
- Not requested and not fetched: the separate Supabase security page, HIPAA pages, "Rotate a leaked key" page, and the GitHub discussion about changing default grants.
- `https://supabase.com/docs/guides/api/securing-your-data` returned 404 (see 3c).
