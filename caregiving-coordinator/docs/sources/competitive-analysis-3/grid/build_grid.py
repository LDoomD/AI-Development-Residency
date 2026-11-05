"""Competitive Analysis 3 grid: 7 competitors x template columns + 5 criteria. Every cell has a source:
 q = exact quote in a saved file (path from docs/sources/), c = exact text in docs/competitive-analysis-2.md,
 t = a theme in competitive-analysis-3/5b/themes-5b.json (competitor, kind, theme), n = a count file, x = no evidence found (stated as such).
verify() checks every source. Writes grid.json."""
import json, re, pathlib
H = pathlib.Path(__file__).parent; S = H.parents[1]
CA2 = "competitive-analysis-2.md"
COLS = ["Type", "Market segment", "Website", "Main features", "How they stand out", "What they do well", "What they don't do well", "Who pays, and the cost",
        "1. Understand, handle behavior, know what to do", "2. Real relief for the caregiver", "3. Money, papers, accounts", "4. Works when the parent refuses help", "5. Relatives share the work"]
CV = "competitors/caring-village/www_caringvillage_com_about.txt"; B5 = "competitors-4/basics-5a.json"
G = {
"Caring Village": [
 ("Direct (business)", [("c", "Direct (coordination)")]),
 ("1 Family care-coordination apps", [("c", "Family care-coordination apps")]),
 ("caringvillage.com", [("c", "https://caringvillage.com/")]),
 ("One family app: shared calendar, to-dos, medication lists, documents, AI helper.", [("c", "calendar, to-dos, medication lists, care plan, journal, group messages, document storage")]),
 ("Says it's one 'command center' built by former caregivers.", [("c", "Claims to be one 'command center'")]),
 ("Keeps the whole family on the same page about the parent's care.", [("c", "Keeps the whole family updated and on the same page (10 of 29)")]),
 ("Can't make relatives help, and getting everyone to join is hard.", [("c", "can't make relatives help"), ("c", "it's hard to get everyone into the group (2)")]),
 ("The caregiver pays: free for 2 people, or $14.99 to $24.99 a month.", [("c", "Circle: $14.99 a month"), ("c", "Village: $24.99 a month")]),
 ("Partly: a 24/7 AI helper gives guidance, but no caregiver says it helped.", [("q", CV, "get 24/7 guidance from Julia, our AI caregiving assistant"), ("x", "no review or post describes the AI helper helping")]),
 ("Partly: reviewers say less stress, but it gives no hands-on help.", [("c", "say it means less stress (5)")]),
 ("Partly: stores documents, but no help with banks, insurers or accounts.", [("c", "group messages, document storage"), ("c", "It doesn't help with getting into the parent's bank, insurer or portal accounts")]),
 ("No: nothing in its features or 29 reviews addresses a refusing parent.", [("x", "not found in the 29 reviews or company pages")]),
 ("Partly: relatives join free with their own login, but it can't make them act.", [("c", "each joins free with their own account"), ("c", "can't make relatives help")])],
"Everplans": [
 ("Direct (business)", [("c", "Direct (access to accounts)")]),
 ("10 Digital vaults and emergency access", [("c", "Digital vaults and emergency access")]),
 ("everplans.com", [("c", "https://www.everplans.com/")]),
 ("Online vault for documents, accounts and wishes, shared with chosen 'deputies'.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("Says it organizes all of a person's life details and next steps.", [("c", "Claims to organize all of a person's life details")]),
 ("Families find a parent's notes and papers in one place after a death.", [("q", "app-reviews/reviews4.csv", "After my dad passed away, we discovered a wealth of notes he had left for us"), ("q", "app-reviews/reviews4.csv", "a secure, cloud-based repository")]),
 ("Only works if the parent set it up first; the iPad app is phone-sized.", [("c", "Everplans needs the parent to set everything up ahead of time, and no caregiver use was found"), ("q", "app-reviews/reviews4.csv", "the iPad app forces an iPhone size")]),
 ("The person pays: free for 3 items, or $99.99 a year.", [("c", "Premium at $99.99 a year")]),
 ("No: it's a document vault with no care guidance.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("No: it stores papers but takes no care work off the caregiver.", [("c", "A secure online vault for documents, IDs, accounts and wishes")]),
 ("Yes, if the parent set it up: papers, accounts and wishes in one vault.", [("c", "A secure online vault for documents, IDs, accounts and wishes"), ("c", "Everplans needs the parent to set everything up ahead of time")]),
 ("No: it only works if the parent filled it in ahead of time.", [("c", "Everplans needs the parent to set everything up ahead of time")]),
 ("Partly: deputies see chosen sections, but it doesn't divide the work.", [("c", "deputies' who get access to chosen sections")])],
"Cariloop": [
 ("Direct (business, employer-paid)", [("q", B5, "Typically our minimum size group is 100 employees")]),
 ("7 Employer and health-plan caregiver benefits", [("q", B5, "The caregiving benefit for every employee")]),
 ("cariloop.com", [("q", B5, "SOURCE: https://www.cariloop.com/")]),
 ("A care coach, a provider marketplace, family Care Team, and document storage.", [("q", B5, "Give your employees access to a dedicated Coach"), ("q", B5, "Employees can search, compare, book, and pay for care all in one place.")]),
 ("Full-time coaches, and no referral fees from care providers.", [("q", B5, "All of our Care Coaches are full-time, W2 employees of Cariloop."), ("q", B5, "We do not accept referral, lead generation, or subscription fees of any kind from any healthcare provider.")]),
 ("Members call its care coaches very helpful in a crisis (few public reviews).", [("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Staff wonderful incredibly helpful in your time of need"), ("q", "competitors-4/review-sites/bbb_2026-11-04.txt", "complaints total: 0. customer reviews total: 0.")]),
 ("Only through an employer; leaving the job means paying yourself.", [("q", B5, "Typically our minimum size group is 100 employees"), ("q", B5, "a 30-day countdown is triggered within our platform that allows the member to shift to an individual membership that they can cover the cost of on their own")]),
 ("The employer pays; extending coaching yourself costs $249 a month (MSU example).", [("q", B5, "employees have the option to extend the coaching for $249/month.")]),
 ("Yes (company claim): coaches explain diagnoses like Alzheimer's and next options.", [("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Understanding diagnoses like ADHD, Alzheimer’s, Anxiety, Autism, Cancer, Down Syndrome, Parkinson’s, etc.")]),
 ("Partly: a coach and booking help, but only if your employer buys it.", [("q", B5, "Employees can search, compare, book, and pay for care all in one place.")]),
 ("Yes (company claim): help with paying for care, benefits, POA, and document storage.", [("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Understanding how to pay for a loved one’s care"), ("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Filling out important legal caregiving documents (wills, POAs, DNRs, etc.)")]),
 ("Partly: coaches handle family dynamics; nothing specific for a refusing parent.", [("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Managing family dynamics related to your loved one’s care")]),
 ("Partly: relatives can join the Care Team and stay updated; no task sharing.", [("q", "competitors-4/manual-saves/google_play_cariloop.txt", "Add whoever needs to be involved in the care of your loved ones to your Care Team")])],
"A Place for Mom": [
 ("Direct (business)", [("q", B5, "A Place for Mom is a referral service.")]),
 ("4 Senior care referral and placement", [("q", B5, "A Place for Mom is a referral service.")]),
 ("aplaceformom.com", [("q", B5, "Find Assisted Living, Memory Care and Senior Living Near Me | A Place for Mom")]),
 ("Free advisor, care and cost assessment, local list with prices, and tours.", [("q", B5, "Receive a free care and financial assessment"), ("q", B5, "Get clear pricing and details so you can make an informed decision.")]),
 ("Claims the largest senior care network in the country.", [("q", B5, "Our senior care network is the largest in the country")]),
 ("Quickly lines up nearby places and tours, guiding families who don't know where to start.", [("q", "competitors-4/review-sites/bbb_2026-11-04.txt", "You helped me to figure out the process of finding a place for mom when I had no idea of where to even start"), ("q", "competitors-4/review-sites/bbb_2026-11-04.txt", "the setting up of appointments")]),
 ("Shares families' details with many places, causing nonstop calls; pushy, commission-driven advisors.", [("q", "competitors-4/review-sites/bbb_2026-11-04.txt", "A Place for Mom has distributed my phone number and email to every assisted living facility in my area without my consent."), ("t", "A Place for Mom", "problems", "Nonstop calls and spam that won't stop"), ("t", "A Place for Mom", "problems", "Paid by commission, not truly free")]),
 ("Senior living communities pay referral fees; free to families.", [("q", B5, "A Place for Mom is paid by our senior living network communities when a family we refer chooses to move into a community."), ("q", B5, "Our services—including personalized guidance and support—are always free to families.")]),
 ("Partly: an advisor guides the search, but families say they don't know the places.", [("q", B5, "Receive a free care and financial assessment"), ("t", "A Place for Mom", "problems", "Doesn't know places or care about quality")]),
 ("Partly: saves search time, but families then face nonstop calls.", [("t", "A Place for Mom", "worked", "Shows options and some prices"), ("t", "A Place for Mom", "problems", "Nonstop calls and spam that won't stop")]),
 ("Partly: has a cost calculator, but can't help Medicaid-only families.", [("q", B5, "Try our senior living cost calculator"), ("t", "A Place for Mom", "problems", "No help for Medicaid-only families")]),
 ("No: one family says an advisor told them to trick the parent into moving.", [("q", "competitors-4/review-sites/bbb_2026-11-04.txt", "Told me the best way to get our mother in a nursing home is to just lie to her")]),
 ("No: it works with one contact person; no tools for relatives to share work.", [("x", "no feature or post about relatives sharing work")])],
"Geriatric care managers": [
 ("Direct (private professionals)", [("q", B5, "Count on paying out of pocket")]),
 ("None of the 14 segments (private care management)", [("q", B5, "These professionals act as advocates and guides for family members")]),
 ("aginglifecare.org (to find one)", [("q", B5, "for those who are members of the Aging Life Care Association")]),
 ("Home assessments, care plans, hiring aides, appointments, and acting for distant families.", [("q", B5, "Evaluating, arranging for and monitoring hired caregivers, such as home health aides."), ("q", B5, "Acting as a liaison to families who may be hundreds of miles away.")]),
 ("In-person, trained professionals with local connections.", [("q", B5, "An in-person assessment gives them the opportunity to observe the home environment"), ("q", B5, "Our specialized experience and local connections can speed families through the roadblocks they often encounter.")]),
 ("Take the load off in a crisis and go to appointments for the family.", [("t", "Geriatric care managers", "worked", "Takes load off in a crisis"), ("t", "Geriatric care managers", "worked", "Goes to appointments and reports back")]),
 ("Expensive hourly billing, and families aren't sure what they do.", [("t", "Geriatric care managers", "problems", "Unsure it's worth the cost"), ("t", "Geriatric care managers", "problems", "Unclear what they do or how to choose")]),
 ("The family pays $150 to $300 an hour; Medicare and Medicaid usually don't.", [("q", B5, "Professionals charge by the hour, ranging from $150 to $300, depending on the geographic region."), ("q", B5, "Neither Medicare nor Medicaid typically pays for care management services.")]),
 ("Yes: they explain hard topics to the parent and family, and give practical advice.", [("q", "competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt", "Explaining complex or difficult topics to care recipients and their families."), ("t", "Geriatric care managers", "worked", "Takes load off in a crisis")]),
 ("Yes, at a price: they take over doctor visits and touring places.", [("t", "Geriatric care managers", "worked", "Goes to appointments and reports back"), ("t", "Geriatric care managers", "worked", "Tours and evaluates places, finds resources")]),
 ("Partly: they advise on money options, but bill for every call and email.", [("t", "Geriatric care managers", "worked", "Tours and evaluates places, finds resources"), ("t", "Geriatric care managers", "problems", "Heavy billing")]),
 ("Partly: they talk with the parent directly, but some parents still refuse.", [("q", "competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt", "Explaining complex or difficult topics to care recipients and their families."), ("t", "Geriatric care managers", "problems", "Family conflict or refusal around them")]),
 ("Partly: they can stand up to a difficult relative, but conflict often follows.", [("t", "Geriatric care managers", "worked", "Stands up to difficult relatives"), ("t", "Geriatric care managers", "problems", "Family conflict or refusal around them")])],
"Group texts and notebooks": [
 ("Indirect (workaround)", [("c", "Indirect (what families use instead)")]),
 ("What families use instead (not a company)", [("c", "Workaround, not a company")]),
 ("n/a", [("c", "n/a")]),
 ("Family group chats, notebooks, binders and whiteboards.", [("c", "Family group chats, group texts and WhatsApp groups"), ("c", "Notebooks, binders, whiteboards, wall calendars")]),
 ("Free, already there, nothing to install.", [("c", "Everyone already has it, it's free, and there's nothing to install.")]),
 ("Tell everyone at once; a whiteboard calms repeated questions.", [("c", "One place to tell the whole family what's happening (6 of 53)"), ("c", "A whiteboard with the date and schedule calms repeated questions")]),
 ("Requests get silence, and notes get lost or stay with one person.", [("c", "Requests and updates get silence or just a 'like' (10)"), ("c", "Notes and calendars get ignored, lost or erased (12)")]),
 ("Free or nearly free.", [("c", "Nearly free.")]),
 ("No: they pass on notes but no advice; a written guide helps others step in.", [("c", "a written guide lets someone else step in (4)")]),
 ("No: constant messages wear the caregiver down.", [("c", "constant messages wear the caregiver down (7)")]),
 ("Partly: paper holds the papers, but it piles up and can't be searched.", [("c", "records pile up and can't be searched when a doctor asks (7)")]),
 ("Yes: they work without the parent needing a phone or app.", [("c", "it works without phones (4)")]),
 ("Partly: everyone hears at once, but requests get silence or just a 'like'.", [("c", "Requests and updates get silence or just a 'like' (10)")])],
"Area Agencies on Aging": [
 ("Indirect (government program)", [("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "provides grants to states and territories")]),
 ("None of the 14 segments (free public service)", [("q", "competitors-4/eldercare-locator/eldercare_acl_gov_home.txt", "a public service of the Administration for Community Living")]),
 ("eldercare.acl.gov (finds your local agency)", [("q", "competitors-4/eldercare-locator/eldercare_acl_gov_home.txt", "Welcome to the Eldercare Locator")]),
 ("Caregiver information, help getting services, counseling, support groups, training, respite.", [("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "individual counseling, organization of support groups, and caregiver training"), ("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "respite care; and")]),
 ("Local, government-funded, and free to eligible families.", [("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "provides grants to states and territories")]),
 ("Point families to local services, support groups and Medicare counseling.", [("t", "Eldercare Locator and Area Agencies on Aging", "worked", "Referrals to local services, groups and Medicare counseling")]),
 ("Long waitlists, and often referrals without concrete help.", [("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Long waits, low priority, no timeline"), ("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Only referrals, nothing concrete")]),
 ("Federal and state grants pay; free to eligible families.", [("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "provides grants to states and territories")]),
 ("Partly: they offer information and training, but staff sometimes don't know answers.", [("q", "competitors-4/manual-saves/acl_gov_nfcsp.txt", "information to caregivers about available services"), ("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Hard to reach or staff didn't know")]),
 ("Partly: can fund respite or home help, after long waits and strict eligibility.", [("t", "Eldercare Locator and Area Agencies on Aging", "worked", "Paid for respite or home help"), ("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Long waits, low priority, no timeline"), ("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Little help, or strict eligibility")]),
 ("Partly: Medicare counseling and legal referrals, but no hands-on help with accounts.", [("t", "Eldercare Locator and Area Agencies on Aging", "worked", "Referrals to local services, groups and Medicare counseling"), ("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Only referrals, nothing concrete")]),
 ("No: they can't act without the parent's consent.", [("t", "Eldercare Locator and Area Agencies on Aging", "problems", "Only referrals, nothing concrete")]),
 ("No: nothing in the program or posts helps relatives share the work.", [("x", "not in the 47 caregiver posts or the program page")])]}
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")).strip()
def verify():
    ca2 = norm(open(S.parent / CA2).read()); th = json.load(open(S / "competitive-analysis-3/5b/themes-5b.json")); bad = 0; n = 0
    codes = {(c["id"]): c for k in (1, 2) for c in json.load(open(S / f"competitive-analysis-3/5b/codes-{k}.json"))}
    for comp, cells in G.items():
        assert len(cells) == len(COLS), comp
        for (text, srcs), col in zip(cells, COLS):
            if len(text.split()) > 16: print("LONG", comp, col, text); bad += 1
            for s in srcs:
                n += 1
                if s[0] == "c" and norm(s[1]) not in ca2: print("CA2 missing", comp, s[1]); bad += 1
                if s[0] == "q" and norm(s[2]) not in norm(open(S / s[1]).read()): print("quote missing", comp, s[2][:50]); bad += 1
                if s[0] == "t" and not th.get(s[1], {}).get(s[2], {}).get(s[3]): print("theme missing", comp, s[3]); bad += 1
                if s[0] == "n" and json.load(open(S / s[1]))[s[2]] != s[3]: print("count wrong", comp); bad += 1
    print(f"cells {sum(len(v) for v in G.values())}, sources checked {n}, problems {bad}")
verify()
json.dump({"columns": COLS, "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}}, open(H / "grid.json", "w"), indent=1, ensure_ascii=False)
