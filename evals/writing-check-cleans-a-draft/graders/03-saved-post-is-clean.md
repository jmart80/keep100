---
type: regex
pattern: 'game-chang|seamless|leverag|unlock|streamlin|—|200 clinics'
flags: i
match: not_contains
target: { source: file, path: social/linkedin-waiting-list.md }
---

The saved post has none of the flagged words, no long dash and no unconfirmed claim.
