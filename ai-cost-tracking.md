# AI Cost Tracking for Life Concierge

**Purpose**: Monitor AI costs per client to understand profitability and optimize usage  
**Created**: 2026-02-05

---

## Why This Matters

**Scenario**: You charge $600/month for Life Concierge
- If AI costs = $50/client/month → Profit: $550 ✅
- If AI costs = $300/client/month → Profit: $300 ⚠️
- If AI costs = $700/client/month → Losing money ❌

**You need to know**:
1. Which clients are expensive vs cheap to serve
2. What features drive the most cost
3. Whether pricing is sustainable
4. How to optimize without reducing quality

---

## OpenAI Cost Structure

### Token-Based Pricing

**GPT-4 (Current pricing as of 2026)**:
- Input tokens: $0.01 per 1K tokens
- Output tokens: $0.03 per 1K tokens
- 1 token ≈ 4 characters or ¾ of a word
- Average conversation: 500-2000 tokens

**Whisper (Voice transcription)**:
- $0.006 per minute of audio

**TTS (Text-to-Speech)**:
- $0.015 per 1K characters (~150 words)

**Embeddings** (for memory search):
- text-embedding-3-small: $0.00002 per 1K tokens
- text-embedding-3-large: $0.00013 per 1K tokens

### Example Cost Breakdown

**Light user** (10 messages/day):
- 10 messages × 500 tokens avg × 30 days = 150K tokens
- Input: 75K × $0.01/1K = $0.75
- Output: 75K × $0.03/1K = $2.25
- Memory searches: 10 × 30 × ~$0.001 = $0.30
- **Total: ~$3.30/month**

**Medium user** (30 messages/day):
- 30 messages × 500 tokens × 30 days = 450K tokens
- Input: 225K × $0.01/1K = $2.25
- Output: 225K × $0.03/1K = $6.75
- Memory searches: 30 × 30 × ~$0.001 = $0.90
- **Total: ~$9.90/month**

**Heavy user** (100 messages/day):
- 100 messages × 500 tokens × 30 days = 1.5M tokens
- Input: 750K × $0.01/1K = $7.50
- Output: 750K × $0.03/1K = $22.50
- Memory searches: 100 × 30 × ~$0.001 = $3.00
- Voice: 10 min/day × 30 days × $0.006 = $1.80
- **Total: ~$34.80/month**

**Power user** (voice-heavy, 200+ messages/day):
- Text: ~$70/month
- Voice: 30 min/day × 30 × $0.006 = $5.40
- TTS responses: Varies
- **Total: ~$75-100/month**

---

## How to Track Costs Per Client

### Method 1: OpenAI Usage API (Recommended)

**OpenAI provides usage data**:
```bash
# Get usage for date range
curl https://api.openai.com/v1/usage \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "date=2026-02-01"
```

**Response includes**:
- Total tokens used
- Cost breakdown by model
- Requests per endpoint

**Limitation**: Not automatically tagged by client

### Method 2: Tag API Calls (Best Practice)

**Add client ID to every API call**:
```javascript
// When making OpenAI request
const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [...],
  user: "client_kimani_123"  // ← Client identifier
});
```

**Benefits**:
- OpenAI tracks usage per `user` field
- Can query usage by client ID
- Export and analyze per-client costs

**Implementation for Life Concierge**:
```javascript
// Generate unique client ID
const clientId = `lc_${client.name}_${client.id}`;

// Every API call includes this
user: clientId
```

### Method 3: Local Logging (Full Control)

**Log every API call**:
```javascript
async function callOpenAI(clientId, messages) {
  const startTime = Date.now();
  
  const response = await openai.chat.completions.create({
    model: "gpt-4",
    messages: messages,
    user: clientId
  });
  
  // Log usage
  await logUsage({
    clientId: clientId,
    timestamp: new Date(),
    model: "gpt-4",
    tokensInput: response.usage.prompt_tokens,
    tokensOutput: response.usage.completion_tokens,
    tokensTotal: response.usage.total_tokens,
    costInput: response.usage.prompt_tokens * 0.01 / 1000,
    costOutput: response.usage.completion_tokens * 0.03 / 1000,
    costTotal: (response.usage.prompt_tokens * 0.01 + 
                response.usage.completion_tokens * 0.03) / 1000,
    latency: Date.now() - startTime,
    requestType: "chat",
    conversationId: messages[0].conversation_id
  });
  
  return response;
}
```

