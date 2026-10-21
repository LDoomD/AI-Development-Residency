---
name: accessibility-check
description: Reviews web pages or UI code for accessibility problems against WCAG 2.2 level AA and reports each finding with its severity and a fix. Use when the user asks to check accessibility, a11y, WCAG, keyboard support, screen reader support, color contrast, form labels, or says a UI is ready to ship. Make sure to use this skill whenever a user interface is about to be called finished, even if the user never says "accessibility". Do not use for visual design critique, general usability review, security review, or backend code with no user interface.
---

# Accessibility Check

Review a user interface for barriers that stop people from using it. People who
use only a keyboard, a screen reader (software that reads the screen aloud),
magnification, or who have low vision or color blindness all depend on this.

The standard is WCAG 2.2 level AA. WCAG means Web Content Accessibility
Guidelines, published by the W3C. Level A is the minimum, AA is the level most
laws and buyers ask for, and AAA is the highest.

## Ground rules

- **Report evidence, not opinions.** Every finding names the file and line, or
  the page element, and the WCAG success criterion it breaks (for example
  `1.4.3`).
- **Never say "accessible" or "compliant".** Code reading finds problems. It
  cannot prove there are none. Say "no problems found in what was checked".
- **State what you could not check.** Reading code cannot test real screen
  readers, real color contrast on rendered pages, or focus order in a browser.
  List those as "needs manual testing".
- **Review first, change later.** Do not edit files unless the user asks for
  fixes after seeing the report.
- **Plain language.** Explain each term the first time you use it.

## Before you start

1. Find out what to review. If the user did not say, ask one question: "Which
   page, component, or folder should I check?"
2. Look at the project: framework (HTML, React, Vue and so on), styling
   approach, and any existing accessibility tools in `package.json`.
3. Read `references/wcag-2-2-aa-checklist.md`. It lists the criteria to check
   and what to look for in code.

## Workflow

1. **Scan structure.** Page language, page title, headings in order, landmarks
   (`header`, `nav`, `main`, `footer`), and links that skip to main content.
2. **Scan images and media.** Text alternatives, captions, and decorative
   images marked as decorative.
3. **Scan forms.** Every input has a visible label tied to it, errors are
   explained in text, required fields are marked, and autofill hints are set.
4. **Scan keyboard use.** Everything clickable can be reached and used with
   the keyboard, focus is visible, focus order makes sense, nothing traps focus,
   and focus is not hidden behind sticky bars.
5. **Scan color and size.** Contrast ratios, information carried by color
   alone, text resizing, reflow at narrow widths, and touch target size.
6. **Scan custom controls.** Anything built from `div` or `span` that acts as
   a button, menu, dialog, or tab needs the right role, name, and state.
7. **Scan changes and messages.** Status messages and errors that appear
   without a page reload must be announced to assistive technology.
8. **Write the report** with `assets/accessibility-report-template.md`.

## Severity

- **Blocker:** a person cannot complete a core task (for example a form cannot
  be submitted by keyboard).
- **Serious:** the task is possible but hard or confusing.
- **Minor:** a small barrier or a best-practice gap.

## Quality check before finishing

- Every finding has a location, a WCAG criterion, a severity, and a fix.
- No finding is a guess. If unsure, move it to "needs manual testing".
- The report lists what was checked and what was not.
- The report does not use the words "compliant" or "fully accessible".
- Suggest a next step, such as running an automated checker (axe or Lighthouse)
  and a quick keyboard-only test.

## If something goes wrong

- **No UI code is found.** Say so and ask what to review.
- **The project is not a web app** (mobile or desktop). Say that WCAG still
  guides the work, but platform guidelines also apply, and limit the review to
  what can be judged from the code.
- **There are hundreds of findings.** Group repeated problems, report the
  pattern once with a count, and list the top ten by severity.

## Files in this skill

- `references/wcag-2-2-aa-checklist.md`: the criteria and what to look for.
- `assets/accessibility-report-template.md`: the format of the report.

## Sources

W3C, Web Content Accessibility Guidelines (WCAG) 2.2, Recommendation of
12 December 2024: https://www.w3.org/TR/WCAG22/
