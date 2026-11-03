# What app-store reviewers say: problems in their own words (2026-11-02)

**Evidence state:** `documented` for every quote (exact text, checked by script against the saved review); `reported` for the category counts (one reader assigned one category per review, so the counts are approximate). Nothing here is a finding about what caregivers would pay for or do.

> **CORRECTION (2026-11-02).** The first version of this file (merged in pull request #20) counted 625 problem reviews from every selected review. Most of those reviews were not about caregiving: the word list also matches words like family, parent and senior in other uses. This version counts only the reviews where the reviewer is clearly caring for or helping a relative (439 reviews, 192 of them describing a problem). Every number below changed; for example, 'wrong readings or location' fell from 144 to 43 and 'price' from 42 to 6.

## How this was made (so you can check it)

1. **Collected:** 9,448 Apple reviews (public review feed, 44 apps, 7 storefronts) and 4,777 Google Play reviews (10 apps, read in Chrome). Saved in `docs/sources/app-reviews/` (`raw/`, `reviews.csv`, `google-play/`). Details and limits: `docs/sources/INDEX.md` section 2p.
2. **Selected:** `analysis/make_slices.py` keeps only reviews whose text or title matches a caregiving or family word list (mom, dad, parent, elderly, caregiver, wife, husband, dementia, loved one, and so on). That is 1,475 of 14,225 reviews. **The other 12,750 were not read for this analysis.**
3. **Read:** reader agents read the selected reviews and gave each one a kind (problem, worked, none), one problem category, who the reviewer cares for, and one exact quote.
3b. **Filtered to caregiving only:** the 1,386 reviews that describe a problem or something that worked were checked one by one (`analysis/verify_relevance.py`, then a blind full-text recheck of 539, then my reading of the 84 upgrade candidates; the result is `analysis/relevance-final.json`). A review counts as caregiving only if it contains an exact quote showing the reviewer is caring for or helping a relative; if in doubt it is left out. Result: **439 caregiving reviews**, 668 not caregiving, 279 unclear. **Everything below counts only the 439.**
4. **Checked:** `analysis/verify_tags.py` accepted a quote only if it is an exact substring of the review's text or title. Result: 439 quotes verified, 0 dropped. Every id is in `analysis/all-reviews.jsonl` (`../all-reviews.jsonl`) with its app, store, stars and date; Apple ids `a-N` are row N (from 0) of `reviews.csv`, Google ids `g-<app>-N` are item N (from 0) in that app's JSON file.

## What was read

- 439 reviews: **192 describe a problem**, 247 describe something that worked, 0 had no usable content.
- **Who the problem reviewers care for** (as stated): parent 111, not stated 26, other relative 24, self 14, spouse 9, child 7, client 1. So 152 of the 192 problem reviews are about a parent, spouse or other relative. Whether that person is old or ill is often not stated, so this is not the same as 'caring for an older or ill relative'. 7 are about a child, 14 about the reviewer themselves, 26 do not say.

## Problems by category

| Problem | All problem reviews | About a parent, spouse or other relative | Apple | Google Play |
|---|---|---|---|---|
| Readings, location or detection wrong, false alarms, missed events | 43 | 37 | 38 | 5 |
| Crashes, bugs, battery, connectivity in general | 42 | 31 | 34 | 8 |
| A person in danger and the tool did not help (falls, wandering, emergencies) | 19 | 19 | 14 | 5 |
| Other problem | 15 | 11 | 12 | 3 |
| Getting access, accounts, logins or permissions for another person | 14 | 9 | 9 | 5 |
| Alerts or notifications missed, late, too many or not arriving | 14 | 13 | 13 | 1 |
| The older person cannot or will not use it | 10 | 8 | 9 | 1 |
| Relatives or helpers cannot see the same information | 7 | 5 | 5 | 2 |
| Setup, pairing or phone compatibility trouble | 6 | 5 | 6 | 0 |
| Price, subscription, paywall, billing | 6 | 4 | 4 | 2 |
| Data does not sync between devices or people | 6 | 4 | 4 | 2 |
| Company or support did not help | 5 | 3 | 4 | 1 |
| Reminders or schedules (medication, appointments) failing | 3 | 1 | 0 | 3 |
| Privacy, tracking or trust worries | 2 | 2 | 2 | 0 |
| **Total** | **192** | **152** | **154** | **38** |

## Quotes by problem (up to 4 per category, chosen by script: relatives first, longer quotes, one per app)

### Readings, location or detection wrong, false alarms, missed events (43)

- "This app is not accurate and does not allow me to keep up with my elderly father via smartphone." (lively-link, apple, 1 stars, 2018-10-02; who: parent; id `a-7601`)
- "I am concerned that the device will not perform as advertised when there is an actual emergency." (MyMedicalGuardian, google, 1 stars, December 19, 2024; who: parent; id `g-mymedicalguardian-0`)

### Crashes, bugs, battery, connectivity in general (42)

- "I am unable to add any photos or write a journal without issues with the cursor moving downward on the page on its own." (CaringBridge, google, 2 stars, November 22, 2022; who: other relative; id `g-caringbridge-28`)
- "they leave us blinded to their status while they try to make the new one work." (mymedicalguardian, apple, 1 stars, 2025-04-18; who: other relative; id `a-3248`)
- "since the last update, I noticed that all my groceries categories are gone" (familywall, apple, 5 stars, 2023-06-24; who: parent; id `a-5544`)
- "Very frustrating to keep track of my Mother when the app doesn’t work." (honor-family, apple, 2 stars, 2023-06-02; who: parent; id `b-0`)

### A person in danger and the tool did not help (falls, wandering, emergencies) (19)

- "He lay outside injured and unable to move for over an hour before a stranger found him." (lively-link, apple, 1 stars, 2019-03-17; who: parent; id `a-7567`)
- "when my mom went missing (which is exactly ehen I needed it), it failed to work!!" (MyMedicalGuardian, google, 1 stars, July 28, 2022; who: parent; id `g-mymedicalguardian-61`)
- "My mother had several falls as an elderly obese person that were not registered." (apple-watch-app, apple, 3 stars, 2026-01-30; who: parent; id `a-1164`)

### Other problem (15)

- "we kids just want to be able to remotely see and record his weight over time, to report to his doctor" (Withings, google, 2 stars, July 19, 2026; who: parent; id `g-withings-6`)
- "The app has no appointment tracking capabilities and the note taking functionality is dismal." (tendercare, apple, 3 stars, 2026-07-17; who: parent; id `a-3283`)
- "I have to have the cardwindow placed just slightly too far away to read her face properly" (carewindow, apple, 5 stars, 2026-03-13; who: parent; id `a-13`)
- "We miss the update that used to show why Great Link was called and why." (lively-link, apple, 3 stars, 2018-08-12; who: parent; id `a-7610`)

### Getting access, accounts, logins or permissions for another person (14)

- "An email invite had to be sent to an address not connected already with the device." (lively-link, apple, 5 stars, 2024-05-31; who: spouse; id `a-7458`)
- "So many of my over 60 relatives have been not able to reaccess their account." (caringbridge, apple, 2 stars, 2024-07-19; who: parent; id `a-3525`)
- "Log in as my MIL to see myself and my husband were removed as portal members" (mymedicalguardian, apple, 1 stars, 2025-08-07; who: other relative; id `a-3227`)
- "When it is successful, they only get notified when I skip medicine, not when I take it." (Medisafe, google, 2 stars, March 29, 2023; who: self; id `g-medisafe-52`)

### Alerts or notifications missed, late, too many or not arriving (14)

- "My phone just lit up three times with a push notification saying that my sister was having a seizure and that no one had responded." (seizure-alert-my-medic-watch, apple, 2 stars, 2019-04-16; who: other relative; id `a-3160`)
- "Sometimes it alerts at 45 minutes past the time, sometimes it alerts at 2 hours" (medisafe, apple, 4 stars, 2025-12-05; who: other relative; id `a-6294`)
- "my mom would tell me she had gone shopping yet the app never notified me" (lively-link, apple, 3 stars, 2016-01-24; who: parent; id `a-7795`)

### The older person cannot or will not use it (10)

- "Dementia patients and other mentally impaired patients could get confused." (medisafe, apple, 4 stars, 2024-12-22; who: spouse; id `a-6522`)
- "What old person is going to remember to turn on their ball detection every single day." (fallcall-detect, apple, 1 stars, 2022-02-20; who: not stated; id `a-3202`)

### Relatives or helpers cannot see the same information (7)

- "I am handicapped and need to use an app that allows my caregivers total access to calendar, lists, notes, medications, etc." (familywall, apple, 3 stars, 2025-12-11; who: self; id `a-5318`)

### Setup, pairing or phone compatibility trouble (6)

- "It works with Samsung phones, but it does not work with iPhones for some reason." (lively-link, apple, 2 stars, 2025-04-17; who: parent; id `a-7453`)
- "I bought my mom the new google pixel watch because she has panic attacks" (wear-os, apple, 1 stars, 2025-07-10; who: parent; id `a-8963`)

### Price, subscription, paywall, billing (6)

- "Paying for 3 circles seems unnecessary and is the only negative I have." (life360, apple, 4 stars, 2026-10-19; who: parent; id `a-3678`)
- "it continues to state that we need to donate to caring bridge again, and that no one from her page has donated." (caringbridge, apple, 1 stars, 2026-09-13; who: not stated; id `a-3296`)

### Data does not sync between devices or people (6)

- "multiple medications of hers stopped showing up on my app, but not hers" (medisafe, apple, 1 stars, 2025-10-22; who: spouse; id `a-6307`)
- "This has left me vulnerable for caregivers not showing up to care for me because the calendar did not show a change that another caregiver had entered." (familywall, apple, 1 stars, 2024-02-23; who: self; id `a-5519`)

### Company or support did not help (5)


### Reminders or schedules (medication, appointments) failing (3)

- "First, weirdly, I would only get the notifications if I were connected to my PC at the time, then they stopped all together." (Medisafe, google, 1 stars, December 12, 2024; who: self; id `g-medisafe-338`)

### Privacy, tracking or trust worries (2)


## Which apps the problems come from (the app choice shapes the counts)

- **Readings, location or detection wrong, false alarms, missed events** (43): lively-link 33, mymedicalguardian 9, seizure-alert-my-medic-watch 1
- **A person in danger and the tool did not help (falls, wandering, emergencies)** (19): lively-link 13, mymedicalguardian 5, apple-watch-app 1
- **Getting access, accounts, logins or permissions for another person** (14): caringbridge 4, mymedicalguardian 3, lively-link 3, ask-annie-dementia-australia 1, caring-village 1
- **Relatives or helpers cannot see the same information** (7): medisafe 4, familywall 2, careapp 1

## Limits

- **Selection:** only apps I chose (family coordination, medication, safety, watches, blood pressure, international). Only reviews matching the word list were read. Reviewers are people who use an app and chose to write.
- **Samples:** Apple is the most recent written reviews (up to 500 per app); Google Play is in the page's default order, about 540 per app, not random; the share of 1 and 2 star reviews varies a lot by app.
- **Coding:** one reader per slice, one category per review, so a review with two problems counts once. Some categories are judgement calls (the readers listed examples). A different reader could code some differently.
- **What this cannot show:** who would pay, what people would do, or needs outside these apps. It shows problems people describe about tools they already use.
- **Not done:** the reviews outside the word list. The word list is English only, so reviews in other languages (for example the Japanese and German storefronts) were not selected.
