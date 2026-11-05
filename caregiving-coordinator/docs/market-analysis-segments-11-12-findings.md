# Findings: how caregivers get relief, and what stops them (segments 11 and 12, 2026-11-04)

Draft for the owner's review. The market analysis is not changed until the owner approves.

## What was read

- 1,086 items read in full by 11 readers following `docs/sources/market-analysis-3/segments-11-12/READING-INSTRUCTIONS.md`:
  - 632 saved Reddit posts that mention respite or adult day (all of them)
  - 115 posts found only by the named-program search (VA, Medicaid waivers, hospice respite, Area Agencies on Aging and the 10 offerings)
  - a random 150 that mention only a support group, and 150 only a therapist
  - 39 saved AgingCare and ALZConnected threads
- **831 were from family caregivers writing about relief** (the rest were ads, paid workers, researchers, or a therapist for the person being cared for).
- **Checks:** `verify_codes.py` confirmed every item was coded exactly once and every quote matches its post word for word (0 problems). `count_results.py` produced every number below, and `results.json` lists the post ids behind each one.

## 1. How many caregivers need a break and have none

**214 of 831 (26%)** say they need a break or relief and have no help in place.

## 2. What caregivers use, and how it goes

Posts can name more than one kind of help.

| Kind of help | Posts | Used it | Tried and stopped | Wanted it, couldn't get it | Looking or considering |
|---|---|---|---|---|---|
| Respite, all types combined | 341 | 128 | 18 | 78 | 81 |
| Paid aide or companion | 185 | 84 | 7 | 34 | 56 |
| Family or friend stepping in | 160 | 85 | 4 | 39 | 28 |
| Therapist or counselor for the caregiver | 139 | 82 | 12 | 11 | 29 |
| Support group | 114 | 49 | 4 | 6 | 43 |
| Adult day program | 101 | 38 | 6 | 17 | 33 |
| Hospice respite | 40 | 20 | 2 | 10 | 6 |
| Apps or online tools | About 30 | Mostly online communities (Reddit, Facebook groups, ALZConnected, WhatsApp, a Discord server). Therapist finders: SonderMind, Zencare, Psychology Today. No meditation or burnout app. | | | |

Respite types (in-home, facility, type not said) are combined because readers handled "respite" with no type differently.

## 3. What stops them (tests AARP's reasons in caregivers' own words)

Posts that name each barrier, out of 831:

| Barrier | Posts | In AARP's list of reasons? |
|---|---|---|
| Cost | 118 | No (new) |
| The parent refuses | 96 | No (new) |
| Family or friends won't help | 93 | No (new) |
| Hard applications or eligibility rules (VA, Medicaid waivers) | 86 | Yes |
| Too few hours, minimum stays and other rigid rules | 59 | Yes ("inflexible program design") |
| Waitlists or no openings | 59 | Yes ("lack of trained providers," partly) |
| Worry about quality or safety | 52 | Yes |
| Guilt or shame about handing off care | 38 | Yes |
| No trained or reliable providers | 38 | Yes |
| Therapy doesn't help or isn't available | 27 | No |
| Support group doesn't fit (Alzheimer's-only, older spouses) | 19 | No |
| Transport or logistics | 16 | No |
| Doesn't trust strangers with the parent | 14 | Yes ("lack of trust") |
| Agencies, social workers or helplines pass people along | 14 | No |
| No time or energy to arrange it | 12 | No |
| Didn't know it existed | 10 | No |

**What this shows:**
- AARP's reasons all appear, but **the three biggest barriers aren't in its list**: cost, the parent refusing, and family not helping.
- **Adult day programs:** cost (24) and the parent refusing (23) are the top barriers.
- **Respite:** cost (59), the parent refusing (46) and family not helping (36) lead.

## 4. Who provides and pays (as caregivers name them)

- **Providers named most:** the VA (28), hospice (20), Area Agencies on Aging (10), Medicaid and Medicaid waivers (about 16), the Alzheimer's Association (6). Wellthy and Teepa Snow come up twice each. No other company comes up more than twice.
- **Costs and payers, as caregivers wrote them (examples from 153 posts):**
  - "more than $2,000 for a 2 week minimum" (facility respite)
  - "$1600 a month for 40 hours a week"
  - "Medicare pays for 2 five-day stays per year" (hospice respite)
  - "Medicaid waiver pays for 15 hours a week"
  - "out of pocket; her insurance won't pay"
  - All 153 are listed in `results.json` under `payer_cost`, each with its post link.

## 5. What helps when they get it

