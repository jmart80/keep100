---
type: regex
pattern: 'Signup path checked[\s\S]*Launch in three places|Launch in three places[\s\S]*Signup path checked'
target: { source: file, path: dashboard.html }
---

The page holds the whole checklist, not a summary.
