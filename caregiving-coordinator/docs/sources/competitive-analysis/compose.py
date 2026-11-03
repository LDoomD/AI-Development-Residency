"""Compose table rows for the competitive analysis from competitive-data.json (verified quotes) and the review data. No figures typed by hand.
Cell text uses exact quotes (a long quote is shown as an exact prefix ending with '...'). 'Reading' cells are marked as my reading of the evidence."""
import json, pathlib, re, urllib.parse
HERE = pathlib.Path(__file__).parent
D = {r["company"]: r for r in json.load(open(HERE / "competitive-data.json"))}
CATLABEL = {"family_cant_see_same_info":"relatives cannot see the same information","access_for_others":"access or logins for another person","alerts_unreliable":"missed or late alerts","readings_wrong":"wrong readings or location","not_syncing":"data not syncing","cost":"price or billing","hard_for_older_person":"hard for an older person to use","setup_compatibility":"setup or phone compatibility","privacy_trust":"privacy or trust worries","support_unresponsive":"support did not help","reminders_failing":"reminders failing","safety_gap":"a person in danger and the tool did not help","app_reliability":"crashes and bugs","other_problem":"other problems"}
META = {  # company: (direct/indirect, segment, candidate problems, website fallback)
 "Caring Village":("Direct (coordination)","Family care-coordination apps (segment 1)","1 scattered information"),
 "CaringBridge":("Direct (coordination)","Family care-coordination apps (segment 1)","1 scattered information"),
 "Lotsa Helping Hands":("Direct (coordination)","Family care-coordination apps (segment 1)","1 scattered information"),
 "ianacare":("Direct (coordination)","Family care-coordination apps (segment 1)","1 scattered information"),
 "Cozi":("Direct (coordination)","General family organizers (segment 15)","1 scattered information"),
 "FamilyWall":("Direct (coordination)","General family organizers (segment 15)","1 scattered information"),
 "TimeTree":("Direct (coordination)","General family organizers (segment 15)","1 scattered information"),
 "Medisafe":("Indirect (covers part of the need)","Medication reminder apps (segment 2)","2 medication list"),
 "MyTherapy":("Indirect (covers part of the need)","Medication reminder apps (segment 2)","2 medication list"),
 "Kin Health":("Indirect (covers part of the need)","Patient-side AI visit notes (segment 8)","3 what the doctor said"),
 "Everplans":("Direct (access to accounts)","Digital vaults and emergency access (segment 10)","4 access to accounts"),
 "Trustworthy":("Direct (access to accounts)","Digital vaults and emergency access (segment 10)","4 access to accounts"),
 "Keeper":("Direct (access to accounts)","Digital vaults and emergency access (segment 10)","4 access to accounts"),
 "1Password":("Direct (access to accounts)","Digital vaults and emergency access (segment 10)","4 access to accounts"),
 "Epic MyChart":("Direct (access to records)","Patient portals with proxy access (segment 9)","4 access to accounts and records"),
 "Lively":("Direct (monitoring and safety)","Remote monitoring and medical alert (segment 6)","8 monitoring and safety"),
 "Medical Guardian":("Direct (monitoring and safety)","Remote monitoring and medical alert (segment 6)","8 monitoring and safety"),
 "Aloe Care":("Direct (monitoring and safety)","Remote monitoring and medical alert (segment 6)","8 monitoring and safety"),
 "Life360":("Direct (monitoring and safety)","Family location sharing (not one of the 16 segments)","8 monitoring and safety"),
 "Apple Watch":("Direct (monitoring and safety)","Health devices and watches (adjacent to segment 6)","8 monitoring and safety"),
 "OMRON connect":("Direct (monitoring and safety)","Health devices (blood pressure) (adjacent to segment 6)","8 monitoring and safety"),
 "Withings":("Direct (monitoring and safety)","Health devices (blood pressure) (adjacent to segment 6)","8 monitoring and safety"),
}
ORDER = ["Caring Village","CaringBridge","Lotsa Helping Hands","ianacare","Cozi","FamilyWall","TimeTree","Medisafe","MyTherapy","Kin Health","Everplans","Trustworthy","Keeper","1Password","Epic MyChart","Lively","Medical Guardian","Aloe Care","Life360","Apple Watch","OMRON connect","Withings"]
def cut(s, n): s = re.sub(r"\s+", " ", s).strip(); return s if len(s) <= n else s[:n].rstrip() + "..."
def quotes(rec, f, k, n=170): return [cut(q["quote"], n) for q in rec["fields"].get(f, [])[:k]]
def fmt(lst, none="Not found in the saved pages"): return "\n".join("• " + x for x in lst) if lst else none
def site(rec):
    us = [q["url"] for q in sum(rec["fields"].values(), []) if q["url"]]
    if not us: return "Not verified (no live page confirmed)"
    p = urllib.parse.urlparse(us[0]); return f"{p.scheme}://{p.netloc}/"
