"""For each saved page in manifest.json, find a live URL whose <title> matches the saved page's <title>.
Candidates: the exact URL (competitors-2 save_log.json), the canonical/og:url, and URLs reconstructed from the file name (underscores as '/', and with '-' variants).
Respects robots.txt (a disallowed URL is not fetched). Output: urls.json {txt_path: {url, basis}}."""
import json, pathlib, re, time, html, itertools, urllib.request, urllib.robotparser, urllib.parse
SRC = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (research; contact: project owner)"
TLDS = {"com","org","net","io","co","app","health","care","ai","us","gov","edu","me"}
m = json.load(open(pathlib.Path(__file__).parent / "manifest.json"))
exact = {}
try:
    for r in json.load(open(SRC / "competitors-2/save_log.json")):
        if r.get("file"): exact["competitors-2/" + r["file"].replace(".html", ".txt")] = r["url"]
except Exception: pass
def title_of(p):
    h = pathlib.Path(p).read_text(errors="ignore")
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", h); return re.sub(r"\s+", " ", html.unescape(t.group(1))).strip().lower() if t else ""
def candidates(txt, manifest_url):
    name = pathlib.Path(txt).name[:-4]; toks = name.split("_"); toks = [t for t in toks if t != ""]
    idx = next((i for i, t in enumerate(toks) if t in TLDS and i >= 1), None)
    out = []
    if idx is not None:
        host = ".".join(toks[:idx + 1]); rest = toks[idx + 1:]
        if not rest: out.append(f"https://{host}/")
        else:
            for k in range(len(rest) + 1):  # join first k tokens with '/', remaining with '-'
                path = "/".join(rest[:k]) + ("/" if k and k < len(rest) else "") + "-".join(rest[k:]) if k < len(rest) else "/".join(rest)
                for s in ("", "/"): out.append(f"https://{host}/{path}{s}")
    if manifest_url: out.append(manifest_url)
    seen = set(); return [c for c in out if not (c in seen or seen.add(c))]
res = {}
for co, files in m.items():
    for f in files:
        txt = f["txt"]
        if "appstore-description" in txt: res[txt] = {"url": f["url"], "basis": "App Store listing"}; continue
        if txt in exact: res[txt] = {"url": exact[txt], "basis": "exact URL used when saved (save_log.json)"}; continue
        want = title_of(SRC / txt.replace(".txt", ".html")); hit = None
        for c in candidates(txt, f["url"])[:14]:
            pu = urllib.parse.urlparse(c)
            try:
                rp = urllib.robotparser.RobotFileParser(f"{pu.scheme}://{pu.netloc}/robots.txt"); rp.read()
                if not rp.can_fetch(UA, c): continue
                raw = urllib.request.urlopen(urllib.request.Request(c, headers={"User-Agent": UA}), timeout=20).read(400000).decode("utf8", "ignore")
                t = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw); got = re.sub(r"\s+", " ", html.unescape(t.group(1))).strip().lower() if t else ""
                if want and got == want: hit = c; break
            except Exception: pass
            time.sleep(0.4)
        res[txt] = {"url": hit, "basis": "live page title equals saved page title" if hit else "NOT RESOLVED: no candidate URL had the same title"}
        print(co.ljust(18), (hit or "NOT RESOLVED")[:80])
json.dump(res, open(pathlib.Path(__file__).parent / "urls.json", "w"), indent=1)
print(sum(1 for v in res.values() if v["url"]), "of", len(res), "resolved")
