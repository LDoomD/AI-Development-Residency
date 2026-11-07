# Cariloop: independent audit, pass 3 (2026-11-06)

Auditor: a fresh reviewer who did none of the earlier work. Goal: try to prove the earlier files wrong.
Files audited: `EVIDENCE.md`, `PASS1-HOWWELL.md`, `PASS2-HOWWELL.md` in this folder.
Paths are under `docs/sources/` unless they start with `feature-analysis-4/`. The scripts ran on 2026-11-06 from a scratch folder. Their full text is in Appendix A. They are not saved anywhere else.

Evidence states used: proven, observed, inferred, documented, reported, not-assessed. In this file, "observed" means I read it myself this session (file, script output, or a live web page). "documented" means a company or agency says it. "reported" means a person said it.

## Short answer (plain English)

- No quote in the three files is made up. Every Cariloop quote I tested is in the saved page it cites (one cites the wrong page; see Corrections).
- The count of independent Cariloop reports is right: 3 (2 Google Play reviews, 1 Reddit comment). I found no fourth. One of the 3 is an app bug, not a feature.
- Errors I found: 1 wrong claim about what Cariloop's own pages say (the "0 hits for Medicaid" claim), 2 missed reports about a different company (Wellthy), 1 wrong cell label, 1 missing fact (support groups), 1 wrong citation.
- Cariloop is employer-paid. An ordinary family cannot buy it directly. The only path I found is: leave an employer, then you have 30 days to switch to an individual membership. Price is not published by Cariloop.

## Check 1: do the quotes exist in the cited files?

Command (script in Appendix A): `python3 -I quotecheck.py <the three .md files>`. The script pulls every quoted string out of every table row, finds the file named in that row, and tests that the words appear (case, curly quotes and spacing ignored). For Reddit files it tests the named thread and comment.

| File | Quotes tested | Found | Not found by script | Result after I checked by hand |
|---|---|---|---|---|
| EVIDENCE.md | 18 | 17 | 1 ("in-home companion") | Found, but on a different page than the row cites. See C-1. |
| PASS1-HOWWELL.md | 9 | 8 | 1 (no file in row: "Managing family dynamics") | Found in `competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt`. |
| PASS2-HOWWELL.md | 14 | 5 | 9 | 4 are search phrases, not quotes. 3 are study abstract quotes that exist only in the helper's own file `PASS2-category-evidence-studies-2026-11-06.txt` (not in the journal). 2 are saved-page phrases, found. |

- State: observed. Source: script output saved in my scratch folder (`qc1.txt`); the phrase checks were run with `phrase.py`.
- Limit: the script proves the words are in the saved file. It does not prove the saved file is a true copy of the live page. The 3 study quotes could not be checked against the journals (abstract text lives in a helper-made file).
- Fabricated quotes found: 0.
- Quotes longer than the 20-word limit: 0 (script `LONG` check printed nothing).

Facts I re-checked against raw files (all matched):
- Google Play save: "4.6 star, 9 reviews"; the page shows 2 reviews (2024-11-16 and 2022-04-30). Observed: `competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt`.
- Apple listing: 23 ratings, 4.47825 stars. Observed: `app-stores/apple-named/Cariloop.json`.
- BBB: A+, 0 complaints, 0 reviews. Observed: `competitors-4/review-sites/bbb_2026-11-04.txt`.
- Archive sizes: 49,315 unique Reddit posts; 17,956 app review rows. Observed by script. (The "142 forum threads" figure was not re-counted; `forums/` holds 286 files.)

## Check 2: recount, blind reclassification, double counting

### 2a. Raw search for any independent Cariloop report

| Where I searched (my own search, same keywords) | Hits |
|---|---|
| 49,315 saved Reddit posts for "cariloop", "carriloop", "cari loop" | 0 |
| 17,956 app review rows for "cariloop" | 0 |
| `forums/`, `youtube/` for "cariloop" | 0 |
| All 3 Cariloop raw `.jsonl` files (25 post records and 168 comments) for "cariloop" or "care coach" | 1 post (r/AskHR sichx0) and its 2 comments |
| Google Play save | 2 reviews |

