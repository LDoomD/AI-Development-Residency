# PASS 3 audit: Everplans (independent check)

Date: 2026-11-06. Branch feature-analysis-4. Nothing committed. I did not do the earlier work. I tried to prove it wrong.
Repo root: `/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator` (note the space before the slash). Paths below start at `docs/sources/`.

State key (skeptical-audit): proven / observed / inferred / documented / reported / not-assessed.

## How blind was I (honest limit)
- I read EVIDENCE.md and the PASS files first, so my recount is "re-derived from raw data", not strictly blind.
- Strictly blind part: the random-sample step (check 2c). There are only 7 counted reports, so I read all 7 with labels hidden.
- I read every raw Everplans mention myself: 5 comments in `everplans/PASS2-reddit-comments-threads.jsonl`, 7 mentions in the 5 saved threads in `competitive-analysis-3/grid/reddit-threads/everplans_*.txt`, 5 posts in `search_everplans.json`, and the 8 Apple reviews (`app-reviews/all-reviews3.jsonl`, ids c-0 to c-7; `all-reviews4.jsonl` repeats them as d-0 to d-7).

## Check 1. Quote and source check

Scripts: Appendix A, B, C (run from `/tmp` with `python3 -I`).

| Test | Result | State | Limit |
|---|---|---|---|
| A. 70 quoted phrases in EVIDENCE.md, PASS1, PASS2 against the files named in their rows | 32 confirmed in the cited file; 38 flagged. Most of the 38 are search words ("everplan", "deputy", "leans NO"). The rest are real quotes whose row cites no path or a wrong path (2 real misses, Q1 and Q2 below). I checked the others by hand: "My step mom's attorney uses an online portal ... Everplans" (everplans_s6gxn7.txt line 523), "My folks use everplans." (everplans_y4q1tc.txt line 635), "I need to get organized. Thank you" (c-7), "has been around" (comment onpdg9r), "definitely" (search_everplans.json) all exist. | proven plus observed | Script proves words exist in a file. |
| B. 12 rows with an id plus a quote: is the quote inside that exact record? | 12 of 12 ok | proven | none |
| C. 12 rows with a path plus an id: is the id inside that file? | 11 ok, 1 fail (Q1) | proven | none |
| D. Any quote cell over 20 words | 0 | proven | none |

Real quote and source misses

