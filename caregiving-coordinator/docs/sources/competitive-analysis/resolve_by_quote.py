"""For saved pages whose live <title> no longer matches, look for a live URL whose visible text contains one of the exact quotes taken from that saved page.
Respects robots.txt. Updates urls.json with basis 'quote from the saved page found on the live page (date)'."""
import json, pathlib, re, time, html, urllib.request, urllib.robotparser, urllib.parse, datetime
HERE = pathlib.Path(__file__).parent; SRC = HERE.parent; UA = "Mozilla/5.0 (research; contact: project owner)"
TLDS = {"com","org","net","io","co","app","health","care","ai","us","gov","edu","me"}
ws = lambda s: re.sub(r"\s+", " ", s).strip()
urls = json.load(open(HERE / "urls.json")); man = json.load(open(HERE / "manifest.json"))
mu = {f["txt"]: f["url"] for v in man.values() for f in v}
quotes = {}
for i in range(1, 5):
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
                p = "/".join(rest[:k]) + ("/" if 0 < k < len(rest) else "") + "-".join(rest[k:])
                out += [f"https://{host}/{p}", f"https://{host}/{p}/"]
    if mu.get(txt): out.append(mu[txt])
    seen = set(); return [c for c in out if not (c in seen or seen.add(c))]
cache = {}
def live_text(u):
    if u in cache: return cache[u]
    pu = urllib.parse.urlparse(u); t = None
    try:
        rp = urllib.robotparser.RobotFileParser(f"{pu.scheme}://{pu.netloc}/robots.txt"); rp.read()
        if rp.can_fetch(UA, u):
            raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=20).read(2_000_000).decode("utf8", "ignore")
            raw = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", raw); t = ws(html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw)))
    except Exception: t = None
    cache[u] = t; time.sleep(0.4); return t
today = datetime.date.today().isoformat(); n = 0
for txt, v in urls.items():
    if v["url"] or txt not in quotes: continue
    for c in cands(txt)[:12]:
        t = live_text(c)
        if t and any(q in t for q in quotes[txt] if len(q) > 25):
            urls[txt] = {"url": c, "basis": f"a quote from the saved page was found on this live page ({today})"}; n += 1; break
json.dump(urls, open(HERE / "urls.json", "w"), indent=1)
print(n, "more resolved;", sum(1 for v in urls.values() if v["url"]), "of", len(urls), "now have a verified URL")
for txt, v in urls.items():
    if not v["url"]: print("still unresolved:", txt[-60:])
