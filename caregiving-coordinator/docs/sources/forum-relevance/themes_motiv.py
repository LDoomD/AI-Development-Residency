"""Group the extracted motivations, situational goals and life goals into themes by keyword rules on the readers' short labels, and count distinct threads per theme.
Counts are approximate and are minimums: readers listed only clear statements (up to 6 per thread)."""
import json, re, collections, pathlib
HERE = pathlib.Path(__file__).parent
RULES = {
 "motivation": [("Keep them safe and comfortable, spare them suffering", r"safe|comfort|suffer|harm|anxiety|clean|dignity|best (possible )?day|ease|eases|distress|hospice help"),
                ("Love, loyalty and promises", r"love|loyal|promise|vow|memories|loved|abandon|remember|compassion|patience|understand"),
                ("Keep them at home and in control of their own life", r"at home|home\b|stuck|choice|decide|friends|pleasures|die at home|memory care|nursing home|move"),
                ("Do the right thing, avoid blame or guilt", r"right|accus|wrongdoing|best for|better|support mother|stop this|other families|spite")],
 "situational_goal": [("Find, choose or pay for a place (memory care, assisted living)", r"memory care|assisted living|place|moved|medicaid|facility|tour|waitlist|house near|move closer|pay for|sell|fund"),
                ("Get help, relief or services", r"help|support group|relief|backup|stay with|hospice|services|insurance|break|learn from|find a place to learn|low-cost|justice|legal"),
                ("Keep them safe and watch over them", r"track|gps|alert|supervision|safety|aides|monitor|blood pressure|know when|walk|driving|know aides|staff keep"),
                ("Manage money and legal affairs", r"financ|poa|account|scam|money|dental|affairs|roles"),
                ("Medicines", r"pills|meds|medic|pillbox"),
                ("Understand what is happening and what to do", r"understand|learn|know what|diagnos|evaluation|cause")],
 "life_goal": [("Time and breaks for themselves", r"break|time to myself|days away|travel|walks|time"),
               ("Their own health and sanity", r"health|sane|sanity|cope|therapy|function|courage|anxiety"),
               ("Keep their own life, job and money", r"job|finances|life|afterward|child|plan|cared for|new life|continue")],
}
def classify(kind, label):
    for name, rx in RULES[kind]:
        if re.search(rx, label, re.I): return name
    return "Other"
out = {}
for aud in ("parent", "spouse"):
    threads = []; 
    for k in ("1", "2"): threads += json.load(open(HERE / f"motiv-{aud}-{k}-items.json"))
    res = {"threads": len(threads)}
    for kind in ("motivation", "situational_goal", "life_goal"):
        th = collections.defaultdict(set); ex = collections.defaultdict(list); unassigned = []
        for t in threads:
            for it in t["items"]:
                if it["type"] != kind: continue
                th_name = classify(kind, it["label"]); th[th_name].add(t["id"])
                ex[th_name].append({"id": t["id"], "quote": it["quote"], "label": it["label"]})
        res[kind] = {n: {"threads": len(s), "examples": ex[n]} for n, s in th.items()}
    out[aud] = res
json.dump(out, open(HERE / "motiv-themes.json", "w"), indent=1, ensure_ascii=False)
for aud, r in out.items():
    print(aud, r["threads"], "threads")
    for kind in ("motivation", "situational_goal", "life_goal"):
        print(" ", kind, {n: v["threads"] for n, v in r[kind].items()})
