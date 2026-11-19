---
name: positioning
description: Positioning for a Keep100 founder - who the product is for, what it beats, why it wins, and what to say - built on named practitioner frameworks (Dunford, Fletch, Moesta, Wiebe, Voje, Laja). Writes company/positioning.md. Use on day 3 of the plan, or whenever the founder asks who their product is for, how to stand out, what their message should be, how to describe the product, or wants their ideal customer narrowed.
---

# Positioning

Adapted from the saas-positioning skill by Keep100's author. The detailed frameworks live in `references/`; read each one at the phase that names it.

## Rules

- **Verbatim discipline.** Customer language is stored word for word, never paraphrased (Wiebe). Copy is later built from these quotes, not invented.
- **Sequence discipline.** Each phase feeds the next. Don't skip ahead.
- **Provenance.** Every line in `positioning.md` traces to a customer quote, a research source or a confirmed fact. If it can't, cut it or mark it as a guess to test.
- **Narrow wins.** At every choice, prefer the narrower segment and the more concrete words. "Almost comically narrow" is the right calibration (Dunford).
- **Homepage leads with clarity**, not a big-picture story (Laja, Fletch).

## Inputs

Read `company/product.md`, `company/customers.md`, `company/competitors.md`, `company/facts.md`, and the HANDOFF block in the latest `research/*-competitors.md`. If competitor research hasn't been done, recommend doing it first (30 minutes), but continue if the founder prefers.

## Pick the branch

- **No paying customers yet** (most Keep100 founders): run phases 1 to 4 using competitor reviews and communities as the research source. Mark `positioning.md` as provisional and list what to learn from the first real customers. Don't over-tighten; the data doesn't exist yet (Dunford).
- **Some paying customers:** do the same, but ask for 3 to 5 short customer conversations first. Offer to write the questions (see phase 1 reference). Real customer words outrank review mining.

## Phase 1: Customer language

Read `references/phase-1-research.md`. Gather the quotes from `customers.md`, research and any customer conversations. Tag each: situation, goal, pain, hesitation, metaphor. Rank the struggles by how often and how strongly they appear.

**Done when:** at least 20 tagged quotes from at least 2 kinds of source, each traceable.

## Phase 2: The position

Read `references/phase-2-positioning.md`. Work Dunford's five components in order, with the founder, one at a time, recommending an answer each time:
1. Alternatives (include doing nothing)
2. What only we have
3. Why that matters to the customer (with proof)
4. Who cares most
5. Category: what the customer would call us

Then make the Fletch anchor decision: category-based or use-case-based, whichever is easier for this buyer to understand.

## Phase 3: Who to win first

Read `references/phase-3-icp.md`. List 3 candidate segments and score each on burning pain, willingness to pay, reachability, and whether they'll give a testimonial. Pick the beachhead. For B2B, name the champion (the person who'd start the purchase). For B2C, describe the person and the moment they start looking.

## Phase 4: The message

Read `references/phase-4-value-props.md` and `references/phase-5-messaging.md`.
1. Three value props, each one pain → one capability → one outcome, in customer words.
2. 10 headline candidates from customer struggle language. Cut any that use internal product words.
3. A one-line positioning statement: {Product} is a {category} for {who} that {outcome} by {what only we have}.

Run `keep100:writing-check`.

## Write it down

Fill `company/positioning.md` (structure already there). Show the founder a short summary, take corrections, and set `Status: Confirmed` (or `Provisional` for the no-customers branch, with the list of what to learn). Add the best quotes to `company/customers.md` with a yes. Log it in `progress.md` and propose pricing next.

`references/packet-template.md` is a fuller format for founders who want the long version; `references/sources.md` lists where each framework comes from.
