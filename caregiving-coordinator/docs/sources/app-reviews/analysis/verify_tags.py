"""Verify reader tags against the original reviews. A quote counts only if it is an exact substring of the review's text or title
(runs of whitespace are collapsed to one space on both sides; nothing else is normalized). Writes verified-tags.json, failed-tags.json and summary.json."""
import collections, json, pathlib, re
HERE = pathlib.Path(__file__).parent
ws = lambda s: re.sub(r"\s+", " ", s).strip()
orig = {}
for i in range(1, 6):
    for line in open(HERE / "slices" / f"slice-{i}.jsonl"):
        r = json.loads(line); r["slice"] = i; orig[r["id"]] = r
CATS = {"family_cant_see_same_info","access_for_others","alerts_unreliable","readings_wrong","not_syncing","cost","hard_for_older_person",
        "setup_compatibility","privacy_trust","support_unresponsive","reminders_failing","safety_gap","app_reliability","other_problem"}
verified, failed, missing = [], [], []
seen = set()
for i in range(1, 6):
    f = HERE / f"slice-{i}-tags.json"
    if not f.exists(): missing.append(f"slice-{i}-tags.json missing"); continue
    for t in json.load(open(f)):
        o = orig.get(t.get("id"))
        if o is None: failed.append({**t, "why": "unknown id"}); continue
        seen.add(t["id"])
        kind, cat, q = t.get("kind"), t.get("category"), t.get("quote", "")
        if kind not in ("problem", "worked", "none"): failed.append({**t, "why": "bad kind"}); continue
        if kind == "problem" and cat not in CATS: t["category"] = "other_problem"
        quote_ok = bool(q) and ws(q) in ws(o["text"]) or bool(q) and ws(q) in ws(o["title"])
        rec = {**t, "store": o["store"], "app": o["app"], "stars": o["stars"], "date": o["date"], "quote_verified": bool(quote_ok), "slice": o["slice"]}
        if q and not quote_ok: rec["quote"] = ""; rec["quote_dropped"] = q; failed.append({"id": t["id"], "why": "quote not an exact substring", "quote": q})
        verified.append(rec)
absent = sorted(set(orig) - seen)
c_kind = collections.Counter(r["kind"] for r in verified)
c_cat = collections.Counter(r["category"] for r in verified if r["kind"] == "problem")
c_cat_store = collections.defaultdict(collections.Counter)
for r in verified:
    if r["kind"] == "problem": c_cat_store[r["category"]][r["store"]] += 1
summary = {"reviews_in_slices": len(orig), "tagged": len(seen), "untagged_ids": len(absent), "missing_files": missing,
           "by_kind": c_kind, "problem_by_category": c_cat.most_common(), "quotes_verified": sum(1 for r in verified if r.get("quote") and r["quote_verified"]),
           "quotes_dropped": sum(1 for r in verified if r.get("quote_dropped")),
           "problem_by_category_and_store": {k: dict(v) for k, v in c_cat_store.items()}}
json.dump(verified, open(HERE / "verified-tags.json", "w"), indent=1, ensure_ascii=False)
json.dump(failed, open(HERE / "failed-tags.json", "w"), indent=1, ensure_ascii=False)
json.dump(summary, open(HERE / "summary.json", "w"), indent=1, ensure_ascii=False, default=dict)
print(json.dumps(summary, indent=1, ensure_ascii=False, default=dict))
