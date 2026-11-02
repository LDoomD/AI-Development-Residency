"""Group the problems readers extracted (type = problem) into use-case themes by keyword rules on their labels; count distinct threads; pick example quotes (prefer ones that say when it happens)."""
import json, re, collections, pathlib
HERE = pathlib.Path(__file__).parent
RULES = {
 "parent": [
  ("Being far away and not knowing what is happening", r"distance|far away|remote|out of state|from far|missed time by not knowing|did not know when|never saw diagnosis"),
  ("Relatives do not help, or block each other", r"brother|sister|sibling|only child|no family|guardian|co-poa|attorney|poa bars|poa blocked|sole caregiver|needs sister|unsupport|no family support"),
  ("Money, legal papers and facility bills", r"medicaid|poa|forms|billing|charge|quotes|savings|costs|ira|read access|sticker|money|afford|house|contracts|payments|price|institution|retire|finances|wallet|scam"),
  ("Choosing and arranging a place for them", r"facility|placing|placement|nursing home|assisted living|move|rehab|mom refuses move|stalling"),
  ("Medicines, eating and personal care", r"pills|meds|eat|hygiene|soaked|clean|laundry|overeat|snack|intimate|change her|bed"),
  ("Staying safe at home", r"stove|fell|falls|wander|lost|fire|police|safety|walks alone"),
  ("Getting answers from doctors and hospitals", r"hospital|diagnos|information|answers|doctor|paperwork|callback|decline signs|er,|bounced|volunteer|calls to get"),
  ("Dementia behavior and hard conversations", r"sundown|calls|constant|anxiety|angry|refus|stories|fibbing|questions|aggression|behavior|hallucinat|violent|begging|meltdown|search|calm|repeated|distract|home"),
  ("Exhaustion, guilt and no life of their own", r"exhaust|sleep|alone|24/7|no breaks|trapped|no life|all-purpose|resent|guilt|overwhelm|mental|depress|ambivalent|broke|funk|consumed|control|shell|retirement|vacation|gone anywhere|dread|visit|focus|school|responsib|support group|spiral")],
 "spouse": [
  ("Dementia behavior and hard conversations", r"sundown|aggress|agitat|anxiety|restless|refuses|combative|questions|whimper|go home|calming|meanness|says no|criticism|blame|resent|yelling|anger|provok|barely speaks|cannot communicate|cannot recall|will not talk|resist|behavior|reaction"),
  ("Safety when they are alone or out", r"alone|leave|fire|lost|restroom|driving|safe|neighbors|emergency|supervision|falls|doors"),
  ("Money, scams and bills", r"money|scam|finance|check|overspend|bills|afford|insurance|home|cost"),
  ("Diagnosis and doctor delays", r"diagnos|neurolog|doctor|tests|delays|hospice promised|no clear"),
  ("Personal care and medicines", r"shower|incontinen|catheter|dress|clean|medic|sedat|drugs|blood pressure|monitor|pills|overeat|carb|sweets|eating|food|alcohol|toilet|bath"),
  ("Placing them and care costs", r"memory care|placing|placement|staff|adjust|care home|nursing home|could no longer"),
  ("Aides, hospice and trusting others", r"aide|hospice|agenc|visit nursing|trust|reliable|hard to leave|with others|daycare|day care"),
  ("Exhaustion, loneliness and own health", r"exhaust|tired|alone|unsupported|vent|own health|own illness|stress|overwhelm|grief|guilt|plate|crying|draining|solely|non-stop|no one|friends|balancing|patient|changing relationship|dread|cannot make myself|drained|no break")]}
def classify(aud, label):
    for name, rx in RULES[aud]:
        if re.search(rx, label, re.I): return name
    return "Other"
WHEN = re.compile(r"\b(after|when|at night|every|morning|evening|during|before|weekend|daily|\d+ ?(am|pm)|once|whenever|each|since|while|always|now)\b", re.I)
out = {}
for aud, n in (("parent", 55), ("spouse", 54)):
    th = collections.defaultdict(set); ex = collections.defaultdict(list); items = 0
    for k in ("1", "2"):
        for t in json.load(open(HERE / f"motiv-{aud}-{k}-items.json")):
            for it in t["items"]:
                if it["type"] != "problem": continue
                name = classify(aud, it["label"]); th[name].add(t["id"]); ex[name].append({"id": t["id"], "quote": it["quote"], "label": it["label"]}); items += 1
    res = {}
    for name, ids in th.items():
        seen = set(); pick = []
        cand = [e for e in ex[name] if 50 <= len(e["quote"]) <= 220]
        cand.sort(key=lambda e: (not WHEN.search(e["quote"]), -len(e["quote"])))
        for e in cand:
            if e["id"] in seen: continue
            seen.add(e["id"]); pick.append(e)
            if len(pick) == 2: break
        res[name] = {"threads": len(ids), "items": len(ex[name]), "examples": pick}
    out[aud] = {"n": n, "problem_items": items, "themes": res}
json.dump(out, open(HERE / "usecase-themes.json", "w"), indent=1, ensure_ascii=False)
for aud, r in out.items():
    print(aud, r["problem_items"], "problem items;", {k: v["threads"] for k, v in sorted(r["themes"].items(), key=lambda kv: -kv[1]["threads"])})
