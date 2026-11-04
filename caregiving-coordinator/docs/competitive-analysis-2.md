# Competitive Analysis 2 (second version, 2026-11-04)

Version 1 (`docs/competitive-analysis.md`) answered most boxes with one pasted quote. This version answers every box with a short synthesis of ALL the research. Same content as the Figma section "CAREGIVING — Competitive Analysis 2" (file `HcDDdEGAnikTImO8v7UPMp`, node `2564:10354`, in Section 8). Version 1 is unchanged.

## How it was made

1. **Evidence packs** (`docs/sources/competitive-analysis-2/packs/`, `build_packs.py`): every caregiving app review (the 439-review filter, plus extra Google Play tags), the never-filtered MyChart and Everplans Apple reviews, every Reddit post in both downloads that names the competitor, and the forum app mentions. 1,101 items in total.
2. **Themes** (`themes/`, rules in `READER-INSTRUCTIONS.md`): readers read every item in full, kept only items written by someone caring for another person that say something about the product (577 kept), and counted themes from what people wrote. `verify_themes.py` checks every count against its id list and every quote word for word: 0 errors.
3. **Company facts** (`facts/`): every saved company page read in full, with each answer backed by quotes. `verify_facts.py` found all 273 quotes in the saved pages.
4. **Answers** (`answers-v2.json`): written from the themes and facts. `audit_answers.py` checks every bracketed number against the theme counts. The 13 numbers it flags come from store splits, prices and the readers' notes, and each was checked by hand.
5. **Figma**: cells pasted from `figma-grid.json` and hash-checked against it: 220 of 220 match.

**Gaps** compare each row with the 7 biggest caregiver problems in `docs/reddit-caregiver-findings-2026-11-03.md`. **Limits**: Everplans (1 caregiving review) and Lotsa (4 items) are too thin to judge. App-store reviews lean toward strong opinions. Reddit venting posts over-represent conflict. Some company pages were saved as 404s. Each row's last column states its own limits.

## The table

### Caring Village

- **Indirect or Direct?** Direct (coordination)
- **Market Segment** Family care-coordination apps
- **Website** https://caringvillage.com/
- **Main Features and Capabilities** One shared app for a family's care: calendar, to-dos, medication lists, care plan, journal, group messages, document storage, and an AI helper called Julia.
- **How do they differentiate themselves?** Claims to be one 'command center' that replaces scattered texts and spreadsheets, built by former caregivers, with a 24/7 AI assistant.
- **What do they do well?** Keeps the whole family updated and on the same page (10 of 29), puts the loved one's care in one place (8), and is easy to use (7). Families mainly use the shared calendar (6) and medication lists (6), and say it means less stress (5) and less back-and-forth than texting (3).
- **What do they not do well?** Small, scattered complaints, none bigger than 3: the daily care plan resets or is too rigid (3), bugs and lost entries (3), 'friends' can see private medical details (2), medication logs don't show who gave a dose (2), and it's hard to get everyone into the group (2).
- **What do customers say about them?** Mostly positive: praise themes reach 10, and no complaint theme is bigger than 3. Writers are mostly adult siblings sharing a parent's care. Caution: 13 of the 5-star reviews came from Sept 2025 to Apr 2026 with similar wording. Most detailed complaints are from 2019 and 2020. Caregivers on Reddit almost never name it (3 posts, none describing use).
- **What market gaps have they NOT filled?** It organizes information but can't make relatives help, the biggest caregiver problem (217 posts), and families say getting everyone to join is hard. It doesn't help with getting into the parent's bank, insurer or portal accounts (132 posts), doesn't help with POA problems (97), and has no safety or alert side (59). Few caregivers know it exists.
- **What's their unique value proposition?** One free app where the whole family coordinates a loved one's care together, so no one carries it alone.
- **What is their business model? How do they make money?** Freemium subscription. A free plan with ads, plus paid Circle and Village plans. It also sells to businesses for their patients or clients, and offers gift subscriptions. No funding figure found.
- **Who uses it, who pays, and what does it cost?** The caregiver who creates the 'village' pays. Everyone invited joins free. Free: 2 members. Circle: $14.99 a month (5 members). Village: $24.99 a month (50 members on the pricing page, 25 in the FAQ). 17% off yearly.
- **How do they retain customers?** The free plan's 2-member limit pushes larger families to pay, and daily to-dos, reminders and journal likes bring people back. Reviewers who stay use it daily for a long time (5). Use ends when the loved one dies (2).
- **How do they approach their customer experience?** Self-serve: a help center, a support email, guided setup, checklists and the Julia AI assistant. No phone support or hours are listed. Reviewers say the support team answers quickly (3).
- **Can a second or third relative join with their own login?** Yes. The creator invites relatives, friends and paid helpers, and each joins free with their own account and a role. Reviewers confirm big families share one group (5), but report limits on who can join and what they see (4).
- **How do they treat health data and consent?** Encrypted and never sold. Only members see the data, by roles the creator sets. Deletion is by emailing support. How to remove one member isn't stated. Reviewers worry that 'friends' can see private medical details (2).
- **What happens in an emergency or when it fails?** No emergency service and no support hours. It only offers preparedness checklists. No reviewer describes an emergency.
- **What does setup take?** The caregiver signs up with email, Apple or Google and is walked through it in a few minutes, then invites others. Works on iPhone, Android and the web. Reviewers call it simple and easy (7).
- **Evidence base and limits** 29 caregiving app reviews (23 Apple, 6 Google). No Reddit post describes using it. Possibly prompted 5-star reviews in 2025-26. Pages saved 2026-11-02. Data: docs/sources/competitive-analysis-2/themes/caring-village.json and facts/caring-village.json

