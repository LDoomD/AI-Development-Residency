import json,re,pickle,collections
P=pickle.load(open('packs.pkl','rb'));rel=json.load(open('rel_ids.json'));sg=set(json.load(open('sg_ids.json')))
N=[
("Alzheimer's Association (incl. hotline/helpline, local chapter)",r"alzheimer'?s?[’]? assoc|alz\.? assoc|alz association|alz\.org|alzheimer'?s?[’]? (hot ?line|help ?line|support line)|alzheimers? hot ?line|alzheimer help ?line|800.272.3900|alzimpact"),
("ALZConnected (Alzheimer's Association online forum)",r"alzconnected|alz connected"),
("Teepa Snow / Positive Approach to Care",r"\bteepa\b|positive approach"),
("Natalie Edmonds / Careblazers (YouTube)",r"natalie edmonds|careblazers"),
("ADEAR (NIA Alzheimer's education center)",r"\bADEAR\b"),
("Al-Anon",r"al-?anon"),
("Emotions Anonymous",r"emotions anonymous"),
("Wellthy",r"\bwellthy\b"),("Torchlight",r"\btorchlight\b"),("Papa Pals",r"\bpapa pals?\b"),
("Psychology Today / SonderMind / Zencare (therapist finders)",r"psychology today|sondermind|zencare"),
("Home Instead / Visiting Angels (franchise home care)",r"home instead|visiting angels"),
("Meals on Wheels",r"meals on wheels"),
("Area Agency on Aging (any name: AAA, council on aging, dept of aging, aging services)",r"area agenc|\bAAA\b|council (on|for) (the )?aging|department (of|on) aging|aging services|senior services|elderly affairs|ageoptions"),
("Pima Council on Aging (AZ)",r"pima council"),
("VA caregiver programs (PCAFC, VA respite, Aid & Attendance, ChampVA, VD-HCBS)",r"\bPCAFC\b|va caregiver|va respite|aid (&|and) attendance|champva|veteran.directed|va (home|health) care|va benefits|va (social|program)|(through|from|with) the va\b|\bVA\b.{0,40}\b(respite|caregiver)"),
("PACE (incl. Innovage, WelbeHealth)",r"\bPACE\b|innovage|welbehealth"),
("IHSS (California)",r"\bIHSS\b|in-home supportive"),
("Medi-Cal (California Medicaid)",r"medi-cal"),
("NY CDPAP / PPL",r"\bCDPAP\b|\bPPL\b"),
("Other state Medicaid waiver programs (SC Community Choices, CAPDA, IRIS, ADvantage, NHTD, Elderly Waiver, SMMC LTC, ACT150, Assisted Living Waiver)",r"community choices|\bCAPDA\b|\bIRIS\b|\bADvantage\b|\bNHTD\b|elderly waiver|\bSMMC\b|act ?150|assisted living waiver|community alternatives program|aged (and|&) disabled waiver|florida community care"),
("Medicaid waiver / HCBS (named generically)",r"medicaid waiver|waiver program|\bHCBS\b|home and community[- ]based"),
("Medicare GUIDE program",r"\bGUIDE (model|program)\b"),
("SHIP counselor",r"\bSHIP\b"),
("Eldercare Locator",r"eldercare locator"),
("Regional Center / state DD agency (DDS, APD)",r"regional center|\bDDS\b|persons with disabilities"),
("Adult Protective Services",r"adult protective|\bAPS\b"),
("Hospice (its respite benefit, hotline, social worker)",r"hospice"),
("Reddit communities",r"\breddit\b|\br/\w+|this sub\b|subreddit"),
("Facebook caregiver groups",r"(facebook|\bfb\b)[ \-]*(\w+ ){0,3}(support |caregiver |dementia )?(groups?|communit)"),
("Discord servers",r"\bdiscord\b"),
("WhatsApp groups (community or family)",r"whats ?app"),
("Meetup group (NYC caregiving)",r"\bmeetup\b"),
("Millennial & Gen X Alzheimer's Caregivers (WhatsApp)",r"millennial (&|and) gen ?x"),
("Disease-specific groups (Huntington's, cancer, Parkinson's, ALS, lung cancer)",r"(huntington|HD|cancer|parkinson|ALS|lung cancer|stroke|MS|COPD)[’']?s? (caregiver )?(support )?(group|community)|HD support group"),
("Hospital-run caregiver support group (e.g., children's hospital)",r"hospital.{0,40}caregiver support group|support group.{0,40}(children.s )?hospital"),
("Zoom support group run by a local nonprofit (e.g., Ontario)",r"zoom.{0,30}support group|support group.{0,60}zoom"),
("Caregiver support via employer: EAP, Torchlight, Wellthy, FMLA, paid leave",r"employee assistance|\bEAP\b|\bFMLA\b|paid (family|medical) leave|\bPFML"),
("Bereavement / grief support group",r"grief (group|support)|bereavement|life after loss"),
("Respite facility by name (Aegis, Passages, Brookdale, Silverado)",r"\baegis\b|\bpassages\b|brookdale|silverado"),
("Retirement community caregiver coordinator",r"caregiver coordinator"),
("Seniors Helping Seniors",r"seniors helping seniors"),
("Care.com / Caring.com / A Place for Mom / AgingCare.com",r"care\.com|caring\.com|place for mom|agingcare"),
("Senior center",r"senior cent(er|re)"),
("Church or faith group",r"\b(church|synagogue|parish|pastor|ministry)\b"),
("Hotline or helpline (any: hospice, Alzheimer's, crisis, 988)",r"hot ?line|help ?line|crisis line|\b988\b"),
("Caregiver social media / YouTube content",r"youtube"),
]
rx=[(n,re.compile(r,re.I if n not in("PACE (incl. Innovage, WelbeHealth)","IHSS (California)","ADEAR (NIA Alzheimer's education center)","SHIP counselor") else 0)) for n,r in N]
out=[]
for n,r in rx:
    ids=[i for i in rel if r.search(P[i]['text'])]
    out.append((n,len(ids),len([i for i in ids if i in sg]),ids))
if __name__=='__main__':
    for n,a,b,_ in sorted(out,key=lambda x:-x[1]): print(f"{a:4d} {b:4d} {n}")
    json.dump({n:ids for n,a,b,ids in out},open('named_hits.json','w'))
