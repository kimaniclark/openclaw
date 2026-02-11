# Model Routing Guidelines

## Philosophy
**Zero friction for the user.** They just send messages. Johnny handles model selection automatically.

## Default Models by Channel

| Channel | Default Model | Reason |
|---------|---------------|--------|
| Telegram (main) | Opus | Large context (100K+ tokens) |
| Discord (all channels) | Sonnet | Fresh context, balanced capability |

## Complexity-Based Routing

### When to Use Each Model

**Haiku (fastest, cheapest)** - DON'T spawn, overhead > savings
- Quick lookups
- Yes/no questions
- Simple confirmations
- Basic math
- *Skip spawning - Sonnet handles these fast enough*

**Sonnet (default for Discord)**
- Writing drafts
- Planning tasks
- Reasoning through problems
- Research summaries
- Most business questions
- *Handle directly in Discord sessions*

**Opus (spawn when needed)**
- Deep analysis
- Multi-step complex reasoning
- Strategy development
- Large document analysis
- Connecting patterns across many data points
- Complex financial analysis
- M&A deal evaluation
- *Spawn from Discord when detected*

## Spawn Triggers

**Spawn Opus from Sonnet when:**
1. Task requires analyzing multiple documents/contexts
2. Deep strategic thinking needed
3. Complex multi-step reasoning
4. User explicitly asks for thorough/deep analysis
5. Task involves synthesizing information across businesses
6. Financial modeling or complex calculations
7. Legal/contract analysis

**Keywords/phrases that suggest Opus:**
- "analyze in depth"
- "comprehensive review"
- "strategic plan"
- "evaluate all options"
- "deep dive"
- "thorough analysis"
- "compare across"
- "what are all the implications"

## Implementation

### Discord Sessions (Sonnet default)
```
User message arrives
  ↓
Evaluate complexity
  ↓
Simple/Medium? → Answer directly (Sonnet)
Complex? → Spawn Opus sub-agent → Return answer
```

### Telegram Session (Opus default)
```
User message arrives
  ↓
Answer directly (Opus handles everything)
```

## Spawn Command Pattern

When spawning Opus for complex tasks:
```
sessions_spawn(
  task: "[restate the user's complex question]",
  model: "anthropic/claude-opus-4-5",
  label: "opus-analysis"
)
```

## Cost Implications

| Model | Input (per 1M) | Output (per 1M) | Relative |
|-------|----------------|-----------------|----------|
| Haiku | $0.25 | $1.25 | 1x |
| Sonnet | $3 | $15 | 12x |
| Opus | $15 | $75 | 60x |

**Strategy:** Use Sonnet for 80% of tasks, Opus for 20% complex tasks.
**Savings:** ~40-50% vs using Opus for everything.

## User Experience

**What the user sees:**
- Messages just work
- No model selection needed
- Complex tasks might take slightly longer (spawn overhead)
- Quality matches task complexity

**What happens behind the scenes:**
- Johnny evaluates each message
- Routes to appropriate model
- Spawns Opus when complexity warrants it
- Returns unified response

---

**Last Updated:** Feb 11, 2026
**Status:** Active
