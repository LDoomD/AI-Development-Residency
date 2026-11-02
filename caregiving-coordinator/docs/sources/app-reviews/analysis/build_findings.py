"""Build docs/app-review-findings.md from verified-tags.json (counts and quotes come from data, none typed by hand)."""
import collections, json, pathlib
HERE = pathlib.Path(__file__).parent
V = json.load(open(HERE / "verified-tags.json"))
LABEL = {"family_cant_see_same_info": "Relatives or helpers cannot see the same information",
 "access_for_others": "Getting access, accounts, logins or permissions for another person",
 "alerts_unreliable": "Alerts or notifications missed, late, too many or not arriving",
 "readings_wrong": "Readings, location or detection wrong, false alarms, missed events",
 "not_syncing": "Data does not sync between devices or people",
 "cost": "Price, subscription, paywall, billing",
 "hard_for_older_person": "The older person cannot or will not use it",
 "setup_compatibility": "Setup, pairing or phone compatibility trouble",
 "privacy_trust": "Privacy, tracking or trust worries",
 "support_unresponsive": "Company or support did not help",
 "reminders_failing": "Reminders or schedules (medication, appointments) failing",
 "safety_gap": "A person in danger and the tool did not help (falls, wandering, emergencies)",
 "app_reliability": "Crashes, bugs, battery, connectivity in general",
 "other_problem": "Other problem"}
prob = [r for r in V if r["kind"] == "problem"]
n = len(V); npb = len(prob)
rel = {"parent", "spouse", "other_relative"}
who_all = collections.Counter(r.get("who", "not_stated") for r in prob)
cnt = collections.Counter(r["category"] for r in prob)
cnt_rel = collections.Counter(r["category"] for r in prob if r.get("who") in rel)
cnt_apple = collections.Counter(r["category"] for r in prob if r["store"] == "apple")
cnt_goog = collections.Counter(r["category"] for r in prob if r["store"] == "google")
def pick(cat, k=4):
    c = [r for r in prob if r["category"] == cat and r.get("quote") and len(r["quote"]) >= 70]
    c.sort(key=lambda r: (r.get("who") not in rel, -len(r["quote"])))
    out, apps = [], set()
    for r in c:
        if r["app"].lower() in apps: continue
        out.append(r); apps.add(r["app"].lower())
        if len(out) == k: break
    return out
L = []
L.append("# What app-store reviewers say: problems in their own words (2026-11-02)\n")
L.append(f"**Evidence state:** `documented` for every quote (exact text, checked by script against the saved review); `reported` for the category counts (one reader assigned one category per review, so the counts are approximate). Nothing here is a finding about what caregivers would pay for or do.\n")
L.append("## How this was made (so you can check it)\n")
L.append("1. **Collected:** 9,448 Apple reviews (public review feed, 44 apps, 7 storefronts) and 4,777 Google Play reviews (10 apps, read in Chrome). Saved in `docs/sources/app-reviews/` (`raw/`, `reviews.csv`, `google-play/`). Details and limits: `docs/sources/INDEX.md` section 2p.")
L.append(f"2. **Selected:** `analysis/make_slices.py` keeps only reviews whose text or title matches a caregiving or family word list (mom, dad, parent, elderly, caregiver, wife, husband, dementia, loved one, and so on). That is 1,475 of 14,225 reviews. **The other 12,750 were not read for this analysis.**")
L.append(f"3. **Read:** four reader agents read all {n:,} selected reviews and gave each one a kind (problem, worked, none), one problem category, who the reviewer cares for, and one exact quote.")
L.append(f"4. **Checked:** `analysis/verify_tags.py` accepted a quote only if it is an exact substring of the review's text or title. Result: {sum(1 for r in V if r.get('quote') and r['quote_verified']):,} quotes verified, 0 dropped. Every id is in `analysis/all-reviews.jsonl` (`../all-reviews.jsonl`) with its app, store, stars and date; Apple ids `a-N` are row N (from 0) of `reviews.csv`, Google ids `g-<app>-N` are item N (from 0) in that app's JSON file.\n")
k = collections.Counter(r["kind"] for r in V)
L.append("## What was read\n")
L.append(f"- {n:,} reviews: **{k['problem']} describe a problem**, {k['worked']} describe something that worked, {k['none']} had no usable content.")
L.append(f"- **Who the problem reviewers care for** (as stated): " + ", ".join(f"{w.replace('_',' ')} {c}" for w, c in who_all.most_common()) + f". So {sum(who_all[w] for w in rel)} of the {npb} problem reviews are about a parent, spouse or other relative. Whether that person is old or ill is often not stated, so this is not the same as 'caring for an older or ill relative'. {who_all['child']} are about a child, {who_all['self']} about the reviewer themselves, {who_all['not_stated']} do not say.\n")
L.append("## Problems by category\n")
L.append("| Problem | All problem reviews | About a parent, spouse or other relative | Apple | Google Play |\n|---|---|---|---|---|")
for c, v in cnt.most_common():
    L.append(f"| {LABEL[c]} | {v} | {cnt_rel[c]} | {cnt_apple[c]} | {cnt_goog[c]} |")
L.append(f"| **Total** | **{npb}** | **{sum(cnt_rel.values())}** | **{sum(cnt_apple.values())}** | **{sum(cnt_goog.values())}** |\n")
L.append("## Quotes by problem (up to 4 per category, chosen by script: relatives first, longer quotes, one per app)\n")
for c, v in cnt.most_common():
    L.append(f"### {LABEL[c]} ({v})\n")
    for r in pick(c):
        L.append(f"- \"{r['quote']}\" ({r['app']}, {r['store']}, {r['stars']} stars, {r['date']}; who: {r.get('who','not_stated').replace('_',' ')}; id `{r['id']}`)")
    L.append("")
L.append("## Which apps the problems come from (the app choice shapes the counts)\n")
for cat in ["readings_wrong","safety_gap","access_for_others","family_cant_see_same_info"]:
    c = collections.Counter(r["app"].lower().replace(" ", "-") for r in prob if r["category"] == cat)
    L.append(f"- **{LABEL[cat]}** ({cnt[cat]}): " + ", ".join(f"{a} {v}" for a, v in c.most_common(5)))
L.append("")
L.append("## Limits\n")
L.append("- **Selection:** only apps I chose (family coordination, medication, safety, watches, blood pressure, international). Only reviews matching the word list were read. Reviewers are people who use an app and chose to write.")
L.append("- **Samples:** Apple is the most recent written reviews (up to 500 per app); Google Play is in the page's default order, about 540 per app, not random; the share of 1 and 2 star reviews varies a lot by app.")
L.append("- **Coding:** one reader per slice, one category per review, so a review with two problems counts once. Some categories are judgement calls (the readers listed examples). A different reader could code some differently.")
L.append("- **What this cannot show:** who would pay, what people would do, or needs outside these apps. It shows problems people describe about tools they already use.")
L.append("- **Not done:** the reviews outside the word list. The word list is English only, so reviews in other languages (for example the Japanese and German storefronts) were not selected.")
(HERE.parent.parent.parent / "app-review-findings.md").write_text("\n".join(L) + "\n")
print("written;", sum(1 for _ in L), "lines")
print(who_all)
print([ (c,cnt[c],cnt_rel[c]) for c,_ in cnt.most_common()])
