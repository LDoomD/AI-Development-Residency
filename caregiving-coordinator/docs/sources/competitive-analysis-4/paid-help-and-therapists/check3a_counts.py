import sys,re,json,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
U,_=load()
D=os.path.dirname(os.path.abspath(__file__))+'/'
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
def hits(rx,universe=U):
    r=re.compile(rx,re.I)
    return {k for k,u in universe.items() if r.search(u['text'])}
R={k:u for k,u in U.items() if u['src']=='reddit'}
cc=hits(r'\bcare\.com\b|care dot com')
print("Care.com regex hits: all",len(cc),"reddit",len(cc&set(R)),"forum",len(cc-set(R)))
print("  total occurrences:",sum(len(re.findall(r'\bcare\.com\b|care dot com',U[k]['text'],re.I)) for k in cc))
print("  broader 'care.com' without word boundary (agingcare.com etc):",len(hits(r'care\.com'))," 'carecom' no dot:",len(hits(r'\bcare ?com\b')))
mr={r['id'] for r in rows if r['name']=='Care.com'}
print("  helper's Care.com ids:",len(mr),"missing from helper:",sorted(cc-mr),"in helper but not my regex:",sorted(mr-cc))
# per-label ids
byl=collections.defaultdict(set)
for r in rows:
    if r['name']=='Care.com': byl[r['label']].add(r['id'])
print("  label->ids",{k:len(v) for k,v in byl.items()})
# 18 users: distinct ids? users counted once?
used=[r for r in rows if r['name']=='Care.com' and r['label']==1]
print("  used rows",len(used),"distinct ids",len({r['id'] for r in used}),"independent flag true",sum(r['independent'] for r in used))
ind=[r for r in rows if r['name']=='Care.com' and r['label'] in(1,2,3) and r['independent']]
print("  indep 1-3:",len(ind))
print("  Care.com label 1-3 ids that are forum messages:",[r['id'] for r in ind if not r['id'].startswith('p')])
# author duplicates: same text prefix across ids
txt=collections.defaultdict(list)
for r in ind: txt[U[r['id']]['text'][:80]].append(r['id'])
print("  dup text prefixes among independent:",[v for v in txt.values() if len(v)>1])
# VA
va=hits(r'visiting angels?')
mv={r['id'] for r in rows if r['name']=='Visiting Angels'}
print("\nVisiting Angels regex hits",len(va),"helper ids",len(mv),"missing:",sorted(va-mv),"extra:",sorted(mv-va))
vl=collections.Counter(); 
for r in rows:
    if r['name']=='Visiting Angels': vl[r['label']]+=1
print("  labels",dict(vl))
# who real: labels 1-3 vs 4,5
HI=hits(r'home instead'); mh={r['id'] for r in rows if r['name']=='Home Instead'}
print("Home Instead regex hits",len(HI),"helper ids",len(mh))
hi_name=hits(r'home instead(?! of)(?!,? (?:i|we|he|she|they|you|of))')  # rough
print("  hits not followed by 'of':",len(hits(r'home instead(?! of)')))
print("  helper 12 ids:",sorted(mh)); 
rest=sorted(HI-mh)
print("  hits NOT in helper's 12:",len(rest))
# capitalized 'Home Instead' as two words
cap=[k for k in rest if re.search(r'Home Instead(?! of)',U[k]['text'])]
print("  of those with capital-H-capital-I and not 'of':",cap)
for k in cap: 
    t=U[k]['text']; m=re.search(r'Home Instead(?! of)',t); print("   ",k,t[max(0,m.start()-100):m.end()+100].replace('\n',' '))
json.dump(dict(care_com_hits=sorted(cc)),open(D+'check3a_carecom_ids.json','w'))
