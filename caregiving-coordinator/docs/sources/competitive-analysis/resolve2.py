"""Live URLs for the problem 5, 6, 7 pages: exact URL where known (competitors-2), else title match, else a quote from the saved page found on the live page. robots.txt respected."""
import json, pathlib, re, time, html, urllib.request, urllib.robotparser, urllib.parse, datetime
HERE = pathlib.Path(__file__).parent; SRC = HERE.parent; UA = "Mozilla/5.0 (research; contact: project owner)"
TLDS = {"com","org","net","io","co","app","health","care","ai","us","gov","edu","me"}
ws = lambda s: re.sub(r"\s+", " ", s).strip()
man = json.load(open(HERE / "manifest2.json")); quotes = {}
for i in (5, 6):
    for c in json.load(open(HERE / f"extract-{i}.json")):
        for qs in c["fields"].values():
            for q in qs: quotes.setdefault(q["file"], set()).add(ws(q["quote"]))
def cands(txt):
    toks = [t for t in pathlib.Path(txt).name[:-4].split("_") if t]
    idx = next((i for i, t in enumerate(toks) if t in TLDS and i >= 1), None); out = []
    if idx is not None:
        host = ".".join(toks[:idx + 1]); rest = toks[idx + 1:]
        if not rest: out += [f"https://{host}/"]
        else:
            for k in range(len(rest) + 1):
                p = "/".join(rest[:k]) + ("/" if 0 < k < len(rest) else "") + "-".join(rest[k:]); out += [f"https://{host}/{p}", f"https://{host}/{p}/"]
    seen = set(); return [c for c in out if not (c in seen or seen.add(c))]
cache = {}
def get(u):
    if u in cache: return cache[u]
    pu = urllib.parse.urlparse(u); res = (None, None)
    try:
        rp = urllib.robotparser.RobotFileParser(f"{pu.scheme}://{pu.netloc}/robots.txt"); rp.read()
        if rp.can_fetch(UA, u):
            raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=20).read(2_500_000).decode("utf8", "ignore")
            t = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw); title = ws(html.unescape(t.group(1))).lower() if t else ""
            body = ws(html.unescape(re.sub(r"(?s)<[^>]+>", " ", re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", raw)))); res = (title, body)
    except Exception: pass
    cache[u] = res; time.sleep(0.4); return res
today = datetime.date.today().isoformat(); out = {}
for co, files in man.items():
    for f in files:
        txt = f["txt"]
        if f.get("url"): out[txt] = {"url": f["url"], "basis": f.get("basis", "exact URL used when saved (save_log2.json)")}; continue
        saved = (SRC / txt.replace(".txt", ".html")).read_text(errors="ignore"); m = re.search(r"(?is)<title[^>]*>(.*?)</title>", saved); want = ws(html.unescape(m.group(1))).lower() if m else ""
        hit = None
        for c in cands(txt)[:12]:
            title, body = get(c)
            if body is None: continue
            if want and title == want: hit = (c, "live page title equals saved page title"); break
            if any(q in body for q in quotes.get(txt, []) if len(q) > 25): hit = (c, f"a quote from the saved page was found on this live page ({today})"); break
        out[txt] = {"url": hit[0] if hit else None, "basis": hit[1] if hit else "NOT RESOLVED"}
json.dump(out, open(HERE / "urls2.json", "w"), indent=1)
print(sum(1 for v in out.values() if v["url"]), "of", len(out), "resolved")
for k, v in out.items():
    if not v["url"]: print("unresolved:", k[-62:])
