"""Checks one reader's output (python3 verify_codes.py N) or all of them (no argument):
every pack item coded exactly once, labels from the allowed lists, every quote an exact substring of its item."""
import json, sys, re, pathlib
H = pathlib.Path(__file__).parent
HELP = {"in-home respite", "short-stay respite (facility)", "adult day program", "hospice respite", "therapist or counselor for the caregiver", "support group", "paid aide or companion", "family or friend stepping in"}
BAR = {"cost", "waitlist or no openings", "hard application or eligibility rules", "inflexible program (hours, minimum stay, days)", "no trained or reliable providers", "doesn't trust strangers with the parent", "guilt or shame about handing off care", "worry about quality or safety", "the parent refuses", "transport or logistics", "didn't know it existed"}
STATUS = {"used", "tried and stopped", "looking or considering", "wanted but couldn't get", "recommends to others", "mentioned only"}
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
def check(n):
    pack = {i["id"]: i for i in json.load(open(H / "packs" / f"pack-{n}.json"))}
    codes = json.load(open(H / "codes" / f"codes-{n}.json")); bad = []
    seen = [c["id"] for c in codes]
    for k in pack:
        if seen.count(k) != 1: bad.append(f"{k}: coded {seen.count(k)} times")
    for c in codes:
        if c["id"] not in pack: bad.append(f"{c['id']}: not in pack"); continue
        if c.get("relevant"):
            if not c.get("quote") or norm(c["quote"]) not in norm(pack[c["id"]]["text"]): bad.append(f"{c['id']}: quote not found exactly")
            if c.get("status") not in STATUS: bad.append(f"{c['id']}: bad status {c.get('status')}")
            for h in c.get("help", []):
                if h not in HELP and not h.startswith(("named program: ", "app or online tool: ")): bad.append(f"{c['id']}: bad help label {h}")
            for b in c.get("barriers", []):
                if b not in BAR and not b.startswith("other: "): bad.append(f"{c['id']}: bad barrier {b}")
    return bad, len(pack), sum(1 for c in codes if c.get("relevant"))
ns = [int(sys.argv[1])] if len(sys.argv) > 1 else range(1, 12)
allbad = 0
for n in ns:
    bad, items, rel = check(n); allbad += len(bad)
    print(f"pack {n}: items {items}, relevant {rel}, problems {len(bad)}"); [print("  ", b) for b in bad[:30]]
print("OK" if allbad == 0 else f"{allbad} problems")
