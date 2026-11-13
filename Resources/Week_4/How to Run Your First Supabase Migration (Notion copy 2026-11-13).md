# How to Run Your First Supabase Migration
- Source copy: https://app.notion.com/p/0bf9219a469183e0a41281d0bd0e08d2
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:23.174Z
- Not saved: none

---

This guide shows you how to take the database code you wrote and make it real. By the end you will have a live database, your tables created, your secret keys stored safely, and your data loaded. Follow the steps in order. Each step says what to do and why it matters.

## What a migration is

A migration is a plain text file full of SQL commands. It usually creates your tables and sets their rules. You keep this file inside your code project. That way every person on your team can build the same tables in the same way, and you have a written history of every change you made to the database.

## Before you start

You need three things. You need a free Supabase account. You need your project code open on your computer, including your migration file. You need a terminal, which is the command line, open in your project folder.

## Steps

1. **Set up your Supabase project.** Supabase is your database. It is the place where your app's information is stored. Without it, your tables have nowhere to live. Go to [supabase.com](http://supabase.com) and sign in. Click New Project. Give it a name, create a strong database password, and save that password somewhere safe. Pick a region that is close to the people who will use your app, because closer servers are faster. Then wait a minute for Supabase to finish building the project.
2. **Find your project's address and keys.** Your code needs two things to talk to the database. It needs the web address of your project, which is called the Project URL. It also needs a key that proves your code is allowed in. Open Settings, then API. Copy the Project URL. On the same screen you will see two keys. The anon key is safe to use in a web browser. The service\_role key is a secret master key that can do anything, so you must keep it private. You will use the service\_role key later to load your data.
3. **Open your migration file in your code.** This is the SQL file you wrote, usually in a folder named something like supabase/migrations. Open it and read it once. Make sure it has the CREATE TABLE commands you expect. Reading it now means you will not get surprised when you run it.
4. **Open the SQL Editor in Supabase.** The SQL Editor is a page in the Supabase dashboard where you can run SQL against your real database. This is the tool that will actually build your tables. In the dashboard, click SQL Editor, then click New query.
5. **Paste your migration and run it.** Copy all of the SQL from your migration file and paste it into the editor. Click Run. This sends your commands to the database and creates your tables. If you see a success message, your tables now exist. If you see an error, read it closely, because it usually names the exact line that is wrong.
6. **Check your tables in the Table Editor.** You want to see with your own eyes that the tables are really there. Checking now saves you from confusion later. Click Table Editor in the dashboard. You should see each table you created. If you turned on Row Level Security, you will see a small shield on the table. That is a good thing. It means the table is locked by default, and no one can read or write it unless you write a rule that allows it.
7. **Create your .env file.** Your app needs the Project URL and the secret key, but you must never type secrets directly into your code. Code gets shared and pushed online, and a secret inside your code is a secret that everyone can see. A .env file is a private file that stays on your computer and holds your secrets. In your project folder, create a file named .env. Add these two lines, and paste your real values after the equals signs:

```javascript
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-secret-service-role-key
```

Do not put spaces around the equals sign. Do not put quotes around the values. Keep each value on one line.

8. **Make sure git ignores your .env file.** If your .env file gets uploaded to GitHub, your secret key is exposed to anyone who can see the repo. A file named .gitignore tells git which files to leave out. Open your .gitignore and make sure it has a line that says .env. You can test it by running this command in your terminal:

```javascript
git check-ignore .env
```

If it prints .env, you are safe. If it prints nothing, add .env to your .gitignore and try again.

9. **Load your data into the tables.** Your tables are empty until you fill them. A load script, sometimes called a sync or a seed script, reads your data and writes it into the database using the key from your .env file. Run your project's load command. Many Node projects can read the .env file for you with this pattern:

```javascript
node --env-file=.env your-load-script.js
```

Watch for a success message. A good script tells you how many rows it wrote. A note for Windows users: in PowerShell you cannot put the keys in front of the command the way you can on a Mac. Writing VAR=value before a command is a Mac and Linux shell trick. Use the --env-file way shown above, or set the values in your shell first.

10. **Confirm your data loaded.** Trust your tools, but check their work. Open the Table Editor one more time and look at the row counts. They should match what you expected to load. If the counts look right, your database is ready to use.

## Keep your keys safe

Never paste your service\_role key into a chat, an email, or a message. Treat it like the password to your database, because that is what it is. If it ever leaks, go to Supabase right away and reset the key. The anon key is fine to use in a browser, but the service\_role key must always stay secret.
