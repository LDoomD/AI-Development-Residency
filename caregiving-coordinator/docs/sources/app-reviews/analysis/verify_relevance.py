"""Check the strict caregiving-relevance tags. 'caregiving' counts only if (1) the id is in the input, (2) there is an evidence quote, and (3) the quote is an exact
substring of the review's title or text (whitespace collapsed). Anything else is downgraded to 'unclear' and logged. Writes relevance-verified.json and relevance-summary.json."""
import collections, json, pathlib, re
H = pathlib.Path(__file__).parent; ws = lambda s: re.sub(r"\s+", " ", s).strip()
inp = {}
for i in (1, 2, 3):
    for l in open(H / f"slices/relevance-{i}.jsonl"):
        r = json.loads(l); inp[r["id"]] = r
out = {}; log = []
for i in (1, 2, 3):
    for t in json.load(open(H / f"relevance-{i}-tags.json")):
        r = inp.get(t["id"])
        if r is None: log.append((t["id"], "unknown id")); continue
        rel, ev = t["relevance"], t.get("evidence", "")
        if rel == "caregiving":
            ok = bool(ev) and (ws(ev) in ws(r["text"]) or ws(ev) in ws(r["title"]))
            if not ok: log.append((t["id"], "caregiving without an exact evidence quote -> unclear")); rel = "unclear"
        out[t["id"]] = {"relevance": rel, "reason": t["reason"], "evidence": ev if rel == "caregiving" else ""}
missing = sorted(set(inp) - set(out))
json.dump(out, open(H / "relevance-verified.json", "w"), indent=1, ensure_ascii=False)
c = collections.Counter(v["relevance"] for v in out.values())
s = {"input": len(inp), "tagged": len(out), "missing": missing, "downgraded": log, "counts": c}
json.dump(s, open(H / "relevance-summary.json", "w"), indent=1, default=dict)
print(json.dumps(s, indent=1, default=dict))
