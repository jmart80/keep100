---
name: positioning
description: Positioning for a Keep100 founder - who the product is for, what it beats, why it wins, who to win first and what to say - built on named practitioner frameworks (Dunford, Fletch, Moesta, Wiebe, Bourgoin, Voje, Kramer, Lerner, Laja). Writes company/positioning.md, which cold email, the prospect list and the landing page all read. Use at the positioning step of the plan, or whenever the founder asks who their product is for, how to stand out, what their message should be, how to describe the product, or wants their ideal customer narrowed.
---

# Positioning

Adapted from the saas-positioning skill by Keep100's author, rewritten for a solo founder with few or no customers. The frameworks live in `references/`. Read each one at the phase that names it. `references/sources.md` says where each comes from.

## Rules

- **Real words only.** Customer language is stored word for word and tagged `[verbatim]` or `[paraphrase]` (Wiebe). Copy is later built from these quotes, not invented.
- **In order.** Each phase feeds the next. Don't skip ahead.
- **Traceable.** Every line in `positioning.md` traces to a quote, a research source or a confirmed fact. If it can't, cut it or mark it as a guess to test.
- **Narrow wins.** At every choice, prefer the narrower segment and the more concrete words. Almost comically narrow is the right calibration (Dunford).
- **Clarity first.** A homepage says what the product is before it says why the world needs it (Laja, Fletch).

## Inputs

Read `company/product.md`, `company/customers.md`, `company/competitors.md`, `company/facts.md` and everything in `conversations/`. If competitor research hasn't been done, recommend doing it first (30 minutes), but continue if the founder prefers.

## Pick the branch

- **No paying customers yet** (most Keep100 founders): run all four phases using conversations, competitor reviews and communities. Set `Status: Provisional` and fill "What to learn from the first customers". Keep it loose where the evidence is thin. The data to tighten it doesn't exist yet (Dunford).
- **Some paying customers:** the same, built first on what those customers said. Set `Status: Confirmed` at the end.

On both branches, real conversations outrank mined reviews. If fewer than five people have been invited to talk, offer `keep100:customer-conversations` now and carry on in parallel.

## Phase 1: Customer language

Read `references/phase-1-customer-language.md`. Gather the quotes from `customers.md`, `conversations/` and research. Tag each: situation, goal, pain, hesitation, trigger, comparison. Rank the struggles by how many people raised them and how strongly.

**Done when:** at least 20 tagged quotes from at least 2 kinds of source, each traceable. With fewer, say how many you have, go on, and mark the gap under what to learn.

## Phase 2: The position

Read `references/phase-2-position.md`. Work Dunford's five components in order, with the founder, one at a time, recommending an answer each time:
1. Alternatives (include doing nothing)
2. What only we have
3. Why that matters to the customer (with proof, or marked unproven)
4. Who cares most
5. Category: what the customer would call us

Then make the Fletch anchor decision (category-based or use-case-based) and record category awareness: known, emerging or unknown.

## Phase 3: Who to win first

Read `references/phase-3-who-first.md`. List 3 candidate segments and score each on burning pain, willingness to pay, reachability, and whether they'd give a testimonial. Pick the beachhead. For B2B, name the champion (the person who'd start the purchase). For B2C, describe the person and the moment they start looking. List the trigger events.

## Phase 4: The message

Read `references/phase-4-message.md`.
1. The job to be done and the top objection, each in the customer's words.
2. Three value props, each one pain, one capability, one outcome.
3. Up to 10 headline candidates from customer struggle language, each with its source quote. Cut any that use internal product words.
4. A one-line positioning statement: {Product} is a {category} for {who} that {outcome} by {what only we have}.

Run `keep100:writing-check`.

## Write it down

Fill every heading in `company/positioning.md`. Other skills read these fields by name, so leave none blank: write "unknown, to learn" where the evidence isn't there. Show the founder the whole file, take corrections, and set the status. Add the best quotes to `company/customers.md` with a yes. Tick "Positioning" in `progress.md`, add a Work log line, run `keep100:dashboard`, and propose pricing next.
