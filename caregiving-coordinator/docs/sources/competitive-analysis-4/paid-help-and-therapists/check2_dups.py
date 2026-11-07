import sys,json,os,difflib,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
U,_=load()
D=os.path.dirname(os.path.abspath(__file__))+'/'
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
real=[r for r in rows if r['label']<=3]
print("rows label1-3:",len(real),"distinct ids:",len({r['id'] for r in real}))
c=collections.Counter(r['id'] for r in real)
print("ids counted for >1 brand (label1-3):",{k:v for k,v in c.items() if v>1})
# near-duplicate texts among distinct ids in label 1-3 (and label 4/5 that helper flagged independent)
ids=sorted({r['id'] for r in rows})
pairs=[]
for a in range(len(ids)):
    for b in range(a+1,len(ids)):
        ta,tb=U[ids[a]]['text'],U[ids[b]]['text']
        if abs(len(ta)-len(tb))>0.3*max(len(ta),len(tb),1): continue
        if len(ta)<60 and len(tb)<60:
            if ta.lower()==tb.lower(): pairs.append((ids[a],ids[b],1.0))
            continue
        s=difflib.SequenceMatcher(None,ta[:600],tb[:600]).quick_ratio()
        if s>0.9 and difflib.SequenceMatcher(None,ta[:600],tb[:600]).ratio()>0.85: pairs.append((ids[a],ids[b],round(s,2)))
print("near-duplicate text pairs among all cited ids:",pairs)
dup=[r for r in rows if r['repeat_of']]
print("helper-flagged repeats:",[(r['id'],r['repeat_of'],r['name'],r['label'],r['independent']) for r in dup])
# same subreddit + same date + label1-3 by Care.com (possible same author multi-posts)
g=collections.defaultdict(list)
for r in real:
    u=U[r['id']]
    if u['src']=='reddit': g[(u['sub'],u['date'])].append((r['id'],r['name']))
print("same sub+same day, label1-3, different ids:",[v for v in g.values() if len({i for i,_ in v})>1])
# quote-sharing across ids
q=collections.defaultdict(set)
for r in real: q[r['quote']].add(r['id'])
print("same quote under different ids:",[k for k,v in q.items() if len(v)>1])
