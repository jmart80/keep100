# Sending setup

Read this before the founder sends a first cold email. Adapted from the deliverability reference of the cold-email skill in coreyhaines31/marketingskills (MIT), cut down to a founder sending a few emails a day by hand.

Mailbox providers and the law both change. Treat every number here as a starting point, and have the founder check the current rules for where their prospects are.

## Before the first send

| Do | Why |
|---|---|
| Send from a real mailbox with the founder's name, on a domain the founder owns | A person writing to a person is the whole approach |
| Prefer a second domain that is plainly the founder's, such as `try{product}.com`, pointing at the main site | If cold email goes wrong, the main domain still delivers invoices and password resets. At a handful of personal emails a day the risk is small, and the founder may choose the main domain knowingly |
| Set up SPF, DKIM and DMARC on the sending domain | Providers reject or junk mail that fails these. The founder's domain or email provider has a setup page for each |
| Send a few normal emails from a new mailbox for two weeks before any cold ones | A brand-new mailbox that sends only cold email looks like spam |
| Check every address before sending | Bounces damage the sender quickly. Use only addresses with a known source in `sales/pipeline.csv` |

If the founder cannot do the domain steps, help them through it one screen at a time, or suggest they ask whoever set up their domain.

## In every email

- Plain text. No images, no tracking pixels, no attachments
- No link in the first email
- A one-line way out, in the founder's own voice, such as "If this isn't relevant, tell me and I won't write again"
- The founder's name and a postal address for the business in the signature, where the law requires one. United States law does for commercial email
- Sent one at a time, each with its own personal detail. Identical bodies sent in bulk are what filters look for

## How many

Start with five new emails a day and move to ten once replies are arriving and nothing bounces. Follow-ups count toward the day's total. A solo founder answering replies personally rarely needs more, and more volume from one mailbox raises the risk for little gain.

## Opt-outs

Anyone who asks to stop is marked `stopped` in `sales/pipeline.csv` the same day and is never written to again. The row is kept so they are never re-added.

## Where the prospect is matters

Rules differ by country. Some require consent before a first email to an individual, and treat a named person at a company differently from a generic company address. Before the first send, ask the founder where most prospects are, and have them check the rules for that country or get advice. Record the answer in `sales/CLAUDE.md`. Claude is not a lawyer and this file is not legal advice.

## Stop and look when

| Sign | Likely cause | Do |
|---|---|---|
| Any bounce on a list this small | A guessed or stale address | Stop. Recheck every remaining address and its source |
| A reply saying it landed in spam | Missing authentication, or copy that reads as bulk | Check SPF, DKIM and DMARC. Send a test to the founder's own other account |
| Two people ask to be removed in a week | The list or the reason for writing is wrong | Stop sending. Review the triggers with `keep100:prospect-list` |
| Many sends over several weeks and no replies at all | Wrong people, or a problem they do not have | More volume will not fix it. Go to `keep100:customer-conversations` and `keep100:pressure-test` |
