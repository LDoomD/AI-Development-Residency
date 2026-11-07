"""Check 2c: is any person counted twice? Look for same-title / same-opening posts among labels 1-3 (all candidates), and posts with identical or near-identical text. Run: python3 -I a_dups.py"""
import json,re,pickle,collections,difflib
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
rep=[r for r in rows if r['label_n'] in(1,2,3) and r['source']=='reddit']
def title(i): return re.sub(r'\W+',' ',U[i]['text'].split('\n')[0].lower()).strip()
g=collections.defaultdict(set)
for r in rep: g[title(r['id'])].add(r['id'])
d={t:v for t,v in g.items() if len(v)>1 and len(t)>8}
print('same-title groups among reddit caregiver reports (labels 1-3):',len(d))
for t,v in d.items():
    print(' ',t[:60],sorted((i,U[i]['date']) for i in v),[ (r['name'][:12],r['label_n']) for r in rep if r['id'] in v][:4])
# near-duplicate body texts (ratio>0.9) within the same candidate, comparing posts <=60 days apart
byname=collections.defaultdict(list)
for r in rep: byname[r['name']].append(r['id'])
n=0
for name,ids in byname.items():
    for a in range(len(ids)):
        for b in range(a+1,len(ids)):
            ta=U[ids[a]]['text'][:400];tb=U[ids[b]]['text'][:400]
            if len(ta)>40 and difflib.SequenceMatcher(None,ta,tb).quick_ratio()>0.9 and difflib.SequenceMatcher(None,ta,tb).ratio()>0.85:
                print('NEAR-DUP',name[:25],ids[a],ids[b],ta[:60].replace('\n',' ')); n+=1
print('near-dup pairs',n)
# explicit: the WhatsApp asks and any posts by same-day same-sub with identical title in whole corpus among relevant
