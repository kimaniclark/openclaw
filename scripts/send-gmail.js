#!/usr/bin/env node

const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

// Load credentials
const credentialsPath = path.join(__dirname, '..', 'credentials.json');
const credentials = JSON.parse(fs.readFileSync(credentialsPath, 'utf8'));

const gmail = google.gmail('v1');

async function sendEmail(to, subject, body, from = 'assistant@kimaniclark.com') {
  try {
    const oauth2Client = new google.auth.OAuth2(
      credentials.gmailPersonal.clientId,
      credentials.gmailPersonal.clientSecret,
      'urn:ietf:wg:oauth:2.0:oob'
    );

    oauth2Client.setCredentials({
      refresh_token: credentials.gmailPersonal.refreshToken
    });

    const rawMessage = [
      `From: ${from}`,
      `To: ${to}`,
      `Subject: ${subject}`,
      '',
      body
    ].join('\n');

    const encodedMessage = Buffer.from(rawMessage)
      .toString('base64')
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=+$/, '');

    const result = await gmail.users.messages.send({
      auth: oauth2Client,
      userId: 'me',
      requestBody: {
        raw: encodedMessage
      }
    });

    console.log('✅ Email sent successfully');
    console.log('Message ID:', result.data.id);
    return result.data;

  } catch (error) {
    console.error('❌ Failed to send email:', error.message);
    throw error;
  }
}

// Command line usage
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length < 3) {
    console.log('Usage: node send-gmail.js <to> <subject> <body> [from]');
    process.exit(1);
  }
  
  const [to, subject, body, from] = args;
  sendEmail(to, subject, body, from).catch(console.error);
}

module.exports = { sendEmail };