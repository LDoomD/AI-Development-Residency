"""Check use case rows: group labels exist, bullets are the top groups in size order (ignoring 'other'), word limits, row order by item count; prints row counts."""
import json, pathlib
H = pathlib.Path(__file__).parent
M = json.load(open(H / "moments-by-usecase.json"))
bad = 0
for a in ("A1", "A2"):
    G = json.load(open(H / f"groups-{a}.json")); rows = json.load(open(H / f"uc-{a}.json"))
    tots = []
    for r in rows:
        key = f"{a}|{r['uc']}"; m = M[key]; tot = m["forum"] + m["reddit"]; tots.append(tot)
        if len(r["problem"].split()) > 16: print(key, "problem too long"); bad += 1
        for t in ("moments", "wants"):
            sizes = {g["label"]: len(g["ids"]) for g in G[key][t] if g["label"] != "other"}
            top = sorted(sizes, key=lambda l: -sizes[l])[:len(r[t])]
            used = [x[1] for x in r[t]]
            for u in used:
                if u not in sizes: print(key, t, "label missing", u); bad += 1
            if sorted(sizes[u] for u in used if u in sizes) != sorted(sizes[l] for l in top): print(key, t, "not top groups", used); bad += 1
            if [sizes.get(u) for u in used] != sorted([sizes.get(u, 0) for u in used], reverse=True): print(key, t, "order"); bad += 1
            for x in r[t]:
                if len(x[0].split()) > 14: print(key, "long bullet", x[0]); bad += 1
        for s in r["scenarios"]:
            if len(s.split()) > 12: print(key, "long scenario", s); bad += 1
        print(a, r["uc"], tot, f'(forum {m["forum"]}, reddit {m["reddit"]})')
    if tots != sorted(tots, reverse=True): print(a, "row order", tots); bad += 1
print("problems", bad)
