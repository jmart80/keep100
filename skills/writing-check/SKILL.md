---
name: writing-check
description: The check every Keep100 draft passes before the founder sees it. Checks every claim against the company files, applies the brand voice, removes AI-sounding phrasing and runs the mechanical checks (word limits, banned terms, leftover placeholders). Use automatically before showing the founder any copy, email, post, script, page or message draft, without being asked, and whenever the founder asks to fact-check, humanize or tighten a draft.
---

# Writing check

Run this on every draft meant for the outside world. For quick pieces (a social post, a reply) fix quietly and show the fixed version, with a one-line note only if you removed a claim. For anything the business stands on (a landing page, a pricing page, the first cold email of a sequence, a launch post) also show the claims table from step 1.

## 1. Facts

- A claim may stay only if it sits in a company file whose `Status:` is Confirmed, or is marked `[confirmed]` in `company/facts.md`. Read the files that the draft touches: `product.md` for what it does, `pricing.md` for prices and offers, `facts.md` for proof.
- Unconfirmed or missing claim: cut it, or replace it with something confirmed. Tell the founder in one line which claim you cut and why, so they can confirm it if it's true.
- Never allowed unless confirmed: numbers, user counts, customer names, testimonials, ratings, stars, logos, "trusted by", results.
- A quote inside quotation marks must be tagged `[verbatim]` in `customers.md`. A `[paraphrase]` may inform the wording but is never presented as someone's words.
- **Claims table**, for the important pieces:

| Claim in the draft | Backed by |
|---|---|
| "{the claim}" | `{file}`: "{the line that backs it}" |

A row with nothing in the second column is a claim to cut. Where the session has subagents, give the draft and the company files to one that did not write the draft, and ask it to fill the table. A reviewer that didn't write the words is less inclined to defend them.

## 2. Brand

Read `company/brand.md`. Use their words, avoid the words they never use, match their voice and the exact spelling of their name.

## 3. Mechanical checks

Save the draft to its file, then run:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/check.py <file> --format <general|cold-email|landing-page|product-email|social|blog> --brand company/brand.md
```

Add `--template` only for a saved email sequence that keeps `{first_name}`. Fix every ERROR and look at every WARNING. The script checks the banned list in `banned.txt` (minus any "Words we allow" in `brand.md`), dashes used as separators, leftover placeholders, and the word limits for the format. If scripts can't run here, read `banned.txt` and check the same things by hand, counting words properly instead of estimating.

## 4. Patterns a script can't see

- Puffery: "a pivotal moment", "setting the stage". State what happened.
- Trailing "-ing" filler: "..., ensuring smooth delivery". Cut it or make it its own concrete sentence.
- Rule of three by reflex: "fast, simple, and powerful". Keep one, make it specific.
- "Not just X, but Y" and "It's not about X, it's about Y".
- Hedge stacking: "can potentially help". Say what it does.
- Every sentence the same length. Vary it.
- Vague praise: "amazing results". Name the result or cut it.
- A word from the banned list used in its plain meaning (a brewery's "craft beer") is fine. Suggest adding it to "Words we allow".

## 5. Read it as a stranger

Would the reader know what this is about from the first line? If not, rewrite the first line.

## 6. Sound like a person

Removing tells isn't enough. Prefer short concrete sentences, the customer's own words, and one opinion over a balanced list. Contractions are fine.
