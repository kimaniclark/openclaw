# Voice Server Guide

## Overview

A standalone voice server at `http://localhost:18791` that handles phone calls for Johnny. It replaces the old OpenClaw voice-call plugin which had ~5 second response times. The new server uses OpenAI's Realtime API for near-instant (~500ms) voice responses.

- **Twilio phone number**: +1 (202) 998-6450
- **Kimani's phone number**: +1 (301) 674-1098
- **Server location**: `~/voice-server/`
- **Config**: `~/voice-server/.env`
- **Port**: 18791

The server runs as an always-on background service (macOS Launch Agent). It starts automatically when the Mac boots up.

## How to Make Outbound Calls

Send a POST request to the voice server:

```bash
curl -X POST http://localhost:18791/call \
  -H "Content-Type: application/json" \
  -d '{
    "to": "+15551234567",
    "prompt": "Your task-specific instructions here"
  }'
```

### Parameters
- `to` (required): Phone number in E.164 format (e.g., `+15551234567`)
- `prompt` (required for useful calls): Custom instructions for this specific call. This is where ALL context and knowledge must be passed — the AI on the call only knows what you put in the prompt. If omitted, uses a generic Johnny greeting.

### Response
```json
{"success": true, "callSid": "CA...", "to": "+15551234567"}
```

Save the `callSid` — you need it to retrieve the call results afterward.

## Getting Call Results

After making a call, retrieve the transcript using the callSid:

```bash
# Get results for a specific call
curl http://localhost:18791/call/{callSid}

# List all recent calls
curl http://localhost:18791/calls
```

### Response format:
```json
{
  "callSid": "CA...",
  "status": "completed",
  "startedAt": "2026-03-30T08:00:03.282Z",
  "endedAt": "2026-03-30T08:00:53.992Z",
  "transcript": [
    {"role": "user", "text": "Hello?", "timestamp": "..."},
    {"role": "assistant", "text": "Hey Kimani, it's Johnny...", "timestamp": "..."},
    {"role": "user", "text": "Thursday at 1 PM works.", "timestamp": "..."}
  ],
  "summary": "Caller: Hello?\nJohnny: Hey Kimani, it's Johnny...\nCaller: Thursday at 1 PM works."
}
```

### Status values:
- `in-progress` — call is still happening, check again in 15-30 seconds
- `completed` — call finished, transcript available

## Complete Workflow for Bot-Initiated Calls

1. **Prepare the prompt** — include ALL context the AI needs (who, why, task, details, fallbacks)
2. **Make the call** — `POST /call` with `to` and `prompt` → save the `callSid`
3. **Wait** — typical calls last 30-60 seconds
4. **Check results** — `GET /call/{callSid}` → if status is `in-progress`, wait and check again
5. **Read the transcript** — determine the outcome (e.g., "they said yes to Friday at 7pm")
6. **Take follow-up actions** — report to Kimani, schedule next call, update records, etc.

## Writing Good Call Prompts

The `prompt` field is the system instruction for the AI on the call. The AI (GPT-4o-mini with the "ash" voice) only knows what you include in the prompt. Include:

1. **Identity** — "You are Johnny, Kimani's AI assistant."
2. **Who you're calling and why** — "You are calling Mike to schedule a dinner."
3. **The specific task** — "Schedule dinner for Friday at 7pm at Founding Farmers."
4. **Relevant context** — Any info needed (preferences, history, details)
5. **Fallback options** — "If Friday doesn't work, suggest Saturday."
6. **Tone** — "Be friendly and conversational. Keep it brief."

### Example prompts:

**Scheduling:**
```
You are Johnny, Kimani's AI assistant. You are calling Sheryl to see if she's available for lunch with Kimani on Thursday at 1 PM at Earl's Restaurant in Tysons Corner, Virginia. If Thursday doesn't work, ask what day works for her this week or next. Get a confirmed day, time, and confirm the restaurant works for her. Be warm and conversational.
```

**Follow-up:**
```
You are Johnny, calling on behalf of Kimani Clark from The Modern Owner. You're following up with this person who expressed interest in life concierge services. Ask if they're still interested, answer basic questions about the service, and if they want to proceed, let them know Kimani will reach out personally.
```

**Reminder:**
```
You are Johnny, Kimani's AI assistant. You're calling to remind them about their dentist appointment tomorrow at 2pm at Dr. Williams' office on K Street. Keep it very brief.
```

**Information gathering:**
```
You are Johnny, Kimani's AI assistant. You're calling the AMC Georgetown theater to ask what times Project Hail Mary is playing tomorrow evening. Get the specific showtimes and whether they recommend booking in advance. Be polite and brief.
```

## Inbound Calls

Anyone who calls +1 (202) 998-6450 will automatically talk to Johnny. Inbound call transcripts are saved just like outbound calls.

### Checking for inbound calls:
```bash
# Get only inbound calls
curl http://localhost:18791/calls?direction=inbound

# Get inbound calls since a specific time
curl "http://localhost:18791/calls?direction=inbound&since=2026-03-30T08:00:00Z"
```

