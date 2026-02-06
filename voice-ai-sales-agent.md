# Voice AI Sales Agent - Project Plan

**Purpose**: Automated voice agent for lead qualification and appointment booking  
**Primary Use Cases**: The Modern Owner (ad submissions) & Crown Acquisitions (M&A leads)  
**Status**: Planning phase - awaiting call script  
**Created**: 2026-02-05

---

## Business Context

### The Modern Owner
- **Website**: modernowner.co
- **Type**: Small business course (recently launched 2026)
- **Lead Source**: Facebook ads (via Keaton Nelson)
- **Need**: Qualify leads from ad submissions and book discovery calls
- **Current Flow**: Lead fills form → Manual follow-up needed
- **Target Flow**: Lead fills form → AI calls within 60 seconds → Qualified → Booked on calendar

### Crown Acquisitions
- **Type**: M&A (Mergers & Acquisitions) business
- **Need**: Qualify business owners interested in selling, book consultation calls
- **Details**: TBD (user will provide voice description)

---

## What We're Building

**Atlas.com-style AI voice agent** that:
1. ✅ Receives inbound calls (24/7 AI receptionist)
2. ✅ Makes outbound calls within 60 seconds of lead opt-in
3. ✅ Follows custom script for qualification
4. ✅ Books appointments on Motion calendar
5. ✅ Confirms appointments 24-48h before (reduces no-shows)
6. ✅ Handles objections and questions
7. ✅ Integrates with CRM (Go High Level)
8. ✅ Re-engages "dead" leads

---

## Technical Architecture

### Infrastructure (Already Have)
- **Twilio Voice**: +1 202-998-6450 (can make & receive calls)
- **OpenAI API**: Whisper (transcription) + GPT (conversation)
- **Motion API**: Calendar booking and auto-scheduling
- **Go High Level API** (coming): CRM integration for 2 instances

### System Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    INBOUND CALLS                             │
└─────────────────────────────────────────────────────────────┘
    Lead dials → Twilio answers → AI conversation
                      ↓
              OpenAI processes speech
                      ↓
            Qualification questions
                      ↓
         Qualified? → Book in Motion
                      ↓
         Send confirmation + update CRM

┌─────────────────────────────────────────────────────────────┐
│                   OUTBOUND CALLS                             │
└─────────────────────────────────────────────────────────────┘
    Lead fills form → Webhook fires
                      ↓
              Wait 60 seconds
                      ↓
         Twilio initiates call
                      ↓
            AI conversation (script)
                      ↓
         Qualified? → Book in Motion
                      ↓
         Update CRM status

┌─────────────────────────────────────────────────────────────┐
│              APPOINTMENT CONFIRMATION                        │
└─────────────────────────────────────────────────────────────┘
    Cron job checks Motion calendar
                      ↓
    24-48h before appointment?
                      ↓
         Call to confirm
                      ↓
    Update calendar if cancel/reschedule
```

---

## Development Phases

### Phase 1: Inbound Calls (1-2 weeks)
**Goal**: AI answers calls and has basic conversation

**Components to Build**:
- [x] Twilio voice webhook endpoint
- [ ] OpenAI integration (Whisper + GPT)
- [ ] Conversation state management
- [ ] Basic script/prompt system
- [ ] Call recording and logging
- [ ] Test with real calls

**Deliverable**: Working AI that can answer calls and hold basic conversation

---

### Phase 2: Outbound + Booking (2-3 weeks)
**Goal**: AI makes outbound calls and books qualified leads

**Components to Build**:
- [ ] Webhook listener for form submissions
- [ ] Outbound call trigger system
- [ ] Lead context injection (pass form data to AI)
- [ ] Qualification logic (decision tree)
- [ ] Motion calendar booking integration
- [ ] Confirmation email/SMS system
- [ ] CRM status updates (Go High Level)

**Deliverable**: End-to-end automation from form fill to booked appointment

---

### Phase 3: Full Automation (4-6 weeks)
**Goal**: Complete system with confirmations and lead revival

**Components to Build**:
- [ ] Appointment confirmation system (cron-based)
- [ ] No-show prevention logic
- [ ] "Dead" lead revival campaigns
- [ ] Objection handling refinements
- [ ] Multi-business routing (Modern Owner vs Crown)
- [ ] Analytics dashboard (calls, conversions, bookings)
- [ ] A/B testing for scripts

**Deliverable**: Fully autonomous sales agent system

---

## Script Requirements

**Waiting on**: User to share call script(s)

**What we need**:
1. **Opening**: How AI introduces itself
2. **Qualification questions**: What to ask to determine fit
3. **Objection handling**: Common pushback and responses
4. **Disqualification criteria**: When to politely end call
5. **Booking logic**: When qualified, how to offer times
6. **Closing**: Confirmation and next steps

**Example Structure**:
```
INTRO:
"Hi [Name], this is Emma calling from The Modern Owner. 
I see you just filled out our form about [topic]. 
Is now a good time for a quick 2-minute conversation?"

