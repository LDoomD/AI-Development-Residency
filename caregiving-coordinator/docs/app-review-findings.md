# What app-store reviewers say: problems in their own words (2026-11-02)

**Evidence state:** `documented` for every quote (exact text, checked by script against the saved review); `reported` for the category counts (one reader assigned one category per review, so the counts are approximate). Nothing here is a finding about what caregivers would pay for or do.

## How this was made (so you can check it)

1. **Collected:** 9,448 Apple reviews (public review feed, 44 apps, 7 storefronts) and 4,777 Google Play reviews (10 apps, read in Chrome). Saved in `docs/sources/app-reviews/` (`raw/`, `reviews.csv`, `google-play/`). Details and limits: `docs/sources/INDEX.md` section 2p.
2. **Selected:** `analysis/make_slices.py` keeps only reviews whose text or title matches a caregiving or family word list (mom, dad, parent, elderly, caregiver, wife, husband, dementia, loved one, and so on). That is 1,475 of 14,225 reviews. **The other 12,750 were not read for this analysis.**
3. **Read:** four reader agents read all 1,475 selected reviews and gave each one a kind (problem, worked, none), one problem category, who the reviewer cares for, and one exact quote.
4. **Checked:** `analysis/verify_tags.py` accepted a quote only if it is an exact substring of the review's text or title. Result: 1,312 quotes verified, 0 dropped. Every id is in `analysis/all-reviews.jsonl` (`../all-reviews.jsonl`) with its app, store, stars and date; Apple ids `a-N` are row N (from 0) of `reviews.csv`, Google ids `g-<app>-N` are item N (from 0) in that app's JSON file.

## What was read

- 1,475 reviews: **625 describe a problem**, 687 describe something that worked, 163 had no usable content.
- **Who the problem reviewers care for** (as stated): parent 187, not stated 132, other relative 105, spouse 92, child 62, self 45, client 2. So 384 of the 625 problem reviews are about a parent, spouse or other relative. Whether that person is old or ill is often not stated, so this is not the same as 'caring for an older or ill relative'. 62 are about a child, 45 about the reviewer themselves, 132 do not say.

## Problems by category

| Problem | All problem reviews | About a parent, spouse or other relative | Apple | Google Play |
|---|---|---|---|---|
| Readings, location or detection wrong, false alarms, missed events | 144 | 112 | 95 | 49 |
| Crashes, bugs, battery, connectivity in general | 129 | 81 | 101 | 28 |
| Other problem | 88 | 40 | 69 | 19 |
| Alerts or notifications missed, late, too many or not arriving | 48 | 31 | 35 | 13 |
| Price, subscription, paywall, billing | 42 | 15 | 36 | 6 |
| A person in danger and the tool did not help (falls, wandering, emergencies) | 33 | 24 | 21 | 12 |
| Getting access, accounts, logins or permissions for another person | 30 | 21 | 21 | 9 |
| Setup, pairing or phone compatibility trouble | 29 | 15 | 26 | 3 |
| Data does not sync between devices or people | 19 | 15 | 13 | 6 |
| Relatives or helpers cannot see the same information | 18 | 9 | 9 | 9 |
| The older person cannot or will not use it | 12 | 9 | 11 | 1 |
| Company or support did not help | 12 | 6 | 10 | 2 |
| Privacy, tracking or trust worries | 12 | 5 | 8 | 4 |
| Reminders or schedules (medication, appointments) failing | 9 | 1 | 5 | 4 |
| **Total** | **625** | **384** | **460** | **165** |

## Quotes by problem (up to 4 per category, chosen by script: relatives first, longer quotes, one per app)

### Readings, location or detection wrong, false alarms, missed events (144)

- "It will say that my mom left our house in the middle of the night even though I know shes sleeping in the next room over." (Life360, google, 3 stars, July 2, 2026; who: parent; id `g-life360-494`)
- "The message also give bad locations some time up to ten miles away when she is sitting in her house." (lively-link, apple, 3 stars, 2015-12-21; who: parent; id `a-7800`)
- "my husband who obviously has sleep apnea will cause earthquakes through the night with his snoring" (google-health-fitbit, apple, 2 stars, 2026-10-14; who: spouse; id `a-4924`)
- "I am concerned that the device will not perform as advertised when there is an actual emergency." (MyMedicalGuardian, google, 1 stars, December 19, 2024; who: parent; id `g-mymedicalguardian-0`)

### Crashes, bugs, battery, connectivity in general (129)

