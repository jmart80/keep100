# Section Templates

Every copy formula for the six page sections, with word limits and anti-patterns beside the template they govern. Draft from these only. Variables are defined in `variables.md`.

## 1. Hero

Elements: H1 headline, subheadline, primary CTA button, CTA microcopy, hero visual, trust strip.

### Headline

Max 10 words. Must contain at least one of: a category noun, a named ICP, a named competitive alternative, or a specific measurable outcome.

| ID | Archetype | Formula | Illustrative example |
|---|---|---|---|
| A | Capability-Led | {category} that {differentiated_capability}, so {icp} can {outcome} | "Issue tracking built for the speed of small software teams" |
| B | Outcome-Led (Anchored) | {outcome} for {icp} who {jtbd_context} | "Close the books in 3 days, not 12" |
| C | Category-Led | The {adjective} {category} for {icp} | "The practice management app built for doulas" |
| D | Competitive-Alternative-Led | Stop {old_painful_way}. / {category} that replaces {competitive_alternative} | "Capacity planning without the spreadsheet" |
| E | POV-Led | {contrarian_statement_about_status_quo} | "Your CRM shouldn't need a full-time admin" |
| F | Question-Led | Still {painful_activity} in {competitive_alternative}? | "Still chasing visa appointments by refreshing the portal?" |
| G | Number-Led | {metric_proof_outcome_statement} | "Cut charting time from 40 minutes to 5" |

Rules: B and G stay anchored only if the subheadline supplies the concrete category and capability. E and F must be resolved immediately by a subheadline naming the product category. Never use G with an invented or unverifiable number.

### Subheadline

Max 2 sentences, 25 words total. Its job is to supply whichever element the headline omitted:

| Headline leads with | Subheadline must supply | Formula |
|---|---|---|
| Outcome (B, G) | Concrete capability + ICP or category | {category} for {icp} that {differentiated_capability_1}, {differentiated_capability_2}, and {differentiated_capability_3} |
| Capability (A) | The outcome + ICP context | {icp} use {product_name} to {jtbd} and {outcome}, without {old_painful_way} |
| Category (C) | Differentiation + ICP specificity | Built for {icp}, {product_name} {differentiated_capability}, unlike {competitive_alternative_description} |
| POV or Question (E, F) | Category + capability resolution | {product_name} is {category} that {differentiated_capability} for {icp} |

### Primary CTA

2-5 words. Formula: {action_verb} {value_noun} or {action_verb} my {specific_deliverable}. Examples: "Start free trial", "See it in action", "Get my free audit", "Book a 20-minute demo". Type comes from the CTA decision table in `SKILL.md`.

### CTA microcopy

One line, max 8 words, directly under the button, addressing the single most common objection to clicking. Examples: "No credit card required", "Free 14-day trial, cancel anytime", "Setup in under 10 minutes", "HIPAA compliant".

### Hero visual

Default: real product UI (screenshot or short looping capture) showing the flagship capability. Illustration only when the product has no meaningful UI.

### Trust strip

No stars and no ratings, ever, unless a real rating is a `[confirmed]` fact with its source. Choose the first of these the founder has earned:

1. Up to three photos of real users (beta testers, design partners, early customers) who gave permission, recorded in `company/facts.md`, with one line saying who they are.
2. A compliance badge row, only for certifications actually held.
3. One specific trust line from confirmed facts ("Built with input from 14 practicing doulas" needs those 14 conversations to exist).
4. Nothing. An empty trust strip is better than an invented one.

## 2. Problem (Status-Quo Agitation)

First scroll after hero. Max 80 words. A point of recognition ("don't you hate this?"), not education ("did you know?"). Pick the one formula that best fits the positioning inputs:

- **Contrast Framing:** Most {icp} still {current_behavior_with_competitive_alternative}. The result: {pain_1}, {pain_2}, and {pain_3}.
  Example: "Most revenue ops teams still build pipeline reports in Google Sheets. The result: hours of manual cleanup, stale numbers by Monday, and no single source of truth."
