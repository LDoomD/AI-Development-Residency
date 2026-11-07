"""Check 1: every quote in MENTIONS-READ.jsonl and SYNTHESIS.md exists in the cited saved item. Run: python3 -I a_quotes.py"""
import json,re,pickle,sys
sys.path.insert(0,'.')
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('&amp;','&').replace('&#x200B;','')
    s=re.sub(r'\*+|_{2,}','',s)
    return re.sub(r'\s+',' ',s).strip().lower()
NT={k:norm(v['text']) for k,v in U.items()}
NP={k:norm(v['text']) for k,v in packs.items()}
thread={}
for k,v in U.items(): thread.setdefault(v['thread'],[]).append(k)
allt=None
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
tiers={'item':0,'pack':0,'thread':0,'corpus':0,'none':0,'noquote':0}
miss=[];long_=[];urlbad=[];idmiss=[]
for i,r in enumerate(rows,1):
    q=r['quote']
    if r['id'] not in U and r['id'] not in packs and r['id'] not in thread: idmiss.append((i,r['id']))
    if not q: tiers['noquote']+=1; continue
    nq=norm(q)
    if len(q.split())>20: long_.append((i,r['id'],len(q.split())))
    # url check
    u=(U.get(r['id']) or packs.get(r['id']) or {}).get('url')
    if u and u!=r['url'] and not r['url'].startswith(u.split('?')[0][:30]): urlbad.append((i,r['id'],r['url'],u))
    if nq in NT.get(r['id'],''): tiers['item']+=1
    elif nq in NP.get(r['id'],''): tiers['pack']+=1
    elif r['id'] in thread and any(nq in NT[k] for k in thread[r['id']]): tiers['thread']+=1; miss.append((i,r['id'],'only elsewhere in same thread',q[:70]))
    elif any(nq in t for t in NT.values()): tiers['corpus']+=1; miss.append((i,r['id'],'only in a DIFFERENT item',q[:70]))
    else: tiers['none']+=1; miss.append((i,r['id'],'NOT FOUND',q[:90]))
print('rows',len(rows),tiers)
print('quotes >20 words',len(long_),long_[:10])
print('ids not in corpus/packs',len(idmiss),idmiss[:10])
print('url mismatches',len(urlbad),urlbad[:5])
print('MISSES',len(miss))
for m in miss: print(' ',m)
# SYNTHESIS.md quotes
syn=open(D+'SYNTHESIS.md').read().split('\n')
alltext=' '.join(NT.values())+' '+' '.join(NP.values())
found=0;sm=[];sl=[]
for ln,line in enumerate(syn,1):
    for q in re.findall(r'"([^"\n]{4,}?)"',line):
        # skip obviously non-quote scare quotes? record all, classify later
        nq=norm(q); w=len(q.split())
        ok=nq in alltext
        if w>20: sl.append((ln,w,q[:60]))
        (found:=found+1) if ok else sm.append((ln,w,q))
print('SYNTHESIS quoted strings found in corpus:',found,'not found:',len(sm),'over20:',len(sl))
for m in sm: print(' ',m)
for m in sl: print(' LONG',m)
