---
name: pricing
description: Sets a first price and plan structure for a Keep100 founder that they can defend and change later, and makes sure a customer can actually pay. Use at the pricing step of the plan, or when the founder asks what to charge, how to price, whether to have a free plan or trial, how many plans to offer, whether their price is too high or low, or how to take payment.
---

# Pricing

The goal is a **first price that gets paying customers and teaches you something**, not the perfect price. It can change next month.

The recommendations below are starting defaults for a solo founder with no customers. They are judgment, not research findings. Say so when the founder asks why, give the reasoning, and let the founder's own evidence overrule any of them.

## Inputs

`company/positioning.md` (who, and what we beat), `company/competitors.md` (the pricing pattern in the niche), `company/pricing.md` (anything already decided), `company/customers.md` (what they pay for the alternative today), `conversations/` (anything a real person said about cost).

## Steps, one question at a time, recommending an answer each time

One question mark per message. Don't stack a second question behind the first ("and has any tester mentioned price?"). Ask it next time. Say what the files already show in two lines at most, ask the question, and give your recommended answer. When the files don't hold a number, such as a competitor's price, say so, say where the founder can read it in two minutes, and recommend what to do if they can't find it.

1. **What they pay today for the alternative.** A tool, a freelancer, staff hours, or lost money from doing nothing. This anchors value, not your costs.
2. **What the customer is buying.** The outcome, in their words. Price that, not features.
3. **Model.** Recommend the simplest that fits:
   - B2B: flat monthly per company, or per seat only if value grows with people. An annual option at a discount is a common pattern. Check what the niche does in `competitors.md`.
   - B2C: monthly and annual subscription, or one-time purchase if it's used once.
   - Usage-based only if the customer naturally thinks in units (per report, per order).
4. **Free plan or free trial.** Default: a short free trial instead of a free plan, because a free plan brings people who never pay and a solo founder has to support them. A free plan fits when the product spreads by people inviting others. Trial length should cover the time it takes a new user to reach the key action in `product.md`.
5. **Number of plans.** Start with one paid plan, two at most. More plans means more decisions for buyers and more work for you.
6. **The price.** Place it against the alternatives from research. When torn between two numbers, recommend the higher one. A price is easier to lower for one customer than to raise for all of them, and a founding offer can soften it.
7. **A way to pay.** Ask how a customer would pay today. If there is no way, help the founder set up the simplest one their tools allow, such as a payment link from their payment provider. For a mobile app, the app stores take a share of each sale and set rules on how you may charge, so have the founder check the current terms before fixing the price. Ask the founder to make one test purchase and refund it. Record the link and the date it worked.

## Write it down

Fill `company/pricing.md`: plans, prices, trial, how a customer pays, why these prices (one line each, with the research behind them), discounts allowed, and when to revisit. Prices live in `pricing.md` only. Don't copy them into `facts.md` or anywhere else. Confirm with the founder by showing the file, then set `Status: Confirmed`.

Revisit after the first 10 paying customers, or sooner if nobody objects to the price at all, which suggests it's too low.

Tick "Pricing and a way to pay" in `progress.md`, add a Work log line, run `keep100:dashboard`, and propose `keep100:offer` next: the founding offer that gives the first customers a reason to buy now.
