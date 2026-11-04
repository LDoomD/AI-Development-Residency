# Feature Comparison Analysis 3 (teacher format, 2026-11-04)

Built to match the teacher's example (Figma node `5:823`) and blank template (`5:3064`): the same columns, his questions in the second row, OUR COMPANY first, and ✅/🚫 in the feature cells. Figma: section `2584:10359` inside "Feature Analysis". Versions 1 and 2 (`docs/feature-analysis.md`, Figma `2436:9443`) are unchanged.

**How it was made:** ✅ = the company offers the feature on its own saved pages (`docs/feature-analysis.md` step 2 and `docs/sources/competitive-analysis-2/facts/`). How well each feature works is counted from the 577 caregiving items in `docs/sources/competitive-analysis-2/themes/`, using `feature-analysis-3/theme-to-feature.json` (Claude's mapping, open for the owner to check) and `build_howwell.py`. `assemble_fa3.py` checks every number. The Figma text matches the source (195 of 195 main cells, 99 of 99 how-well cells, plus the gaps and notes texts).

## Main table (teacher format)

| COMPANY | WEBSITE | PRICING STRUCTURE | MARKET | MARKET SEGMENT / CHANNEL | CUSTOMERS OF THE SOFTWARE | SHARED CALENDAR AND TASK SIGN-UP | ONE UPDATE REACHES EVERYONE | RELATIVES JOIN WITH THEIR OWN ACCESS | MEDICATION REMINDERS FAMILY CAN SEE | STORE AND SHARE IMPORTANT DOCUMENTS | SEE MEDICAL RECORDS AND TEST RESULTS | EMERGENCY HELP AND ALERTS TO FAMILY | SUPPORT FOR THE CAREGIVER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | What’s the product’s website URL? | How does the product “charge” for its services to its clients and customers? | Care coordination, health records, medication, safety or document software? | Which segment of the family caregiving market does this company fit (based on customers and website language)? | Who are the main customers of the competitor? | Does the product offer ways for family and friends to share one calendar and sign up for tasks? | Does the product offer ways to send one update to the whole family at once? | Does the product offer ways for relatives to join with their own login and permissions, without sharing a password? | Does the product offer ways to remind about medications and show family when a dose is missed? | Does the product offer ways to keep and share documents like IDs, legal and medical papers? | Does the product offer ways for a caregiver to see the person's medical records and test results? | Does the product offer ways for the older person to get emergency help, with an alert to family? | Does the product offer ways to support the caregiver, such as guidance, messages or community? |
| OUR COMPANY |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CARING VILLAGE | https://caringvillage.com/ | Freemium: free plan (2 members, with ads); Circle $14.99/month; Village $24.99/month | FAMILY CARE COORDINATION | Families caring for a loved one; care businesses for their clients | Family caregivers (B2C); some care businesses (B2B) | ✅ | ✅ | ✅ | ✅ | ✅ | 🚫 | 🚫 | ✅ |
| CARINGBRIDGE | https://www.caringbridge.org/ | Free; nonprofit funded by donations | FAMILY CARE COORDINATION | Patients and families during a health journey | Patients and family caregivers (B2C); donors fund it | ✅ | ✅ | ✅ | 🚫 | 🚫 | 🚫 | 🚫 | ✅ |
| LOTSA HELPING HANDS | https://lotsahelpinghands.com/ | Free | FAMILY CARE COORDINATION | Caregivers, friends, neighbors and volunteer helpers | Caregivers and volunteer helpers (B2C) | ✅ | ✅ | ✅ | 🚫 | 🚫 | 🚫 | 🚫 | ✅ |
| EVERPLANS | https://www.everplans.com/ | Freemium: free (3 items); Premium $99.99/year; also through financial advisors | DOCUMENT VAULT | People planning their own affairs; financial advisors and partners | Individuals and households (B2C); financial advisors (B2B) | 🚫 | 🚫 | ✅ | 🚫 | ✅ | 🚫 | 🚫 | ✅ |
| EPIC MYCHART | https://www.mychart.org/ | Free to patients; licensed by Epic to healthcare organizations (price not stated) | HEALTH RECORDS (PATIENT PORTAL) | Health systems and their patients | Healthcare organizations (B2B); patients and family proxies use it | 🚫 | 🚫 | ✅ | 🚫 | 🚫 | ✅ | 🚫 | 🚫 |
| LIVELY | https://www.lively.com/ | Device ($89.99) plus monthly plan ($24.99 or $34.99); fall detection +$9.99/month; caregiver bundle $99/year | SENIOR SAFETY (MEDICAL ALERT) | Older adults and their families; sold online and in stores | Older adults, and the adult children or spouses who buy it (B2C) | 🚫 | ✅ | ✅ | 🚫 | 🚫 | 🚫 | ✅ | ✅ |
| MEDICAL GUARDIAN | https://www.medicalguardian.com/ | Monitoring subscription, about $1 a day; device often free with a promo; cancellation fees may apply | SENIOR SAFETY (MEDICAL ALERT) | Older adults and families; also dealers, health plans and senior living | Older adults and families (B2C); health plans and partners (B2B) | 🚫 | 🚫 | ✅ | 🚫 | 🚫 | 🚫 | ✅ | 🚫 |
| MEDISAFE | https://medisafeapp.com/ | Free app with a paid subscription (price not stated); also sold to drug makers and providers | MEDICATION | Patients and family members; drug makers and providers | Patients and family caregivers (B2C); drug makers and providers (B2B) | 🚫 | 🚫 | ✅ | ✅ | 🚫 | 🚫 | 🚫 | ✅ |
| GROUP TEXTS (WORKAROUND) | n/a | Free | WORKAROUND, NOT CARE SOFTWARE | Every family; also paid care staff and agencies | Family caregivers and relatives | 🚫 | ✅ | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| PAPER NOTEBOOK AND VISIT LOG (WORKAROUND) | n/a | Nearly free (store-bought planners cost a little) | WORKAROUND, NOT CARE SOFTWARE | Families caring at home | The main caregiver, paid aides and the person being cared for | ✅ | 🚫 | 🚫 | 🚫 | ✅ | 🚫 | 🚫 | 🚫 |

✅ comes from the company's own saved pages (docs/feature-analysis.md step 2 and facts/*.json). Exceptions: Medical Guardian 'relatives join' is ✅ because reviewers describe its MyMedicalGuardian family app (its saved pages only list family as emergency contacts). Group texts 'relatives join' is 🚫 because anyone can be added but there are no permissions. Paper calendar and documents are ✅ for use inside the home only. MyChart shows medications but has no reminders, so medication is 🚫.

## How well each feature works (evidence)

Label: fewer than 5 items = Too few to judge; at least 2 of 3 say it works = Mostly works; at least 2 of 3 report a problem = Mostly problems; otherwise Mixed.

| COMPANY | SHARED CALENDAR AND TASK SIGN-UP | ONE UPDATE REACHES EVERYONE | RELATIVES JOIN WITH THEIR OWN ACCESS | MEDICATION REMINDERS FAMILY CAN SEE | STORE AND SHARE IMPORTANT DOCUMENTS | SEE MEDICAL RECORDS AND TEST RESULTS | EMERGENCY HELP AND ALERTS TO FAMILY | SUPPORT FOR THE CAREGIVER |
|---|---|---|---|---|---|---|---|---|
| CARING VILLAGE | 🟢 Mostly works · works 9, problems 4 · Shared calendar and handing out tasks work. Some say the care plan resets or is too rigid (3). | 🟢 Mostly works · works 13, problems 0 · Keeps the whole family updated and on the same page (10). No complaints found. | 🟠 Mixed · works 5, problems 4 · Big families share one group (5), but there are limits on who can join and what they see (4), and getting everyone in is hard (2). | 🟢 Mostly works · works 6, problems 2 · Medication lists and reminders work (6). Logs don't show who gave a dose (2). | 🟠 Mixed · works 3, problems 2 · Storing documents works (3), but old records can't be kept or found (2). | Not offered | Not offered | Too few to judge · works 2, problems 0 · Only the new AI question feature is mentioned (2). |
| CARINGBRIDGE | Too few to judge · works 0, problems 3 · Reviewers say it isn't built for day-to-day coordination (3). | 🟢 Mostly works · works 62, problems 2 · Its main strength: one post reaches everyone (49), and far-away family can follow (15). | 🟢 Mostly works · works 8, problems 3 · Invite-only pages work (6), but the 2024 sign-in change locked family out (3). | Not offered | Not offered | Not offered | Not offered | 🟢 Mostly works · works 9, problems 0 · Comments and messages lift up the family (9). |
| LOTSA HELPING HANDS | Too few to judge · works 3, problems 0 · Helpers sign up for tasks (3). Very little evidence. | ✅ Offered · no caregiver mentions it | ✅ Offered · no caregiver mentions it | Not offered | Not offered | Not offered | Not offered | ✅ Offered · no caregiver mentions it |
| EVERPLANS | Not offered | Not offered | ✅ Offered · no caregiver mentions it | Not offered | ✅ Offered · no caregiver mentions it | Not offered | Not offered | ✅ Offered · no caregiver mentions it |
| EPIC MYCHART | Not offered | Not offered | 🟠 Mixed · works 13, problems 25 · Several family members under one login works (12), but access is hard to set up (8), and with no caregiver login families share the password (7). | Not offered | Not offered | 🟢 Mostly works · works 34, problems 5 · Results and doctor notes (13), messaging the doctor (11), appointments and meds (11). Hard to share outside MyChart (3). | Not offered | Not offered |
| LIVELY | Not offered | ✅ Offered · no caregiver mentions it | 🟠 Mixed · works 10, problems 14 · Several relatives follow one person (10), but linking family is confusing (13). | Not offered | Not offered | Not offered | 🔴 Mostly problems · works 36, problems 100 · Seeing location (23) and a quick operator (15) work, but location is wrong (58), the device shows as off (28), and family alerts come late or never (27). | ✅ Offered · no caregiver mentions it |
| MEDICAL GUARDIAN | Not offered | Not offered | 🔴 Mostly problems · works 7, problems 16 · Checking on a parent from a phone is the main draw (7), but the family app won't sign in (16). | Not offered | Not offered | Not offered | 🔴 Mostly problems · works 5, problems 20 · Help comes fast (5), but readings and location are wrong (9), fall detection misses (7), and family isn't told (6). | Not offered |
| MEDISAFE | Not offered | Not offered | 🟠 Mixed · works 5, problems 6 · Watching a relative's doses works (4), but sharing breaks between linked caregivers (4). | 🟢 Mostly works · works 16, problems 8 · Keeps a loved one's complicated schedule on track (10), but caregivers can't share the work (4) and views go out of sync (3). | Not offered | Not offered | Not offered | ✅ Offered · no caregiver mentions it |
| GROUP TEXTS (WORKAROUND) | Not offered, but families use it for this: 🔴 Mostly problems · works 3, problems 10 · Quick to ask someone to cover a shift (3), but requests get silence (10), and being in the chat doesn't mean helping (7). | 🔴 Mostly problems · works 6, problems 20 · One place to tell everyone (6), but updates get silence (10) and details get buried (10). | Not offered, but families use it for this: Too few to judge · works 0, problems 4 · Not everyone joins (2), and side chats leave people out (2). | Not offered, but families use it for this: 🔴 Mostly problems · works 0, problems 10 · Medication changes get buried, causing near double doses (10). | Not offered | Not offered | Not offered, but families use it for this: 🔴 Mostly problems · works 0, problems 5 · Not dependable when something urgent happens (3). | Not offered |
| PAPER NOTEBOOK AND VISIT LOG (WORKAROUND) | 🔴 Mostly problems · works 6, problems 16 · A whiteboard calms repeated questions (6), but notes get ignored, lost or erased (12) and stay with one person (6). | Not offered | Not offered | Not offered, but families use it for this: 🔴 Mostly problems · works 0, problems 6 · Paper stays with one person, so family miss medication changes (6). | 🟠 Mixed · works 8, problems 12 · A binder lets someone step in (4) and is ready in a crisis (4), but records pile up and can't be found fast (7). | Not offered | Not offered | Not offered |

## Feature gaps and opportunities (report version, updated 2026-11-04 from the updated market analysis)

FEATURE GAPS AND OPPORTUNITIES (updated 2026-11-04, from the updated market analysis)  
What this is: the features caregivers need that no company does well. These are open problems, not things to build. Nothing is chosen.  
How to read the numbers: "(13, 25)" means 13 caregiving reviews or posts say it works and 25 report a problem. "How big" is the share of caregiving forum threads (117) and Reddit caregiver posts (412) that mention the problem, from the updated market analysis.  
  
1. Relatives rarely get working access of their own  
• How big: money, accounts and legal papers: forums 33%, Reddit 28%. On Reddit, banks refuse the caregiver (46), passwords are lost (32), codes go to the parent's phone (22).  
• Offered by: all 8 companies  
• Works well at: only CaringBridge (8, 3)  
• Mixed at: MyChart (13, 25), Lively (10, 14), Medisafe (5, 6), Caring Village (5, 4)  
• Mostly problems at: Medical Guardian (7, 16)  
  
2. Shared calendars don't get relatives to help  
• How big: family coordination: forums 24%, Reddit 24%. On Reddit, siblings won't share the work (63).  
• Offered by: 3 companies. Caring Village mostly works (9, 4). CaringBridge isn't built for day-to-day use (3). Lotsa is too thin to judge.  
• Families fall back on group texts (3, 10) and paper (6, 16), and both mostly have problems  
  
3. Emergency alerts don't reach the family  
• How big: safety: forums 24%, Reddit 19%  
• Offered by: 2 companies, and both mostly have problems: Lively (36, 100), Medical Guardian (5, 20)  
• The button reaches help, but location is wrong, alerts come late, and family isn't told  
  
4. Medication info breaks when caregivers share it  
• How big: medications: forums 16%, Reddit 13%. On Reddit, unshared changes caused double doses or mix-ups (24).  
• Offered by: 2 companies. Both work for one caregiver: Caring Village (6, 2), Medisafe (16, 8)  
• Breaks when shared (Medisafe): sharing the work (4), views out of sync (3), whose dose it is (2)  
• Group texts (10) and paper (6) lose medication changes  
  
5. Documents and power of attorney have no real home  
• How big: inside money, accounts and legal papers (forums 33%, Reddit 28%). On Reddit, POA missing or rejected (29), papers scattered (22).  
• Offered by: 2 companies, with little evidence: Caring Village is mixed (3, 2), Everplans has none  
• Paper binders are mixed (8, 12). No company helps with a rejected POA.  
  
6. Medical records stay inside MyChart  
• How big: doctors, appointments and records: forums 20%, Reddit 21%  
• Only MyChart offers them, and they mostly work once a caregiver is in (34, 5)  
• The problem is getting in (see gap 1)  
  
7. Caregiver support misses the real problem  
• How big: burnout and doing it alone, the top problem everywhere (forums 43%, Reddit 51%)  
• 6 companies offer something: AI questions, comments, well wishes, guides, a care-coordinator bundle, resource centers  
• Caregivers only mention CaringBridge comments (9) and Caring Village's AI feature (2)  
  
8. No one covers the whole job  
• Caring Village offers the most (6 of 8 features), but has no records or emergency alerts  
• Caregivers on Reddit almost never name it (3 posts, none describing use). Families stitch tools together instead.  
  
PROBLEMS NO FEATURE COLUMN COVERS (from the updated market analysis)  
• Dementia behavior and hard conversations: forums 34%, Reddit 24%. None of the 8 companies covers it.  
• The person refuses help: forums 10%, Reddit 20%. Every tool assumes the older person will use it.  
• Choosing, placing and paying for care: forums 30%, Reddit 22%. Not covered by these companies.  
• Hands-on personal care and supplies: 17 Reddit posts as main topic. Not covered.  
  
LIMITS  
• ✅ only means a company says it offers a feature, not that it works  
• Reviews and Reddit posts lean toward strong opinions  
• Everplans (1 caregiving review) and Lotsa (4 items) are too thin to judge  
• Which theme counts toward which feature was Claude's call (feature-analysis-3/theme-to-feature.json)  
  
NEXT STEP FOR YOU  
• Fill the OUR COMPANY row with ✅ or 🚫. Claude doesn't choose.
