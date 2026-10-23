# Obsidian Best Practices — Current Practice (2026)

**Researched:** 2026-08-10. **Obsidian version checked against:** 1.13.6 (released 2026-08-10).
**Scope:** vault organization, core settings, community plugins, and accessibility /
ADHD / dyslexia / low-friction study use.

**Why this brief exists:** this repo *is* the Obsidian vault (see `specs/vault-convention.md`),
and Orlando is a non-developer using Obsidian for the first time. On 2026-08-10 he opened the
vault and found the file explorer showing `src/`, `bin/`, `data/` — a code repo, not study
material. The session's reactive fix was to add `userIgnoreFilters` to `.obsidian/app.json`.
This brief was commissioned to check whether that was the right mechanism.

**It was not.** That is the headline finding and it is section 1.

**Intended downstream use:** correct `specs/vault-convention.md`, correct
`.obsidian/`, and give Orlando a short list of settings that actually matter.

---

## Evidence grading used in this brief

Same scale as the rest of `specs/research/`.

| Grade | Means |
|---|---|
| **High** | Official Obsidian documentation (the `obsidianmd/obsidian-help` repo, which is the source of truth for `obsidian.md/help`), or official Obsidian blog. Verified by reading the repo directly, not a search summary. |
| **Moderate** | Multiple independent sources agree; or a named practitioner with standing (e.g. Obsidian's own CEO on his own vault); or peer-reviewed research. |
| **Low** | Single blog post, listicle, or forum comment with no methodology. |
| **Anecdote** | One person's experience, explicitly presented as such. Useful as a signal that a friction point exists; useless as evidence that a fix works. |
| **Hype** | Widely repeated, not supported by anything traceable. Named so it stops circulating. |

**Standing caution specific to this topic.** Obsidian advice online is unusually
contaminated. The app has a large affiliate/course/template economy, so the "top 10 plugins"
genre is written to sell things. Several of the highest-ranking results for the exact
questions in this brief — `saturnitystools.com`, `obsidianmate.com`, `obsibrain.com`,
`shadow.do`, `notes-automate.com` — are SEO properties whose "2026" content is
indistinguishable from their 2024 content. **A specific, checkable problem:** a large share
of internet advice about the `Excluded files` setting is guesswork, because until recently
Obsidian never documented what that setting does (GitHub issue
`obsidianmd/obsidian-help#956`). People described the behaviour they assumed, and each other
copied it. That is exactly the failure this brief corrects.

---

## Sources

Primary (official Obsidian):

- `obsidianmd/obsidian-help` repo, `en/User interface/Settings.md` — the settings reference,
  including the `Excluded files` definition —
  `https://github.com/obsidianmd/obsidian-help/blob/master/en/User%20interface/Settings.md`
- `en/Plugins/File explorer.md`, `en/Plugins/Bookmarks.md`, `en/Plugins/Workspaces.md`,
  `en/Plugins/Search.md`, `en/Plugins/Graph view.md`, `en/Plugins/Backlinks.md`,
  `en/Plugins/Outgoing links.md`, `en/Plugins/Quick switcher.md`, `en/Plugins/Core plugins.md`
- `en/Getting started/Create a vault.md`, `en/Getting started/Glossary.md`,
  `en/Getting started/Sandbox vault.md`, `en/Files and folders/Manage vaults.md`
- `en/Extending Obsidian/CSS snippets.md` — `https://obsidian.md/help/snippets`
- `en/Extending Obsidian/Plugin security.md` — `https://obsidian.md/help/plugin-security`
- `en/Extending Obsidian/Community directory.md` — `https://obsidian.md/help/community-directory`
- `en/Editing and formatting/Callouts.md`
- Obsidian blog, "The future of Obsidian plugins," 2026-05-12 —
  `https://obsidian.md/blog/future-of-plugins/`
- Obsidian changelog — `https://obsidian.md/changelog/`
- `obsidianmd/obsidian-help` issue #956, "'Excluded files' setting is undocumented" —
  `https://github.com/obsidianmd/obsidian-help/issues/956`

Primary (peer-reviewed):

- Rello, L. & Baeza-Yates, R., "Good fonts for dyslexia" (ASSETS), eye-tracking, n=48 —
  `https://dyslexiahelp.umich.edu/wp-content/uploads/2014/02/good_fonts_for_dyslexia_study.pdf`
- Rello, L. & Baeza-Yates, R., "How to present more readable text for people with dyslexia,"
  *Universal Access in the Information Society*, eye-tracking, n=92 (46 dyslexic / 46 control) —
  `https://superarladislexia.org/pdf/2017-Luz%20Rello-UAIS_How%20to%20present%20text.pdf`

Named practitioner:

- Steph Ango (kepano), CEO of Obsidian, "How I use Obsidian" — `https://stephango.com/vault`

Community (graded individually below):

- Obsidian Forum, "Ignore/exclude completely files or a folder from all obsidian indexers and
  parsers" — `https://forum.obsidian.md/t/ignore-exclude-completely-files-or-a-folder-from-all-obsidian-indexers-and-parsers/52025`
- Obsidian Forum, "Trying to find a good setup for ADHD" —
  `https://forum.obsidian.md/t/trying-to-find-a-good-setup-for-adhd/12218`
- Obsidian Forum, "How to hide some files (for example by extension or filename)?" —
  `https://forum.obsidian.md/t/how-to-hide-some-files-for-example-by-extension-or-filename/45250`
- Obsidian Forum, "Hide folders/file that includes 'X' in title in all folders" —
  `https://forum.obsidian.md/t/hide-folders-file-that-includes-x-in-title-in-all-folders/63515`
- Community directory listings for Homepage, Explorer Hider, File Hider, Dataview,
  Spaced Repetition — `https://community.obsidian.md/plugins/...`, adoption figures
  cross-checked on `https://www.obsidianstats.com/`
- `sjelms/Openlexia` theme — `https://github.com/sjelms/Openlexia`

Surveyed but **not** relied on (SEO content, recycled, or selling something):
`saturnitystools.com`, `obsidianmate.com`, `obsibrain.com`, `shadow.do`,
`notes-automate.com`, `facedragons.com`, and the `makeuseof.com` / `xda-developers.com`
cluster of "Obsidian mistakes I made" posts. These appear below only where they are the
*subject* of a claim about what the discourse says, never as support for a technique.

---

## 1. The `Excluded files` setting does not do what this vault is using it for

### What it actually does — High

Official, verbatim, from `en/User interface/Settings.md`, under **Files and links →
Advanced → Excluded files**:

> Excluded files will be hidden in Search, Graph View, and Unlinked Mentions (Backlinks and
> Outgoing links), and less noticeable in Quick Switcher and link suggestions.

Corroborated by the per-feature docs, which each carry a matching callout:

| Feature | Official wording | Effect |
|---|---|---|
| Search | "will not appear in Search results" | Hidden |
| Graph view | "will not appear in Graph view" | Hidden |
| Backlinks | "will not appear in Unlinked mentions" | Hidden |
| Outgoing links | "will not appear in Unlinked mentions" | Hidden |
| Quick switcher | "are **deprioritized** in Quick switcher results" | Demoted, still there |
| Link suggestions | "less noticeable" | Demoted, still there |
| **File explorer** | **not mentioned anywhere** | **No effect** |

`en/Plugins/File explorer.md` documents the entire file explorer feature set — create,
delete, rename, move, sort order, auto-reveal, expand/collapse all. **There is no filtering,
hiding, or exclusion feature in the file explorer at all.** The word "exclude" does not
appear in that file.

The five-year-old feature request thread asking for a real ignore mechanism
(`forum.obsidian.md/t/.../52025`) says the same thing from the user side — excluded folders
"still cause performance problems and display issues," and the file pane is explicitly listed
as somewhere exclusion does not reach. That thread has **no official response** and no
`.obsidianignore` has shipped. **Grade: Moderate** (many independent users, no staff reply),
and it agrees with the High-grade official docs, so treat the conclusion as settled.

### Why the internet told us otherwise — Moderate

Until the docs were updated, this setting had **no documentation outside the settings screen
itself** (`obsidian-help#956`). The whole "excluded files hides folders from the sidebar"
claim is a folk belief that propagated through blogs and forum replies because nobody had a
source to check. This is the same pattern the rest of `specs/research/` keeps catching:
confident, repeated, unsourced.

### What this means for this vault

`.obsidian/app.json` currently contains:

```json
{ "userIgnoreFilters": ["bin/", "src/", "data/", "docs/", "specs/", "system/",
                        "README.md", "SETUP.md", "SESSION-LOG"] }
```

Two corrections:

1. **It is not useless — keep it.** It is doing real work: search results, graph view,
   backlinks, and unlinked mentions are all now free of repo noise. For a vault that is also
   a code repo, that is genuinely valuable, and it is the officially supported way to get it.
   Note it also excludes `system/`, which means `tracker.md` and `inbox.md` are demoted in
   Quick Switcher and invisible to search — see §7, recommendation 3.
2. **The claim in `specs/vault-convention.md` is wrong** and must be fixed. That file
   currently says the filter "hides non-study folders (`bin`, `src`, `data`, `docs`, `specs`,
   `system`) from the file explorer so only `learning/` and `canvas/` show." It does not.
   Orlando will still see the whole repo in the sidebar.

