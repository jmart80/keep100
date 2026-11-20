---
name: setup
description: First-run setup for Keep100. Builds the founder's workspace folder, drafts their company files from their website and documents, interviews only for gaps, picks the B2B or B2C track, schedules the weekly brief, builds their progress dashboard, and ends with a homepage headline rewrite. Use when the founder says "set me up", "set up Keep100", "get started", "continue setup", or has just installed Keep100 and no finished Keep100 workspace exists yet.
---

# Keep100 setup (the first session)

Kit version: 1.1.0

The founder leaves this session with two wins: **Claude set up properly for them**, and **a better headline for their own homepage**. Everything else serves those two.

Keep it moving. Ask one question at a time. Give a recommended answer with each question so the founder can just say "yes". Never ask for something you can find in their website or documents.

## Step 0: Check before starting

- **A finished workspace exists** (a `progress.md` whose Setup steps are all ticked): don't set up again. Say so and switch to `keep100:today`, or `keep100:update-workspace` if its `Kit version:` is older than the version above.
- **A half-finished workspace exists** (Setup steps unticked): say where it stopped and continue from the first unticked step. Never redo confirmed work.
- **No folder access** (claude.ai in a browser or on a phone): you can't create folders. Run the same steps, but give each workspace file to the founder as text to save into their Keep100 Project, following `docs/guides/browser-setup.md` in the Keep100 repo. Skip step 6.1.
- Say in two sentences what's about to happen, that it takes about an hour, that it can be split across two sittings, and that Keep100 needs a paid Claude plan to run well.

## Step 1: Create the workspace

1. Ask their first name and product name.
2. Ask where the folder should live. Recommend `Documents/Keep100`. If you don't have access to that location, ask them to choose or connect the folder in the app.
3. Copy everything in this skill's `workspace/` folder into it, keeping the structure.
4. Fill the placeholders: `{{FOUNDER_NAME}}`, `{{PRODUCT_NAME}}`, `{{START_DATE}}` (today), `{{KIT_VERSION}}` (the version above). Leave the track, hours and email placeholders for step 4.
5. Tick "Workspace created" in `progress.md`.

Done when: the folder exists with every template file and no placeholders except track, hours and emails.

## Step 2: Gather what already exists

Ask for, in this order, and accept whatever they have:
1. Their website address. Read the home, pricing, about and FAQ pages, and stop at about ten pages.
2. Any documents: pitch notes, product docs, FAQ, past posts, customer emails, call notes. Ask them to drop files into `company/sources/` or paste text.
3. Their app, if it's public, and any demo video.

If the Exa connector isn't connected, mention once that connecting it makes research much better later, and that they can add it under connectors in settings. Don't block on it.

Done when: you've read everything they offered, or they've said there's nothing more.

## Step 3: Draft the company files

From the material only, draft `product.md`, `customers.md`, `pricing.md` and `brand.md`. Leave `positioning.md` and `competitors.md` for later steps.

Rules:
- Each fact goes in one file. Prices go in `pricing.md`, features in `product.md`. Put in `facts.md` only proof that has no other home (results, credentials, named customers, testimonials), marked `[unconfirmed]` with its source.
- Quote customer language word for word, tagged as the template shows. If you did not see the exact words, tag it `[paraphrase]`.
- Write "unknown" for anything the material doesn't say. Don't infer prices, user counts or results. Silence is unknown, never "none": if the founder didn't mention discounts, a guarantee, a trial length or a competitor, write "unknown", not "no discounts".
- For `brand.md`, describe the voice their existing writing actually has, with an example sentence from it.

Tick "Company files drafted".

## Step 4: Fill the gaps and pick the track

Interview only for what's missing, highest-value gaps first, at most about eight questions. Always include:

1. **Track:** "Who pays you: businesses, or individual people?" Businesses means B2B, people means B2C. If both, pick the one bringing more revenue now. They can switch later.
2. **Ideal customer:** push for narrow. "Small businesses" is not an answer. "Independent physiotherapy clinics with 2 to 5 staff" is.
3. **What they use today instead**, including doing nothing.
4. **What's live and what isn't**, so Claude never promises a feature that doesn't exist.
5. **How a customer would pay:** "If someone said yes today, how would they pay you?" Record the answer in `pricing.md`. If there is no way yet, say that the pricing step will set one up.
6. **Time:** "How many hours a day can you give this?" Recommend an honest number. One focused hour is enough to run the plan.