**Database schema**:
```sql
CREATE TABLE api_usage (
  id SERIAL PRIMARY KEY,
  client_id VARCHAR(100),
  timestamp TIMESTAMP,
  model VARCHAR(50),
  tokens_input INTEGER,
  tokens_output INTEGER,
  tokens_total INTEGER,
  cost_input DECIMAL(10,6),
  cost_output DECIMAL(10,6),
  cost_total DECIMAL(10,6),
  latency_ms INTEGER,
  request_type VARCHAR(50),
  conversation_id VARCHAR(100)
);

-- Index for fast client queries
CREATE INDEX idx_client_costs ON api_usage(client_id, timestamp);
```

### Method 4: Proxy/Middleware Layer

**Route all API calls through tracking middleware**:
```javascript
class OpenAIProxy {
  constructor(apiKey, costTracker) {
    this.openai = new OpenAI({ apiKey });
    this.costTracker = costTracker;
  }
  
  async chat(clientId, messages, options = {}) {
    const start = Date.now();
    
    try {
      const response = await this.openai.chat.completions.create({
        ...options,
        messages,
        user: clientId
      });
      
      // Track successful request
      await this.costTracker.log({
        clientId,
        success: true,
        usage: response.usage,
        latency: Date.now() - start
      });
      
      return response;
    } catch (error) {
      // Track failed request (still costs money!)
      await this.costTracker.log({
        clientId,
        success: false,
        error: error.message
      });
      
      throw error;
    }
  }
  
  async transcribe(clientId, audioFile) {
    const duration = await getAudioDuration(audioFile);
    const cost = duration * 0.006 / 60; // $0.006 per minute
    
    const response = await this.openai.audio.transcriptions.create({
      file: audioFile,
      model: "whisper-1"
    });
    
    await this.costTracker.log({
      clientId,
      type: "transcription",
      duration,
      cost
    });
    
    return response;
  }
}
```

---

## Monitoring Dashboard

### Real-Time Cost Tracking

**What to display**:
```
┌─────────────────────────────────────────────────┐
│         Life Concierge - AI Costs               │
├─────────────────────────────────────────────────┤
│ Total Clients: 50                               │
│ Monthly AI Cost: $487.50                        │
│ Avg Cost/Client: $9.75                          │
│ Revenue: $30,000 (50 × $600)                   │
│ AI Cost %: 1.6%                                 │
│ Profit Margin: 98.4%                            │
└─────────────────────────────────────────────────┘

Top 5 Most Expensive Clients:
1. Erik Kimel      $45.20  (4.6x avg)  ⚠️
2. Kristin Jepsen  $28.30  (2.9x avg)
3. Client C        $15.80  (1.6x avg)
4. Client D        $12.40  (1.3x avg)
5. Client E        $10.90  (1.1x avg)

Bottom 5 Least Expensive:
1. Client F        $2.10   (0.2x avg)
2. Client G        $3.50   (0.4x avg)
3. Client H        $4.20   (0.4x avg)
4. Client I        $5.80   (0.6x avg)
5. Client J        $6.30   (0.6x avg)
```

### Per-Client Cost Report

**Monthly report for each client**:
```
Client: Erik Kimel
Billing Period: Feb 1-28, 2026

Usage Summary:
- Total messages: 890
- Voice messages: 45 (67 minutes)
- Average session: 12 messages
- Peak usage: Feb 15 (78 messages)

Cost Breakdown:
- GPT-4 conversations:  $35.20
- Whisper transcription: $6.70
- TTS responses:         $2.50
- Memory searches:       $0.80
- TOTAL:                $45.20

Compared to average: 4.6x higher
Status: Within acceptable range ✅
```

### Trend Analysis

**Track over time**:
```javascript
{
  clientId: "erik_kimel",
  costHistory: {
    "2026-01": "$42.10",
    "2026-02": "$45.20",
    "2026-03": "$38.90"
  },
  trend: "stable",
  avgMonthly: "$42.07",
  projectedAnnual: "$504.84"
}
```

---

## Cost Optimization Strategies

### 1. Use Cheaper Models When Possible

**GPT-4 vs GPT-3.5-turbo**:
- GPT-4: $0.01 input / $0.03 output per 1K tokens
- GPT-3.5-turbo: $0.0005 input / $0.0015 output per 1K tokens
- **GPT-3.5 is 20x cheaper!**

**Strategy**: Use GPT-3.5 for simple tasks, GPT-4 for complex reasoning

