"""Independent corpus loader for the audit (written by the auditor, not reused from helper scripts).
Builds a dict id -> {src,url,text,sub,date,thread}. Run: python3 -I a_corpus.py (prints counts)."""
import json,glob,os,re,pickle,sys
S="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/"
SCRATCH="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
def load():
    U={}
    for f in ['posts.jsonl','posts_targeted.jsonl']:
        for l in open(S+'reddit/arctic-shift-2026-11-03/'+f):
            d=json.loads(l)
            U.setdefault(d['key'],dict(id=d['key'],src='reddit',sub=d.get('subreddit'),date=d.get('created'),url=d.get('url'),text=d['text'],thread=d['key']))
    for site in ['agingcare','alzconnected']:
        for fn in sorted(glob.glob(S+f'forums/{site}/*/*.txt')):
            t=open(fn).read(); tid=os.path.basename(fn)[:-4]
            m=re.search(r'^SOURCE: (.*)$',t,re.M); url=m.group(1) if m else ''
            parts=re.split(r'^=== (POST|COMMENT \d+)[^\n]*===\n',t,flags=re.M)
            for i in range(1,len(parts),2):
                lab=parts[i]; k=f"{site}-{tid}" if lab=='POST' else f"{site}-{tid}-{lab.replace(' ','')}"
                U[k]=dict(id=k,src=site,sub=site,date='',url=url,text=parts[i+1].strip(),thread=f"{site}-{tid}")
    packs={}
    for f in glob.glob(S+'market-analysis-3/segments-11-12/packs/pack-*.json'):
        for p in json.load(open(f)): packs[p['id']]=p
    codes=[]
    for f in glob.glob(S+'market-analysis-3/segments-11-12/codes/*.json'): codes+=json.load(open(f))
    return U,packs,codes
if __name__=='__main__':
    U,packs,codes=load()
    pickle.dump((U,packs,codes),open(SCRATCH+'corpus.pkl','wb'))
    print('items',len(U),'reddit',sum(v['src']=='reddit' for v in U.values()),'forum',sum(v['src']!='reddit' for v in U.values()),'packs',len(packs),'codes',len(codes),'relevant',sum(c['relevant'] for c in codes))
