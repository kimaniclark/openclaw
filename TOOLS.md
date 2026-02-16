# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Integrations

### Gmail (Email Access)
- **kimani@kimaniclark.com** — Kimani's personal email (primary inbox I monitor)
- **assistant@kimaniclark.com** — My email address (use for sending on Kimani's behalf)
- **admin@kimaniclark.com** — Newsletters and website logins (alias)
- All under the kimaniclark.com Google Workspace
- Set up via Telegram session

### Motion (Calendar/Task Management)
- **API Key**: Stored in `credentials.json`
- **Docs**: https://docs.usemotion.com
- **Usage**: Create tasks, get schedules, manage calendar
- **Setup**: Already configured and working
- **Important**: Always include `autoScheduled` when creating tasks, otherwise they don't appear on calendar
  ```json
  "autoScheduled": {
    "startDate": "YYYY-MM-DD",
    "deadlineType": "SOFT",
    "schedule": "Work Hours"
  }
  ```

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
