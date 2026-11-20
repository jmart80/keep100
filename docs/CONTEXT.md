# Keep100 (the solo SaaS founder kit for Claude)

A public kit that turns Claude into a growth team for a founder with no technical, product or go-to-market background who has an MVP built or in progress.

## Language

**Founder**:
The person the kit is for: a solo, non-technical builder of a SaaS product who has an MVP built or in progress, intends to grow it without investors, and is on a paid Claude plan.
_Avoid_: user, customer, developer

**Kit**:
Everything a Founder receives from the one repo URL: guides, skills and connector setup.
_Avoid_: toolkit, pack, bundle

**Finish line**:
The outcome the Kit promises on both Tracks: paying customers within 30 days of starting the Kit. Framed as a plan, not a guarantee.
_Avoid_: launch, traction, success

**30-day plan**:
The ordered checklist the Kit walks a Founder through: Workspace setup, research, conversations, positioning, pricing, the founding offer and the landing page, followed by getting customers on their Track, with content and SEO near the end. Thirty days is the pace with about two hours a day. Progress is counted in Steps done, never in calendar days.
_Avoid_: course, program, roadmap

**Step**:
One checkbox in the Progress log. A Step is done, to do, or skipped with a reason. Each Step is ticked by exactly one Step skill.
_Avoid_: task, milestone, day

**Daily driver**:
How the Kit is used during the 30-day plan: the Founder asks Claude what today's work is, and Claude answers from the Progress log and Company model, then drafts the work.
_Avoid_: assistant mode, coach

**Progress log**:
The Workspace file (`progress.md`) holding the checklist of Steps, open loops, paying customers, one line of numbers a week, and the work log. It is read at the start of every session, so it stays small. It does not hold contacts or posts.
_Avoid_: tracker, journal, CRM

**Progress dashboard**:
A page built from the Progress log by a script, showing every Step, the next one, company file statuses and outreach numbers. It is a picture of the Progress log and holds nothing of its own. Claude rebuilds it whenever a Step changes.
_Avoid_: tracker, scorecard, report

**Pipeline**:
The one file (`sales/pipeline.csv`) recording every person contacted on the B2B track, the evidence for contacting them, each send and each reply.
_Avoid_: CRM, lead list, prospects file

**Customer conversation**:
A real exchange with a customer or prospect, filed in `conversations/` with quotes tagged verbatim or paraphrase.
_Avoid_: interview, user research

**Founding offer**:
The specific, true and limited reason for the first customers to buy now, recorded in `company/pricing.md`. Nothing may appear in copy as an offer unless it is recorded there.
_Avoid_: promo, deal, launch discount

**Key action**:
The first thing a new user does that shows the product works for them, recorded in `company/product.md`.
_Avoid_: aha moment, activation event

**Weekly brief**:
A scheduled weekly message that reminds the Founder where they are in the 30-day plan and setup, and once setup is done, suggests specific growth work to draft next (a blog post on a named topic, a social post about a named angle). It is about next actions. It carries one line of last week's numbers so the Founder can see which stage is losing people, and never a chart or a scorecard.
_Avoid_: weekly report, scorecard

**First session**:
The Founder's first sitting with the Kit. It delivers two wins: a Workspace and Claude set up properly for a solo founder, shown to them so they see what changed, and a before-and-after rewrite of their homepage headline built from their own material.
_Avoid_: onboarding, setup wizard

**Bootstrapped stance**:
The Kit's point of view, separate from the Finish line: with today's AI tools a Founder can do the work a funded team used to do, so they should keep 100% of their equity and skip pitch decks, fundraising and investors.
_Avoid_: no-investor promise, bootstrapping guarantee

**Track**:
The go-to-market motion a Founder follows, either the **B2B track** (selling to businesses, led by direct outreach) or the **B2C track** (selling to consumers, led by social media).
_Avoid_: mode, version, edition

**Workspace**:
The folder the Kit creates for a Founder, holding the Company model, one folder per Area, and the house rules Claude follows.
_Avoid_: project, vault, setup folder

**Company model**:
The single source of truth about the Founder's company: product, ICP, positioning, pricing, brand kit, competitors and facts. Every Area reads it; nothing copies it.
_Avoid_: company profile, knowledge base, context files

**Area**:
One kind of work in the Workspace (marketing, social, sales, research), with its own rules and saved outputs, reading from the Company model.
_Avoid_: project, department, module

