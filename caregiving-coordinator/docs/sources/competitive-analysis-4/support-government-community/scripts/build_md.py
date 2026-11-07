import json,collections,pickle,re
import named,partb
rows=pickle.load(open('rows.pkl','rb'))
RH=json.load(open('rawhits.json'))
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
def line(*c): return '| '+' | '.join(str(x) for x in c)+' |'
# ---- Part C table
ORDER=[("Medicaid waiver / HCBS / paid-family-caregiver programs (incl. CDPAP)",255+0,"yes (but 48 of 78 are one NY change)"),
("IHSS (California paid family caregiver program)",101,"yes"),
("PACE (all-inclusive care program)",62,"yes"),
("Hospice respite benefit",27,"yes (23)"),
("Alzheimer's Association (helpline, groups, education)",22,"yes (19), but only 7 used it"),
("Support group (generic; any sponsor)",347,"yes (37 of 41 read; 114 coded posts exist)"),
("Subreddit communities (r/CaregiverSupport etc.; sample read)",1485,"yes, but circular"),
("ALZConnected forum (the data source itself)",165,"yes, but circular"),
("Facebook caregiver groups",405,"yes (21)"),
("Discord caregiver servers",37,"no (10)"),
("WhatsApp caregiver community groups",84,"no (5)"),
("WhatsApp family group chat",84,"no (5)"),
("CaringBridge",7,"no (6)"),
("Meals on Wheels",64,"no (6)"),
("NAMI",8,"no (4)"),
("Regional Center / state developmental disability agency",None,"no (4)"),
("Teepa Snow / Positive Approach to Care",4,"no (4)"),
("Al-Anon",4,"no (3)"),
("Medicare GUIDE program",7,"no (3, none used it)"),
("Meal Train",4,"no (3)"),
("Franchise home care (Home Instead, Visiting Angels)",None,"no (3)"),
("Wellthy",2,"no (2 asks)"),
("Psychology Today / online therapist finders",None,"no (2)"),
("Named respite facilities (Aegis, Passages)",None,"no (2 asks)"),
("Torchlight",None,"no (1 ask)"),("Papa Pals",None,"no (1 ask)"),("Well Spouse Association",3,"no (1)"),
("Hospice hotline",None,"no (1)"),("Meetup caregiver group (NYC)",None,"no (1)"),("SHIP counselor",None,"no (1)"),
("Lotsa Helping Hands",3,"no (0 real)"),("Cozi",2,"no (0 real)"),("Family Caregiver Alliance",1,"no (0 real)"),("Eldercare Locator",1,"no (0 real)")]
tc=[line('Candidate','Posts read','Raw hits','Caregiver reports (labels 1-3)','Used it (label 1)','A1 parent','A2 spouse/partner','Other or unclear','Worked','Mixed','Did not work','No outcome','Enough to decide?'),line(*['---']*13)]
for nm,raw,en in ORDER:
    rs=by.get(nm,[]);cg=[r for r in rs if r['label_n'] in(1,2,3)]
    A1=sum(r['cared_for']=='parent' for r in cg);A2=sum(r['cared_for']=='spouse or partner' for r in cg)
    o=collections.Counter(r['outcome'] for r in cg)
    tc.append(line(nm,len(rs),raw if raw is not None else 'n/a',len(cg),sum(r['label_n']==1 for r in cg),A1,A2,len(cg)-A1-A2,o['WORKED'],o['MIXED'],o['DID NOT WORK'],o['NO OUTCOME'],en))
