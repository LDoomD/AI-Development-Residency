# PASS 3 audit: Group texts and notebooks (independent check)

Date: 2026-11-06. Branch feature-analysis-4. Nothing committed. I did not do the earlier work. I tried to prove it wrong.
Repo root: `/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator` (note the space before the slash). Paths below start at `docs/sources/`.

What this "competitor" is: a workaround, not a product (family group chats and texts, shared calendars, shared sheets and docs, paper notebooks, binders, whiteboards, written password lists). The owner's Figma row (`figma-competitive-tables-2026-11-06.md`, section 4a) defines it as "Family group chats, notebooks, binders and whiteboards". Facebook groups are not in that definition. This matters for F1 and F10 below.

State key (skeptical-audit): proven / observed / inferred / documented / reported / not-assessed.

## How blind was I (honest limit)
- I read EVIDENCE.md and the PASS files first. My recount is "re-derived from raw data", not strictly blind.
- Strictly blind part: the 15-report random sample (check 2e). The script hid the labels; I classified the raw text first.
- Raw data I read myself: all 96 comment rows that mention a tool word in the 12 busiest threads of `group-texts-notebooks/PASS2-reddit-comments-threads.jsonl` (698 comments total), all comments in the 7 password and estate threads that mention a notebook, binder, list or sheet, every Facebook or support-group mention in all 698 comments, and 15 of the Reddit posts behind the pass-1 counts (through the random sample). I did not re-read all 87 counted entries one by one.

## Check 1. Quote and source check

Scripts: Appendix A, B, C (run from `/tmp` with `python3 -I`).

| Test | Result | State | Limit |
|---|---|---|---|
| A. 151 quoted phrases in EVIDENCE.md, PASS1, PASS2 against the files named in their rows | 110 confirmed in the cited file. 41 flagged. Nearly all 41 are search words ("group chat", "WhatsApp", "Marco Polo"), vendor-bait phrases ("I built") or quotes whose row cites no path. I checked the rest by hand. 1 real citation error (Q1). | proven plus observed | Words in a file, not what the file means. |
| B. 93 rows with a record id plus a quote: is the quote inside that exact record? | 93 of 93 ok | proven | none |
| C. 93 rows with a file path plus an id: is the id in that file? | 92 ok, 1 fail (Q1) | proven | none |
| D. Any quote cell over 20 words | 0 | proven | none |
| E. Kokorelias quote "my sister has set up a google calendar and everything is on there and we will assign who does what" | Present, split over two lines in `PASS2-paper-PMC8996302-kokorelias-siblings-dementia.md` lines 517 to 518. | observed | none |
| F. Yin 2023 numbers (140, 29%, p = 0.006) and Linden 2022 (51, 61, "wasn't alone in the darkness") and Bachmann 2020 (2,110 posts) | All present in the saved copies. | observed | Numbers exist; I did not re-judge the readings. |
| G. EVIDENCE.md note: 49,315 saved posts "de-duplicated" | posts.jsonl 43,665 + posts_targeted.jsonl 5,650 = 49,315, overlap 0. Statement true; "de-duplicated" changed nothing. | proven | none |

Real misses

| # | File and line | What is wrong | Fix |
|---|---|---|---|
| Q1 | `group-texts-notebooks/PASS1-HOWWELL.md` line 92 | Cites `reddit/arctic-shift-2026-11-03/posts.jsonl` for key p1xdkg46. The key is in `posts_targeted.jsonl`. Quote is real. (Same error in `everplans/PASS1-HOWWELL.md` line 43.) | Change the path. |
| Q2 | `group-texts-notebooks/PASS2-HOWWELL.md` line 127 | Bateman et al. 2017 numbers (6 caregivers did the first interview; 4 joined; 90% and 100% acceptability) come from an abstract that was "not saved". No saved copy exists in the folder. The project rule is to save every cited source. | Save the abstract. |
| Q3 | `group-texts-notebooks/EVIDENCE.md` line 26 | "write it on a board" is a Facebook snippet, not saved (disclosed as not relied on). | none, already disclosed |

## Check 2. Recount from raw data

### 2a. Table arithmetic (proven by script)
Row-count script over PASS1 and PASS2 tables: every cell's worked / did-not / mixed numbers match the summary tables.
- PASS1: 44 entries = 41 distinct posts (p1ct3r7y, p1wlrtcw, p1q2kzsl each count in two cells). The headline "44 counted reports" (PASS1 line 9) is 44 cell entries, not 44 independent reports.
- PASS2: 43 entries = 40 distinct (nlogime, nlpas1r, o112918 each count in two cells). Disclosed in PASS2 line 10.
- Across passes: no post counted twice between PASS1 and PASS2.

