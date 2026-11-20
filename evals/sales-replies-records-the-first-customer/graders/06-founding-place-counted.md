---
type: regex
pattern: '\b1 taken\b|\b1 of 10\b|\b9 (left|remaining|open)\b'
flags: i
target: { source: file, path: company/pricing.md }
---

The founding offer has 10 places. One is now taken, and every page and email reads that count.
