# Variables

Single source of truth for every template variable, the banned vocabulary list, and fallback behavior for missing inputs. Specificity here determines output quality: if a value looks like the Bad example, push it toward the Good example before drafting.

## Dictionary

| Variable | Definition (source: `company/` files) | Good example | Bad example |
|---|---|---|---|
| `{icp}` | Specific role, team, or company type that buys | "doulas running solo practices" | "businesses" |
| `{jtbd}` | The functional job the buyer is hiring the product for | "track client visits and file session notes" | "manage their work" |
| `{category}` | The product noun a buyer would use to search or categorize | "practice management software" | "platform" |
| `{competitive_alternative}` | The named tool or vivid process being replaced, including "spreadsheets" or "do nothing" | "a shared Google Sheet and paper intake forms" | "legacy tools" |
| `{pain}` | A cost of the current way, in customer language | "re-typing intake info into three different places" | "inefficiency" |
| `{differentiated_capability}` | What the user can do with this product that the alternative cannot deliver | "auto-generate visit summaries from voice notes" | "powerful features" |
| `{feature}` | The technical component powering a capability | "HIPAA-compliant voice transcription engine" | "AI" |
| `{outcome}` | Falsifiable result with a unit (time, money, %, count) or a named before/after state | "cut charting from 40 minutes to 5 per visit" | "save time" |
| `{old_painful_way}` | The behavior the buyer stops doing | "copy-pasting between calendar, notes, and invoices" | "manual work" |
| `{objection}` | The top reason a convinced buyer still hesitates | "is my client data HIPAA-safe" | "price" |
| `{metric_proof}` | A real, defensible number from internal benchmarks or real usage. Optional. | "8x faster than manual charting (internal benchmark)" | any invented number |
| `{action_verb}` + `{value_noun}` | CTA components naming the action and the value received | "Start" + "your free practice" | "Submit" |

## Banned vocabulary (page-wide)

supercharge, streamline, revolutionize, transform, empower, unlock, leverage, cutting-edge, next-generation, world-class, seamless

## Fallbacks

When a positioning input is missing, do this instead of guessing:

| Missing input | Fallback |
|---|---|
| `{icp}` or `{jtbd}` | Halt and ask the user. Do not draft. |
| `{competitive_alternative}` | Default to the vivid manual process ("a shared spreadsheet and email threads"). Never "legacy tools". |
| `{outcome}` with a metric | Use a named before/after state only if defensible; otherwise state the eliminated behavior ("no more re-typing intake forms"). Never invent a number. |
| `{metric_proof}` | Exclude archetype G and the "Join N+" reinforcing line entirely. |
| Real users for the trust strip | Use the trust strip fallback beside the hero template in `templates.md`. |
| `{objection}` | Default the first FAQ to pricing or data security, whichever fits the ICP. |