| # | File and line | What is wrong | Fix |
|---|---|---|---|
| Q1 | `everplans/PASS1-HOWWELL.md` line 43 | Cites `reddit/arctic-shift-2026-11-03/posts.jsonl` for key p1xdkg46. That key is not in posts.jsonl. It is in `posts_targeted.jsonl`. The quote itself is real ("Her password book I got her is a jumbled, scribbled out mess"). The same wrong path is in `group-texts-notebooks/PASS1-HOWWELL.md` line 92. | Change the path. |
| Q2 | `everplans/PASS2-HOWWELL.md` line 49 | Quotes a CNBC Select snippet ("includes a digital storage vault through Everplans"). It is in no saved file. The row says "not saved", so this is disclosed, but the claim cannot be opened. | Save the page or drop the claim. |
| Q3 | `everplans/EVIDENCE.md` line 24 | Says the help center has a page for "an Everplans subscription received through a partner". No saved file holds that page. It is real: I fetched it today (https://help.everplans.com/hc/en-us/articles/115013055908-...). It says Everplans has "special partnerships with insurance companies, employers, and financial advisors". | Save the page. |

## Check 2. Recount from raw data

### 2a. F6 (account access): the only cell with counted reports
Earlier: 7 reports, all WORKED (PASS1 4 + PASS2 3). My reading of each raw text:

| Id | What the writer actually says | Is this a user of the feature? | My class | Earlier |
|---|---|---|---|---|
| isfovjd (Reddit, y4q1tc) | "My parents use Everplans and are quite happy with it. I have a profile/login so that when something happens to them I can access all of their financial information..." | Yes, adult child with a deputy login; parents still alive | WORKED (set up only, never used) | WORKED |
| c-2 (App Store, 2025-04-24) | "After my dad passed away, we discovered a wealth of notes he had left for us..." | Yes, an heir. Notes, not logins | WORKED (best evidence; notes not account access) | WORKED |
| c-1 (App Store, 2026-02-24) | Long 5-star review from the account owner: "I absolutely feel secure in knowing that everything will be readily available". It also pitches Nolo's Quicken WillMaker bundle. | Owner planning for self | WORKED (owner satisfaction; reads like affiliate copy; low weight) | WORKED |
| grwtwfu (Reddit, mb0o23) | "We use everplans... if both you and your husband go another chosen family member can access it" | Yes, a planner | WORKED (setup only) | WORKED |
| hwruhay (Reddit, sr80o8) | "Everplans does exactly this for you. They have a bunch of articles... which I found valuable even if you don't use their service." | No. Praises articles | EXCLUDE | WORKED |
| grwhh4b (Reddit, mb0o23) | "look into Everplans. It was made exactly for this. Super simple interface and very thorough." | No. A recommendation with no stated use | EXCLUDE | WORKED |
| grxzn1n (Reddit, mb0o23) | "Combining a password manager with something like Everplan is a huge bonus." | No. Advice | EXCLUDE | WORKED |

- My count: 4 users (isfovjd, c-2, c-1, grwtwfu), all positive, none describing a deputy getting into an account. 0 did not work, 0 mixed. Earlier "7 / 0 / 0" overstates by 3.
- For the cell's real question ("get into a parent's accounts when the parent cannot set it up"): 0 reports either way.
- Raw mention scan: I read all 25 Everplans mentions (5 + 7 + 5 + 8). None is about F1, F2, F3, F4, F5, F8, F9 or F10 as something Everplans did or did not do. Match with earlier: 0 for those cells. (observed)
- Other Everplans mentions not counted, and I agree: ishktln "My folks use everplans." (name only), grwur87 and the "going to check out" posts (intent), onpdg9r (plan to use), lel5klc (describes the product), lergxsb (pasted company FAQ), onorkbp (view on vaults). I would also leave out the iPad complaints c-0, c-3, c-4, c-5, c-6.
- Double counting: none (7 different ids). Same App Store review is saved twice (c-x and d-x); counted once. (proven: id check)
- Vendor / promo: c-1 possible affiliate tone. Post 3e3log (discount code) rightly excluded. The Evaheld comparison page is a competitor page and was rightly not counted.

### 2b. Raw counts of sources
- PASS2 line 74: threads 1i56ze6 (2) + 1tmpm3i (6) + 1r7scv7 (8) + mb0o23 (719) = 735 comments. I counted 735 rows in the jsonl. (proven)
- "5 comments mention Everplans or 'ever plans'": I found exactly 5 (onpdg9r, grwhh4b, grwtwfu, grwur87, grxzn1n). (proven: regex over the 735 rows)
- 3 counted + 2 intent only is wrong: 1 user (grwtwfu) + 2 recommendations + 2 intent/plan. See 2a.

### 2c. Random sample, labels hidden (seed 7, Script D)
Counted entries = 7, so the sample is all 7. I classified raw text before comparing.

| Id | My class (raw text only) | Earlier | Agree? |
|---|---|---|---|
| c-1 | owner satisfaction, low weight | WORKED | partly |
| c-2 | WORKED (notes) | WORKED | yes |
| hwruhay | not a user, exclude | WORKED | NO |
| isfovjd | WORKED (set up) | WORKED | yes |
| grwtwfu | WORKED (set up) | WORKED | yes |
| grwhh4b | not a user, exclude | WORKED | NO |
| grxzn1n | not a user, exclude | WORKED | NO |

4 of 7 agree (57%); 3 disagree. This is the weakest evidence base of my three companies.

## Check 3. Try to disprove

robots.txt: `https://www.everplans.com/robots.txt` returns 404 (no rules). help.everplans.com pages came back status 200. Trustpilot skipped. aplaceformom.com not touched.

| Cell | Earlier | What I searched | What I found | Effect |
|---|---|---|---|---|
| F1 Relief finder | inferred NO | Site map search "caregiver respite caring aging parent eligibility" and "medicaid long-term care assisted living cost caregiver support group" on everplans.com; search limited to everplans.com and help.everplans.com | The site map returned only death-certificate, pet, funeral and help-center pages. One assisted-living question checklist article was already saved. No respite or day-care finder. | NO holds (search found nothing; the site-search index is partial). |
| F2 Eligibility and applications | inferred NO | same | One article (All You Need To Know About Advance Directives) says an agent may have "the right to apply for Medicare, Medicaid, or other programs" on your behalf. That is a legal-papers fact, not a checker. | NO holds. |
| F3 Paying for relief | inferred NO | same plus saved pricing page | Everplans' own prices (Free: 3 items; Premium $99.99 a year). Premium bank import (Plaid) pulls account name, type and number of the owner's own accounts, no balances. | NO holds. |
| F4 Refusing parent | documented NO | help page "Why don't I see any information" (saved) and two article hits below | The tool needs the owner to fill it in. Two articles about talking with parents (see F9). They do not help with a parent who refuses help. | NO holds. |
| F5 Relatives cover time | NO | Re-read "Can other people edit my Everplan" | The page says: "Under certain circumstances, you can invite other people to collaborate with you to help you create your Everplan. Currently, if your Everplan was provided to you by your Financial Advisor or another professional, you can grant them access to make changes." EVIDENCE.md turned this into "Only a financial advisor or professional partner can be given edit rights". The word "only" is not on the page. Still no task assigning or tracking anywhere. | NO holds, but the stated reason is an over-reading. |
| F6 | LIMITED | Fetched 3 more help pages today | Deputy sharing needs Premium. Items can be shared now or locked until after death. After-death unlock: deputy reports the death on the web only, then a wait of 3 hours to 30 days that the owner can set and use to block it. Item-level permissions since August 2023. Nothing about unlocking when a parent is alive but cannot act (for example dementia). | LIMITED confirmed. New limit: death only, not incapacity. |
| F8 | NO | Saved pricing page footer | "the employees of Everplans are not acting as your healthcare providers, medical professionals, attorneys, or financial advisors." "Expert guidance" is a step-by-step screen. | NO holds. |
| F9 hard talks | VERIFY then inferred NO | Search "everplans.com how to talk to your parents about end of life planning conversation" | FOUND: `https://www.everplans.com/articles/talking-with-your-parents-about-estate-planning` (a short summary of a New York Times piece; says "These are difficult conversations to have"; lists power of attorney, health care proxy, will, passwords) and `https://www.everplans.com/articles/5-important-bits-of-information-to-gather-from-your-parents-before-you-lose-them` (guidelines for a "pleasant conversation, and not a police interrogation", plus a link to a podcast "about Having Uncomfortable Conversations"). A third, "Guide: Online End-Of-Life Resources", points to The Conversation Project. | The earlier "I did not find a guide on talking with a parent" is wrong. F9 hard talks becomes LIMITED (thin articles about estate and end-of-life talks; no dementia behavior help). |
| F9 behavior | inferred NO | same searches | Nothing on dementia behavior. | NO holds. |
| F10 People | inferred NO | same searches | No community feature. "Grief Support & Loss" articles only. | NO holds. |
| Every YES/LIMITED | n/a | Looked for "does not work" | No independent report of a failed unlock. Terms.law (attorney, saved) grades the terms C and says the deputy system "works well". Limits stand: Premium needed, parent must set up. | n/a |

## Corrections list (every error found in earlier files)

| # | File and line | Problem | Severity |
|---|---|---|---|
| 1 | `everplans/EVIDENCE.md` line 16 (F9 hard-talk) | Says no guide on talking with a parent was found. Two such articles and a podcast link exist (check 3). Also the quote in that row ("individuals you are a deputy for might not have entered any information") does not support a claim about talks. | High |
| 2 | `everplans/PASS2-HOWWELL.md` lines 26 and 109 | Repeats "NO (settled, inferred)" for F9 hard talks. Wrong, see above. | High |
| 3 | `everplans/PASS1-HOWWELL.md` line 33 (hwruhay) and `PASS2-HOWWELL.md` lines 38 and 39 (grxzn1n, grwhh4b) | Counted as F6 WORKED, but the writers are not users of the feature (article praise or recommendation). Real user reports = 4, not 7. Headlines in PASS2 lines 11 and 24 and the Combined column are wrong. | High |
| 4 | `everplans/PASS1-HOWWELL.md` line 43 | Wrong file path (Q1). | Low |
| 5 | `everplans/PASS1-HOWWELL.md` line 32 (c-1) | Owner review with a bundle pitch counted as F6 WORKED. It is not an access report; possible affiliate tone. | Medium |
| 6 | `everplans/PASS2-HOWWELL.md` line 74 | "3 counted, 2 are intent or a plan only": 1 user, 2 recommendations, 2 intent. | Medium |
| 7 | `everplans/EVIDENCE.md` line 11 (F5) | "Only a financial advisor or professional partner can be given edit rights": the page does not say "only". | Medium |
| 8 | `everplans/EVIDENCE.md` lines 8, 15, 17 | The quotes cited for F2, F9-behavior and F10 do not prove a missing feature (F10 cites a Trustpilot score line). They prove only what the product says it is. | Low |
| 9 | `everplans/EVIDENCE.md` line 24 and `PASS2-HOWWELL.md` line 49 | Quotes with no saved copy (Q2, Q3). | Low |
| 10 | `everplans/PASS2-HOWWELL.md` line 11 | "Combined with pass 1: 7 F6 reports, all WORKED, ... none from someone who needed access." The cell question is "parent cannot set it up". For that, the evidence is 0 reports, and the documented answer is that Everplans cannot do it. Reword. | Medium |
| 11 | `everplans/EVIDENCE.md` line 13 (F6 if parent filled it in, LIMITED) | Correct, but add: unlock works after death only, not when a parent is alive and unable to act. | Medium |

## Final verdict per cell

Counts = independent reports who actually used the feature (my count).

| Cell | Verdict | Confidence | Reports worked / did not / mixed | Documented evaluations | Why, in one sentence |
|---|---|---|---|---|---|
| F1 Relief finder | NO | medium | 0 / 0 / 0 | SeniorLiving 2025 feature list and FreeWill table: no finder | It is a document vault with no respite or day-care search. |
| F2 Eligibility and applications | NO | medium | 0 / 0 / 0 | same | No program checker or application help. |
| F3 Paying for relief | NO | medium | 0 / 0 / 0 | same | Pricing is for Everplans itself; the bank import only copies the owner's own account details. |
| F4 Refusing parent support | NO | high | 0 / 0 / 0 | Everplans help page (parent must enter the information) | The tool does nothing if the parent will not fill it in. |
| F5 Relatives cover time | NO | medium | 0 / 0 / 0 | Everplans help pages | Deputies can view what you share; nothing assigns or tracks tasks. |
| F6 Account access | LIMITED (Premium $99.99 a year; parent must set it up and name you; unlock only after death, via the web, after a 3 hour to 30 day wait; stores details, no bank login) | high on the limits, low on real-world results | 4 / 0 / 0 (3 setup only, 1 heir found notes) | SeniorLiving 2025 (set-up tested, no real death); terms.law 2026 (terms only); Foong 2025 (n = 657) and Khadka 2026 (800 posts) are category studies | If a parent filled it in before they died, you get what they chose to share; if not, you get nothing. |
| F8 Personal guidance | NO | high | 0 / 0 / 0 | Everplans own disclaimer | Its staff say they are not advisors; "expert guidance" is a step-by-step screen. |
| F9 Behavior and hard talks | LIMITED (hard talks: three thin articles and a podcast link on estate and end-of-life talks; behavior: none) | low to medium | 0 / 0 / 0 | none | It has short articles on talking to parents about money and end of life, and nothing on dementia behavior. |
| F10 People who understand | NO | medium | 0 / 0 / 0 | none | No community or group finder. |

### Where I disagree with earlier helpers
- F9: earlier NO (inferred); me LIMITED (articles found).
- F6 counts: earlier 7 worked; me 4.
- F5: same verdict (NO), different reason.
- EVIDENCE.md F6 splits into NO (parent entered nothing) and LIMITED (parent filled it in). I merge them into one LIMITED cell with the limit named, and keep the NO case as the first limit.

### Where the evidence differs from the Figma table
- Figma "Yes, if the parent fills it in" (F6): I say LIMITED, with three limits Figma lacks: Premium, death only, wait window.
- Figma F9 / need 1 "No: no care or behavior advice": true for behavior; the hard-talk articles are a small exception.
- Figma "The parent pays": partly true; advisors, insurers and employers can hand out Everplans (help page, saved today), so some users pay nothing.

## Not checked
- A real deputy unlock after a death or a login-gated Everplans account (no account).
- What a deputy sees for passwords and bank logins (only the help pages).
- Google Play reviews (the review tool returned "not found"), BBB complaints (blocked), Capterra and G2 (no pages), WSJ (paywall).
- The IBTimes video story and Facebook comments.
- Whether the Reddit commenters are real users.
- The Evaheld, Eternal Vault, IronClad and other competitor pages (marketing).
- The Khadka arXiv paper review status.
- Everplans article set beyond the pages I searched (the site-map search index is partial).

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

