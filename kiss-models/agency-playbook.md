# Modeling Agency AI Operations Playbook
*A repeatable framework for AI-assisted agency management*
*Built on Kiss Model Management — exportable to any agency*

---

## Purpose
This playbook documents every repeatable process we build for Kiss Models. The goal is:
1. Run Kiss Models efficiently with AI
2. Package this as a standalone agent/bot for other agencies
3. Sell as a product ("Agency AI" or similar)

Every section should be written as if explaining to a new agency — not Kiss-Models-specific.

---

## Integrations Required

| Integration | Purpose | Notes |
|-------------|---------|-------|
| Gmail (agency email) | Read/send all agency communications | OAuth via Google Cloud |
| Slack | Internal comms with agency team | Bot token + app token |
| Portfolio Pad / talent CRM | Roster database | Export CSV; no API yet |
| Jace.ai | Email classification + auto-drafts | Configured per agency |
| Apollo.io | Lead generation for brand outreach | API key |
| Instantly.ai | Cold email campaign management | API key |

---

## Core Workflows

### 1. Inbound Email Triage (Daily)
**Trigger:** Morning heartbeat / email check
**Steps:**
1. Check agency inbox for new emails
2. Classify by type: casting inquiry, model application, admin, spam
3. For castings → post to #ai-client-inquiry Slack channel with full details + ask booker to confirm models to submit
4. For model applications → check if Jace drafted a response; post to #ai-model-applications with context + ask booker for decision
5. For follow-ups awaiting action (contracts, replies) → flag urgency, escalate to booker
6. Archive/ignore: Facebook notifications, promotional emails

**Jace.ai role:** Handles auto-classification and drafts standard replies (digitals request, Zoom invite). Agent reviews for accuracy and handles exceptions.

**Key rule:** Never send an email without human approval.

---

### 2. Casting Submission Workflow
**Trigger:** New casting inquiry received
**Steps:**
1. Parse casting details: brand, location, dates, pay, model requirements (gender, age, height, size, hair type)
2. Cross-reference talent roster for matching models
3. Post to #ai-client-inquiry with:
   - Full casting brief
   - Suggested matching models (with notes on why they fit)
   - Submission deadline
   - Ask booker to confirm models + provide package links
4. Once confirmed → draft submission email to casting director
5. Booker approves → send
6. Log submission in tracking sheet

**Submission format:** Photo package links + model type indicators per casting spec

---

### 3. Model Application Workflow
**Trigger:** New Squarespace form submission or direct email application
**Steps:**
1. Jace auto-classifies and drafts digitals request
2. Agent reviews draft for accuracy
3. Post to #ai-model-applications with:
   - Applicant name, basic stats (age, height, measurements, location)
   - Instagram handle
   - Experience level
   - Whether Jace's draft applies
4. Booker decides: send digitals request / schedule interview / decline
5. Agent executes decision
6. If interview scheduled → Jace sends Zoom invite template
7. Post-interview → booker decides: contract / more info needed / decline
8. If contract → send representation agreement via SignWell (or equivalent)

---

### 4. Contract Sending Workflow
**Trigger:** Booker approves model for representation
**Steps:**
1. Confirm model type: exclusive vs non-exclusive
2. Pull appropriate contract template
3. Pre-fill model details (name, email, date)
4. Send via e-signature platform (SignWell)
5. CC agency email
6. Log in model's record
7. Follow up if not signed within 5 business days

---

### 5. Brand Outreach Campaign Workflow
**Trigger:** Scheduled (weekly/monthly) or on-demand
**Steps:**
1. Apollo list building: target industry, job titles, location, company size
2. Export + enrich contacts
3. Build Instantly campaign with personalized templates
4. Launch at 25-50 emails/day
5. Monitor open/reply rates
6. Route replies to booker via Slack
7. Track bookings that originate from outreach

**Campaign types:**
- Fresh Faces (new brands, never worked together)
- Success Stories (similar to past clients)
- Seasonal Push (upcoming shoot seasons)

---

### 6. Model Recruitment Pipeline
**Channels:**
1. Social media scouting (Instagram/TikTok scraping)
2. University outreach (fashion schools)
3. Event-based recruitment (fashion weeks, trade shows)
4. Referral program (current model incentives)
5. Content marketing (blog/social to attract inbound applicants)
6. Casting platform monitoring (Model Mayhem, Backstage, etc.)

---

### 7. Weekly Email Automation Advisory
**Trigger:** Weekly review
**Steps:**
1. Review emails that fell outside Jace's templates
2. Identify patterns (3+ similar emails = automation candidate)
3. Recommend new Jace template/rule to booker
4. Document new automation added

---

## Slack Channel Structure (Standard)
| Channel | Purpose |
|---------|---------|
| #ai-assistance | General AI comms, onboarding |
| #ai-model-applications | New talent pipeline decisions |
| #ai-client-inquiry | Casting + client work |
| #ai-marketing | Outreach campaigns, recruitment strategy |

---

## Talent Roster Management
- Export from Portfolio Pad (or equivalent) as CSV monthly
- Store as structured JSON for AI querying
- Fields: name, active status, career type, gender, age, email, mobile, social handles
- Photos: store per-model in organized folder structure
- Social handles: collect separately (often not in CSV export)

---

## Key Metrics to Track (Future Dashboard)
- Models signed per month
- Castings received vs submitted vs booked
- Outreach email open/reply/booking rates
- Average response time to inquiries
- Revenue per booking (once billing integrated)

---

## Productization Notes (For Other Agencies)
**What's agency-agnostic (reusable as-is):**
- Email triage logic
- Casting submission workflow
- Model application workflow
- Brand outreach campaigns (Apollo + Instantly)
- Slack channel structure
- Jace.ai automation advisory

**What needs customization per agency:**
- Email credentials + OAuth
- Slack workspace tokens
- Jace.ai templates (tone, signature, specific scripts)
- Talent roster import format (varies by CRM)
- Contract templates
- Specific client relationships

**Pricing model idea:** Monthly SaaS fee per agency seat, tiered by roster size or email volume.

---

*Last updated: July 2, 2026*
*Built from: Kiss Model Management operations*
