"""Check 2 step A: draw a reproducible stratified random sample of 50 mentions and write a BLIND reading file (no helper labels).
Run: python3 -I a_sample.py   (seed 20261106)"""
import json,random,re,pickle,collections
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
random.seed(20261106)
pick=[]
used=set()
def add(r):
    k=(r['id'],r['name'])
    if k in used: return False
    used.add(k); pick.append(r); return True
# step 1: one random mention from EVERY candidate (34), cycling through labels so labels spread out
names=sorted(set(r['name'] for r in rows))
for i,n in enumerate(names):
    L=[1,2,3,4,5][i%5]
    pool=[r for r in rows if r['name']==n and r['label_n']==L]
    if not pool: pool=[r for r in rows if r['name']==n]
    random.shuffle(pool); add(pool[0])
# step 2: make sure each label has at least 6
for L in (1,2,3,4,5):
    while sum(p['label_n']==L for p in pick)<6:
        pool=[r for r in rows if r['label_n']==L]; random.shuffle(pool)
        for r in pool:
            if add(r): break
# step 3: top up to 50 at random from labels 1-3 of the 9 big candidates
KEY=['IHSS','Medicaid','PACE','Hospice respite','Alzheimer','Support group','Facebook','Subreddit','ALZConnected']
pool=[r for r in rows if r['label_n'] in(1,2,3) and any(r['name'].startswith(K) for K in KEY)]; random.shuffle(pool)
for r in pool:
    if len(pick)>=50: break
    add(r)
random.shuffle(pick)
print('sample size',len(pick),collections.Counter(p['label_n'] for p in pick))
print('candidates covered',len(set(p['name'] for p in pick)))
print(collections.Counter(p['name'][:25] for p in pick).most_common())
json.dump(pick,open(SC+'sample50.json','w'))
KW={'IHSS':r'ihss|in.home supportive','Medicaid':r'cdpap|medicaid|waiver|hcbs|consumer.directed|ppl','PACE':r'\bPACE\b|all.inclusive','Hospice':r'respite','Alzheimer':r'association|alz\.org|helpline|800','Support group':r'support group|group','Facebook':r'facebook','Discord':r'discord','WhatsApp':r'whatsapp','Subreddit':r'this sub|subreddit|r/|reddit','ALZConnected':r'alzconnected|forum|this group|this site|here'}
def snip(t,name):
    rx=None
    for k,v in KW.items():
        if name.startswith(k) or k in name: rx=re.compile(v,re.I); break
    if len(t)<=1100: return t
    out=t[:350]+' [...] '
    if rx:
        ms=list(rx.finditer(t))[:3]
        for m in ms:
            a=max(0,m.start()-300); b=min(len(t),m.end()+300); out+=t[a:b].replace('\n',' ')+' [...] '
    return out
with open(SC+'blind50.txt','w') as f:
    for i,p in enumerate(pick,1):
        t=(U.get(p['id']) or packs.get(p['id']))['text']
        f.write(f"##### {i}  candidate: {p['name']}\n{snip(t,p['name'])}\n\n")
