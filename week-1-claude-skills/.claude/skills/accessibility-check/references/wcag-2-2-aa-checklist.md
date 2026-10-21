# WCAG 2.2 level AA checklist for code review

Source: W3C, WCAG 2.2 (12 December 2024), https://www.w3.org/TR/WCAG22/
Check the exact wording of any criterion there before quoting it.
Criterion 4.1.1 Parsing was removed in WCAG 2.2, so do not report it.
Items marked NEW were added in WCAG 2.2.

Contents: Perceivable, Operable, Understandable, Robust, What code reading cannot prove

## Perceivable

- **1.1.1 Non-text content (A):** images have `alt` text that says what the
  image means. Decorative images use `alt=""`. Icon-only buttons have a name.
- **1.3.1 Info and relationships (A):** headings use heading tags, lists use
  list tags, tables use header cells, form labels are tied to inputs.
- **1.3.5 Identify input purpose (AA):** personal fields use `autocomplete`
  values (name, email, address).
- **1.4.1 Use of color (A):** color is never the only way to show an error,
  required field, or selected state.
- **1.4.3 Contrast minimum (AA):** text needs a ratio of at least 4.5 to 1.
  Large text needs at least 3 to 1.
- **1.4.4 Resize text (AA):** text can grow to 200 percent without losing
  content. Look for fixed pixel heights and `overflow: hidden`.
- **1.4.10 Reflow (AA):** content works at 320 CSS pixels wide with no
  sideways scrolling, except for things like data tables and maps.
- **1.4.11 Non-text contrast (AA):** input borders, icons, and focus rings
  have at least 3 to 1 contrast.
- **1.4.12 Text spacing (AA):** layout survives larger line, letter, and word
  spacing.
- **1.4.13 Content on hover or focus (AA):** tooltips can be dismissed,
  hovered over, and stay until dismissed.

## Operable

- **2.1.1 Keyboard (A):** every action works without a mouse. Watch for
  click handlers on `div` or `span`.
- **2.1.2 No keyboard trap (A):** focus can always move away, including from
  dialogs (use Escape to close).
- **2.4.1 Bypass blocks (A):** a "skip to main content" link or landmarks.
- **2.4.2 Page titled (A):** each page has a clear `title`.
- **2.4.3 Focus order (A):** tab order follows the visual and logical order.
  Watch for positive `tabindex` values.
- **2.4.4 Link purpose (A):** link text makes sense in context. Avoid bare
  "click here".
- **2.4.6 Headings and labels (AA):** headings and labels describe their
  content.
- **2.4.7 Focus visible (AA):** keyboard focus is visible. Watch for
  `outline: none` with no replacement.
- **2.4.11 Focus not obscured, minimum (AA) NEW:** a focused item is not fully
  hidden by sticky headers, banners, or cookie bars.
- **2.5.3 Label in name (A):** the visible label text is part of the
  accessible name.
- **2.5.7 Dragging movements (AA) NEW:** anything done by dragging also has a
  simple click or tap alternative.
- **2.5.8 Target size, minimum (AA) NEW:** pointer targets are at least 24 by
  24 CSS pixels, with listed exceptions such as inline links in text.

## Understandable

- **3.1.1 Language of page (A):** `lang` is set on `html`.
- **3.2.1 On focus and 3.2.2 On input (A):** focus or typing does not cause
  surprise changes of context.
- **3.2.3 Consistent navigation and 3.2.4 Consistent identification (AA):**
  navigation and same-purpose controls look and are named the same across pages.
- **3.2.6 Consistent help (A) NEW:** help links or contact options appear in
  the same place across pages.
- **3.3.1 Error identification (A):** errors are described in text and tied
  to the field.
- **3.3.2 Labels or instructions (A):** inputs have labels or hints.
- **3.3.3 Error suggestion (AA):** the message says how to fix the error.
- **3.3.4 Error prevention for legal, financial, data (AA):** submissions can
  be reviewed, corrected, or undone.
- **3.3.7 Redundant entry (A) NEW:** the user is not asked to retype
  information already given in the same process.
- **3.3.8 Accessible authentication, minimum (AA) NEW:** logins do not depend
  on remembering or retyping a puzzle or code. Allow paste and password
  managers.

## Robust

- **4.1.2 Name, role, value (A):** custom controls expose a name, role, and
  state. Prefer native elements (`button`, `a`, `input`, `select`) over
  ARIA. ARIA is a set of attributes that add accessibility meaning, and bad
  ARIA is worse than none.
- **4.1.3 Status messages (AA):** messages such as "saved" or "3 results"
  are announced, for example with `role="status"` or `aria-live`.

## What code reading cannot prove

Report these as "needs manual testing":

- real contrast on the rendered page
- screen reader behavior (try VoiceOver on Mac)
- true focus order and focus visibility in the browser
- zoom and reflow on real screens
- automated checks (axe, Lighthouse) catch only part of all problems, so
  keyboard-only use and a screen reader pass are still needed
