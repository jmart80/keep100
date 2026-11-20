---
type: regex
pattern: 'Priya Nair[^\n]*,won,'
target: { source: file, path: sales/pipeline.csv }
---

Priya's row says won, so no follow-up email is ever queued for her.
