# Competitive analysis 4: proposed changes to the existing 9 rows (draft, 2026-11-06)

Status: **draft for the owner's review. Figma is not changed.** The owner said to include all 18 differences. Branch: `competitive-analysis-4`.

Source of truth for the old text: the owner's Figma competitive analysis (node 2843:15117), copied at `docs/sources/feature-analysis-4/figma-competitive-tables-2026-11-06.md`. Source for the new text: the final verdict tables in each company's `AUDIT-PASS3.md` under `docs/sources/feature-analysis-4/<folder>/`. Cell wording follows the table rules: the first word answers, two short sentences at most, no counts or quotes in the cell. Counts and quotes stay in the evidence files.

Rule for the Yes / Partly / No scale: **Yes** means the product does it for any caregiver without limits. **Partly** means it does some of it, or only for some people. **No** means it does not.

## Caregiver needs table (4c)

| # | Competitor and need | Old cell | Proposed cell | Change | Evidence |
|---|---|---|---|---|---|
| 1 | Caring Village, 5 Relatives share | Partly: relatives join free with their own login. Can't make them do tasks. | Partly: tasks can be assigned or claimed, and show who finished them. The free plan allows only 2 members, so some relatives can't join. | Wording | `caring-village/AUDIT-PASS3.md` |
| 2 | Caring Village, 2 Relief | Partly: less stress and back-and-forth. Takes no care tasks off the caregiver. | Partly: a link finds in-home caregivers through Care.com. It does not find respite stays or take care tasks off the caregiver. | Wording | `caring-village/AUDIT-PASS3.md` |
| 3 | Caring Village, 1 Understand | Partly: an AI helper answers care questions. No help with dementia behavior. | Partly: an AI helper answers care questions. Dementia behavior help is only in blog articles, not in the app. | Wording | `caring-village/AUDIT-PASS3.md` |
| 4 | Everplans, 3 Money and accounts | Yes, if the parent fills it in: accounts, papers, insurance and wishes in one vault. | Partly: needs the paid plan, and relatives get access only after a death is reported. Works only if the parent filled it in. | Yes to Partly | `everplans/AUDIT-PASS3.md` |
| 5 | Cariloop, 3 Money and accounts | Yes: help paying for care, with Medicare, Medicaid and VA benefits, and POAs. | Partly: coaches explain Medicare, Medicaid and VA benefits and powers of attorney. No page shows they file applications. | Yes to Partly | `cariloop/AUDIT-PASS3.md` |
| 6 | Cariloop, 4 Parent refuses | Partly: coaches handle family dynamics. Nothing for a parent who refuses. | Partly: coaches handle family dynamics. No source shows what they do when a parent refuses. | Wording | `cariloop/AUDIT-PASS3.md` |
| 7 | Cariloop, 5 Relatives share | Partly: relatives join the Care Team and get updates. Tasks aren't split. | Partly: relatives join the Care Team and can take on tasks. Tasks are not assigned or confirmed. | Wording | `cariloop/AUDIT-PASS3.md` |
| 8 | A Place for Mom, 4 Parent refuses | No: an advisor told one family to lie to the parent to move her. | Partly: guides explain how to talk with a parent who refuses assisted living. One complaint says an advisor suggested lying to the mother. | No to Partly | `a-place-for-mom/AUDIT-PASS3.md` |
| 9 | Care managers, 3 Money and accounts | Partly: advise on financial options. One took power of attorney without telling the family. | Partly: advise on financial options and help with power of attorney and mail. One report is of a fiduciary firm taking power of attorney without telling the family. | Wording | `aging-life-care/AUDIT-PASS3.md` |
| 10 | Care managers, 4 Parent refuses | Partly: talk with the parent directly. Some parents still refuse them. | Partly: talk with the parent directly. It works when the parent accepts the manager. | Wording | `aging-life-care/AUDIT-PASS3.md` |
| 11 | Group texts, 4 Parent refuses | Partly: work without the parent using any tech. Nothing helps when the parent refuses. | No: parents often refuse the calendar, notebook or whiteboard too. | Partly to No | `group-texts-notebooks/AUDIT-PASS3.md` |
| 12 | Area Agencies, 5 Relatives share | No: services go to one caregiver. Nothing for relatives to share. | Partly: in some places a relative other than the main caregiver can be hired as the respite worker. Most services go to one caregiver. | No to Partly. Saved page confirms it, with limits: the main caregiver can't be the hire, and each local agency chooses whether to offer it. | `competitive-analysis-4/live-pages/ny-nysofa-26-tam-01-caregiver-directed-respite.txt` |
| 13 | Area Agencies, 3 Money and accounts | Partly: Medicare counseling. Otherwise referrals, no hands-on help with accounts. | Partly: Medicare counseling, plus bill-paying help in some states for low-income older people who qualify. Otherwise referrals. | Wording. Saved pages confirm it, with limits: Illinois serves only certain program participants in listed counties, and Massachusetts serves income-eligible people 60 and older. | `competitive-analysis-4/live-pages/il-money-management-program.txt`, `ma-money-management-program.txt` |
| 14 | Respite and adult day, 5 Relatives share | No: nothing helps relatives share. Family not helping keeps caregivers from taking breaks. | Partly: some state respite programs can pay a relative who is not the main caregiver. Otherwise nothing helps relatives share. | No to Partly. Supported by the New York memo. The ARCH page lists other ways to pay a family caregiver, but it is not about respite specifically. | `competitive-analysis-4/live-pages/ny-nysofa-26-tam-01-caregiver-directed-respite.txt`, `arch-how-do-i-get-paid-to-be-a-family-caregiver.txt` |
| 15 | VA, 4 Parent refuses | No: nothing works unless the veteran agrees and applies with the caregiver. | Partly: the veteran must agree, but the VA offers tips for a veteran who resists care. | No to Partly | `va-caregiver/AUDIT-PASS3.md` |
| 16 | VA, 5 Relatives share | Partly: the veteran can name up to 2 backup caregivers. | Partly: the veteran can name 2 backup caregivers, and in one program can hire a family member or neighbor as a paid helper. | Wording. Saved page confirms it. It does not say whether a spouse can be hired, and it is for enrolled veterans only. | `competitive-analysis-4/live-pages/va-veteran-directed-care.txt` |

