# 🎨 Prototypes - Hat Check
- Source copy: https://app.notion.com/p/d7d9219a46918385bbab81ed9789b490
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:11.975Z
- Not saved: screenshots (v6-01-input.png, v6-04-reading.png, v6-05-verdict.png, v6-06-matched.png, v6-07-missing.png, v6-08-not-standard.png, v6-09-unplaced.png, v6-10-how-it-works.png, v6-02c-too-long.png, v6-03-not-covered.png, v6-19-decode-failed.png, v6-21-no-lines.png, v6-11-basic-read.png, v6-12-ats.png, v6-13-skills.png, v6-14-highlights.png, v6-15-cover-letter.png, v6-16-interview.png, v6-17-no-extra.png, t15-footer.png, v6-18-license.png, v6-tablet-05.png, v6-mobile-05.png, v6-mobile-14.png); table of contents block

---

## Links

### Figma file

[Hat Check Job Decoder Prototypes (Figma)](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3)

### Clickable prototypes

- [Desktop (1440)](https://www.figma.com/proto/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?page-id=9%3A210&node-id=48-893&starting-point-node-id=48%3A893&scaling=scale-down-width)
- [Tablet (834)](https://www.figma.com/proto/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?page-id=9%3A211&node-id=49-1104&starting-point-node-id=49%3A1104&scaling=scale-down-width)
- [Mobile (412)](https://www.figma.com/proto/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?page-id=0%3A1&node-id=49-2570&starting-point-node-id=49%3A2570&scaling=scale-down-width)

Each prototype opens on the Input screen. Select Decode, and the app reads the posting and moves to the results by itself. Use Next and Back to step through the 5 result steps. On step 5, select Prepare your application to enter the prep flow. Every state also has its own flow starting point in the prototype menu, such as Decode failed, Basic read, and Prep with no extra scope.

### Figma screens for the main flow (desktop)

- [Results step 1: verdict](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=50-649)
- [Results step 5: lines we could not place](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=50-1109)
- [Prep step 1: ATS keywords](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=53-628)

## Flow 1: Decode a posting

The main path. All screenshots are the desktop (1440) versions.

### 01 Input

The posting can be up to 20,000 characters. The helper text counts the characters as you type.

[video/file not saved: v6-01-input.png] (caption: 01 Input)

### 04 Reading

A second state, 04b, appears when reading takes longer than usual. Cancel keeps the title and posting filled in.

[video/file not saved: v6-04-reading.png] (caption: 04 Reading)

### 05 Results step 1: verdict

The verdict, the match percent, one stat tile for each hat set, and the scope of the posting.

[video/file not saved: v6-05-verdict.png] (caption: 05 Results step 1, verdict)

### 06 Results step 2: matched hats

Filter chips by match type. Each hat card shows its match counts, then accordions for Evidence, Why it matters, and What it takes. Evidence lists every quote, the framework item, the match type, and the role.

[video/file not saved: v6-06-matched.png] (caption: 06 Results step 2, matched hats)

### 07 Results step 3: expected but missing

These hats have no posting quote, so each card shows the framework evidence instead.

[video/file not saved: v6-07-missing.png] (caption: 07 Results step 3, expected but missing)

### 08 Results step 4: not standard

Each card names the job function the hat usually belongs to.

[video/file not saved: v6-08-not-standard.png] (caption: 08 Results step 4, not standard)

### 09 Results step 5: lines we could not place

A second state, 09b, shows when every line was placed. Empty states also exist for steps 2, 3, and 4 (06e, 07e, 08e).

[video/file not saved: v6-09-unplaced.png] (caption: 09 Results step 5, lines we could not place)

### 10 How it works

A dialog with all 17 steps, the verdict thresholds, and how the framework and the AI split the work. It opens over the results (10), the input (10b), and the basic read (10c).

[video/file not saved: v6-10-how-it-works.png] (caption: 10 How it works)

## Flow 2: Input problems and errors

### 02c Input with a posting that is too long

The other input states are 02a (posting missing), 02b (title missing), and 02d (posting is a link). Each one has an error summary at the top and an error under the field.

[video/file not saved: v6-02c-too-long.png] (caption: 02c Posting too long)

### 03 Title not covered

[video/file not saved: v6-03-not-covered.png] (caption: 03 Title not covered)

### 19 Decode failed

Screen 20, Too many decodes, uses the same layout.

[video/file not saved: v6-19-decode-failed.png] (caption: 19 Decode failed)

### 21 No lines matched

[video/file not saved: v6-21-no-lines.png] (caption: 21 No lines matched)

## Flow 3: Basic read when the AI is down

The same banner appears on results step 1 (11), results step 2 (11b), and prep step 1 (22). Similar matches are not counted, so only 1 hat is not standard.

### 11 Results step 1: basic read

[video/file not saved: v6-11-basic-read.png] (caption: 11 Basic read)

## Flow 4: Prepare your application

Entered from results step 5. ATS keywords come first. Each screen is one list of Hat cards. Each card reads "For the \[hat\] Hat" and shows its status as a pill. Missing Hats come first, then matched Hats, then extra scope. On mobile, only the first Hat is open, and a jump list sits at the top.

### 12 Prep step 1: ATS keywords

The posting's own wording, then the Hats, tools, activities, and key skills. Each keyword appears once.

[video/file not saved: v6-12-ats.png] (caption: 12 ATS keywords)

### 13 Prep step 2: skills for your resume

Skills the posting names come first, then skills shared by several Hats (listed once), then each Hat's own skills.

[video/file not saved: v6-13-skills.png] (caption: 13 Skills for your resume)

### 14 Prep step 3: what to highlight

Each item has a fill-in line: "\[Activity\] \_\_\_\_, which resulted in \[deliverable\] \_\_\_\_, so that \_\_\_\_". The hint is the framework's reason that deliverable matters. Items the posting names show their quote.

[video/file not saved: v6-14-highlights.png] (caption: 14 What to highlight)

### 15 Prep step 4: cover letter points

[video/file not saved: v6-15-cover-letter.png] (caption: 15 Cover letter points)

### 16 Prep step 5: interview points

The primary action is Back to results.

[video/file not saved: v6-16-interview.png] (caption: 16 Interview points)

### 17 Empty state: no extra scope

[video/file not saved: v6-17-no-extra.png] (caption: 17 Cover letter points with no extra scope)

## Flow 5: License and attribution (T15)

Every screen ends with the same Footer component. Screens that show framework data carry the credit line, which links to the framework on GitHub. Every screen also has a License and attribution link that opens screen 18. The credit sentence lives in one Credit line component, so it is never retyped.

### Figma links

- [License and attribution, desktop](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=53-1931)
- [Tablet](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=54-3052)
- [Mobile](https://www.figma.com/design/HvbMGxsYUXHCJmt0pv8bg3/Hat-Check-Job-Decoder-Prototypes?node-id=54-4812)
- Ticket: T15: Licensing and attribution

### Footer on a screen with framework data

[video/file not saved: t15-footer.png] (caption: Footer: the credit line, then the License and attribution link)

### 18 License and attribution

[video/file not saved: v6-18-license.png] (caption: 18 License and attribution)

## Tablet and mobile

Every screen above also exists at tablet (834) and mobile (412) in the same Figma file.

### Tablet verdict (834)

[video/file not saved: v6-tablet-05.png] (caption: Tablet, 05 verdict)

### Mobile verdict (412)

[video/file not saved: v6-mobile-05.png] (caption: Mobile, 05 verdict)

### Mobile prep with collapsed Hats (412)

[video/file not saved: v6-mobile-14.png] (caption: Mobile, 14 What to highlight, with the jump list and collapsed Hats)

## Change note — ADR-0039 match-level model (2026-11-04)

The prototype is being brought up to **ADR-0039** (proportional per-hat scoring) under ticket **T17**. Done so far, across desktop (1440), tablet (834), and mobile (412):

- Each hat card's pill now shows its **match level and share** (for example, `Full · 50% of its work named`, `Partial · 12% of its work named`) instead of a flat `Matched` pill. Full is 25% or more of the hat's work; partial is above 0 and under 25%.
- The results step-2 subtitle now reads in match-level language (grouped fully, then partly).
- The verdict stat tiles are relabeled **Hats covered / Hidden hats / Extra hats** (was Matched hats / Expected but missing / Not standard), matching the app's wording.
- The basic-read variants carry the same labels.

Still to do on T17: explicit **Fully covered / Partly covered** group headings within results step 2; a decision on whether the by-match-type filter chips (Exact / Alias / Similar) stay or are replaced by level grouping; and the open ADR-0039 decision on whether tools still show as supporting evidence under a hat (owner: Morgan).

**Update (2026-11-04, later):** the explicit **Fully covered (25% or more)** and **Partly covered (under 25%)** group headings are now in across desktop, tablet, and mobile, and the step title is **Hats this posting covers** (was Matched hats). The two remaining T17 items are decisions for Morgan: keep or replace the by-match-type filter chips, and whether tools still show as supporting evidence under a hat.
