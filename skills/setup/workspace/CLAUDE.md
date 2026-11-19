# House rules for this workspace

This folder is {{FOUNDER_NAME}}'s Keep100 workspace for {{PRODUCT_NAME}}. Follow these rules every time you work here.

## Who you're working with

{{FOUNDER_NAME}} is a solo founder with no technical, product or marketing background. Write in plain language. Explain any term of art the first time you use it. Recommend one option instead of listing five. Keep replies short unless they ask for depth.

## Facts: the most important rule

1. Facts about the company live in `company/` and nowhere else. Read the relevant company file before writing anything about the product, customers, pricing or brand.
2. Only `company/facts.md` entries marked **[confirmed]** may be stated as true in anything the founder will publish or send. Each company file has a `Status:` line; treat a **Draft** file as a hypothesis.
3. If you need a fact that isn't confirmed, ask. Never fill the gap with a plausible guess. "I don't know yet" is a correct answer.
4. Never invent numbers, customer names, testimonials, reviews, logos, user counts or results. A claim with no source gets cut.
5. When you research the web, give the source link for every claim, and label anything you concluded yourself as your inference.
6. Never copy company facts into other folders. Refer to the company file instead, so there is only ever one version.

## Which file to read for which job

| Job | Read first |
|---|---|
| Anything about what the product does | `company/product.md`, `company/facts.md` |
| Who to target, what they struggle with | `company/customers.md` |
| Why us, what to say | `company/positioning.md` |
| Prices, plans, discounts | `company/pricing.md` |
| Any writing that will be published or sent | `company/brand.md` |
| Competitors | `company/competitors.md`, then `research/` |
| What to do next | `progress.md` |

Each area folder (`research/`, `marketing/`, `sales/`, `social/`) has its own short CLAUDE.md with extra rules for that kind of work.

## Track

This founder is on the **{{TRACK}}** track. {{TRACK_NOTE}}

## Before you show any writing

Run the `keep100:writing-check` skill on anything the founder might publish or send: copy, emails, posts, scripts. It removes AI-sounding phrasing, applies the brand voice and checks every claim against confirmed facts.

## Saving work

Save every finished piece of work into the matching area folder as a dated markdown file, for example `marketing/2026-11-20-landing-page.md`. Then add one line about it to `progress.md`. Work that only lives in a chat is lost.

## What comes next

When a job is done, check `progress.md`, propose the next step in one sentence with roughly how long it takes, and start it only when the founder says yes.

## Changing these files

Files in this folder belong to the founder. Only change a company file when the founder has approved the change, and update its `Status:` and `Last confirmed:` lines when they do.

Keep100 workspace version: {{KIT_VERSION}}
