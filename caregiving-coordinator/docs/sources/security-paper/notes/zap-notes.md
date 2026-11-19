# Notes: ZAP (Zed Attack Proxy), official documentation

- **Source:** ZAP Dev Team. (2026). *ZAP* [Software documentation]. ZAP by Checkmarx. https://www.zaproxy.org/ (Pages are marked "Copyright 2026 the ZAP Dev Team". Individual pages show no author or date, so cite the page title and the retrieval date: Retrieved November 18, 2026.)
- **Label for the paper:** tool documentation. Tier 1 for what the tool does and how its scans work. It is NOT evidence that any app is secure. **Correction to the source list:** the list calls ZAP an OWASP project. The ZAP Ownership page says the team took ZAP out of OWASP in September 2023 to get funding, and that it is now "ZAP by Checkmarx", an independent open source project. Do not call it an OWASP project or flagship in the paper. Pages that say "OWASP ZAP" are out of date (per the same page).
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/zap/` holds an `.html` file (raw download) and, for the main pages, a `.txt` file (text I extracted from the HTML to read; the HTML is the original). Also `latest.json` and `repo.json` (GitHub API answers).
- **Newest release found:** **ZAP 2.17.0, published 2025-12-15.** Seen in two places: the Download page (lists "ZAP 2.17.0" and a "2.17.0 Release Page") and the GitHub API `releases/latest` (tag `v2.17.0`, not a pre-release, published 2025-12-15T14:41:51Z). The two agree. The Download page says it supports only the latest full release.
- **License:** GitHub API for the repo `zaproxy/zaproxy` reports Apache License 2.0 (`repo.json`). I did not find a license statement in the pages themselves other than the installer's "Read the License agreement" step (Download page).
- **Read in full (retrieved 2026-11-18, plain `curl -L`):**
  1. https://www.zaproxy.org/ (home)
  2. https://www.zaproxy.org/download/
  3. https://www.zaproxy.org/getting-started/
  4. https://www.zaproxy.org/docs/ (Docs landing page)
  5. https://www.zaproxy.org/docs/automate/
  6. https://www.zaproxy.org/docs/docker/about/
  7. https://www.zaproxy.org/docs/docker/baseline-scan/
  8. https://www.zaproxy.org/faq/ (FAQ index)
  9. https://www.zaproxy.org/docs/zap-ownership/ (ownership, OWASP status)
  10. https://www.zaproxy.org/docs/scans/ (ZAP Scans: test apps)
  11. FAQ answers: /faq/what-does-zap-test-for/, /faq/is-there-any-danger-when-scanning-with-zap-against-a-live-website-e-g-create-delete-update-corrupt-data/, /faq/what-data-does-zap-collect/, /faq/what-calls-home-does-zap-make/, /faq/what-is-zaps-assurance-case/, /faq/how-do-i-handle-a-false-positive/, /faq/how-do-i-report-a-false-negative/, /faq/why-can-zap-scans-be-inconsistent/, /faq/someone-is-using-zap-to-attack-my-website-what-should-i-do/
  12. GitHub API: https://api.github.com/repos/zaproxy/zaproxy/releases/latest and https://api.github.com/repos/zaproxy/zaproxy
- **Pages that do not exist (404):** https://www.zaproxy.org/about/ and https://www.zaproxy.org/docs/faq/ and https://www.zaproxy.org/getting-further/. I used the ownership page and FAQ pages instead. There is no separate "Legal" page that I found; the permission warnings are in Getting Started and the live-website FAQ.
- **Skipped on purpose:** the other FAQ answers (how-to, networking, desktop UI, Java, fonts and similar), the add-on marketplace, the Alert Details catalogue (list of every rule), API reference lists, the Desktop User Guide, the Developer Guide, "Getting Further" guides, the Automation Framework reference pages, GitHub Actions pages, blog posts (including "ZAP Has Joined Forces With Checkmarx"), and the pages for the other automation options (ZAPit, quick start command line, API and daemon mode). I read only the one-line descriptions of those on the Automate page.

## What the pages say (my words)

| Point | Page and heading |
|---|---|
| ZAP is a free, open source scanner for web apps. The home page calls it "the world's most widely used web app scanner" (the project's own claim, not checked). | Home |
| ZAP is a "manipulator-in-the-middle" proxy. It sits between the tester's browser and the web app so it can read, change and pass on messages. | Getting Started, "Introducing ZAP" |
| It was made for web applications, and it can run as a desktop app or as a background (daemon) process. | Getting Started, "Introducing ZAP" |
| The guide splits security testing into vulnerability assessment (look for issues without exploiting them) and penetration testing (try to exploit them). | Getting Started, "Security Testing Basics" |
| Passive scanning only watches traffic that passes through ZAP. It changes nothing and is called safe. It is good for a first feel of an app's basic security state. | Getting Started, "Running an Automated Scan" |
| Active scanning uses known attacks on the target. It is "a real attack" and can put the target at risk. | Getting Started, "Running an Automated Scan" |
| Spiders (crawlers) find pages. The older spider reads HTML and is fast but weak on JavaScript-heavy apps. The newer Client spider uses real browsers and is slower. The AJAX spider is no longer recommended in most cases. | Getting Started, "Running an Automated Scan" |
| Pages behind a login are not found unless authentication is set up. Spiders enter only basic data in forms, so manual exploring through the proxy should be added. | Getting Started, "Exploring an Application Manually" |
| ZAP tests HTTP with active and passive rules, and WebSockets with passive rules. The full rule list is on a separate Alert Details page (not read). | FAQ, "What does ZAP test for?" |
| A baseline scan crawls the target for 1 minute by default, then reports what passive scanning found. It does "not" run actual attacks, runs a few minutes at most, and is meant to be ideal for CI/CD, "even against production sites." | Docker, Baseline Scan (intro) |
| By default every alert is a warning. A config file can set a rule to FAIL (fail the build), IGNORE, or INFO. | Baseline Scan, "Configuration File" |
| Baseline exit codes: 0 success, 1 at least one FAIL, 2 warnings but no FAIL, 3 any other failure. | Baseline Scan, "Exit Value" |
| A "progress file" can mark known issues as in progress, so new issues stand out. | Baseline Scan, "Progress File" |
| Baseline output lists rule checks that passed and warned, for example missing X-Frame-Options and missing cookie flags. (This example output is from 2016 per its timestamp; the rule names are old.) | Baseline Scan, "Example Output" |
| Docker images ship three packaged scans: Baseline (passive), Full (adds an active scan) and API (active scan of an OpenAPI or GraphQL definition). | Docker About, "Packaged Scans" |
| Warning: the packaged scans expose an unauthenticated ZAP API on the host. Do not expose that port to untrusted systems. | Docker About, "Packaged Scans" |
| A "bare" Docker image is small and meant for CI. The Automation Framework runs ZAP from one YAML file and is described as recommended for most non-trivial automation. | Docker About; Automate |
| Automation options: ZAPit, quick start command line, Docker packaged scans, GitHub Actions, Automation Framework, and API/daemon mode. | Automate |
| GitHub Actions wrap the packaged scans and can open GitHub issues for findings. | Docker About, "GitHub Actions" |
| Permission warning: only use ZAP on an app you have permission to test with an active attack, because real damage to function or data can happen. Safe Mode limits ZAP to safe actions. | Getting Started, "IMPORTANT" |
| Proxying and passive scanning are "completely safe and legal." Spidering can cause problems. Active scanning "may create/modify/delete data." The last two could be illegal on apps you do not have permission to test. Safe mode and protected mode (only sites in scope) are recommended. | FAQ, "Is there any danger when scanning with ZAP against a live website" |
| False positives are alerts for things that are not real problems. The FAQ says to understand and manually test an alert before calling it false. False negatives (missed issues) are a known thing and can be reported. | FAQ, false positive and false negative answers |
| Repeat scans of an unchanged target can give slightly different results, mostly because crawling differs. | FAQ, "Why can ZAP scans be inconsistent?" |
| ZAP is meant for single-user and CI/CD use. It does not try to protect against someone with command line access to the machine it runs on. It does not generally trust the sites it connects to; for possibly malicious sites it suggests a container or VM. | FAQ, "What is ZAP's assurance case?" |
| By default ZAP "calls home" to the zaproxy.org domain to check for updates, show news and send telemetry. These can be turned off. The `-silent` option stops them (some third-party add-ons may ignore it). | FAQ, "What 'calls home' does ZAP make?" |
| ZAP says it does not collect personally identifiable information. Since it sits in the middle of traffic, it can see very sensitive data. | FAQ, "What data does ZAP collect?" |
| ZAP's own test results page says test apps can test for issues that are outdated, very unlikely in real apps, or that automated scanners cannot realistically find. | Docs, "ZAP Scans" |
| If someone uses ZAP against your site, it is not covert (it leaves "ZAP" marks in server logs). The FAQ says it is "generally best not to test your production site" and to use a development or staging copy. | FAQ, "Someone is using ZAP to attack my website" |
| ZAP left OWASP in September 2023; three Core Team members work for Checkmarx. License per GitHub: Apache 2.0. | Ownership page; GitHub API |
| The Docs landing page lists a guide that maps the OWASP Top 10 (2021) to ZAP features, and a Burp-to-ZAP feature map (titles only; I did not read those pages). | Docs landing page |

## Useful for the paper

- **Topic 4, current methods and tools.** ZAP is a free example of DAST (testing a running web app from the outside). It has passive scanning (watch only), spidering (crawl) and active scanning (attack). The paper can use these three levels to explain what each costs in risk.
- **What scanners find.** The baseline example shows the kind of issues passive checks catch: missing security headers, cookie flags, debug messages, and similar. These are things visible in responses.
- **What scanners do not find.** The pages say: pages behind a login are missed unless authentication is set up; spiders fill forms with basic data; results vary between runs; test apps can contain issues scanners cannot realistically find. The pages do not list what ZAP cannot find, so any longer "cannot find" list needs a second source (for example OWASP WSTG or NIST SP 800-115).
- **Automated baseline scan in CI (topic 7).** A passive baseline scan can run in a build with a Docker one-liner, fail the build on rules you choose, and keep a record of known issues. The docs say it is meant for CI/CD. This can be described as a method a team could use on a proposed product, not as something done.
- **Permission and legal use.** Get permission before spidering or active scanning. Use Safe or Protected mode. Prefer a development or staging copy over production (FAQ). This is useful for a proposed caregiving product that would hold health information: tests should never touch real family data.
- **Relationship to WSTG.** I did not find WSTG named in the pages I read. ZAP's pages describe a tool. WSTG (read separately) describes test goals. I can say a tool like ZAP could help with some WSTG checks, but I did not read a ZAP page that maps the two, so the paper should state it as my own link between two sources, not as ZAP's claim. The Docs page does list a map to the OWASP Top 10 (2021) that I did not open.

## Limits and cautions

- A scanner does not prove an app is secure. A clean scan means ZAP's rules found nothing in the places it reached. The paper must not say a tool run "makes" anything secure.
- Active scans can create, change or delete data. Only run them against systems you own or have written permission to test, and prefer a test copy.
- Because ZAP is a middle proxy, it can see sensitive data in the traffic it handles. Treat ZAP's saved sessions and reports as sensitive if they hold real data.
- The Docker packaged scans open an unauthenticated API port; do not expose it.
- The ZAP team's statements about data collection and assurance are the vendor's own claims. I did not test them.
- The home page's "most widely used" claim is the project's own and not checked.
- The baseline example output is old (2016 timestamp); do not cite its rule names as current.
- OWASP status is not current (see label above). The Download page also warns that releases are unsigned and may be flagged by browsers; check checksums before installing.
- ZAP 2.17.0 is dated 2025-12-15. Check the download page again before the paper is final.

## Not read

The pages and groups listed under "Skipped on purpose" above: other FAQ answers, Alert Details (full rule list), add-on marketplace and per-add-on pages, Desktop User Guide, Developer Guide, Automation Framework and GitHub Actions detail pages, authentication pages, the "ZAPping the OWASP Top 10 (2021)" guide, blog posts, the release notes for 2.17.0, and the ZAP Getting Started PDF. The alert-risk categories in Getting Started are shown as an image on the page, so I could not read them as text.
