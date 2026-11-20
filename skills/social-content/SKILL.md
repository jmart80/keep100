---
name: social-content
description: Social posts and short-form video scripts for Keep100 founders, built from their customers' own words. Picks the platforms, sets content pillars, writes posts and 30 to 60 second scripts, plans daily posting, and records what worked. Main customer-getting skill on the B2C track; optional LinkedIn posts on B2B. Use when the founder wants social media posts, TikTok, Reels, Shorts, LinkedIn or X content, a content calendar, ideas for what to post, or help replying to comments.
---

# Social content

## Inputs

`company/customers.md` (quotes, where they spend time), `company/positioning.md`, `company/brand.md`, `company/product.md` (the link posts point to), the latest research, `social/posted.csv` and `learnings.md` (what has worked).

## Branch A: Set up

1. **Platforms:** pick 1, at most 2, where the ideal customer actually spends time, from `customers.md` and research. Recommend one. A solo founder spread across five platforms posts badly on all of them.
2. **Three content pillars**, each from a real customer struggle with a quote behind it. Examples of pillar types: the problem and its hidden cost, how-to tips that help even without the product, behind the scenes of building it.
3. **Communities:** 3 to 5 places customers already talk (subreddits, groups, forums). Open each one's rules and note what they say about self-promotion. The rule there: help first, mention the product only when it truly answers the question.
4. **Where posts lead:** the landing page or signup link from `product.md`, with a tag per platform (`?ref=tiktok`) so signups can be traced. One link in the profile. Without somewhere to go, a post that works wins nothing.
5. Save the plan to `social/plan.md`. Tick "Platforms and pillars chosen" in `progress.md`.

## Branch B: Write posts and scripts

Read `learnings.md` first and lean toward what worked.

**Every post:**
- One idea. The hook is the first line and uses the customer's words or a specific, surprising detail.
- Built from a quote, a research finding or a real moment from building the product. Never generic tips anyone could write.
- A light call to action only where it fits (link in bio, "comment X and I'll send it").
- A customer's words appear in quotation marks only when tagged `[verbatim]`, and never with their name unless `facts.md` records permission.

**Short-form video script (30 to 60 seconds):**
```
HOOK (0-3s): {one line on screen and spoken, stops the scroll}
SETUP (3-10s): {the situation the viewer recognizes}
VALUE (10-45s): {the tip, the story, or the before and after}
CLOSE (45-60s): {one takeaway, and a soft call to action}
On-screen text: {what appears, beat by beat}
Shot notes: {talking head, screen recording, b-roll}
```
Write how people talk: short sentences, no reading-from-a-page phrasing.

**One idea, several posts.** When an idea is strong, write it once and reshape it: a short video, a text post, and a reply-sized version for a community thread. It saves the founder's time and shows which form the idea works in.

If the Higgsfield connector is connected and the founder wants AI-generated visuals or video, say what it costs in credits before generating anything.

Run `keep100:writing-check`, save to `social/<date>-posts.md`. Tick "First week of posts written" the first time.

## Branch C: Daily

Each day: one post or video ready to publish, replies drafted for comments, and 3 helpful replies in the communities from the plan. When the founder has published, add a row to `social/posted.csv` with the link. Tick "First post published" the first time.

Every Friday, ask the founder for what they can see on each post from the week (saves, shares, comments, link clicks, signups) and fill in the rows. Write two or three lines to `learnings.md`: which pillar, hook and format did best, and what to drop. Add the week to Weekly numbers in `progress.md`.

## Platform notes

Platforms change their rules and what they reward. Treat these as starting points and trust the founder's own results in `learnings.md` over them.

- **TikTok, Reels, Shorts:** hook in the first second, captions on, vertical, native feel over polish.
- **LinkedIn (B2B):** first two lines carry the post. Plain text, short paragraphs, a specific story beats advice.
- **X:** one sharp idea per post. Threads only for real step-by-steps.
- **Reddit:** never post ads. Answer questions well. The profile and occasional relevant mentions do the work.
