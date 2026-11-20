---
name: competitor-research
description: Competitor and market research for a Keep100 founder, run inside Claude with web search. Finds who else customers could choose (including doing nothing), where they are weak, how they price and position, where customers gather, and the exact words customers use. Use early in the plan, or when the founder asks about competitors, alternatives, the market, how to stand out, or what customers complain about.
---

# Competitor research

Adapted from the deep-competitive-analysis skill by Keep100's author. Research runs here, inside Claude, so the founder never has to copy prompts between tools.

## Before you start

- Read `company/product.md`, `company/customers.md` and `company/competitors.md`.
- Confirm three things with the founder (recommend answers from the files): the niche in one line, the ideal customer, and any competitors they already know. "None" is fine.
- Use the Exa connector if it's connected. Otherwise use web search. If neither is available, say so and offer the Perplexity route at the end of this file.

## Research, in this order

Tag every claim **[source]** with its link and the date you checked, or **[inference]** if it's your conclusion. Never present inference as fact. End each part with confidence: high, medium or low.

1. **Who they could choose instead.** Up to 5 direct competitors, plus the substitutes the customer really uses: spreadsheets, a freelancer, a generic tool bent to fit, or doing nothing. Doing nothing is often the real competitor. Five done properly beats eight skimmed.
2. **How each one sells.** Homepage headline (quoted), who they say it's for, the category they claim, price points and free tier, and how you get started (trial, demo, waitlist).
3. **What customers say.** The most important part. Mine 1 to 3 star reviews (G2, Capterra, app stores), Reddit, forums and communities. Aim for 20 quotes, and follow the quote rule below. Group them: pains, what they wish existed, what they praise (praised features are table stakes), what makes them hesitate.
4. **Where customers gather.** Subreddits, groups, newsletters, creators, communities, events, and which of these competitors ignore. This feeds outreach (B2B) and social (B2C) directly.
5. **The gaps.** Cross the top pains against what competitors cover. Name 2 or 3 openings where pain is high and coverage is weak, and recommend one, with the reason. Name what the founder should refuse to be.

Keep it decision-grade: every sentence should change a decision. No generic SaaS advice.

## The quote rule

Everything downstream (positioning, the landing page, posts) is built from these quotes, so a quote that isn't real poisons all of it.

- Tag a quote `[verbatim]` only when you saw those exact words in the text of the page. A search result summary, a fetched page that came back summarized, or your recollection is `[paraphrase]`.
- Review sites and forums often block automated reading. When you can't get the page text, say so. Ask the founder to open the page and paste the reviews, or use a browser tool if one is connected. Don't fill the gap from memory.
- Tag whose customer spoke. Almost everything here is `[competitor's customer]`.
- Twenty honest paraphrases with links are worth more than twenty invented "quotes". Report how many of each you have.

## Save and hand off

1. Save the full report to `research/<date>-competitors.md`.
2. Propose (don't apply without a yes):
   - `company/competitors.md` filled in: a dated section per alternative, the top five pains with a quote and link each, the recommended opening, what to refuse to be, the pricing pattern in the niche, and open questions for real customers;
   - the best quotes, tagged and linked, added to `company/customers.md`;
   - any new places customers gather, added to `company/customers.md`.
3. Tick "Competitor research" in `progress.md`, add a Work log line, and run `keep100:dashboard`.
4. Propose the next step: inviting people to talk with `keep100:customer-conversations`, then positioning.

## Going deeper with Perplexity (optional)

If the founder has Perplexity and wants more depth, write one ready-to-paste prompt covering the five parts above for their niche, ask them to run it in Perplexity Deep Research, and audit what they bring back against the same five parts and the quote rule before merging it into the report.
