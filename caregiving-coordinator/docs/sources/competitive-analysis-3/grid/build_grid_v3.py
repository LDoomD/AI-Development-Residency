"""Competitive Analysis 3 grid, VERSION 3 (2026-11-04): version 2 (approved) plus 2 rows for exhaustion,
"Respite and adult day services" and "VA caregiver programs" (checklist: docs/research-checklist-ca3-exhaustion.md).
Version 2 rows are copied unchanged from build_grid_v2.py. New source types:
  r  = a relief reader code (market-analysis-3/segments-11-12/codes): (id, field, exact text in that field)
  rc = a relief barrier count: (subset, barrier) must be > 0 in that subset (respite_adultday or va)
Writes grid-v3.json and business-v2.json."""
import json, re, pathlib, collections, sys, io, contextlib
H = pathlib.Path(__file__).parent; S = H.parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    v2 = {"__file__": str(H / "build_grid_v2.py")}; exec(open(H / "build_grid_v2.py").read(), v2)
    b1 = {"__file__": str(H / "build_business.py")}; exec(open(H / "build_business.py").read(), b1)
COLS = v2["COLS"]; G = dict(v2["G"]); BCOLS = b1["COLS"]; BG = dict(b1["G"])
VA = "competitors-4/va-caregiver/"; VAP = VA + "www_va_gov_family_and_caregiver_benefits_health_and_disability_comprehensive_ass.txt"; VAH = VA + "www_caregiver_va_gov.txt"
ALZ = [p for p in (S / "competitors-4/adult-day").glob("*.txt")][0].relative_to(S).as_posix()
HOS = "competitors-4/hospice-respite/www_medicare_gov_coverage_hospice_care.txt"; ARCH = "competitors-4/respite-arch/archrespite_org.txt"
RA = "respite_adultday"
G["Respite and adult day services"] = [
 ("Indirect (local care services)", [("q", ARCH, "Find a Respite Provider")]),
 ("11 Respite care and adult day services", [("q", ARCH, "Types of Respite")]),
 ("archrespite.org (to find one)", [("q", ARCH, "ARCH National Respite Network & Resource Center")]),
 ("In-home sitters, short facility stays, hospice respite, and adult day centers with activities, meals and rides.", [("r", "agingcare-498174", "help", "in-home respite"), ("q", HOS, "short-term care to help give caregivers a rest"), ("q", ALZ, "transportation and meals are often provided"), ("q", ALZ, "staffed activities such as music and exercise programs")]),
 ("Trained staff take over the care, so the caregiver gets real time off.", [("q", ALZ, "you'll have time to rest, run errands or finish other tasks")]),
 ("Give caregivers sleep, trips, dates and time alone while the parent is cared for.", [("r", "p14seksz", "helped", None), ("rhelp", RA, "can go on vacation"), ("rhelp", RA, "date with spouse"), ("rhelp", RA, "real sleep improved depression"), ("rhelp", RA, "massage and quiet time alone")]),
 ("Cost too much, have waitlists and minimum stays, and many parents refuse to go.", [("rc", RA, "cost"), ("rc", RA, "waitlist or no openings"), ("rc", RA, "too few hours, minimum stays or other limits"), ("rc", RA, "the parent refuses")]),
 ("Families pay, often on sliding scales. Medicaid, the VA and hospice cover some.", [("q", ALZ, "Many centers offer services on sliding scales, where caregivers pay according to ability or income."), ("q", ALZ, "In some states, Medicaid covers cost for people with very low income and few assets."), ("q", VAP, "At least 30 days of respite care per year."), ("q", HOS, "You may pay 5% of the Medicare-approved amount for inpatient respite care")]),
 ("No: gives a break, not guidance on behavior or next steps.", [("q", ALZ, "staffed activities such as music and exercise programs")]),
 ("Yes, when families can get it: time to rest, run errands and travel.", [("q", ALZ, "you'll have time to rest, run errands or finish other tasks"), ("rhelp", RA, "can go on vacation")]),
 ("No: adds eligibility rules and applications instead of handling them.", [("rc", RA, "hard application or eligibility rules")]),
 ("No: the parent refusing to go is a top reason respite goes unused.", [("rc", RA, "the parent refuses")]),
 ("No: nothing helps relatives share. Family not helping keeps caregivers from taking breaks.", [("rc", RA, "family or friends won't help")])]
