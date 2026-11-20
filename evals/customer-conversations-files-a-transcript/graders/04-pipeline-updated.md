---
type: regex
pattern: 'Ana Costa[^\n]*,queued,'
match: not_contains
target: { source: file, path: sales/pipeline.csv }
---

Ana has now talked to the founder. She must not stay queued for a cold first email.
