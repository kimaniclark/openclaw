#!/usr/bin/env node
// Quick Gmail API check script
const fs = require('fs');
const path = require('path');

const CREDS_PATH = path.join(process.env.HOME, '.openclaw/workspace/credentials.json');
const creds = JSON.parse(fs.readFileSync(CREDS_PATH, 'utf8'));

const account = process.argv[2] || 'gmailPersonal';
const query = process.argv[3] || 'is:unread';
const maxResults = parseInt(process.argv[4]) || 10;

const gmail = creds[account];
if (!gmail || !gmail.accessToken) {
  console.error(`No credentials found for ${account}`);
  process.exit(1);
}

async function refreshTokenIfNeeded() {
  // Check if token is expired
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
      // Update credentials file
      creds[account] = gmail;
      fs.writeFileSync(CREDS_PATH, JSON.stringify(creds, null, 2));
    }
  }
}

async function searchEmails() {
  await refreshTokenIfNeeded();
  
  const url = `https://gmail.googleapis.com/gmail/v1/users/me/messages?q=${encodeURIComponent(query)}&maxResults=${maxResults}`;
  const response = await fetch(url, {
    headers: { 'Authorization': `Bearer ${gmail.accessToken}` }
  });
  
  if (!response.ok) {
    const error = await response.text();
    console.error('API Error:', response.status, error);
    return;
  }
  
  const data = await response.json();
  if (!data.messages || data.messages.length === 0) {
    console.log('No messages found matching query:', query);
    return;
  }
  
  console.log(`Found ${data.messages.length} messages:\n`);
  
  // Fetch details for each message
  for (const msg of data.messages.slice(0, 5)) {
    const detailUrl = `https://gmail.googleapis.com/gmail/v1/users/me/messages/${msg.id}?format=metadata&metadataHeaders=From&metadataHeaders=Subject&metadataHeaders=Date`;
    const detailRes = await fetch(detailUrl, {
      headers: { 'Authorization': `Bearer ${gmail.accessToken}` }
    });
    const detail = await detailRes.json();
    
    const headers = detail.payload?.headers || [];
    const from = headers.find(h => h.name === 'From')?.value || 'Unknown';
    const subject = headers.find(h => h.name === 'Subject')?.value || '(no subject)';
    const date = headers.find(h => h.name === 'Date')?.value || '';
    
    console.log(`📧 ${subject}`);
    console.log(`   From: ${from}`);
    console.log(`   Date: ${date}`);
    console.log(`   ID: ${msg.id}\n`);
  }
}

searchEmails().catch(console.error);
