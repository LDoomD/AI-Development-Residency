# Live pages: five findings from the independent audit

Date read: 2026-11-06. Skill used: skeptical-audit (every claim has a state, a source and a limit).
Auditor notes read first: `docs/sources/feature-analysis-4/area-agencies-on-aging/AUDIT-PASS3.md` (section 4), `.../respite-adult-day/AUDIT-PASS3.md` (section 4), `.../va-caregiver/AUDIT-PASS3.md` (section 4).

## Main table

| # | Finding | URL | Saved file | Exact quote (20 words or fewer) | Auditor right? | Why, in one sentence |
|---|---|---|---|---|---|---|
| 1 | New York: a family member can be hired for caregiver-directed respite | https://aging.ny.gov/26-tam-01-implementing-caregiver-directed-respite-care-service-delivery-model-under-nfcsp | `ny-nysofa-26-tam-01-caregiver-directed-respite.txt` | "Family members may be hired as respite providers under both the Voucher Model and the FI Model." | YES | The state memo says so, but the primary caregiver cannot be the hired person and each local agency chooses whether to offer the model. |
| 2 | Illinois: volunteers help low-income older people pay bills | https://ilaging.illinois.gov/programs/money-mgmt.html | `il-money-management-program.txt` | "The program matches trained volunteers with older persons who need help with tasks such as organizing, reviewing, and paying bills" | YES | The page says it, but only for people in the Community Care Program or with a proven Adult Protective Services case, in listed counties. |
| 3 | Massachusetts: same idea | https://www.mass.gov/info-details/money-management-program | `ma-money-management-program.txt` | "Support may include help creating budgets and paying bills on time" | YES | Staff and volunteers help income-eligible people 60 and older, and the page says "may include" instead of promising bill help. |
| 4 | VA Veteran Directed Care: a veteran can hire a family member | https://www.va.gov/geriatrics/pages/Veteran-Directed_Care.asp | `va-veteran-directed-care.txt` | "hiring workers (which might include their own family member or neighbor)" | YES | The VA page says it, but the word is "might", and it does not say if a spouse is allowed. |
| 5 | ARCH: paid-relative routes for respite, state rules differ | https://archrespite.org/caregiver-resources/how-do-i-get-paid-to-be-a-family-caregiver/ | `arch-how-do-i-get-paid-to-be-a-family-caregiver.txt` | "including payment to the family caregiver or to pay for respite" | PARTLY | The page does list paid-relative routes and says states differ, but most routes pay a relative for caregiving, and only one line mentions respite. |

## Evidence tags

| Claim | State | Source | Limit |
|---|---|---|---|
| NY memo 26-TAM-01 (February 10, 2026) lets family members be hired as respite providers | documented | NY page above, read 2026-11-06; whole 16-page memo saved | Rule is for NY agencies that choose the model. Not checked: how many NY agencies use it. |
| NY: primary caregiver cannot be the hired respite provider | documented | Same memo, section "Who can be a Respite Provider?". Quote: "Cannot be the primary caregiver" | Same as above. |
| NY: the model is optional for agencies | documented | Same memo, section I. Quote: "NYSOFA allows AAAs to implement a caregiver-directed respite care service delivery model" | Does not say how many agencies did. |
| NY: caregivers must keep time records and a timesheet | documented | Same memo, section "Roles and Responsibilities" | Not quoted here to save words. |
| Illinois program: volunteers help with paying bills | documented | Illinois page above | Page says "Demonstration Program". Not checked: whether it is still funded. |
| Illinois: limited to Community Care Program participants and substantiated Adult Protective Services cases, in listed counties | documented | Same page, "Eligibility". Quote: "available to Community Care Program (CCP) participants and individuals who have a substantiated Adult Protective Services (APS) case" | The older person is the client. This is not a login for an adult child to a parent's accounts. |
| Massachusetts program: staff and volunteers help older adults with budgets and paying bills | documented | MA page above. Quote: "run by program staff and volunteers who assist older adults who are having difficulty managing their personal finances" | Text came from Firecrawl, not a script (see Blocked or limited). |
| Massachusetts: free, income-eligible, age 60 and over | documented | Same page. Quote: "free program for income eligible individuals aged 60 and older" | Page gives no income number. |
| VA Veteran Directed Care lets veterans hire workers who might be a family member | documented | VA page above (footer: "Last updated March 6, 2026") | "Might" is the page's word. Not checked: local rules, or whether a spouse can be hired. |
| VA: only enrolled veterans who meet clinical criteria, where offered | documented | Same page. Quote: "meet the clinical criteria for the service, and it is available. Services may vary by location." | Exact clinical criteria are not on this page. |
| ARCH lists routes that can pay a relative: Medicaid self-direction, Structured Family Caregiving (7 states, as of 10/2022), adult foster care by relatives (7 states), VA programs | documented | ARCH page above, read 2026-11-06. Quote: "The following states allow relatives as paid foster care providers: Connecticut, Louisiana, Indiana, Massachusetts, Ohio, Rhode Island, and Texas." | ARCH page was last modified 2023-08-11 per its metadata. The state lists may have changed. |
| ARCH: state rules differ | documented | Same page. Quotes: "resources are limited, may not exist in your state at all, and eligibility is restrictive" and "some states may require you to become a certified Medicaid provider or meet other state requirements" | General statement, not a list of each state's rule. |
| ARCH: self-direction can pay a relative "to pay for respite" | documented | Same page; the same sentence also appears on https://archrespite.org/caregiver-resources/how-to-pay-for-respite/ (saved as `arch-how-to-pay-for-respite.txt`) | One line only. The other routes on the page are for paid caregiving, not respite. |
| ARCH page says anything about Alabama or New York respite vouchers paying a relative | observed (absent from this page) | Searched both saved ARCH pages (grep): Alabama is not named; New York appears once, only in a paid-family-leave list for workers, not in a voucher | The respite audit note cites Alabama and New York from another file. This task did not re-check Alabama. Status: not-assessed. |

