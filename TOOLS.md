# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## 🔌 Available API Integrations

All credentials stored in `credentials.json`. These are ALREADY SET UP AND WORKING.

### Grain (Meeting Recordings & Transcripts) ✅
- **Workspace**: Kiklis and Clark (teams: Main, The Modern Owner, Life Concierge)
- **What I can do**:
  - List all recorded meetings
  - Pull full transcripts with speaker names + timestamps
  - Search meetings by title or participant
  - Get AI-generated summaries
  - Download recordings (video/audio)
- **Use cases**: Pull notes from past calls, find what was discussed in a specific meeting, summarize coaching sessions

### Gmail (Email Access) ✅
- **kimani@kimaniclark.com** — Personal email (primary inbox)
- **kimani@modernowner.co** — The Modern Owner business email
- **kimani@crownacquisitions.co** — Crown Acquisitions business email
- **kimani@kiklisclark.com** — Kiklis Clark law firm email ✅ NEW
- **assistant@kimaniclark.com** — Johnny's sending address (alias)
- **admin@kimaniclark.com** — Newsletters/logins (alias)

### OpenClaw Config Notes
- When setting `dmPolicy: "open"` for any channel account, MUST also include `allowFrom: ["*"]`
- Config validation enforces this as a safety requirement

### Motion (Task Management) ✅
- **Docs**: https://docs.usemotion.com
- **What I can do**: Create tasks, get schedules
- **LIMITATION**: Motion API only supports Tasks, NOT Events. Tasks show in Motion but don't sync to Apple Calendar.
- **CRITICAL**: Always include `autoScheduled` when creating tasks — without it, tasks won't appear on calendar!
  ```json
  "autoScheduled": {
    "startDate": "YYYY-MM-DD",
    "deadlineType": "SOFT",
    "schedule": "Work Hours"
  }
  ```
- **Workspaces**: Law Company = `BNopGoBRs6iIYs4ulAkT8`, Personal = `QDEsQoPza_p5clRPrh3LE`, Crown Acquisitions = `GwzH_8QWAAjwoYs18vKkm`, The Modern Owner = `uduxE79OeLU1QEZlh1Euq`, Life Concierge = `qoZOmVGH4FFfuuoWc2_0Q`, One Call Away = `1UYNj9zhkFS4l4iuFLlIs`

### Google Calendar (via Gmail OAuth) ✅
- **Account**: kimani@kimaniclark.com
- **What I can do**: Create, edit, delete calendar events
- **Syncs to iPhone**: Yes! Events appear in iOS Calendar app alongside Apple Calendar
- **Use this for**: Creating calendar events that need to show on Kimani's phone
- **Note**: Motion tasks don't sync to Apple Calendar, so use Google Calendar API for actual calendar events

### iCloud Calendar (via CalDAV) ✅
- **Apple ID**: kclark@alum.mit.edu
- **Principal ID**: 171088746
- **What I can do**: Read all iCloud calendar events
- **Calendars available**:
  - Calendar (main) - `00D3B8D0-6B3A-4B46-9E0D-15687351F8AD`
  - Assistant - `work/`
  - Home Assistant - `4D520B86-0865-41F9-BCBC-A983C786EA3E`
  - Free time - `51700024-1341-4626-AAA6-911B72A00EAF`
  - Reminders ⚠️ - `b72694ac-2025-4c3d-acfc-191263add5c9`
  - Notification - `home/`
- **Use this for**: Checking Kimani's schedule before creating events, avoiding conflicts

### Twilio (SMS/Voice) ⏳
- **Status**: A2P 10DLC campaign PENDING carrier approval
- **Voice calls**: Working
- **SMS**: Blocked until A2P approved

### LearnWorlds - The Modern Owner ✅
- **What I can do**: List students, check enrollments, course progress
- **16 students** currently accessible

### Coachmarketer CRM (Go High Level) ✅
- **Platform**: Go High Level
- **114 contacts** accessible
- **Use**: CRM for coaching/consulting leads

### Apollo (Lead Generation) ✅
- **What I can do**: People search, enrichment, sequences
- **Use**: Find leads, enrich contact data

### Instantly (Cold Email) ✅
- **What I can do**: Manage campaigns, lead finder
- **Use**: Cold email outreach

### Asana (Task Management) ✅
- **Workspace**: Assistance
- **Use**: Home assistant training and task management

### USPTO Open Data Portal ✅ NEW
- **API Base**: https://api.uspto.gov/api/v1
- **Key stored in**: `credentials.json` → `usptoODP.apiKey`
- **Rate Limits**: 1.2M document retrievals/week, 5M metadata retrievals/week
- **What I can do**:
  - Get application status and metadata by app number
  - List all documents in file wrapper (office actions, responses, etc.)
  - Get transaction history
  - Search applications by various criteria
- **Endpoints**:
  - `GET /patent/applications/{appNum}` — Full application data
  - `GET /patent/applications/{appNum}/documents` — Document list
  - `GET /patent/applications/{appNum}/transactions` — Transaction history
- **Note**: PDF downloads require browser (Patent Center doesn't expose doc content via API)
- **Reference Files**: `law-firm/patent-matters.md`, `law-firm/appcoll_docket_*.csv`

## Web Design Resources

**Design Inspiration:**
- **Dribbble** — https://dribbble.com — Designer portfolios, UI/UX inspiration
- **Godly** — https://godly.website — Curated gallery of beautiful websites
- **Awwwards** — https://awwwards.com — Award-winning web design showcase

**Website Builders:**
- **Framer** — https://framer.com — Design-forward, great templates
- **Webflow** — https://webflow.com — Powerful, more technical

**Reference Video:**
- "Stealing $10K Website Designs with Claude Code" — https://youtu.be/AaO6ujcx6TY

---

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