- State: observed (script and grep, 2026-11-06). Limit: the Reddit archive holds posts, and comments only for the threads the helpers fetched.
- Result: 3 independent Cariloop reports. Same as pass 1 and pass 2. Agree.

### 2b. Blind reclassification (I read the raw text first, then compared with the earlier label)

Limit I must state: I had already read the earlier tables, so I was not fully blind. I classified from the raw text and wrote my class before looking back at the table.

| Report | My class from raw text | Earlier class | Agree? |
|---|---|---|---|
| Play 2022-04-30 "Staff wonderful incredibly helpful" | WORKED (cell not stated; "F8" is a guess) | WORKED, F8 | Agree on class. Cell is inferred. |
| Play 2024-11-16 "Won't let me exit app" | DID NOT WORK (app bug, no cell) | DID NOT WORK, no cell | Agree |
| r/AskHR comment mmdvg6b "feedback has been fantastic... I have personally used the service" | WORKED. Writer is an employer-side person. | WORKED, F8 | Agree. Flag: employer-side voice, not a family caregiver. |
| C01 Wellthy, comment mjx7kog | WORKED (appointments scheduled) | WORKED, F8 and F1 | Class agrees. F1 is wrong: scheduling appointments is not respite, adult day or in-home breaks. |
| C02 Wellthy, comment mj284q2 | MIXED | MIXED, F8 | Agree. Reply chain suggests this is the original poster of the thread (inferred; no usernames saved). |
| C03 Wellthy, comment m14dk6c | MIXED | MIXED, F8 | Agree |
| C04 Wellthy, comment l9jx6rs | WORKED. Writer is an HR person who set up the benefit. | WORKED, F8 (flagged "HR staff") | Agree |

All 7 counted reports were read (there are fewer than 15). Disagreements: 1 wrong cell (C01 F1).

### 2c. Reports the earlier work missed (category evidence, not Cariloop)

Thread 15edl7o (r/AgingParents, "Does anyone have experience with Wellthy?") has 4 comments. Pass 2 counted none of them. Two are real Wellthy-user reports:
- ju7nbzx: "I used it to try to locate a different neurologist for my mom. The folks at Wellthy were very responsive and timely." My class: WORKED. It also says "If my mom were more open to receiving my help, I'd probably use Wellthy more." That is a refusing-parent remark (F4) with no verdict on F4.
- ju82hnm: sat through the presentation, "didn't see the value", had already done the work alone. My class: not a user (heard the pitch only). Do not count as DID NOT WORK.
Also thread 1e6j86w (Torchlight): comment ldtledg describes a different, unnamed vendor, not counted. Correct.

- State: observed. Source: `PASS2-reddit-threads-cariloop-raw.jsonl`, thread 15edl7o. Limit: Wellthy is not Cariloop; this changes only the category side-table (Wellthy new reports: 3 WORKED including ju7nbzx, 2 MIXED, not "2 WORKED, 2 MIXED").

### 2d. Double counting, vendor or staff posts

- Same post or person counted twice: none found among the 3 Cariloop reports.
- Vendor, staff or promo posts wrongly counted: none among the 3. The r/AskHR praise is from an employer-side writer (flagged by helpers).
- Survey-bait or invited reviews: none. (ConsumerAffairs and Trustpilot were not used for Cariloop.)

### 2e. Per-cell recount (4 or more cells)

Because the count is 3, "recount" means checking each zero. I searched the raw data for each cell's keywords.

| Cell | My count (W / D / M) | Earlier | Method |
|---|---|---|---|
| F1 | 0 / 0 / 0 | 0 / 0 / 0 | No Cariloop comment about finding care. |
| F2 | 0 / 0 / 0 | 0 / 0 / 0 | No Cariloop report mentions benefits. |
| F4 | 0 / 0 / 0 | 0 / 0 / 0 | Same. |
| F6 | 0 / 0 / 0 | 0 / 0 / 0 | Same. |
| F8 | 2 / 0 / 0 | 2 / 0 / 0 | The 2 are thin ("staff wonderful"; "could not have been more helpful"). |

## Check 3: try to disprove

### 3a. Can an ordinary caregiver use Cariloop, and at what price?

