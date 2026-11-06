"""Same topic words as build_candidates.py, for posts_targeted.jsonl (the 11 other communities).
Narrow topics: all kept. Documents and support: random 25 per community at most (seed 42).
Writes tagging/other-chunk-1..4.jsonl. Re-run: python3 build_candidates_other.py"""
import json, re, random, collections, pathlib, ast
HERE = pathlib.Path(__file__).parent
tree = ast.parse(open(HERE/"build_candidates.py").read())
ns = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) in ("NARROW", "BROAD"):
        ns[node.targets[0].id] = ast.literal_eval(node.value)
NARROW, BROAD = ns["NARROW"], ns["BROAD"]
picked, broad, stats = [], collections.defaultdict(list), collections.Counter()
for l in open(HERE/"posts_targeted.jsonl"):
    d = json.loads(l); t = d["text"].lower()
    if len(t) < 80: continue
    hits = [k for k, p in NARROW.items() if re.search(p, t)]
    if hits: d["topics"] = hits; picked.append(d); stats[d["subreddit"]] += 1; continue
    for k, p in BROAD.items():
        if re.search(p, t): broad[(d["subreddit"], k)].append(d); break
random.seed(42)
for (s, k), lst in sorted(broad.items()):
    for d in random.sample(lst, min(25, len(lst))): d["topics"] = [k]; picked.append(d); stats[s] += 1
for d in picked: d["text"] = d["text"][:2500]
print(len(picked), dict(stats))
for i in range(4):
    with open(HERE/f"tagging/other-chunk-{i+1}.jsonl", "w") as o:
        for d in picked[i::4]: o.write(json.dumps(d, ensure_ascii=False) + "\n")
