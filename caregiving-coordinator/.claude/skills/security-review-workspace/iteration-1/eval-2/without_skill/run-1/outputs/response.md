# XSS regression test for routes/visit-notes.js

## What I wrote

`visit-notes.xss.test.js` — a test that loads the **actual** `visit-notes.js`
route handler (not a reimplementation of its logic) and feeds it
attacker-controlled `note_text` / `author_name` values, then asserts the
resulting HTML sent via `res.send()` does not contain an unescaped
`<script>` tag or an `onerror=` attribute.

Since this file has no `package.json`/`node_modules` next to it and the
project has no test framework installed, I used Node's built-in test runner
(`node:test`, available with no install on Node >= 18 — this machine has
v26) instead of adding a dependency.

The route file does `require('express')` and `require('../db')`, neither of
which exist in this fixture-only directory. Rather than skip the real file
and test a copy, the test temporarily patches `Module._load` to hand back a
minimal fake `express.Router()` (just enough to capture the registered
`get()` handler) and a fake `../db` whose `query()` resolves with the
attacker-controlled rows. It then calls the real handler with a fake
`req`/`res` and inspects what `res.send()` was given. This way the
assertions are exercising the production code path, not a stand-in.

Four cases:
1. `note_text = '<script>alert(document.cookie)</script>'` must not appear verbatim in the output.
2. `note_text = '<img src="x" onerror="alert(1)">'` must not leave a live `onerror=` attribute in the output.
3. `author_name` with the same `<script>` payload — included because it's concatenated the same unescaped way in the same file, so it's the same bug class, not a separate issue.
4. Sanity check: an ordinary benign note's text still shows up in the output (so a fix that escapes everything into unreadable mush would also fail this).

## Did it actually run?

Yes, with `node --test visit-notes.xss.test.js`. Against the current,
unfixed `visit-notes.js`:

```
✖ note_text containing a <script> payload is not sent to the browser unescaped
✖ note_text containing an onerror-image payload is not sent to the browser unescaped
✖ author_name containing a script payload is not sent to the browser unescaped
✔ sanity check: a normal, benign note still renders its text content

tests 4
pass 1
fail 3
```

That's the expected result right now: 3 failures proving the stored-XSS
hole exists, 1 pass showing the test isn't just failing on something
unrelated. I also hand-verified the test flips to green once the handler
HTML-escapes `author_name`, `created_at`, and `note_text` before
interpolating them — so once you apply the real escaping fix in
`routes/visit-notes.js`, re-run:

```
node --test visit-notes.xss.test.js
```

and all 4 should pass. If any of the 3 XSS tests still fail after your fix,
that's a sign the escaping isn't applied to every interpolated field (e.g.
you fixed `note_text` but left `author_name` raw).

## Files produced
- `visit-notes.xss.test.js` — the test file, in this same `outputs/` folder.
- `response.md` — this write-up.