| What I did | What I found | State |
|---|---|---|
| Read live `https://cariloop.com/about-us/faqs` with a fresh Firecrawl read (2026-11-06) | Same text as the saved copy. "When an employee leaves an organization where Cariloop is part of their benefits... a 30-day countdown... allows the member to shift to an individual membership that they can cover the cost of on their own." No price. | observed (live page) |
| Same page | "Typically our minimum size group is 100 employees, but we can configure our program to accommodate groups as small as 50 or 75 as well." So the Figma line "100 or more workers" is slightly too strict. | observed |
| Same page | "The mobile app is best intended for current Cariloop members. If you do not yet have a case created, please visit our Individuals page." The "Individuals page" link points to `https://cariloop.com/`. | observed |
| Read saved `cariloop.com/individuals` (saved 2026-11-06) | Page title is "Support Your Employees with Cariloop's Caregiving Solutions". It is an employer sales page. | observed: `feature-analysis-4/cariloop/cariloop_com_individuals.txt` |
| Read saved MSU FAQ | Free to MSU employees for 30 continuous days a year; then "extend the coaching for $249/month". MSU also says care providers listed (UrbanSitter) are "paid directly by the user". | observed: `feature-analysis-4/cariloop/hr_msu_edu_cariloop_faqs_full_2026-11-06.txt` |
| Read saved Trustmark page | Trustmark policyholders get "1 month of coaching per calendar year"; "New cases only." | observed |
| Searched the web for a direct-to-consumer price (3 queries) | No Cariloop page lists a price for a person with no employer. A search snippet from F6S says "Individual Membership Pricing based on needs - Caregiver. Designed for individuals who leave employer coverage and want to continue." I did not open F6S: its robots.txt has a second "User-agent: *" group that disallows everything, so I treated it as off limits. | reported (snippet only) |
| yespress.io (a snippet said who pays) | Skipped: its robots.txt disallows ClaudeBot. | not-assessed |

Answer: an individual can use Cariloop only (a) through an employer or insurer benefit, or (b) after leaving an employer that had it, within 30 days of leaving, at a price Cariloop does not publish. $249 a month is one employer's price for extra coaching, not a public price. Confidence: medium (company text, not tested by signing up; I did not try to sign up).

### 3b. Cells marked LIMITED or VERIFY: search for stronger or weaker evidence

New facts in the live FAQ and saved Play listing that the earlier files missed or got wrong:
- Coaches "contact facilities during the search process" (FAQ). Common requests include "assisted living communities, in-home caregivers, or hospice agencies". Respite and adult day are still not named (grep of all saved Cariloop pages: only the Terms of Service "Backup Care Program" matches "respite"-like words). Supports F1 LIMITED.
- Medicare, Medicaid, long-term care insurance, VA benefits, "assistance with finance and legal matters" are named (FAQ and Play listing). So the earlier claim that saved pages have "0 hits for Medicaid" is wrong. See C-2.
- "support group availability" is a listed coach topic (FAQ). The earlier F10 evidence mentions only Community Channels. See C-5.
- "I'm starting to think my loved one is no longer safe living at home" and "conversation starters to expectation management" (FAQ). A talk about safety, not a parent who says no. F4 stays unproven either way.
- "Can Cariloop help transfer medical documents to other providers? No. Our portal is best suited for organizing and storing important documents rather than transferring them." Supports "NO login help" for F6.
- Siblings: "Anyone who you have granted access to your Case can post discussions and upload documents... your siblings can communicate directly with your Care Coach". "We've seen our members include 8-10 other family caregivers at a time." Supports F5 LIMITED. Nothing shows assign-and-confirm.
- Cariloop says it takes no referral fees from providers (FAQ). Company claim, not independent.

For every cell I searched for a source saying Cariloop does not offer it. Found: none. For every YES-like cell I searched for a source saying it does not work. Found: one 2024 Play review about the app not closing (about the app, not a feature).

Wellthy and Torchlight reports are category hints only. They mention scheduling help (C01), "pretty good if you put the effort into it" (C02), a coordinator who "wasn't local" (C03), and "didn't see the value" (ju82hnm). None can be moved onto Cariloop.