- "My only gripes are that it has difficulty connecting when attempting to add a contact OR opening contacts causes a crash." (familywall, apple, 4 stars, 2024-10-15; who: other relative; id `a-5476`)
- "I am unable to add any photos or write a journal without issues with the cursor moving downward on the page on its own." (CaringBridge, google, 2 stars, November 22, 2022; who: other relative; id `g-caringbridge-28`)
- "They constantly pop up and completely cover the current location box of family members." (Life360, google, 2 stars, July 21, 2026; who: other relative; id `g-life360-92`)
- "they leave us blinded to their status while they try to make the new one work." (mymedicalguardian, apple, 1 stars, 2025-04-18; who: other relative; id `a-3248`)

### Other problem (88)

- "now we have to delete on the machine all readings prior to taking measurements to avoid her readings on my phone and vice versa" (OMRON connect, google, 4 stars, September 13, 2026; who: spouse; id `g-omron-connect-328`)
- "we kids just want to be able to remotely see and record his weight over time, to report to his doctor" (Withings, google, 2 stars, July 19, 2026; who: parent; id `g-withings-6`)
- "The app has no appointment tracking capabilities and the note taking functionality is dismal." (tendercare, apple, 3 stars, 2026-07-17; who: parent; id `a-3283`)
- "I have to have the cardwindow placed just slightly too far away to read her face properly" (carewindow, apple, 5 stars, 2026-03-13; who: parent; id `a-13`)

### Alerts or notifications missed, late, too many or not arriving (48)

- "My phone just lit up three times with a push notification saying that my sister was having a seizure and that no one had responded." (seizure-alert-my-medic-watch, apple, 2 stars, 2019-04-16; who: other relative; id `a-3160`)
- "Sometimes it alerts at 45 minutes past the time, sometimes it alerts at 2 hours" (medisafe, apple, 4 stars, 2025-12-05; who: other relative; id `a-6294`)
- "I still get several notifications regarding the features and premium benefits." (Life360, google, 1 stars, July 20, 2026; who: other relative; id `g-life360-324`)
- "It mostly features changes I have made but not my husband or family members." (familywall, apple, 4 stars, 2026-08-26; who: spouse; id `a-5136`)

### Price, subscription, paywall, billing (42)

- "the paywall for new users to auto-import to the Apple Health app prompted me to dissuade my family member from buying a Withings scale" (withings, apple, 1 stars, 2026-10-13; who: other relative; id `a-5887`)
- "I am extremely disappointed to learn that Caring Bridge is trying to raise money from my husband" (caringbridge, apple, 1 stars, 2025-08-25; who: spouse; id `a-3344`)
- "The more activity a family member has in a day, the less amount of days I see!" (Life360, google, 1 stars, April 28, 2026; who: other relative; id `g-life360-122`)
- "they want you to sign/buy an additional care package to just obtain a copy of your own EKG" (kardia, apple, 1 stars, 2026-05-31; who: self; id `a-6880`)

### A person in danger and the tool did not help (falls, wandering, emergencies) (33)

- "He lay outside injured and unable to move for over an hour before a stranger found him." (lively-link, apple, 1 stars, 2019-03-17; who: parent; id `a-7567`)
- "when my mom went missing (which is exactly ehen I needed it), it failed to work!!" (MyMedicalGuardian, google, 1 stars, July 28, 2022; who: parent; id `g-mymedicalguardian-61`)
- "My mother had several falls as an elderly obese person that were not registered." (apple-watch-app, apple, 3 stars, 2026-01-30; who: parent; id `a-1164`)
- "neither of our Life360 alerted anyone and we both have crash detection on" (Life360, google, 3 stars, July 12, 2026; who: spouse; id `g-life360-265`)

### Getting access, accounts, logins or permissions for another person (30)

- "Others in groups actively following the same pages that I am cannot even access CaringBridge (e.g., cannot log on)" (caringbridge, apple, 3 stars, 2024-08-10; who: other relative; id `a-3493`)
- "An email invite had to be sent to an address not connected already with the device." (lively-link, apple, 5 stars, 2024-05-31; who: spouse; id `a-7458`)
- "Log in as my MIL to see myself and my husband were removed as portal members" (mymedicalguardian, apple, 1 stars, 2025-08-07; who: other relative; id `a-3227`)
- "My mom now blames me for constantly missing events and not knowing addresses" (cozi, apple, 1 stars, 2026-08-14; who: parent; id `a-4241`)

### Setup, pairing or phone compatibility trouble (29)

