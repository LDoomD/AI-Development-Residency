import sys,json,glob,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import S
M=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/manual_codes.json'))
codes={}
for f in glob.glob(S+'market-analysis-3/segments-11-12/codes/codes-*.json'):
    for d in json.load(open(f)): codes[d['id']]=d
aud=json.load(open(S+'market-analysis-3/segments-11-12/audience-labels.json'))
paid=[i for i,d in codes.items() if d['relevant'] and 'paid aide or companion' in d['help']]
ther=[i for i,d in codes.items() if d['relevant'] and 'therapist or counselor for the caregiver' in d['help']]
print("paid-aide posts",len(paid),"therapist posts",len(ther),"union",len(set(paid)|set(ther)),"manual_codes sizes",len(M['paid']),len(M['ther']),"sets equal:",set(paid)==set(M['paid']),set(ther)==set(M['ther']))
def A(i):
    l=aud.get(i,{}).get('label','MISSING')
    return {'parent':'A1','spouse or partner':'A2'}.get(l,'other:'+l)
def grp(book,pref,label):
    ids=[i for i,v in M[book].items() if v.split()[0] in pref]
    c=collections.Counter('A1' if A(i)=='A1' else 'A2' if A(i)=='A2' else 'other' for i in ids)
    print(f"{label:22} n={len(ids):3} A1 {c['A1']:3} A2 {c['A2']:3} other {c['other']:3} | missing audience label: {sum(1 for i in ids if A(i)=='other:MISSING')}")
    for a in('A1','A2'):
        o=collections.Counter(M[book][i].split()[1] for i in ids if A(i)==a)
        print('     ',a,dict(o))
grp('paid',['AG'],'agency'); grp('paid',['PV'],'family-paid'); grp('paid',['PR'],'program-paid'); grp('paid',['RW'],'respite worker'); grp('ther',['TH'],'therapist'); grp('ther',['TC'],'couples')
# blockers
def bl(book,pref,label):
    ids=[i for i,v in M[book].items() if v.split()[0] in pref]
    keys={'cost':'cost','refuses':'refuses','trust':'trust|quality|safety','rules':'rules|eligib|application','wait':'wait'}
    c=collections.Counter()
    for i in ids:
        b=' | '.join(codes[i]['barriers']).lower()
        import re
        for k,rx in keys.items():
            if re.search(rx,b): c[k]+=1
    print(label,len(ids),dict(c))
bl('paid',['AG'],'agency'); bl('paid',['PV'],'family-paid'); bl('paid',['PR'],'program-paid'); bl('ther',['TH'],'therapist')
allb=collections.Counter(b for i,d in codes.items() if d['relevant'] for b in d['barriers'])
print(allb.most_common(12))
