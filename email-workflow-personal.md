# Personal Email Workflow — kimani@kimaniclark.com

**Version 2** — March 30, 2026
**Volume:** ~111 emails/month (~4/day)

---

## Inbox Snapshot (30-day audit)

| Category | Count | % |
|----------|-------|---|
| Updates (Calendly, Zoom, LearnWorlds, etc.) | 47 | 42% |
| Primary (real conversations) | 38 | 34% |
| Newsletters/Marketing | 23 | 21% |
| Promotions | 3 | 3% |

**Top senders:** kimaniclark.com aliases (16), Bookclubs (15), Calendly (10), Zoom (9), Google (5), Craigslist (4), LearnWorlds (4), Skool (4), Netflix (4)

---

## Tools

### Jace.ai — Labeling & Sorting
Jace handles AI-powered email classification. It has a chat interface where instructions can be given in natural language. If a new label or rule is needed, Tron will provide Kimani with a prompt to paste into Jace.

### Tron — Reviewing & Acting
Tron reviews auto-archived labels during heartbeats, alerts Kimani in Discord, drafts replies, and cross-references emails with calendar/tasks/business context.

**Split: Jace sorts → Tron reviews and acts**

---

## Labels (managed in Jace.ai)

| Label | Purpose | Skips Inbox? | Tron Reviews? |
|-------|---------|:---:|:---:|
| **Receipts** | Payment confirmations, subscription charges, things already paid | ✅ | ✅ Flag failures/unexpected charges |
| **Invoices** | Bills, payment requests, payments that didn't go through | ✅ | ✅ **Always alert Kimani** |
| **Meetings** | Zoom, Calendly, scheduling notifications | ✅ | ✅ **Always alert Kimani** |
| **Bookclub** | Bookclubs.com notifications | ✅ | Check for action items |
| **FYI** | General informational (status pages, digests, non-financial) | ✅ | Scan for anything notable |
| **Gym Equipment Sales** | Craigslist responses | ✅ | Alert in #home |
| **Needs Reply** | Emails awaiting Kimani's response | ❌ | Help draft replies |
| **To Do** | Action items (DocuSign, etc.) | ❌ | Alert if time-sensitive |
| **Waiting** | Sent, awaiting other party's response | ❌ | Track and follow up |
| **Promotion** | Marketing/promos | ✅ | Ignore unless relevant |

---

## VIP Senders (always alert Kimani)

| Sender | Who | Context |
|--------|-----|---------|
| **Kristin Sakowski** (tripplans.co) | Travel agent | Important — always flag |
| **Lu Molenje** (mastermindmedia.com) | Friend from high school + patent law client | Important — always flag |
| **DocuSign** (docusign.net) | Signature requests | Time-sensitive — always flag |

---

## Newsletters to Keep

These are wanted — Jace should NOT archive or unsubscribe:

- **Exotic Car Hacks** (exoticcarhacks.com)
- **Watch Trading Academy**
- **Operation Underground Railroad / OUR Rescue** (ourrescue.org)
- **Efficient App**

### Unsubscribe Candidates

- **ZBiotics** — unsub?
- **Metropolis (parking)** — unsub?

---

## Tier 1: Auto-Archived (Jace handles, Tron reviews)

| Type | Examples | Label | Tron Action |
|------|----------|-------|-------------|
| Zoom join notifications | "has joined your meeting" | Meetings | Alert Kimani of upcoming/new meetings |
| Calendly events | New/canceled/rescheduled | Meetings | Alert Kimani, cross-reference calendar |
| Subscription payments | LearnWorlds, Netflix, etc. | Receipts | Flag failures or unexpected charges |
| Payment failures | Google Workspace, etc. | Invoices | **Alert Kimani immediately** |
| Bills/invoices | Any payment due | Invoices | **Alert Kimani immediately** |
| Status page alerts | Claude status, etc. | FYI | Ignore unless prolonged outage |
| Skool/community digests | Monthly digests | FYI | Ignore |
| Craigslist inquiries | Buyer messages | Gym Equipment Sales | Alert in #home |
| Bookclub routine | Ratings, reminders | Bookclub | Alert only if meeting changes |

## Tier 2: Tron Reviews, Alerts If Important

| Type | Examples | Action |
|------|----------|--------|
| **VIP senders** | Kristin Sakowski, Lu Molenje | Alert immediately in Discord |
| **DocuSign** | Signature requests | Alert immediately — time-sensitive |
| **Unknown senders** | New contacts, cold emails | Summarize & alert if seems legit |
| **Craigslist buyer inquiries** | Gym equipment | Alert in #home |

## Tier 3: Stays in Inbox (Kimani's Eyes)

| Type | Examples | Tron Support |
|------|----------|--------------|
| Personal conversations | Direct replies, threads | Draft replies if possible |
| Business contacts | Gospel NYC, clients, lawyers | Provide context |
| Wanted newsletters | Exotic Car Hacks, OUR Rescue, etc. | Stays in inbox |

---

## Tron's Heartbeat Email Checks

During regular heartbeats (2-4x/day), Tron will:

1. **Check Invoices label** — alert Kimani about any bills to pay or failed payments
2. **Check Meetings label** — alert Kimani about new/changed meetings
3. **Check Receipts label** — flag payment failures or unexpected charges
4. **Scan inbox** for unread messages from VIP senders
5. **Review other archived labels** (FYI, Bookclub, Gym Equipment Sales) for anything notable
6. **Alert in Discord** for anything time-sensitive
7. **Draft replies** when possible (scheduling, simple responses)

### Priority order for heartbeat email checks:
1. Invoices (money owed)
2. Meetings (scheduling)
3. VIP senders (Kristin, Lu, DocuSign)
4. Inbox unread
5. Everything else

---

## Alias Usage

| Address | Purpose |
|---------|---------|
| kimani@kimaniclark.com | Personal (primary inbox) |
| assistant@kimaniclark.com | Tron sends on Kimani's behalf |
| admin@kimaniclark.com | Newsletter signups, website logins |

---

## Next Steps

1. ✅ Kimani sets up Receipts and Invoices labels in Jace
2. ✅ Kimani enables auto-archive (skip inbox) for Tier 1 labels in Jace
3. ⬜ Tron starts heartbeat email monitoring
4. ⬜ Monthly review — adjust labels/rules based on new patterns

---

*This is a living document. Tron updates it as the workflow evolves.*
