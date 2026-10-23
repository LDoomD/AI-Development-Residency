# Vault convention

**Decided 2026-08-09.** Build order step 2.

## The vault is this repo

No separate vault directory, no sync layer, no export step. Open
`ADHD-Learning-System/` directly in Obsidian and everything is already there,
already version-controlled, already plain Markdown.

**Why:** every alternative adds a seam where material can go missing. A separate vault
means two copies drifting apart; a sync service means a dependency and an account. The
repo is already Markdown, already backed up by git, already where the specs live.

Anything Obsidian writes (`.obsidian/`) is local config and stays out of git.

---

## Folder map

| Folder | Holds | Edited by |
|---|---|---|
| `learning/` | Study material — one folder per subject | Engine + Orlando |
| `learning/<subject>/` | Numbered lesson files, `00-` prefix for the domain map | Engine |
| `system/` | `tracker.md` (sole durable state), `inbox.md` (capture) | Examiner + Orlando |
| `specs/` | Design docs, decisions, build plan | Orlando + Claude |
| `specs/research/` | Dated research briefs. Append-only in spirit — supersede, don't delete | Research agents |
| `specs/briefs/` | Research *requests* (what to go find out) | Orlando |
| `canvas/` | Obsidian Canvas files (JSON Canvas) for visual schemas | Engine + Orlando |
| `docs/` | Postmortems, session logs | Claude |

## Naming

- **Lessons:** `NN-kebab-case-title.md`, numbered in study order. `00-` is always the domain map.
- **Research:** `YYYY-MM-DD_topic-slug.md`. Date is when the research ran.
- **Canvas:** `<subject>-<concept>.canvas`, matching the lesson it belongs to.

## Rules

1. **`system/tracker.md` is the only durable state.** Not conversation history, not agent
   memory. If it isn't in the tracker, it didn't happen.
2. **Exactly one row is `current`.** This removes "what should I study today" entirely.
3. **Plain Markdown only** in `learning/` and `system/`. No Obsidian-proprietary syntax
   that would break the file outside Obsidian — the exit cost stays near zero.
4. **Canvas files are an addition, never a replacement.** Per the integration gate, a
   diagram without a written explain-back scores worse than nothing.
5. **Nothing enters `learning/` that hasn't been through a gate**, except the `00-` map
   and raw capture. Ungated material in the study folder is how you end up drilling
   things you only think you understood.

## Seams to watch

**Gemini Notebook.** Material generated there lives in Google's product, not here. Export
to Markdown into `learning/<subject>/` is manual and currently undesigned — see
`adhd-learning-system-design.md` open item 3. This is the most likely place for work to
silently accumulate outside the system.

**Obsidian local config.** `.obsidian/` is gitignored (see "Anything Obsidian writes"
above), which means anything configured there is **not backed up by git** unless a copy is
kept in `specs/obsidian-config/`. Two things currently live only there, with a versioned
backup:

- **Typography CSS snippet** — implements the locked rules in `DECISIONS.md` §7 (16px+
  sans-serif, 1.5 line-height, 60–66ch width, letter-spacing, functional-colour callouts).
  Source: `specs/obsidian-config/adhd-dyslexia-typography.css` → restore to
  `.obsidian/snippets/`, enable in Settings → Appearance → CSS snippets.
- **`userIgnoreFilters`** (`.obsidian/app.json`) — per
  `specs/research/2026-08-10_obsidian-best-practices.md` §1, this setting does **not** hide
  folders from the file explorer/sidebar — that was a wrong assumption made when it was
  first set. It only hides matching files/folders from Search, Graph view, and
  Backlinks/Unlinked mentions, and demotes them in the Quick Switcher. It's still worth
  keeping for that (search/graph noise reduction), just not for sidebar clutter — see that
  research brief for the actual sidebar fix (Bookmarks, the officially-supported option).
  Source: `specs/obsidian-config/app.json` → restore to `.obsidian/app.json`.

If `.obsidian/` is ever reset or a new machine is set up, both files need to be copied back
manually — there's no automation for this yet.