G["VA caregiver programs"] = [
 ("Indirect (government program)", [("q", VAH, "Compr Assistance Family Caregivers (PCAFC)")]),
 ("11 Respite care and adult day services (VA benefits for veterans' families)", [("q", VAP, "At least 30 days of respite care per year.")]),
 ("caregiver.va.gov", [("q", VAH, "VA Caregiver Support Line (CSL)")]),
 ("Respite of at least 30 days a year, a monthly stipend, counseling, training, legal and financial planning, and a support line.", [("q", VAP, "At least 30 days of respite care per year."), ("q", VAH, "Education and training, health insurance (if caregiver is otherwise uninsured), mental health counseling, monthly financial stipend, respite care and other services."), ("q", VAP, "Free legal and financial planning assistance"), ("q", VAH, "VA Caregiver Support Line (CSL)")]),
 ("Pays family caregivers directly and lets the veteran name up to 2 backup caregivers.", [("q", VAP, "A monthly stipend (payment)."), ("q", VAP, "Up to 2 secondary family caregivers")]),
 ("Pays caregivers, funds home aides and respite, and teaches care tips.", [("r", "p1l9w918", "helped", "monthly payments"), ("r", "p1ifpmxx", "helped", "VA got dad an aide"), ("r", "p1l9w918", "helped", "30 days respite care"), ("r", "p1udyrtl", "helped", "learned new tips")]),
 ("Slow, uncertain approvals, capped aide hours, and unreliable aides.", [("rc", "va", "hard application or eligibility rules"), ("r", "p1mbxwso", "barriers", "other: seven months to get approved"), ("rc", "va", "too few hours, minimum stays or other limits"), ("rc", "va", "no trained or reliable providers")]),
 ("The VA pays. Only veterans' families who qualify can use it.", [("r", "p1x2f8kr", "payer_cost", "VA pays the agency"), ("q", VAP, "You may be eligible if you and the Veteran you’re caring for meet all of these requirements.")]),
 ("Partly: training and a support line, for veterans' families only.", [("q", VAH, "Education and training"), ("q", VAH, "VA Caregiver Support Line (CSL)")]),
 ("Yes, if approved: at least 30 days of respite a year and paid aide hours.", [("q", VAP, "At least 30 days of respite care per year."), ("r", "p1l9w918", "helped", "20 hours a week home caregiver")]),
 ("Partly: free legal and financial planning and a stipend. Approval can take months.", [("q", VAP, "Free legal and financial planning assistance"), ("q", VAP, "A monthly stipend (payment)."), ("r", "p1mbxwso", "barriers", "other: seven months to get approved")]),
 ("No: the veteran must meet the rules and apply with the caregiver.", [("q", VAP, "You may be eligible if you and the Veteran you’re caring for meet all of these requirements."), ("q", VAP, "Veteran and the new caregiver will need to submit a new application")]),
 ("Partly: the veteran can name up to 2 backup caregivers.", [("q", VAP, "Up to 2 secondary family caregivers")])]
BG["Respite and adult day services"] = [
 ("Fees per day or stay, sliding scales, and payments from Medicaid, the VA and Medicare hospice.", [("q", ALZ, "Many centers offer services on sliding scales, where caregivers pay according to ability or income."), ("q", ALZ, "In some states, Medicaid covers cost for people with very low income and few assets."), ("q", VAP, "At least 30 days of respite care per year."), ("q", HOS, "Medicare will cover your stay in the facility")]),
 None,
 ("Demand outruns supply: many areas have waitlists.", [("rc", RA, "waitlist or no openings")]),
 ("In person: trained staff, activities, meals and often rides.", [("q", ALZ, "staffed activities such as music and exercise programs"), ("q", ALZ, "transportation and meals are often provided")]),
 ("Find a provider, then tour, apply, meet eligibility rules and often wait.", [("q", ARCH, "Find a Respite Provider"), ("q", ARCH, "How to Choose a Respite Provider"), ("rc", RA, "hard application or eligibility rules"), ("rc", RA, "waitlist or no openings")])]
BG["VA caregiver programs"] = [
 ("No revenue: a federal benefit for veterans' families.", [("q", VAP, "Program of Comprehensive Assistance for Family Caregivers (PCAFC)"), ("r", "p1x2f8kr", "payer_cost", "VA pays the agency")]),
 None,
 ("Ongoing benefits with reassessments. Families stay while they qualify.", [("q", VAH, "PCAFC Reassessments"), ("q", VAH, "will not experience a decrease in the monthly stipend amount based on a reassessment")]),
 ("Local caregiver support teams and a weekday phone line. Some calls go unanswered.", [("q", VAP, "Monday through Friday, 8:00 a.m. to 8:00 p.m. ET"), ("r", "p1vfh78m", "barriers", "other: nobody called back")]),
 ("The veteran and caregiver apply together online, by mail or in person. Approval can take months.", [("q", VAP, "You can apply online, by mail, or in person."), ("r", "p1mbxwso", "barriers", "other: seven months to get approved")])]