QUALIFICATION:
Q1: "What made you interested in [course/service]?"
Q2: "Tell me about your current business situation..."
Q3: "What's your timeline for [solving problem]?"

OBJECTION - Price:
"I understand. Many of our clients felt that way initially. 
What they found was [value statement]..."

BOOKING:
"Based on what you've shared, I think [founder] could really 
help you with [specific pain point]. I have availability 
Tuesday at 2pm or Thursday at 11am - which works better?"
```

---

## Technical Implementation Details

### Twilio → OpenAI Integration

**Flow**:
1. Twilio receives call → webhook to OpenClaw
2. Stream audio to OpenAI Whisper (real-time transcription)
3. Pass transcript + context to GPT-4 (conversation logic)
4. GPT generates response text
5. Convert to speech (OpenAI TTS or ElevenLabs)
6. Stream audio back to Twilio → caller hears response

**Key Libraries**:
- Twilio Node SDK (voice)
- OpenAI Node SDK (Whisper + GPT + TTS)
- WebSocket for audio streaming

### Conversation State Management

**Store in memory**:
- Call SID (Twilio identifier)
- Lead info (name, email, source)
- Conversation history (transcript)
- Qualification status (not qualified / qualified / booked)
- Next action (continue / book / disqualify)

**Persist to database** (for analytics):
- All call recordings
- Full transcripts
- Qualification outcomes
- Booking results

### Calendar Booking Logic

**When AI determines "qualified"**:
1. Query Motion API for available times
2. Present 2-3 options to lead
3. Lead selects time
4. Create Motion task with autoScheduled
5. Send confirmation email (via Gmail API)
6. Update CRM status (Go High Level)

### Webhook Configuration

**Modern Owner Form**:
```
Form submission → Go High Level webhook
    ↓
POST to OpenClaw endpoint: /webhooks/modern-owner/lead
    ↓
Extract: name, email, phone, source, answers
    ↓
Wait 60 seconds (optional delay)
    ↓