### There is no "Focus mode" — High

Worth stating because it comes up in searches. Obsidian has no core focus/zen mode that
filters the file explorer. `Workspaces` (core plugin, currently disabled in this vault) saves
"open files and tabs, and the width and visibility of each sidebar" — it can save *"sidebar
collapsed"*, but it cannot save *"sidebar showing only these folders."* Workspaces will not
solve this problem.

### The three real options, ranked

**Option A — Bookmarks (core plugin, already enabled). Grade: High. Recommended.**

`Bookmarks` is an official core plugin that bookmarks files, folders, searches, headings, and
graphs, organized into groups, in its own sidebar tab. The intended workflow is: collapse the
file explorer entirely, bookmark `learning/` and `canvas/` (and each active subject), and
navigate from Bookmarks. Zero third-party code, zero CSS, cannot break on an Obsidian update,
and it is *additive* — Orlando gets a two-item sidebar instead of a filtered twelve-item one.

This is the answer Obsidian actually supports. It is already enabled in
`.obsidian/core-plugins.json` (`"bookmarks": true`) and is currently unused.

**Option B — a CSS snippet. Grade: Moderate. Recommended as a supplement.**

The file explorer renders folders as `.nav-folder-title` elements carrying a `data-path`
attribute, so CSS can hide them:

```css
.nav-folder-title[data-path="src"],
.nav-folder-title[data-path="src"] + .nav-folder-children { display: none; }
```

Widely used and independently reproduced across forum threads and the Explorer Hider plugin
(which is, by its own README, "a plugin and a bit of CSS"). CSS snippets are an officially
documented, first-class Obsidian feature (`obsidian.md/help/snippets`) — this is not a hack in
the "unsupported" sense.

Caveats, honestly: `.nav-folder-title` and `data-path` are *theme/DOM* internals, not a
published API. Obsidian has kept them stable for years, but a future release could rename
them, and the failure mode is silent (folders reappear). Also, hiding is cosmetic — the files
are still indexed, so this is complementary to `userIgnoreFilters`, not a replacement.

Concrete advantage for this vault: `.obsidian/snippets/adhd-dyslexia-typography.css` already
exists and is already enabled and already backed up. Adding ten lines to it costs nothing new.

**Option C — a hiding plugin. Grade: Low. Not recommended.**

| Plugin | Downloads | Stars | Last release | Verdict |
|---|---|---|---|---|
| File Hider (`OA-file-hider`) | 47,803 | 79 | ~4 years ago, 18 open issues | Abandoned. Do not install. |
| Explorer Hider (`explorer-hider`) | 4,790 | 16 | ~1 year ago | Maintained-ish, but tiny adoption |

For scale, Dataview has 4.7M downloads and the Homepage plugin 1.2M. Explorer Hider's ~4.8k
is a rounding error in a 120-million-download ecosystem. This is a case where "there's a
plugin for that" is true but the plugin is a solo project with fewer users than a mid-sized
office building, doing something ten lines of CSS do. Adding a third-party dependency with
full filesystem access (§2) to save ten lines of CSS is a bad trade.

---

## 2. How to evaluate community plugins in 2026 — this changed recently

### The security model — High

From `obsidian.md/help/plugin-security`, verbatim in substance: Obsidian ships in **Restricted
Mode** by default, which blocks all third-party code. Once you disable it, *"due to technical
limitations, Obsidian cannot reliably restrict plugins to specific permissions or access
levels."* Plugins inherit Obsidian's full access — they *"can read files on your computer,
connect to the internet, and install additional programs."*

