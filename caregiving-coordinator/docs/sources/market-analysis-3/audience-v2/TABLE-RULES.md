# Rules for the new audience tables (2026-11-04)

The user has ADHD and found the old use case table (Figma 2378:7144) hard to read. These rules come from the ux-ui-design-review skill (Nielsen heuristics: aesthetic and minimalist design, recognition rather than recall, consistency; NN/g data tables) and WCAG 2.2 AA (contrast 1.4.3, text spacing 1.4.12, reading level 3.1.5).

## What made the old table hard to read
- Walls of text in every cell: two long quotes, thread IDs, and the word "ASSUMPTION" repeated.
- Small text in a very large table, with little space between rows.
- Every cell had a different length and shape, so the eye has no rhythm to follow.
- Nothing stood out: the problem, the moments and the goals all looked the same.

## Rules for the new tables
1. **One idea per bullet.** At most 4 bullets per cell, and each bullet is 12 words or fewer.
2. **No IDs, quotes, percentages, ranks or "ASSUMPTION" in the cells.** The evidence goes in one note below the table.
3. **The problem column is bold:** one sentence of 16 words or fewer.
4. **One plain number per row:** "Seen in N posts and threads", under the problem. No other numbers.
5. **Rows are numbered** and ordered from most common to least.
6. **Same start words in every cell of a column:** "When / After / During…" for moments, "We want them to…" for goals, "Help them…" for scenarios.
7. **One table per audience,** under a big title, so the reader doesn't track an extra Audience column.
8. **Readable type:**
   - Body text 28 px and the header row 32 px bold.
   - Line height 1.4, left aligned, top aligned.
   - A padded cell.
9. **Contrast:**
   - Dark text (#1E1E1E) on white or very light rows (#F5F5F5 every other row).
   - The header row is white text on dark (#1E1E1E).
   - All pass 4.5:1.
   - Color is never the only signal.
10. **Short headers,** each with a one-line question in plain words, using the teacher's four column names.
