"""Step 5a copy of save_pages.py (new URLs only). Save exact copies of public company pages (HTML) and extract text by code. Respects robots.txt (urllib.robotparser) and waits between requests.
A page that is blocked, disallowed or returns an error is logged and NOT bypassed. Usage: python3 save_pages.py"""
import json, pathlib, re, time, urllib.request, urllib.robotparser, urllib.parse, html
HERE = pathlib.Path(__file__).parent
UA = "Mozilla/5.0 (research; contact: project owner)"
PAGES = {
 "trualta": ["https://www.trualta.com/getting-started/", "https://areaagencyonaging.org/trualta-caregiver-support/", "https://www.ageways.org/caregiver-services/trualta-family-caregiver-online-learning/", "https://www.coaaa.org/services/trualta-online-caregiver-resource/"],
 "cariloop": ["https://hr.msu.edu/benefits/caregiving/cariloop-faqs.html"],
 "calm": ["https://www.calm.com/freetrial/plans", "https://www.everydayhealth.com/mental-health-services/calmapp-review/"],
 "headspace": ["https://www.headspace.com/teachers/sam", "https://lifestack.ai/blog/headspace-pricing"],
}
PAGES_OLD = {
 "lively": ["https://www.lively.com/", "https://www.lively.com/mobile-apps/lively-link/", "https://www.lively.com/medical-alert-systems/"],
 "medical-guardian": ["https://www.medicalguardian.com/", "https://www.medicalguardian.com/caregiver-portal", "https://www.medicalguardian.com/pricing"],
 "aloe-care": ["https://www.aloecare.com/", "https://www.aloecare.com/pages/aloe-care-app"],
 "life360": ["https://www.life360.com/", "https://www.life360.com/membership/"],
 "apple-watch": ["https://www.apple.com/watch/", "https://support.apple.com/en-us/108896", "https://support.apple.com/guide/watch/use-fall-detection-apd8ac6d8f6e/watchos"],
 "omron": ["https://omronhealthcare.com/", "https://omronhealthcare.com/omron-connect-app"],
 "withings": ["https://www.withings.com/us/en/", "https://www.withings.com/us/en/health-mate"],
 "1password": ["https://1password.com/", "https://1password.com/features/", "https://1password.com/pricing/"],
 "keeper": ["https://www.keepersecurity.com/", "https://www.keepersecurity.com/features.html", "https://www.keepersecurity.com/pricing/personal-and-family.html"],
 "epic-mychart": ["https://www.mychart.org/", "https://www.epic.com/epic/mychart/"],
}
def text_of(h):
    h = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", h); h = re.sub(r"(?s)<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()
log = []
for co, urls in PAGES.items():
    d = HERE / co; d.mkdir(exist_ok=True)
    for u in urls:
        pu = urllib.parse.urlparse(u); rp = urllib.robotparser.RobotFileParser(f"{pu.scheme}://{pu.netloc}/robots.txt")
        try: rp.read(); allowed = rp.can_fetch(UA, u)
        except Exception: allowed = True
        name = re.sub(r"[^a-z0-9]+", "_", (pu.netloc + pu.path).lower()).strip("_")[:80]
        rec = {"company": co, "url": u, "robots_allowed": allowed, "file": None, "status": None, "bytes": 0}
        if not allowed: rec["status"] = "disallowed by robots.txt"; log.append(rec); continue
        try:
            req = urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "en-US"})
            resp = urllib.request.urlopen(req, timeout=30); raw = resp.read(); rec["status"] = resp.status
            (d / f"{name}.html").write_bytes(raw); (d / f"{name}.txt").write_text(text_of(raw.decode("utf8", "ignore")))
            rec["file"] = f"{co}/{name}.html"; rec["bytes"] = len(raw)
            t = text_of(raw.decode("utf8", "ignore")).lower()
            if len(raw) < 3000 or "verify you are human" in t or "access denied" in t or "just a moment" in t: rec["note"] = "possible bot page or tiny page: check before use"
        except Exception as ex: rec["status"] = f"error: {str(ex)[:80]}"
        log.append(rec); time.sleep(1.5)
json.dump(log, open(HERE / "save_log.json", "w"), indent=1)
for r in log: print(r["company"].ljust(17), str(r["status"]).ljust(34), r["bytes"], r.get("note", ""), "|", r["url"][-55:])