```javascript
function selectModel(taskComplexity) {
  if (taskComplexity === "simple") {
    return "gpt-3.5-turbo"; // Email drafts, simple questions
  } else if (taskComplexity === "complex") {
    return "gpt-4"; // Strategic planning, nuanced coaching
  }
}
```

### 2. Implement Caching

**Cache common responses**:
```javascript
const responseCache = new Map();

async function getChatResponse(clientId, question) {
  const cacheKey = `${clientId}_${hash(question)}`;
  
  // Check cache first
  if (responseCache.has(cacheKey)) {
    return responseCache.get(cacheKey); // $0 cost!
  }
  
  // Not cached, call API
  const response = await callOpenAI(clientId, question);
  
  // Cache for 1 hour
  responseCache.set(cacheKey, response);
  setTimeout(() => responseCache.delete(cacheKey), 3600000);
  
  return response;
}
```

### 3. Limit Context Window

**More context = more tokens = higher cost**:

```javascript
// ❌ Expensive: Send entire conversation history
messages = [
  ...last500Messages,  // 50K tokens!
  newMessage
];

// ✅ Cheaper: Send summary + recent messages
messages = [
  systemMessage,
  conversationSummary,  // 1K tokens
  ...last10Messages,    // 5K tokens
  newMessage
];
```

### 4. Batch Requests

**Multiple small requests = overhead**:
```javascript
// ❌ Expensive: 10 separate API calls
for (const task of tasks) {
  await processTask(task);
}

// ✅ Cheaper: 1 API call with 10 tasks
const batchResults = await processBatch(tasks);
```

### 5. Set Usage Limits

**Per-client caps**:
```javascript
const CLIENT_LIMITS = {
  messagesPerDay: 100,
  tokensPerMonth: 500000,
  costPerMonth: 50.00  // $50 max
};

async function checkLimit(clientId, requestTokens) {
  const usage = await getClientUsage(clientId);
  
  if (usage.monthlyTokens + requestTokens > CLIENT_LIMITS.tokensPerMonth) {
    throw new Error("Monthly token limit reached");
  }
  
  if (usage.monthlyCost > CLIENT_LIMITS.costPerMonth) {
    throw new Error("Monthly cost limit reached");
  }
  
  // Proceed with request
}
```

### 6. Prompt Engineering

**Shorter prompts = lower cost**:

```javascript
// ❌ Expensive prompt (verbose)
const prompt = `
You are a helpful AI assistant for Life Concierge clients. 
Your role is to help them manage their entire life across 
20+ different areas including travel, health, fitness, home, 
fashion, entertainment, and more. You should be friendly, 
professional, and proactive. Always consider the client's 
context and remember previous conversations...
[500 more words]
`;

// ✅ Cheaper prompt (concise)
const prompt = `
Life Concierge AI. Help client with travel, health, fitness, 
home, fashion, entertainment. Be friendly & proactive. Use context.
`;
```

---

## Alerting System

### Cost Alerts

**Set up notifications**:
```javascript
async function checkCostAlerts(clientId) {
  const dailyCost = await getClientCost(clientId, "today");
  const monthlyCost = await getClientCost(clientId, "month");
  
  // Daily limit
  if (dailyCost > 5.00) {
    await notify({
      channel: "telegram",
      to: "kimani",
      message: `⚠️ Client ${clientId} has spent $${dailyCost} today (limit: $5)`
    });
  }
  
  // Monthly limit
  if (monthlyCost > 50.00) {
    await notify({
      channel: "telegram",
      to: "kimani",
      message: `🚨 Client ${clientId} has spent $${monthlyCost} this month (limit: $50)`
    });
  }
  
  // Unusual spike
  const avgDailyCost = monthlyCost / new Date().getDate();
  if (dailyCost > avgDailyCost * 3) {
    await notify({
      channel: "telegram",
      to: "kimani",
      message: `📈 Client ${clientId} daily cost is 3x above average`
    });
  }
}
```

### Budget Forecasting

**Predict monthly costs**:
```javascript
function forecastMonthlyCost(clientId) {
  const daysElapsed = new Date().getDate();
  const daysInMonth = 30;
  const costToDate = getClientCost(clientId, "month");
  
  const projectedCost = (costToDate / daysElapsed) * daysInMonth;
  
  return {
    currentCost: costToDate,
    projectedCost: projectedCost,
    onTrack: projectedCost < 50.00
  };
}
```

---

## Pricing Strategy Based on Costs

### Cost-Plus Pricing

**Determine pricing based on actual costs**:

