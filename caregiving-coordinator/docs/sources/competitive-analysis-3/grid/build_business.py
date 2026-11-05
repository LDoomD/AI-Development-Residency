"""Competitive Analysis 3, business questions table (2026-11-04). Added after the owner asked for the business
questions from the board's "Questions to answer about the competitors" (Figma 4:533) to come back.
Same source types and cell rules as build_grid_v2.py: q = exact quote in a saved file, c = exact text in
docs/competitive-analysis-2.md, t = a 5b theme, k = a 5b reader code. Writes business.json."""
import json, re, pathlib
H = pathlib.Path(__file__).parent; S = H.parents[1]
COLS = ["How do they make money?", "Who pays, and the cost", "How do they keep customers?", "How do they approach customer experience?", "What does it take to get started?"]
B5 = "competitors-4/basics-5a.json"; AARP = "competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt"
CLF = "competitors/cariloop/www_cariloop_com_about_us_faqs.txt"; CLH = "competitors/cariloop/www_cariloop_com_.txt"; CLP = "competitors/cariloop/www_cariloop_com_privacy_policy.txt"
APA = "competitors/a-place-for-mom/www_aplaceformom_com_about.txt"; APH = "competitors/a-place-for-mom/www_aplaceformom_com_.txt"; APU = "competitors/a-place-for-mom/www_aplaceformom_com_about_us.txt"
EL = "competitors-4/eldercare-locator/www_usaging_org_eldercareloc.txt"; ELH = "competitors-4/eldercare-locator/eldercare_acl_gov_home.txt"
AA = "Eldercare Locator and Area Agencies on Aging"; GC = "Geriatric care managers"
grid = json.load(open(H / "grid-v2.json")); PAY = {k: v[7] for k, v in grid["rows"].items()}; PAYSRC = {k: v[7] for k, v in grid["sources"].items()}
G = {
"Caring Village": [
 ("Monthly subscriptions, a free plan with ads, sales to businesses and gift subscriptions.", [("c", "Freemium subscription. A free plan with ads, plus paid Circle and Village plans. It also sells to businesses for their patients or clients, and offers gift subscriptions.")]),
 None,
 ("The free plan caps at 2 members, pushing families to pay. Daily to-dos and reminders bring people back. Use ends when the parent dies.", [("c", "The free plan's 2-member limit pushes larger families to pay, and daily to-dos, reminders and journal likes bring people back."), ("c", "Use ends when the loved one dies (2).")]),
 ("Self-serve: help center, email, guided setup and an AI assistant. No phone support.", [("c", "Self-serve: a help center, a support email, guided setup, checklists and the Julia AI assistant. No phone support or hours are listed.")]),
 ("Sign up with email, Apple or Google in minutes, then invite relatives. Works on iPhone, Android and the web.", [("c", "The caregiver signs up with email, Apple or Google and is walked through it in a few minutes, then invites others. Works on iPhone, Android and the web.")])],
"Everplans": [
 ("Yearly subscriptions, plus deals through financial advisors and partners.", [("c", "Freemium: free (3 items) or Premium at $99.99 a year, plus deals through financial advisors and partners.")]),
 None,
 ("The free plan stops at 3 items. Date reminders bring people back.", [("c", "The free tier stops at 3 items, and date reminders bring people back.")]),
 ("Self-serve: FAQs, a contact form, articles and checklists.", [("c", "Self-serve: FAQs, a contact form, articles and checklists.")]),
 ("The parent fills in their own plan on the web or the app.", [("c", "The person fills in their own plan on the web or the app.")])],
"Cariloop": [
 ("Employer contracts, priced per employee per month or in blocks of cases.", [("q", CLF, "While the vast majority of our work is done on a per employee per month basis, we also offer our services in blocks of cases.")]),
 None,
 ("Employer contracts. Members who leave the job get 30 days to switch to a paid individual plan.", [("q", CLF, "a 30-day countdown is triggered within our platform that allows the member to shift to an individual membership that they can cover the cost of on their own")]),
 ("Full-time care coaches who answer in under 2 hours on average.", [("q", CLF, "All of our Care Coaches are full-time, W2 employees of Cariloop."), ("q", CLH, "Timely access with average response times under 2 hours")]),
 ("An employer benefit first, then the web or mobile app.", [("q", CLF, "Typically our minimum size group is 100 employees"), ("q", CLP, "download and use our mobile application (whether it is the web application or the mobile application)")])],
"A Place for Mom": [
 ("Referral fees: senior living places pay when a family moves in, and home care agencies pay per referral.", [("q", APA, "A Place for Mom is paid by our senior living network communities when a family we refer chooses to move into a community."), ("q", APA, "We are paid by home care agencies each time we refer a family to them.")]),
 None,
 ("Families are leads, not paying customers. Signing up allows calls and texts from its paying communities.", [("q", APH, "You also consent to receive texts and calls from us and our community customers, including telemarketing and/or advertising")]),
 ("A free local advisor, a care quiz and a cost calculator.", [("q", APU, "Connect with a local advisor"), ("q", APH, "Take our free care quiz for personalized senior living advice"), ("q", APH, "Try our senior living cost calculator")]),
 ("Take a care quiz or contact a local advisor. Sales calls from communities follow.", [("q", APH, "Take our free care quiz for personalized senior living advice"), ("q", APU, "Connect with a local advisor"), ("t", "A Place for Mom", "problems", "Nonstop calls and spam that won't stop")])],
GC: [
 ("Hourly fees of $150 to $300, a one-time first assessment, and sometimes travel time.", [("q", AARP, "Professionals charge by the hour, ranging from $150 to $300, depending on the geographic region."), ("q", AARP, "Many begin with an initial assessment of 4 to 6 hours, which may require a one-time charge."), ("q", AARP, "Some also charge for mileage and travel time.")]),
 None,
 ("Ongoing retainers and regular home visits. Families pay even in quiet months.", [("k", "p1woat2e", "regular home visits to know parent"), ("k", "p1woat2e", "paying retainer for little in quiet periods")]),
 ("In person: home visits, doctor appointments, and reports back to the family.", [("k", "p1woat2e", "regular home visits to know parent"), ("t", GC, "worked", "Goes to appointments and reports back")]),
 ("A paid first assessment of 4 to 6 hours in the parent's home.", [("q", AARP, "Many begin with an initial assessment of 4 to 6 hours, which may require a one-time charge."), ("q", B5, "An in-person assessment gives them the opportunity to observe the home environment")])],
"Group texts and notebooks": [
 ("None: free tools families already have.", [("c", "Not a company. Free.")]),
 None,
 ("None. Caregivers mute, leave or refuse group chats to protect themselves.", [("c", "Caregivers mute, leave or refuse group chats to protect themselves (4).")]),
 ("None. No company stands behind them.", [("c", "Not a company.")]),
 ("Nothing to install. Getting everyone onto one app is hard.", [("c", "Nothing new to install, but getting everyone onto one app is hard (2).")])],
"Area Agencies on Aging": [
 ("No revenue: federal funding through the Administration on Aging, with grants to states.", [("q", EL, "The Locator was established and is funded by the U.S. Administration on Aging"), ("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "provides grants to states and territories")]),
 None,
 ("None: a free public service with no paying customers.", [("q", EL, "The Locator was established and is funded by the U.S. Administration on Aging")]),
 ("Phone, text, chat or email with trained staff. Staff are kind but often hard to reach.", [("q", ELH, "Call or send a text message to trained staff."), ("t", AA, "worked", "Helpful, kind or quick staff"), ("t", AA, "problems", "Hard to reach or staff didn't know")]),
 ("Contact the Eldercare Locator, then meet eligibility rules and wait for services.", [("q", ELH, "Welcome to the Eldercare Locator"), ("t", AA, "problems", "Little help, or strict eligibility"), ("t", AA, "problems", "Long waits, low priority, no timeline")])]}
for k in G: G[k][1] = (PAY[k], [tuple(s) for s in PAYSRC[k]])
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")).strip()
def verify():
    ca2 = norm(open(S.parent / "competitive-analysis-2.md").read()); th = json.load(open(S / "competitive-analysis-3/5b/themes-5b.json")); bad = n = 0
    codes = {c["id"]: c for k in (1, 2) for c in json.load(open(S / f"competitive-analysis-3/5b/codes-{k}.json"))}
    for comp, cells in G.items():
        for (text, srcs), col in zip(cells, COLS):
            if len(text.split()) > 30: print("LONG", comp, col); bad += 1
            if ";" in text or re.search(r"\b(evidence|mentions?|claims?|reviews?|posts?|data|sources?)\b|\(", text, re.I): print("WORDING", comp, col, text); bad += 1
            for s in srcs:
                n += 1
                if s[0] == "c" and norm(s[1]) not in ca2: print("CA2 missing", comp, s[1][:60]); bad += 1
                if s[0] == "q" and norm(s[2]) not in norm(open(S / s[1]).read()): print("quote missing", comp, s[2][:60]); bad += 1
                if s[0] == "t" and not th.get(s[1], {}).get(s[2], {}).get(s[3]): print("theme missing", comp, s[3]); bad += 1
                if s[0] == "k" and s[2] not in codes[s[1]]["problems"] + codes[s[1]]["worked"]: print("code missing", comp, s[1]); bad += 1
                if s[0] == "x": print("NO-DATA", comp, col); bad += 1
    print(f"cells {sum(len(v) for v in G.values())}, sources checked {n}, problems {bad}")
verify()
json.dump({"columns": COLS, "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}}, open(H / "business.json", "w"), indent=1, ensure_ascii=False)
