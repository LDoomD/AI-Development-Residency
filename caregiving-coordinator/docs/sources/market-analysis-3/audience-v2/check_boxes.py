"""Each box statement's [forum, reddit] counts must match goals/audience-tables.json (forum 'not on the board' = 0), and statements must be in combined-count order."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
T = json.load(open(H.parent / "goals/audience-tables.json")); B = json.load(open(H / "boxes.json"))
KEY = {"A1": "Audience 1: parent", "A2": "Audience 2: spouse or partner"}
def num(s): m = re.match(r"(\d+)", s); return int(m.group(1)) if m else 0
bad = 0
for a, boxes in ((k, v) for k, v in B.items() if k in KEY):
    for cat, rows in boxes.items():
        src = [(num(r[1]), num(r[2])) for r in T[KEY[a]]["tables"][cat]]
        got = [(r[1], r[2]) for r in rows]
        for g in got:
            if g not in src: print(a, cat, "count not in source", g); bad += 1
        tot = [f + r for f, r in got]
        if tot != sorted(tot, reverse=True): print(a, cat, "order", tot); bad += 1
print("problems", bad)
