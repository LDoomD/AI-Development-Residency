# (id, name, label, used_for, cared_for, outcome, blockers, quote, note)
# label: 1 used, 2 considering/asking, 3 recommends/warns, 4 vendor/staff/ad/bait, 5 passing/wrong meaning
# writer role is "family caregiver" unless note says otherwise
A=[]
def a(id,name,label,used_for,cared_for,outcome,blockers,quote,note=''):
    A.append(dict(id=id,name=name,label=label,used_for=used_for,cared_for=cared_for,outcome=outcome,blockers=blockers,quote=quote,note=note))
NA='n/a'
# ---- small names
a('p1pwakzb','Comfort Keepers',4,NA,NA,NA,'', 'Established provider with franchises nationwide.','ad-style list of providers; no personal experience')
a('p1pwakzb','Visiting Angels',4,NA,NA,NA,'','National franchise with local offices.','same ad-style list')
a('p1pwakzb','Papa',4,NA,NA,NA,'','Tech-enabled care coordination platform.','same ad-style list')
a('p1sm8qcp','Senior Helpers',4,NA,NA,NA,'','Caregivers needed Bryan/ College station','job ad')
a('p1wu66hr','Senior Helpers',5,NA,'parent','NO OUTCOME','trust','I will not use their service based solely on that.','title says "Sensi senior helpers" but body names a company "Senai"; unclear if it is Senior Helpers; writer rejects an AI-sounding call')
a('p1wu65tj','Senior Helpers',5,NA,NA,NA,'','[removed]','repeat of p1wu66hr, body removed',) 
a('p10838b6','Senior Helpers',5,NA,'parent',NA,'','Senior helper/companion','generic phrase "senior helper/companion", not the company')
a('alzconnected-77395-COMMENT2','Senior Helpers',3,'finding a paid aide','unclear','NO OUTCOME','quality','A few names that pop into my mind are Home Instead, Senior Helpers, Right at Home, Visiting Angels, etc.','forum comment gives advice; says "The agencies will tell you they match the aide to the person. They try but they send whoever they can get."')
a('alzconnected-77395-COMMENT2','Right at Home',3,'finding a paid aide','unclear','NO OUTCOME','quality','A few names that pop into my mind are Home Instead, Senior Helpers, Right at Home, Visiting Angels, etc.','same comment as Senior Helpers (one person)')
a('alzconnected-77395-COMMENT2','Home Instead',3,'finding a paid aide','unclear','NO OUTCOME','quality','A few names that pop into my mind are Home Instead, Senior Helpers, Right at Home, Visiting Angels, etc.','same comment (one person)')
a('alzconnected-77395-COMMENT2','Visiting Angels',3,'finding a paid aide','unclear','NO OUTCOME','quality','A few names that pop into my mind are Home Instead, Senior Helpers, Right at Home, Visiting Angels, etc.','same comment (one person)')
a('p11bowfc','Right at Home',2,'a break','unclear','NO OUTCOME','','I am looking into them for some occasional care relief.','asks about "seniors helping seniors"; also looking at Right at Home and Visiting Angels')
a('p11bowfc','Visiting Angels',2,'a break','unclear','NO OUTCOME','','I am looking into them for some occasional care relief.','same post as Right at Home')
a('p1woym4s','Right at Home',4,NA,NA,NA,'','Senior Respite Care | Right at Home South Bend, IN','vendor ad, body removed')
a('p1wisur2','Right at Home',4,NA,NA,NA,'','Senior Respite Care | Right at Home South Bend, IN','vendor ad, body removed (repeat)')
a('p11kats4','Psychology Today',5,NA,NA,NA,'','Psychology Today Article: "When You Secretly Wish a Parent Would Die"','link to an article, not the therapist directory')
a('p12anay0','Psychology Today',5,NA,NA,NA,'','It does not attack spousal caregivers, but offers a compassionate explanation.','link to an article, not the therapist directory')
a('alzconnected-77427-COMMENT5','Psychology Today',1,'finding a therapist','unclear','WORKED','','I found my therapist though the Psychology Today website. It is a great resource.','forum comment; therapist for the writer')
a('alzconnected-77427-COMMENT6','SonderMind',1,'therapy for the caregiver','unclear','WORKED','','I found a gem through SonderMind.','forum comment; weekly then every other week')
a('p196re2l','Zencare',2,'finding a therapist','unclear','NO OUTCOME','quality (caregiving not searchable)','I want to find someone who understands caregiving stress.','asks about online therapy sites like Zencare; says most searches do not include caregiving as a topic')
a('p1k2fdi8','Talkspace',4,NA,'parent','WORKED','insurance','Found an option through Talkspace that gave her the ability to get the help she needed!','post link carries utm_campaign=grassroots and utm_medium=paidsocial: likely paid advertising; therapy is for the mother, not the writer')
a('p1k2fe6g','Talkspace',4,NA,'parent','WORKED','insurance','Found an option through Talkspace that gave her the ability to get the help she needed!','identical text posted to a second subreddit; same ad')
# Headway: all wrong meaning ("make headway")
for i,q in [('p1dg490a','make headway with benefits programs'),('p1dtfju3','make any headway with anybody'),('p1nqsczj','I might have finally made headway.'),('p14pweaa','I was making headway'),('p16pmqb9','that I’ve been making headway on'),('p1krko87','I thought I was making a little headway this week'),('p1mdflzz','not enough for her to actually make any headway'),('p1wa96tf','I cannot make headway with reason.')]:
    a(i,'Headway',5,NA,NA,NA,'',q,'the English word headway, not the therapy company')
# BetterHelp
a('p12j16pg','BetterHelp',2,'therapy for the caregiver','other relative','DID NOT WORK','cost, insurance, waitlist','I’m too poor to afford better insurance or to pay for any online services like BetterHelp.','writer cares for a brother; says three better therapists were overbooked and others did not take her insurance')
a('p15zsrse','BetterHelp',2,'therapy for the person cared for (not the caregiver)','other relative','DID NOT WORK','cost, insurance','We can’t afford BetterHelp.','therapy is for the ALS brother, not for the writer')
for i,q in [('p1disobf','wish he had some better help'),('p1dx0zvx','How can I provide better help to your families working as an EMT'),('p1ego2lu','she is getting better help there than if we went private'),('p1ktx989','that can better help me understand'),('p1rrvl66','how to better help them'),('p1u1wigy','how to better help caregivers'),('p1fvy6ho','How can I better help and cope'),('p1jdo94h','I can better help her as she ages')]:
    a(i,'BetterHelp',5,NA,NA,NA,'',q,'the words "better help", not the company')
a('p1f4b12j','BetterHelp',1,'therapy for the caregiver','other relative','NO OUTCOME','trust (sold data)','Betterhelp.com sold people’s information','writer says they used to be a client and got a small payout; no therapy result stated')
a('p1j8g4ez','BetterHelp',5,NA,NA,NA,'','I chose the BetterHelp/AlphaBrain/MyPillow company of cremating my mom?!','used as a joke comparison to a bad company')
a('p1nim5y7','BetterHelp',1,'therapy for the caregiver','parent','DID NOT WORK','','I also joined BetterHelp, but nothing has erased this constant anxiety','writer is an only child of an ill father; mom also has a diagnosis')
# Papa
a('p18a42uc','Papa',2,'a break','parent','NO OUTCOME','','Does anyone here have experience with this company?','Papa Pals: 30 free hours a year in the mother’s Medicare supplement plan')
