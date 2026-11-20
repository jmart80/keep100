# House rules for this workspace

This folder is {{FOUNDER_NAME}}'s Keep100 workspace for {{PRODUCT_NAME}}. Follow these rules every time you work here.

## Who you're working with

{{FOUNDER_NAME}} is a solo founder with no technical, product or marketing background. Write in plain language. Explain any term of art the first time you use it. Recommend one option instead of listing five. Keep replies short unless they ask for depth.

## Facts: the most important rule

1. Facts about the company live in `company/` and nowhere else. Read the relevant company file before writing anything about the product, customers, pricing or brand.
2. A claim may go into anything the founder will publish or send only if it sits in a company file whose `Status:` is **Confirmed**, or is marked **[confirmed]** in `company/facts.md`. Treat a **Draft** or **Provisional** file as a hypothesis.
3. Each fact has one home. Prices live in `pricing.md`, features in `product.md`. `facts.md` holds only proof with no other home: results, credentials, customer names, testimonials.
4. If you need a fact that isn't confirmed, ask. Never fill the gap with a plausible guess. "I don't know yet" is a correct answer.
5. Never invent numbers, customer names, testimonials, reviews, ratings, logos, user counts or results. A claim with no source gets cut.
6. When you research the web, give the source link for every claim, and label anything you concluded yourself as your inference.
7. The company files override anything you remember from earlier chats or from memory. Never save prices, features or customer details to memory.

## Which file to read for which job

| Job | Read first |
|---|---|
| What the product does, how someone starts, where they pay | `company/product.md` |
| Who to target, their words, where they gather | `company/customers.md` |
| Why us, who to win first, what to say | `company/positioning.md` |
| Prices, plans, discounts, the founding offer | `company/pricing.md` |
| Any writing that will be published or sent | `company/brand.md` |
| Proof: results, credentials, named customers | `company/facts.md` |
| Competitors | `company/competitors.md`, then `research/` |
| What to do next | `progress.md` |
| Who was contacted and what they said | `sales/pipeline.csv` |
| What has worked so far | `learnings.md` |
| What was decided and why | `decisions.md` |

Before working in an area folder (`research/`, `marketing/`, `sales/`, `social/`, `conversations/`), read the short `CLAUDE.md` inside it.

## Track

This founder is on the **{{TRACK}}** track. {{TRACK_NOTE}}

## Before you show any writing

Run the `keep100:writing-check` skill on anything the founder might publish or send: copy, emails, posts, scripts. It checks every claim against the company files, applies the brand voice and removes AI-sounding phrasing.

## Saving work

Save every finished piece of work into the matching area folder as a dated markdown file, for example `marketing/2026-11-20-landing-page.md`. Then tick the step in `progress.md` if it finished one, add one line to its Work log, and refresh the dashboard with `keep100:dashboard`. Work that only lives in a chat is lost.

## What comes next

When a job is done, check `progress.md`, propose the next step in one sentence with roughly how long it takes, and start it only when the founder says yes.

## Changing these files

Files in this folder belong to the founder. Only change a company file when the founder has approved the change, and update its `Status:` and `Last confirmed:` lines when they do. Nothing is sent, posted or published without the founder's yes.

Keep100 workspace version: {{KIT_VERSION}}
