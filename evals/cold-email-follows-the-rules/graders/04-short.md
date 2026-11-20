---
type: regex
pattern: '(?:\S+\s+){130,}\S+'
match: not_contains
target: { source: file, path: sales/ana-costa-email-1.md }
---

The whole file, subject included, is under about 130 words. The email itself must be under 100.
