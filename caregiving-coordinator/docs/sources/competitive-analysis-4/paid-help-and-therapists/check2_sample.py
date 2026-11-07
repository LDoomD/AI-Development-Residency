import sys,re,json,random,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
D=os.path.dirname(os.path.abspath(__file__))+'/'
U,_=load()
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
random.seed(20261106)
idx=list(range(len(rows))); picked=[]
def pick(cands):
    c=[i for i in cands if i not in picked]
    if c: picked.append(random.choice(c))
names=sorted({r['name'] for r in rows})
for n in names: pick([i for i in idx if rows[i]['name']==n])
for lab in (1,2,3,4,5):
    for _ in range(5): pick([i for i in idx if rows[i]['label']==lab])
while len(picked)<40: pick(idx)
random.shuffle(picked)
json.dump([[rows[i]['id'],rows[i]['name']] for i in picked],open(D+'check2_sample_ids.json','w'))
nm={'Care.com':r'care\.com|care dot com','Home Instead':r'home instead','Visiting Angels':r'visiting angels?','Senior Helpers':r'senior helpers?','Right at Home':r'right at home','Comfort Keepers':r'comfort keepers?','Papa':r'papa|joinpapa','BetterHelp':r'better ?help','Talkspace':r'talk ?space','Headway':r'headway','Psychology Today':r'psychology ?today','SonderMind':r'sonder ?mind','Zencare':r'zencare'}
out=[]
for n,i in enumerate(picked,1):
    r=rows[i]; t=U[r['id']]['text']
    m=re.search(nm[r['name']],t,re.I); s=m.start() if m else 0
    a=max(0,s-900); b=min(len(t),s+900)
    out.append(f"##### [{n}] id={r['id']} name={r['name']} src={U[r['id']]['src']} len={len(t)}\n"+("(...)" if a>0 else "")+t[a:b]+("(...)" if b<len(t) else "")+"\n")
open(D+'check2_blind_packet.txt','w').write('\n'.join(out))
print(len(out), 'names covered',len({rows[i]['name'] for i in picked}),'labels',sorted({rows[i]['label'] for i in picked}))
import collections;print(collections.Counter(rows[i]['label'] for i in picked),collections.Counter(rows[i]['name'] for i in picked))
