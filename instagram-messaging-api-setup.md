# Instagram Messaging API Setup Guide

**For:** Life Concierge click-to-message ads  
**Instagram Account:** [@lifeconcierge.co](https://www.instagram.com/lifeconcierge.co)  
**Future consideration:** Reserve @lifeconcierge.ai handle

---

## What is Instagram Messaging API?

The Instagram Messaging API allows businesses to:
- Receive Instagram DMs programmatically
- Send automated responses
- Handle conversations at scale
- Integrate with click-to-message ads

**Key difference from WhatsApp Business API:** No 24-hour messaging window restriction for Instagram DMs.

---

## Prerequisites

### 1. Instagram Business Account ✅
- Your account must be converted to a **Business** or **Creator** account
- Check current status: Instagram Settings → Account → Switch to Professional Account
- Likely already done if you ran ads before

### 2. Facebook Page Connected
- Instagram Business account must be linked to a Facebook Page
- This is how Meta connects the API permissions

### 3. Meta Business Account
- Create at [business.facebook.com](https://business.facebook.com)
- Add your Facebook Page to Business Manager
- Add Instagram account to Business Manager

### 4. Meta Developer Account
- Register at [developers.facebook.com](https://developers.facebook.com)
- Create a new App (type: Business)

---

## Setup Process (Step-by-Step)

### Phase 1: Meta Business Setup

**1. Create/Verify Meta Business Manager**
- Go to [business.facebook.com](https://business.facebook.com)
- Create business (or use existing)
- **Business verification required** (may take days-weeks)
  - Upload business documents
  - Confirm business details
  - Wait for Meta approval

**2. Connect Instagram Account**
- Business Manager → Settings → Instagram Accounts
- Add @lifeconcierge.co
- Confirm ownership

**3. Create Facebook Page (if needed)**
- Create page for Life Concierge
- Link to Instagram account in Page Settings

### Phase 2: Developer App Setup

**1. Create Meta App**
- Go to [developers.facebook.com/apps](https://developers.facebook.com/apps)
- Click "Create App"
- Type: **Business**
- Purpose: Messenger Platform / Instagram Messaging

**2. Add Instagram Messaging Product**
- In your app dashboard
- Add Product → Messenger
- Configure → Instagram → Enable

**3. Generate Access Tokens**
- App Dashboard → Messenger → Settings
- Generate Page Access Token
- **Important:** This token expires; you'll need a long-lived or permanent token for production

**4. Configure Webhooks**
- Need a public HTTPS endpoint to receive messages
- Webhook URL: `https://your-domain.com/webhook/instagram`
- Subscribe to events:
  - `messages`
  - `messaging_postbacks`
  - `messaging_optins`
  - `message_reads`

**5. Request Instagram Messaging Access**
- App Dashboard → Instagram → Request Access
- Meta will review your use case
- Approval can take 1-3 weeks
- Need to demonstrate legitimate business purpose

### Phase 3: OpenClaw Integration

**Current Status:** OpenClaw does not have a built-in Instagram Messaging plugin.

**Two Options:**

#### Option A: Custom Plugin (Build it)
- Create OpenClaw plugin for Instagram Messaging
- Similar to existing Telegram plugin architecture
- Handles webhook receiving + API sending
- **Effort:** Medium-High (development required)

#### Option B: External Service Bridge
- Use third-party service (e.g., ManyChat, Chatfuel) as middleware
- Service receives Instagram DMs → forwards to OpenClaw via webhook
- OpenClaw responds via their API
- **Effort:** Low-Medium (configuration only)
- **Downside:** Additional cost, less control

#### Option C: Direct Implementation
- Build Node.js service that:
  - Receives Instagram webhooks
  - Sends messages to OpenClaw Gateway API
  - Receives responses from OpenClaw
  - Sends via Instagram API
- **Effort:** Medium (custom glue code)

---

## Technical Requirements

### Webhook Server Needs:
- **HTTPS endpoint** (Meta requires SSL)
- **Public domain** (not localhost)
- Can use **ngrok** for development (like your Twilio setup)
- Production: Deploy on cloud server

### API Integration Needs:
- Store Instagram Page Access Token securely
- Handle webhook verification (Meta challenge)
- Parse incoming message payload
- Send messages via Graph API
- Track conversation state

---

## Instagram Graph API Basics

**Send a message:**
```bash
curl -X POST "https://graph.facebook.com/v18.0/me/messages" \
  -H "Content-Type: application/json" \
  -d '{
    "recipient": {"id": "<INSTAGRAM_USER_ID>"},
    "message": {"text": "Hello from Life Concierge!"}
  }' \
  -d "access_token=<PAGE_ACCESS_TOKEN>"
```

**Receive messages:** Via webhook POST to your endpoint

---

## Click-to-Message Ad Setup

Once API is configured:

**1. Create Ad in Ads Manager**
- Campaign Objective: **Messages**
- Placement: Instagram only
- Messaging App: Instagram

**2. Ad Creative**
- Image/video showcasing Life Concierge
- Headline: "Your AI Executive Assistant"
- CTA Button: **"Send Message"**

**3. Destination**
- Instagram Direct
- Messages go to @lifeconcierge.co
- Bot receives and responds automatically

**4. Audience Targeting**
- Age: 25-55
- Interests: Productivity, entrepreneurship, coaching
- Lookalike audience from Circle.so members (if possible)

---

## Estimated Timeline

| Phase | Task | Time |
|-------|------|------|
| 1 | Meta Business verification | 3-14 days |
| 2 | Developer app setup | 1 day |
| 3 | Instagram Messaging access request | 7-21 days |
| 4 | Webhook server deployment | 1-3 days |
| 5 | OpenClaw integration (custom) | 3-7 days |
| 6 | Testing | 2-3 days |
| **Total** | | **3-7 weeks** |

---

## Alternative: Faster Path with Telegram

While Instagram API is being set up, you can launch ads **now** using:

**Option 1: Instagram Bio Link**
- Ad drives to Instagram profile
- Bio link: "Message us on Telegram: @LifeConciergeBot"
- User clicks → opens Telegram
- **Pro:** Can launch immediately
- **Con:** Extra friction (one more tap)

**Option 2: Landing Page with Telegram Widget**
- Ad drives to lifeconcierge.ai landing page
- Telegram chat widget embedded
- User clicks "Start Chat" → opens Telegram
- **Pro:** Professional, works now
- **Con:** Requires landing page

**Option 3: Instagram DMs (Manual Bridge)**
- Ad CTA: "Send Message" to Instagram
- You manually forward DM leads to Johnny on Telegram
- Johnny drafts responses, you paste back to Instagram
- **Pro:** Test demand immediately
- **Con:** Manual work (but validates concept)

---

## Recommended Approach

**Phase 1 (Now - Beta):**
- Run ads with Instagram bio link → Telegram
- Or landing page with Telegram widget
- Validate demand, refine messaging
- Manual/semi-automated (proof of concept)

**Phase 2 (Post-Beta - Weeks 4-8):**
- Begin Meta Business verification process
- Request Instagram Messaging API access
- Build integration while beta runs

**Phase 3 (Scale - Month 3+):**
- Full automated Instagram DM → Johnny flow
- Scale ad spend with proven funnel

---

## Costs

| Item | Cost |
|------|------|
| Meta Business verification | Free |
| Instagram Messaging API | Free (pay for ads only) |
| Webhook hosting (ngrok dev) | Free tier OK |
| Webhook hosting (production) | $5-20/month |
| Development (if outsourced) | $500-2000 |
| Ads budget | Variable ($50-500+/day) |

---

## Domain Strategy

**Current:** @lifeconcierge.co (Instagram), thelifeconcierge.co (web)  
**Future:** Consider securing:
- **@lifeconcierge.ai** (Instagram handle)
- **lifeconcierge.ai** (domain) - already owned ✅
- Stronger brand for AI product positioning

---

## Next Steps

1. **Immediate:** Verify if @lifeconcierge.co is Business account
2. **Week 1:** Create Meta Business Manager, start verification
3. **Week 1:** Create landing page with Telegram widget (launch ads fast)
4. **Week 2-4:** Developer app setup, request API access
5. **Week 4-8:** Build/deploy webhook integration
6. **Week 8+:** Launch fully automated Instagram DM ads

---

## Questions to Answer

- [ ] Is @lifeconcierge.co currently a Business or Creator account?
- [ ] Do you have a Facebook Page for Life Concierge?
- [ ] Do you have Meta Business Manager set up?
- [ ] Is business verified with Meta?
- [ ] Preference: Build custom integration or use faster Telegram bridge?
- [ ] Budget for development if needed?

---

*Created: 2026-02-02*  
*This guide will be updated as we progress through setup.*
