---
name: setup
description: First-run setup for Keep100. Builds the founder's workspace folder, drafts their company files from their website and documents, interviews only for gaps, picks the B2B or B2C track, schedules the weekly brief, and ends with a homepage headline rewrite. Use when the founder says "set me up", "set up Keep100", "get started", or has just installed Keep100 and no Keep100 workspace exists yet.
---

# Keep100 setup (the first session)

The founder leaves this session with two wins: **Claude set up properly for them**, and **a better headline for their own homepage**. Everything else serves those two.

Keep it moving. Ask one question at a time. Give a recommended answer with each question so the founder can just say "yes". Never ask for something you can find in their website or documents.

## Step 0: Check before starting

- If a folder with a Keep100 `progress.md` already exists where you're working, don't set up again. Say so and switch to `keep100:today` (or `keep100:update-workspace` if its `Kit version:` is older than this plugin's version).
- Confirm they're on a paid Claude plan. If not, point them to the README requirements and stop.
- **Browser (claude.ai) users:** you can't create folders. Run the same steps, but give each workspace file to the founder as text to save into their Keep100 Project's knowledge (company files) and instructions (`CLAUDE.md`), following `docs/guides/browser-setup.md` in the Keep100 repo. Skip scheduling the weekly brief.
- Tell them in two sentences what's about to happen and that it takes about an hour.

## Step 1: Create the workspace

1. Ask their first name and product name.
2. Ask where the folder should live. Recommend `Documents/Keep100`. If you don't have access to that location, ask them to choose or connect the folder in the app.
3. Copy everything in this skill's `workspace/` folder into it, keeping the structure.
4. Fill the placeholders: `{{FOUNDER_NAME}}`, `{{PRODUCT_NAME}}`, `{{START_DATE}}` (today), `{{KIT_VERSION}}` (this plugin's version from `plugin.json`). Leave `{{TRACK}}` and `{{TRACK_NOTE}}` for step 4.

Done when: the folder exists with every template file and no placeholders except track.

## Step 2: Gather what already exists

Ask for, in this order, and accept whatever they have:
1. Their website address. Read every page you can reach (home, pricing, about, FAQ, docs).
2. Any documents: pitch notes, product docs, FAQ, past posts, customer emails, call notes. Ask them to drop files into `company/sources/` or paste text.
3. Their app, if it's public, and any demo video.

If the Exa connector isn't connected, mention once that connecting it makes research much better later, and that they can add it under connectors in settings. Don't block on it.

Done when: you've read everything they offered, or they've said there's nothing more.

## Step 3: Draft the company files

From the material only, draft `product.md`, `customers.md`, `pricing.md` and `brand.md`, and add every fact you found to `facts.md` as `[unconfirmed]` with its source. Leave `positioning.md` and `competitors.md` for days 2 and 3.

Rules:
- Quote customer language word for word, with where it came from.
- Write "unknown" for anything the material doesn't say. Don't infer prices, user counts or results.
- For `brand.md`, describe the voice their existing writing actually has, with an example sentence from it.

## Step 4: Fill the gaps and pick the track

Interview only for what's missing, highest-value gaps first, at most about eight questions. Always include:

1. **Track:** "Who pays you: businesses, or individual people?" Businesses means B2B, people means B2C. If both, pick the one bringing more revenue now; they can switch later.
2. **Ideal customer:** push for narrow. "Small businesses" is not an answer; "independent physiotherapy clinics with 2 to 5 staff" is.
3. **What they use today instead**, including doing nothing.
4. **What's live and what isn't**, so Claude never promises a feature that doesn't exist.

Fill the track placeholders in `CLAUDE.md` and `progress.md`:
- B2B: `{{TRACK_NOTE}}` = "Customers come from direct outreach first: finding the right people and writing to them. Social is optional (LinkedIn)."
- B2C: `{{TRACK_NOTE}}` = "Customers come from social media and short video first. No cold email."

## Step 5: Confirm

Walk through the drafted files one at a time. For each, show a short summary (not the whole file), ask "anything wrong or missing?", apply their corrections, then set `Status: Confirmed` and `Last confirmed:` to today. In `facts.md`, mark each fact `[confirmed]` once they've approved it. Anything they aren't sure about stays `[unconfirmed]`.

Done when: product, customers, pricing and brand are Confirmed, or the founder has explicitly left one as Draft.

## Step 6: Weekly brief and settings

1. **Weekly brief:** create a scheduled task for Monday at 9am their time that runs the `keep100:weekly-brief` skill in this workspace. If scheduled tasks aren't available to you, tell them where to set one up in the app with that instruction, and move on.
2. **Account instructions:** give them this text to paste into their Claude settings, in the profile instructions field where Claude asks what it should know about them, and tell them why (so even chats outside the workspace check their company files before stating facts):

```
I'm a solo SaaS founder using Keep100. My company facts live in my Keep100 folder under company/. Before stating anything about my product, customers, pricing or brand, read those files. Only state facts marked [confirmed]. If you don't know something about my business, ask me instead of guessing. Write in plain language and recommend one option rather than listing many.
```

## Step 7: First win, the homepage headline

1. Quote their current homepage headline and subheadline exactly. If they have no website yet, use the one sentence they'd use to describe the product.
2. Score the current version on three questions, one line each: would a stranger know **what it is**, **who it's for**, and **why it's different** within five seconds?
3. Write 3 new headline and subheadline pairs using only confirmed facts and the customer's own words. Headline max 10 words, and it must contain at least one of: what the product is, who it's for, what it replaces, or a real measurable result. The subheadline (max 25 words) supplies whatever the headline left out. No hype words (revolutionize, supercharge, unlock, seamless, transform, empower, streamline, leverage).
4. Run `keep100:writing-check` on them.
5. Show the before and after side by side and recommend one, with the reason in a sentence.
6. Save to `marketing/<date>-homepage-headline.md` and log it in `progress.md`.

Say plainly this is a quick win from what Claude knows today, and that positioning on days 2 and 3 will sharpen it further.

## Step 8: Show how their Claude is now set up

End with a short summary, in plain language, of what changed and why it matters. Cover:
- **The workspace:** one folder for all growth work, so nothing is lost between chats.
- **Company files:** one source of truth. Change a fact once and everything uses it.
- **Confirmed facts:** Claude only states what they've approved, and says "I don't know" otherwise. This is what stops Claude making things up about their product.
- **House rules:** `CLAUDE.md` tells Claude how to work with them every time.
- **Daily driver:** from tomorrow, open a chat in this folder and ask "what's today?"
- **Weekly brief:** arrives Mondays.

Tick the day 1 items in `progress.md`, then propose day 2: "Tomorrow: competitor research, about 30 minutes. Want to start now or tomorrow?"