```
Average AI cost per client: $10/month

Pricing options:

1. Basic: $600/month
   - AI cost: $10 (1.7%)
   - Other costs: ~$50 (8.3%)
   - Profit: $540 (90%)
   
2. Cost cap pricing:
   - Price: $600/month
   - If AI > $100/month → Move to higher tier or optimize
   
3. Usage-based pricing:
   - Base: $500/month (includes $50 of AI)
   - Overage: $1 per $1 of AI costs above $50
   - Heavy user example: $500 + $30 overage = $530/month
```

### Tiered Pricing by Usage

**Life Concierge tiers**:

**Starter** - $300/month
- 50 messages/month
- $25 AI budget
- Basic features

**Professional** - $600/month (CURRENT)
- Unlimited messages
- $100 AI budget
- All features

**VIP** - $1,200/month
- Unlimited everything
- No AI budget cap
- Priority support
- Weekly strategy calls

---

## Expected Life Concierge Costs

### Realistic Projections

**Typical client** (medium usage):
- 30 messages/day
- 10% voice messages
- Memory searches
- **Cost: $9-12/month**

**Heavy user client**:
- 100 messages/day
- 30% voice messages
- Frequent searches
- **Cost: $35-50/month**

**Worst case "power user"**:
- 200+ messages/day
- Heavy voice usage
- **Cost: $75-100/month**

### Profitability Analysis

**At $600/month pricing**:
- Typical client: $600 - $10 = $590 profit (98.3% margin)
- Heavy user: $600 - $45 = $555 profit (92.5% margin)
- Power user: $600 - $100 = $500 profit (83.3% margin)

**At 50 clients** (mix):
- 40 typical clients: 40 × $10 = $400
- 8 heavy users: 8 × $45 = $360
- 2 power users: 2 × $100 = $200
- **Total AI costs: $960/month**
- **Total revenue: $30,000/month**
- **AI cost: 3.2% of revenue**
- **This is extremely healthy!**

---

## Implementation Plan

### Phase 1: Basic Tracking (Week 1)
- [x] Add `user` field to all OpenAI calls
- [ ] Log all API calls to database
- [ ] Create basic cost calculation script
- [ ] Daily cost summary email

### Phase 2: Dashboard (Week 2)
- [ ] Build cost monitoring dashboard
- [ ] Per-client cost reports
- [ ] Alert system for high usage
- [ ] Export to CSV for analysis

### Phase 3: Optimization (Week 3-4)
- [ ] Implement model selection logic
- [ ] Add response caching
- [ ] Optimize prompts
- [ ] Test usage limits

### Phase 4: Analytics (Ongoing)
- [ ] Trend analysis
- [ ] Cost forecasting
- [ ] Optimization recommendations
- [ ] ROI reporting

---

## Tools & Resources

### Cost Tracking Tools

**1. OpenAI Dashboard**
- https://platform.openai.com/usage
- View total usage
- Export to CSV
- Set spending limits

**2. Helicone (Third-party)**
- https://helicone.ai
- OpenAI proxy with analytics
- Cost tracking per user
- Free tier available

**3. Custom Dashboard**
- Build your own (recommended for Life Concierge)
- Full control
- Custom metrics
- Real-time alerts

### Monitoring Scripts

**Daily cost summary**:
```bash
#!/bin/bash
# Run daily at 9 AM
node scripts/cost-report.js --date yesterday --email kimani@kimaniclark.com
```

**Weekly report**:
```bash
#!/bin/bash
# Run every Monday
node scripts/cost-report.js --range week --format detailed
```

---

## Questions for Consideration

1. **Pricing**: Is $600/month sustainable if a client uses $100/month in AI?
2. **Limits**: Should there be usage caps per client?
3. **Tiers**: Should heavy users pay more?
4. **Optimization**: Is it worth saving $5/client with cheaper models?
5. **Transparency**: Should clients see their AI usage?

---

## Summary

**✅ Yes, you can absolutely track AI costs per client!**

**Recommended approach**:
1. Add `user: clientId` to every OpenAI API call
2. Log usage data to database
3. Build simple dashboard showing cost per client
4. Set alerts for high usage clients
5. Optimize prompts and model selection

**Expected costs**:
- Typical client: $10-15/month
- Heavy user: $30-50/month
- Power user: $75-100/month

**At $600/month pricing, these are extremely healthy margins** (90%+ profit even for heavy users).

**Start simple**: Just log the data. You can build fancy dashboards later once you see patterns.

---

*Last updated: 2026-02-05*
*Status: Ready to implement cost tracking*

---

## Usage-Based Tiered Pricing (Added Feb 5, 2026)