For this vault specifically: the vault is the repo. A plugin has read/write access to
`src/`, `bin/`, `data/`, and every research brief. That raises the bar for "is this plugin
worth it" well above where a normal notes vault would put it.

### The 2026 change — High

On **2026-05-12** Obsidian launched a new Community directory at `community.obsidian.md`
(blog: "The future of Obsidian plugins"). What changed materially:

- Every plugin **version** is now automatically scanned for vulnerabilities, code quality, and
  malware. Previously only the initial submission got a manual review.
- Every listing now has a **Scorecard** tab with two separate scores:
  - **Health** — hygiene (README, license, description), maintenance (recent commits and
    releases), responsiveness (issues closed, active contributors), adoption (installs, stars).
  - **Review** — result of the latest automated scan, plus **disclosures**: things the plugin
    does that you should know about, e.g. clipboard access, requests to external domains, and
    which Obsidian APIs it uses (Vault Read / Vault Write).
- The official docs give an explicit traffic-light reading: 🟢 few/no disclosures = low risk;
  🟡 a handful, check clipboard/network; 🔴 several = review carefully before installing.

**This is the single most useful practical change for a non-developer.** It replaces "is this
plugin on someone's top-10 list" — which is what the SEO layer sells — with a checkable,
first-party signal on the plugin's own page. It is also newer than most of the plugin advice
currently ranking on Google, which is why almost none of that advice mentions it.

### The "everyone recommends X" test, applied — Moderate

Asked to name essential plugins, the listicle layer converges on roughly: Dataview, Templater,
Calendar, Tasks, Kanban, Excalidraw, Style Settings, Minimal theme. Checking real adoption:

| Item | Downloads | Notes |
|---|---|---|
| Dataview | ~4.7M, 9,264 stars | Genuinely ubiquitous. Last release ~1 year ago. |
| Homepage | ~1.2M | Health "Excellent", review "Passed", updated ~2 months ago |
| Spaced Repetition | ~548,883, 2,512 stars | Actively maintained (v1.15.4, ~2 months ago) |
| Minimal (theme) | ~500k, most-downloaded theme | Written by kepano, Obsidian's CEO |
| Explorer Hider | ~4,790 | Listicle-adjacent, ecosystem-invisible |

So the consensus list is *not* purely fabricated — Dataview really is that widely installed.
But two things are true at once: (a) the popular plugins are popular, and (b) **popularity
tracks the general-purpose PKM use case, which is not this vault's use case.** Dataview
exists to query a large heterogeneous note collection. This vault has a hand-maintained
tracker with exactly one `current` row. Dataview would be solving a problem this vault
deliberately does not have.

**Verdict for this vault: install zero community plugins.** The one arguable exception is
Homepage (open `system/tracker.md` on launch), evaluated in §7.

---

## 3. Vault organization philosophies, evaluated honestly

### The evidence situation — Moderate, and the honest answer is "none"

PARA, Zettelkasten, CODE, LATCH, MOCs. Searching for evidence that any of these improves
learning or retrieval turns up **no controlled studies whatsoever** — only advocacy (usually
attached to a course or book) and counter-anecdote. The most useful source found was an
XDA piece cataloguing the author abandoning PARA, Zettelkasten, CODE, and LATCH in six months;
it is **Anecdote** grade and says so, offering no data. Its diagnosis is nevertheless the one
that recurs everywhere: each system demands a categorization decision *at capture time*, and
that decision cost is what kills adoption. Zettelkasten in particular *"required excessive
precision at capture time."*

That failure mode is not incidental for this project. Decision cost at the moment of capture is
precisely the ADHD tax the whole system is designed to remove — the same reasoning behind
"exactly one row is `current`" in `specs/vault-convention.md`.

### What the Obsidian CEO actually does — Moderate (named practitioner, own vault)

Steph Ango (kepano) publishes his vault rules at `stephango.com/vault`. His stated principles:
*"Avoid splitting content into multiple vaults. Avoid folders for organization. Avoid
non-standard Markdown."* And: *"My system is oriented towards speed and laziness. I don't want
the overhead of having to consider where something should go... I avoid folders because many of
my entries belong to more than one area of thought."* He navigates by Quick Switcher, backlinks,
and links — **not** the file explorer.