for k in ["Respite and adult day services", "VA caregiver programs"]: BG[k][1] = G[k][7]
# relief codes and subsets
RS = S / "market-analysis-3/segments-11-12"
sys.path.insert(0, str(RS))
with contextlib.redirect_stdout(io.StringIO()):
    import count_results as cr
codes = {c["id"]: c for c in cr.codes}; rel = [c for c in cr.codes if c.get("relevant")]
SUB = {RA: [c for c in rel if cr.is_resp(c) or "adult day program" in c.get("help", [])],
       "va": [c for c in rel if "VA" in (c.get("provider") or "") or any("VA" in h for h in c.get("help", []))]}
def bcount(sub, b): return sum(1 for c in SUB[sub] if b in {cr.group_other(x) if x.startswith("other: ") else x for x in c.get("barriers", [])})
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")).strip()
def verify(grid, cols, label):
    ca2 = norm(open(S.parent / "competitive-analysis-2.md").read()); th = json.load(open(S / "competitive-analysis-3/5b/themes-5b.json"))
    c5b = {c["id"]: c for k in (1, 2) for c in json.load(open(S / f"competitive-analysis-3/5b/codes-{k}.json"))}
    bad = n = 0
    for comp, cells in grid.items():
        for (text, srcs), col in zip(cells, cols):
            lim = 30 if col in ("What they do well", "What they don't do well") or label == "business" else (30 if comp in ("Respite and adult day services", "VA caregiver programs") and col in COLS[3:5] else 16)
            if len(text.split()) > max(lim, 16) and col not in COLS[3:5]: print("LONG", comp, col); bad += 1
            if ";" in text or (col not in COLS[:3] and re.search(r"\b(evidence|mentions?|claims?|reviews?|posts?|data|sources?)\b|\(", text, re.I)): print("WORDING", comp, col, text); bad += 1
            for s in srcs:
                n += 1; t = s[0]
                if t == "c" and norm(s[1]) not in ca2: print("CA2 missing", comp, s[1][:50]); bad += 1
                elif t == "q" and norm(s[2]) not in norm(open(S / s[1]).read()): print("quote missing", comp, s[2][:60]); bad += 1
                elif t == "t" and not th.get(s[1], {}).get(s[2], {}).get(s[3]): print("theme missing", comp, s[3]); bad += 1
                elif t == "k" and s[2] not in c5b[s[1]]["problems"] + c5b[s[1]]["worked"]: print("5b code missing", comp, s[1]); bad += 1
                elif t == "r":
                    c = codes.get(s[1]); v = c and c.get(s[2])
                    ok = c and c.get("relevant") and (s[3] is None and v or (isinstance(v, list) and s[3] in v) or (isinstance(v, str) and s[3] and s[3] in v))
                    if not ok: print("relief code missing", comp, s[1], s[2], s[3]); bad += 1
                elif t == "rhelp" and not any(s[2] == g.lower() for c in SUB[s[1]] for g in c.get("helped", [])): print("helped missing", comp, s[2]); bad += 1
                elif t == "rc" and bcount(s[1], s[2]) == 0: print("count zero", comp, s[2]); bad += 1
                elif t == "x": print("NO-DATA", comp); bad += 1
    print(f"{label}: cells {sum(len(v) for v in grid.values())}, sources {n}, problems {bad}")
verify(G, COLS, "grid"); verify(BG, BCOLS, "business")
counts = {sub: {"posts": len(rows), "barriers": {b: bcount(sub, b) for b in ["cost", "waitlist or no openings", "too few hours, minimum stays or other limits", "the parent refuses", "hard application or eligibility rules", "family or friends won't help", "no trained or reliable providers"]}} for sub, rows in SUB.items()}
json.dump({"columns": COLS, "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}, "relief_counts_behind_rc": counts}, open(H / "grid-v3.json", "w"), indent=1, ensure_ascii=False)
json.dump({"columns": BCOLS, "rows": {k: [c[0] for c in v] for k, v in BG.items()}, "sources": {k: [c[1] for c in v] for k, v in BG.items()}}, open(H / "business-v2.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps(counts))