### CaringBridge

- **Indirect or Direct?** Direct (coordination)
- **Market Segment** Family care-coordination apps
- **Website** https://www.caringbridge.org/
- **Main Features and Capabilities** A private web page or app journal for health updates, with comments, a help calendar for meals and rides, and links to GoFundMe and Meal Train.
- **How do they differentiate themselves?** Claims to be the established nonprofit (since 1997) built only for health journeys: private, ad-free, and never selling personal data.
- **What do they do well?** One update reaches everyone, so far fewer calls and texts (49 of 95). It frees the caregiver to be with the sick person (19), is easy to post and read (16), lets far-away family follow along (15), and the same page works again for each new crisis (8).
- **What do they not do well?** The app is the weak spot. Posting freezes or loses posts and photos (7), the app is weaker than the website (6), and the mid-2024 update broke features (4) and locked family out of sign-in (3). It isn't built for day-to-day care coordination (3), and donation requests feel pushy (2).
- **What do customers say about them?** Strongly positive about one job, telling everyone at once. Most of the 95 caregiving items are short 5-star Google reviews from 2020 to 2023. Usually a spouse or parent posts and relatives read (14). Complaints cluster around the 2024 app redesign. On Reddit it is rarely named (7 posts).
- **What market gaps have they NOT filled?** It's a one-way news feed, so it doesn't split tasks or get siblings to help day to day (217 and 187 posts). It doesn't touch accounts, POA or records (132, 97, 67). Medications and safety (77, 59) aren't covered. Families run group texts and spreadsheets next to it for the daily work (3).
- **What's their unique value proposition?** Update everyone at once about a loved one's health and gather support, so no one goes through it alone.
- **What is their business model? How do they make money?** A free, donation-funded nonprofit: about $10.6M revenue in FY2025, 97% from contributions. It asks users for gifts, and its privacy policy also lists sharing data for targeted ads.
- **Who uses it, who pays, and what does it cost?** A patient or family caregiver creates the page, and friends and family read it. It's free for everyone. Donors fund it, often the same families (6).
- **How do they retain customers?** No contract. People come back for comments, update alerts and journaling. Reviewers stay because it saves time in every crisis (8) and drop only the app, not the service, when posting fails (2).
- **How do they approach their customer experience?** A help center, video tutorials, customer care staff and online chat with a virtual or live agent. No reviewer mentions support.
- **Can a second or third relative join with their own login?** Yes. The author adds co-authors, and readers use their own accounts. Private pages limit readers to an approved list. Reviewers say people follow a shared link, often without signing up (4), and more than one relative can post (2). Older relatives got locked out when sign-in changed in 2024 (2).
- **How do they treat health data and consent?** The creator picks public, semi-private or private, and the default lets any signed-in user see posts. It says it doesn't sell health data but shares some data for targeted ads. Page deletion is by email and can take up to 90 days. Families trust it as a private space (6).
- **What happens in an emergency or when it fails?** Not stated on its pages. It isn't an emergency tool. When the app fails, families switch to the website (5).
- **What does setup take?** A patient or caregiver makes a page on the web or app and sets privacy (18 and over). Reviewers say it's easy to start and restart (6), but app posting is buggy (5).
- **Evidence base and limits** 95 caregiving items: 91 app reviews (79 Google, 12 Apple) and 4 Reddit posts. 15 copied reviews removed. Mostly short and positive. Eight company pages saved as empty. Data: docs/sources/competitive-analysis-2/themes/caringbridge.json and facts/caringbridge.json

### Lotsa Helping Hands

