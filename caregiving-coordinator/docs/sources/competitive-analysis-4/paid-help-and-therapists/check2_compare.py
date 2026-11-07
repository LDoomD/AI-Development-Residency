import json,os,collections
D=os.path.dirname(os.path.abspath(__file__))+'/'
rows={(r['id'],r['name']):r for r in map(json.loads,open(D+'MENTIONS-READ.jsonl'))}
ids=json.load(open(D+'check2_sample_ids.json')); mine=json.load(open(D+'check2_my_labels.json'))
def norm_out(o):
    o=(o or '').upper()
    if o in('WORKED',):return 'worked'
    if o=='MIXED':return 'mixed'
    if o in('DID NOT WORK','NOT WORK'):return 'did not work'
    if o=='NO OUTCOME':return 'no outcome'
    return 'n/a'
def norm_aud(a): return (a or 'n/a')
agree=collections.Counter();tot=collections.Counter();dis=[]
for n,(i,nm) in enumerate(ids,1):
    r=rows[(i,nm)]; m=mine[str(n)]
    h=[r['label'],norm_out(r['fields']['outcome']),norm_aud(r['fields']['cared_for'])]
    for f,k in enumerate(['label','outcome','cared_for']):
        # outcome/cared compared only where both of us say it's a real caregiver mention (label 1-3 by either)
        if k!='label' and not (h[0] in(1,2,3) or m[0] in (1,2,3)): continue
        tot[k]+=1
        if h[f]==m[f]: agree[k]+=1
        else: dis.append((n,i,nm,k,'helper='+str(h[f]),'audit='+str(m[f])))
for k in tot: print(k,agree[k],'/',tot[k],f'{100*agree[k]/tot[k]:.0f}%')
# also: label agreement on "real family caregiver mention (1-3) vs not (4-5)"
rb=sum(1 for n,(i,nm) in enumerate(ids,1) if (rows[(i,nm)]['label']<=3)==(mine[str(n)][0]<=3))
print('real(1-3) vs not(4-5):',rb,'/ 40')
for d in dis: print(d)