### 2b. F5 (relatives cover time): my recount
My rule: counts only if a family describes a chat, calendar, sheet or notebook and what happened when relatives were asked to help or share time.

| Class | Earlier combined | Mine | Why different |
|---|---|---|---|
| WORKED | 10 (PASS1 1 + PASS2 9) | 7 (+1 flagged) | Remove nb06d7p (a household wall calendar for meds, not relatives sharing time; the earlier file admits "not a relative sign-up"). Remove o112918 (the writer says "I dont have siblings"; the earlier file admits it is "not a test of relatives covering time"). The one PASS1 WORKED (p1nzsodj) is flagged as "may be a promotional post" and is polished copy; I hold it out. |
| MIXED | 9 | 9 | agree (nlo3ujy, nlo5c4d, nlpas1r, nlpg1iu, phwtel4 and the 4 pass-1 posts) |
| DID NOT WORK | 23 | 21 | Remove nlwi86e (follows the same ad template as the Caring Village promo comments; see below). Remove p1u9ey0z (a lost message in a group text; about information, not relatives helping). |
| Total | 42 | 37 (+1 flagged) | |

Uncounted but relevant: nlo7g8a ("I started with a ToDo list template in Google Sheets with easy to update status and who was working on what... We also have a shared calendar.") is a self-described success and was not counted. o1162b0 ("We use Cozi too... either help or at least acknowledge it") was not counted. Both are borderline. (observed)

### 2c. F4 (refusing parent support): my recount
Important fit problem: 14 of the 16 earlier reports are about a parent refusing a calendar, notebook, pillbox or reminder. That is accepting a memory aid, not accepting help from aides, day programs or relatives. Only p1gjgtgp (parents "stubborn at allowing help", reluctantly accepted caregivers) and p1q2kzsl (refused rehab) touch accepting care.