- **Indirect or Direct?** Direct (coordination)
- **Market Segment** Family care-coordination apps
- **Website** https://lotsahelpinghands.com/
- **Main Features and Capabilities** A free volunteer-help organizer: a shared task calendar (meals, rides, visits), announcements, well wishes and photos.
- **How do they differentiate themselves?** Claims to be the easiest free way to organize help from people who want to help but don't know how.
- **What do they do well?** Helpers sign up for shifts, tasks and meals (3 of 4).
- **What do they not do well?** Glitches block basic actions such as signing up or adding events (2 of 4).
- **What do customers say about them?** Too little evidence to judge: only 4 caregiving items. Two of the reviews are from 2013, and the Reddit writer only gives a short opinion.
- **What market gaps have they NOT filled?** It organizes outside volunteers, not the family's own daily care. Nothing for accounts, papers, medications, records or safety (132, 97, 77, 67, 59 posts). Caregivers on Reddit almost never name it (4 posts).
- **What's their unique value proposition?** A free central place to organize meals, rides and other help from friends and family for someone in need.
- **What is their business model? How do they make money?** Free. The saved pages don't say how it makes money. Old links hint at sponsors and partners (for example CancerCare's 'My Cancer Circle'). No funding found.
- **Who uses it, who pays, and what does it cost?** Caregivers, friends, neighbors and new parents use it. Free, and no payer is named.
- **How do they retain customers?** No tiers or contracts. The shared task calendar and emailed announcements keep a group active. No reviewer evidence.
- **How do they approach their customer experience?** A small help base for members and admins, plus contact emails. No reviewer evidence.
- **Can a second or third relative join with their own login?** Yes. The organizer invites people with their own logins. Admins assign roles and private groups. No reviewer evidence.
- **How do they treat health data and consent?** Admins can limit posts to chosen groups. Data handling and deletion aren't stated (the privacy page saved as a 404).
- **What happens in an emergency or when it fails?** Not stated. Not an emergency tool.
- **What does setup take?** The organizer creates a community, invites people and posts tasks. Web, iPhone and Android. Reviewers report glitches (2).
- **Evidence base and limits** Very thin: 3 app reviews (2 from 2013) and 1 Reddit post. Its privacy, FAQ and features pages saved as 404s. Data: docs/sources/competitive-analysis-2/themes/lotsa.json and facts/lotsa.json

### Medisafe

- **Indirect or Direct?** Indirect (covers part of the need)
- **Market Segment** Medication reminder apps
- **Website** https://medisafeapp.com/
- **Main Features and Capabilities** Medication reminders and refill alerts, drug-interaction warnings, one account for several family members' meds, and a 'Medfriend' who is alerted to missed doses.
- **How do they differentiate themselves?** Claims to be the number-one medication reminder, ranked first by pharmacists, with complicated dosing and security certifications.
- **What do they do well?** Keeps a loved one's complicated medication schedule on track (10 of 21), handles meds for several family members in one app (5), and lets a relative see from afar that doses were taken (4).
- **What do they not do well?** It's built for one person managing one set of meds. It's hard for more than one caregiver to share the work (4), the caregiver's view goes out of sync or loses meds (3), you can't tell whose dose or refill it is (2), alerts are unreliable (2), and setup is hard (2).
- **What do customers say about them?** Mixed: it works for one caregiver tracking a loved one (10), and breaks when caregivers share it (4) or their views go out of sync (3). Writers are adult children (7), spouses (5) and parents of a child (3). Many reviews that passed the first filter were patients tracking their own meds (9 dropped). Reddit barely names it (1 post, an ad for a rival).
- **What market gaps have they NOT filled?** Medications only. It doesn't spread the wider care work across siblings (187 posts), and gives no help with accounts, papers, records or safety (132, 97, 67, 59). Even the medication part breaks when two caregivers share it, which Reddit also shows: medication changes not shared, near double doses (24 posts).
- **What's their unique value proposition?** Never miss or double a dose, so you think less about medications and live more.
- **What is their business model? How do they make money?** Free app with a paid subscription (price not shown, the pricing pages saved as 404s). It also sells a platform to drug makers and providers and may share de-identified data commercially. Raised a $30M Series C in 2021.
- **Who uses it, who pays, and what does it cost?** Patients and family members use it. Some users pay the subscription, and drug companies and providers are business customers. Price isn't stated. A rival's ad says it limited free users in 2026 (not confirmed).
- **How do they retain customers?** Daily reminders, missed-dose alerts and a community, plus limited access without a subscription in some countries. Reviewers leave when the caregiver side fails (2), and fans recommend it (2).
- **How do they approach their customer experience?** A help center, email, a US phone number and a Facebook beta group. No reviewer theme on support.
- **Can a second or third relative join with their own login?** Yes, as a 'Medfriend' (gets alerts) or 'Caregiver' (can edit). Reviewers say watching doses works (4), but sharing breaks down between linked caregivers (4).
- **How do they treat health data and consent?** Collects meds, prescriptions, insurance and pharmacy data. It may share with drug makers and researchers, says it isn't bound by medical secrecy, and keeps data up to 7 years. Users can delete the account in the app. No reviewer theme.
- **What happens in an emergency or when it fails?** No emergency service. It warns that phone battery savers can silently stop reminders. Reviewers report unreliable alerts (2).
- **What does setup take?** Download it (iPhone, Android or web) and add meds. An account is optional. Reviewers find setup hard (2).
- **Evidence base and limits** 21 caregiving app reviews (15 Apple, 6 Google). No real Reddit use. Pricing pages missing. Data: docs/sources/competitive-analysis-2/themes/medisafe.json and facts/medisafe.json

### Everplans

