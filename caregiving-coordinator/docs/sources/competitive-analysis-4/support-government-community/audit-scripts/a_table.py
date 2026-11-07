"""Re-derive the Part C table from MENTIONS-READ.jsonl and compare with SYNTHESIS.md section 4. Run: python3 -I a_table.py"""
import json,re,collections,hashlib,pickle
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
tbl={}
for ln,l in enumerate(open(D+'SYNTHESIS.md'),1):
    if l.startswith('| ') and 69<ln<105 and not l.startswith('| ---') and 'Candidate' not in l:
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        tbl[c[0]]=(ln,c)
print('table rows in md',len(tbl),'names in jsonl',len(by))
bad=0
for n,rs in by.items():
    cg=[r for r in rs if r['label_n'] in(1,2,3)]
    used=[r for r in rs if r['label_n']==1]
    oc=collections.Counter(r['outcome'] for r in cg)
    a1=sum(r['cared_for']=='parent' for r in cg); a2=sum(r['cared_for']=='spouse or partner' for r in cg)
    mine=[len(rs),len(cg),len(used),a1,a2,len(cg)-a1-a2,oc['WORKED'],oc['MIXED'],oc['DID NOT WORK'],oc['NO OUTCOME']]
    if n not in tbl: print('NOT IN MD',n); continue
    ln,c=tbl[n]
    md=[int(c[1]),int(c[3]),int(c[4]),int(c[5]),int(c[6]),int(c[7]),int(c[8]),int(c[9]),int(c[10]),int(c[11])]
    # md cols: posts read(1) raw(2) reports(3) used(4) a1 a2 other worked mixed dnw no
    ok=mine==md
    if not ok: bad+=1; print('MISMATCH line',ln,n,'jsonl',mine,'md',md)
print('mismatching rows',bad)
# duplicates: same id twice within same candidate
for n,rs in by.items():
    ids=collections.Counter(r['id'] for r in rs)
    d=[i for i,c in ids.items() if c>1]
    if d: print('same id twice in',n,d)
# same text counted twice among labels 1-3 for same candidate (crossposts) using corpus
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
def key(i):
    t=(U.get(i) or packs.get(i) or {}).get('text','')
    return hashlib.md5(re.sub(r'\W+','',t.lower())[:300].encode()).hexdigest()
for n,rs in by.items():
    cg=[r for r in rs if r['label_n'] in(1,2,3)]
    g=collections.defaultdict(list)
    for r in cg: g[key(r['id'])].append(r['id'])
    d={k:v for k,v in g.items() if len(v)>1}
    if d: print('same text (first 300 chars) counted twice in',n,list(d.values())[:6])
# forum: reports from same thread
for n,rs in by.items():
    th=collections.Counter()
    for r in rs:
        if r['label_n'] in(1,2,3) and r['source']=='alzconnected': th[r['url']]+=1
    if th: print('forum reports',n,'total',sum(th.values()),'threads',len(th),'threads w/ >1:',sum(1 for c in th.values() if c>1))