Fill the placeholders in `CLAUDE.md` and `progress.md`. The daily email number is the kit's starting default, not something the founder said. When you report it, say so: "5 new emails a day to start, which you can change."
- B2B: `{{TRACK_NOTE}}` = "Customers come from direct outreach first: finding the right people and writing to them. Social is optional (LinkedIn)." `{{DAILY_NEW_EMAILS}}` = 5 for up to an hour a day, 10 for two hours or more. Delete the "Getting customers (B2C)" section from `progress.md`.
- B2C: `{{TRACK_NOTE}}` = "Customers come from social media and short video first. No cold email." `{{DAILY_NEW_EMAILS}}` = "not used". Delete the "Getting customers (B2B)" section from `progress.md`.

## Step 5: Confirm

Walk through the drafted files one at a time. Show every fact line in the file, grouped under its headings, without the template comments. Ask "anything wrong or missing?", apply their corrections, then set `Status: Confirmed` and `Last confirmed:` to today. A founder can only confirm what they have seen, so never confirm a file from a summary. In `facts.md`, mark an entry `[confirmed]` only when they approved that entry. Anything they aren't sure about stays unconfirmed.

Done when: product, customers, pricing and brand are Confirmed, or the founder has explicitly left one as Draft. Tick "Company files confirmed".

**Checkpoint.** Run `keep100:dashboard` so the founder sees their progress page for the first time. Tell them this is a safe place to stop, and that saying "continue setup" picks up from here.

## Step 6: Weekly brief and settings

1. **Weekly brief:** create a scheduled task for Monday at 9am their time that runs the `keep100:weekly-brief` skill, and attach this workspace folder to the task. A scheduled task with no folder runs in the cloud and cannot see the workspace. Tell them the brief runs when their computer is awake with the Claude app open. If scheduled tasks aren't available to you, tell them where to set one up in the app with that instruction. Tick "Weekly brief scheduled", or mark it skipped with the reason.
2. **Project (desktop app):** if the app offers projects, suggest they create one named Keep100 on this folder, with one instruction: "Read CLAUDE.md in this folder first and follow it." It keeps every Keep100 chat in one place.
3. **Account instructions:** give them this text to paste into their Claude settings, in the field where Claude asks what it should know about them, and say why (so chats outside the workspace don't guess about their company):

```
I'm a solo SaaS founder using Keep100. My company facts live in my Keep100 folder under company/. Before stating anything about my product, customers, pricing or brand, read those files. If you can't open them in this chat, say so and ask me instead of guessing or relying on memory. Write in plain language and recommend one option rather than listing many.
```

## Step 7: First win, the homepage headline

1. Quote their current homepage headline and subheadline exactly. If they have no website yet, use the one sentence they'd use to describe the product.
2. Score the current version on three questions, one line each: would a stranger know **what it is**, **who it's for**, and **why it's different** within five seconds?
3. Write 3 new headline and subheadline pairs using only confirmed facts and the customer's own words. Headline max 10 words, and it must contain at least one of: what the product is, who it's for, what it replaces, or a real measurable result. The subheadline (max 25 words) supplies whatever the headline left out.
4. Run `keep100:writing-check` on them.
5. Show the before and after side by side and recommend one, with the reason in a sentence.
6. Save to `marketing/<date>-homepage-headline.md`, tick "Homepage headline rewritten" and add a Work log line.

Say plainly this is a quick win from what Claude knows today, and that positioning will sharpen it further.

## Step 8: Show how their Claude is now set up

End with a short summary, in plain language, of what changed and why it matters. Cover:
- **The workspace:** one folder for all growth work, so nothing is lost between chats.
- **Company files:** one source of truth. Change a fact once and everything uses it.
- **Confirmed facts:** Claude only states what they've approved, and says "I don't know" otherwise.
- **House rules:** `CLAUDE.md` tells Claude how to work with them every time.
- **The dashboard:** their checklist, ticked off as work gets done. Run `keep100:dashboard` again and show it.
- **Daily driver:** from tomorrow, open a chat in this folder and ask "what's today?"
- **Weekly brief:** arrives Mondays.
- **Back it up:** suggest keeping the folder somewhere with version history, such as a synced drive, because one bad edit can undo an hour of confirming.

Then propose the next step: "Next: competitor research, about 30 minutes. Want to start now or tomorrow?"
