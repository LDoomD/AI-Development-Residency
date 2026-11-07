"""Independent loader (written by the auditor, not the helper's corpus.py)."""
import json,re,glob,os
S="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/"
def load():
    U={}
    dup=0
    for f in ['reddit/arctic-shift-2026-11-03/posts.jsonl','reddit/arctic-shift-2026-11-03/posts_targeted.jsonl']:
        for l in open(S+f):
            d=json.loads(l)
            if d['key'] in U: dup+=1; continue
            U[d['key']]=dict(id=d['key'],src='reddit',sub=d['subreddit'],date=d['created'],url=d['url'],text=d['text'],nc=d.get('num_comments'))
    for site in ['agingcare','alzconnected']:
        for fn in sorted(glob.glob(S+f'forums/{site}/*/*.txt')):
            t=open(fn).read(); tid=os.path.basename(fn)[:-4]
            parts=re.split(r'^=== (POST|COMMENT \d+)[^\n]*===\n',t,flags=re.M)
            for i in range(1,len(parts),2):
                lab=parts[i]; k=f"{site}-{tid}" if lab=='POST' else f"{site}-{tid}-{lab.replace(' ','')}"
                U[k]=dict(id=k,src=site,sub=site,date='',url='',text=parts[i+1].strip())
    return U,dup
