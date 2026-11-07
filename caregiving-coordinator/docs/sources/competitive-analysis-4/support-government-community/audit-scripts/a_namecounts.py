"""Check 3b/4: raw hit counts for the names the helper rejected. Run: python3 -I a_namecounts.py"""
import re,pickle
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
N={'Lotsa Helping Hands':r"\blotsa\b",'Meal Train':r"meal ?train",'Cozi':r"\bcozi\b",'CaringBridge':r"caring ?bridge",'Teepa/PAC':r"\bteepa\b|positive approach to care",'NAMI':r"\bNAMI\b",'Meals on Wheels':r"meals on wheels",'Savvy Caregiver':r"savvy caregiver",'Family Caregiver Alliance':r"family caregiver alliance|caregiver\.org\b",'Caregiver Action Network':r"caregiver action network|caregiveraction",'Well Spouse (org)':r"well spouse (association|summit)|wellspouse\.org",'Wellthy':r"\bwellthy\b",'Area Agency on Aging':r"area agency on aging|council on aging|dept\.? of aging|department of aging",'Adult day program/center':r"adult day (program|center|care|health)",'Senior center':r"senior cent(er|re)s?",'Discord':r"\bdiscord\b",'WhatsApp':r"whats ?app"}
for k,rx in N.items():
    R=re.compile(rx,0 if k=='NAMI' else re.I)
    print(f"{k:28s} {sum(1 for v in U.values() if R.search(v['text'])):4d} items")