Initiate Twilio call to lead's phone
```

**Crown Acquisitions Form**:
```
Similar flow, different script/qualification criteria
```

---

## Script Customization Per Business

### The Modern Owner
- **Tone**: Educational, helpful, entrepreneurial
- **Goal**: Book discovery call with Kimani
- **Qualification**: Business owner, revenue level, growth goals
- **Disqualify**: No business yet, wrong industry fit, price shopper

### Crown Acquisitions
- **Tone**: Professional, confidential, strategic
- **Goal**: Book M&A consultation
- **Qualification**: Business owner looking to sell, revenue range, timeline
- **Disqualify**: Tire kickers, not decision maker, too small

---

## Cost Estimation

### Per Call Costs
- **Twilio Voice**: $0.0130/min inbound, $0.0140/min outbound (US)
- **OpenAI Whisper**: $0.006/min transcription
- **OpenAI GPT-4**: ~$0.03/call (conversation)
- **OpenAI TTS**: $0.015/1K characters (~$0.05/call)
- **Total per call**: ~$0.20-0.30 for 5-minute call

### Volume Pricing (100 calls/month)
- **Twilio**: ~$7/month
- **OpenAI**: ~$15/month
- **Total**: ~$25/month for 100 calls
- **Compare to**: Atlas.com likely charges $300-500/month

### ROI Calculation
- Cost per booked call: ~$1-2 (assuming 20-30% booking rate)
- Value of booked call: $500-5,000+ (course sale or M&A deal)
- ROI: 250x - 5,000x

---

## Success Metrics

### Key Performance Indicators (KPIs)
- **Call Answer Rate**: % of outbound calls that connect
- **Conversation Completion**: % who stay on entire call
- **Qualification Rate**: % determined as good fit
- **Booking Rate**: % of qualified leads who book
- **Show Rate**: % of booked appointments who attend
- **Conversion Rate**: % who ultimately buy

### Target Benchmarks (Based on Atlas.com)
- Answer Rate: 75-85%
- Qualification Rate: 30-50%
- Booking Rate: 40-60%
- Show Rate: 70-80%
- Overall Lead → Booked: 15-25%

### A/B Testing Ideas
- Different opening lines
- Question order variations
- Objection handling approaches
- Booking time presentation (2 vs 3 options)
- Follow-up timing (60 sec vs 2 min vs 5 min)

---

## Integration Points

### Go High Level (CRM)
- **Read**: Lead data (name, email, phone, source, tags)
- **Write**: Call outcome, qualification status, booking link
- **Update**: Lead stage in pipeline
- **Trigger**: New form submission → webhook → call

### Motion (Calendar)
- **Read**: Available time slots
- **Write**: Create new appointment
- **Update**: Confirmation status
- **Delete**: Cancel if no-show or rescheduled

### Gmail (Communication)
- **Send**: Booking confirmation emails
- **Send**: Appointment reminders
- **Send**: Post-call follow-up

---

## Risk Mitigation

### Potential Issues
1. **AI sounds robotic** → Use ElevenLabs for more natural TTS
2. **Misunderstands questions** → Tune prompts, add fallback responses
3. **Doesn't handle objections** → Build comprehensive objection library
4. **Books wrong times** → Add double-confirmation step
5. **Privacy concerns** → Disclose AI at call start, record consent

### Legal Compliance
- **Recording consent**: "This call may be recorded..." (check state laws)
- **AI disclosure**: "You're speaking with an AI assistant..." (optional but recommended)
- **Do Not Call (DNC)**: Only call leads who opted in
- **TCPA compliance**: Get written consent for automated calls

---

## Next Actions

### Immediate (This Week)
- [x] Research Atlas.com functionality ✅
- [x] Document technical architecture ✅
- [ ] **Get call script from user** ⏳
- [ ] Create proof-of-concept plan
- [ ] Set up development environment

### Short-term (Next 2 Weeks)
- [ ] Build Phase 1: Inbound call handler
- [ ] Test with real calls
- [ ] Refine conversation logic
- [ ] Document findings

### Medium-term (Weeks 3-6)
- [ ] Build Phase 2: Outbound + booking
- [ ] Integrate with Modern Owner form
- [ ] Get Crown Acquisitions details
- [ ] Test end-to-end flow
- [ ] Launch pilot with 10-20 leads

### Long-term (Months 2-3)
- [ ] Build Phase 3: Full automation
- [ ] Add appointment confirmations
- [ ] Implement dead lead revival
- [ ] Scale to 100+ calls/month
- [ ] Build analytics dashboard

---

## Questions for User

1. **Call script**: Can you share the script(s) you mentioned?
2. **Crown Acquisitions**: Can you describe this business by voice now that transcription works?
3. **Priority**: Modern Owner or Crown Acquisitions first?
4. **Timeline**: When do you need this operational?
5. **Volume**: How many leads/month are you expecting per business?
6. **Calendar**: Use Motion for bookings, or different system?
7. **Phone number**: Use +1 202-998-6450, or get dedicated numbers per business?

---

## Reference Materials

### Competitor Analysis
- **Atlas.com**: $300-500/month for AI sales agents
- **Features**: Inbound/outbound, qualification, booking, confirmations
- **USP**: "Plug in these ruthless AI Sales Agents... doubling, tripling, even quadrupling your call bookings"
- **Target**: Service businesses (HVAC, plumbing, dental, legal, etc.)

### Similar Tools
- **Conversica**: AI sales assistant (email + chat focused)
- **Drift**: Conversational marketing (chat bot)
- **Outreach.io**: Sales engagement (email/call sequences)
- **Close.com**: CRM with built-in calling

**Our Advantage**: 
- Custom-built for your exact businesses
- Full control over scripts and logic
- 90% cheaper than Atlas.com
- Integrated with your existing tools (Motion, CRM, Gmail)

---

*Last updated: 2026-02-05*
*Status: Awaiting call script to begin development*
