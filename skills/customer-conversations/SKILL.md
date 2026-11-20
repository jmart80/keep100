---
name: customer-conversations
description: Gets a Keep100 founder talking to real customers and prospects, then turns each conversation into evidence the rest of the kit can use. Finds people to talk to, writes the invitation, prepares questions about what people actually did, extracts word-for-word quotes from a transcript or notes, and updates company/customers.md once a pattern repeats. Use early in the plan alongside competitor research and every week after that, or whenever the founder mentions a customer call, a user interview, a demo, a transcript, call notes, feedback from a user, "nobody is replying", "is anyone going to pay for this", or asks who their customer really is.
---

# Customer conversations

Adapted from the customer-research skill in coreyhaines31/marketingskills (MIT). The question style follows Rob Fitzpatrick's *The Mom Test* and Bob Moesta's switch interviews.

Review mining tells you what strangers said about other products. A conversation tells you what this person did last month, what it cost them, and whether they would pay. One good conversation outranks twenty mined reviews, so the kit asks for five early and one or two every week after.

## Rules

- **Past behavior beats opinion.** Ask what they did, when, and what it cost. "Would you use this?" produces a polite yes that means nothing.
- **Listen, don't pitch.** The founder talks less than a third of the time. The product comes up only if they ask, or at the very end.
- **Quotes are exact or they are not quotes.** Tag a line `[verbatim]` only when the words appear in a transcript, a recording summary with speaker text, or a message the person wrote. Anything from memory or from the founder's notes is `[paraphrase]`. Copy later uses verbatim lines only.
- **A pattern needs repeats.** One person is an anecdote. Change `company/customers.md` or `company/positioning.md` only when the same thing shows up in three conversations, and say how many of how many.
- **Compliments are not evidence.** "Love it", "great idea" and "I'd definitely buy that" get logged as compliments and ignored. A commitment is evidence: time booked, an introduction made, money paid.
- **Ask before recording, and store little.** First name, role and company type are enough. Never store anything about health, money trouble or other sensitive matters, even if the person volunteers it.

## Inputs

`company/customers.md`, `company/positioning.md`, `sales/pipeline.csv` (people who replied), `conversations/`, `progress.md`. Read `conversations/CLAUDE.md` before filing anything. If Granola or another call-notes connector is connected, use it to fetch transcripts instead of asking the founder to paste them.

## Branch A: Find people and invite them

1. Pick the source by what the founder has, in this order:
   - Paying customers or active users. Start with the ones who use it most.
   - People who replied to outreach, signed up, or joined a waitlist.
   - People who posted publicly about the problem in a professional setting. Use `keep100:prospect-list` to find them.
   - People the founder knows who fit the ideal customer exactly. Friends who do not fit are worse than no one, because they are kind.
2. Aim for five booked. Invite ten.
3. Draft the invitation with the founder. Under 60 words, from the founder, no pitch, a specific reason this person was chosen, a 20-minute ask, two time options. Read `references/invitations.md` for the shapes.
4. Run `keep100:writing-check`. The founder sends. Log each invitation in `sales/pipeline.csv` if the person is a prospect, otherwise in `conversations/invited.md`. Tick "Customer conversations invited" in `progress.md` once ten invitations are out.

## Branch B: Prepare a conversation

1. Write down, in one line each, the three things the founder most needs to learn. If positioning is Provisional, use its "what to learn from the first customers" list.
2. Write down what answer would prove the founder wrong on each. If no answer could, the question is a leading one. Rewrite it.
3. Build a one-page guide from `references/questions.md`: an opener, five or six questions, and the closing ask. Save to `conversations/<date>-guide.md`.
4. Remind the founder of the closing ask, because it is the part people skip: "Who else should I talk to?" and, when the person clearly has the problem, one request for a commitment that fits the stage. Options are a second call to see the product, an introduction, a paid pilot, or a pre-order.

## Branch C: Process a conversation

Run this the same day, while the founder still remembers what the notes leave out.

1. Get the raw material: a transcript from the connector, a pasted transcript, or the founder's notes. Say which one you have, because it decides how quotes are tagged.
2. Extract into `conversations/<date>-<first-name>-<role>.md` using this shape:

```
# {First name}, {role} at {type of company}
Date: {date} | Source: {transcript|notes} | Recorded with permission: {yes|no}
Fit: {ideal customer | near | not a fit}, because {one line}

## What happened, in order
{The moment they noticed the problem, what they tried, what they use now, what it costs them.}

## Quotes
- [verbatim|paraphrase] [{pain|goal|trigger|alternative|hesitation|wording}] "{line}"

## What they do today instead
## What would make them switch, and what would stop them
## Commitments made
{Time, introduction, money. "None" is a valid answer.}
## Compliments (not evidence)
## Surprises
{Anything that contradicts a company file. Name the file and the line.}
```

3. Tell the founder the two or three things that matter from this one conversation, and name anything that contradicts a company file.
4. If the person is in `sales/pipeline.csv`, update their row.

## Branch D: Roll up

Run after every third conversation, and before positioning or a landing page rewrite.

1. Read every file in `conversations/`. Count each pain, trigger, alternative and hesitation by how many people raised it without being prompted.
2. Report as a short table: the theme, how many of how many, the strongest verbatim quote, and whether the people who said it were ideal customers.
3. Propose changes, each with its count, and apply only on a yes:
   - new verbatim quotes for `company/customers.md`, tagged as our customer or prospect
   - a change to the ideal customer, if the people with the strongest pain are not who the file describes
   - a note for `company/positioning.md` when three or more conversations contradict it. Recommend rerunning `keep100:positioning` instead of editing it by hand
4. Write what was learned, and what is still unknown, to `learnings.md` under Customers. Add a Work log line to `progress.md` and run `keep100:dashboard`.
5. If five conversations with ideal customers produced no commitment of any kind, say so plainly. That is the most important finding the kit can give a founder, and the next step is `keep100:pressure-test` on who the product is for.

## When nobody agrees to talk

Three invitations with no answer is normal. Twenty is information. Check the list first (are these people who have the problem this month?), then the reason given for choosing them, then the ask. Offer something useful in return, such as the summary of what the founder learns across all conversations.
