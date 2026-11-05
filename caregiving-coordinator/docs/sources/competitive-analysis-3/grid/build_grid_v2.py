"""Competitive Analysis 3 grid, VERSION 2 (2026-11-04): every cell rewritten as a direct, plain answer to its column's question.
Version 1 (build_grid.py, grid.json) is kept unchanged.
Competitive Analysis 3 grid: 7 competitors x template columns + 5 criteria. Every cell has a source:
 q = exact quote in a saved file (path from docs/sources/), c = exact text in docs/competitive-analysis-2.md,
 t = a theme in competitive-analysis-3/5b/themes-5b.json (competitor, kind, theme), n = a count file, k = a reader code in 5b/codes-*.json (id, exact text in its problems/worked list). x is no longer allowed.
verify() checks every source. Writes grid.json."""
import json, re, pathlib
H = pathlib.Path(__file__).parent; S = H.parents[1]
CA2 = "competitive-analysis-2.md"
COLS = ["Type", "Market segment", "Website", "Main features", "How they stand out", "What they do well", "What they don't do well", "Who pays, and the cost",
        "1. Understand, handle behavior, know what to do", "2. Real relief for the caregiver", "3. Money, papers, accounts", "4. Works when the parent refuses help", "5. Relatives share the work"]
CV = "competitors/caring-village/www_caringvillage_com_about.txt"; B5 = "competitors-4/basics-5a.json"
RT = "competitive-analysis-3/grid/reddit-threads/"; GP = "competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt"; BBB = "competitors-4/review-sites/bbb_2026-11-04.txt"
AARP = "competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt"; ACL = "competitors-4/manual-saves/acl_gov_nfcsp.txt"; AA = "Eldercare Locator and Area Agencies on Aging"
G = {
"Caring Village": [
 ("Direct (business)", [("c", "Direct (coordination)")]),
 ("1 Family care-coordination apps", [("c", "Family care-coordination apps")]),
 ("caringvillage.com", [("c", "https://caringvillage.com/")]),
 ("A shared family app with a calendar, to-dos, medication lists, documents and an AI helper.", [("c", "calendar, to-dos, medication lists, care plan, journal, group messages, document storage")]),
 ("Built by former caregivers as one place for the whole family's care.", [("c", "Claims to be one 'command center'")]),
 ("Shared calendar and medication list keep all siblings on the same care information.", [("c", "Keeps the whole family updated and on the same page (10 of 29)"), ("c", "Families mainly use the shared calendar (6) and medication lists (6)"), ("c", "less back-and-forth than texting (3)")]),
 ("Loses entries, resets the care plan, shows medical details to friends, and cannot get relatives to join.", [("c", "the daily care plan resets or is too rigid (3)"), ("c", "bugs and lost entries (3)"), ("c", "'friends' can see private medical details (2)"), ("c", "it's hard to get everyone into the group (2)")]),
 ("The caregiver pays: free for 2 people, or $14.99 to $24.99 a month.", [("c", "Circle: $14.99 a month"), ("c", "Village: $24.99 a month")]),
 ("Partly: an AI helper answers care questions. No help with dementia behavior.", [("q", CV, "get 24/7 guidance from Julia, our AI caregiving assistant"), ("c", "calendar, to-dos, medication lists, care plan, journal, group messages, document storage")]),
 ("Partly: less stress and back-and-forth. Takes no care tasks off the caregiver.", [("c", "say it means less stress (5)"), ("c", "less back-and-forth than texting (3)")]),
 ("Partly: stores documents. No help getting into bank, insurer or portal accounts.", [("c", "group messages, document storage"), ("c", "It doesn't help with getting into the parent's bank, insurer or portal accounts")]),
 ("No: nothing for a parent who refuses help.", [("c", "calendar, to-dos, medication lists, care plan, journal, group messages, document storage")]),
 ("Partly: relatives join free with their own login. Can't make them do tasks.", [("c", "each joins free with their own account"), ("c", "can't make relatives help")])],
"Everplans": [
 ("Direct (business)", [("c", "Direct (access to accounts)")]),
 ("10 Digital vaults and emergency access", [("c", "Digital vaults and emergency access")]),
 ("everplans.com", [("c", "https://www.everplans.com/")]),
 ("Online vault for documents, accounts and wishes, shared with chosen family.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("Walks a person through organizing all their life details and next steps.", [("c", "Claims to organize all of a person's life details")]),
 ("Gives adult children the parent's accounts, insurance policies and end-of-life wishes in one place.", [("q", RT + "everplans_y4q1tc.txt", "access all of their financial information, medical end-of-life wishes, insurance policies"), ("q", "app-reviews/reviews4.csv", "After my dad passed away, we discovered a wealth of notes he had left for us")]),
 ("Useless unless the parent filled it in. The iPad app runs only at phone size.", [("c", "Everplans needs the parent to set everything up ahead of time"), ("c", "the iPad app is only a phone-size version (5 of 7)")]),
 ("The parent pays: free for 3 items, or $99.99 a year.", [("c", "Premium at $99.99 a year"), ("c", "People organizing their own affairs pay for Premium themselves")]),
 ("No: stores papers only. No care or behavior advice.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("No: takes no care work or time off the caregiver.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("Yes, if the parent fills it in: accounts, papers, insurance and wishes in one vault.", [("q", RT + "everplans_y4q1tc.txt", "access all of their financial information, medical end-of-life wishes, insurance policies"), ("c", "Everplans needs the parent to set everything up ahead of time")]),
 ("No: the parent must fill it in and can lock sections until death.", [("q", RT + "everplans_1eaenyg.txt", "Your parent can LOCK areas they don’t want shared until their death"), ("c", "Everplans needs the parent to set everything up ahead of time")]),
 ("Partly: relatives see chosen sections. Nothing splits the work.", [("c", "deputies' who get access to chosen sections")])],
"Cariloop": [
 ("Direct (business, employer-paid)", [("q", B5, "Typically our minimum size group is 100 employees")]),
 ("7 Employer and health-plan caregiver benefits", [("q", B5, "The caregiving benefit for every employee")]),
 ("cariloop.com", [("q", B5, "SOURCE: https://www.cariloop.com/")]),
 ("A personal care coach, a care-booking marketplace, a family Care Team and document storage.", [("q", B5, "Give your employees access to a dedicated Coach"), ("q", B5, "Employees can search, compare, book, and pay for care all in one place."), ("q", GP, "Add whoever needs to be involved in the care of your loved ones to your Care Team")]),
 ("Full-time coaches who take no money from the care providers they suggest.", [("q", B5, "All of our Care Coaches are full-time, W2 employees of Cariloop."), ("q", B5, "We do not accept referral, lead generation, or subscription fees of any kind from any healthcare provider.")]),
 ("Assigns a full-time care coach who guides families through a crisis.", [("q", B5, "All of our Care Coaches are full-time, W2 employees of Cariloop."), ("q", GP, "Staff wonderful incredibly helpful in your time of need"), ("q", RT + "cariloop_sichx0.txt", "I have personally used the service and it could not have been more helpful.")]),
 ("Available only through employers with 100 or more workers. The app freezes.", [("q", B5, "Typically our minimum size group is 100 employees"), ("q", GP, "Won't let me exit app. I have to restart my phone to exit.")]),
 ("The employer pays. At MSU, keeping the coach yourself costs $249 a month.", [("q", B5, "employees have the option to extend the coaching for $249/month.")]),
 ("Yes: coaches explain diagnoses like Alzheimer's and find the right doctors and care.", [("q", GP, "Understanding diagnoses like ADHD, Alzheimer’s, Anxiety, Autism, Cancer, Down Syndrome, Parkinson’s, etc."), ("q", GP, "Finding the right type of doctor or specialist for a loved one")]),
 ("Partly: coaches find and book care. Only if the employer offers it.", [("q", B5, "Employees can search, compare, book, and pay for care all in one place."), ("q", B5, "Typically our minimum size group is 100 employees")]),
 ("Yes: help paying for care, with Medicare, Medicaid and VA benefits, and POAs.", [("q", GP, "Understanding how to pay for a loved one’s care"), ("q", GP, "Filling out important legal caregiving documents (wills, POAs, DNRs, etc.)"), ("q", GP, "Understanding a loved one’s Medicare, Medicaid, or VA benefits")]),
 ("Partly: coaches handle family dynamics. Nothing for a parent who refuses.", [("q", GP, "Managing family dynamics related to your loved one’s care")]),
 ("Partly: relatives join the Care Team and get updates. Tasks aren't split.", [("q", GP, "Add whoever needs to be involved in the care of your loved ones to your Care Team")])],
"A Place for Mom": [
 ("Direct (business)", [("q", B5, "A Place for Mom is a referral service.")]),
 ("4 Senior care referral and placement", [("q", B5, "A Place for Mom is a referral service.")]),
 ("aplaceformom.com", [("q", B5, "Find Assisted Living, Memory Care and Senior Living Near Me | A Place for Mom")]),
 ("A free advisor, a care and cost check, local places with prices, and tours.", [("q", B5, "Receive a free care and financial assessment"), ("q", B5, "Get clear pricing and details so you can make an informed decision.")]),
 ("Says it has the country's largest senior care network.", [("q", B5, "Our senior care network is the largest in the country")]),
 ("Lists nearby senior living options with prices and books tours.", [("q", BBB, "You helped me to figure out the process of finding a place for mom when I had no idea of where to even start"), ("q", BBB, "the setting up of appointments"), ("t", "A Place for Mom", "worked", "Shows options and some prices")]),
 ("Shares families' contact details, causing nonstop sales calls. Commission-paid advisors know little about the places.", [("q", BBB, "A Place for Mom has distributed my phone number and email to every assisted living facility in my area without my consent."), ("t", "A Place for Mom", "problems", "Nonstop calls and spam that won't stop"), ("t", "A Place for Mom", "problems", "Paid by commission, not truly free"), ("t", "A Place for Mom", "problems", "Doesn't know places or care about quality")]),
 ("Senior living places pay it when a family moves in. Free to families.", [("q", B5, "A Place for Mom is paid by our senior living network communities when a family we refer chooses to move into a community."), ("q", B5, "Our services—including personalized guidance and support—are always free to families.")]),
 ("Partly: an advisor guides the search. Advisors often don't know the places.", [("q", B5, "Receive a free care and financial assessment"), ("t", "A Place for Mom", "problems", "Doesn't know places or care about quality")]),
 ("Partly: saves search time. Nonstop calls add stress.", [("t", "A Place for Mom", "worked", "Shows options and some prices"), ("t", "A Place for Mom", "problems", "Nonstop calls and spam that won't stop")]),
 ("Partly: cost calculator and assessment. No help for Medicaid-only families.", [("q", B5, "Try our senior living cost calculator"), ("t", "A Place for Mom", "problems", "No help for Medicaid-only families")]),
 ("No: an advisor told one family to lie to the parent to move her.", [("q", BBB, "Told me the best way to get our mother in a nursing home is to just lie to her")]),
 ("No: one family contact. Nothing for relatives to share.", [("q", B5, "Receive a free care and financial assessment"), ("q", B5, "Get clear pricing and details so you can make an informed decision.")])],
"Geriatric care managers": [
 ("Direct (private professionals)", [("q", B5, "Count on paying out of pocket")]),
 ("None of the 14 segments (private care management)", [("q", B5, "These professionals act as advocates and guides for family members")]),
 ("aginglifecare.org (to find one)", [("q", B5, "for those who are members of the Aging Life Care Association")]),
 ("Home visits, care plans, hiring and checking aides, appointments, and help for families far away.", [("q", B5, "Evaluating, arranging for and monitoring hired caregivers, such as home health aides."), ("q", B5, "Acting as a liaison to families who may be hundreds of miles away."), ("q", AARP, "Creating short- and long-term care plans")]),
 ("Trained local professionals who see the parent and the home in person.", [("q", B5, "An in-person assessment gives them the opportunity to observe the home environment"), ("q", B5, "Our specialized experience and local connections can speed families through the roadblocks they often encounter.")]),
 ("Attend doctor visits, evaluate care facilities and arrange respite during a crisis.", [("t", "Geriatric care managers", "worked", "Takes load off in a crisis"), ("t", "Geriatric care managers", "worked", "Goes to appointments and reports back"), ("t", "Geriatric care managers", "worked", "Tours and evaluates places, finds resources"), ("q", AARP, "Arranging for relief or respite care for stressed-out caregivers."), ("q", AARP, "got the time back to take care of myself again")]),
 ("Cost $150 to $300 an hour, offer unclear services, and sometimes never make the agreed care plan.", [("q", B5, "Professionals charge by the hour, ranging from $150 to $300, depending on the geographic region."), ("t", "Geriatric care managers", "problems", "Unclear what they do or how to choose"), ("t", "Geriatric care managers", "problems", "Didn't deliver"), ("k", "p1x0fqwe", "never made the agreed care plan")]),
 ("The family pays $150 to $300 an hour. Medicare and Medicaid usually don't.", [("q", B5, "Professionals charge by the hour, ranging from $150 to $300, depending on the geographic region."), ("q", B5, "Neither Medicare nor Medicaid typically pays for care management services.")]),
 ("Yes: explain hard topics to the parent and family, and make a care plan.", [("q", AARP, "Explaining complex or difficult topics to care recipients and their families."), ("q", AARP, "Creating short- and long-term care plans")]),
 ("Yes, for a price: respite, doctor visits and place tours taken off the caregiver.", [("q", AARP, "Arranging for relief or respite care for stressed-out caregivers."), ("q", AARP, "got the time back to take care of myself again"), ("t", "Geriatric care managers", "worked", "Goes to appointments and reports back")]),
 ("Partly: advise on financial options. One took power of attorney without telling the family.", [("k", "agi-499305", "advises on financial options"), ("k", "p1x0fqwe", "took power of attorney without telling family")]),
 ("Partly: talk with the parent directly. Some parents still refuse them.", [("q", AARP, "Explaining complex or difficult topics to care recipients and their families."), ("t", "Geriatric care managers", "problems", "Family conflict or refusal around them")]),
 ("Partly: stand up to difficult relatives. Family fights often follow.", [("t", "Geriatric care managers", "worked", "Stands up to difficult relatives"), ("t", "Geriatric care managers", "problems", "Family conflict or refusal around them")])],
"Group texts and notebooks": [
 ("Indirect (workaround)", [("c", "Indirect (what families use instead)")]),
 ("What families use instead (not a company)", [("c", "Workaround, not a company")]),
 ("n/a", [("c", "n/a")]),
 ("Family group chats, notebooks, binders and whiteboards.", [("c", "Family group chats, group texts and WhatsApp groups"), ("c", "Notebooks, binders, whiteboards, wall calendars")]),
 ("Everyone already has them, they're free, and there's nothing to install.", [("c", "Everyone already has it, it's free, and there's nothing to install.")]),
 ("Reach every relative instantly for free. A whiteboard schedule reduces a parent's repeated questions.", [("c", "One place to tell the whole family what's happening (6 of 53)"), ("c", "Nearly free."), ("c", "A whiteboard with the date and schedule calms repeated questions")]),
 ("Help requests get ignored or just a 'like.' Notes and calendars get lost or erased.", [("c", "Requests and updates get silence or just a 'like' (10)"), ("c", "Notes and calendars get ignored, lost or erased (12)")]),
 ("Nobody: they're free or nearly free.", [("c", "Nearly free.")]),
 ("Partly: a written guide lets someone else step in. No advice on what to do.", [("c", "a written guide lets someone else step in (4)")]),
 ("No: constant messages wear the caregiver down.", [("c", "constant messages wear the caregiver down (7)")]),
 ("Partly: a binder holds papers. Records pile up and can't be searched.", [("c", "records pile up and can't be searched when a doctor asks (7)")]),
 ("Partly: work without the parent using any tech. Nothing helps when the parent refuses.", [("c", "it works without phones (4)")]),
 ("Partly: everyone hears at once. Requests get silence or a 'like'.", [("c", "Requests and updates get silence or just a 'like' (10)")])],
"Area Agencies on Aging": [
 ("Indirect (government program)", [("q", ACL, "provides grants to states and territories")]),
 ("None of the 14 segments (free public service)", [("q", "competitors-4/eldercare-locator/eldercare_acl_gov_home.txt", "a public service of the Administration for Community Living")]),
 ("eldercare.acl.gov (finds your local agency)", [("q", "competitors-4/eldercare-locator/eldercare_acl_gov_home.txt", "Welcome to the Eldercare Locator")]),
 ("Caregiver information, help finding services, counseling, support groups, training and respite.", [("q", ACL, "individual counseling, organization of support groups, and caregiver training"), ("q", ACL, "respite care; and")]),
 ("Local, government-funded and free to families who qualify.", [("q", ACL, "provides grants to states and territories")]),
 ("Connect families to free local services, support groups and Medicare counseling. Some fund respite.", [("t", AA, "worked", "Referrals to local services, groups and Medicare counseling"), ("t", AA, "worked", "Paid for respite or home help"), ("q", ACL, "provides grants to states and territories")]),
 ("Mostly referrals, long waitlists, hard-to-reach staff and strict eligibility.", [("t", AA, "problems", "Only referrals, nothing concrete"), ("t", AA, "problems", "Long waits, low priority, no timeline"), ("t", AA, "problems", "Hard to reach or staff didn't know"), ("t", AA, "problems", "Little help, or strict eligibility")]),
 ("Federal and state grants pay. Free to families who qualify.", [("q", ACL, "provides grants to states and territories")]),
 ("Partly: information and training. Staff often don't know the answer.", [("q", ACL, "information to caregivers about available services"), ("t", AA, "problems", "Hard to reach or staff didn't know")]),
 ("Partly: can pay for respite or home help. Long waits and strict rules.", [("t", AA, "worked", "Paid for respite or home help"), ("t", AA, "problems", "Long waits, low priority, no timeline"), ("t", AA, "problems", "Little help, or strict eligibility")]),
 ("Partly: Medicare counseling. Otherwise referrals, no hands-on help with accounts.", [("t", AA, "worked", "Referrals to local services, groups and Medicare counseling"), ("t", AA, "problems", "Only referrals, nothing concrete")]),
 ("No: can't act without the parent's consent.", [("k", "p12hnruv", "can't act without parent's consent")]),
 ("No: services go to one caregiver. Nothing for relatives to share.", [("q", ACL, "individual counseling, organization of support groups, and caregiver training")])]}
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")).strip()
def verify():
    ca2 = norm(open(S.parent / CA2).read()); th = json.load(open(S / "competitive-analysis-3/5b/themes-5b.json")); bad = 0; n = 0
    codes = {(c["id"]): c for k in (1, 2) for c in json.load(open(S / f"competitive-analysis-3/5b/codes-{k}.json"))}
    for comp, cells in G.items():
        assert len(cells) == len(COLS), comp
        for (text, srcs), col in zip(cells, COLS):
            if len(text.split()) > (30 if col in COLS[5:7] else 16): print("LONG", comp, col, text); bad += 1
            if ";" in text or (col not in COLS[:3] and re.search(r"\b(evidence|mentions?|claims?|reviews?|posts?|data|sources?)\b|\(", text, re.I)): print("WORDING", comp, col, text); bad += 1
            for s in srcs:
                n += 1
                if s[0] == "c" and norm(s[1]) not in ca2: print("CA2 missing", comp, s[1]); bad += 1
                if s[0] == "q" and norm(s[2]) not in norm(open(S / s[1]).read()): print("quote missing", comp, s[2][:50]); bad += 1
                if s[0] == "t" and not th.get(s[1], {}).get(s[2], {}).get(s[3]): print("theme missing", comp, s[3]); bad += 1
                if s[0] == "k" and s[2] not in codes[s[1]]["problems"] + codes[s[1]]["worked"]: print("code missing", comp, s[1]); bad += 1
                if s[0] == "x": print("NO-DATA source not allowed", comp, col); bad += 1
                if s[0] == "n" and json.load(open(S / s[1]))[s[2]] != s[3]: print("count wrong", comp); bad += 1
    print(f"cells {sum(len(v) for v in G.values())}, sources checked {n}, problems {bad}")
verify()
json.dump({"columns": COLS, "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}}, open(H / "grid-v2.json", "w"), indent=1, ensure_ascii=False)