- **Cost Amplification:** Every time {icp} {painful_activity}, {cost}. Multiply that by {frequency_or_scale}, and the math hurts.
  Example: "Every time your finance team manually reconciles an invoice, you risk a data error. Multiply that by 400 invoices a month, and the math hurts."
- **Status Quo Indictment:** {competitive_alternative} was not built for {jtbd}. It was built for {what_it_was_actually_built_for}. That gap costs {icp} {specific_cost}.
  Example: "Excel was not built for capacity planning. It was built for data storage. That gap costs engineering managers 6 hours a week they cannot get back."

Anti-patterns:

- Generic pain not tied to the named competitive alternative ("manual processes slow you down")
- Pain the product does not actually solve (breaks the payoff rule and creates distrust)
- Hyperbolic marketing language ("crippling inefficiencies", "drowning in data")
- More than 3 pain clusters; select the top 1-2

## 3. Solution Introduction

Immediately after Problem. Max 60 words. Names the new way and anchors it to the category and differentiated mechanism. Pick one formula:

- **Mechanism Intro:** Introducing {product_name}: {category} that {differentiated_capability}, built for {icp}.
- **Contrast Bridge:** {product_name} gives {icp} a {category} that {does_what_competitive_alternative_cannot}. The result: {outcome}.
- **Category Claim:** There is a better way. {product_name} is {category} that replaces {competitive_alternative} with {differentiated_capability}.

## 4. Value Props (Feature-to-Outcome Blocks)

4-6 blocks, each with a placeholder for a real product visual. This is where the page gets specific about HOW, at the feature and capability level. Maintain the **ladder** in every block:

- **Feature:** the technical component ("real-time sync engine")
- **Capability:** what the user does with it ("see every team's capacity updated live")
- **Outcome:** the result it produces ("stop rescheduling sprints because of surprise blockers")

Per-block formula, max 50 words per block:

```
[Block headline: capability statement, active voice, max 6 words]
{capability_description_in_active_voice}, so {icp} can {outcome_tied_to_jtbd}.
[Visual: screenshot or animated UI of this capability in action]
```

For High-complexity products, precede the blocks with a 3-step "How it works" strip (verb + noun, max 5 words per step) so the blocks have a mental model to attach to.

Anti-patterns:

- Block headline is a feature name or noun phrase with no user action
- Outcome missing from a block, or the same outcome repeated across blocks
- More than 6 blocks (dilution) or fewer than 4 (page feels thin)

## 5. FAQ (Objection Handling)

5-6 questions. Purpose: remove the specific, predictable blockers for a buyer who understands and values the product but has one unanswered question.

Rules:

- Replace the generic "FAQ" header with the answer to the single most important objection, then list the remaining questions below it
- Draw questions only from real objections for the founder's track. B2B: pricing details, contract terms, setup time, moving existing data, security and compliance, integrations. B2C: price and what happens after the trial, cancelling, privacy, whether it works for their situation, what they need to get started, who is behind it
- Answer each in 1-3 sentences; link to documentation for deep technical answers
- `{objection}`, from "Top objection" in `company/positioning.md`, is the first question
- Answer only from confirmed facts. If the files can't answer a question a buyer would ask, tell the founder and leave it out

## 6. Final CTA

A clear, specific, low-risk next step for the buyer who consumed the full page. No new value props here.

```
[Headline: echo the primary outcome from the hero, max 8 words]
{outcome_echo_from_hero}

[One reinforcing sentence: pick ONE]
  With proof:      Join {real_number}+ {icp_descriptor} who already {outcome_verb} with {product_name}.
  Pre-traction:    {risk_reducer_sentence} ("Set up your first {value_noun} in under 10 minutes, free.")

[Primary CTA button: identical text to hero primary CTA]
[Secondary CTA: "Talk to us" or "See pricing", for buyers who need more before committing]
[Microcopy: risk reducer, max 8 words]
```

Anti-patterns:

- A new value prop introduced here for the first time
- Generic headline ("Ready to get started?" tells the buyer nothing)
- Missing secondary CTA for buyers who need a human touch
- "Join N+ users" with a number that is not real
