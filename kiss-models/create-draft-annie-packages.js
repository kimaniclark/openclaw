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
  const subject = 'KiSS Model Management — Photography Packages';
  const to = 'annie.angle.aa@gmail.com';
  const from = 'KiSS Models <info@kissmodelmanagement.com>';
  const boundary = 'boundary_kiss_models_packages_2026';

  const htmlBody = [
    '<div style="font-family: Arial, sans-serif; line-height: 1.6;">',
    '<p>Hi Ann,</p>',
    '<p>Welcome to KiSS Model Management! We\'re excited to have you on board.</p>',
    '<p>As a next step, we wanted to share our photography packages with you. Professional photos are essential for building your portfolio and booking work. Please see the attached flyer for our current offerings:</p>',
    '<ul>',
    '<li><b>Package 1 — Digitals/Headshots:</b> $250</li>',
    '<li><b>Package 2 — 2 Looks Studio:</b> $600</li>',
    '<li><b>Package 3 — Editorial:</b> $1,000</li>',
    '</ul>',
    '<p>If you\'re interested in any of these packages or have questions, feel free to reach out and we\'ll get you scheduled!</p>',
    '<p>Best,<br/>',
    'Maria Mara<br/>',
    'Head Booker<br/>',
    'Email: <a href="mailto:info@kissmodelmanagement.com">info@kissmodelmanagement.com</a> | Office: 202-640-3560<br/>',
    'Web: <a href="http://www.kissmodelmanagement.com">www.kissmodelmanagement.com</a> | Instagram: @kissmodelsus</p>',
    '</div>'
  ].join('\n');

  // Read the photography packages flyer
  const flyerPath = path.join(__dirname, 'photo-packages-2026-final.jpg');
  const flyerData = fs.readFileSync(flyerPath).toString('base64');

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
    'Content-Type: image/jpeg; name="KiSS-Photography-Packages.jpg"',
    'Content-Disposition: attachment; filename="KiSS-Photography-Packages.jpg"',
    'Content-Transfer-Encoding: base64',
    '',
    flyerData,
    '',
    '--' + boundary + '--'
  ];

  const raw = Buffer.from(messageParts.join('\r\n')).toString('base64url');

  const draftBody = { message: { raw } };

  const draft = await gmail.users.drafts.create({
    userId: 'me',
    requestBody: draftBody
  });
  console.log('Draft created! ID:', draft.data.id);
}
main().catch(e => console.error(e));
