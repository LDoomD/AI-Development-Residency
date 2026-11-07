# PASS 3 audit: Caring Village (independent check)

Date: 2026-11-06. Branch feature-analysis-4. Nothing committed. I did not do the earlier work. I tried to prove it wrong.
Repo root for all paths: `/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator` (note the space before the slash). Paths below start at `docs/sources/`.

State key (skeptical-audit): proven = a check that would fail if the claim were false ran and passed; observed = I saw it directly this session; inferred = follows from observed facts; documented = a company or neutral page says so; reported = a person's own account; not-assessed = not checked.

## How blind was I (honest limit)
- I read the earlier EVIDENCE.md and PASS files first (to know what to audit). So my recount is "re-derived from raw data", not blind in the strict sense.
- Strictly blind part: the 15-report random sample (check 2c). The script hid the old labels and I classified the raw text before looking at them.
- All 96 Caring Village store reviews were read by me in full from the raw files, not from the earlier tables.

## Check 1. Quote and source check

Scripts: Appendix (A, B, C). Run from `/tmp` with `python3 -I`.

| Test | Result | State | Limit |
|---|---|---|---|
| A. 86 quoted phrases in EVIDENCE.md, PASS1, PASS2 against the files named in their rows | 46 confirmed in the cited file. 40 flagged. Most of the 40 are not quotes at all (search words such as "caring village", "eligib", or quoted review titles) or quotes whose row cites no path (I checked those by hand: all are in the raw data). 1 real miss (below). | proven (script output) plus observed (my hand check) | Script checks that words exist in the file, not that the file says what the row claims. |
| B. 29 rows that give a record id plus a quote: is the quote inside that exact record? | 23 ok. 6 reported "RECORD-NOT-FOUND" only because the Google Play rows say "review index N" and my id pattern read "N". I re-checked all 6 by hand against the JSON (index 38, 18, 7, 5, 20, 9). All 6 match. | proven | none |
| C. 23 rows with a file path plus an id: does the id exist in that file? | 23 of 23 ok. | proven | none |
| D. Word limit: any quote cell over 20 words? | 0 found. | proven | none |

Real quote misses

| # | File and line | What is wrong | Fix |
|---|---|---|---|
| Q1 | `feature-analysis-4/caring-village/PASS2-HOWWELL.md` line 80 | Quotes the Ask-A-Nurse page metadata: "Each week we answer a new question from a caregiver in our Ask-A-Nurse video series." That sentence is in no saved file. The saved `caringvillage_com_questions.md` has only the menu and the title. | The sentence is real: I saw it today in the live site map result for https://caringvillage.com/questions ("Do you have questions about caregiving? Each week we answer a new question from a caregiver in our Ask-A-Nurse video series. Ask away!"). Save that page text so the quote can be opened. |

Not a miss but worth knowing: the AARP quotes ("calendar synchronization; checklists for a variety of situations; medical document upload and access"; "secure in-app messaging, shareable to-do lists and other features") are in `PASS2-aarp-top-caregiving-apps.md` (observed by grep).

## Check 2. Recount from raw data

Raw data used: `docs/sources/app-reviews/all-reviews.jsonl` (54 Apple reviews with app = caring-village; 42 Google Play reviews with ids g-caring-village-0 to 41; same 42 sit in `app-reviews/google-play/google-play-reviews-caring-village.json`), `feature-analysis-4/caring-village/PASS2-reddit-comments-threads.jsonl`, and the PASS2 Reddit post file.

### 2a. Totals match the earlier files
- 54 Apple + 42 Google = 96 reviews. Matches PASS1 line 23. (observed: Python count of the file, 54 and 42; google json "count": 42.)
- PASS1 says 25 distinct reviews were counted (F5 23 plus F8 3, with a-1372 in both = 25). I re-added the rows: F5 7 worked, 8 mixed, 8 did not work = 23; F8 3 worked; one id (a-1372) appears twice. Correct. (proven: row-count script)
- Double counting inside Caring Village: none other than a-1372 (two different cells, so fine).

### 2b. My own F5 recount (relatives cover time), all 96 reviews plus the Reddit comments
My rule: a review counts for F5 only if it is about handing tasks or time to relatives, relatives joining, or who-does-what. A bug about calendar sync alone does not count.

