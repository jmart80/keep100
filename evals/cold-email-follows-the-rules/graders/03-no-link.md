---
type: regex
pattern: 'https?://|www\.'
match: not_contains
target: { source: file, path: sales/ana-costa-email-1.md }
---

No link in a first email. Links in cold first emails hurt delivery.
