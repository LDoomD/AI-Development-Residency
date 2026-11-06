"""Group each competitor's worked/problems labels into themes by keyword rules, count distinct posts/threads per theme.
Unmatched labels are listed so nothing is dropped silently. Writes themes-5b.json."""
import json, re, pathlib
H = pathlib.Path(__file__).parent; C = json.load(open(H / "counts-5b.json"))
R = {
 "Eldercare Locator and Area Agencies on Aging": {
  "worked": {"Helpful, kind or quick staff": r"helpful|kindly|called back|responsive|listened",
             "Paid for respite or home help": r"respite|housework|home aide|pays someone|grant",
             "Referrals to local services, groups and Medicare counseling": r"refer|support group|resources|SHIP|programs|Medicaid nursing|location-specific"},
  "problems": {"Long waits, low priority, no timeline": r"wait|priority|timeline|timeframe|state funding|60 days|reassess|bottom",
               "Hard to reach or staff didn't know": r"reply|answer|returned|hold times|didn't know|unresponsive|bureaucratic|conflicting",
               "Paperwork and caregiver pay problems": r"paperwork|not on file|fax|caregiver pay|no pay|paid caregiver|getting paid|pay family|assessments|back and forth",
               "Little help, or strict eligibility": r"eligib|low-income|40 hours|\$1500|small amount|barely|won't pay|family must pay|denied|aides all booked|same caregiver|depends on county",
               "Only referrals, nothing concrete": r"referrals only|nothing happens|tired of being told|no one explains|only refers|homeless shelter|no help finding|no one acted|could not stop|still needed|consent|no better|spam|shared"}},
 "Geriatric care managers": {
  "worked": {"Takes load off in a crisis": r"load|overwhelmed|godsend|crises|sympathetic|practical advice",
             "Goes to appointments and reports back": r"doctor|appointments|hospital|reports back",
             "Tours and evaluates places, finds resources": r"tours|facilities|resources|financial|memory care|home visits",
             "Stands up to difficult relatives": r"relative"},
  "problems": {"Unsure it's worth the cost": r"cost|wasting money|overspending|worth",
               "Unclear what they do or how to choose": r"unclear|choose|fit and scope|right first step|lawyer",
               "Heavy billing": r"bill|retainer",
               "Family conflict or refusal around them": r"sibling|stepparent|refuses|dissatisfied|many calls",
               "Didn't deliver": r"no options|never made|pushed|found no housing|more work|power of attorney"}},
 "A Place for Mom": {
  "worked": {"Shows options and some prices": r"prices|search"},
  "problems": {"Shares or sells family's details": r"shared|sells|name, phone",
               "Nonstop calls and spam that won't stop": r"call|spam|contact|harass|block|emails",
               "Paid by commission, not truly free": r"commission|not truly free|pay to be listed|fee",
               "Doesn't know places or care about quality": r"firsthand|quality|safety|marketing|horror|no good|investigation|suspiciously|less helpful|intake|unhelpful|no response|rushes",
               "No help for Medicaid-only families": r"medicaid|private pay"}},
 "Alzheimer's Association helpline": {
  "worked": {"Support groups and trained facilitators": r"group|facilitator",
             "Information, facility lists, social worker": r"preview|list|social worker|24/7"},
  "problems": {"Generic advice, didn't listen": r"generic|listen|answers",
               "Few groups, inconvenient times": r"few|inconvenient|during the day"}},
}
out = {}
for comp, rules in R.items():
    out[comp] = {}
    for kind in ("worked", "problems"):
        groups = {g: set() for g in rules[kind]}; un = []
        for pid, label in C[comp][kind]:
            g = next((g for g, rx in rules[kind].items() if re.search(rx, label, re.I)), None)
            if g: groups[g].add(pid)
            else: un.append(label)
        out[comp][kind] = {g: sorted(v) for g, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))}
        print(comp, kind, {g: len(v) for g, v in out[comp][kind].items()}, "UNMATCHED:", un)
json.dump(out, open(H / "themes-5b.json", "w"), indent=1)