Each inbound call result includes `"direction": "inbound"` and the caller's phone number in the `"from"` field. The bot should periodically check for new inbound calls and report them to Kimani.

### Customizing the inbound persona:

The default inbound prompt can be changed on the fly without restarting:

```bash
# View current inbound prompt
curl http://localhost:18791/inbound-prompt

# Update it
curl -X PUT http://localhost:18791/inbound-prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt": "You are Johnny, Kimani'\''s AI assistant. You answer calls on his behalf. Take messages and let callers know Kimani will get back to them."}'
```

To make a permanent change, edit `INBOUND_PROMPT` in `~/voice-server/.env` and restart the server.

The default inbound prompt tells Johnny to take messages, handle scheduling requests, and let callers know he'll pass information along to Kimani.

## Service Management

### Check if services are running:
```bash
# Quick health check
curl -s http://localhost:18791/

# Check launch agent status
launchctl list | grep voice-server
```

### Stop the voice server:
```bash
launchctl unload ~/Library/LaunchAgents/com.voice-server.realtime.plist
launchctl unload ~/Library/LaunchAgents/com.voice-server.tunnel.plist
```

### Start the voice server:
```bash
launchctl load ~/Library/LaunchAgents/com.voice-server.tunnel.plist
launchctl load ~/Library/LaunchAgents/com.voice-server.realtime.plist
```

### Restart (e.g. after config changes):
```bash
launchctl unload ~/Library/LaunchAgents/com.voice-server.realtime.plist
sleep 1
launchctl load ~/Library/LaunchAgents/com.voice-server.realtime.plist
```

### After a Mac reboot:
Both services start automatically. The tunnel startup script (`~/voice-server/start-tunnel.sh`) automatically:
1. Starts the Cloudflare tunnel
2. Gets the new tunnel URL (it changes each restart)
3. Updates `~/voice-server/.env` with the new URL
4. Updates the Twilio webhook to point to the new URL
5. Restarts the voice server to pick up the new URL

No manual action needed after reboot.

### View logs:
```bash
cat ~/voice-server/logs/server.log        # Server output
cat ~/voice-server/logs/server.err.log    # Server errors
cat ~/voice-server/logs/tunnel-startup.log # Tunnel startup log
cat ~/voice-server/logs/tunnel.err.log    # Tunnel errors
```

## Server Modes (Backup Options)

Three server modes are available. OpenAI Realtime is the primary one. The others are backups built during testing:

| Command | Backend | Latency | Voice | Notes |
|---|---|---|---|---|
| `npm run start:realtime` | OpenAI Realtime API | ~500ms | ash | **Primary — use this** |
| `npm start` | Claude Haiku + ElevenLabs/OpenAI TTS | ~1.5-2s | configurable | Backup — better intelligence (Claude), needs ElevenLabs paid plan for best voice |
| `npm run start:gemini` | Gemini Live API | ~5-20s | Aoede | Not recommended — high latency, thinking out loud issues |

### To switch modes:
1. Stop the current server: `launchctl unload ~/Library/LaunchAgents/com.voice-server.realtime.plist`
2. Edit the launch agent plist to point to a different server file (e.g., `server.js` instead of `server-realtime.js`)
3. Restart: `launchctl load ~/Library/LaunchAgents/com.voice-server.realtime.plist`

Or for quick manual testing: `cd ~/voice-server && npm start` (runs the Claude + ElevenLabs backup)

### Backup: Claude + ElevenLabs (Option A)
The `npm start` server uses a streaming pipeline: OpenAI STT → Claude Haiku 4.5 → ElevenLabs TTS with sentence-level chunking. It has higher latency (~1.5-2s) but uses Claude (smarter) and ElevenLabs (better voice quality). Currently configured with OpenAI TTS as fallback since ElevenLabs requires a paid plan for API voice access. If Kimani upgrades ElevenLabs, update the voice ID and model to `eleven_flash_v2_5` in `~/voice-server/.env` for the best voice quality.

## Architecture Summary

```
BEFORE (OpenClaw voice-call plugin, ~5s latency):
  Twilio → OpenAI STT → Claude Haiku → ElevenLabs TTS → Twilio
  (each step runs sequentially — 0.5s + 2.3s + 2.5s = ~5s)

NOW (voice-server, ~500ms latency):
  Twilio ↔ Bridge Server ↔ OpenAI Realtime API
  (single WebSocket connection, audio in → audio out)
```

## Key Files
- `~/voice-server/server-realtime.js` — Primary server (OpenAI Realtime)
- `~/voice-server/server.js` — Backup server (Claude + ElevenLabs/OpenAI TTS)
- `~/voice-server/server-gemini.js` — Experimental (Gemini Live, not recommended)
- `~/voice-server/.env` — API keys and config
- `~/voice-server/start-tunnel.sh` — Tunnel startup script (auto-updates URL + Twilio)
- `~/voice-server/package.json` — npm scripts
- `~/Library/LaunchAgents/com.voice-server.realtime.plist` — Server launch agent
- `~/Library/LaunchAgents/com.voice-server.tunnel.plist` — Tunnel launch agent
