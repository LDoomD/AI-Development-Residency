# Code review checklist

Based on the idea in Google's Engineering Practices guide: approve a change
once it definitely improves the overall health of the code. Read the guide for
the full wording: https://google.github.io/eng-practices/review/reviewer/standard.html

Contents: Design, Behavior, Complexity, Tests, Naming and comments, Style and consistency, Documentation, Comment labels

## Design

- Does the change belong here, and fit how the rest of the project is built?
- Is it a good time to add it, or does it add things nobody needs yet?

## Behavior

- Does the code do what the author intended, and is that good for users?
- Edge cases: empty input, huge input, wrong input, slow network, failures.
- If it handles several users or tasks at once, are there race conditions
  (two actions interfering with each other)?

## Complexity

- Could a new teammate understand each part quickly?
- Is anything more general or clever than it needs to be?
- Is there copied code that should be shared, or shared code that is too
  tangled?

## Tests

- New behavior has tests; bug fixes have a test that failed before the fix.
- Tests check behavior, not just that code runs.
- Tests would actually fail if the code broke. Be wary of tests with no
  assertions.

## Naming and comments

- Names say what things are or do.
- Comments explain why, not what. Remove stale comments and commented-out code.

## Style and consistency

- Matches the project's existing style and formatter.
- Do not mix style cleanups with behavior changes in one review.

## Documentation

- README, setup steps, and examples still match the code.
- New settings, commands, or environment variables are documented.
- Big decisions have a decision record.

## Comment labels

Label each review comment so the author knows what matters:

- **Blocking:** must be fixed before it is ready.
- **Suggestion:** an improvement worth making.
- **Nit:** a tiny point the author can skip.
- **Question:** something to understand.