## Competitor profiles and business model tables (4a and 4b)

| # | Competitor and column | Old cell | Proposed cell | Evidence |
|---|---|---|---|---|
| 17 | Cariloop, Weaknesses and Who pays | Available only through employers with 100 or more workers. | Available only through employers or insurers, usually with 100 or more workers. | `cariloop/AUDIT-PASS3.md` (live FAQ) |
| 18 | Care managers, Weaknesses | Cost $150 to $300 an hour, offer unclear services, and sometimes never make the agreed care plan. | Cost $150 to $350 an hour, though some families report paying less. Services vary, and some never make the agreed care plan. | `aging-life-care/AUDIT-PASS3.md` |
| 19 | Area Agencies, Weaknesses | Mostly referrals, long waitlists, hard-to-reach staff and strict eligibility. | Mostly referrals through the Eldercare Locator, and what local agencies give varies. Long waitlists, hard-to-reach staff and strict eligibility. | `area-agencies-on-aging/AUDIT-PASS3.md` |
| 20 | VA, Type | Indirect (government; veterans with a 70%+ rating) | Indirect (government; veterans' families). The comprehensive program needs a 70% rating, and the general program does not. | `va-caregiver/AUDIT-PASS3.md` |

## What this does not change

- The 5 needs, the 5 business questions and the 4 gaps stay as they are. The 4 gaps still hold: nothing here makes any competitor strong on a refusing parent or on relatives sharing the work.
- Group texts and Everplans, relatives share (Partly) stay as they are. The audit found them consistent with the evidence.
- The market analysis and the audience segmentation.

## Limits

- The new cells come from the audited verdict tables, not from re-reading every source file.
- Rows 12, 13, 14 and 16 rest on pages the auditors first read live. A helper then saved them (`docs/sources/competitive-analysis-4/live-pages/`) and confirmed the claims with limits, which the proposed cells now state. Four of the five claims held. The fifth, ARCH, held only partly, so row 14 relies on the New York memo.
- Rows 4 and 5 move Yes to Partly, and rows 8, 12, 14 and 15 move No to Partly, and row 11 moves Partly to No. These changes are the ones most open to the owner's judgment.
