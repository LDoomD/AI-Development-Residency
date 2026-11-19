# Notes: Next.js middleware / proxy authorization-bypass advisories (2025 and 2026)

- **Sources:** NVD records, GitHub Security Advisories (the vercel/next.js repository list and the GitHub Advisory Database), the Vercel postmortem and changelog, and two Next.js documentation guides. All fetched 2026-11-18 with plain `curl -L` (no changed headers).
- **Label for the paper:** vendor advisories and official vendor documentation (tier 1 for what the vendor says; NVD is the U.S. government database that copies and scores CVE data). These are facts about specific Next.js versions, not a rating of any product idea.
- **Local copies:** all in `caregiving-coordinator/docs/sources/security-paper/nextjs-middleware-advisories/`. Raw JSON: `nvd-CVE-*.json` (NVD API), `ghadv-CVE-*.json` (GitHub Advisory Database API), `repo-GHSA-*.json` (vercel/next.js repository advisory API), `repo-advisories-page1.json` (the full list of 79 published repository advisories). Pages: `nextjs-docs-authentication`, `nextjs-docs-data-security`, `nextjs-docs-proxy`, `nextjs-blog-cve-2025-29927` (this URL redirects to a vercel.com blog post), `vercel-changelog-may-2026` (each as `.html` plus extracted `.txt`).
- **Read in full (2026-11-18):** the full text of every advisory in the tables below (JSON text fields: summary, description, versions, CVSS, CWE, dates, credits), the NVD records for each, the postmortem, the Vercel May 2026 changelog, the Authentication guide (whole page, including all Server Component, Server Action and Route Handler sections) and the Data Security guide (read down to its Server Action "closures and encryption" section; later sections on environment poisoning and similar topics were skimmed, see "Not read").
- **Dates and "today":** the pages say they were last updated 2026-09-16 (Authentication guide) and 2026-11-18 (Data Security guide and Proxy page).

## The advisories

All affect the npm package `next`. "Patched" lists the first fixed version in each version line. CVSS is shown as the source shows it, and every one of these is CVSS v3.1 unless the row says v4.0. A CVSS score is a Base severity score, not a risk rating.

