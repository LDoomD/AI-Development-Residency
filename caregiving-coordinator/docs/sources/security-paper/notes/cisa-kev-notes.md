# Notes: CISA Known Exploited Vulnerabilities (KEV) Catalog

- **Source:** Cybersecurity and Infrastructure Security Agency. (2026). *Known exploited vulnerabilities catalog* [Data set]. U.S. Department of Homeland Security. https://www.cisa.gov/known-exploited-vulnerabilities-catalog (the saved JSON file's own title is "CISA Catalog of Known Exploited Vulnerabilities"). The catalog changes almost daily, so cite the **catalog version and retrieval date** below.
- **Label for the paper:** official government data (tier 1). It is a list of vulnerabilities that CISA says have been exploited in the wild. It is not a list of every vulnerability and not a ranking of danger.
- **Version read:** catalogVersion **2026.11.18**, dateReleased **2026-11-18T19:17:41Z** (the "Z" means UTC time), count **1,786** entries. This comes from the saved JSON file's header, checked 2026-11-18.
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/cisa-kev/catalog-page.html` and `caregiving-coordinator/docs/sources/security-paper/cisa-kev/known_exploited_vulnerabilities.json` (retrieved 2026-11-18).
- **No page numbers.** Cite by CVE number, the catalog version and the retrieval date.

## How much I read (be exact)
- **Read in full:** the text of the saved catalog page, which holds CISA's one-paragraph purpose statement, the filter menu (a long list of vendor and project names) and the first page of entries (20 entries, the newest ones). I also read the header and field names of the JSON file.
- **Read by script, not line by line:** the 1,786 entries in the JSON file. I ran a script that counted entries, sorted by date, counted by year, counted entries marked as used in ransomware campaigns, and searched all text fields for names of the web stack. I then read every matching entry's fields (listed below). I did **not** read every one of the 1,786 entries one at a time. Any count in this note is my own count from the saved file, not a number CISA publishes.

## What the page and file say

| Point | Where |
|---|---|
| CISA says it "maintains the authoritative source of vulnerabilities that have been exploited in the wild", and that organizations "should use the KEV catalog as an input to their vulnerability management prioritization framework." | Catalog page, purpose paragraph |
| Each entry has these fields: cveID, vendorProject, product, vulnerabilityName, dateAdded, shortDescription, requiredAction, dueDate, knownRansomwareCampaignUse, forensicTriage, notes, cwes. | JSON file, field names |
| The catalog has **1,786** entries. The oldest dateAdded is 2021-11-03. | JSON file; my count |
| Entries added by year (my count, 2026 runs to 2026-11-18): 2021: 311; 2022: 555; 2023: 187; 2024: 186; 2025: 245; 2026: 302. | JSON file; my count |
| 361 entries are marked "Known" for use in ransomware campaigns (my count). Most others are marked "Unknown", which means CISA has no knowledge of use, not that there was none. | JSON file; my count |
| The five newest entries by date added: **CVE-2026-90817** (REDCap code injection, 2026-11-18, due 2026-11-21); **CVE-2026-90436** (Apache Axis unsafe reflection, 2026-11-18, due 2026-11-21); **CVE-2026-40217** (BerriAI LiteLLM unprotected alternate channel, 2026-11-18, due 2026-12-02); **CVE-2024-10441** (Synology DiskStation Manager improper encoding, 2026-11-18, due 2026-11-21); **CVE-2026-115731** (Perforce Puppet Enterprise deserialization, 2026-11-17, due 2026-12-01). Four entries share the date 2026-11-18, so "newest" depends on how ties are sorted; I sorted by date then CVE number. | JSON file; my sort |
| Entries from the last few weeks mention "BOD 26-04 Prioritizing Security Updates Based on Risk" and "Forensics Triage Requirements" in their required action. The page links these as CISA directive pages. I did not open the directive. | Catalog page, newest entries |
| Due dates in the newest entries are short: 3 days for some (for example 2026-11-18 to 2026-11-21) and 14 days for others. | JSON file; the entries above |

## Entries that touch the stack of a small web product (matches from my search)
I searched all text fields for these names: Next.js, React, npm, Supabase, Vercel, PostgREST, Node.js, Vite, TanStack and GitHub Actions. Results:
- **Next.js:** no entry. In particular, the Next.js middleware bypass **CVE-2025-29927** is **not** in the saved catalog (checked by exact ID). A word search for "next" matched only unrelated entries.
- **Supabase and PostgREST:** no entry.
- **Vercel:** no entry for the company or its products. The word appears only inside a link in the notes of the React entry below (a GitHub repository name, "vercel-labs/fix-react2shell-next").
- **React:** **CVE-2025-55182**, "Meta React Server Components Remote Code Execution Vulnerability", added 2025-12-05, due 2025-12-12, marked **Known** for ransomware campaign use. It lets an unauthenticated attacker run code by sending crafted data to React Server Function endpoints. The notes tell organizations to check for signs of compromise on all internet-accessible React instances after applying mitigations. (Verizon's report names this as React2Shell; see `caregiving-coordinator/docs/sources/security-paper/notes/verizon-dbir-2026-notes.md`.) Also **CVE-2025-11953** (React Native Community CLI OS command injection, added 2026-02-05, ransomware use Unknown).
- **npm and build-tool supply chain entries:**
  - **CVE-2026-45321**, TanStack, added 2026-05-27, due 2026-06-10, **Known**: malicious versions were published to the npm registry to "publish credential-stealing malware under a trusted identity".
  - **CVE-2026-48027**, Nx Console, added 2026-05-27, **Known**: a malicious version of the extension was published and "fetched an obfuscated payload that could harvested credentials" (the entry text has this typo).
  - **CVE-2025-54313**, eslint-config-prettier, added 2026-01-22: installing an affected package ran an install script that launched Windows malware.
  - **CVE-2025-30066**, tj-actions/changed-files GitHub Action, added 2025-03-18: it let an attacker read secrets in workflow logs, including cloud access keys, GitHub tokens, npm tokens and private keys. **CVE-2025-30154**, reviewdog/action-setup, added 2025-03-24, is related.
  - **CVE-2021-21315**, an npm package for Node.js system information, added 2022-01-18: command injection.
  - **CVE-2025-31125**, Vite, added 2026-01-22: improper access control.
  - **CVE-2026-33634**, Trivy (a security scanner), added 2026-03-26: embedded malicious code.
- Hits for other products in my search (LiteLLM, Langflow, Strapi, Metabase, n8n and others) are unrelated to the proposed coordinator's stack as far as I know and are not listed here.

## Possible use in the paper
- **Topic 5 (what it includes) and topic 6 (what teams do):** KEV is the "known exploited" input that a vulnerability team uses to decide what to fix first. Pair it with CVSS (a severity score) and the CVSS pages' point that a Base score is severity and not risk.
- **Topic 7 (tools and skills):** knowing how to look up a CVE in KEV and checking the "ransomware use" field are concrete beginner skills.
- **Topic 8:** a plan for the proposed coordinator can say that when its tools flag a dependency, the owner would check the CISA list first. Honest facts to state: as of catalog version 2026.11.18 the list holds an entry for React Server Components (CVE-2025-55182) and several npm supply chain compromises, and none for Next.js, Supabase or Vercel. The paper must not say the coordinator is safe because of that. The absence of an entry only means CISA has not listed one.

## Limits
- KEV lists only vulnerabilities CISA has evidence were exploited and that have a CVE ID and a clear fix action. A product can have serious flaws that are not in it.
- The catalog changes often. Numbers here are only true for version 2026.11.18.
- I did not read the BOD 26-04 directive that the entries mention, and I did not open the NVD pages for any CVE.
- The year counts and the "Known" count are mine, from a script run on the saved file; they are not published by CISA.
