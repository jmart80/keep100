# sales/pipeline.csv

One row per person. This file is the only record of who was contacted. `progress.md` holds a one-line summary and nothing else about prospects.

## Columns

| Column | Meaning | Required |
|---|---|---|
| `added` | Date the row was added, YYYY-MM-DD | Yes |
| `name` | Full name as published | Yes |
| `role` | Job title or description | Yes |
| `company` | Company or project name | Yes |
| `link` | Public profile or company page for this person | Yes |
| `email` | Address, or blank | No |
| `email_source` | Where the address came from: `published`, the name of the founder's tool, or blank | When `email` is set |
| `lane` | `trigger` or `pain` | Yes |
| `trigger` | The event or the pain signal, in one line | Yes |
| `trigger_date` | Date of the event or post, YYYY-MM-DD | Yes |
| `source_url` | The page where the trigger was seen | Yes |
| `grade` | `A`, `B` or `C` | Yes |
| `status` | See below | Yes |
| `sent_1` to `sent_5` | Date each email in the sequence was sent | No |
| `replied` | Date of their first reply | No |
| `reply_type` | See below | When `replied` is set |
| `next_step` | What happens next, in a few words | No |
| `next_date` | When it happens | No |
| `notes` | Anything else, kept short | No |

## Status

| Value | Meaning |
|---|---|
| `queued` | Graded A or B, not yet contacted |
| `active` | In the sequence, no reply yet |
| `replied` | Replied, conversation open |
| `call_booked` | A call is on the calendar |
| `won` | Paying customer |
| `lost` | Said no, or the conversation ended |
| `not_now` | Asked to be contacted later. `next_date` says when |
| `stopped` | Opted out. Never contact again. Never delete the row |
| `bounced` | The address failed |
| `parked` | Graded C, or the trigger went stale |

## Reply types

`positive`, `question`, `objection`, `not_now`, `referral`, `wrong_person`, `opt_out`, `auto_reply`

## Follow-up timing

The script counts from `sent_1`: email 2 after 3 days, email 3 after 7, email 4 after 12, email 5 after 19. Any reply ends the sequence. Change the numbers at the top of `scripts/pipeline.py` if the founder's sequence differs.

## Header row

```
added,name,role,company,link,email,email_source,lane,trigger,trigger_date,source_url,grade,status,sent_1,sent_2,sent_3,sent_4,sent_5,replied,reply_type,next_step,next_date,notes
```
