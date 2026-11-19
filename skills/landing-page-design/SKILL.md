---
name: landing-page-design
description: Turns a Keep100 founder's approved landing page copy into a designed, working web page, using the UI/UX Pro Max design database to pick a layout, style, colors and fonts that fit their product and customer. Use right after landing page copy is approved, or when the founder wants their landing page designed, built, made to look professional, or wants a design direction, colors or fonts for their site.
---

# Landing page design

Copy first, design second. This skill never writes new copy: it designs and builds the page around the copy the founder already approved with `keep100:landing-page`. The design intelligence comes from the bundled `keep100:ui-ux-pro-max` skill by NextLevelBuilder (MIT); read its SKILL.md before step 2.

## Inputs

- The latest `marketing/*-landing-page.md`. If none exists, or the founder hasn't approved it, run `keep100:landing-page` first.
- `company/brand.md` (colors, fonts, voice), `company/product.md` (product type, platform), `company/customers.md` (who the visitor is).

## Step 1: Brief

Write a one-line design brief from the company files, for example: "B2B SaaS invoicing tool for freelance designers, calm and trustworthy, free trial CTA". Include product type, customer, the voice words from `brand.md`, and the primary CTA. Never put private details (customer names, revenue) into search queries.

## Step 2: Design direction

- **Brand already set:** if `brand.md` is Confirmed and has colors and fonts, keep them. Use UI/UX Pro Max only for the layout pattern, style and UX rules (`--domain landing`, `--domain style`, `--domain ux`).
- **No brand yet:** run the design-system search with the brief:
  ```bash
  python "${CLAUDE_PLUGIN_ROOT}/skills/ui-ux-pro-max/scripts/search.py" "<brief>" --design-system --persist --preview -p "<product name>" --output-dir "<workspace>/marketing"
  ```
  If `python` fails, try `python3`. If `${CLAUDE_PLUGIN_ROOT}` isn't set, find the `ui-ux-pro-max/scripts/search.py` file inside the installed Keep100 plugin. If scripts can't run at all here, read the CSV files in `ui-ux-pro-max/data/` directly (`products.csv`, `landing.csv`, `styles.csv`, `colors.csv`, `typography.csv`) and pick the rows that match the brief.

Show the founder the direction in plain words, not jargon: the page structure, the overall look (one sentence), the colors as swatches or hex codes with what each is for, the two fonts, and what it deliberately avoids. Recommend it, and offer one alternative look if they want a choice. On their yes, propose adding the colors and fonts to `company/brand.md` and confirming it.

## Step 3: Build the page

Build one self-contained `marketing/site/index.html` that opens in any browser: HTML with Tailwind from its CDN (or inline CSS), Google Fonts links for the chosen fonts, no build step.

- **Copy:** use the approved copy word for word, section by section. If the layout needs a line that doesn't exist (a nav label, a button), keep it to a few plain words and flag it.
- **Structure:** the six copy sections in order (hero, problem, solution, value props, FAQ, final CTA), laid out with the pattern from step 2.
- **Proof stays earned:** no fake testimonials, logos, star ratings, user counts or stock-photo "customers". Where a product screenshot belongs, leave a clearly labelled placeholder box and tell the founder exactly which screenshot to put there.
- **B2C mobile apps:** App Store and Google Play buttons as the primary CTA.
- **Quality:** apply UI/UX Pro Max's pre-delivery checklist: SVG icons (never emoji), text contrast at least 4.5:1, visible focus states, mobile-first and checked at 375, 768, 1024 and 1440 px wide, no horizontal scroll, reduced motion respected, buttons at least 44 px tall.

## Step 4: Review with the founder

Show the page (open the file, or a screenshot if you can take one). Ask for reactions on three things only: does it feel like them, is anything hard to read, and does the main button stand out. Make the changes, then save.

## Step 5: Get it live

Explain the options in plain language and recommend one:
- **They already have a website builder** (Webflow, Framer, Wix, Squarespace, Carrd): use the page as the exact blueprint and paste the copy section by section.
- **They used an AI app builder** (Lovable, Bolt, v0, Replit) or have a developer: hand over `marketing/site/index.html` and `marketing/design-system/` and ask for it as the homepage.
- **They have nothing yet:** a free static host such as Netlify Drop takes the file as is.

Log the page in `progress.md` and propose the next step in the plan.