### User Feedback
"We could charge higher use clients more money too. Yes let's build the tracking system. I'll be curious to know what people are using"

### Proposed Tiered Structure

**Base** - $600/month
- Includes: $50 of AI usage (~500 messages)
- Best for: Typical clients, moderate usage
- Overage: $1.50 per $1 of AI costs above $50

**Professional** - $900/month
- Includes: $100 of AI usage (~1,000 messages)
- Best for: Heavy users, daily engagement
- Overage: $1.25 per $1 of AI costs above $100

**VIP** - $1,200/month
- Unlimited AI usage (no overage charges)
- Best for: Power users, voice-heavy, constant engagement
- Includes: Priority support, weekly strategy calls

### Real-World Examples

**Client A - Light User**:
- Usage: $12/month AI
- Tier: Base ($600/month)
- Overage: $0 (under $50 cap)
- **Total: $600/month**

**Client B - Medium User**:
- Usage: $35/month AI
- Tier: Base ($600/month)
- Overage: $0 (under $50 cap)
- **Total: $600/month**

**Client C - Heavy User**:
- Usage: $80/month AI
- Tier: Base ($600/month)
- Overage: ($80 - $50) × $1.50 = $45
- **Total: $645/month** OR upgrade to Professional

**Client D - Power User**:
- Usage: $150/month AI
- Tier: Professional ($900/month)
- Overage: ($150 - $100) × $1.25 = $62.50
- **Total: $962.50/month** OR upgrade to VIP

**Client E - Super User**:
- Usage: $250/month AI
- Tier: VIP ($1,200/month)
- Overage: $0 (unlimited)
- **Total: $1,200/month** (saves $150+ on overages)

### When to Upgrade Clients

**Automatic upgrade suggestions**:
```
If 2 months in a row AI usage > tier cap:
  → Send upgrade recommendation

Example:
"Hi Erik, I noticed you're using Life Concierge heavily 
(which is great!). Over the last 2 months, you've averaged 
$85/month in AI usage, which puts you over the Base tier cap.

I recommend upgrading to Professional ($900/month) which 
includes $100 of AI usage. This would save you money and 
give you room to grow.

Want to discuss?"
```

### Revenue Impact

**50 Clients Mixed Tiers**:

**Base tier** (30 clients at $600):
- 25 clients: $12 avg = no overage
- 5 clients: $65 avg = $75 total overage
- Revenue: (30 × $600) + $75 = **$18,075/month**

**Professional tier** (15 clients at $900):
- 12 clients: $75 avg = no overage
- 3 clients: $120 avg = $75 total overage
- Revenue: (15 × $900) + $75 = **$13,575/month**

**VIP tier** (5 clients at $1,200):
- Unlimited usage
- Revenue: 5 × $1,200 = **$6,000/month**

**Total Monthly Revenue**: $18,075 + $13,575 + $6,000 = **$37,650**
**vs. Flat $600**: 50 × $600 = $30,000
**Increase**: $7,650/month = **$91,800/year extra!**

### Dashboard Requirements

**What you'll see**:
1. **Client Usage Overview**
   - Each client's monthly AI costs
   - Current tier
   - If they're over tier cap
   - Upgrade recommendation flag

2. **Usage Patterns**
   - What times they use it most
   - Voice vs text ratio
   - Feature usage breakdown
   - Session length

3. **Revenue Analysis**
   - Total AI costs vs revenue
   - Profit per client
   - Tier distribution
   - Overage revenue

4. **Alerts**
   - Client hitting 80% of tier cap
   - Client consistently over cap (upgrade candidate)
   - Unusual usage spikes
   - Total daily cost exceeding threshold

### Implementation Timeline

**Created**: Motion task "Build AI Cost Tracking System"
- **Duration**: 240 minutes (4 hours)
- **Start date**: Feb 10, 2026
- **Due date**: Feb 17, 2026
- **Workspace**: Executive Assistance
- **Priority**: MEDIUM

**What gets built**:
1. Client ID tagging on all API calls
2. Usage logging database
3. Cost calculation engine
4. Dashboard (simple first version)
5. Telegram alerts for high usage
6. Weekly cost summary reports

**You'll be able to see**:
- "Wow, Erik uses voice messages constantly - that's why his costs are high"
- "Kristin only uses it in the mornings for planning"
- "This client barely uses it - might churn"
- "These 5 clients should be on VIP tier"

---

*Status: Task created, ready to build after core features*
*User wants to: "Be curious to know what people are using"*