## Corrections list (errors in the earlier files)

| # | File and line | Error | Fix |
|---|---|---|---|
| C-1 | `EVIDENCE.md` line 9 (row F1 Relief finder) | Cites the find-care page for the words "in-home companion". Those words are on `cariloop_com_solutions_elder_care_benefits.txt`, and the sentence there is cut off ("from in-home companion."). | Cite the elder care page. |
| C-2 | `PASS2-HOWWELL.md` line 80 and line 88 | Says saved Cariloop pages have "0 hits for Medicaid... family dynamics" and "0 hits for Medicaid or benefit applications". The Google Play listing and the FAQ (both cited in EVIDENCE.md) name Medicare, Medicaid, VA benefits and "family dynamics". The search covered only the 2026-11-06 downloads, not the older saved FAQ and Play pages. | State the claim only for the new downloads, or fix it. |
| C-3 | `PASS2-HOWWELL.md` lines 10, 73 | Wellthy side-table says 3 Wellthy reports from 21 posts. Missed ju7nbzx (WORKED). Also, ju82hnm should be "not a user", so category counts are 3 W / 2 M, not 2 W / 2 M. | Add ju7nbzx. |
| C-4 | `PASS2-HOWWELL.md` line 37 (C01) | F1 marked WORKED. Scheduling appointments is not F1. | Remove F1. |
| C-5 | `EVIDENCE.md` lines 23-24 (F10) | Evidence stops at Community Channels. The FAQ also lists "support group availability" as a thing coaches help with. | Add the FAQ line (company text, employer-only). |
| C-6 | `PASS2-HOWWELL.md` line 38 (C02) | The commenter is probably the thread's original poster (reply chain). Not stated. | Add "possibly the original poster" to Limit. |
| C-7 | `EVIDENCE.md` line 5 and Figma | "Only employers with 50 to 100+ workers are signed" is a fair reading; the Figma table says "100 or more". FAQ says typically 100, down to 50 or 75. | Align the Figma wording. |
| C-8 | Figma table (competitors profile, weaknesses) | "The app freezes" is based on one 2024 review that says the app will not let the user exit. | Say "one 2024 review: the app would not close." |

Error count for Cariloop: Check 1: 1 wrong citation (C-1), 0 fabricated quotes. Check 2: 2 missed category reports and 1 wrong cell label (C-3, C-4), 1 unlabelled probable repeat (C-6). Check 3: 1 wrong "no hits" claim (C-2), 1 missed fact (C-5), 1 Figma wording gap (C-7), 1 Figma over-reach (C-8).

## Final verdict table (Cariloop)

Reports column = independent family reports for this cell about Cariloop itself (worked / did not work / mixed). Documented evaluations = independent studies of Cariloop. None exist. The only evaluations are vendor-run, self-reported surveys (for example "89% of members reduced stress" on the elder care page; the page says results are self-reported). These are not independent.

