---
name: launch
description: Plans and runs a small, honest launch for a Keep100 founder, aimed at first customers instead of a big announcement. Checks the product is ready to be bought by a stranger, picks three places where the ideal customer already is (communities, directories, other people's audiences, app stores), prepares one listing kit to reuse everywhere, schedules the posts, and records which place brought signups and customers. Use once the landing page and offer exist, or when the founder asks how to launch, announce, get noticed, get first users, post on Product Hunt, Hacker News, Reddit or directories, get listed, find newsletters or creators, or says "I launched and nothing happened".
---

# Launch

Adapted from the launch and directory-submissions skills in coreyhaines31/marketingskills (MIT).

For a founder with no audience, a launch is a week of showing up where customers already are, with something worth their attention, and answering everyone who responds. It is repeatable. Each new feature or milestone can use the same kit again.

## Rules

- **Say who you are.** Post as the founder, and say so. No fake accounts, no asking friends to pose as users, no traded votes, no reviews from people who have not used the product.
- **Each place has rules. Read them first.** Open the community's or directory's current rules before drafting. They change, and breaking them gets the founder banned from the one place their customers are.
- **Give before you ask.** In a community, the post has to be useful to someone who never clicks the link.
- **Only confirmed facts**, and only the offer recorded in `company/pricing.md`.
- **Three places done well beat thirty done once.** A solo founder can answer comments in three places.
- **Disclose paid relationships.** If a creator or newsletter is paid or given something of value, the post says so.

## Inputs

`company/product.md` (signup or payment URL, what is live), `company/positioning.md`, `company/customers.md` (where they spend time), `company/pricing.md` (founding offer), `company/brand.md`, the latest landing page in `marketing/`, `learnings.md`.

## Step 1: Ready check

Launching sends strangers to the product once. Check before spending that attention.

| Check | How |
|---|---|
| A stranger can sign up and pay with no help from the founder | Ask the founder to do it in a private browser window, start to finish, and say where they got stuck |
| The landing page is live and scores on the rubric | The latest `marketing/*-landing-page.md` has a passing checklist |
| The first session reaches the key action | `keep100:activation` has been run, or the founder has watched one real person try |
| Links can be told apart | Each place gets its own tagged link, so signups can be traced |
| The founder is free to answer for two days | Replies in the first hours matter more than the post |

If the first row fails, stop and fix it. Everything else can be imperfect.

If the product is not live, launch the waitlist or the pre-sale from `keep100:offer` instead, and say plainly what exists today.

## Step 2: Pick three places

Start from "Where they spend time" in `company/customers.md`. Recommend one from each row that fits the track, and name the specific place.

| Kind | B2B | B2C | What it is good for |
|---|---|---|---|
| A community the customer is already in | A role or industry forum, subreddit, Slack or LinkedIn group | A hobby or interest subreddit, Facebook group, Discord | First users and honest feedback |
| A launch site or directory | Product Hunt, Indie Hackers, Hacker News "Show HN" for technical buyers, review sites such as G2 or Capterra, an "alternative to" directory | Product Hunt, app stores for mobile apps, niche directories for the interest | A burst of visits and a lasting listing |
| Someone else's audience | A small newsletter or podcast the champion reads | A creator the customer follows | Trust the founder has not earned yet |

Check each candidate with a search: is it active this month, do posts like this one get answered, and what do its rules say about self-promotion. Drop any that fail. Save the three, with links to their rules, in `marketing/launch-plan.md`.

For someone else's audience, pick small and specific over large and general. Draft a pitch under 80 words that offers something for their readers: early access, a founding price, or a useful finding from the founder's research.

## Step 3: Build the listing kit once

Fill `references/listing-kit.md` from the company files and save it as `marketing/listing-kit.md`. Every post and listing is cut from it, which keeps the product described the same way everywhere. Run `keep100:writing-check` on the kit.

## Step 4: Write each post for its place

One draft per place, in that place's style. Read `references/post-shapes.md`.

- A community post leads with the problem and what the founder learned. The product comes late and once.
- A launch-site post leads with what it is and who it is for, in the words of the landing page hero.
- A pitch to a newsletter or creator leads with what their audience gets.

Each uses its own tagged link.

## Step 5: Run it

Spread the three across a week instead of one day, so the founder can answer each properly.

For each day, give the founder: the post, the time to publish, and a reminder to check back three times that day. Draft replies to comments as they come. Every person who signs up gets a short personal note from the founder within a day, asking what they were hoping it would do. Those answers go to `keep100:customer-conversations`.

## Step 6: Record what happened

A week after each post, ask the founder for the numbers they can see: visits from that link, signups, paying customers, and the two most useful comments. Save one row per place in `marketing/launch-results.csv` (`date, place, link, visits, signups, paid, notes`) and one line in `learnings.md` under Posts and launches on what to repeat.

Tick "Launch in three places" in `progress.md` once all three have run, and run `keep100:dashboard`.

Then recommend: repeat the place that worked with a new angle in a month, drop the one that did not, and add the listing kit to five more directories from the same family as the one that worked.

## If nothing happened

Check in this order, and say which it is:

1. Few visits. The post did not earn attention, or the place was wrong. Look at what does get answered there.
2. Visits and no signups. The page is the problem. Score it with `keep100:landing-page`.
3. Signups and no use. The first session is the problem. Run `keep100:activation`.
4. Use and no payment. The offer or the price is the problem. Run `keep100:offer`.