Caregivers who got a break describe sleep, time alone, a date with a spouse, seeing friends, and "relaxed for the first time in months." Support groups and online communities most often help them "feel less alone." For example:
- "I had almost a full week to be 28 again. I got to go on a date with my husband, spend time with my dogs, and relax for the first time in months." ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/14seksz/))
- "I wish we could afford respite care but we're barely scraping by as is" ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/1179uxg/))
- "there's currently a wait list for the waitlist in our county." ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/11awqmt/))

## 6. Proposed verdicts for the market analysis (for the owner to decide)

- **Segment 11, respite and adult day:** a real unmet need, and **the gap is access, not supply**. Help exists (respite, adult day, VA, Medicaid waivers, hospice respite), but cost, eligibility rules, waitlists and rigid hours block it. The parent refusing and family not helping block it too. This confirms AARP's 39% (would help) vs 13% (use it), and adds three bigger barriers AARP doesn't list.
- **Segment 12, burnout support:** the need is large, but **"crowded" is wrong for caregivers**. Burnout and meditation apps are crowded in general, yet caregivers almost never use them. What they use is therapy (often helpful, sometimes unaffordable or not caregiver-aware), support groups (when one fits) and online peer communities.

## Limits

- Reddit and forum writers are not a random sample of all caregivers, and they lean toward people having a hard time.
- Counts are posts that mention something, not how many caregivers face it nationally.
- Readers made some judgment calls, listed in their reports: borderline caregivers (parents of disabled children, siblings) counted as relevant, and "respite" with no type handled differently. That's why respite is reported combined.
- "Other" barriers were grouped by keyword rules written in `count_results.py`. 129 one-off barriers stay ungrouped.
- Each quote shows a post's main point, not always the barrier it's counted under. Use the ids in `results.json` to read the post behind any count.

---

## Added 2026-11-04: the findings split by audience

Checklist: `sources/market-analysis-3/segments-11-12/research-checklist-audience-split.md`. Each of the 831 relief posts was labeled with the market analysis "cared_for" labels.
- **How:** a script labeled the 278 clear posts. Readers labeled the other 553, each with an exact quote checked by script (0 problems).
- **Accuracy:** a random 40 of the script's labels were re-read, and 38 agreed (95%).
- **Files:** `audience-labels.json` (every label and how it was decided), `count_by_audience.py` → `results-by-audience.json`.

**Labels:** parent 486 (Audience 1), spouse or partner 98 (Audience 2), other relative 119, unclear 103, own child 24, client 1.

**No new search needed.** The checklist's rule was to search again if fewer than 50 spouse posts turned up, and there are 98. But some Audience 2 barriers have under 10 posts each, so read their order as a rough guide.

| | Audience 1: adult child caring for a parent (486 posts) | Audience 2: spouse or partner (98 posts) |
|---|---|---|
| Need a break, no help in place | 121 (25%) | 29 (30%) |
| Respite, any type | 205 (42%): 79 used, 48 wanted it and couldn't get it, 48 looking | 34 (35%): 12 used, 9 couldn't get it, 9 looking |
| Adult day program | 70 (14%) | 9 (9%) |
| Therapist or counselor for themselves | 85 (17%) | 25 (26%) |
| Support group | 58 (12%) | 22 (22%) |
| Family or friend stepping in | 97 (20%) | 13 (13%) |
| Top barriers | Cost 77 (16%), the parent refuses 75 (15%), family won't help 57 (12%), eligibility rules 45 (9%), quality worries 30 (6%), waitlists 29 (6%) | Family won't help 12 (12%), eligibility rules 10 (10%), cost 8 (8%), no reliable providers 8 (8%), quality worries 8 (8%), the spouse refuses 7 (7%) |
| Providers named most | Hospice 16, VA 15, Alzheimer's Association 5, Area Agency on Aging 4, Medicaid and waivers 10 | VA 7, local aging councils 2, Medicaid 1 |

**What differs between the audiences:**
1. **Adult children** are blocked most by cost and by the parent refusing. They lean on respite, paid aides and siblings, and family not helping is a major barrier.
2. **Spouses** are more often left with no help (30% vs 25%). They turn more to therapy and support groups for themselves (26% and 22%, vs 17% and 12%), and less to adult day programs. Family not helping and eligibility rules lead their barriers. The VA is their most named provider.
3. **Both audiences share** the same core blockers (family not helping, eligibility rules, cost, the person refusing), so the access gap applies to both.

**Limits:**
- 247 posts (other relatives, own children, unclear) belong to neither audience and are counted separately.
- Two spot-check posts disagreed with the script, both edge cases (a partner's child, and a parent and child mix-up).
- Some forum threads are cut off at the start, so their labels come from the replies.