This is worth taking seriously and worth *not* copying wholesale. His "avoid folders" argument
is explicitly conditional: it holds *because* his entries belong to multiple areas of thought.
This vault's lesson files do not. A lesson belongs to exactly one subject and has exactly one
position in a study order. Folder-per-subject plus `NN-` numeric prefixes is not a compromise
here — it *is* the correct structure, because the ordering is load-bearing pedagogy, not
filing. The one principle of his that transfers directly is "avoid non-standard Markdown,"
which `vault-convention.md` rule 3 already locks in.

### The ADHD forum thread, read carefully — Low

`forum.obsidian.md/t/trying-to-find-a-good-setup-for-adhd/12218` (14 replies, self-identified
ADHD users) converges on: PARA, nested tags, an INBOX, templates to reduce decision fatigue,
and warnings against "high-maintenance" systems and over-planning folders before you know your
needs. The warnings are the valuable half and align with everything above. The PARA
recommendation is the less valuable half — **it is answering a different question.** Those
users are organizing an open-ended stream of personal capture. This vault has a fixed
curriculum with a defined pipeline (`learning/`, `system/`, `canvas/`). PARA would add four
buckets and a sorting decision to a system whose entire design goal is to have no sorting
decision.

### Bottom line — do not adopt a methodology

Every popular vault-organization method is aimed at a *large, general, growing, ambiguous*
note collection. This vault is *small, single-purpose, curated, and ordered.* Adopting PARA
or Zettelkasten here would import overhead to solve a problem the vault does not have, and
would violate the one durable-state rule that makes the tracker work. **The existing folder
map in `specs/vault-convention.md` is already better-suited to this vault than any of them.**
No change recommended. Flag this as a live risk anyway: methodology advice is the single most
abundant Obsidian content on the internet, and it will keep showing up.

---

## 4. Accessibility, dyslexia, and low-friction settings

### There is no accessibility settings page — High

Obsidian has no dedicated accessibility section. The relevant levers are scattered across
Appearance and Editor. Recent releases have improved keyboard navigation (1.13 added settings
search and arrow-key navigation across views, and expanded `Escape` handling), but screen
reader support remains weak per multiple open forum threads. Not relevant to this user, but
worth knowing the app's accessibility story is thin — *do not expect Obsidian to accommodate
anything; the accommodation has to be built in the vault.* Which is what this project already
does.

The settings that do matter, all official:

| Setting | Location | Relevance |
|---|---|---|
| **Font size** | Appearance → Font → Font size | Affects editing and reading views |
| **Text font** | Appearance → Font → Text font | Sans-serif; see below |
| **Readable line length** | Editor → Display → "Limit maximum line length" | Column width control |
| **Default view for new tabs** | Editor | Reading view vs Editing view |
| **Default editing mode** | Editor | Live Preview vs Source mode |
| **Base color scheme** | Appearance | Light / Dark / Adapt to system |
| **Show inline title** | Appearance → Interface | Filename as an editable heading |
| **Quick font size adjustment** | Appearance → Font | `Cmd+Scroll` / pinch-zoom on the fly |

That last one is genuinely useful and almost never mentioned: Orlando can change text size
mid-session with a trackpad pinch, no settings trip. Worth telling him it exists.

### What the peer-reviewed evidence supports — High

Two eye-tracking studies by Rello & Baeza-Yates, both directly relevant and both consistent
with what `specs/DECISIONS.md` §7 already locked:

- **"Good fonts for dyslexia"** (n=48). Sans-serif, monospaced, and roman styles significantly
  improved reading performance over serif, proportional, and italic. Purpose-built dyslexia
  fonts (OpenDyslexic) were **not** easier to read; Arial and Helvetica produced shorter
  fixation durations. This is the study behind the debunking already recorded in `DECISIONS.md`
  §7 — **not re-litigated here**, only cited as the source.
- **"How to present more readable text for people with dyslexia"** (n=92; 46 dyslexic, 46
  control). Two findings this repo has *not* yet acted on:
  1. **Larger text and larger character spacing led both groups to read significantly faster.**
     The paper's design recommendation is **18pt**. The current snippet sets 17px.
  2. **Readers with dyslexia preferred *lower* brightness and colour difference between text
     and background than average readers.** That is a caution against maximum contrast —
     pure white on pure black, or pure black on pure white, is not the target. WCAG 2.2 is a
     *floor*, not a goal.

