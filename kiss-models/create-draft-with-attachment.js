const creds = require('../credentials.json');
const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

const oauth2Client = new google.auth.OAuth2(
  creds.gmailKissModels.clientId,
  creds.gmailKissModels.clientSecret
);
oauth2Client.setCredentials({
  refresh_token: creds.gmailKissModels.refreshToken
});
const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

async function main() {
  // First delete the old draft
  try {
    await gmail.users.drafts.delete({ userId: 'me', id: 'r-2403106262991398879' });
    console.log('Old draft deleted');
  } catch (e) {
    console.log('Could not delete old draft:', e.message);
  }

  const subject = 'DEVACURL Shoot \u2014 Call Sheet Details \u2014 September 3, 2026';
  const to = 'inquire.shavonne@gmail.com';
  const from = 'KiSS Models <info@kissmodelmanagement.com>';
  const boundary = 'boundary_kiss_models_2026';

  const htmlBody = [
    '<div style="font-family: Arial, sans-serif; line-height: 1.6;">',
    '<p>Hi ShaVonne,</p>',
    '<p>Here are the details for the upcoming DevaCurl shoot:</p>',
    '<ul>',
    '<li><b>Date:</b> Wednesday, September 3, 2026</li>',
    '<li><b>Arrival Time:</b> 8:00 AM</li>',
    '<li><b>Location:</b> 5800 Bristol Parkway, Suite 700, Culver City, CA 90230</li>',
    '<li><b>Check-in:</b> 7th Floor Lobby for further instructions (no elevator key needed)</li>',
    '<li><b>Parking:</b> C3 Parking Structure, entrance on Hannum Ave. Parking validation available at the Henkel Lobby, 7th floor.</li>',
    '</ul>',
    '<p><b>Important \u2014 Please follow these instructions:</b></p>',
    '<ul>',
    '<li><b>Hair:</b> Come with your hair washed and clean \u2014 <b>no product at all</b> in your hair. No chemical processes (relaxers, perms, bleaching), no extensions or weaves.</li>',
    '<li><b>Makeup:</b> Come with no makeup.</li>',
    '<li><b>Wardrobe:</b> Bring a white tank top or regular jeans (your own clothes will be used for &quot;before shots&quot;).</li>',
    '</ul>',
    '<p><b>On-site Contact:</b> Susan Lopez \u2014 424.353.9884</p>',
    '<p><b>Rate:</b> $1,200.00 \u2013 20% agency fee (one day)</p>',
    '<p>Please confirm you\'ve received this and that you\'re all set for September 3rd!</p>',
    '<p>Best,<br/>',
    'Maria Mara<br/>',
    'Head Booker<br/>',
    'Email: <a href="mailto:info@kissmodelmanagement.com">info@kissmodelmanagement.com</a> | Office: 202-640-3560<br/>',
    'Web: <a href="http://www.kissmodelmanagement.com">www.kissmodelmanagement.com</a> | Instagram: @kissmodelsus</p>',
    '</div>'
  ].join('\n');

  // Read the PDF attachment
  const pdfPath = path.join(__dirname, 'On pager- Model call (2).pdf');
  const pdfData = fs.readFileSync(pdfPath).toString('base64');

  const messageParts = [
    'From: ' + from,
    'To: ' + to,
    'Subject: ' + subject,
    'MIME-Version: 1.0',
    'Content-Type: multipart/mixed; boundary="' + boundary + '"',
    '',
    '--' + boundary,
    'Content-Type: text/html; charset=utf-8',
    '',
    htmlBody,
    '',
    '--' + boundary,
    'Content-Type: application/pdf; name="DevaCurl Call Sheet.pdf"',
    'Content-Disposition: attachment; filename="DevaCurl Call Sheet.pdf"',
    'Content-Transfer-Encoding: base64',
    '',
    pdfData,
    '',
    '--' + boundary + '--'
  ];

  const raw = Buffer.from(messageParts.join('\r\n')).toString('base64url');

  // Find existing thread
  const threadSearch = await gmail.users.messages.list({
    userId: 'me',
    q: 'from:inquire.shavonne@gmail.com subject:DevaCurl',
    maxResults: 1
  });

  let threadId;
  if (threadSearch.data.messages && threadSearch.data.messages.length > 0) {
    const msg = await gmail.users.messages.get({ userId: 'me', id: threadSearch.data.messages[0].id, format: 'metadata' });
    threadId = msg.data.threadId;
    console.log('Found existing thread:', threadId);
  }

  const draftBody = { message: { raw } };
  if (threadId) draftBody.message.threadId = threadId;

  const draft = await gmail.users.drafts.create({
    userId: 'me',
    requestBody: draftBody
  });
  console.log('Draft created with attachment! ID:', draft.data.id);
}
main().catch(e => console.error(e));
