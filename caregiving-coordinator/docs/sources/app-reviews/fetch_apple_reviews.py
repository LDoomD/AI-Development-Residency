"""Save exact copies of Apple's public App Store review feed (RSS/JSON) for a list of apps, then extract text by code.
No login, no scraping of HTML pages: this is Apple's public customer-reviews feed (max 10 pages x 50 most recent per app and country).
Usage: python3 fetch_apple_reviews.py            (fetch + extract)
       python3 fetch_apple_reviews.py extract    (extract only, from saved raw files)
Raw files keep reviewer usernames; reviews.csv does not."""
import csv, json, pathlib, re, sys, time, urllib.request

ROOT = pathlib.Path(__file__).parent
RAW = ROOT / "raw"
# (country, app id, short name, group)
APPS = [
 # coordination and family sharing
 ("us",1093814557,"caring-village","family-coordination"),("us",365726944,"caringbridge","family-coordination"),
 ("us",606923858,"lotsa-helping-hands","family-coordination"),("us",1441737626,"ianacare","family-coordination"),
 ("us",407108860,"cozi","family-organizer"),("us",952578473,"timetree","family-organizer"),("us",496889629,"familywall","family-organizer"),
 ("us",1451631772,"caregiver-john-hancock","family-coordination"),("us",1658816779,"tendercare","family-coordination"),
 # medication and visit notes
 ("us",573916946,"medisafe","medication"),("us",662170995,"mytherapy","medication"),("us",6756894542,"kin","visit-notes"),
 # safety, alerts, location
 ("us",584004617,"lively-link","safety-alert"),("us",1577560184,"mymedicalguardian","safety-alert"),("us",1467385415,"aloe-care","safety-alert"),
 ("us",384830320,"life360","location-safety"),("us",1122758716,"snug","safety-checkin"),("us",1547299584,"fallcall-detect","safety-alert"),
 # health devices and watches
 ("us",1069511734,"apple-watch-app","watch"),("us",1117310635,"samsung-galaxy-watch","watch-android"),("us",986496028,"wear-os","watch-android"),
 ("us",1027370544,"fossil-smartwatches","watch-android"),("us",462638897,"google-health-fitbit","watch"),("us",583446403,"garmin-connect","watch"),
 ("us",1224541484,"samsung-health","watch-android"),("us",1392205704,"seizure-alert-my-medic-watch","watch"),
 ("us",1166317885,"omron-connect","blood-pressure"),("us",542701020,"withings","blood-pressure"),("us",579769143,"kardia","heart-monitor"),
 # international (home storefront; learning only, the market stays US)
 ("gb",1573762662,"altra-family","intl-family-coordination"),("gb",1603401574,"careberry-family","intl-family-coordination"),
 ("gb",1317876340,"komp","intl-senior-connection"),("au",1272475947,"careapp","intl-family-coordination"),
 ("au",1541576444,"ask-annie-dementia-australia","intl-dementia"),("au",1410066247,"dayspringcare","intl-family-coordination"),
 ("au",6475165496,"carewindow","intl-family-coordination"),("de",1622027002,"marta","intl-family-coordination"),
 ("de",6756123783,"luma-life","intl-family-coordination"),("in",6761720384,"famcare","intl-family-coordination"),
 ("in",1486830873,"guardio-family-care","intl-family-coordination"),("jp",6767451603,"keazu","intl-family-coordination"),
 ("jp",867437900,"ouchi-karte","intl-family-health"),("jp",1062745479,"heartwatch-jp","watch"),("ca",1588765065,"tuktu","intl-family-coordination"),
]
MAX_PAGES = 10

def fetch():
    for cc, aid, name, grp in APPS:
        d = RAW / cc; d.mkdir(parents=True, exist_ok=True)
        for p in range(1, MAX_PAGES + 1):
            f = d / f"{aid}-{name}-p{p}.json"
            if f.exists(): continue
            url = f"https://itunes.apple.com/{cc}/rss/customerreviews/page={p}/id={aid}/sortby=mostrecent/json"
            try:
                raw = urllib.request.urlopen(url, timeout=30).read()
            except Exception as ex:
                print("STOP", cc, name, p, ex); break
            f.write_bytes(raw)
            ents = json.loads(raw).get("feed", {}).get("entry", [])
            ents = ents if isinstance(ents, list) else [ents]
            n = sum(1 for e in ents if "im:rating" in e)
            print(cc, name, "page", p, n, "reviews", flush=True)
            time.sleep(1.2)
            if n < 50: break

def extract():
    meta = {(cc, str(aid)): (name, grp) for cc, aid, name, grp in APPS}
    rows = []
    for f in sorted(RAW.glob("*/*.json")):
        cc = f.parent.name; aid = f.name.split("-")[0]
        name, grp = meta.get((cc, aid), (f.name, ""))
        ents = json.loads(f.read_text()).get("feed", {}).get("entry", [])
        ents = ents if isinstance(ents, list) else [ents]
        for e in ents:
            if "im:rating" not in e: continue
            rows.append([cc, grp, name, aid, e["im:rating"]["label"], e["title"]["label"], e["content"]["label"],
                         e.get("im:version", {}).get("label", ""), e.get("updated", {}).get("label", ""), f.name])
    with open(ROOT / "reviews.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["country","group","app","app_id","stars","title","text","app_version","date","source_file"]); w.writerows(rows)
    print(len(rows), "reviews written to reviews.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2: fetch()
    extract()