| Class | Earlier count (PASS1 + PASS2) | My count | Difference and why |
|---|---|---|---|
| WORKED | 10 (7 + 3 Reddit) | 7 firm (a-1356, a-1372, a-1365, a-1350, a-1355, a-1351, g-38) + 2 borderline I found and they did not (a-1371 "up to the family to play quarterback... a tool that allows us to do that a lot easier"; a-1397 "wouldn't have been able to coordinate care") + 1 weak Reddit (lj4o3n4 "We used Caring Village for a while", no outcome) | 2 earlier Reddit WORKED (nlwi86e, o11fvj3) are probable promo, see 2d. Removed. |
| MIXED | 8 | 9 | a-1381 moved here from DID NOT WORK (a 2-star wish list: "Ok but", about alert routing, not a failure). |
| DID NOT WORK | 8 | 5 (a-1389, a-1364, g-5, a-1367, g-20) | a-1366 and a-1394 are calendar bugs (sync, freeze). Not about tasks or relatives. Removed. g-20 ("Checklist feature didn't work") may be the care-plan checklist, so it is low confidence. a-1381 moved to MIXED. |

Combined, earlier: 10 / 8 / 8 = 26. Mine: 7 (+2 borderline, +1 weak) / 5 / 9 = 21 firm (24 with borderline and weak). Disagreement: 5 reports moved or removed, 2 added as borderline. (observed: all from the raw text.)

