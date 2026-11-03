"""Second batch of public company pages (problems 5, 6, 7). Same rules as save_pages.py: robots.txt respected, nothing bypassed, errors logged."""
import json, pathlib, re, time, html, urllib.request, urllib.robotparser, urllib.parse
HERE = pathlib.Path(__file__).parent; UA = "Mozilla/5.0 (research; contact: project owner)"
PAGES = {
 "calm": ["https://www.calm.com/", "https://www.calm.com/pricing"],
 "headspace": ["https://www.headspace.com/", "https://www.headspace.com/subscriptions"],
 "talkspace": ["https://www.talkspace.com/", "https://www.talkspace.com/how-it-works"],
 "betterhelp": ["https://www.betterhelp.com/", "https://www.betterhelp.com/get-started/"],
 "alight": ["https://alight.com/", "https://alight.com/solutions/alight-worklife"],
 "accolade": ["https://www.accolade.com/", "https://www.accolade.com/solutions"],
 "included-health": ["https://includedhealth.com/", "https://includedhealth.com/about"],
 "rightway": ["https://www.rightwayhealthcare.com/", "https://www.rightwayhealthcare.com/about"],
}
def text_of(h):
    h = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", h); h = re.sub(r"(?s)<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()
log = []
for co, urls in PAGES.items():
    d = HERE / co; d.mkdir(exist_ok=True)
    for u in urls:
        pu = urllib.parse.urlparse(u); rp = urllib.robotparser.RobotFileParser(f"{pu.scheme}://{pu.netloc}/robots.txt")
        try: rp.read(); ok = rp.can_fetch(UA, u)
        except Exception: ok = True
        name = re.sub(r"[^a-z0-9]+", "_", (pu.netloc + pu.path).lower()).strip("_")[:80]
        rec = {"company": co, "url": u, "robots_allowed": ok, "file": None, "status": None, "bytes": 0}
        if not ok: rec["status"] = "disallowed by robots.txt"; log.append(rec); continue
        try:
            resp = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "en-US"}), timeout=30); raw = resp.read(); rec["status"] = resp.status
            (d / f"{name}.html").write_bytes(raw); tx = text_of(raw.decode("utf8", "ignore")); (d / f"{name}.txt").write_text(tx)
            rec["file"] = f"{co}/{name}.html"; rec["bytes"] = len(raw); rec["final_url"] = resp.geturl()
            if len(tx) < 1500 or re.search(r"verify you are human|access denied|just a moment", tx.lower()): rec["note"] = "tiny or possible bot page: check before use"
        except Exception as ex: rec["status"] = f"error: {str(ex)[:80]}"
        log.append(rec); time.sleep(1.5)
json.dump(log, open(HERE / "save_log2.json", "w"), indent=1)
for r in log: print(r["company"].ljust(16), str(r["status"]).ljust(30), r["bytes"], r.get("note", ""), "|", r["url"][-48:])
