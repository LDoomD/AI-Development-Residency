import sys,re,json,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
U,_=load()
D=os.path.dirname(os.path.abspath(__file__))+'/'
helper={json.loads(l)['id'] for l in open(D+'MENTIONS-READ.jsonl')}
N={ 'Rula':r'\brula\b','Grow Therapy':r'grow therapy|growtherapy','Alma (capital A)':r'\bAlma\b','Lyra':r'\blyra\b','CareYaya':r'careyaya','Homewatch':r'homewatch','Interim HealthCare':r'interim (?:health|home)','BrightStar':r'bright ?star','Comfort Keepers':r'comfort keepers?','Right at Home':r'right at home','Senior Helpers':r'senior helpers?','Honor (capital, company)':r'\bHonor(?: Care| Home|\.com)|joinhonor|honorcare','Papa':r'joinpapa|papa pals|papa (?:app|inc|health)|\bPapa\b','Wellthy':r'wellthy','Amada':r'\bamada\b','Brightwood':r'brightwood','Seniors Helping Seniors':r'seniors helping seniors','A Place for Mom':r'place for mom','Caring.com':r'\bcaring\.com\b','Cerebral':r'\bcerebral\b','Thriveworks':r'thriveworks','Teladoc':r'teladoc','Charlie Health':r'charlie health','Ahead/Headspace':r'headspace','Home Helpers':r'home helpers','Always Best Care':r'always best care','Synergy HomeCare':r'synergy home','Bayada':r'bayada','Amedisys':r'amedisys','CareLinx':r'carelinx','Caregiver.com':r'caregiver\.com','Torchlight':r'torchlight','Cake/Cariloop':r'cariloop','Lotsa Helping Hands':r'lotsa helping','CaringBridge':r'caringbridge','Nurse Next Door':r'nurse next door','NannyServices':r'nannyservices','Sittercity':r'sittercity','Rover/Wag':r'\bwag!?\b','Angi/Thumbtack':r'thumbtack','Honor home care (word)':r'\bhonor\b(?=.{0,30}(?:care|home))','Brightside':r'brightside','Hims':r'\bhers\b(?=.{0,0})','SeniorAdvisor':r'seniorAdvisor|senior advisor','Care Patrol':r'carepatrol|care patrol','Caring Senior Service':r'caring senior service','Visiting Angels':r'visiting angels?','Home Instead':r'home instead','BetterHelp':r'better ?help','Open Path':r'open ?path','Talkspace':r'talk ?space','Headway':r'headway','Psychology Today':r'psychology ?today','SonderMind':r'sonder ?mind','Zencare':r'zencare','Cerebral(Cerebral)':r'zzzz'}
res={}
for n,rx in N.items():
    flags=0 if n in('Alma (capital A)','Honor (capital, company)','Papa') else re.I
    r=re.compile(rx,flags)
    hs=[k for k,u in U.items() if r.search(u['text'])]
    res[n]=hs
print(f"{'name':28} hits  in_helper_file  not_in_helper")
for n,hs in res.items():
    if n=='Cerebral(Cerebral)':continue
    print(f"{n:28} {len(hs):4} {len([h for h in hs if h in helper]):5} {len([h for h in hs if h not in helper]):5}")
json.dump(res,open(D+'check3b_hits.json','w'))