## Where the auditor's claim needs a correction

1. Finding 5 is only PARTLY right. The ARCH page "How Do I Get Paid to be a Family Caregiver?" is about paying a family caregiver for ongoing care. Only the Medicaid self-direction paragraph also mentions paying "for respite". The page does not describe NY or Alabama respite vouchers. The NY rule comes from finding 1 (a different, state source).
2. Findings 2 and 3 are YES, but the auditor's own limits matter more than the headline. Illinois restricts the service to two groups in listed counties. Massachusetts says "may include". Both serve the older person. Neither gives a caregiver access to a parent's bank accounts.
3. Finding 1 is YES, but add two limits when it is used: the hired person cannot be the primary caregiver, and a local agency must choose to offer the model.
4. Finding 4 is YES, but the page says "might include", not "can hire anyone". It does not say if the veteran's spouse is allowed.

## Blocked or limited

| Item | What happened |
|---|---|
| `www.mass.gov` | A plain curl request returned HTTP 403 for both robots.txt and the page. robots.txt was read through Firecrawl instead. It does not disallow `/info-details/` and has no ClaudeBot group. The page text came from one Firecrawl scrape and was copied into the file by hand, so it is not a script copy. Quotes 3, 3b and 3c match that copy. |
| `aging.ny.gov` | The memo page resolves to a PDF. Saved the PDF text with pdftotext (16 pages). Page numbers are form-feed breaks. |
| robots.txt for NY, Illinois, VA, ARCH | Read with curl. For `User-agent: *` none disallows the paths used. None has a ClaudeBot group. Copies in `robots-checks.txt`. Illinois blocks some named bots (Amazonbot, Bingbot ads, AhrefsBot, CCBot and others) but not general agents or ClaudeBot. |
| Pages not fetched | Nothing was skipped for robots reasons. I did not fetch Trustpilot, aplaceformom.com or gao.gov. |

## Quote check

Command: `python3 docs/sources/competitive-analysis-4/live-pages/check_quotes.py docs/sources/competitive-analysis-4/live-pages` (run from the repo root). It collapses spaces and curly quotes, then looks for each quote inside its saved file and counts words.
Result, 2026-11-06: all 15 quotes (the 5 above plus 10 supporting quotes) MATCH, and none is over 20 words. Output saved in `QUOTE-CHECK.txt`.
Limit: this proves the text is in my saved copy. It does not prove the live page has not changed since 2026-11-06.

## Not checked

- Whether any of these programs is open or funded in a given family's area.
- Page history: pages change, and only the 2026-11-06 text is saved.
- Alabama and North Carolina voucher rules (outside the five findings).
- Whether Illinois or Massachusetts volunteers can act as a caregiver's agent for a parent's accounts (neither page says so).

## Skills

Applied: skeptical-audit. Judged not relevant (no code, UI, or personal data was built or reviewed): security-review, accessibility-check, engineering-quality-check, judge-arch, architectural-decision-records, enterprise-architecture-standards, owasp-secure-coding-bdd, test-strategy, operational-readiness, release-deployment-safety, data-lifecycle-compliance, ux-ui-design-review, writing-security-tests.
