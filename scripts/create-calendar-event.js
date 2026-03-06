#!/usr/bin/env node
// Create Google Calendar event using Gmail OAuth credentials
const fs = require('fs');
const path = require('path');

const CREDS_PATH = path.join(process.env.HOME, '.openclaw/workspace/credentials.json');
const creds = JSON.parse(fs.readFileSync(CREDS_PATH, 'utf8'));
const gmail = creds.gmailPersonal;

if (!gmail || !gmail.accessToken) {
  console.error('No gmailPersonal credentials found');
  process.exit(1);
}

async function refreshTokenIfNeeded() {
  if (gmail.expiresAt && Date.now() > gmail.expiresAt - 60000) {
    const response = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        client_id: gmail.clientId,
        client_secret: gmail.clientSecret,
        refresh_token: gmail.refreshToken,
        grant_type: 'refresh_token'
      })
    });
    const data = await response.json();
    if (data.access_token) {
      gmail.accessToken = data.access_token;
      gmail.expiresAt = Date.now() + (data.expires_in * 1000);
      creds.gmailPersonal = gmail;
      fs.writeFileSync(CREDS_PATH, JSON.stringify(creds, null, 2));
    }
  }
}

async function createEvent(event) {
  await refreshTokenIfNeeded();
  
  const response = await fetch('https://www.googleapis.com/calendar/v3/calendars/primary/events', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${gmail.accessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(event)
  });
  
  const data = await response.json();
  if (data.error) {
    console.error('Error:', JSON.stringify(data.error, null, 2));
    process.exit(1);
  }
  return data;
}

// Event details from command line or stdin
const eventJson = process.argv[2];
if (!eventJson) {
  console.error('Usage: node create-calendar-event.js \'{"summary":"...", "start":{...}, "end":{...}}\'');
  process.exit(1);
}

const event = JSON.parse(eventJson);
createEvent(event).then(result => {
  console.log('✅ Event created:', result.htmlLink);
  console.log('ID:', result.id);
}).catch(err => {
  console.error('Failed:', err.message);
  process.exit(1);
});