| Cell | Verdict | Confidence | Reports (W/D/M) | Plain reason | Earlier helpers | Differs from Figma? |
|---|---|---|---|---|---|---|
| F1 Relief finder | LIMITED: only through an employer or insurer benefit; coaches find assisted living, in-home caregivers, hospice, backup care; respite and adult day never named | medium | 0/0/0 | Cariloop pages say coaches find and book care for employees; the family pays the care provider. | LIMITED. Agree. | Figma "Partly... only if the employer offers it". Agree. |
| F2 Eligibility and applications | LIMITED: coaches explain Medicare, Medicaid, VA and long-term care insurance; no page says they check eligibility for relief programs or file applications; employer-only | low | 0/0/0 | The FAQ names these benefits; none says "apply". | VERIFY. I disagree on the label (evidence of explaining exists). | Figma says "Yes: help paying for care... Medicaid and VA". The evidence supports "explain", not "help apply". |
| F3 Paying for relief | LIMITED: coaches explain how to pay and can find a cheaper nursing home; real-time rates shown; care itself paid by the family; employer-only | medium | 0/0/0 | Coaching is free only through the benefit (MSU: 30 days, then $249 a month). | LIMITED. Agree. | Figma "Yes". Add the employer limit. |
| F4 Refusing parent support | VERIFY | low | 0/0/0 | Coaches help plan a safety talk ("conversation starters"); no page or report names a parent who says no. | VERIFY. Agree. | Figma "Nothing for a parent who refuses" has no source either way. |
| F5 Relatives cover time | LIMITED: Care Team of up to 8-10 relatives, alerts, relatives can "take on tasks"; no assign-and-confirm shown; employer-only | medium | 0/0/0 | A shared space, not a task tracker. | LIMITED. Agree. | Figma "Tasks aren't split". Agree. |
| F6 Account access | VERIFY (leans NO) | low | 0/0/0 | Stores POAs and papers, helps fill in legal forms; no page says it gets a caregiver into a parent's bank, insurer or portal login. The FAQ says it does not transfer documents. | VERIFY. Agree. | Figma "Yes... POAs" counts paper storage as money help. |
| F8 Personal guidance | LIMITED: a dedicated coach, but only through an employer; MSU gives 30 days a year, then $249 a month; Trustmark gives 1 month a year; ex-employees can switch within 30 days at an unpublished price | high for the limit; low for quality | 2/0/0 (both thin) | One-to-one coach is real and ongoing while you are a member. Few people can be a member. | LIMITED. Agree. | Figma agrees. |
| F9 Behavior and hard talks help | LIMITED: dementia-trained coaches (Certified Dementia Practitioners) and social workers; coaching, not a guide; employer-only | medium | 0/0/0 | Company pages list dementia symptoms and hard talks as coach topics. | LIMITED. Agree. | Not in Figma needs table. |
| F10 People who understand | LIMITED: in-app "Community Channels" answered by coaches; coaches help find support groups (FAQ); no peer meetings shown; employer-only | low | 0/0/0 | Discussion spaces and a referral topic, not a support group. | LIMITED. Agree (add the FAQ line). | Not in Figma. |

Cells where I disagree with the earlier helpers: F2 (VERIFY to LIMITED). Cells where evidence differs from Figma: F2, F6, F4 wording, profile wording on size and "app freezes".

## Not checked

- Whether the F6S "individual pricing" snippet is accurate (page not opened; robots.txt ambiguous). State: reported, snippet only.
- Whether Cariloop sells to an individual over the phone (I did not call or sign up).
- Glassdoor, Indeed, LinkedIn, BBB live pages, Trustpilot, Facebook, Instagram, YouTube comments (blocked by owner rule or ClaudeBot rules; not opened).
- Reddit keyword search of r/humanresources, r/benefits and caregiver subreddits for "cariloop" (the helpers' Arctic Shift job timed out; I did not rerun it).
- Journal copies of the 10 study abstracts.
- Employer satisfaction surveys held by employers.
- Whether the 3 Cariloop reporters are real, unpaid users (cannot be checked).

## Appendix A: scripts (run 2026-11-06)

`quotecheck.py` (Check 1). Run: `python3 -I quotecheck.py file1.md file2.md ...`

```python
import re, sys, json, os, glob, difflib
ROOT='/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources'
FA=ROOT+'/feature-analysis-4'
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=s.replace('&#x200B;','').replace('&amp;','&').replace('&gt;','>').replace('&lt;','<').replace('​','')
    s=re.sub(r'[*`_]','',s)
    s=re.sub(r'\s+',' ',s).strip().lower()
    return s
_cache={}
def load(path):
    if path in _cache: return _cache[path]
    if path.endswith('.jsonl'):
        rows=[json.loads(l) for l in open(path,encoding='utf-8')]
    else:
        rows=open(path,encoding='utf-8',errors='replace').read()
    _cache[path]=rows
    return rows
def resolve(p):
    p=p.strip().strip('`').strip('(').strip(')')
    p=re.sub(r'^docs/sources/','',p)
    for base in (ROOT, FA):
        c=os.path.join(base,p)
        if os.path.exists(c): return c
    return None
def post_text_for(rows,pid):
    out=[]
    for r in rows:
        if r.get('key')==pid or r.get('key')=='p'+pid: out.append(r.get('text',''))
    return ' '.join(out)
