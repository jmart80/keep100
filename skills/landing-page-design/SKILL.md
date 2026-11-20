---
name: landing-page-design
description: Turns a Keep100 founder's approved landing page copy into a designed, working web page, using the UI/UX Pro Max design database to pick a layout, style, colors and fonts that fit their product and customer, then helps get it live. Use right after landing page copy is approved, or when the founder wants their landing page designed, built, made to look professional, published, or wants a design direction, colors or fonts for their site.
---

# Landing page design

Copy first, design second. This skill never writes new copy: it designs and builds the page around the copy the founder already approved with `keep100:landing-page`. The design intelligence comes from the bundled `keep100:ui-ux-pro-max` skill by NextLevelBuilder (MIT).

## Inputs

- The latest `marketing/*-landing-page.md`. If none exists, or the founder hasn't approved it, run `keep100:landing-page` first.
- `company/brand.md` (colors, fonts, voice), `company/product.md` (product type, platform, the signup or payment link), `company/customers.md` (who the visitor is).

If `company/product.md` has no signup or payment link, stop and ask for it. The page exists to send people there.

## Step 1: Brief

Write a one-line design brief from the company files, for example: "B2B SaaS invoicing tool for freelance designers, calm and trustworthy, free trial CTA". Include product type, customer, the voice words from `brand.md`, and the primary CTA. Never put private details (customer names, revenue) into search queries.

## Step 2: Design direction

- **Brand already set:** if `brand.md` is Confirmed and has colors and fonts, keep them. Use `keep100:ui-ux-pro-max` only for the layout pattern, style and UX rules.
- **No brand yet:** invoke the `keep100:ui-ux-pro-max` skill and ask it for a design system for the brief, saved under `marketing/`. That skill owns its own scripts and data. Don't call its files from here.

Show the founder the direction in plain words, not jargon: the page structure, the overall look (one sentence), the colors as swatches or hex codes with what each is for, the two fonts, and what it deliberately avoids. Recommend it, and offer one alternative look if they want a choice. On their yes, propose adding the colors and fonts to `company/brand.md` and confirming it.

## Step 3: Build the page

Build one self-contained `marketing/site/index.html` that opens in any browser: HTML with Tailwind from its CDN (or inline CSS), Google Fonts links for the chosen fonts, no build step.

- **Copy:** use the approved copy word for word, section by section. If the layout needs a line that doesn't exist (a nav label, a button), keep it to a few plain words and flag it.
- **Structure:** the six copy sections in order (hero, problem, solution, value props, FAQ, final CTA), laid out with the pattern from step 2.
- **Buttons:** every primary button opens the signup or payment link from `company/product.md`. Add `?ref=landing` if the founder wants to count clicks.
- **Proof stays earned:** no fake testimonials, logos, stars, ratings, user counts or stock-photo "customers". Where a product screenshot belongs, leave a clearly labelled placeholder box and tell the founder exactly which screenshot to put there.
- **Page basics:** a title under 60 characters and a description under 155, both from the hero. A share image note. A footer with the founder's or company's name and links to privacy and terms pages if they exist. If they don't, tell the founder they'll need them before collecting emails or payments.
- **B2C mobile apps:** App Store and Google Play buttons as the primary CTA.
- **Quality:** apply UI/UX Pro Max's pre-delivery checklist: SVG icons (never emoji), text contrast at least 4.5:1, visible focus states, mobile-first, no horizontal scroll, reduced motion respected, buttons at least 44 px tall.

## Step 4: Look at it, then review with the founder

If a browser or screenshot tool is available, open the page at phone width (375 px) and desktop width (1440 px) and look before showing it. Fix anything that overlaps, overflows or is hard to read. If you can't look, say so, and ask the founder to open the file on their phone and laptop.

Ask for reactions on three things only: does it feel like them, is anything hard to read, and does the main button stand out. Make the changes, then save.

## Step 5: Get it live

Explain the options in plain language and recommend one:
- **They already have a website builder** (Webflow, Framer, Wix, Squarespace, Carrd): use the page as the exact blueprint and paste the copy section by section.
- **They used an AI app builder** (Lovable, Bolt, v0, Replit) or have a developer: hand over `marketing/site/index.html` and the design system files and ask for it as the homepage.
- **They have nothing yet:** a free static host such as Netlify Drop takes the file as is.

When it's live, ask the founder to click the main button on their phone and confirm it reaches signup or payment. Record the live address in `company/product.md` under Links, with their yes. Tick "Landing page live" in `progress.md`, add a Work log line, run `keep100:dashboard`, and propose the next step in the plan.
