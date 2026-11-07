import json,re,glob,os
S="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/"
def load():
    U={}
    for f in ['reddit/arctic-shift-2026-11-03/posts.jsonl','reddit/arctic-shift-2026-11-03/posts_targeted.jsonl']:
        for l in open(S+f):
            d=json.loads(l)
            if d['key'] not in U:
                U[d['key']]=dict(id=d['key'],src='reddit',sub=d['subreddit'],date=d['created'],url=d['url'],text=d['text'])
    for site in ['agingcare','alzconnected']:
        for fn in glob.glob(S+f'forums/{site}/*/*.txt'):
            t=open(fn).read()
            tid=os.path.basename(fn)[:-4]
            m=re.search(r'^SOURCE: (.*)$',t,re.M); url=m.group(1) if m else ''
            parts=re.split(r'^=== (POST|COMMENT \d+)[^\n]*===\n',t,flags=re.M)
            # parts: [header, label, text, label, text...]
            for i in range(1,len(parts),2):
                lab=parts[i]; txt=parts[i+1].strip()
                k=f"{site}-{tid}" if lab=='POST' else f"{site}-{tid}-{lab.replace(' ','')}"
                U[k]=dict(id=k,src=site,sub=site,date='',url=url,text=txt)
    return U