Point 2 is the one genuinely new thing in this section, and it is a real constraint on any
future theme decision. The current snippet deliberately sets no colours and inherits the
theme, which is the right call — it means the theme choice is where this constraint bites.

### The "accessible Obsidian theme" trap — Low, and worth naming

`sjelms/Openlexia` markets itself as *"a clean, accessible Obsidian theme designed for
academic writing and neurodivergent users... with the OpenDyslexic typeface at its core."*
Its headline feature is the one thing the evidence says does not work. The theme's *other*
properties — high contrast palette, clear typographic hierarchy — are the parts with support.

This is the general pattern to expect: "accessible" and "dyslexia-friendly" in the Obsidian
theme/plugin space are marketing terms, and the most visible signal (the font) is the one with
the weakest evidence. **Do not install accessibility-branded themes.** The existing CSS
snippet is better-grounded than anything on offer.

### Text-to-speech — no plugin needed

`DECISIONS.md` §7 already treats TTS as a real accommodation (d ≈ 0.35). Obsidian has no core
TTS and no well-adopted TTS plugin worth the filesystem-access trade from §2. macOS has
system-level speech (System Settings → Accessibility → Spoken Content, then select text and
press the configured shortcut) that works inside Obsidian like any other app. Use that. Zero
dependencies, zero configuration in the vault.

### Pomodoro / focus plugins — not evaluated, deliberately

Several exist. None have adoption or evidence justifying a plugin with full filesystem access
in a vault that is also a code repo, and timer apps are not an Obsidian-shaped problem. If a
timer is wanted, use anything outside Obsidian. No recommendation.

---

## 5. Beginner friction points

The "Obsidian mistakes" genre is entirely **Low** grade — listicles on `makeuseof.com` and
`xda-developers.com` that agree with each other partly because they are copying each other.
Their convergence is weak evidence. But two of the friction points they name were **observed
first-hand in this session**, which upgrades those two specifically:

| Friction point | Status here |
|---|---|
| **Confusion about what a vault is** | **Observed.** Orlando opened the repo as a vault and did not expect to see code folders. Official definition (Glossary, High): *"A vault is a folder on your file system which contains notes and an `.obsidian` folder with Obsidian-specific configuration."* A vault is not a database or a project — it is literally a folder, and Obsidian shows you everything in it. |
| **Sidebar clutter** | **Observed.** §1 of this brief. |
| Accidentally opening a subfolder as the vault | Not observed, but plausible. Obsidian's "Open folder as vault" will happily open `learning/` alone, which would make `system/tracker.md` invisible. If that ever happens, the fix is the vault switcher (Vault profile at the bottom of the left sidebar), not re-cloning anything. |
| Building elaborate folder structures before writing anything | Not applicable — the folder map is derived from the pipeline, not invented up front. |
| Installing many plugins on day one | Not applicable yet. §2 says keep it at zero. |
| Not knowing where the vault lives on disk | Not applicable — it is a git repo at a known path. |

### The Sandbox vault — High, and underused

Obsidian ships a **Sandbox vault**: a separate throwaway vault with built-in tutorial content,
opened from the Help icon next to the vault switcher, or via the command palette
("Open sandbox vault"). It opens in its own window and cannot touch the real vault.

This is the correct place for a first-time user to click around, break things, try settings,
and learn what a callout or a link does — **without any risk to a repo containing months of
work.** It is officially supported, requires nothing, and is not mentioned by any of the
beginner listicles surveyed. Best single "learn Obsidian" recommendation in this brief.

---

## 6. Two things in the current config that need verifying

Both are in `.obsidian/snippets/adhd-dyslexia-typography.css`. Neither is certainly broken —
both are *unverified against current Obsidian* and have silent failure modes.

**a) Custom callout colour format.** The snippet uses:

```css
.callout[data-callout="fact"] { --callout-color: 76, 175, 80; }
```

A bare comma-separated RGB triple. The current official docs (`en/Editing and formatting/
Callouts.md`) say `--callout-color` *"defines the background color. Any valid CSS color works,
for example a hex code (`#000000`) or an `rgb()` value."* A bare `76, 175, 80` is not a valid
CSS colour on its own — it only works if Obsidian internally wraps it as `rgb(var(--callout-color))`,
which was the older convention. The docs now describe the newer one. **Unresolved.** Cannot be
settled from documentation; it needs someone to look at a `> [!fact]` callout in the app and
confirm it is green.