- "when my wife invited me it said I am on an iPhone and not allowed to participate." (samsung-health, apple, 1 stars, 2024-01-04; who: spouse; id `a-2829`)
- "It works with Samsung phones, but it does not work with iPhones for some reason." (lively-link, apple, 2 stars, 2025-04-17; who: parent; id `a-7453`)
- "I bought my mom the new google pixel watch because she has panic attacks" (wear-os, apple, 1 stars, 2025-07-10; who: parent; id `a-8963`)
- "Following the directions step-by-step were not helpful at all for me, & I gave up." (OMRON connect, google, 2 stars, October 1, 2022; who: not stated; id `g-omron-connect-103`)

### Data does not sync between devices or people (19)

- "This calendar app constantly unsyncs itself and my wife and I have to manually update almost daily to ensure our calendars match." (timetree, apple, 1 stars, 2026-09-08; who: spouse; id `a-8489`)
- "if i try and share things from my apple calendar, it will only show on my phone and not my family members phones" (familywall, apple, 5 stars, 2026-01-01; who: other relative; id `a-5311`)
- "I will add something and it will vanish when my husband refreshes his list" (cozi, apple, 1 stars, 2026-04-20; who: spouse; id `a-4392`)
- "multiple medications of hers stopped showing up on my app, but not hers" (medisafe, apple, 1 stars, 2025-10-22; who: spouse; id `a-6307`)

### Relatives or helpers cannot see the same information (18)

- "I am handicapped and need to use an app that allows my caregivers total access to calendar, lists, notes, medications, etc." (familywall, apple, 3 stars, 2025-12-11; who: self; id `a-5318`)
- "Wish the calendar appts would go to everyone in inner circles category instead of only to the person assigned." (caring-village, apple, 2 stars, 2023-04-06; who: not stated; id `a-1381`)
- "none of my family or friends can see any of the posts from both Facebook and at the website either" (caringbridge, apple, 2 stars, 2024-07-04; who: not stated; id `a-3565`)
- "Notifications only work for one family member (the first one to have access)." (lively-link, apple, 1 stars, 2025-08-16; who: not stated; id `a-7451`)

### The older person cannot or will not use it (12)

- "Mom cannot see charge light so she cannot tell if the unit is fully charged." (lively-link, apple, 2 stars, 2018-05-11; who: parent; id `a-7628`)
- "Dementia patients and other mentally impaired patients could get confused." (medisafe, apple, 4 stars, 2024-12-22; who: spouse; id `a-6522`)
- "What old person is going to remember to turn on their ball detection every single day." (fallcall-detect, apple, 1 stars, 2022-02-20; who: not stated; id `a-3202`)

### Company or support did not help (12)

- "Spent over an hour on hold and 4 people refused to just close the account." (MyMedicalGuardian, google, 1 stars, June 11, 2024; who: other relative; id `g-mymedicalguardian-23`)
- "So obviously the next step is to call but they will NEVER answer the phone and you have to leave a message." (snug, apple, 5 stars, 2024-12-12; who: self; id `a-2051`)

### Privacy, tracking or trust worries (12)

- "constant tracking can sometimes feel more like surveillance than protection" (Life360, google, 5 stars, August 11, 2026; who: other relative; id `g-life360-368`)

### Reminders or schedules (medication, appointments) failing (9)

- "First, weirdly, I would only get the notifications if I were connected to my PC at the time, then they stopped all together." (Medisafe, google, 1 stars, December 12, 2024; who: self; id `g-medisafe-338`)

## Which apps the problems come from (the app choice shapes the counts)

- **Readings, location or detection wrong, false alarms, missed events** (144): lively-link 67, life360 50, mymedicalguardian 11, withings 7, familywall 3
- **A person in danger and the tool did not help (falls, wandering, emergencies)** (33): lively-link 14, life360 12, mymedicalguardian 5, apple-watch-app 1, fallcall-detect 1
- **Getting access, accounts, logins or permissions for another person** (30): mymedicalguardian 6, caringbridge 5, withings 5, familywall 4, lively-link 3
- **Relatives or helpers cannot see the same information** (18): medisafe 4, mytherapy 4, familywall 3, withings 3, careapp 1

## Limits

- **Selection:** only apps I chose (family coordination, medication, safety, watches, blood pressure, international). Only reviews matching the word list were read. Reviewers are people who use an app and chose to write.
- **Samples:** Apple is the most recent written reviews (up to 500 per app); Google Play is in the page's default order, about 540 per app, not random; the share of 1 and 2 star reviews varies a lot by app.
- **Coding:** one reader per slice, one category per review, so a review with two problems counts once. Some categories are judgement calls (the readers listed examples). A different reader could code some differently.
- **What this cannot show:** who would pay, what people would do, or needs outside these apps. It shows problems people describe about tools they already use.
- **Not done:** the reviews outside the word list. The word list is English only, so reviews in other languages (for example the Japanese and German storefronts) were not selected.
