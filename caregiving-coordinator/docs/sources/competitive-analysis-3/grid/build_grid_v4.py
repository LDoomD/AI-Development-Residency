"""Competitive Analysis 3 grid VERSION 4 and business table VERSION 3 (2026-11-05): version 3 with the owner-approved
fixes from the audit (docs/reports/audit-2026-11-05-results.md, items C1-C3). Only cells of the two exhaustion rows
change. Every new cell is checked against saved sources by version 3's verify(). Writes grid-v4.json, business-v3.json."""
import json, pathlib, io, contextlib
H = pathlib.Path(__file__).parent
v3 = {"__file__": str(H / "build_grid_v3.py")}
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(H / "build_grid_v3.py").read(), v3)
G, BG, ALZ, HOS, ARCH, VAP, RA = v3["G"], v3["BG"], v3["ALZ"], v3["HOS"], v3["ARCH"], v3["VAP"], v3["RA"]
VAR = "competitors-4/va-caregiver/www_va_gov_geriatrics_pages_respite_care_asp.txt"
R, V = "Respite and adult day services", "VA caregiver programs"
G[R][4] = ("Staff take over the care for hours or days, so the caregiver can rest and run errands.", [("q", ALZ, "you'll have time to rest, run errands or finish other tasks")])
G[R][7] = ("Mostly families. Medicaid helps very low incomes, hospice the dying, and the VA some veterans.", [("q", ALZ, "Many centers offer services on sliding scales, where caregivers pay according to ability or income."), ("q", ALZ, "In some states, Medicaid covers cost for people with very low income and few assets."), ("q", HOS, "certify that you’re terminally ill"), ("q", VAR, "A copay for Respite Care may be charged based on your VA service-connected disability status and financial information.")])
G[R][8] = ("Partly: some adult day centers offer family counseling and behavior help. Respite itself is a break.", [("q", ALZ, "Counseling: The center may provide support services for people with dementia and their families."), ("q", ALZ, "Behavior management: Find out if the center is prepared to deal with behaviors associated with dementia.")])
G[R][10] = ("No: doesn't touch the parent's money, papers or accounts. Applying adds more paperwork.", [("rc", RA, "hard application or eligibility rules")])
G[V][3] = ("Respite of at least 30 days a year, a monthly stipend, counseling, training, legal and financial planning, and a support line. The stipend, planning help and 30 days of respite require the veteran to have a 70% or higher disability rating.", G[V][3][1] + [("q", VAP, "The Veteran has a VA disability rating (individual or combined) of 70% or higher"), ("q", VAP, "Eligible primary family caregivers may also receive these benefits: A monthly stipend (payment).")])
G[V][6] = ("Strict rules to qualify, limited aide hours, and unreliable aides.", [("rc", "va", "hard application or eligibility rules"), ("rc", "va", "too few hours, minimum stays or other limits"), ("rc", "va", "no trained or reliable providers")])
G[V][7] = ("The VA pays, though respite may have a copay. Only qualifying veterans' families can use it.", [("r", "p1x2f8kr", "payer_cost", "VA pays the agency"), ("q", VAR, "A copay for Respite Care may be charged"), ("q", VAP, "You may be eligible if you and the Veteran you’re caring for meet all of these requirements.")])
G[V][11] = ("No: nothing works unless the veteran agrees and applies with the caregiver.", [("q", VAP, "You may be eligible if you and the Veteran you’re caring for meet all of these requirements."), ("q", VAP, "Veteran and the new caregiver will need to submit a new application")])
BG[R][0] = ("Fees, sliding scales at many adult day centers, state respite vouchers, and some payment from Medicaid, the VA and hospice.", [("q", ALZ, "Many centers offer services on sliding scales, where caregivers pay according to ability or income."), ("q", ARCH, "Respite Voucher Programs"), ("q", ALZ, "In some states, Medicaid covers cost for people with very low income and few assets."), ("q", HOS, "Medicare will cover your stay in the facility")])
BG[R][2] = ("Families come back for regular days or repeat stays while the parent needs care.", [("q", ALZ, "you'll have time to rest, run errands or finish other tasks"), ("rhelp", RA, "got weekends back"), ("rhelp", RA, "two in-office work days a week")])
BG[R][3] = ("In person: staff, activities, meals and often rides.", [("q", ALZ, "staffed activities such as music and exercise programs"), ("q", ALZ, "transportation and meals are often provided")])
BG[V][4] = ("The veteran and caregiver apply together online, by mail or in person. One caregiver waited 7 months for approval.", [("q", VAP, "You can apply online, by mail, or in person."), ("r", "p1mbxwso", "barriers", "other: seven months to get approved")])
for k in (R, V): BG[k][1] = G[k][7]
v3["verify"](G, v3["COLS"], "grid v4"); v3["verify"](BG, v3["BCOLS"], "business")
json.dump({"columns": v3["COLS"], "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}}, open(H / "grid-v4.json", "w"), indent=1, ensure_ascii=False)
json.dump({"columns": v3["BCOLS"], "rows": {k: [c[0] for c in v] for k, v in BG.items()}, "sources": {k: [c[1] for c in v] for k, v in BG.items()}}, open(H / "business-v3.json", "w"), indent=1, ensure_ascii=False)
