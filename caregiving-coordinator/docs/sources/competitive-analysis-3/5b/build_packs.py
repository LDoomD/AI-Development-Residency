"""Build the 5b reading packs: every Reddit post naming a new competitor (full text), plus forum threads naming one.
Forum threads are long, so each forum item holds the text around every match (1,500 characters each side).
For the Alzheimer's Association, forum matches count only if they name the helpline or its number, because
ALZConnected is run by the Association and its name appears in the page text."""
import json, re, glob, pathlib
H = pathlib.Path(__file__).parent
src = open(H / "count_new_mentions.py").read(); P = eval(src.split("P = ")[1].split("\nc = ")[0])
P_FORUM = dict(P); P_FORUM["Alzheimer's Association helpline"] = r"help ?line|hotline|800[- .]?272[- .]?3900"
items = [{"id": m["key"], "source": "reddit", "competitor": m["competitor"], "url": m["url"], "text": m["text"]} for m in json.load(open(H / "mentions.json"))]
for f in sorted(glob.glob(str(H.parents[1] / "forums/**/*.txt"), recursive=True)):
    t = open(f, errors="ignore").read(); low = t.lower()
    tid = ("agi-" if "agingcare" in f else "alz-") + pathlib.Path(f).stem
    for k, p in P_FORUM.items():
        spans = [m.span() for m in re.finditer(p, low)]
        if not spans: continue
        parts = []; last = -1
        for a, b in spans:
            s, e = max(0, a - 1500), min(len(t), b + 1500)
            if s <= last: parts[-1] = (parts[-1][0], e)
            else: parts.append((s, e))
            last = parts[-1][1]
        items.append({"id": tid, "source": "forum", "competitor": k, "url": f.split("docs/sources/")[1], "text": "\n[...]\n".join(t[s:e] for s, e in parts)})
A = {"Eldercare Locator and Area Agencies on Aging", "Alzheimer's Association helpline", "Medicare GUIDE Model", "Trualta", "Calm", "Headspace", "Cariloop", "Aeroflow Urology"}
for name, sel in (("pack-1.json", lambda i: i["competitor"] in A), ("pack-2.json", lambda i: i["competitor"] not in A)):
    p = [i for i in items if sel(i)]; json.dump(p, open(H / name, "w"), indent=1, ensure_ascii=False)
    print(name, len(p), sum(len(i["text"]) for i in p), {k: sum(1 for i in p if i["competitor"] == k) for k in sorted({i["competitor"] for i in p})})