### 2c. Other cells recount (keyword scan of all 96 reviews, then reading each hit)
| Cell | Reviews that are really about it | Earlier | Match? |
|---|---|---|---|
| F1 Relief finder | 0 (a-1355 mentions "very lonely", not respite) | 0 | yes |
| F2 Eligibility | 0 (a-1372 "information on proper paperwork" is not eligibility) | 0 | yes |
| F3 Paying for relief | 0 (price complaints are about Caring Village's own plan: a-1364, g-5, a-1386) | 0 | yes |
| F4 Refusing parent | 0 (g-18 "depends on how much info the patient wants to share" is privacy) | 0 | yes |
| F6 Account access | 0 about getting into outside accounts. a-1371 names "patient portals, pharmacies" as a problem the family faces, but does not say the app helps. | 0 | yes |
| F8 Personal guidance | 3 about the AI helper (a-1372, a-1373, g-9). a-1362 says the app holds "advice" (vague). None about a human coach. | 3 | yes (a-1362 optional, vague) |
| F9 Behavior and hard talks | 0 | 0 | yes |
| F10 People who understand | 0 (a-1355 "less alone" is her own family village) | 0 | yes |

### 2d. Promo, vendor and bait check on the Reddit reports (PASS2 lines 36 to 38)
Source: `PASS2-reddit-comments-threads.jsonl`, read in full.
- nlwi86e (thread 1ohiafw, posted the day after the question): "so what actually worked: the Caring Village app (free, sends reminders so people actually use it)...". Reads like an ad template. It also contains a line that attacks group texts. I treat it as probable promo. Earlier file flagged it but still counted it as WORKED in the totals.
- o11fvj3 (thread 1qjr6ug): the same thread has near-identical duplicated comments (o11ecje = o11ehv9; o12oqry = o12pc8x) that push "caregiver apps". Pattern of a promo campaign. Flagged earlier, still counted.
- lj4o3n4: a plain reply, no outcome. Keep as weak.
- Result: independent new Reddit reports = 1 weak, not 3. (inferred from text pattern; the usernames are not saved, so this cannot be proven.)

### 2e. Random sample of 15 counted reports, labels hidden (seed 20261106, Script D)
Counted entries in the earlier files = 29. I classified the raw text first.

| # | Id | Cell | My class | Earlier class | Agree? |
|---|---|---|---|---|---|
| 1 | a-1367 | F5 | DID NOT WORK | DID NOT WORK | yes |
| 2 | a-1372 | F5 | WORKED (feature praise, no outcome) | WORKED | yes |
| 3 | a-1365 | F5 | WORKED (weak) | WORKED | yes |
| 4 | a-1350 | F5 | WORKED (weak) | WORKED | yes |
| 5 | a-1387 | F5 | MIXED | MIXED | yes |
| 6 | a-1356 | F5 | WORKED | WORKED | yes |
| 7 | a-1366 | F5 | not about F5 (calendar connection) | DID NOT WORK | NO |
| 8 | a-1374 | F5 | MIXED | MIXED | yes |
| 9 | g-caring-village-7 | F5 | MIXED | MIXED | yes |
| 10 | a-1390 | F5 | MIXED | MIXED | yes |
| 11 | a-1372 | F8 | WORKED, AI helper only | WORKED | yes |
| 12 | g-caring-village-5 | F5 | DID NOT WORK (member cap and bugs) | DID NOT WORK | yes |
| 13 | a-1351 | F5 | WORKED | WORKED | yes |
| 14 | g-caring-village-38 | F5 | WORKED | WORKED | yes |
| 15 | g-caring-village-9 | F8 | WORKED, AI helper only | WORKED | yes |

14 of 15 agree (93%). The one disagreement is the same off-topic calendar bug found in 2b.

## Check 3. Try to disprove

robots.txt for caringvillage.com read first: `https://caringvillage.com/robots.txt` blocks only /calendar and /events action pages. Pages I fetched are allowed. Trustpilot skipped. aplaceformom.com not touched.

| Cell | Earlier said | What I searched | What I found | Effect |
|---|---|---|---|---|
| F1 | YES | Re-read saved `caringvillage_com_homecare.md`; live site map shows `/homecare` still exists | The page is a Care.com zip-code search and lists "Respite Care Providers" as a category. The saved text never says "free" and shows no search results. It covers in-home help only; no adult day centers. The dementia blog also points to the Eldercare Locator for respite and adult day (saved blog, line 260). | Downgrade YES to LIMITED. |
| F2 | VERIFY then inferred NO | Firecrawl search restricted to caringvillage.com for eligibility, benefits; site map search "community support group eligibility benefits coach" | Only articles: "How to Get Paid as a Family Caregiver", "Veteran Health Benefit Qualifications Explained", "Veterans Affairs Caregiver Support", "How to Find Caregiver Resources". No checker, no apply tool. | NO as a tool. Articles exist. |
| F3 | YES | Re-read blog | The blog has a section "The Home Care Cost Estimator" and "What Medicare & Medicaid Cover". It prices in-home care in general, not respite, and lives on the web, not in the app. | LIMITED, not YES. |
| F4 | VERIFY then inferred NO | Fetched `blog/caregiver-wellness/accepting-help` (live) | It is advice for the caregiver on asking for and accepting help. Nothing on a parent who says no. | NO confirmed. |
| F5 | YES | Live FAQ and saved app page | Free plan = 1 village, up to 2 members. Circle $14.99 a month (5 members). Village $24.99 a month (50 members). "Invited members join for free" but the cap is total members per village. EVIDENCE.md leaves this out. Nine reviews describe relatives who could not join or could not see tasks. | LIMITED, not YES. |
| F6 | VERIFY then inferred NO | grep of product, app and FAQ pages for password, login, bank | "Each person has their own login" and "bank-level encryption" are about Caring Village itself. Documents section stores "Medical, legal and financial folders". Nothing connects to outside accounts. | NO confirmed. |
| F8 | VERIFY then split | Fetched app page and FAQ | "Meet Julia, Your AI Virtual Caregiver" (24/7 answers). Weekly Ask-A-Nurse video series (live metadata). No one-to-one coach. Page does not say which plan includes Julia. | LIMITED (AI helper and weekly videos). |
| F9 | behavior YES; hard talks VERIFY | grep of the dementia blog for talk, conversation, driving, living alone | Behavior: stage guides cover refusing a bath or pills, evening agitation, wandering. Hard talks: one line "Both are conversations to open with the doctor" and a section on whether someone can live alone. Not a talk guide. | LIMITED. |
| F10 | VERIFY then inferred NO | Fetched `blog/family-caregiving/caregiver-resources-near-you` (live) | The blog links out to Family Caregiver Alliance's online support group and the NAC directory. No community inside the product. | NO in the product; link-out only. |

Searches that found nothing for a YES-to-NO flip: none of the Caring Village cells marked NO had an in-product tool turn up. Searches that tried to find "does not work" for each YES: only F5 and F1 had real limits (above).

## Corrections list (every error found in earlier files)

| # | File and line | Problem | Severity |
|---|---|---|---|
| 1 | `caring-village/EVIDENCE.md` line 11 (F5) | Says YES. Omits that the Free plan allows only 2 members, so a family with 3 or more relatives must pay (app page lines 458 to 460 and 530; live FAQ). Should be LIMITED. | High |
| 2 | `caring-village/EVIDENCE.md` line 7 (F1) | Says YES and calls the search "free". The saved homecare page never says free and saved no results. Care.com helps hire in-home caregivers. Should be LIMITED. | Medium |
| 3 | `caring-village/EVIDENCE.md` line 9 (F3) | Says YES. It is a web article about in-home care costs, not respite costs and not in the app. LIMITED. | Medium |
| 4 | `caring-village/PASS1-HOWWELL.md` lines 50 and 53 (F5 #20 a-1366, #23 a-1394) | Counted as F5 DID NOT WORK but they are calendar sync and freeze bugs. | Low |
| 5 | `caring-village/PASS1-HOWWELL.md` line 46 (F5 #16 a-1381) | Class DID NOT WORK; text is a mixed wish list. MIXED. | Low |
| 6 | `caring-village/PASS1-HOWWELL.md` line 52 (g-20) | "Checklist feature" may be the care-plan checklist, not tasks for relatives. Low confidence. | Low |
| 7 | `caring-village/PASS1-HOWWELL.md` lines 31 to 53 | Missed borderline F5 reports a-1371 and a-1397. | Low |
| 8 | `caring-village/PASS2-HOWWELL.md` lines 36 to 38 and line 22 | Two probable-promo Reddit comments are in the WORKED total (10). Remove them from totals. | Medium |
| 9 | `caring-village/PASS2-HOWWELL.md` line 80 | Quote not in any saved file (Q1). | Low |
| 10 | `caring-village/PASS2-HOWWELL.md` lines 18 to 26 vs EVIDENCE.md | PASS2 turns VERIFY into "NO (settled, inferred)". The product page has no mention of the words, but a product page is not a full feature list. State stays inferred. Fine, but F9 hard talks and F10 should say "link-out" and "articles exist". | Low |
| 11 | Figma table (`figma-competitive-tables-2026-11-06.md`) | Need 5 says "relatives join free with their own login". True only up to the Free cap of 2 members. | Medium (Figma, not helper) |

## Final verdict per cell

Counts are independent family reports (store reviews, one per reviewer, and Reddit comments). "Docs" = documented evaluations.

| Cell | Verdict | Confidence | Reports worked / did not / mixed | Documented evaluations | Why, in one sentence |
|---|---|---|---|---|---|
| F1 Relief finder | LIMITED (link-out to Care.com for in-home caregivers; no adult day; untested) | medium | 0 / 0 / 0 | none (company page only) | The site sends you to a Care.com zip-code search for in-home help, and no one has reported using it. |
| F2 Eligibility and applications | NO as a tool (articles only) | medium | 0 / 0 / 0 | none | It explains VA and state program rules in blog posts but has no checker or apply step. |
| F3 Paying for relief | LIMITED (web article with a cost estimator) | medium | 0 / 0 / 0 | none | A blog guide shows hourly in-home care prices and what Medicare, Medicaid and VA cover, but not respite prices and not inside the app. |
| F4 Refusing parent support | NO | medium | 0 / 0 / 0 | none | Nothing in the app or help center helps a parent who says no. |
| F5 Relatives cover time | LIMITED (shows who owns each task; free plan only 2 members; cannot make people act; invite and access trouble) | high that it exists, medium on how well it works | 7 (+2 borderline, +1 weak Reddit) / 5 / 9 | AARP 2019 (relays company claims); category studies (Linden 2022, Breebaart 2018, Kokorelias 2022) not about this app | Tasks get a named owner and relatives can claim them, but 9 reviewers say relatives could not join or see things, and the free plan stops at 2 people. |
| F6 Account access | NO (stores papers only) | medium | 0 / 0 / 0 | none | It keeps documents and IDs but has no tool to get into a parent's bank, insurer or portal logins. |
| F8 Personal guidance | LIMITED (AI helper "Julia" plus weekly Ask-A-Nurse videos; no one-to-one human) | medium | 3 / 0 / 0 (all about the AI helper) | AARP 2019 (said AI "coming soon") | Reviewers like the AI helper, but no coach or personal expert is offered. |
| F9 Behavior and hard talks | LIMITED (behavior articles; no hard-talk guide) | medium | 0 / 0 / 0 | none | The dementia guide covers refusing a bath, evening agitation and wandering, but not how to start hard family talks. |
| F10 People who understand | NO in the product (blog links out to outside groups) | medium | 0 / 0 / 0 | none | The village is your own family and care team, and the blog only points to Family Caregiver Alliance and a directory. |

### Where I disagree with earlier helpers
- F1: earlier YES, me LIMITED. F3: earlier YES, me LIMITED. F5: earlier YES, me LIMITED (EVIDENCE.md line 11 only; the earlier file itself said the owner "may keep Partly").
- F2, F4, F6, F8, F10: earlier VERIFY, later inferred NO. I agree with NO for F2, F4, F6, F10 and LIMITED for F8 (AI helper exists).
- F9: earlier "behavior YES, hard talks VERIFY". I say LIMITED for the whole cell.

### Where the evidence differs from the Figma table (`figma-competitive-tables-2026-11-06.md`)
- Figma F3 "no money help": there is a cost-estimator article (LIMITED).
- Figma F9 "no help with dementia behavior": the blog has it (LIMITED, web only).
- Figma F5 "relatives join free": only up to 2 members on Free.
- Figma F1 (real relief Partly): the Care.com link is the only relief-finding path; I rate LIMITED.
- Figma F4, F6, F10: agree (No).

## Not checked
- Using the app or Julia (no account, so no login-gated features were seen).
- Whether the Free plan includes Julia and Ask-A-Nurse.
- The Care.com search results themselves (the form needs a zip code; results are not saved).
- Google Play reviews beyond the 42 saved; Apple reviews beyond the 54 saved (the Apple page shows about 36 ratings; I did not verify that number).
- Whether the two flagged Reddit comments are real users (usernames not saved).
- Any PASS2 claim about sites I skipped for robots reasons (healthify, usnews, caring.com).
- The `PASS2-caringvillage-com-blog-11-best-caregiver-apps-VENDOR.md` file (vendor listicle, not used by me).

## Appendix: scripts (re-runnable)

#### Script A: quotecheck.py (every quoted phrase in a table row, checked against the files named in that row)
```python
import re,sys,json,os
ROOT="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator"
SRC=ROOT+"/docs/sources"
slug=sys.argv[1]
FA=SRC+"/feature-analysis-4/"+slug
def norm(s):
    s=s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"').replace("—","-").replace("–","-").replace(" "," ").replace("\x00","")
    s=re.sub(r"[*_`]","",s)
    s=re.sub(r"\s+"," ",s).strip().lower()
    return s
cache={}
def load(path):
    if path in cache: return cache[path]
    if not os.path.exists(path): cache[path]=None; return None
    t=open(path,errors="replace").read()
    if path.endswith(".jsonl"):
        parts=[]
        for l in t.splitlines():
            try:
                d=json.loads(l); parts.append(json.dumps(d,ensure_ascii=False)); parts.append(" ".join(str(v) for v in d.values()))
            except Exception: parts.append(l)
        t="\n".join(parts)
    elif path.endswith(".json"):
        try:
            d=json.load(open(path)); t=json.dumps(d,ensure_ascii=False)+" "+" ".join(str(r) for r in (d.get("reviews",[]) if isinstance(d,dict) else []))
        except Exception: pass
    cache[path]=norm(t); return cache[path]
def resolve(p):
    cands=[SRC+"/"+p, ROOT+"/"+p, FA+"/"+p, FA+"/"+os.path.basename(p)]
    for c in cands:
        if os.path.exists(c): return c
    return None
qre=re.compile(r'"([^"]{6,})"|“([^”]{6,})”')
pre=re.compile(r'([A-Za-z0-9_./\-]+\.(?:md|jsonl|json|txt))')
tot=0;miss=[]
for fn in ["EVIDENCE.md","PASS1-HOWWELL.md","PASS2-HOWWELL.md"]:
    path=FA+"/"+fn
    if not os.path.exists(path): continue
    for ln,line in enumerate(open(path).read().splitlines(),1):
        if not line.startswith("|") and '"' not in line: continue
        qs=[a or b for a,b in qre.findall(line)]
        if not qs: continue
        paths=[p for p in pre.findall(line)]
        files=[resolve(p) for p in paths if resolve(p)]
        for q in qs:
            tot+=1
            nq=norm(q)
            # split on ellipsis
            segs=[s.strip() for s in re.split(r"\.\.\.|…",nq) if len(s.strip())>5]
            found_in=None
            for f in files:
                t=load(f)
                if t and all(s in t for s in segs): found_in=f;break
            anywhere=None
            if not found_in:
                for f2 in os.listdir(FA):
                    pp=FA+"/"+f2
                    if os.path.isfile(pp):
                        t=load(pp)
                        if t and all(s in t for s in segs): anywhere=f2;break
            status="OK-cited" if found_in else ("FOUND-ELSEWHERE:"+str(anywhere) if anywhere else "MISS")
            if status!="OK-cited": miss.append((fn,ln,status,q[:110],[os.path.basename(x) for x in files][:3] or paths[:3]))
print("quotes checked:",tot,"not confirmed in cited file:",len(miss))
for m in miss: print(m)
```

#### Script B: strictcheck.py (the quote must be inside the exact record named by the row id)
```python
import re,sys,json,os,glob
ROOT="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources"
slug=sys.argv[1]
FA=ROOT+"/feature-analysis-4/"+slug
def norm(s):
    s=s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"').replace("—","-").replace("–","-").replace(" "," ").replace("\x00","")
    s=re.sub(r"&amp;","&",s); s=re.sub(r"&#x200B;","",s)
    return re.sub(r"\s+"," ",s).strip().lower()
idx={}
files=[ROOT+"/reddit/arctic-shift-2026-11-03/posts.jsonl",ROOT+"/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl",ROOT+"/app-reviews/all-reviews.jsonl",ROOT+"/app-reviews/all-reviews3.jsonl"]+glob.glob(ROOT+"/feature-analysis-4/*/*.jsonl")
for f in files:
    for l in open(f):
        try: d=json.loads(l)
        except: continue
        k=d.get("key") or d.get("id")
        if not k: continue
        t=" ".join(str(v) for v in d.values())
        idx.setdefault(str(k),[]).append((os.path.basename(f),norm(t)))
# thread txt files
for f in glob.glob(ROOT+"/competitive-analysis-3/grid/reddit-threads/*.txt"):
    t=open(f).read()
    for m in re.finditer(r"\[comment (\w+)\](.*?)(?=\n- \[comment|\Z)",t,re.S):
        idx.setdefault(m.group(1),[]).append((os.path.basename(f),norm(m.group(2))))
    idx.setdefault("THREAD:"+os.path.basename(f),[]).append((os.path.basename(f),norm(t)))
qre=re.compile(r'"([^"]{6,})"|“([^”]{6,})”')
idre=re.compile(r'\((?:key|id|comment|review index)\s+([A-Za-z0-9_-]+)')
tot=ok=0;bad=[]
for fn in ["PASS1-HOWWELL.md","PASS2-HOWWELL.md"]:
    for ln,line in enumerate(open(FA+"/"+fn).read().splitlines(),1):
        if not line.startswith("|"): continue
        m=idre.search(line)
        if not m: continue
        rid=m.group(1)
        qs=[a or b for a,b in qre.findall(line)]
        if not qs: continue
        q=qs[0]; tot+=1
        segs=[s.strip() for s in re.split(r"\.\.\.|…",norm(q)) if len(s.strip())>5]
        recs=idx.get(rid,[])
        if not recs: bad.append((fn,ln,rid,"RECORD-NOT-FOUND",q[:80])); continue
        if any(all(s in t for s in segs) for _,t in recs): ok+=1
        else: bad.append((fn,ln,rid,"QUOTE-NOT-IN-RECORD",q[:90],[f for f,_ in recs]))
print("rows with id+quote:",tot,"ok:",ok,"problems:",len(bad))
for b in bad: print(b)
```

#### Script C: pathcheck.py (the id must exist inside the file path the row cites)
```python
import re,sys,json,os
ROOT="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator"
slug=sys.argv[1]; FA=ROOT+"/docs/sources/feature-analysis-4/"+slug
idre=re.compile(r'\((?:key|id|comment)\s+([A-Za-z0-9_-]+)')
pre=re.compile(r'(docs/sources/[A-Za-z0-9_./\-]+\.(?:jsonl|txt|json))')
cache={}
def txt(p):
    if p not in cache: cache[p]=open(p,errors="replace").read() if os.path.exists(p) else None
    return cache[p]
n=0;bad=[]
for fn in ["PASS1-HOWWELL.md","PASS2-HOWWELL.md"]:
    for ln,line in enumerate(open(FA+"/"+fn).read().splitlines(),1):
        if not line.startswith("|"): continue
        m=idre.search(line); p=pre.search(line)
        if not (m and p): continue
        n+=1; path=ROOT+"/"+p.group(1); t=txt(path)
        if t is None: bad.append((fn,ln,"FILE-MISSING",p.group(1))); continue
        rid=m.group(1)
        if rid not in t: bad.append((fn,ln,"ID-NOT-IN-CITED-FILE",rid,p.group(1)))
print(slug,"rows with path+id:",n,"problems:",len(bad))
for b in bad: print(b)
```

#### Script D: sample.py (seeded random pick of counted reports, labels hidden)
```python
import re,sys,json,os,random,glob
ROOT="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources"
slug=sys.argv[1]; seed=int(sys.argv[2]); N=int(sys.argv[3])
FA=ROOT+"/feature-analysis-4/"+slug
idre=re.compile(r'\((?:key|id|comment)\s+([A-Za-z0-9_-]+)')
qre=re.compile(r'"([^"]{6,})"|“([^”]{6,})”')
cellre=re.compile(r'^#### (F\d+)')
entries=[]
for fn in ["PASS1-HOWWELL.md","PASS2-HOWWELL.md"]:
    cell=None
    for ln,line in enumerate(open(FA+"/"+fn).read().splitlines(),1):
        m=cellre.match(line)
        if m: cell=m.group(1); continue
        if line.startswith("| ") and re.match(r"\| \d+ \|",line):
            cols=[c.strip() for c in line.strip("|").split("|")]
            q=qre.search(line); i=idre.search(line)
            gi=re.search(r'g-caring-village-(\d+)|review index (\d+)',line)
            entries.append(dict(file=fn,ln=ln,cell=cell,cls=cols[1],id=(i.group(1) if i else (("g-caring-village-"+(gi.group(1) or gi.group(2))) if gi else None)),quote=(q.group(1) or q.group(2)) if q else None))
print("counted entries:",len(entries))
random.seed(seed); pick=random.sample(entries,min(N,len(entries)))
json.dump(pick,open(os.environ.get("OUT","/tmp/pick.json"),"w"))
idx={}
for f in [ROOT+"/reddit/arctic-shift-2026-11-03/posts.jsonl",ROOT+"/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl",ROOT+"/app-reviews/all-reviews.jsonl",ROOT+"/app-reviews/all-reviews3.jsonl"]+glob.glob(ROOT+"/feature-analysis-4/*/*.jsonl"):
    for l in open(f):
        try:d=json.loads(l)
        except: continue
        k=d.get("key") or d.get("id")
        if k: idx.setdefault(str(k),str(d.get("text") or d))
for f in glob.glob(ROOT+"/competitive-analysis-3/grid/reddit-threads/*.txt"):
    t=open(f).read()
    for m in re.finditer(r"\[comment (\w+)\](.*?)(?=\n- \[comment|\Z)",t,re.S): idx.setdefault(m.group(1),m.group(2))
for n,e in enumerate(pick,1):
    txt=idx.get(e['id'] or "","(not found)")
    q=e['quote'] or ""
    pos=txt.find(q[:30]); s=max(0,pos-500) if pos>=0 else 0
    print(f"--- SAMPLE {n} | {e['file']}:{e['ln']} {e['cell']} id={e['id']} (label hidden)")
    print(txt[s:s+1100].replace("\n"," "));print()
```

