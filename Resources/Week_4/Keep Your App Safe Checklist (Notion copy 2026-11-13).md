# Keep Your App Safe Checklist
- Source copy: https://app.notion.com/p/68c9219a46918309b206016d623d1cf3
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:24.462Z
- Not saved: none

---

> ⚠️ Your GitHub repository is public. Anyone on the internet can read every file in it. Check every item on this list before you push.

# Keep your keys secret

- [ ] My Supabase keys are in a file called `.env.local`, not in my code.
- [ ] My `.gitignore` file lists `.env.local`, so Git never uploads it. Ask Claude: "Check that my .env.local file is in .gitignore and has never been committed."
- [ ] I added my keys to Vercel's environment variable settings, so the live app can use them.
- [ ] The Supabase secret key (also called the service\_role key) is never used in the browser. Supabase says: "Never use a secret key in the browser or expose it to customers." It skips your access rules.
- [ ] If a secret key ever went to GitHub, I made a new key in Supabase right away. Deleting the file is not enough, because GitHub keeps the history.

# Keep people's information private

- [ ] RLS is turned on for every table. See the Database Design Template.
- [ ] Each person can see and change only their own information.
- [ ] I tested this with two accounts.

# Use fake data only

- [ ] I use made-up names, numbers, and money amounts when I test.
- [ ] I never type my real bank or card information into my app.

# Ask Claude to check

Ask Claude Code: "Check my app for security problems. Look for secret keys in my code, tables without access rules, and places where one person could see another person's information. Explain each problem in plain language before you fix it."
