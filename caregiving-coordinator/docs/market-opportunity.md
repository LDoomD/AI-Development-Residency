# Market opportunity

Written 2026-11-01. Template text: "Market opportunity is the chance a business has to make money by meeting a need or solving a problem that isn't being fully taken care of yet... If you find a segment that's big enough and doesn't have too many competitors, that's a good sign... What market segment has the largest opportunity? Why?"

Method: the teacher's rule has three tests: (1) big enough, (2) not too many competitors, (3) a need that isn't being met. Evidence comes from `docs/market-research-prompt2-results.md` (size, competitors) and `docs/qualitative-research-findings.md` (what caregivers say). No new research was done for this step. Claims carry an evidence state from the `skeptical-audit` skill.

## Segment-by-segment against the three tests

| Segment | Big enough? | Few competitors? | Unmet need? | Verdict |
|---|---|---|---|---|
| 1 Family care-coordination apps | Medium: $1.3B to $4B for all caregiver apps (5 reports, `reported`, scope includes professional caregiver apps) | Yes: 3 named players, with 2 built for broadcasting updates or volunteer sign-ups (`documented`: [Caring.com](https://www.caring.com/articles/caregiving-apps)) | Yes: 15 sources on updates, siblings and long distance; "everything ends up scattered between texts and calendars"; group texts called too noisy (`documented`, our Reddit file) | **Best fit** |
| 2 Medication reminder apps | Small: $0.6B to $0.85B (`reported`) | No: many apps, plus 8+ vendors pitching in the Reddit threads (`documented`, our Reddit file) | Partly: the most-described problem (11 sources) but many existing workarounds and tools | Crowded and small |
| 3 Pharmacy packaging | Small to medium: $0.8B to $1.8B, likely packaging products and not services (`inferred`) | No: Amazon, UnitedHealth, Walgreens (`documented`) | Served by large players | Not open |
| 4 Senior care referral and placement | Unmeasurable alone; the problem is the biggest in the Reddit file (21 sources) | No: A Place for Mom is the largest and is under a Senate probe (`documented`, [NBC News](https://www.nbcnews.com/news/us-news/senate-announces-probe-place-for-mom-referral-service-rcna157282)) | Yes, but dominated by a fee-funded incumbent | Large need, hard to enter |
| 5 Home care and marketplaces | Largest: about $8.7B to $9.1B global non-medical (`reported`) | No: 18 franchise brands with $10.4B US system sales (`reported`) | Served; it is the care itself | Crowded |
| 6 Medical alert | Large: $6.3B to $9.0B global (`reported`) | No: many established companies | Served | Crowded |
| 7 Employer benefits | Small: $0.55B, one source (`reported`) | Few well-funded players (4 named) | Yes, but the buyer is an employer, not the family | Different customer |
| 8 Patient-side AI visit notes | Not measurable; only clinician-side scribe figures exist ($1.2B to $1.7B, 19% to 29% CAGR) | Yes: new and small (Kin Health raised a $9M seed in May 2026) (`documented`, [TechCrunch](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients)) | Unclear: the Reddit file has no theme for it | Open but unproven |
| 9 Patient portals | Medium: $3.9B to $6.6B (`reported`) | Dominated by Epic (about 42.3% of acute-care hospitals) | Partly served; buyer is the hospital | Not open |
| 10 Digital vaults | Medium for password managers: $3.1B to $3.75B | Strong incumbents | Not a theme in the Reddit file | Not a clear need |
| 11 to 14 | Not researched this session | not assessed | not assessed | Not assessed |

## Answer: which segment has the largest opportunity, and why

**Segment 1, family care-coordination apps, on this evidence. Confidence: medium to low.**

- **Big enough:** it is not the largest segment by dollars. Home care and medical alert are bigger. It is big enough that five research firms put the caregiver-app category at $1.3B to $4B, growing 8% to 17% a year (`reported`).
- **Not too many competitors:** only 3 named players, and none is described as a full coordination tool for a small family team except Caring Village, a vendor that ranks itself first. No source gave active-user numbers for any of them (`not-assessed`).
- **Unmet need:** the Reddit file shows caregivers coordinating through group texts, texts and calendars, and many say it is noisy and scattered. That is the second-largest actionable theme after choosing care.

**Why the other candidates ranked lower**
- Segment 4 has the biggest problem, but one fee-funded company dominates it.
- Segment 8 has the least competition but no measurable market and no demand signal in the Reddit research. It reflects your own experience, which is real but a single case.
- Segments 2, 3, 5, 6 and 9 are served by established players or sold to institutions.

## Limits (what would change this answer)

- **Size is for the wrong scope.** The $1.3B to $4B range covers all caregiver apps, including professional caregivers. A family-only figure (44%) comes from one publisher and isn't verified.
- **"Few competitors" counts named apps only.** The real competitor is probably group texts and shared spreadsheets, which are free and already in use. I couldn't measure how many families use the three named apps.
- **Reddit skews toward distress and toward asking for tools** (see the limits in `docs/qualitative-research-findings.md`). Theme counts are rough.
- **Segments 11 to 14 were not assessed.** Respite care, caregiver mental health, telehealth and insurance navigation could change the ranking.
- **This is a hypothesis to test, not a finding.** In Agile terms it is an assumption. Interviews with caregivers or a small prototype test would be the next check.
