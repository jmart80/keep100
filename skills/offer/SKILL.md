---
name: offer
description: Designs the founding-customer offer for a Keep100 founder, the specific reason the first ten or twenty people should buy now from a company nobody has heard of. Builds it from four parts (what they get, how the risk is removed, why now, and the price), checks that every part is true and that the founder can deliver it, then records it in company/pricing.md so every page and email uses the same words. Also covers pre-selling before the product is live, paid pilots and deposits. Use right after pricing, or when the founder asks about a launch offer, founding members, early-bird pricing, a guarantee, a pilot, pre-orders, discounts, urgency, or says people are interested but not buying.
---

# Offer

Adapted from the offers skill in coreyhaines31/marketingskills (MIT), narrowed to a new software product with no customers. The value equation is Alex Hormozi's, from *$100M Offers*.

The price says what it costs. The offer says why a stranger should take the risk today. A new product has no reviews and no track record, so the offer has to carry the trust the brand cannot.

## Rules

- **Every part is true.** A deadline that does not end, a limit that is not a limit and a guarantee the founder would not honor are lies, and customers find out. Fake scarcity is the fastest way to lose the people most likely to recommend the product.
- **Add help before cutting price.** The first lever is making success more likely and faster. A low price is hard to raise later and says the product is cheap. Use a price reduction only as a named founding price with an end.
- **The founder must be able to deliver it.** Count the hours.
- **Recorded or it does not exist.** Only an offer written in `company/pricing.md` may appear in any copy, email or reply.

## Inputs

`company/pricing.md` (plans and prices must be Confirmed; if not, run `keep100:pricing` first), `company/positioning.md`, `company/customers.md` (hesitations, what they pay today), `company/product.md` (what is live), hours a day from `progress.md`.

## Steps

One question at a time, with a recommended answer each time.

### 1. Find what is stopping people

Read the hesitations in `company/customers.md` and the lost reasons in `learnings.md`. Sort the main one into a row:

| The hesitation | The lever |
|---|---|
| "I don't believe it will work for me" | Make success more likely: set it up with them, show it on their own data, guarantee it |
| "It will take too long to see anything" | Shorten the wait: a first result in the first session, done by the founder if needed |
| "It's too much effort to switch" | Take the work away: migrate their data, build their first project for them |
| "What if you disappear, or it doesn't fit" | Remove the risk: refund window, cancel any time, export their data |
| "I'm not sure it's worth the money" | Sharpen the outcome: restate what the alternative costs them today, in their numbers |

If the files hold no hesitations yet, say so, default to the first row, and note that the offer should be revisited after five conversations.

### 2. Build the four parts

**What they get.** The product, plus one or two things only an early customer can have. Good ones cost the founder time and nothing else: a setup call, their data moved over, a direct line to the founder, a say in what gets built next. Each must be something the founder will do every time.

**How the risk is removed.** Recommend one, by what fits the product:

| Type | Use when | Wording must include |
|---|---|---|
| Refund window | Value shows up within days | The number of days and how to ask |
| Cancel any time | Monthly plan, low effort to start | That there is no minimum term |
| Paid pilot, credited | B2B, needs proof on their own situation | The fee, the length, what counts as success, and that the fee counts toward the plan |
| Result or refund | The outcome is specific and inside the founder's control | The exact result, the period, and what the customer must do |

Never guarantee an outcome that depends on things the founder does not control.

**Why now.** Real limits only. Two honest kinds exist for a solo founder:
- Capacity. "The first 10 customers get setup done with me." It is true because the founder's hours are finite. Do the arithmetic: hours per customer times the number of places must fit inside the founder's week.
- A date or a count on the founding price. "Founding price for the first 20 customers, kept for as long as they stay." It ends when the count is reached, and the kit removes it from copy when it does.

**The price.** The plan and price from `company/pricing.md`. If a founding price is used, state the normal price beside it and what happens later.

### 3. Check it

Every line is a yes or the offer goes back to step 2.

- Would the founder deliver every promised thing to customer number ten in a bad week?
- Is every limit real, with a count or a date that will be enforced?
- Does the guarantee state its conditions in plain words?
- Can a stranger repeat the offer in one sentence after reading it once?
- Does it answer the hesitation from step 1?
- Is anything promised that `company/product.md` lists under "what it does not do"?

### 4. Write it down

Fill `## Founding offer` in `company/pricing.md` with: who it is for, what they get, the guarantee and its terms, the limit and how it ends, places taken out of the total, whether it is Open or Closed, and the date it was confirmed. Confirm with the founder. Then produce three versions for other skills to use, and run `keep100:writing-check` on each:

- one sentence, for cold emails and replies
- a short block for the landing page, near the final button
- two lines for the trial-ending email

Tick "Founding offer" in `progress.md`, add a Work log line and run `keep100:dashboard`. Propose the landing page next, or updating it if one exists.

### 5. Keep it honest

When a customer takes a place, `keep100:sales-replies` updates the count. When the count or date is reached, the offer is marked closed in `company/pricing.md` and `keep100:today` lists every saved page and email that still mentions it.

## Before the product is live

Selling first is the cheapest test there is. Three forms, mildest first:

| Form | The ask | What it proves |
|---|---|---|
| Waitlist with a question | An email address and one answer about their situation | Interest, weakly |
| Refundable deposit | A small payment that holds a founding place | Real intent |
| Paid pilot | A fee for a hands-on version the founder runs partly by hand | That someone will pay for the outcome |

Say exactly what exists today and when the rest is expected. Refund without argument if the date slips. Record deposits in `progress.md`. Rules on taking money for something not yet delivered vary by country, so the founder should check what applies to them before taking a deposit.

## What not to build

- Countdown timers that reset
- "Only 3 left" on something unlimited
- Bonus lists with invented dollar values
- A discount for anyone who asks. If the founder wants to give one, it goes in `company/pricing.md` under "Discounts allowed" first
