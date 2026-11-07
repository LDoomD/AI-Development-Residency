import sys,json,re,collections
sys.path.insert(0,'.')
from corpus import load
from annA2 import A
U=load()
def normmap(t):
    out=[];idx=[];prev_ws=False
    for i,ch in enumerate(t):
        if ch in '’‘': ch="'"
        elif ch in '“”': ch='"'
        elif ch in '‑‐–': ch='-'
        if ch.isspace():
            if prev_ws: continue
            ch=' '; prev_ws=True
        else: prev_ws=False
        out.append(ch); idx.append(i)
    return ''.join(out),idx
def verify(q,t):
    nt,idx=normmap(t); nq,_=normmap(q)
    nq=nq.strip()
    p=nt.find(nq)
    if p<0: return None
    raw=t[idx[p]:idx[p+len(nq)-1]+1]
    return re.sub(r'\s+',' ',raw)
# duplicates (same person or repeat post): id -> counted_with
DUP={'p1wu65tj':'p1wu66hr','p1hdsgrs':'p1hdsbd5','p1n1i991':'p1n1iak7','p1x1tgt8':'p1x1tdgi','p1x21nge':'p1x1tdgi','p1x48i33':'p1x1tdgi','p1k2fe6g':'p1k2fdi8','p1wisur2':'p1woym4s'}
AUD={'parent':'parent','spouse or partner':'spouse or partner','other relative':'other relative','child':'child','client':'client','unclear':'unclear','n/a':'n/a'}
LAB={1:'caregiver used it',2:'caregiver considering or asking',3:'caregiver recommends or warns',4:'vendor, staff, ad or survey-bait',5:'passing mention or wrong meaning'}
rows=[];bad=[]
seen=set()
for x in A:
    u=U[x['id']]
    key=(x['id'],x['name'])
    if key in seen: bad.append(('DUPKEY',key)); continue
    seen.add(key)
    raw=verify(x['quote'],u['text'])
    if raw is None: bad.append((x['id'],x['name'],x['quote']))
    src=u['src']
    rows.append(dict(id=x['id'],name=x['name'],label=x['label'],label_text=LAB[x['label']],
        used_for=x['used_for'],cared_for=AUD.get(x['cared_for'],x['cared_for']),outcome=x['outcome'],blockers=x['blockers'],
        quote=raw if raw else x['quote'],quote_machine_checked=raw is not None,
        source=('forum:'+src if src!='reddit' else 'reddit:r/'+u['sub']),date=u['date'],url=u['url'],
        independent=(x['id'] not in DUP),repeat_of=DUP.get(x['id'],''),note=x['note']))
print(len(rows),'bad:',bad)
json.dump(rows,open('rows.json','w'))
