import json,re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load,S
U,dup=load()
print("messages loaded:",len(U),"reddit:",sum(1 for u in U.values() if u['src']=='reddit'),"forum:",sum(1 for u in U.values() if u['src']!='reddit'),"dup keys",dup)
D=os.path.dirname(os.path.abspath(__file__))+'/'
def ws(s): return re.sub(r'\s+',' ',s).strip()
def soft(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('‑','-').replace('–','-')
    return ws(s)
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
exact=soft_only=miss=0; over=[]; misses=[]; wrongpost=[]
for r in rows:
    q=r['quote']; t=U.get(r['id'],{}).get('text')
    if t is None: misses.append((r['id'],r['name'],'ID NOT IN CORPUS')); miss+=1; continue
    nw=len(q.split())
    if nw>20: over.append((r['id'],r['name'],nw))
    if q in t: exact+=1
    elif ws(q) in ws(t): exact+=1   # whitespace only
    elif soft(q) in soft(t): soft_only+=1
    else:
        miss+=1; misses.append((r['id'],r['name'],q))
print("MENTIONS-READ rows:",len(rows),"exact/whitespace-only:",exact,"needed curly-quote/dash fold:",soft_only,"MISS:",miss)
print("quotes >20 words:",over)
for m in misses: print("MISS",m)
# does quote sit in the id's own text AND does the name appear near? (name check)
nm={'Care.com':r'care\.com|care dot com','Home Instead':r'home instead','Visiting Angels':r'visiting angels?','Senior Helpers':r'senior helpers?','Right at Home':r'right at home','Comfort Keepers':r'comfort keepers?','Papa':r'papa','BetterHelp':r'better ?help','Talkspace':r'talk ?space','Headway':r'headway','Psychology Today':r'psychology ?today','SonderMind':r'sonder ?mind','Zencare':r'zencare'}
noname=[(r['id'],r['name']) for r in rows if not re.search(nm[r['name']],U[r['id']]['text'],re.I)]
print("rows whose cited post does not contain the business name at all:",noname)
# SYNTHESIS quotes
syn=open(D+'SYNTHESIS.md').read()
qs=re.findall(r'"([^"\n]{6,}?)"',syn)
# also curly
qs+=re.findall(r'“([^”\n]{6,}?)”',syn)
allsoft={k:soft(u['text']) for k,u in U.items()}
big=soft('\n'.join(u['text'] for u in U.values())).lower()
print("\nSYNTHESIS quoted strings found:",len(qs))
miss2=[];over2=[]
def norm_el(q):
    # split on ellipsis marks
    return [p for p in re.split(r'\.\.\.|…|\[[^\]]*\]',q) if len(p.strip())>5]
for q in qs:
    if len(q.split())>20: over2.append((len(q.split()),q))
    ok=all(soft(p).strip(' .,;').lower() in big for p in norm_el(q))
    if not ok: miss2.append(q)
print("not found anywhere in corpus (incl. paraphrase / non-quote phrases):",len(miss2))
for q in miss2: print("  SYN-MISS:",q)
print("over 20 words:",over2)