- **Indirect or Direct?** Direct (access to accounts)
- **Market Segment** Digital vaults and emergency access
- **Website** https://www.everplans.com/
- **Main Features and Capabilities** A secure online vault for documents, IDs, accounts and wishes, with guided checklists and 'deputies' who get access to chosen sections.
- **How do they differentiate themselves?** Claims to organize all of a person's life details and tell them what to do next, using a smart planning system.
- **What do they do well?** Not enough caregiver evidence to answer. Only 1 caregiving review: a child said a late father's notes made settling his estate easier.
- **What do they not do well?** Not enough caregiver evidence to answer. Non-caregiver reviews (people planning their own affairs) mostly say the iPad app is only a phone-size version (5 of 7).
- **What do customers say about them?** No caregiver voice: 1 of 8 reviews comes from someone acting for another person, and none on Reddit. It's used to plan your own affairs, or after a death, not during ongoing care.
- **What market gaps have they NOT filled?** It depends on the parent organizing everything ahead of time. Reddit shows the opposite: passwords lost, codes going to the parent's phone, banks rejecting POAs (132 and 97 posts). Nothing for daily coordination, medications or safety.
- **What's their unique value proposition?** Keep every important document and decision of your life in one safe place you can share with the people who will need it.
- **What is their business model? How do they make money?** Freemium: free (3 items) or Premium at $99.99 a year, plus deals through financial advisors and partners. Owned by Precoa since October 2024.
- **Who uses it, who pays, and what does it cost?** People organizing their own affairs pay for Premium themselves, or get it through an advisor (who pays then isn't stated). $99.99 a year.
- **How do they retain customers?** The free tier stops at 3 items, and date reminders bring people back. Cancellation terms aren't stated.
- **How do they approach their customer experience?** Self-serve: FAQs, a contact form, articles and checklists. No reviewer evidence on support.
- **Can a second or third relative join with their own login?** Yes. The owner names deputies for chosen sections, sections can open only after death, and household co-administrators get full edit rights. No caregiver evidence.
- **How do they treat health data and consent?** Sensitive data is encrypted and stored with a HIPAA-compliant host, shared only with chosen deputies. The owner deletes the account themselves, but some personal data may be kept.
- **What happens in an emergency or when it fails?** No emergency service. Chosen sections are released after death. It disclaims liability for lost or breached data.
- **What does setup take?** The person fills in their own plan on the web or the app. Time isn't stated.
- **Evidence base and limits** 8 Apple reviews (1 caregiving), no Reddit or forum use. Too thin to judge from reviews. Data: docs/sources/competitive-analysis-2/themes/everplans.json and facts/everplans.json

### Epic MyChart

- **Indirect or Direct?** Direct (access to records)
- **Market Segment** Patient portals with proxy access
- **Website** https://www.mychart.org/
- **Main Features and Capabilities** A patient portal: test results, doctor notes, messages to the doctor, appointments, medications, bills, and 'proxy access' to a family member's chart.
- **How do they differentiate themselves?** Claims scale (over 190 million patients) and one login that pulls care together across several healthcare organizations.
- **What do they do well?** Once a caregiver gets in, it works. They see a loved one's results and notes (13 of 78), keep several family members under one login (12), message the doctor directly (11), track appointments and meds (11), and follow a hospital stay day by day (5).
- **What do they not do well?** Getting in is the problem. Older parents can't or won't use it (11), caregivers have no login of their own so families share the parent's password (7), proxy access is hard to set up (6), the parent's privacy wishes clash with family access (6), and a spouse's login keeps failing (5).
- **What do customers say about them?** Mostly positive once access is set up, with frustration about getting it. The 78 caregiving items come mainly from adult children (42) and spouses (15). 9 are parents of minors, counted separately. It's the competitor caregivers name most on Reddit (36 posts kept).
- **What market gaps have they NOT filled?** It covers one clinic system's records. It doesn't solve banks, insurers or other accounts (132 posts), shares nothing with siblings except by screenshots (3), and doesn't coordinate tasks, safety or caregiver support. Each clinic sets proxy rules, so access is uneven.
- **What's their unique value proposition?** See and manage all your medical information and care in one place.
- **What is their business model? How do they make money?** Not stated on its page. It is licensed by Epic to healthcare organizations, and patients reach it through their provider. Epic's revenue was about $5.7B in FY2024.
- **Who uses it, who pays, and what does it cost?** Patients and their family use it. Healthcare organizations license it. Free to patients, as far as reviews show (no item mentions a price). Caregivers pay the parent's medical bills through it (5).
- **How do they retain customers?** Not stated. Patients don't choose it, their clinic does. Caregivers stay because it becomes essential (4) but feel let down when it matters most (3).
- **How do they approach their customer experience?** Split: care questions go to the clinic, technical questions go to Epic by email. Reviewers say messages and refill requests go unanswered (3), and there is little help when a loved one's account is locked (2).
- **Can a second or third relative join with their own login?** Through 'proxy access' set up by each healthcare organization. Some families get it working (6), but many find it hard (8) or share the parent's password instead (7). Siblings get updates by screenshot (3).
- **How do they treat health data and consent?** The saved page only covers two-step login and scam warnings, and deletion goes through the clinic. Reviewers say the parent's privacy wishes clash with family access (6) and security steps get in caregivers' way (3).
- **What happens in an emergency or when it fails?** Not for emergencies: it tells people to call 911. In urgent moments app messages didn't replace a phone call (4).
- **What does setup take?** The patient creates an account with their clinic's MyChart. Getting caregiver access set up is the hard part (6). Easy day to day once set up (5).
- **Evidence base and limits** 78 caregiving items: 42 Google and Apple reviews and 36 Reddit posts. The Apple reviews cover only one week. Only the home page was saved, so company answers are thin. Data: docs/sources/competitive-analysis-2/themes/mychart.json and facts/mychart.json

### Lively

- **Indirect or Direct?** Direct (monitoring and safety)
- **Market Segment** Remote monitoring and medical alert
- **Website** https://www.lively.com/
- **Main Features and Capabilities** Jitterbug senior phones and a medical alert device with a 24/7 urgent-response button, optional fall detection, nurses on call, and the Lively Link app that lets family see alerts and location.
- **How do they differentiate themselves?** Claims its people set it apart: 100% US-based agents, nurses on call and ride booking, on easy senior phones with no long-term contract.
- **What do they do well?** When it works, it reassures the family (25 of 193). They can see where the person is (23), the button reaches a quick, helpful operator (15), low-battery alerts let family remind the person to charge (11), and the phone is simple enough for the older person (7).
- **What do they not do well?** The family app is unreliable. Location is wrong or stale (58), support is slow or can't fix it (40), sign-in fails or the app crashes (37), the device shows as off when it's on (28), and alerts to family come late or never (27). Linking family is confusing (13), and people pay for a service that doesn't work with no refund (11).
- **What do customers say about them?** Mostly negative about the family app, positive about the operators. Buyers are adult children far away (12) and spouses (9), often for dementia (8). 14 say they're leaving because it's unreliable. Most reviews are from 2015 to 2020, with location and notification bugs again in 2024-26.
- **What market gaps have they NOT filled?** It watches one person's safety. The family side, being told reliably and fast, is where it fails (27). Families want alerts to reach them, not only a dispatcher (Reddit, 59 safety posts). Nothing for sharing tasks, accounts, papers or records (187, 132, 97, 67).
- **What's their unique value proposition?** Older adults stay independent and protected with easy phones and one-button help, while family feels reassured.
- **What is their business model? How do they make money?** Device plus monthly service plans and add-ons, plus a $99 a year caregiver bundle of partner services. Part of Best Buy Health (Best Buy bought it for $800M in 2018).
- **Who uses it, who pays, and what does it cost?** The older adult wears or carries it. Adult children or spouses usually buy it and hold the account (5). Alert device $89.99, plans $24.99 or $34.99 a month, fall detection +$9.99 a month. Reviewers split: good value (6) versus paying for something that fails (11).
- **How do they retain customers?** Monthly plans with no long-term contract, plus an auto-renewing caregiver bundle. Reviewers who stay do so for one key reason despite problems (6). 14 are leaving, and cancelling is hard (3).
- **How do they approach their customer experience?** Phone-first human support: US agents 24/7, Nurse On-Call, care advocates, stores. Reviewers split: friendly support (7) versus slow or unable to fix the problem (40), with replies taking days or weeks (10).
- **Can a second or third relative join with their own login?** Yes. The owner invites family to Lively Link, and they get alerts and location. Several relatives often follow one person (10), but linking is confusing (13), and following two people in one app is hard (2).
- **How do they treat health data and consent?** Barely stated: family see location when an alert fires, and the privacy policy wasn't saved. Reviewers raise privacy worries (4), and more often lose trust in it with a loved one's safety (10).
- **What happens in an emergency or when it fails?** The button reaches US agents 24/7 who send help or call a caregiver. Fall detection is a paid add-on. Reviewers: quick, helpful operator (15), but emergencies handled badly or family not told (10), and missed falls (4).
- **What does setup take?** Buy online or in a store, activate and pick a plan, then family install the app on their phones. Reviewers say it's hard for the older person (13), linking is confusing (13), and fixes need reboots the older person can't do (9).
- **Evidence base and limits** 193 caregiving items, mostly reviews of the Lively Link family app (177 reviews: 112 Apple, 65 Google), plus 15 Reddit posts and 1 forum thread describing real use. Many complaints repeat the same app versions. Data: docs/sources/competitive-analysis-2/themes/lively.json and facts/lively.json

### Medical Guardian

- **Indirect or Direct?** Direct (monitoring and safety)
- **Market Segment** Remote monitoring and medical alert
- **Website** https://www.medicalguardian.com/
- **Main Features and Capabilities** Medical alert devices for home and on the go, with a 24/7 monitoring center, GPS, optional fall detection, and the MyMedicalGuardian family app.
- **How do they differentiate themselves?** Claims to be faster and more personal than calling 911 because the center already knows who and where you are. Also its lightest device, with 5-day battery, and an AARP 'Best Overall' award.
- **What do they do well?** Help comes fast when the button is pressed (5 of 52), families get peace of mind and the parent more independence (5), and checking on a parent from your phone is the main reason to buy (7).
- **What do they not do well?** The family app fails. It won't sign in or errors (16), steps, battery and location are wrong (9), support gives different answers or long waits (7), fall detection misses falls or false-alarms (7), and family isn't told when something happens (6). Parents stop wearing it (5), and there are extra fees and hard refunds (5).
- **What do customers say about them?** Mostly negative about the family app (39 of 52 items are app reviews, mostly 1-star, 2024-25 after a forced update). Positive about the button itself. Buyers are adult children watching from afar (10). 8 cancel, return or plan to leave.
- **What market gaps have they NOT filled?** Family appear only as emergency contacts. There's no real family login on its pages, and the app that exists is unreliable. Families can't trust the data shown (9). Nothing for sharing care work, accounts, papers or records (187, 132, 97, 67).
- **What's their unique value proposition?** One button gets you to a 24/7 monitoring center that sends the right help fast, at home or on the go.
- **What is their business model? How do they make money?** Devices with ongoing (often yearly) monitoring subscriptions, with the device often free with a promo. Also sold through dealers, health plans and senior living. No funding figure found.
- **Who uses it, who pays, and what does it cost?** The older adult wears it, and adult children usually arrange it (10). About $1 a day. Some insurance may cover it. Reviewers report $400 a year, $80 a month for two devices, and $120 a year extra for fall detection (3).
- **How do they retain customers?** Ongoing subscriptions with possible cancellation fees. Reviewers cancel, return or plan to leave (8), and parents stop wearing it (5).
- **How do they approach their customer experience?** A 24/7 US monitoring center, a member support line and sales consultants. Reviewers say support gives different answers, long waits or rudeness (7).
- **Can a second or third relative join with their own login?** Not described on its pages: family are emergency contacts only. Reviewers say several relatives get called after an alert (2), but app access is uneven or gets lost (2).
- **How do they treat health data and consent?** Only marketing consent is stated (AI chat, recorded calls, texts). The privacy policy wasn't saved. Reviewers mostly say they can't trust the data shown (9). No reviewer raises privacy.
- **What happens in an emergency or when it fails?** The button reaches a 24/7 US center that sends EMS or a contact. The company warns fall detection doesn't always work. Reviewers: fast help (5), but the response failed or was slow in a real emergency (4).
- **What does setup take?** Order by phone or online, free activation, worn on the neck or wrist. Reviewers say the family app won't sign in (16) and setup fails to connect or save (5).
- **Evidence base and limits** 52 caregiving items: 39 app reviews and 13 Reddit or forum posts. Rival-brand ads were removed. The saved pricing page is really the home page. Data: docs/sources/competitive-analysis-2/themes/medical-guardian.json and facts/medical-guardian.json

### Group texts

- **Indirect or Direct?** Indirect (what families use instead)
- **Market Segment** Workaround, not a company
- **Website** n/a
- **Main Features and Capabilities** Family group chats, group texts and WhatsApp groups used to share news and ask for help.
- **How do they differentiate themselves?** Not a company. Everyone already has it, it's free, and there's nothing to install.
- **What do they do well?** One place to tell the whole family what's happening (6 of 53), a quick way to ask someone to cover a shift (3), and 'works well enough' until care gets complicated (2).
- **What do they not do well?** Requests and updates get silence or just a 'like' (10), and important details get buried, causing missed appointments and near double doses (10). Relatives use the chat to judge the caregiver (8), and constant messages wear the caregiver down (7). It's not dependable in an emergency (3).
- **What do customers say about them?** Mostly frustration: 53 caregiver posts on Reddit, and most describe the chat failing or causing conflict. The main caregiver does most of the posting (4). Being in the chat doesn't mean helping (7).
- **What market gaps have they NOT filled?** Turning messages into shared, tracked tasks, and getting siblings to act, not just read (187 posts on sharing work, 217 on doing it alone). No place for medication changes, papers or account access.
- **What's their unique value proposition?** Not a company.
- **What is their business model? How do they make money?** Not a company. Free.
- **Who uses it, who pays, and what does it cost?** The main family caregiver, relatives, and also paid care staff and agencies (6). Free.
- **How do they retain customers?** Not a company. Caregivers mute, leave or refuse group chats to protect themselves (4).
- **How do they approach their customer experience?** Not a company.
- **Can a second or third relative join with their own login?** Anyone can be added, but getting everyone onto one app is hard (2), and side chats leave people out (2).
- **How do they treat health data and consent?** No controls. Private things end up in the wrong chat (2).
- **What happens in an emergency or when it fails?** Not dependable when something urgent happens (3). Alarming news arrives with no warning (2).
- **What does setup take?** Nothing new to install, but getting everyone onto one app is hard (2). Families add shared calendars, docs and notes next to it (6).
- **Evidence base and limits** 53 caregiver Reddit posts (of 189 naming a chat). Venting posts over-represent conflict. 44 app-maker posts removed. Data: docs/sources/competitive-analysis-2/themes/group-texts.json

### Paper notebook and visit log

- **Indirect or Direct?** Indirect (what families use instead)
- **Market Segment** Workaround, not a company
- **Website** n/a
- **Main Features and Capabilities** Notebooks, binders, whiteboards, wall calendars and home visit logs for meds, appointments, papers and notes.
- **How do they differentiate themselves?** Not a company. It needs no phone, and anyone, including nurses and the parent, can write in it.
- **What do they do well?** A whiteboard with the date and schedule calms repeated questions from someone with memory loss (6 of 51). A notebook carried to every appointment helps (5), a written guide lets someone else step in (4), paper is ready to grab in an emergency (4), and it works without phones (4).
- **What do they not do well?** Notes and calendars get ignored, lost or erased (12), records pile up and can't be searched when a doctor asks (7), and the paper stays with one person so family miss changes (6), including a near double dose of heart medicine. Old money and ID papers take weeks to sort (4), and logs can be faked or disputed (3).
- **What do customers say about them?** Families like it for simple, in-home use but outgrow it. Six posts want something digital once paper stops coping. The main caregiver usually keeps it alone (4), and paid aides write in a shared home log (4).
- **What market gaps have they NOT filled?** Sharing with family who aren't in the house, and finding records quickly (67 records posts, 97 papers posts). Paper can't reach siblings, can't alert anyone, and doesn't help with accounts or POA.
- **What's their unique value proposition?** Not a company.
- **What is their business model? How do they make money?** Not a company. Cheap to start, but store-bought planners can disappoint (4).
- **Who uses it, who pays, and what does it cost?** The main caregiver, paid aides and the person being cared for. Nearly free.
- **How do they retain customers?** Not a company. Families stay with paper because it needs no phone (2), and move to digital when it gets too big (6).
- **How do they approach their customer experience?** Not a company.
- **Can a second or third relative join with their own login?** No. The paper stays with one person (6). A binder can be handed to a stand-in caregiver (3).
- **How do they treat health data and consent?** No controls. Handwritten logs can be faked or disputed (3).
- **What happens in an emergency or when it fails?** Paper ready for the hospital helps in a crisis (3), but families worry it won't be at hand (2).
- **What does setup take?** Quick: people hunt for a ready-made care binder or make their own (5). It's usually used next to digital calendars, chats and photos (11).
- **Evidence base and limits** 51 caregiver Reddit posts (of 136 naming paper tools). 24 logbook or app promotions removed. Some posts describe a plan rather than long use. Data: docs/sources/competitive-analysis-2/themes/paper-notebook.json

## GAPS IN THE MARKET AND IN COMPETITOR OFFERINGS, version 2 (2026-11-04)

Synthesized from 577 caregiving reviews and posts about the 10 competitors in the table, plus 825 caregiver posts on Reddit. (Lively 58) means 58 Lively items say it. (Reddit 132) means 132 Reddit caregiver posts.

**1. Nobody gets the rest of the family to actually help.** It's the biggest caregiver problem: doing it alone (Reddit 217), and siblings won't share the work (Reddit 63). Competitors share information, not work. CaringBridge is praised because one update reaches everyone (CaringBridge 49), but it isn't built for day-to-day coordination (CaringBridge 3). In group chats, requests get silence or a 'like' (Group texts 10), and being in the chat doesn't mean helping (Group texts 7). Only small signs of relatives taking on tasks exist: Lotsa sign-ups (Lotsa 3) and asking someone to cover a shift (Group texts 3).

**2. Relatives can't get their own way into the parent's accounts.** Reddit shows banks and agencies refusing the caregiver (Reddit 46), lost passwords (Reddit 32) and codes going to the parent's phone (Reddit 22). MyChart works once a caregiver is in (MyChart 13), but there's no caregiver login, so families share the parent's password (MyChart 7), and proxy access is hard to get (MyChart 8). Linking family is confusing on Lively (Lively 13), and sharing breaks between caregivers on Medisafe (Medisafe 4). Everplans needs the parent to set everything up ahead of time, and no caregiver use was found. No competitor covers banks or insurers.

**3. Safety tools work for the older person but fail the family.** The button reaches help (Lively 15, Medical Guardian 5), but the family app fails. Location is wrong or stale (Lively 58), sign-in fails or the app crashes (Lively 37, Medical Guardian 16), and alerts to family come late or never (Lively 27), or family isn't told (Medical Guardian 6). Parents stop wearing the device (Medical Guardian 5) or find it hard to use (Lively 13). Families on Reddit want the alert to reach them, not only a dispatcher (Reddit 59 safety posts).

**4. Information gets lost between people, especially medication changes.** In group chats, details get buried, causing missed appointments and near double doses (Group texts 10). Paper stays with one person, so family miss changes (Paper notebook 6). In Medisafe the caregiver's view goes out of sync (Medisafe 3), and you can't tell whose dose it is (Medisafe 2). On Reddit, medication changes not being shared caused double doses or mix-ups (Reddit 24).

**5. Papers, records and power of attorney have no real home.** On Reddit: POA missing, rejected or delayed (Reddit 29), and papers scattered or lost (Reddit 22). Paper records pile up and can't be found when a doctor asks (Paper notebook 7). MyChart records are hard to share outside the app (MyChart 3), so siblings get screenshots (MyChart 3). Caring Village stores documents (Caring Village 3), but old records can't be kept or found (Caring Village 2). No competitor helps with POA.

**6. No one covers the whole job, so families stitch tools together.** Each row covers one piece: updates, records, medications or safety. Paper is used alongside digital calendars, chats and photos (Paper notebook 11). Group chats run next to shared calendars and docs (Group texts 6). CaringBridge families add group texts and spreadsheets for the daily work (CaringBridge 3).

WHAT THIS DOES NOT SHOW: whether people would pay for any of this. Companies outside these 10. Reviews lean toward strong opinions, and Reddit venting over-represents conflict. Everplans (1 caregiving review) and Lotsa (4 items) are too thin to judge.

FOR THE OWNER TO DECIDE: which of these gaps to be better at than the competitors, and why.

## SUMMARIZE THE UNIQUE VALUE OPPORTUNITIES, version 2 (2026-11-04). Open problems, nothing chosen.

Every number is (Source N). Checked by `audit_gaps_uvo.py` (97 claims, each matched to its theme). Same content as the Figma section `2570:10217` inside Competitive Analysis 2.

| Area | What competitors do well | What competitors do not do well | What our business could do differently (open problem, not a feature) | How strong is the evidence? |
|---|---|---|---|---|
| 1. Getting the family to share the work | Telling everyone at once saves the caregiver time (CaringBridge 49, CaringBridge 19). Keeping the family on the same page (Caring Village 10). Signing up helpers for tasks (Lotsa 3). | They share news, not work. CaringBridge isn't built for daily coordination (CaringBridge 3). Getting everyone to join is hard (Caring Village 2). Requests get silence (Group texts 10), and being in the chat doesn't mean helping (Group texts 7). | Help the main caregiver get relatives to take on and follow through on real tasks, not just read updates. | Strong need: the biggest Reddit theme (Reddit 217). Competitor evidence is thin on tasks. |
| 2. Relatives' own access to the parent's accounts | Once in, a caregiver can see results, message doctors and manage several people (MyChart 13, MyChart 12, MyChart 11). Medisafe lets a relative watch doses (Medisafe 4). | No caregiver login, so families share passwords (MyChart 7). Proxy setup is hard (MyChart 8). Linking is confusing (Lively 13). Sharing breaks between caregivers (Medisafe 4). Banks and insurers aren't covered by anyone (Reddit 46). | Help a relative get and keep their own access to what the parent needs managed, without sharing the parent's login. | Strong: second-largest Reddit theme (Reddit 132), and seen in competitor reviews too. |
| 3. Safety alerts that reach the family | Reassurance (Lively 25), seeing where the person is (Lively 23), and quick help from an operator (Lively 15, Medical Guardian 5). | Wrong location (Lively 58), late or missing alerts to family (Lively 27), sign-in failures (Lively 37, Medical Guardian 16), and parents not wearing it (Medical Guardian 5). | Help the family trust that they'll know quickly and correctly when something happens. | Strong complaints, but a crowded market with device costs. Reddit need is smaller (Reddit 59). |
| 4. Passing on medication changes between caregivers | Keeping one loved one's complicated schedule on track (Medisafe 10), managing several people's meds (Medisafe 5), and paper checklists for in-home helpers (Paper notebook 4). | Changes get buried or stay with one person (Group texts 10, Paper notebook 6). Caregiver views go out of sync (Medisafe 3). You can't tell whose dose it is (Medisafe 2). | Help every caregiver see the same, current medication information, so no dose is missed or doubled. | Medium: a real risk (Reddit 24), but medication apps are crowded. |
| 5. Papers, records and power of attorney | MyChart records are ready to hand to others (MyChart 5). Caring Village stores documents (Caring Village 3). A binder lets a stand-in caregiver step in (Paper notebook 3). | Paper can't be searched (Paper notebook 7). Old records get lost (Caring Village 2). Sharing outside MyChart is hard (MyChart 3). No one helps when a POA is rejected (Reddit 29). | Help the family keep the parent's key papers and records findable and usable when a bank or doctor asks. | Medium to strong need (Reddit 97). No competitor addresses POA. |
| 6. Money and who pays | Easy to start: CaringBridge and Lotsa are free, Caring Village has a free plan, and some find Lively good value (Lively 6). | Paying for a service that doesn't work, with no refunds (Lively 11). Extra fees and hard refunds (Medical Guardian 5). Donation prompts feel pushy (CaringBridge 2). Caring Village's free plan stops at 2 members. | Find out who would pay for family coordination, and how much. Unknown today. | Weak: no evidence on willingness to pay for coordination. |
| 7. Health data and consent | Families trust invite-only spaces (CaringBridge 6). Caring Village and CaringBridge say they don't sell health data. | 'Friends' can see private medical details (Caring Village 2). The parent's privacy wishes clash with family access (MyChart 6). Security steps block caregivers (MyChart 3). Private things end up in the wrong chat (Group texts 2). Medisafe may share data with drug makers. | Let family help while respecting what the parent wants shared. | Medium: more a design risk to plan around than a reason people choose a tool. |
