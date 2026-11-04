"""Count the tagged Reddit posts (tagging/tags-*.jsonl, plus tags-other-*.jsonl when present).
Only posts tagged caregiver=true AND relevant=true count. Per column: works / problem / need-with-nothing,
then the problem phrases grouped into plain-word themes by keyword (a phrase can fall in one theme;
first match wins, the rest is "other"). Writes reddit-findings.json. Re-run: python3 -I analyze_tags.py"""
import json, re, glob, collections, pathlib, sys
GROUP = sys.argv[1] if len(sys.argv) > 1 else "main"  # main = CaregiverSupport + AgingParents; other = the 11 other communities
HERE = pathlib.Path(__file__).parent
THEMES = {
 "1": [("Siblings or relatives won't share the work", r"sibling|brother|sister|uncle|cousin|relative|family|aunt|alone|help"),
       ("Info spread across group chats, calendars and paper; things slip", r"group|chat|text|whatsapp|calendar|paper|scatter|lost|missed|track|system|app|update")],
 "2": [("Updates lost, ignored or start fights in group chats and texts", r"group|chat|text|whatsapp|thread|ignore|lost|messy|calendar"),
       ("Constant requests for updates; answering the same questions", r"ask|update|same question|constant|calls|coordinat"),
       ("A parent or relative withholds information", r"withhold|block|share|told|won't|exclud|mislead|tells only"),
       ("Parent can't use the tech to stay in touch", r"can't use|can't operate|confus|landline|smartphone|video|portal|photo")],
 "3": [("Bank, insurer or agency won't deal with the caregiver (even with POA)", r"bank|poa|insur|social security|company|agency|dfas|ppl|won't talk|government"),
       ("Codes and sign-ins go to the parent's phone or email", r"code|2fa|2-step|two-step|phone|email|proxy|mychart|portal"),
       ("Parent's passwords lost, forgotten, hidden or on scraps of paper", r"password|login|log in|pin|locked"),
       ("Scams or hacked accounts", r"scam|hack|fake")],
 "4": [("Can't tell from afar whether doses were taken", r"took|taken|tell|remote|far|afar|confirm|missed dose|alert"),
       ("Med changes not shared; double doses or mix-ups in the family", r"double|share|group|whatsapp|sister|family|calendar|chang|scatter|list|conflict|mis-given|nobody"),
       ("Parent forgets or refuses; organizers and reminders don't stick", r"organizer|forget|ignore|refus|remind|box|pill|text|call|app")],
 "5": [("No power of attorney, or POA rejected or delayed", r"poa|power of attorney|guardian|attorney|lawyer|notar"),
       ("Papers and records scattered or lost (binders, camera roll, portals)", r"scatter|lost|binder|paper|camera|portal|pile|find|organiz|search"),
       ("Parent won't share wishes, will or account info", r"won't|refuse|hid|secret|not shared|share")],
 "6": [("Too many portals, or proxy access blocked", r"portal|mychart|proxy|login|password|code"),
       ("Doctors' offices don't share or talk to each other", r"doctor|office|share|talk|records|hospital|prescription")],
 "7": [("Parent won't wear, charge or use the device", r"wear|charg|refuse|won't|will not|disabl|turn off|reject|carry|can't operate|hassle|misuse|pressing"),
       ("Device unreliable: missed falls, false alarms, can't connect", r"false|connect|reliab|fail|broke|accident|hear"),
       ("Device calls a dispatcher, not the family; or costs too much", r"service|dispatch|call center|random number|\$|fee|cost|month"),
       ("No way for family to know the parent is OK or where they are", r"alone|far|know|check|reach|watch|track|location|gps|timeline|monitor|fall")],
 "8": [("Doing it alone; family won't help", r"alone|sibling|brother|sister|family|nobody|no one|relative|uncle|only child|sole"),
       ("No respite or breaks", r"respite|break|sleep|vacation|relief|day off|days off"),
       ("Burnout with no one who understands", r"burn|understand|talk|vent|therap|support|grief|cope")],
}
rows = []
for f in sorted(glob.glob(str(HERE/("tagging/tags-*.jsonl" if GROUP == "main" else "tagging/other-tags-*.jsonl")))):
    rows += [json.loads(l) for l in open(f)]
# full post text, to drop app-maker posts and copies of the same post
TEXT = {}
for f in glob.glob(str(HERE/"tagging/chunk-*.jsonl")) + glob.glob(str(HERE/"tagging/other-chunk-*.jsonl")):
    for l in open(f): d = json.loads(l); TEXT[d["key"]] = d["text"]
BUILDER = r"i'?m building|we built|i built|we're building|building something|i am making something|i made an app|my startup|feedback on (my|our)|ended up building|building a (small )?(tool|app)|i created an app|i developed"
keep, seen, dropped = [], set(), {"app_maker": [], "duplicate": []}
for r in rows:
    if not (r.get("caregiver") and r.get("relevant")): continue
    t = TEXT.get(r["key"], "")
    sig = re.sub(r"\W+", "", t.lower())[:300]
    if re.search(BUILDER, t.lower()): dropped["app_maker"].append(r["url"]); continue
    if sig in seen: dropped["duplicate"].append(r["url"]); continue
    seen.add(sig); keep.append(r)
out = {"posts_tagged": len(rows), "caregiver_and_relevant": len(keep), "dropped": dropped, "columns": {}}
print("kept", len(keep), "dropped app-maker", len(dropped["app_maker"]), "duplicates", len(dropped["duplicate"]))
for c in "12345678":
    tagged = [r for r in keep if c in (r.get("columns") or {})]
    cnt = collections.Counter(r["columns"][c] for r in tagged)
    th = collections.Counter(); ex = collections.defaultdict(list)
    for r in tagged:
        if r["columns"][c] not in "PN": continue
        p = (r.get("problem") or "").lower()
        name = next((n for n, pat in THEMES[c] if re.search(pat, p)), "Other")
        th[name] += 1
        if r.get("quote") and len(ex[name]) < 4:
            ex[name].append({"quote": r["quote"], "url": r["url"], "date": r["created"], "subreddit": r["subreddit"]})
    wq = [{"quote": r["quote"], "url": r["url"], "date": r["created"]} for r in tagged if r["columns"][c] == "W" and r.get("quote")][:3]
    out["columns"][c] = {"posts": len(tagged), "works": cnt["W"], "problem_with_tool": cnt["P"], "need_nothing_works": cnt["N"],
                         "themes": th.most_common(), "theme_quotes": ex, "works_quotes": wq}
tools = collections.Counter()
for r in keep:
    for t in set(x.lower().strip().rstrip("s") for x in r.get("tools") or []): tools[t] += 1
out["tools_named"] = tools.most_common(40)
out["wishes"] = [{"wish": r["wish"], "url": r["url"], "date": r["created"]} for r in keep if r.get("wish")]
json.dump(out, open(HERE/("reddit-findings.json" if GROUP == "main" else "reddit-findings-other.json"), "w"), indent=1, ensure_ascii=False)
for c, v in out["columns"].items():
    print(c, v["posts"], "W", v["works"], "P", v["problem_with_tool"], "N", v["need_nothing_works"], v["themes"])
