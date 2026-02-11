# Social Contacts Database

Personal CRM for managing relationships, context, and social planning.

## Structure

Each contact is a markdown file: `contacts/firstname-lastname.md`

## Contact Template

```markdown
# [Full Name]

## Basic Info
- **Phone:** 
- **Email:** 
- **Location:** 
- **Birthday:** 
- **Met:** [how/where you met]

## Context
[Who they are, what they do, how you know them]

## Their World
- **Business/Work:** 
- **Interests:** 
- **Family:** 

## Notes
[Anything useful - their favorite spots, things they mentioned, gift ideas, etc.]

## History
- [Date] - [Interaction/event]
```

## Usage

Johnny has full access to search and update these files. Use for:
- Planning social events and who to invite
- Remembering context before reaching out
- Tracking last interactions
- Gift ideas and preferences

## Relationship Maintenance

Johnny monitors contact frequency and sends reminders when someone is overdue.

**Frequency tiers:**
- weekly, monthly, quarterly, 6-months, 9-months (max)

**Meetup types:**
- lunch, dinner, drinks, activity, text-only

**What Johnny does:**
1. During heartbeats, checks who's overdue
2. Pings with context and suggests reaching out
3. For meetup contacts: offers to schedule lunch/dinner/drinks
4. Tracks when you actually reached out
5. Weekly summary on Sundays: "4 people to catch up with this week"

## Two-Tier System

**Full CRM** (from Quo/OpenPhone)
- Everyone in Kimani's network
- Stored for reference and context
- No proactive outreach unless requested

**Inner Circle** (from Contacts Journal)
- ~100 curated people Kimani wants to stay in touch with
- Active relationship maintenance with frequency tracking
- Proactive reminders and meetup scheduling
- Marked with `Inner Circle: yes`

## Sources

- Quo (OpenPhone) contacts - broad network, notes on friends' stores
- Contacts Journal CSV export - inner circle with frequencies
