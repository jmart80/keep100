---
name: activation
description: Finds out why people who sign up for a Keep100 founder's product do not get to the point of paying, and fixes the path from the first click to the first moment of value. Walks the signup and first session step by step, sorts every step into keep, defer, prefill or cut, and hands the founder plain-language change requests they can paste into their app builder or send to a developer. Also sets up hands-on onboarding for the first twenty users. Use when the founder has signups or trial users, before or alongside product emails, or when they say signups are not converting, nobody comes back, people sign up and disappear, the trial is not working, or ask about onboarding, the signup form, the first-run experience, or whether to ask for a credit card.
---

# Activation

Adapted from the signup and onboarding skills in coreyhaines31/marketingskills (MIT).

Emails remind people to come back. They cannot rescue a first session that never reached the point of the product. Fix the path first, then write the emails.

## Rules

- **Look, don't guess.** Work from what a new user sees, step by step. A founder's description of their own signup always skips steps.
- **One moment of value.** Everything before the first time the product does its job for the user is cost. Count it.
- **Change requests in plain words.** The founder is not technical. Each fix is written so they can paste it into Lovable, Bolt, v0 or Replit, or forward it to a developer.
- **No benchmarks from memory.** Do not quote typical conversion or drop-off rates. Use the founder's own counts.
- **Small numbers are stories.** With twenty signups, a percentage means little. Find out what each person did.

## Inputs

`company/product.md` (how someone starts, Key action, Signup or payment link, what is live), `company/customers.md` (hesitations), `company/pricing.md` (trial, plans), `progress.md`. The product itself, by one of the routes in step 2.

## Step 1: Name the key action

Ask one question, with a recommendation from `company/product.md`: "What is the first thing a new user does that makes them think 'this works'?" It must be something the user does and can be seen in the product, such as sending a first invoice or finishing a first workout. "Signs up" and "looks around" do not count. Save it to `company/product.md` under "Key action" with the founder's yes. `keep100:product-emails` uses the same answer.

## Step 2: Walk the path

Get the real path by the best route available:

1. A browser tool is connected and the product is public. Sign up as a new user and record every screen.
2. The founder shares screenshots or a screen recording of signing up in a private window with a new email.
3. The founder describes each screen while clicking through. Ask "then what?" until the key action is reached.

List every step from the button on the landing page to the key action: each screen, each field, each email to confirm, each permission, each choice.

## Step 3: Sort every step

| Step | What the user must do | Verdict | Why |
|---|---|---|---|

Verdicts:

- **Keep.** The product cannot do its job without it right now.
- **Defer.** Needed, but after the key action. Profile details, team invites, preferences and billing details on a free trial usually belong here.
- **Prefill.** Needed now, but the product could supply a default, an example or a guess.
- **Cut.** Nobody needs it.

Then answer four questions, one line each:

1. How many steps and fields stand between the click and the key action?
2. Where is the first screen with nothing on it? An empty screen with no example and no next step is where people leave.
3. Does the user see the product work before being asked for anything hard, such as a card, a long form or an import?
4. Does what the landing page promised appear in the first session, in the same words?

## Step 4: The three fixes

Pick the three changes that remove the most cost before the key action. For each, write:

```
Fix {n}: {plain name}
Why: {what the user faces now, in one sentence}
Change request to paste:
"{Exactly what to change, screen by screen, in words an app builder or developer can act on. One change per request.}"
How we'll know: {what the founder should see or count afterwards}
```

Typical high-value fixes: start with a filled example instead of an empty screen, move questions to after the key action, let the user begin with one field, put one clear next step on every screen, and show the result of the key action immediately.

On asking for a card before the trial: it trades fewer signups for more serious ones, and the right answer depends on how much each trial costs the founder to support. State that trade and recommend one, with the reason. Record the choice in `company/pricing.md` under "Free trial or free plan".

Save the table and the fixes to `marketing/<date>-activation.md`. Tick "Signup path checked" in `progress.md`, add a Work log line and run `keep100:dashboard`.

## Step 5: Onboard the first twenty by hand

Before any of this is automated, the founder should personally get the first twenty users to the key action. Draft:

- a welcome note from the founder, sent within a day of each signup, offering a 15-minute setup call or to set it up for them
- a short script for that call: ask what they hoped it would do, watch them try, help only when they are stuck, note where they hesitated
- a line to add to the note for anyone who has not reached the key action after three days

Every call is a customer conversation. Hand the notes to `keep100:customer-conversations`.

## Step 6: Count by hand

No analytics tool is required. Once a week the founder opens their user list and counts three numbers: new signups, how many reached the key action, how many paid. Record them in the Weekly numbers table in `progress.md`. Tick "First signup" on the B2C track when the first one arrives. For each person who signed up and did not reach the key action, write down the last thing they did, if the product shows it. Three people stopping at the same step is the next fix.

Once there are paying customers and steady signups, suggest connecting an analytics tool and note that it becomes part of month two.

## Hand off

Propose `keep100:product-emails` next, now that the emails have a working path to point at. If the walk showed that the landing page promises something the first session does not deliver, say so and propose fixing whichever one is wrong.
