import sys,re,json,random,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
D=os.path.dirname(os.path.abspath(__file__))+'/'
U,_=load()
M=json.load(open(D+'manual_codes.json'))
random.seed(7)
S={}
S['paid_PV']=random.sample(sorted(k for k,v in M['paid'].items() if v.startswith('PV')),30)
S['paid_PR']=random.sample(sorted(k for k,v in M['paid'].items() if v.startswith('PR')),30)
S['ther_TH']=random.sample(sorted(k for k,v in M['ther'].items() if v.startswith('TH')),30)
json.dump(S,open(D+'check3d_sample_ids.json','w'),indent=1)
cue=re.compile(r"aide|caregiver|care giver|carer|agency|hired|hire|home care|companion|sitter|CNA|respite|VA\b|waiver|medicaid|helper|therap|counsel|psycholog|social worker|\bEAP\b|psychiatr|support group|insurance|afford|waitlist|wait list",re.I)
def excerpt(t,cap=1300):
    t=t.strip(); first=t.split('\n')[0][:140]
    sents=re.split(r'(?<=[.!?])\s+|\n+',t)
    keep=[s.strip() for s in sents if cue.search(s) and s.strip()!=first]
    out=first+' || '+' '.join(keep)
    return out[:cap]
for grp,ids in S.items():
    out=[]
    for n,i in enumerate(ids,1):
        out.append(f"[{grp} {n}] {i} (len {len(U[i]['text'])})\n{excerpt(U[i]['text'])}\n")
    open(D+f'check3d_blind_{grp}.txt','w').write('\n'.join(out))
    print(grp,len(ids))
