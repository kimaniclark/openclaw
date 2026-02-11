# Discord Setup

## Current Configuration

**Bot:** @Johnny  
**Bot Token:** Stored in `openclaw.json` (channels.discord.token)  
**Bot ID:** 1470546329208885440  
**Developer Portal:** https://discord.com/developers/applications/1470546329208885440

### Active Servers

**Personal Server (ID: 1470332865123188767)**
- **Owner:** Kimani Clark (@kimaniclark)
- **Channels:**
  - Text Channels → #general (working)
  - Personal → #general-personal (working)
  - Personal → #life-concierge
  - Business → #the-modern-owner
  - Business → #crown-acquisitions
  - Business → #modeling-agency
- **Config:** `requireMention: false` (no @mentions needed - zero friction)
- **Purpose:** Personal workspace, quick access, low friction communication

### Configuration Pattern

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "***REDACTED_DISCORD_TOKEN***",
      "groupPolicy": "open",
      "guilds": {
        "1470332865123188767": {
          "requireMention": false
        }
      }
    }
  }
}
```

## Bot Permissions

**Enabled Intents (in Developer Portal):**
- ✅ Message Content Intent (required to read message text)
- ✅ Server Members Intent (recommended for member lookups)

**Bot Permissions (OAuth invite):**
- View Channels
- Send Messages
- Read Message History
- Embed Links
- Attach Files
- Add Reactions
- Use External Emojis

**Invite URL Template:**
```
https://discord.com/oauth2/authorize?client_id=1470546329208885440&permissions=277025508416&scope=bot+applications.commands
```

## Adding New Servers

### Quick Setup (for future servers)

1. **Generate invite link** (use template above)
2. **Join server** → Accept invite, authorize permissions
3. **Get Server ID:**
   - Enable Developer Mode (Settings → Advanced → Developer Mode)
   - Right-click server → Copy Server ID
4. **Add to config:**
   ```json
   "guilds": {
     "SERVER_ID_HERE": {
       "requireMention": false
     }
   }
   ```
5. **Restart gateway:** `openclaw gateway restart`

### Channel-Specific Configuration (if needed)

For more granular control (specific channels only, different mention settings):

```json
"guilds": {
  "SERVER_ID": {
    "requireMention": false,
    "channels": {
      "channel-name": { "allow": true },
      "another-channel": { "allow": true, "requireMention": true }
    }
  }
}
```

## Planned Future Servers

### Life Concierge Client Servers
- **Purpose:** Individual Discord servers for premium Life Concierge clients
- **Pattern:** One server per client (private workspace)
- **Features:** 
  - Task management channels
  - Quick communication
  - File sharing
  - Voice notes support
- **Config:** `requireMention: false` (low friction for clients)
- **Onboarding:** Part of Life Concierge product setup

### Kiss Model Management Server
- **Purpose:** Business communication with Victoria (business partner)
- **Channels:**
  - #model-outreach (portfolio pitches)
  - #brand-partnerships (fashion brands, photographers)
  - #operations (scheduling, admin)
  - #portfolio-pad (PortfolioPad integration tasks)
- **Config:** `requireMention: false` (team workspace)
- **Integration:** Apollo.io lead lists, automated follow-ups

### Modern Owner / Crown Acquisitions Servers
- **Purpose:** Separate business context if needed
- **Pattern:** Could use existing Personal server channels OR separate servers for clients/partners
- **Decision:** TBD based on communication volume

## Design Philosophy

**Zero Friction Communication:**
- No @mentions required in private servers
- Voice messages + text seamlessly
- One-touch interaction pattern
- Matches Telegram workflow efficiency

**Multi-Context Separation:**
- Telegram: Personal + Business (two channels for mental separation)
- Discord: Can support unlimited servers (clients, partners, teams)
- Each server = separate context (no token limit issues)

**Scalability:**
- Same bot can join unlimited servers
- Same bot token works everywhere
- Per-server configuration (mention requirements, channel access, etc.)
- Easy to add new servers (5 minute setup)

## Troubleshooting Notes

**Common Issues Solved:**

1. **Bot not responding:**
   - Check Message Content Intent is enabled
   - Check bot has channel permissions (View + Send + Read History)
   - Verify bot is actually in the channel (not just the server)

2. **"No mention" error even with @mention:**
   - Set `requireMention: false` to bypass
   - Restart gateway after config change

3. **404 Unknown Channel:**
   - Bot needs to be added to specific channels (categories don't auto-grant access)
   - Right-click channel → Permissions → Add Johnny

4. **Intents changed after bot joined:**
   - Remove bot from server (kick)
   - Re-invite with fresh link
   - Discord caches intent permissions on join

## Cost & Limits

- **Discord Bot:** Free (unlimited servers, unlimited messages)
- **Rate Limits:** 50 requests/second (way more than needed)
- **Message Length:** 2000 characters (OpenClaw handles chunking)
- **File Uploads:** 8MB default (configurable in OpenClaw)

## Security

- **Bot Token:** Never share publicly, treat like a password
- **Server Access:** Only add bot to servers you control
- **groupPolicy:** Set to "open" for personal use, "allowlist" for production multi-tenant
- **Credentials:** Token stored in `openclaw.json` (not in git)

## Next Steps

- [ ] Create Life Concierge client server template (reusable setup)
- [ ] Set up Kiss Model Management server with Victoria
- [ ] Document server onboarding process for clients
- [ ] Consider webhook integrations (Discord → CRM for client communication tracking)

---

**Last Updated:** Feb 11, 2026  
**Status:** ✅ Personal server working, ready to scale to multiple servers
