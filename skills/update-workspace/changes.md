# Workspace changes by version

Each change has an id, whether skills need it, a plain sentence for the founder, and the exact edit. New versions go at the top.

## 1.1.0

### 1.1.0-progress
Needed: yes. The daily driver and the dashboard read the new layout.
Say: "Your progress file becomes a checklist of steps, so I can show you a dashboard and you never lose your place when you take days off."
Do: Rewrite `progress.md` to the 1.1.0 template layout. Carry over the track and start date. Tick every step the old file shows as done. Keep the Paying customers table and every Work log line unchanged. Ask the founder for `Hours a day:`. Delete the "Getting customers" section for the track they are not on.

### 1.1.0-pipeline
Needed: yes, on the B2B track.
Say: "Everyone you've contacted moves into one list, so follow-ups are never missed and nobody is logged twice."
Do: Create `sales/pipeline.csv` with the header from the template. Move each person in the old Getting customers table and in `sales/prospects.md` into one row each. Leave any column you can't fill blank. Show the founder the result, then remove the old table and offer to delete `sales/prospects.md`. Create `social/posted.csv` and move logged posts into it.

### 1.1.0-positioning-fields
Needed: yes. Cold email, prospect list and landing page read these.
Say: "Your positioning file gets places for who to win first, the champion, their top objection and your value props."
Do: Add any missing headings from the 1.1.0 `company/positioning.md` template, in template order, below the founder's existing content. Don't fill them in. If positioning was already done, offer to rerun `keep100:positioning` to fill the new ones.

### 1.1.0-pricing-product-fields
Needed: yes.
Say: "Your pricing and product files get places for how a customer pays, your founding offer, and the first thing a new user should do."
Do: Add to `company/pricing.md`: How a customer pays, Founding offer, When to revisit. Add to `company/product.md`: Signup or payment link, Key action, How the product sends email. Headings only.

### 1.1.0-one-home-per-fact
Needed: no, recommended.
Say: "Prices and features listed in your facts file are also in your pricing and product files. I'll remove the duplicates so a price can never be right in one place and wrong in another."
Do: List each `facts.md` entry that repeats something in `pricing.md` or `product.md`. On a yes, delete those entries from `facts.md`. If the two copies disagree, ask which is right first. Rename the facts sections to Results, Customers and testimonials, Company and founder.

### 1.1.0-quote-tags
Needed: no, recommended.
Say: "Each customer quote gets a tag saying whose customer said it and whether it's word for word, so copy only quotes real words."
Do: In `company/customers.md`, tag every existing quote `[paraphrase]` unless its source link or file shows the exact words. Tag whose customer spoke. Don't reword any quote.

### 1.1.0-new-files
Needed: yes.
Say: "You get a place for what's worked, a place for decisions, and a folder for customer conversations."
Do: Create `learnings.md`, `decisions.md` and `conversations/CLAUDE.md` from the template. Add `## Words we allow` to `company/brand.md`. Replace the four area `CLAUDE.md` files with the 1.1.0 versions only if the founder has not edited them. If they have, show the new lines and add them below theirs.

### 1.1.0-house-rules
Needed: yes.
Say: "The house rules now say where each fact lives, tell me to trust your files over my memory, and keep your dashboard current."
Do: Show the founder the 1.1.0 `CLAUDE.md` template beside theirs. Replace the Facts section, the file table and the Saving work section. Keep anything they added.

### 1.1.0-weekly-brief-folder
Needed: yes, if the weekly brief is scheduled.
Say: "Your Monday brief needs your Keep100 folder attached, or it runs without your files."
Do: Check the scheduled task has the workspace folder attached. If you can't check or change it, tell the founder where to do it in the app.

### 1.1.0-account-instructions
Needed: no, recommended.
Say: "The note in your Claude settings should tell me to ask you when I can't open your files, instead of guessing."
Do: Give the founder the account instructions text from the setup skill, step 6, to paste over the old one.

## 1.0.0
First release. No changes to apply.
