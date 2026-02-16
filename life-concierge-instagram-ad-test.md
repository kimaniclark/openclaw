# Life Concierge Instagram Ad Test

**Created:** Feb 11, 2026  
**Status:** Setting up

---

## Ad Creative

**Image:** "Your entire life. Fully managed" post (man on laptop)  
**Source:** https://www.instagram.com/p/DPM_srwjWZu/

---

## Ad Copy

### Version A (Telegram CTA)
> One voice note = flights booked, bags packed, car waiting.
> 
> What if running your life was as easy as sending a text?
> 
> Life Concierge handles the details so you can focus on what matters.
> 
> Message us to get started → t.me/LifeConciergeBot

### Version B (Instagram DM CTA)
> One voice note = flights booked, bags packed, car waiting.
> 
> What if running your life was as easy as sending a text?
> 
> Life Concierge handles the details so you can focus on what matters.
> 
> Send us a DM to get started →

---

## A/B Test Structure

| Version | Platform CTA | Response Handler | Response Speed |
|---------|--------------|------------------|----------------|
| A | Telegram | Johnny (automated) | Fast |
| B | Instagram DM | Kimani (with Johnny suggestions) | Slower |

**Goal:** Test if people will actually go through the funnel to the point of paying. At checkout, they hit a pre-signup waitlist instead of Stripe.

---

## Technical Setup

- [ ] Create Telegram bot (@LifeConciergeBot or similar)
- [ ] Add bot token to OpenClaw config
- [ ] Create Discord mirror channel (#life-concierge-inbox)
- [ ] Set up welcome message for prospects
- [ ] Test bot flow

---

## Conversation Flow (Johnny)

1. Prospect messages
2. Johnny greets, asks what areas of life they want help with
3. Discovery conversation (pain points, current challenges)
4. Explain how Life Concierge works
5. When ready to sign up → collect info for waitlist (not actual payment)

**Key insight being tested:** Will people actually go through the full funnel, or do they drop off before "paying"?

---

## Tracking

- Ad impressions
- Ad clicks
- Telegram conversations started
- Instagram DM conversations started
- Conversations that reach "sign up" point
- Waitlist signups

---

## Budget

TBD - recommend $50-100 for initial test

---

## Notes

- Same image for both ads, different CTAs
- Testing platform friction AND response speed
- WhatsApp can be phase 2 if this works