| Class | Earlier combined | Mine |
|---|---|---|
| WORKED | 2 | 1 (nlogime: whole family adopts the mother's own notebook) |
| DID NOT WORK | 12 | 11 |
| MIXED | 2 | 3 (p1gjgtgp moves here: parents accepted home caregivers, a written food list went unused; nlpas1r; o12rx9t) |
| Excluded | 0 | 1 (o112918: no refusal in the text) |

### 2d. F6, F1, F10 recount
- F6: 5 / 6 / 1 = 12 matches earlier. But 4 of the 5 WORKED are "list exists, not yet needed" (p1mie58p, p1oq44vv, binders in a safe lel6bun, lgqgdq8). Only lgoqped (child already uses locked notes on mother's computer) shows use. Call them WORKED (setup).
- F1: 0 valid reports for this competitor. The 2 PASS1 F1 entries (p1ct3r7y, p1wlrtcw) are about relatives not offering respite (an F5 problem). They are counted again in F5 #17 and #18. The 4 PASS2 F1 entries are about Facebook neighborhood groups used to find paid aides or facilities (p1j4yvgj, p1uk9twg, p1ilzbk7, p1o90jd8). Facebook groups are not in the Figma definition and none is about respite.
- F10, if Facebook and WhatsApp caregiver groups are counted: WORKED 1 (p1af8zpl), DID NOT WORK 8, MIXED 2 (p1n2pezc, and ko92avy, which I move from DID NOT WORK because the writer blocked some members but stayed). Earlier 1 / 9 / 1.
- F10 selection bias: in the same thread (1ocibas) the earlier pass counted Facebook negatives but not positives about support groups that are not Facebook: nknnixq ("I found a number of support groups/programs that worked for me... in-person, zoom, message boards") and nkoiw10 (says Facebook is "a no go" but "This group has been truthful, open... helpful"). I held these out because they are not Facebook; the earlier file did not say why it held them out.

### 2e. Random sample of 15 counted reports, labels hidden (seed 20261106, Script D)
Counted entries in the earlier files: 87.

| # | Id | Cell | My class | Earlier | Agree? |
|---|---|---|---|---|---|
| 1 | nkoiw10 | F10 | DID NOT WORK for Facebook only (same comment praises a non-Facebook group) | DID NOT WORK | yes, with note |
| 2 | p1qa4240 | F4 | DID NOT WORK (spouse ignores calendar; tool, not help) | DID NOT WORK | yes |
| 3 | p1gjgtgp | F4 | MIXED (parents accepted caregivers; list unused) | DID NOT WORK | NO |
| 4 | p1n1ottl | F5 | DID NOT WORK | DID NOT WORK | yes |
| 5 | p1ricuz1 | F5 | MIXED | MIXED | yes |
| 6 | p1ct3r7y | F1 | DID NOT WORK, but it belongs in F5 | DID NOT WORK (F1) | wrong cell |
| 7 | p1ocibas | F10 | DID NOT WORK | DID NOT WORK | yes |
| 8 | p1xdkg46 | F6 | DID NOT WORK | DID NOT WORK | yes |
| 9 | o112918 | F4 | not an F4 report (no refusal) | WORKED | NO |
| 10 | p1mie58p | F6 | WORKED, setup only | WORKED | yes, with note |
| 11 | p1e2c8u9 | F10 | DID NOT WORK | DID NOT WORK | yes |
| 12 | p1wlrtcw | F1 | DID NOT WORK, belongs in F5 | DID NOT WORK (F1) | wrong cell |
| 13 | p15wl31v | F4 | DID NOT WORK | DID NOT WORK | yes |
| 14 | p1bjkr0q | F5 | DID NOT WORK | DID NOT WORK | yes |
| 15 | p1q2kzsl | F5 | DID NOT WORK | DID NOT WORK | yes |

Class agrees 13 of 15; 2 disagree (#3, #9); 2 more are in the wrong cell (#6, #12). Clean agreement 11 of 15 (73%).

### 2f. Promo, vendor and bait
- nlwi86e: ad-template comment (see Caring Village audit). It is counted here as DID NOT WORK and counted in the Caring Village file as WORKED. Same comment, opposite use. Exclude from both.
- Duplicate pitch comments in thread 1qjr6ug (o11ecje = o11ehv9, o12oqry = o12pc8x) are word-for-word copies. Not counted here (good).
- nkoat05 (counted F10 DID NOT WORK) ends with an app pitch ("With Haven Ai"). The earlier file notes this. The Facebook sentence stands alone, so I keep it.
- PASS1 survey-bait exclusion list (line 112) looks right on the phrases I could check ("I built", "before I build anything").

## Check 3. Try to disprove

Reddit pages not fetched (robots for reddit.com not readable, 403); I used saved archives. PubMed Central pages fetched through Firecrawl (HTML only). Facebook not crawled. Trustpilot skipped. aplaceformom.com not touched.

| Cell | Earlier | What I searched | What I found | Effect |
|---|---|---|---|---|
| F1 | NO | Searched all 698 saved comments for respite and finder words; re-read the 4 Facebook F1 reports | No report of a chat or notebook finding respite. Facebook neighborhood groups gave a lead on an assisted-living home (p1ilzbk7) and a board-and-care lead (p1o90jd8), not respite. | NO holds (out-of-scope Facebook evidence noted). |
| F2 | NO (inferred) | Pass-2 scan said 41 close hits, 0 counted. I read all saved comments for Medicaid, apply, waiver | Nothing where a chat or sheet checks eligibility. Threads 12xgw3a and 1m48zh6 give Medicaid advice from strangers, not from a tool. | NO holds. |
| F3 | NO / LIMITED asking relatives | Searched comments for venmo, zelle, split costs, chip in | p1x4kmj4: asked about 20 relatives in a chat to chip in for a wheelchair, "all I got was crickets". One post. | NO. Asking relatives for money is an F5-type request; LIMITED only if the owner counts it. |
| F4 | NO | Firecrawl search: "parent refuses help calendar whiteboard notebook memory aid dementia accepted tips caregivers" | Alzheimers.gov and the Alzheimer's Society recommend notebooks, calendars and whiteboards as memory aids (documented). Nothing says a notebook gets a refusing parent to accept outside help. A home-care vendor page (myhometouch.com, not read in full) says a trusted carer works better than family-led approaches. | NO holds. |
| F5 | NO (EVIDENCE.md) / "NO as a tool; families do share time" (PASS2) | Firecrawl research search "WhatsApp group chat family caregivers coordinate care older parent qualitative study siblings" | Results are snippets only (PMC12223452 caregivers using mobile apps; PubMed 41259025 on caregiver coordination experiences). Not read in full. Saved studies: Kokorelias 2022 (14 sibling pairs; sisters often lead; calendar used to assign who does what), Breebaart 2018 (7 networks), Linden 2022 (CareVirtue shared journal, 51 caregivers). | The data say it can work for small organized families with one organizer. EVIDENCE.md NO is too strong. LIMITED. |
| F6 | LIMITED | Re-read counted posts | Paper lists work only if the parent keeps them current; 6 of 12 reports show scattered or forgotten lists. | LIMITED holds. |
| F8 | VERIFY then LIMITED | Searched saved posts for advice and expert words (43 close hits, 0 counted) | Group chats of relatives give no expert. Peer tips come from Facebook groups (Bachmann 2020, 100 pairs, 2,110 posts), which are outside the Figma definition. | NO for this competitor. |
| F9 | VERIFY then LIMITED | 9 close hits, 0 counted. Re-read p1nf3iw2 | Mother with repeated questions: "I have tried index cards and white boards but it's always the same opening volley." A hard message sent to a family chat (p1gozxxr) had no outcome. | NO (low confidence). |
| F10 | PARTLY | Firecrawl research search "caregiver WhatsApp support group peer support dementia caregivers online messaging group"; fetched PMC12761628 | Reviews say online peer support helps (snippets of PMC7646914, PMC10753418, PMC11811647; not read in full). I read PMC12761628 (Jain et al., Innovation in Aging, Dec 2025): 110 caregivers in 29 facilitated chat groups; activity ranged 1 to 904 messages per group; "some participants found the chatgroups to be supportive and helpful, several participants expressed that their chat group did not fully establish cohesion". Facilitated groups of strangers, not a family chat. | Mixed. Cell depends on whether Facebook and WhatsApp caregiver groups count as this competitor. VERIFY. |
| Every YES/LIMITED | n/a | Looked for "does not work" | F5 and F6 both have large DID NOT WORK counts (21 and 6). | Limits stated. |

## Corrections list (every error found in earlier files)

| # | File and line | Problem | Severity |
|---|---|---|---|
| 1 | `group-texts-notebooks/EVIDENCE.md` line 7 (F5) | Says NO. PASS2 later found 7 firm WORKED comments. The summary line in PASS2 (line 24) says "NO as a tool" while counting 10 worked. Verdict should be LIMITED. | High |
| 2 | `group-texts-notebooks/EVIDENCE.md` whole file | Has rows only for F1, F4, F5, F6. No row for F2, F3, F8, F9, F10, so the owner has no capability line for 5 of 9 cells. | Medium |
| 3 | `group-texts-notebooks/PASS1-HOWWELL.md` lines 36 and 37 (F1 #1 #2) | Not F1. These are relatives not offering respite (F5). They are also counted again in F5 #17 and #18. F1 count of 2 is wrong (0). | Medium |
| 4 | `group-texts-notebooks/PASS1-HOWWELL.md` line 9 | "44 counted reports" are 44 entries, 41 distinct posts. | Low |
| 5 | `group-texts-notebooks/PASS1-HOWWELL.md` line 52 (F4 #10 p1gjgtgp) | DID NOT WORK; should be MIXED. | Low |
| 6 | `group-texts-notebooks/PASS1-HOWWELL.md` lines 41 to 52 (F4 block) | 14 of 16 are about refusing memory aids, not help. The cell question is accepting help. | Medium |
| 7 | `group-texts-notebooks/PASS1-HOWWELL.md` line 72 (F5 #15 p1u9ey0z) | A lost message is not relatives failing to help. | Low |
| 8 | `group-texts-notebooks/PASS1-HOWWELL.md` line 80 (F5 #23 p1nzsodj) | The only WORKED in pass 1 is flagged as possible promo, still counted. | Low |
| 9 | `group-texts-notebooks/PASS1-HOWWELL.md` line 92 | Wrong file path (Q1). | Low |
| 10 | `group-texts-notebooks/PASS2-HOWWELL.md` lines 66 and 67 (F5 #8 nb06d7p, #9 o112918) | Counted WORKED though both Limit cells say they are not relatives sharing time. | Medium |
| 11 | `group-texts-notebooks/PASS2-HOWWELL.md` line 51 (F4 #4 o112918) | WORKED for a refusal that is not in the text. | Medium |
| 12 | `group-texts-notebooks/PASS2-HOWWELL.md` line 73 (F5 #15 nlwi86e) | Counted DID NOT WORK though the same comment is flagged as possible promo in the Caring Village file. | Medium |
| 13 | `group-texts-notebooks/PASS2-HOWWELL.md` lines 39 to 42 (F1) and 91 to 101 (F10) | Facebook groups are not in the competitor definition. F1 reports are about paid aides and facilities, not respite. | High (scope) |
| 14 | `group-texts-notebooks/PASS2-HOWWELL.md` lines 91 to 101 (F10) | Counts only Facebook negatives; omits non-Facebook positive comments in the same threads (nknnixq, nkoiw10) without saying why. Also ko92avy is MIXED, not DID NOT WORK. | Medium |
| 15 | `group-texts-notebooks/PASS2-HOWWELL.md` line 127 | Unsaved source (Q2). | Low |
| 16 | `group-texts-notebooks/PASS2-HOWWELL.md` lines 26 and 27 (F8, F9 "LIMITED: peers swap tips only") | The only evidence is a Facebook-group study (Bachmann 2020). Not this competitor. | Medium |
| 17 | `group-texts-notebooks/EVIDENCE.md` line 13 (F6) | The quote is a person who had no passwords ("I didn't have access to her computer or cell phone passwords"). It shows need, not that a paper list works. | Low |

## Final verdict per cell

Counts are independent family reports (mine). "Docs" = documented evaluations.

| Cell | Verdict | Confidence | Reports worked / did not / mixed | Documented evaluations | Why, in one sentence |
|---|---|---|---|---|---|
| F1 Relief finder | NO | medium | 0 / 0 / 0 valid | none | A chat or notebook cannot search for respite. |
| F2 Eligibility and applications | NO | medium | 0 / 0 / 0 | none | A chat or notebook holds no program data. |
| F3 Paying for relief | NO | low to medium | 0 / 1 / 0 (one chip-in ask got no reply) | none | Chats can ask relatives for money and nothing more. |
| F4 Refusing parent support | NO | medium | 1 / 11 / 3 (most are about memory aids) | Alzheimers.gov and Alzheimer's Society recommend memory aids; nothing about refusal of help | Nothing here helps a parent who says no; tools offered to a parent are usually refused. |
| F5 Relatives cover time | LIMITED (works for small, organized families with one organizer; no way to assign, track or confirm; asks to quiet relatives get silence) | medium | 7 (+1 flagged) / 21 / 9 | Kokorelias 2022 (14 sibling pairs); Breebaart 2018 (7 care networks); Linden 2022 (51 caregivers, a purpose-built app) | Many families make a shared calendar or notebook work, but 21 reports describe relatives who ignored it. |
| F6 Account access | LIMITED (paper list or password book helps only if the parent keeps it current and the child can reach it) | medium | 5 (4 setup only) / 6 / 1 | none for this workaround; category studies in the Everplans folder (Foong 2025, Khadka 2026) | A written list helps when it is current; 6 of 12 reports show lists scattered, lost or forgotten. |
| F8 Personal guidance | NO | low to medium | 0 / 0 / 0 | none for this workaround | Relatives in a chat are not a coach. |
| F9 Behavior and hard talks | NO | low | 0 / 1 / 0 (whiteboards did not stop repeated questions) | none | No behavior or hard-talk help; one post says memory aids did not work. |
| F10 People who understand | VERIFY (owner decision: does this competitor include Facebook and WhatsApp caregiver groups?) | low | If yes: 1 / 8 / 2 | Bachmann 2020 (100 pairs, 2,110 posts); Yin 2023 (140 caregivers); Jain 2025 (110 caregivers, 29 chat groups, mixed). If no: NO | A family chat connects relatives, not other caregivers, and caregiver groups on Facebook get mostly bad reviews from people who tried them. |

### Where I disagree with earlier helpers
- F5: EVIDENCE.md NO; me LIMITED. (PASS2 and Figma already say "partly".)
- F1: earlier 6 reports, me 0 valid. F10: earlier PARTLY; me VERIFY because of scope.
- F8, F9: earlier LIMITED; me NO (evidence is about Facebook groups, not this workaround).
- F4: same verdict (NO); I flag that most of the evidence answers a different question.
- F6: same (LIMITED).

### Where the evidence differs from the Figma table (need 4c row)
- Figma "Partly: work without the parent using any tech" for refusing parents: my NO. The reports show parents refuse the tools too.
- Figma F5 "Partly: everyone hears at once. Requests get silence or a like": agrees with my LIMITED and with PASS2; disagrees with EVIDENCE.md NO.
- Figma F6 "Partly: a binder holds papers. Records pile up": agrees.
- Figma need 1 "Partly: a written guide lets someone else step in": my F8/F9 NO is about coaching and hard talks, not a written care guide.

## Not checked
- The other 83 "take turns" posts and the long tail of posts that match none of the earlier search words (iMessage, Marco Polo, GroupMe, Signal, Telegram).
- The 87 counted entries one by one (I read a sample of 15 plus all F5, F10 and F6 comments).
- Facebook and WhatsApp groups themselves (private or login-walled).
- Whether the commenters are real people (usernames not kept).
- Whether relatives later helped after a post was written.
- The full text of the search-result papers I only saw as snippets (PMC12223452, PubMed 41259025, PMC7646914, PMC10753418, PMC11811647) and the vendor page myhometouch.com.
- Whether Reddit's vent-heavy sample under-counts quiet success (the earlier files say it does; I cannot size it).

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

