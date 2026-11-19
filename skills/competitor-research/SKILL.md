---
name: competitor-research
description: Competitor and market research for a Keep100 founder, run inside Claude with web search. Finds who else customers could choose (including doing nothing), where they are weak, how they price and position, where customers gather, and the exact words customers use. Use on day 2 of the plan, or when the founder asks about competitors, alternatives, the market, how to stand out, or what customers complain about.
---

# Competitor research

Adapted from the deep-competitive-analysis skill by Keep100's author. Research runs here, inside Claude, so the founder never has to copy prompts between tools.

## Before you start

- Read `company/product.md`, `company/customers.md` and `company/competitors.md`.
- Confirm three things with the founder (recommend answers from the files): the niche in one line, the ideal customer, and any competitors they already know. "None" is fine.
- Use the Exa connector if it's connected; otherwise use web search. If neither is available, say so and offer the Perplexity route at the end of this file.

## Research, in this order

Tag every claim **[source]** with its link, or **[inference]** if it's your conclusion. Never present inference as fact. End each part with confidence: high, medium or low.

1. **Who they could choose instead.** 5 to 8 direct competitors, plus the substitutes the customer really uses: spreadsheets, a freelancer, a generic tool bent to fit, or doing nothing. Doing nothing is often the real competitor.
2. **How each one sells.** Homepage headline (quoted), who they say it's for, the category they claim, price points and free tier, and how you get started (trial, demo, waitlist).
3. **What customers say.** The most important part. Mine 1 to 3 star reviews (G2, Capterra, app stores), Reddit, forums and communities. Collect at least 20 quotes **word for word** with links. Group them: pains, what they wish existed, what they praise (praised features are table stakes), what makes them hesitate.
4. **Where customers gather.** Subreddits, groups, newsletters, creators, communities, events, and which of these competitors ignore. This feeds outreach (B2B) and social (B2C) directly.
5. **The gaps.** Cross the top pains against what competitors cover. Name 2 or 3 openings where pain is high and coverage is weak, and recommend one, with the reason. Name what the founder should refuse to be.

Keep it decision-grade: every sentence should change a decision. No generic SaaS advice.

## Save and hand off

1. Save the full report to `research/<date>-competitors.md`.
2. Propose (don't apply without a yes):
   - a section per competitor in `company/competitors.md`;
   - the best customer quotes, with links, added to `company/customers.md`;
   - any new places customers gather, added to `company/customers.md`.
3. Close with a short handoff block at the end of the report for the positioning skill:

```
HANDOFF
Alternatives: {including doing nothing}
Top 5 pains: {each with one verbatim quote and link}
Recommended opening: {one paragraph}
Refuse to be: {one line}
Pricing pattern in the niche: {one or two lines}
Where customers gather: {list}
Open questions to ask real customers: {list}
```

4. Propose positioning as the next step.

## Going deeper with Perplexity (optional)

If the founder has Perplexity and wants more depth, write one ready-to-paste prompt covering the five parts above for their niche, ask them to run it in Perplexity Deep Research, and audit what they bring back against the same five parts before merging it into the report.
