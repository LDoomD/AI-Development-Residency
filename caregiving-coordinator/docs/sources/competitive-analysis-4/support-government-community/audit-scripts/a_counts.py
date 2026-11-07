"""Check 3a: re-derive raw hit counts and caregiver-report counts from raw data with the auditor's own regexes. Run: python3 -I a_counts.py"""
import json,re,pickle,collections,hashlib
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
RX={
 'PACE':(re.compile(r"\bPACE\b(?! ?of)|program of all[- ]inclusive"),'PACE (all-inclusive care program)'),
 'IHSS':(re.compile(r"\bIHSS\b|in[- ]home supportive services"),'IHSS (California paid family caregiver program)'),
 'Hospice respite':(re.compile(r"hospice.{0,60}respite|respite.{0,60}hospice",re.I|re.S),'Hospice respite benefit'),
 "Alz Assoc":(re.compile(r"alzheimer'?s? assoc|alz\.org|\balz assoc|800[- .]?272[- .]?3900|alzheimer'?s? (hotline|helpline)",re.I),"Alzheimer's Association (helpline, groups, education)"),
 'Facebook(narrow)':(re.compile(r"(facebook|\bfb\b)[ \-]*(\w+ ){0,3}(groups?|pages?|communit(y|ies))\b|\b(groups?|communit(y|ies)) (on|in|at|through) (facebook|fb)\b",re.I),'Facebook caregiver groups'),
 'Support group':(re.compile(r"support groups?",re.I),'Support group (generic; any sponsor)'),
}
rd=lambda n:{r['id'] for r in by[n]}
for k,(rx,name) in RX.items():
    hits={i for i,v in U.items() if rx.search(v['text'])}
    # packs-only items (pack texts that are not in U)
    ph={i for i,v in packs.items() if rx.search(v['text'])}
    read=rd(name); reps={r['id'] for r in by[name] if r['label_n'] in(1,2,3)}
    print(f"{k:18s} raw hits in all {len(U)} items: {len(hits):4d} | helper read {len(read)} | hits not read by helper: {len(hits-read)} | read but not matching my regex: {len(read-hits)} | caregiver reports(1-3): {len(reps)} | in 831-relief set hits: {len(ph)}")
# Medicaid/IHSS/PACE/etc: how many unique posts if you merge PACE+IHSS+Medicaid reports
allrep=collections.defaultdict(set)
for r in rows:
    if r['label_n'] in(1,2,3): allrep[r['id']].add(r['name'][:14])
multi={i:n for i,n in allrep.items() if len(n)>1}
print('post ids that count as a caregiver report under >1 candidate:',len(multi))
c=collections.Counter(tuple(sorted(n)) for n in multi.values()); print(c.most_common(15))
# looser duplicate test on candidate reports: first 120 normalized chars
def k(i,n=120):
    t=(U.get(i) or packs.get(i) or {}).get('text','')
    return re.sub(r'\W+','',t.lower())[:n]
for name in ['PACE (all-inclusive care program)','IHSS (California paid family caregiver program)','Hospice respite benefit',"Alzheimer's Association (helpline, groups, education)",'Facebook caregiver groups','Support group (generic; any sponsor)','Medicaid waiver / HCBS / paid-family-caregiver programs (incl. CDPAP)']:
    reps=[r['id'] for r in by[name] if r['label_n'] in(1,2,3)]
    g=collections.defaultdict(list)
    for i in reps: g[k(i)].append(i)
    d=[v for v in g.values() if len(v)>1]
    # forum threads
    th=collections.Counter(U[i]['thread'] for i in reps if i in U and U[i]['src']!='reddit')
    print(f'{name[:30]:30s} reports {len(reps)} | same first-120-chars groups {len(d)} {d[:3]} | forum reports {sum(th.values())} in {len(th)} threads')