rows = []
for co in ORDER:
    r = D[co]; m = META[co]; rv = r["reviews"]
    feats = fmt(quotes(r, "main_features", 3))
    diff = fmt(quotes(r, "differentiation", 1))
    uvp = fmt(quotes(r, "uvp_claim", 1))
    who = quotes(r, "audience", 2) + quotes(r, "price", 2)
    who = fmt(who)
    shared = quotes(r, "shared_access", 1)
    if rv["reviews_read"]:
        well = fmt([f"\"{cut(q['quote'],150)}\" (review {q['id']})" for q in rv["worked_quotes"][:1]], "No 'worked' quote in the sample")
        notwell = fmt([f"\"{cut(q['quote'],150)}\" (review {q['id']})" for q in rv["problem_quotes"][:1]], "No problem quote in the sample")
        cats = ", ".join(f"{CATLABEL[c]} ({n})" for c, n in rv["top_problem_categories"][:2]) or "none"
        say = f"{rv['reviews_read']} app-store reviews read (those that mention a caregiving or family word): {rv['problem']} describe a problem, {rv['worked']} describe something that worked. Most common problems: {cats}."
    else:
        well = notwell = "No app reviews collected"; say = "No app reviews collected for this company"
    empty = [lbl for f, lbl in [("differentiation","how it differs"),("shared_access","sharing with another person"),("price","price")] if not r["fields"].get(f)]
    gap = "Reading (mine, from the evidence in this row): "
    top = [CATLABEL[c] for c, n in rv["top_problem_categories"][:2]] if rv["reviews_read"] else []
    gap += ("reviewers raise " + " and ".join(top) + "; " if top else "") + ("its saved pages say nothing on: " + ", ".join(empty) + "." if empty else "its saved pages state all three of: how it differs, sharing, price.")
    urls = []
    for q in sum(r["fields"].values(), []):
        u = q["url"] or "page link not verified"; t = f"{u} [{q['file'].split('/',1)[1]}]"
        if t not in urls: urls.append(t)
    src = "Company claims (cols 4, 5, 10, 12): " + "; ".join(urls[:4]) + (f"; +{len(urls)-4} more in docs/sources/competitive-analysis/competitive-data.json" if len(urls) > 4 else "") + ". Reviews: docs/sources/app-reviews/analysis/verified-tags.json (ids in cells)." + (f" Note: {r['not_found_note'][:140]}" if co in ("1Password",) else "")
    if shared: who += "\n• Sharing (company's words): " + shared[0]
    rows.append([co, m[0], m[1], site(r), feats, diff, well, notwell, say, gap, uvp, m[2], who, src])
json.dump(rows, open(HERE / "table-rows.json", "w"), ensure_ascii=False)
print(len(rows), "rows;", len(json.dumps(rows, ensure_ascii=False)), "chars; longest cell", max(len(c) for r in rows for c in r))
for r in rows[:2]: print(json.dumps(r, ensure_ascii=False)[:1800]); print()
