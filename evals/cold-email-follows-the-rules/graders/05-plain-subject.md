---
type: regex
pattern: '[Ss]ubject[:*\s]+[a-z0-9'',-]+(?: [a-z0-9'',-]+){1,4}\s*(?:\n|$)'
target: { source: file, path: sales/ana-costa-email-1.md }
---

The subject is two to five lowercase words with no question mark, like a note from a colleague.
