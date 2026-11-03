"""Check forum relevance tags: every evidence and lives_with quote must be an exact substring (whitespace collapsed) of the saved thread, at most 250 characters.
A 'caregiving' tag without a verified evidence quote is downgraded to 'unclear'. Writes forum-verified.json."""
import json, re, sys, pathlib, collections
HERE = pathlib.Path(__file__).parent; BASE = HERE.parent
ws = lambda s: re.sub(r"\s+", " ", s).strip()
items = {i["id"]: i for k in range(1, 5) for i in json.load(open(HERE / f"slice-{k}.json"))}
tagfiles = sys.argv[1:] or [f"tags-{k}.json" for k in range(1, 5)]
out = {}; fails = []
for tf in tagfiles:
    for t in json.load(open(HERE / tf)):
        it = items.get(t["id"]); text = ws((BASE / it["path"]).read_text(errors="ignore")) if it else ""
        ev_ok = bool(t["evidence"]) and ws(t["evidence"]) in text and len(t["evidence"]) <= 250
        lw_ok = (not t.get("lives_with_quote")) or (ws(t["lives_with_quote"]) in text and len(t["lives_with_quote"]) <= 250)
        rel = t["relevance"]
        if rel == "caregiving" and not ev_ok: fails.append((t["id"], "evidence not exact")); rel = "unclear"
        if not lw_ok: fails.append((t["id"], "lives_with quote not exact")); t["lives_with"] = "not_stated"; t["lives_with_quote"] = ""
        out[t["id"]] = {**t, "relevance_verified": rel, "site": it["site"] if it else None}
json.dump(out, open(HERE / "forum-verified.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "threads;", collections.Counter(v["relevance_verified"] for v in out.values()), "failures:", len(fails)); [print(f) for f in fails]
missing = set(items) - set(out); print("missing from tags:", sorted(missing))
