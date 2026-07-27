# Kiss Models — Casting Workflow

## Current Process

### Step 1: Casting Inquiry Arrives
- Casting director emails info@kissmodelmanagement.com
- I parse the email and post a structured summary to Slack (#ai-client-inquiry)

### Step 2: Pricing
- I calculate the model rate from what the client offers using 20% + 20% model:
  - **Client says "$X + 20%":** Model gross = $X. Template shows `$X - 20% agency fee`
  - **Client says "$X flat":** Model gross = $X ÷ 1.20. Template shows `$[calculated] - 20% agency fee`
- If the math lands on an odd number, suggest rounding options to Victoria (e.g., "$833 → round to $825 or $850?")
- Victoria confirms the final rate

### Step 3: Create Casting
- I format the casting details into copy/paste-ready text using the template below
- Victoria pastes it into Portfolio Pad, selects models, and sends
- *Future:* I suggest specific models based on requirements + model database/Dropbox photos

### Step 4: Model Notification
- *Now:* Portfolio Pad emails models with accept/decline
- *Future:* I email models directly. Text non-responders as follow-up (no need to text those who responded by email)

### Step 5: Collect Responses
- Models accept, decline, or ask questions
- I track status and give Victoria a running tally
- Handle any questions/conditions from models

### Step 6: Package Creation
- Compile accepted models into a branded submission package
- *Now:* Building test versions alongside Portfolio Pad for comparison
- *Future:* Fully replace Portfolio Pad packages

### Step 7: Submit to Client
- Victoria sends package to casting director
- *Future:* I send directly (with Victoria's approval)

---

## Casting Template (for Portfolio Pad copy/paste)

```
Company: [Client/Brand Name]

[Job Description]

Date: [Day, Month Date, Year]
Location: [City, State]
Rate: $[amount] - 20% agency fee
Usage: [Usage rights]
Schedule: [Schedule details]

Submission Deadline: [Deadline]
```

### Example (Kevin Murphy — $1,000 flat from client):

```
Company: Kevin Murphy

Behind The Chair — Hair Show

Date: Friday-Saturday, August 22-23, 2026
Location: Fort Lauderdale, FL
Rate: $833 - 20% agency fee
Usage: Event/show only
Schedule: TBD (2-day event)

Submission Deadline: Submit ASAP!
```

---

## Commission Structure (20% + 20%)

- Client pays 20% agency fee on top of model fee (or it's baked into a flat rate)
- Model pays 20% commission from their gross fee
- Agency total revenue = both 20% portions
- Flat 20% across all jobs (Victoria's decision, July 2026)

### Calculation Examples

**Client says "$1,000 + 20%":**
- Client pays: $1,200
- Model gross: $1,000
- Model commission (20%): $200
- Model nets: $800
- Agency revenue: $400

**Client says "$1,000 flat":**
- Client pays: $1,000
- Model gross: $833.33 ($1,000 ÷ 1.20)
- Client agency fee (baked in): $166.67
- Model commission (20%): $166.67
- Model nets: $666.67
- Agency revenue: $333.33

---

## Standing Directive

When Victoria does any task not yet defined in a workflow:
1. Ask if I can help make it a repeatable process
2. Build the process with her
3. Create templates
4. Get them approved
5. Test with her

---

## Model Database Build-Out

### Channel: #ai-model-database (C0BJAC5CWR5)

### Process
- Every Tuesday (or when Victoria finishes the current batch), I send Victoria 10 model names to provide details on
- Victoria shares what she knows about each model (stats, personality, look, strengths, availability notes)
- Victoria can also tell me which models to remove from the roster
- Data sources: Victoria's knowledge, Portfolio Pad export, email scans, Dropbox photos (future)
- Victoria can send voice messages — I'll transcribe and extract the details

### Data to Capture Per Model
- Full name
- Height, measurements (waist, hips, bust/chest), shoe size
- Hair color/type/length
- Eye color
- Age / date of birth
- Ethnicity / look
- Experience level
- Location / willingness to travel
- Contact info (email, phone)
- Portfolio photos (future — Dropbox)
- Victoria's notes (personality, reliability, strengths, special skills)

---

## AI Replacement Roadmap

### Phase 1 (Now): Process Assistant
- Parse incoming casting emails → structured Slack summary
- Calculate pricing and format casting template for Portfolio Pad
- Track accept/decline responses
- Build test packages alongside Portfolio Pad

### Phase 2 (Near-term): Model Database + Suggestions
- Build model stats database (height, measurements, hair, photos)
- Source from: Portfolio Pad export, email scans, Dropbox photos
- Start suggesting models for castings based on requirements

### Phase 3 (Future): Full Portfolio Pad Replacement
- Email models directly with casting details + accept/decline
- Text follow-up for non-responders
- Auto-generate branded submission packages
- Send packages to casting directors
- Handle commission calculations and pricing
