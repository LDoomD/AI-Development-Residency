"""Two small checks: (1) app-maker words among the 55 Subreddit 'caregiver reports'; (2) VA caregiver-program posts, loose regex. Run after a_corpus.py: python3 -I a_subreddit_vendor_va.py"""
import re,pickle,json
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
R=re.compile(r"\b(launch(ed)?|our app|my app|we built|i built|we're building|i'm building|survey|beta|waitlist|download|startup|founder|our platform|our tool|feedback on)\b",re.I)
sr=[r for r in rows if r['name'].startswith('Subreddit') and r['label_n'] in(1,2,3)]
print('subreddit reports',len(sr))
for r in sr:
    t=U[r['id']]['text']; m=R.search(t)
    if m: print('VENDOR WORDS',r['id'],r['label_n'],r['outcome'],'|',t[max(0,m.start()-70):m.end()+90].replace('\n',' '))
V=re.compile(r"\bPCAFC\b|program of comprehensive assistance|veteran[- ]directed|\bVDC\b|VA caregiver|caregiver support program|VD-?HCBS|PACT act",re.I)
hits=[i for i,v in U.items() if V.search(v['text'])]
print('VA loose regex items',len(hits))
for i in hits:
    t=U[i]['text'];m=V.search(t); print(i,U[i]['date'],'|',t[max(0,m.start()-80):m.end()+120].replace('\n',' '))