**b) Lucide icon names.** The snippet uses `lucide-check-circle` and `lucide-alert-triangle`.
Lucide renamed these to `circle-check` and `triangle-alert` (shape-first scheme), keeping the
old names as aliases. Obsidian bundles **Lucide 0.446.0** (per `en/Obsidian/Credits.md`), and
the callouts doc carries an explicit warning: *"Obsidian updates Lucide icons periodically...
use these or earlier icons in custom callouts."* Whether Obsidian's `--callout-icon` resolves
deprecated aliases is undocumented. Silent failure mode: no icon renders, colour still works.
**Also needs a visual check**, and if the icons are missing, `lucide-circle-check` /
`lucide-triangle-alert` are the current names.

Neither of these affects the parts of the snippet that carry the actual evidence — the font,
size, line-height, letter-spacing, and line width all use standard CSS and will work.

---

## 7. What this means for THIS vault

Plain language, in priority order. Items 1–3 are corrections to things that are currently
wrong or missing. Items 4–8 are improvements.

### 1. Fix the false claim in `specs/vault-convention.md`

The "Seams to watch" section says the `userIgnoreFilters` list "hides non-study folders...
from the file explorer so only `learning/` and `canvas/` show." **That is not what it does**
(§1). Replace with: it hides those folders from *search, graph view, and backlinks*, and
demotes them in the Quick Switcher — but they still appear in the sidebar.

Leaving the wrong sentence in place is the real risk. It is exactly the kind of thing that
gets treated as settled six months later.

### 2. Back up the two `.obsidian/` files that are currently unprotected

`specs/obsidian-config/` holds `app.json` and `adhd-dyslexia-typography.css`. `.obsidian/` is
gitignored (`.gitignore:51`, confirmed: zero `.obsidian` files tracked). But `.obsidian/`
also contains:

- **`appearance.json`** — this is the file that contains `"enabledCssSnippets": ["adhd-dyslexia-typography"]`.
  **Without it, the CSS snippet is present but switched off, and does nothing.** The backup
  currently preserves the snippet and loses the switch that turns it on. On a new machine,
  restoring the backup produces a vault with the typography silently disabled — and nobody
  would notice for a while, because the text would just look normal.
- **`core-plugins.json`** — records which core plugins are on (Bookmarks on, Workspaces off,
  Canvas on, etc.).

Copy both into `specs/obsidian-config/`. This is the highest-value item in this section
because it is a silent data-loss path in a backup that currently *looks* complete.

### 3. Reconsider `system/` in the exclusion list

`userIgnoreFilters` currently includes `system/`. Per §1 that means `tracker.md` and
`inbox.md` are **invisible to search** and **demoted in the Quick Switcher**. Given that
`vault-convention.md` rule 1 says the tracker is the single source of durable truth, making it
unsearchable is backwards. Remove `system/` from the list. It will still be visible in the
sidebar either way — that was never what this setting controlled.

### 4. Make the sidebar actually show only study material

Two changes, both cheap, and they stack:

**(a) Use Bookmarks.** Right-click `learning/` → Bookmark. Same for `canvas/` and
`system/tracker.md`. Then collapse the file explorer and navigate from the Bookmarks tab.
Core plugin, already enabled, cannot break. This is the officially supported answer.

**(b) Add folder-hiding CSS** to the existing snippet — no new file, no new plugin, and it is
already backed up (once item 2 is done):

```css
/* Hide repo-infrastructure folders from the file explorer. Obsidian's
   "Excluded files" setting does NOT do this — it only affects search, graph,
   and backlinks. See specs/research/2026-08-10_obsidian-best-practices.md §1. */
.nav-folder-title[data-path="bin"],   .nav-folder-title[data-path="bin"]   + .nav-folder-children,
.nav-folder-title[data-path="src"],   .nav-folder-title[data-path="src"]   + .nav-folder-children,
.nav-folder-title[data-path="data"],  .nav-folder-title[data-path="data"]  + .nav-folder-children,
.nav-folder-title[data-path="docs"],  .nav-folder-title[data-path="docs"]  + .nav-folder-children,
.nav-folder-title[data-path="specs"], .nav-folder-title[data-path="specs"] + .nav-folder-children,
.nav-file-title[data-path="README.md"],
.nav-file-title[data-path="SETUP.md"],
.nav-file-title[data-path="claude-flow.config.json"],
.nav-file-title[data-path="ruvector.db"] { display: none; }
```

