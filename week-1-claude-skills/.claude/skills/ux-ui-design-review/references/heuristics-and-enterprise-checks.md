# Heuristics and enterprise checks

Sources: Nielsen Norman Group (NN/g). Read the articles for the full wording
before quoting. Links are in SKILL.md.

Contents: The 10 heuristics, Enterprise checks, Questions to ask while walking a task, Common enterprise problems

## The 10 usability heuristics (Nielsen)

1. **Visibility of system status:** the screen shows what is happening
   (loading, saved, failed).
2. **Match between system and the real world:** words and ideas the user
   already knows, not internal jargon.
3. **User control and freedom:** a clear way to undo, cancel, or go back.
4. **Consistency and standards:** the same thing looks and works the same
   everywhere.
5. **Error prevention:** stop mistakes before they happen with confirmations,
   sensible defaults, and constraints.
6. **Recognition rather than recall:** show options instead of making people
   remember them.
7. **Flexibility and efficiency of use:** shortcuts and saved views for
   experts, simple paths for new users.
8. **Aesthetic and minimalist design:** show what matters now; hide the rest.
9. **Help users recognize, diagnose, and recover from errors:** plain-language
   messages that say what went wrong and how to fix it.
10. **Help and documentation:** easy to find, specific to the task.

## Enterprise checks

NN/g's guidance for complex applications covers these themes. Check the
articles for the exact guidelines.

- **Progressive disclosure:** show common options first and reveal advanced
  ones on request.
- **Flexible workflows:** people can do steps in different orders, save work,
  and come back.
- **Expert accelerators:** keyboard shortcuts, bulk actions, saved filters.
- **In-context help:** help appears where the question arises.
- **Error prevention in high-risk actions:** deleting, sending, paying, and
  bulk changes ask for confirmation and can be undone.
- **Data tables:** users can scan, sort, filter, find records, and act on
  rows. Check column choices, alignment, and large-data behavior. NN/g's
  article describes four user tasks for tables.
- **Role-based views:** each role sees what it needs and no clutter.
- **Consistency through a design system:** shared components reduce effort
  for both users and developers. A design system does not replace a full
  review of each flow.

## Questions to ask while walking a task

- What does the user see first, and is it the thing they need?
- What would they click next, and is it obvious?
- How do they know it worked?
- How do they undo it?
- What if the list is empty, or has 10,000 rows?
- What if they are interrupted halfway?

## Common enterprise problems

- Too many fields and options on one screen
- Internal terms instead of user words
- No feedback after saving or submitting
- Destructive actions with no confirmation or undo
- Dense tables with no sorting, filtering, or saved views
- Different names or buttons for the same action across screens
- Error messages such as "Error 500"