open('out/tbl_c.md','w').write('\n'.join(tc))
# ---- Part B tables
REAL={"Alzheimer's Association (incl. hotline/helpline, local chapter)","ALZConnected (Alzheimer's Association online forum)","Teepa Snow / Positive Approach to Care","Natalie Edmonds / Careblazers (YouTube)","ADEAR (NIA Alzheimer's education center)","Al-Anon","Emotions Anonymous","Wellthy","Torchlight","Papa Pals","Psychology Today / SonderMind / Zencare (therapist finders)","Home Instead / Visiting Angels (franchise home care)","Meals on Wheels","Pima Council on Aging (AZ)","PACE (incl. Innovage, WelbeHealth)","IHSS (California)","NY CDPAP / PPL","Medicare GUIDE program","SHIP counselor","Eldercare Locator","Meetup group (NYC caregiving)","Millennial & Gen X Alzheimer's Caregivers (WhatsApp)","Seniors Helping Seniors","Care.com / Caring.com / A Place for Mom / AgingCare.com","Medi-Cal (California Medicaid)","Respite facility by name (Aegis, Passages, Brookdale, Silverado)","Facebook caregiver groups","Discord servers","Reddit communities","Adult Protective Services","Area Agency on Aging (any name: AAA, council on aging, dept of aging, aging services)","VA caregiver programs (PCAFC, VA respite, Aid & Attendance, ChampVA, VD-HCBS)","Other state Medicaid waiver programs (SC Community Choices, CAPDA, IRIS, ADvantage, NHTD, Elderly Waiver, SMMC LTC, ACT150, Assisted Living Waiver)","Regional Center / state DD agency (DDS, APD)"}
b=[]
for n,a,s,ids in named.out:
    b.append((a,s,n,'Real named organization, program or service' if n in REAL else 'Generic type or group of names'))
for k,(ids,sgids) in partb.res.items():
    if k[0]=='G' and k[1] not in ('Hotline / helpline (any)','Church / faith community','Bereavement / grief group','Senior center / community center'): b.append((len(ids),len(sgids),k[1],'Generic type'))
b.sort(key=lambda x:(-x[0],x[2]))
tb=[line('Rank','Name or type','Posts naming it (of 831 relief posts)','Of the 114 support-group posts','Kind'),line(*['---']*5)]
for i,(a,s,n,k) in enumerate(b,1): tb.append(line(i,n,a,s,k))
open('out/tbl_b.md','w').write('\n'.join(tb))
# raw hits table
rh=[line('Name','Filter used (short)','Raw hits in all 50,547 saved items','Read by me'),line(*['---']*4)]
RAW=[("Medicaid waiver / HCBS (incl. CDPAP, 'waiver program', 'home and community based')","medicaid waiver, waiver program, HCBS, CDPAP, consumer-directed, community choices, ...",255,"101 (random 100 + 1 forum comment)"),
("IHSS","IHSS, in-home supportive services",101,"101 (all)"),("PACE","PACE (capital letters) or 'program of all-inclusive'",62,"62 (all)"),
("Hospice respite","'hospice' within 60 characters of 'respite'",27,"27 (all)"),
("Alzheimer's Association","association, alz.org, helpline, 800 number",22,"22 (all) + 3 more found later"),
("ALZConnected forum","'alzconnected' (almost all hits were links, not talk)",165,"45 prose mentions (all that were not links)"),
("Family Caregiver Alliance","name or caregiver.org",1,"1 (all)"),("Well Spouse Association","'well spouse', 'wellspouse'",3,"3 (all)"),("Caregiver Action Network","name",0,"0"),
("Medicare GUIDE","'GUIDE program/model'",7,"7 (all)"),("Teepa Snow","teepa, positive approach to care",4,"4 (all)"),("Wellthy","name",2,"2 (all)"),
("Lotsa Helping Hands","'lotsa'",3,"3 (all; 0 real)"),("CaringBridge","name",7,"7 (all)"),("Meal Train","name",4,"4 (all)"),("Cozi","name",2,"2 (all; 0 real)"),
("Facebook groups","'facebook' within 3 words of group/page/community (broad word 'facebook' alone: 405 hits)",64,"64 (all narrow hits)"),
("Discord","name",37,"37 (all)"),("WhatsApp","name",84,"84 (all)"),
("Subreddit communities","'this sub', 'subreddit', 'r/CaregiverSupport' etc. (1,485); with support words nearby (959)",959,"100 (random of 959)"),
("Al-Anon","name",4,"4 (all)"),("NAMI","capital letters",8,"8 (all)"),("Savvy Caregiver","name",0,"0"),("Meals on Wheels","name",64,"6 (those inside the 831 relief posts)"),
("Senior center / church","'senior center', 'church' near caregiver words",117,"29 (read inside the 831 relief posts)"),("Caregiver stipend / paid family caregiver","stipend, voucher, 'paid caregiver program'",76,"covered inside the Medicaid and IHSS reading"),
("Respite voucher / ARCH / lifespan respite","names",1,"1 (all)"),("Eldercare Locator","name",1,"1 (all)")]
for r in RAW: rh.append(line(*r))
open('out/tbl_raw.md','w').write('\n'.join(rh))
print(len(b))