**Confirmed fact**:
A statement the Founder has approved: anything in a company file whose status is Confirmed, or an entry marked `[confirmed]` in `facts.md`. Claude treats only Confirmed facts as true and says "I don't know" for anything else. Each fact has one home.
_Avoid_: draft fact, assumption

**Verbatim quote**:
Customer words that were seen exactly as written, in a page, a transcript or a message. Anything else is a paraphrase and is never shown inside quotation marks.
_Avoid_: testimonial, soundbite

**Writing check**:
The one skill that runs on every draft before the Founder sees it: checking claims against Confirmed facts, applying the brand voice, removing AI-sounding phrasing, and running the scripted checks. It runs because the house rules and every writing skill call it.
_Avoid_: always-on skill, background skill, filter

**Step skill**:
A skill that does one job in the 30-day plan (positioning, pricing, landing page, cold email). Claude proposes the next Step skill and starts it once the Founder says yes; the Founder never has to name it.
_Avoid_: workflow, module, command

**Kit-owned**:
Files that come from the Kit and update whenever it is released: skills, guides, templates.
_Avoid_: system files, core

**Founder-owned**:
Everything in a Founder's Workspace. The Kit never changes these without the Founder's yes.
_Avoid_: user data, local files

**Primary path**:
Installing the Kit as a plugin and using it in the Claude desktop app, where Claude keeps the Workspace folder up to date.
_Avoid_: default install

**Browser path**:
Installing the same plugin at claude.ai and keeping the Company model in a Claude Project, updated by hand.
_Avoid_: browser fallback, manual install

## Relationships

- A **Founder** follows exactly one **Track** toward the **Finish line**
- A **Workspace** has one **Company model** and many **Areas**; each **Area** reads the **Company model** and never copies it
- The **Company model** is filled from the Founder's existing material first, then by interview for the gaps, and each part becomes **Confirmed** when the Founder approves it
- A **Founder** installs the **Kit** as a plugin and works on the **Primary path**, or the **Browser path** when they have no desktop app
- A **Step** is ticked in the **Progress log** by the skill that finishes it, and the **Progress dashboard** is rebuilt from the log

## The company model contract

Skills hand work to each other through files. This table is the interface. A skill may read only what is listed here, and every heading listed must exist in the setup templates. `docs/contract.json` is the same contract in a form `scripts/validate.py` checks on every push.

| What | Lives in | Written by | Read by |
|---|---|---|---|
| Track, hours a day, start date, the checklist | `progress.md` | setup, then the skill that finishes each step | every skill, the dashboard |
| What it is, what is live, signup or payment link, key action, how email is sent | `company/product.md` | setup, activation | landing page, design, product emails, activation, launch |
| Ideal customer, tagged quotes, where they gather, hesitations | `company/customers.md` | setup, competitor research, customer conversations | positioning, social, cold email, offer, content |
| Alternatives, what only we have, category, category awareness, one-line statement | `company/positioning.md` | positioning | landing page, cold email, pricing, sales replies |
| Who to win first, champion, trigger events | `company/positioning.md` | positioning | prospect list, cold email |
| Job to be done, top objection | `company/positioning.md` | positioning | landing page |
| Value props, headline candidates | `company/positioning.md` | positioning | landing page, social |
| Plans, prices, trial, how a customer pays, allowed discounts, founding offer | `company/pricing.md` | pricing, offer | landing page, product emails, sales replies, launch |
| Voice, words to use and avoid, allowed words, colors, fonts | `company/brand.md` | setup, design | writing check, design |
| Alternatives, top pains, recommended opening, pricing pattern | `company/competitors.md` | competitor research | positioning, pricing, landing page, content |
| Proof with no other home: results, credentials, named customers | `company/facts.md` | the founder, through any skill | writing check, landing page, cold email |
| Who was contacted, why, each send and reply | `sales/pipeline.csv` | prospect list, cold email, sales replies | today, weekly brief, the dashboard |
| What worked | `learnings.md` | the weekly review, launch, conversations | every writing skill, weekly brief |
| What was decided and why | `decisions.md` | pressure test, workspace audit | pressure test |

Changing this table changes the kit's interface. Update `docs/contract.json`, the templates, both example workspaces and `update-workspace/changes.md` in the same change.
