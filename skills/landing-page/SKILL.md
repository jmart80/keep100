---
name: landing-page
description: Writes complete homepage or landing page copy for a Keep100 founder, hero through final call to action, from their company files, then scores it against a 20-point checklist. Works for B2B and B2C. Use on day 5 of the plan, or when the founder wants landing page or homepage copy, a new hero headline, or their existing page scored and fixed.
---

# Landing page

Adapted from the saas-landing-page skill by Keep100's author. Six fixed sections in fixed order, with copy that is **anchored** (every outcome tied to what produces it), **falsifiable** (every claim could be checked), and **earned** (proof real or absent, never invented). Built for products with no logos, case studies or reviews yet.

Reference files, each read at the step that names it: [variables.md](variables.md), [templates.md](templates.md), [rubric.md](rubric.md).

## Branches

- **Full page** (default): steps 1 to 5.
- **Hero only:** steps 1 and 2, draft the hero from `templates.md`, score checks 1 to 5 and 17 to 19.
- **Score existing page:** read their live page (or pasted copy), run step 4 only, and give one fix per failing check.

## Steps

1. **Map.** Read `variables.md`. Fill every variable from `company/positioning.md`, `customers.md`, `product.md`, `pricing.md` and `facts.md` (confirmed facts only). Use the fallback table for gaps. If the ideal customer or the job they're hiring the product for is missing, stop and suggest running positioning first.
2. **Select** a headline archetype and CTA type from the tables below, naming the row that fired.
3. **Draft** all six sections from `templates.md` only, respecting every word limit. Every pain raised in section 2 must be answered in section 3 or 4.
4. **Score** all 20 checks in `rubric.md`. A failure sends that section back to step 3. Then run `keep100:writing-check`.
5. **Deliver** in the output shape below, save to `marketing/<date>-landing-page.md`, log it in `progress.md`.

Once the founder approves the copy, propose `keep100:landing-page-design` to design and build the actual page.

## Page sections

| # | Section | The belief it must create |
|---|---|---|
| 1 | Hero | "I understand what this is, who it's for, and why to keep reading." |
| 2 | Problem | "My current way is costing me more than I'd admitted." |
| 3 | Solution | "There's a better way, and this product is how." |
| 4 | Value props | "The specific mechanisms behind the promise are believable." |
| 5 | FAQ | "My specific question is answered." |
| 6 | Final CTA | "The next step is clear, specific and low-risk." |

## Track differences

| | B2B | B2C |
|---|---|---|
| `{icp}` | A role at a type of company ("operations leads at 10 to 50 person agencies") | A person in a situation ("new runners training for their first half marathon") |
| Primary CTA | Free trial, or a time-boxed demo if sales-assisted | Free signup or download; app store buttons for mobile apps |
| Typical top objection | Data security, setup time, switching cost | Price, privacy, "will I actually use it", cancelling |
| Proof that's allowed pre-traction | Specificity, certifications actually held, founder credibility | Specificity, a real screenshot or short demo, founder story |
| Tone | Calm, concrete, ROI in time or money | Warm, concrete, the feeling of the after-state |

## Decision rules

Inputs: **category awareness** (do buyers search for this category by name: known, emerging, unknown), **market sophistication** (stage 1-2 new and few competitors, 3-4 established, 5 over-marketed), **product complexity** (low, medium, high), **situation** (replacing something, or creating a new behavior), **motion** (self-serve or sales-assisted).

Headline archetype (formulas in `templates.md`):

| Awareness | Sophistication | Situation | Use |
|---|---|---|---|
| Known | 1-2 | Replacement | A (Capability-led) or B (Outcome-led) |
| Known | 3-4 | Replacement | D (Alternative-led) or A |
| Known | 4-5 | Replacement | E (Point-of-view) or D |
| Emerging | Any | New behavior | C (Category-led), capability in subheadline |
| Unknown | 1 | New behavior | C, point of view in subheadline |
| Known | Any | Any | G (Number-led) only with a confirmed number 3x+ better than the norm |
| Known | 3-5 | Replacement, pain widely felt | F (Question-led) as a variant to test |

Tie-breaker: pick the one that puts a concrete product noun in the hero.

CTA type:

| Motion | Complexity | Primary | Secondary |
|---|---|---|---|
| Self-serve | Low or medium | Free trial or free plan | Short demo video |
| Self-serve | High | Interactive demo | Free trial |
| Sales-assisted (B2B) | Any | Time-boxed demo | Pricing |
| Any, with a diagnostic offer | Any | "Get my free {deliverable}" | Demo |

## Output shape

```
# Landing page: {product}
Archetype: {id} (row that fired) | CTA: {type} | Track: {B2B|B2C}

## 1. Hero        headline / subheadline / CTA + microcopy / visual note / trust line
## 2. Problem     formula used + copy
## 3. Solution    formula used + copy
## 4. Value props "how it works" strip if high complexity; 4-6 blocks
## 5. FAQ         lead answer as the header, then 5-6 questions, top objection first
## 6. Final CTA   headline / reinforcing line / CTAs / microcopy

## Checklist score (20 rows: check, pass/fail, one line of evidence)
```

## Hard rules

- Never invent metrics, user counts, ratings, testimonials, customer names, faces or logos.
- No outcome without its mechanism in the same section.
- No word from the banned list in `variables.md`.