| CVE | GHSA | Dates (GitHub repository advisory published; NVD published) | Affected | Patched | CVSS (as shown) | CWE | Plain description |
|---|---|---|---|---|---|---|---|
| CVE-2025-29927 | GHSA-f82v-jwr5-mffw | 2025-03-21; 2025-03-21 | 12.x (from 11.1.4 per NVD), 13.x, 14.x, 15.x before the fixes | 12.3.5, 13.5.9, 14.2.25, 15.2.3 | v3.1 9.1 Critical, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N` | CWE-285 (GitHub); NVD also lists CWE-863 | If access checks happen in middleware, an outside request can skip them. |
| CVE-2026-44572 | GHSA-3g8h-86w9-wvmq | 2026-05-06; 2026-05-13 | 12.2.0 to before 15.5.16; 16.0.0 to before 16.2.5 | 15.5.16, 16.2.5 | v3.1 3.7 Low, `AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L` (GitHub). NVD's own score: v3.1 5.9 Medium, `...C:N/I:N/A:H` | CWE-349 | A fake internal header can make a middleware redirect unusable, and a caching CDN can then store the broken redirect. This is an availability problem, not an access bypass. Included because it is a middleware advisory in the same release. |
| CVE-2026-44573 | GHSA-36qx-fr4f-26g5 | 2026-05-06; 2026-05-13 | 12.2.0 to before 15.5.16; 16.0.0 to before 16.2.5 (Pages Router with i18n) | 15.5.16, 16.2.5 | v3.1 7.5 High, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | CWE-863 (GitHub Advisory Database); the repository advisory shows no CWE; NVD adds CWE-551 from a second source | A request for the page data file without the language prefix skips middleware, so protected page data can be read. |
| CVE-2026-44574 | GHSA-492v-c6pp-mqqv | 2026-05-06; 2026-05-13 | 15.4.0 to before 15.5.16; 16.0.0 to before 16.2.5 | 15.5.16, 16.2.5 | v3.1 8.1 High, `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N` | CWE-288 (NVD adds CWE-551) | Crafted query parameters change which dynamic route value the page sees while the visible path stays the same, so the middleware check does not match. Needs a low-privilege account (PR:L). |
| CVE-2026-44575 | GHSA-267c-6grr-h53f | 2026-05-06; 2026-05-13 | 15.2.0 to before 15.5.16; 16.0.0 to before 16.2.5 (App Router) | 15.5.16, 16.2.5 | v3.1 7.5 High, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | CWE-288 (NVD adds CWE-551) | Special `.rsc` and segment-prefetch URLs reach the same page without matching the middleware rule. |
| CVE-2026-45109 | GHSA-26hh-7cqf-hhc6 | 2026-05-07; 2026-05-13 | 15.2.0 to before 15.5.18; 16.0.0 to before 16.2.6 | 15.5.18, 16.2.6 | v3.1 7.5 High, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | CWE-288 and CWE-358 (GitHub Advisory Database); the repository advisory lists only CWE-288 | The fix for CVE-2026-44575 did not apply to `middleware.ts` when built with Turbopack. An incomplete-fix follow-up. |
| CVE-2026-64642 | GHSA-6gpp-xcg3-4w24 | 2026-07-21; 2026-07-27 | 16.0.0 to before 16.2.11 (App Router, Turbopack, exactly one entry in `i18n.locales`) | 16.2.11 | **v4.0** 8.3 High, `CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:L/VA:N/SC:N/SI:N/SA:N` (GitHub). NVD adds its own v3.1 8.2 High, `...C:H/I:L/A:N` | CWE-285 | Crafted requests can skip middleware/proxy authentication in that one configuration. |

**Why I added CVE-2026-44572 and CVE-2026-64642:** I listed all 79 published vercel/next.js repository advisories (`repo-advisories-page1.json`) and picked the 2026 ones whose title names Middleware or Proxy. Only these two were not already in the approved list. I left out other 2026 advisories (server actions, image optimization, caching, SSRF) because their titles are not about middleware or access bypass. CVE-2026-64643 ("Unauthenticated disclosure of internal Server Function endpoints") is access-related but I did not read its text, so I did not include it (see "Not read").

**CVE counts differ by source.** The Vercel changelog (2026-05-07) says the May release fixed 13 advisories and lists five as middleware and proxy items (four bypasses and the redirect cache issue). NVD lists these same CVEs with a later published date than GitHub (2026-05-13 against 2026-05-06). The GitHub Advisory Database shows 2026-05-11 for the four 2026 advisories I fetched from it, which also differs from the repository date.

## What the pages say (my words)

| What the pages say (my words) | Source and section |
|---|---|
| The 2025 bug let an outside request skip an access check if the check lived in middleware. The advisory says Next.js sites hosted on Vercel were "automatically protected." | GHSA-f82v-jwr5-mffw, Impact and Patches (note) |
| The workaround for 2025 was to block outside requests that carry the internal `x-middleware-subrequest` header before they reach Next.js. | GHSA-f82v-jwr5-mffw, Workaround |
| Credits for the 2025 bug: Allam Rachid (zhero) and Allam Yasser (inzo_). | GHSA-f82v-jwr5-mffw, Credits |
| Vercel's postmortem says self-hosted Next.js (`next start` and `standalone`) was hit. It says Vercel was not hit because routing runs in a separate system, and that Netlify and Cloudflare Workers were never affected for the same reason. Static exports were ruled out. | Vercel postmortem, 2025-03-14 timeline entry |
| The report was sent 2025-02-27; the fix was released 2025-03-17 and 2025-03-18; the CVE became public 2025-03-21. Vercel admits triage was slow because the first report named old versions. | Vercel postmortem, timeline |
| Vercel says some apps use middleware to check a login cookie early, and that it does "not recommend" using middleware as the sole way to protect routes. | Vercel postmortem, Technical analysis |
| The 2026 advisories say apps that rely on middleware or proxy checks for authorization can let protected content through when a request takes a different URL shape (data file URL, segment-prefetch URL, altered route parameter, one-locale Turbopack build). | GHSA-36qx..., GHSA-267c..., GHSA-492v..., GHSA-6gpp..., Impact |
| Four 2026 advisories give the same workaround: if you cannot upgrade, check authorization in the page or route logic or the server-side data path, not only in middleware. | GHSA-36qx..., GHSA-267c..., GHSA-492v..., GHSA-6gpp..., Workarounds |
| Fixes in May 2026: add the extra URL shapes to the middleware matcher, make the i18n data route match like the normal one, and ignore route-parameter encodings that outside requests should not supply. | GHSA-267c..., GHSA-36qx..., GHSA-492v..., Fix |
| The incomplete-fix advisory says the first App Router fix missed `middleware.ts` built with Turbopack, so a second release (15.5.18 and 16.2.6) was needed. | GHSA-26hh-7cqf-hhc6, Impact |
| The 2026 advisories I read do **not** say whether Vercel-hosted apps were protected. The Vercel changelog says no new WAF (web firewall) rules were deployed for the May release, that those issues "cannot be reliably blocked at the WAF layer," and that patching is the only complete fix. | Vercel changelog, Resolution |
| The changelog says all 13.x and 14.x versions are affected by the May release and should move to 15.5.18 or 16.2.6. | Vercel changelog, Affected versions |
| The 2026 advisories list no credits. | repo-GHSA-*.json, `credits` field (empty) |
| The Authentication guide splits checks into "optimistic" (read the cookie, for quick redirects and hiding UI) and "secure" (check the session in the database, for sensitive data and actions). It recommends a Data Access Layer (DAL) and data transfer objects (DTOs), and says Proxy is optional. | Next.js Authentication guide, Authorization |
| The guide says Proxy "should not be your only line of defense" and that most security checks should be as close to the data as possible. | Next.js Authentication guide, Optimistic checks with Proxy |
| A page-level or layout check does not protect Server Actions or nested routes. Treat Server Actions and Route Handlers like public API endpoints and verify the user in each one. | Authentication guide, Layouts and auth checks; Server Actions; Route Handlers |
| A Server Action can be called by a direct POST request even if no page uses it, so check login and permission inside every action, and check the user may act on that specific item (to prevent insecure direct object reference). | Data Security guide, Mutating Data; Authentication and authorization |
| The Proxy page says a matcher change or moving a Server Function to another route can silently remove Proxy coverage, so verify authorization inside each Server Function. | Proxy page, Good to know (matcher section) |
| The file convention "middleware" was renamed "proxy" in v16.0.0. Next.js says it recommends avoiding it unless nothing else works. | Proxy page, Version history and Migration to Proxy |
| The Data Security guide recommends a server-only Data Access Layer that does authorization checks and returns small DTOs, and picking one data-fetching approach, not mixing them. | Data Security guide, Data fetching approaches |

## Useful for the paper

- **Lesson (topics 5 and 8):** middleware or proxy is not the only access check. The 2025 bug and four 2026 bugs show that a check placed only in front of the app can be skipped when a request takes another path or shape. The vendor's own workaround and docs say the same: check where the data is read or changed.
- **Check at the data layer.** For the proposed coordinator this would mean the server code that reads a care circle's records would confirm the caller belongs to that circle, and Server Actions and Route Handlers would each check too. This is a design idea to examine, not a claim that anything is built or safe.
- **Tie to Supabase Row Level Security (RLS).** If the product used Supabase, RLS would add a second check inside the database itself, so a bypass of the web layer would still face a database rule. I have not read Supabase sources in this batch; cite its docs separately before making this claim.
- **Keep dependencies patched.** The 2026 case shows a first fix can be incomplete (CVE-2026-45109), and the Vercel changelog says patching is the only complete fix. This supports a dependency-update routine and a way to learn about new advisories.
- **Hosting is not the whole answer.** In 2025 Vercel's routing design protected hosted apps, but the 2026 advisories I read say nothing about that, and Vercel says its firewall cannot reliably block them. The paper should not say "Vercel hosting protects you."
- **Timeline example for lessons on disclosure:** the 2025 postmortem shows a 2025-02-27 report, public CVE on 2025-03-21, and Vercel's own list of process changes (private GitHub reporting only, partner mailing list, support policy).

## Limits and cautions

- Each advisory applies to specific version ranges and, for several, to specific setups (Pages Router with i18n, App Router, Turbopack, one locale). Do not say "Next.js is vulnerable" in general.
- CVSS scores here are Base severity scores. They are not risk to a particular product. Sources disagree: CVE-2026-44572 is 3.7 Low at GitHub and 5.9 Medium at NVD. CVE-2026-64642 is shown in v4.0 at GitHub and v3.1 at NVD. Always name the CVSS version.
- CWE labels differ between GitHub, NVD and the repository record for the same CVE (for example CVE-2026-44573 shows CWE-863, CWE-551, or none, depending on where you look). I report each as shown.
- The NVD status for CVE-2026-44573 through 45109 was "Modified" (not "Analyzed") when fetched. NVD records change; the pages may differ after 2026-11-18.
- The Authentication guide's code examples use `proxy.ts` and v16 names. The 2025 advisory uses "middleware." They are the same feature under two names.
- The GitHub repository API returned 79 advisories in one page. I did not confirm that the list is complete beyond that.
- No exploit steps are given here or in the saved text beyond what the advisories themselves say.

## Not read

- NVD and GHSA full web pages (github.com/vercel/next.js/security/advisories and nvd.nist.gov) in a browser. I read the same records through their APIs instead.
- The text of CVE-2026-64643 (internal Server Function endpoint disclosure) and all other 2026 advisories not about middleware.
- Linked pages: the Red Hat advisories, the reporter's write-up of CVE-2025-29927, the Next.js "Security in Next.js" article, and the GitHub commits and release notes.
- Later sections of the Data Security guide (environment poisoning and similar) and the Authentication guide's code samples were skimmed, not studied line by line. The Proxy page was read only for the matcher, runtime and rename sections.
- cve.org records.

## Source list claims I could not confirm

- The approved list says "others" and "one later CVE number from a single source is unconfirmed." I found no middleware or proxy advisory with a later number than CVE-2026-64642. The CVE numbers in November 2026 (CVE-2026-119346 and later) are for other topics (cache and image issues). I could not tell which later number the list meant, so it stays unconfirmed.
- All four named 2026 CVEs and CVE-2025-29927 exist in NVD and GitHub and are about Next.js. Their dates match "May to Jul 2026" only if you add CVE-2026-64642 (July 2026); the four named ones are all May 2026.
- CVE-2026-44575 and CVE-2026-45109 carry different GHSA IDs but the NVD record for CVE-2026-45109 also links to the GHSA of CVE-2026-44575. That is as shown in NVD.

## References (APA 7)

- Next.js. (2026, September 16). *Authentication*. Next.js documentation. https://nextjs.org/docs/app/guides/authentication
- Next.js. (2026, November 18). *How to think about data security in Next.js*. Next.js documentation. https://nextjs.org/docs/app/guides/data-security
- Next.js. (2026, November 18). *proxy.js* [File convention reference]. Next.js documentation. https://nextjs.org/docs/app/api-reference/file-conventions/proxy
- Sbano, T. (2025, March 25). *Postmortem on Next.js Middleware bypass*. Vercel. https://nextjs.org/blog/cve-2025-29927 (redirects to a vercel.com blog post)
- Lai, J. (2026, May 7). *Next.js May 2026 security release*. Vercel changelog. https://vercel.com/changelog/next-js-may-2026-security-release
- Vercel. (2025, March 21). *Authorization bypass in Next.js middleware* (GHSA-f82v-jwr5-mffw; CVE-2025-29927) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw
- Vercel. (2026, May 6). *Middleware / Proxy redirects can be cache-poisoned* (GHSA-3g8h-86w9-wvmq; CVE-2026-44572) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq
- Vercel. (2026, May 6). *Middleware / Proxy bypass in Pages Router applications using i18n* (GHSA-36qx-fr4f-26g5; CVE-2026-44573) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5
- Vercel. (2026, May 6). *Middleware / Proxy bypass through dynamic route parameter injection* (GHSA-492v-c6pp-mqqv; CVE-2026-44574) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv
- Vercel. (2026, May 6). *Middleware / Proxy bypass in App Router applications via segment-prefetch routes* (GHSA-267c-6grr-h53f; CVE-2026-44575) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f
- Vercel. (2026, May 7). *Middleware / Proxy bypass in App Router applications via segment-prefetch routes: Incomplete fix follow-up* (GHSA-26hh-7cqf-hhc6; CVE-2026-45109) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-26hh-7cqf-hhc6
- Vercel. (2026, July 21). *Middleware / Proxy bypass in App Router applications using Turbopack and single locale* (GHSA-6gpp-xcg3-4w24; CVE-2026-64642) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24
- National Institute of Standards and Technology. (n.d.). *CVE-2025-29927, CVE-2026-44572, CVE-2026-44573, CVE-2026-44574, CVE-2026-44575, CVE-2026-45109, CVE-2026-64642* [Vulnerability records]. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-44573 (change the CVE ID for each record; records read through the NVD API on 2026-11-18)
