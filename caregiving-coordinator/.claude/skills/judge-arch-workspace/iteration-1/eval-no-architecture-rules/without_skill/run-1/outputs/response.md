I can't review this against your architecture, because none is documented and I haven't seen your code. I haven't read utils/helpers.js or lookup.js, so everything below is a general expectation, not a finding about your change.

**Date formatter in utils/helpers.js**
- This is usually fine. A pure date-formatting function is a normal fit for a utility module.
- Check that it has no side effects and doesn't import app or data code.
- Watch for helpers.js turning into a grab bag. If it keeps growing, split it by topic, for example dates.js.

**User lookup moved to lookup.js**
- The name "lookup.js" is vague. Something like userRepository.js or users.js says what it owns.
- Check who imports it now. Make sure every caller was updated and nothing imports it in a circle.
- A lookup is a data-access concern. Callers such as UI code or route handlers should go through it. They shouldn't query the data store directly.
- Check how it handles errors, including a user that isn't found. Does it return null, throw, or return a default? Callers should be able to rely on one behavior.
- If it touches health or personal data, check who is allowed to call it. This is a security question, so it needs a separate security review.

**What I'd need to go further**
1. The diff or the two files.
2. Your intended layers, such as UI, services and data, and which way dependencies should point.
3. Which module owns user data.

If you don't have an architecture document yet, I can help you write a short one first. Then reviews have something to check against.
