# Variables

Single source of truth for every template variable, the banned vocabulary list, and fallback behavior for missing inputs. Specificity here determines output quality: if a value looks like the Bad example, push it toward the Good example before drafting.

## Dictionary

| Variable | Definition and source | Good example | Bad example |
|---|---|---|---|
| `{icp}` | Who buys. `positioning.md`: Who to win first, Champion | "doulas running solo practices" | "businesses" |
| `{jtbd}` | The job the buyer is hiring the product for. `positioning.md`: Job to be done | "track client visits and file session notes" | "manage their work" |
| `{category}` | The product noun a buyer would use to search. `positioning.md`: Category | "practice management software" | "platform" |
| `{competitive_alternative}` | The named tool or vivid process being replaced, including "spreadsheets" or "do nothing". `positioning.md`: Alternatives we beat | "a shared Google Sheet and paper intake forms" | "legacy tools" |
| `{pain}` | A cost of the current way, in customer language. `customers.md` quotes, `positioning.md`: Value props | "re-typing intake info into three different places" | "inefficiency" |
| `{differentiated_capability}` | What the user can do with this product that the alternative cannot deliver. `positioning.md`: What only we have, checked against `product.md` | "auto-generate visit summaries from voice notes" | "powerful features" |
| `{feature}` | The technical component powering a capability | "HIPAA-compliant voice transcription engine" | "AI" |
| `{outcome}` | Falsifiable result with a unit (time, money, %, count) or a named before/after state | "cut charting from 40 minutes to 5 per visit" | "save time" |
| `{old_painful_way}` | The behavior the buyer stops doing | "copy-pasting between calendar, notes, and invoices" | "manual work" |
| `{objection}` | The top reason a convinced buyer still hesitates. `positioning.md`: Top objection | "is my client data HIPAA-safe" | "price" |
| `{metric_proof}` | A real number marked `[confirmed]` in `facts.md`. Optional. | "8x faster than manual charting (internal benchmark)" | any invented number |
| `{action_verb}` + `{value_noun}` | CTA components naming the action and the value received | "Start" + "your free practice" | "Submit" |

## Banned vocabulary

Keep100 has one banned list. `keep100:writing-check` holds it and its script checks the page against it. Words the founder allows for their field are in `company/brand.md`.

## Fallbacks

When a positioning input is missing, do this instead of guessing:

| Missing input | Fallback |
|---|---|
| `{icp}` or `{jtbd}` | Stop and ask the founder. Do not draft. |
| `{competitive_alternative}` | Default to the vivid manual process ("a shared spreadsheet and email threads"). Never "legacy tools". |
| `{outcome}` with a metric | Use a named before/after state only if defensible; otherwise state the eliminated behavior ("no more re-typing intake forms"). Never invent a number. |
| `{metric_proof}` | Exclude archetype G and the "Join N+" reinforcing line entirely. |
| Real users for the trust strip | Work down the trust strip list beside the hero template in `templates.md`. Never stars. |
| `{objection}` | Default the first FAQ to price, or to data security for B2B. Tell the founder it's a default. |
| Signup or payment link | Stop and ask. A page whose button goes nowhere can't get a customer. |
