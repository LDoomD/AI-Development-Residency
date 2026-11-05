"""Step 1 of the audience split (checklist: research-checklist-audience-split.md). Labels each of the 831 relevant
relief posts with the market analysis "cared_for" labels, using how the writer names the person cared for.
A post gets a script label only when one group of words clearly dominates (at least 3 matches, and at least 3 times
any other group). Everything else goes to readers (audience-packs/). The matched words are saved for every post.
Writes audience-script.json and audience-packs/apack-N.json (unclear posts + a random 40 of the script labels)."""
import json, re, random, pathlib, collections
H = pathlib.Path(__file__).parent
G = {
 "parent": r"\b(?:my|our)\s+(?:elderly\s+|aging\s+|aged\s+|own\s+)?(?:mom|mother|mum|mama|dad|father|papa|parents?|mil|fil|mother[- ]in[- ]law|father[- ]in[- ]law|in[- ]laws|step ?(?:mom|mother|dad|father))\b|\b(?:Mom|Dad|Mother|Father|Mum)\b(?!\s+and\s+(?:I|me))",
 "spouse or partner": r"\b(?:my|our)\s+(?:husband|wife|spouse|partner|hubby|dh|dw|boyfriend|girlfriend|bf|gf|fianc[eé]e?)\b",
 "other relative": r"\b(?:my|our)\s+(?:grand(?:ma|mother|pa|father|parents?)|nana|granny|brother|sister|aunt|uncle|cousin|sibling|niece|nephew)\b",
 "child": r"\b(?:my|our)\s+(?:son|daughter|child|kid|toddler|baby)\b",
}
RX = {k: re.compile(v) for k, v in G.items()}
RXI = {k: re.compile(v, re.I) for k, v in G.items() if k != "parent"}
items = {}; codes = []
for n in range(1, 12):
    for i in json.load(open(H / "packs" / f"pack-{n}.json")): items[i["id"]] = i
    codes += json.load(open(H / "codes" / f"codes-{n}.json"))
rel = [c["id"] for c in codes if c.get("relevant")]
out = {}; unclear = []
for i in rel:
    t = items[i]["text"]
    cnt = {"parent": len(re.findall(re.compile(G["parent"].split("|\\b(?:Mom")[0], re.I), t)) + len(re.findall(r"\b(?:Mom|Dad|Mother|Father|Mum)\b", t))}
    for k, rx in RXI.items(): cnt[k] = len(rx.findall(t))
    words = {k: sorted({m.group(0) for m in (RX[k] if k == "parent" else RXI[k]).finditer(t)})[:8] for k in G}
    top = max(cnt, key=cnt.get); rest = max([v for k, v in cnt.items() if k != top] + [0])
    if cnt[top] >= 3 and cnt[top] >= 3 * max(rest, 1) and rest <= cnt[top] / 3:
        out[i] = {"label": top, "how": "script", "counts": cnt, "words": words}
    else:
        out[i] = {"label": None, "how": "reader", "counts": cnt, "words": words}; unclear.append(i)
rnd = random.Random(20261104)
spot = rnd.sample([i for i, v in out.items() if v["how"] == "script"], 40)
for i in spot: out[i]["spot_check"] = True
json.dump(out, open(H / "audience-script.json", "w"), indent=1, ensure_ascii=False)
todo = unclear + spot; rnd.shuffle(todo)
(H / "audience-packs").mkdir(exist_ok=True)
k = max(1, round(len(todo) / 110)); size = -(-len(todo) // k)
for n in range(k):
    part = todo[n * size:(n + 1) * size]
    json.dump([{"id": i, "text": items[i]["text"], "url": items[i]["url"]} for i in part], open(H / "audience-packs" / f"apack-{n+1}.json", "w"), indent=1, ensure_ascii=False)
print("relevant", len(rel), "| script-labeled", sum(v["how"] == "script" for v in out.values()), collections.Counter(v["label"] for v in out.values() if v["how"] == "script"))
print("to readers:", len(unclear), "unclear +", len(spot), "spot check =", len(todo), "in", k, "packs")