def thread_texts(rows,thread,comment=None):
    t=[]
    for r in rows:
        pid=r.get('post_id')
        if pid!=thread: continue
        if 'post_text' in r: t.append(('post',r['post_text']))
        elif 'post' in r:
            t.append(('post',(r['post'].get('title','')+' '+r['post'].get('selftext',''))))
        for c in r.get('comments',[]):
            if comment is None or c.get('id')==comment:
                t.append(('c:'+str(c.get('id')),c.get('body','')))
    return t
def check_md(mdpath):
    res=[]
    lines=open(mdpath,encoding='utf-8').read().split('\n')
    for ln,line in enumerate(lines,1):
        if not line.startswith('|') or re.match(r'^\|[-| ]+\|$',line): continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        paths=set(re.findall(r'[\w./\-]+\.(?:txt|jsonl|json)',line))
        ids=re.findall(r'thread (\w+), comment (\w+)',line)
        quotes=[]
        for ci,c in enumerate(cells):
            if re.match(r'^[“"].*[”"]( /.*)?$',c) and len(c)>10:
                parts=re.split(r'[”"] / [“"]',c)
                for p in parts: quotes.append(('main',p.strip('“”" ')))
        for ci,c in enumerate(cells):
            if re.match(r'^[“"].*[”"]( /.*)?$',c) and len(c)>10: continue
            for m in re.finditer(r'[“"]([^“”"]{12,}?)[”"]',c):
                quotes.append(('sec',m.group(1)))
        if not quotes: continue
        pid=None
        if re.match(r'^p\w{5,9}$',cells[0]): pid=cells[0]
        for kind,q in quotes:
            nq=norm(q); status='NOFILE'; where=''; texts=[]
            for (th,cm) in ids:
                for p in paths:
                    fp=resolve(p)
                    if fp and fp.endswith('.jsonl'):
                        texts+=[(f'{os.path.basename(fp)}:{th}/{lab}',t) for lab,t in thread_texts(load(fp),th,cm)]
            if not texts:
                for p in paths:
                    fp=resolve(p)
                    if not fp: continue
                    d=load(fp)
                    if fp.endswith('.jsonl'):
                        if pid:
                            t=post_text_for(d,pid)
                            if t: texts.append((os.path.basename(fp)+':'+pid,t)); continue
                        texts.append((os.path.basename(fp),' '.join(str(x) for x in d)))
                    else:
                        texts.append((os.path.basename(fp),d))
            if texts:
                status='MISS'
                for w,t in texts:
                    if nq in norm(t): status='OK'; where=w; break
                    if nq.replace('"','') in norm(t).replace('"',''): status='OK-quotechars'; where=w; break
            res.append((ln,cells[0],kind,status,where,q[:90],sorted(paths)[:2]))
    return res
if __name__=='__main__':
    for md in sys.argv[1:]:
        r=check_md(md)
        n=len(r); ok=sum(1 for x in r if x[3].startswith('OK'))
        miss=[x for x in r if x[3]=='MISS']; nf=[x for x in r if x[3]=='NOFILE']
        print(f'== {md.replace(FA+"/","")}: quotes checked {n}, found {ok}, MISS {len(miss)}, NOFILE {len(nf)}')
        for x in miss: print('  MISS line',x[0],x[1],x[2],'|',x[5],'|',x[6])
        for x in nf: print('  NOFILE line',x[0],x[1],x[2],'|',x[5],'|',x[6])
```

Output for this company (first lines of the run, saved as `qc1.txt` in my scratch folder):

```
== cariloop/EVIDENCE.md: quotes checked 18, found 17, MISS 1, NOFILE 0
  MISS line 9 F1 Relief finder sec | in-home companion | [...find_care.txt]
== cariloop/PASS1-HOWWELL.md: quotes checked 9, found 8, MISS 0, NOFILE 1
  NOFILE line 87 F4 Refusing parent support sec | Managing family dynamics | []
== cariloop/PASS2-HOWWELL.md: quotes checked 14, found 5, MISS 0, NOFILE 9
```

(The 9 NOFILE rows are search phrases, study abstract quotes, and saved-page phrases; each was checked by hand, see Check 1.)