Keep `system/` visible — the tracker is the daily entry point.

Known risk, stated plainly: `data-path` is a DOM internal, not a supported API. If a future
Obsidian release changes it, the folders quietly reappear. That is a cosmetic regression with
an obvious symptom, and Bookmarks (a) keeps working regardless. This is why both, not either.

**Do not install Explorer Hider or File Hider** (§1, Option C).

### 5. Bump the font size 17px → 18px

`--adhd-font-size: 17px` in the snippet. Rello & Baeza-Yates (n=92) found larger text produced
significantly faster reading for dyslexic *and* control readers, and recommend 18pt. This is a
one-character change with peer-reviewed support behind it. `DECISIONS.md` §7 locks "16px+", so
this is inside the locked range — no decision needs reopening.

### 6. Set `Default view for new tabs` to Reading view

Settings → Editor → Default view for new tabs → **Reading view**.

Why: lesson files in `learning/` are content to be *read*, and reading view applies the
typography cleanly without cursor, without markdown syntax visible, and without the risk of
accidentally typing into generated study material. Editing is still one `Cmd+E` away.

Honest tradeoff: `system/tracker.md` gets edited constantly, and this setting is global, so
the tracker will also open in reading view and need a `Cmd+E`. If that becomes annoying,
revert — it is a preference, not a finding.

### 7. Tell Orlando about the Sandbox vault

Command palette → "Open sandbox vault". It opens a separate throwaway vault with tutorial
content, in its own window, that cannot touch this repo. This is where to experiment with
settings and click unfamiliar buttons. Given that the vault contains months of work and the
user is new to the app, having a designated safe place to break things is worth more than any
plugin in this brief.

Also worth telling him: **`Cmd`+scroll or trackpad pinch changes text size instantly**, no
settings trip required.

### 8. Verify the two callout items in §6

Open any note, add a `> [!fact]` callout, and check it is green with an icon. If the colour is
wrong, switch `--callout-color` to `rgb(76, 175, 80)` or `#4CAF50`. If the icon is missing,
switch to `lucide-circle-check` / `lucide-triangle-alert` / `lucide-gavel`. Sixty seconds,
and it closes the only two unresolved items in the current config.

### Explicitly NOT recommended

- **No community plugins.** Zero. Plugins get full read/write access to a vault that contains
  the codebase (§2). Homepage (1.2M downloads, Excellent scorecard, Passed review) is the only
  one with a defensible case — it would open `tracker.md` on launch, which is a real ADHD
  friction reduction. But bookmarking the tracker and pinning its tab gets ~80% of that with
  zero dependencies. **If** a plugin is ever wanted, Homepage is the one, and its listing page
  scorecard should be re-checked at install time.
- **No PARA, no Zettelkasten, no MOCs** (§3). Wrong tool, different problem, no evidence.
- **No accessibility-branded themes** (§4). The headline feature is the debunked one.
- **No Workspaces plugin** for this problem (§1) — it cannot filter the file explorer.
- **No Dataview.** It queries large heterogeneous collections. This vault has one tracker
  table with one `current` row, maintained by hand on purpose.

---

## Confidence and what would change this

**High confidence:** everything in §1 about what `Excluded files` does. It is quoted from
official documentation and corroborated by six separate per-feature doc pages and a
long-running user thread. This is settled.

**Moderate confidence:** the CSS folder-hiding approach (widely reproduced, but relies on
unpublished DOM internals), and the reading of the plugin ecosystem.

**Would change this brief:** Obsidian shipping a real ignore mechanism (`.obsidianignore`, or
gitignore support) — requested for five years with no official response, but it is the obvious
fix and would make §1's Option B obsolete. Also: if the Community directory scorecards prove
unreliable in practice, §2's recommended evaluation method weakens and the answer reverts to
"install nothing," which is what this brief recommends anyway.

**Deliberately not covered:** Obsidian Sync (paid, and `vault-convention.md` already rejected
a sync layer), Obsidian Publish, Bases, mobile setup, and Canvas mechanics — Canvas is already
covered by the visual-spatial encoding research and `vault-convention.md` rule 4.
