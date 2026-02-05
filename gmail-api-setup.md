# Gmail API Setup for Life Concierge

**Date**: February 5, 2026  
**Purpose**: Fast email management across multiple Gmail accounts  
**Why**: Email management is core Life Concierge service - API access = speed + automation

---

## What Gmail API Enables

### Email Management Capabilities:
✅ **Read emails** - Fetch inbox, filter by sender/subject/date  
✅ **Send emails** - Send on your behalf with proper formatting  
✅ **Search emails** - Fast search across entire mailbox  
✅ **Label/organize** - Apply labels, archive, mark as read  
✅ **Attachments** - Download and save attachments  
✅ **Draft management** - Create drafts for your review  
✅ **Multi-account** - Manage multiple Gmail accounts from one place  
✅ **Watch/webhooks** - Get notified of new emails in real-time  

### Life Concierge Use Cases:
- **Phase 1**: Johnny reads emails, creates drafts for you to review
- **Phase 2**: Johnny handles routine responses automatically (confirmations, scheduling, etc.)
- **Email triage**: Categorize and prioritize incoming emails
- **Search & retrieve**: "Find that email from Erik Kimel about..."
- **Follow-ups**: Track emails that need responses
- **Unsubscribe management**: Clean up newsletter spam
- **Receipt organization**: Auto-save receipts to folders
- **Calendar integration**: Extract meeting invites, add to calendar

---

## Setup Steps

### Step 1: Enable Gmail API in Google Cloud Console

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account (kimani@kimaniclark.com or k@kimaniclark.com)

2. **Create a New Project** (or use existing)
   - Click dropdown at top: "Select a project"
   - Click "New Project"
   - Name: "Life Concierge" or "OpenClaw Email"
   - Click "Create"

3. **Enable Gmail API**
   - In the project, go to: "APIs & Services" → "Library"
   - Search for "Gmail API"
   - Click "Gmail API"
   - Click "Enable"

### Step 2: Create OAuth 2.0 Credentials

1. **Configure OAuth Consent Screen**
   - Go to: "APIs & Services" → "OAuth consent screen"
   - Choose "External" (unless you have Google Workspace)
   - App name: "Life Concierge"
   - User support email: Your email
   - Developer contact: Your email
   - Click "Save and Continue"
   - Scopes: Skip for now (we'll add later)
   - Test users: Add your email addresses
   - Click "Save and Continue"

2. **Create OAuth Client ID**
   - Go to: "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "OpenClaw Desktop"
   - Click "Create"
   - **IMPORTANT**: Download the JSON file
   - Save as: `~/.openclaw/credentials/gmail-credentials.json`

### Step 3: Configure Scopes (Permissions)

**Recommended Scopes for Life Concierge:**

**Read & Search** (Phase 1):
- `https://www.googleapis.com/auth/gmail.readonly` - Read all emails
- `https://www.googleapis.com/auth/gmail.metadata` - Read email metadata (headers, labels)

**Send & Compose** (Phase 2):
- `https://www.googleapis.com/auth/gmail.compose` - Create and send drafts
- `https://www.googleapis.com/auth/gmail.send` - Send emails

**Organize** (Phase 2):
- `https://www.googleapis.com/auth/gmail.modify` - Modify labels, archive, mark read
- `https://www.googleapis.com/auth/gmail.labels` - Manage labels

**Full Access** (Phase 3 - use with caution):
- `https://mail.google.com/` - Full mailbox access

**Start with**: `gmail.readonly` and `gmail.compose` for Phase 1

### Step 4: First-Time Authorization

When you first use the Gmail API, you'll need to authorize:

1. Run the Gmail script (Johnny will create this)
2. Browser will open asking you to sign in
3. Google will warn "This app isn't verified" - Click "Advanced" → "Go to Life Concierge (unsafe)"
4. Grant permissions
5. Authorization token saved to `~/.openclaw/credentials/gmail-token.json`

**This only needs to be done once per account!**

### Step 5: Add Multiple Email Accounts

To manage multiple Gmail accounts:
1. Repeat authorization flow for each account
2. Save tokens with different names:
   - `gmail-token-kimani.json` (kimani@kimaniclark.com)
   - `gmail-token-admin.json` (admin@thelifeconcierge.co)
   - `gmail-token-personal.json` (personal account)

---

## Gmail API Usage Examples

### Read Recent Emails
```javascript
// Get 10 most recent unread emails
const messages = await gmail.users.messages.list({
  userId: 'me',
  q: 'is:unread',
  maxResults: 10
});
```

### Search for Specific Email
```javascript
// Find email from Erik Kimel
const results = await gmail.users.messages.list({
  userId: 'me',
  q: 'from:ekimel@hfhsinc.com subject:Hassle'
});
```

### Send Email
```javascript
// Send email on your behalf
const raw = makeEmail(
  'kimani@kimaniclark.com',
  'recipient@example.com',
  'Subject Line',
  'Email body text...'
);

await gmail.users.messages.send({
  userId: 'me',
  requestBody: { raw: raw }
});
```

### Create Draft for Review
```javascript
// Johnny creates draft, you review before sending
await gmail.users.drafts.create({
  userId: 'me',
  requestBody: {
    message: { raw: emailContent }
  }
});
```

### Get Email with Attachments
```javascript
// Fetch full email including attachments
const message = await gmail.users.messages.get({
  userId: 'me',
  id: messageId,
  format: 'full'
});

// Download attachment
const attachment = await gmail.users.messages.attachments.get({
  userId: 'me',
  messageId: messageId,
  id: attachmentId
});
```

---

## Phase 1: Draft Mode (Safe Start)

**How it works:**
1. Johnny reads your inbox
2. Identifies emails that need responses
3. **Creates drafts** (doesn't send)
4. You review drafts in Gmail
5. You send when ready

**Why this approach:**
- ✅ You maintain full control
- ✅ No risk of wrong response being sent
- ✅ Build trust in Johnny's email writing
- ✅ Learn your communication style

**Transition to Phase 2:**
Once you're confident in Johnny's draft quality, authorize automatic sending for routine emails:
- Confirmations ("Got it, thanks!")
- Meeting RSVPs ("I'll be there")
- Information requests Johnny can answer
- Standard responses you approve

---

## Email Accounts to Set Up

Based on what you've mentioned:

1. **Primary**: kimani@kimaniclark.com (current via Hey.com, migrating to Gmail)
2. **Alternate**: k@kimaniclark.com
3. **Life Concierge**: admin@thelifeconcierge.co (when created)
4. **Johnny's email**: johnny@kimaniclark.com (when created)

**Priority**: Start with kimani@kimaniclark.com

---

## Email Management Workflow

### Daily Email Triage (Phase 1)

**Morning scan** (Johnny does this):
1. Fetch unread emails from last 24 hours
2. Categorize:
   - 🔴 **Urgent**: Needs immediate response
   - 🟡 **Important**: Needs response today
   - 🟢 **Info**: FYI, no response needed
   - ⚪ **Noise**: Newsletters, marketing, spam
3. Present summary to you via Telegram
4. Create drafts for urgent/important emails
5. Archive or label others

**Your action**:
- Review summary (2-5 min)
- Approve/edit/send drafts
- Delegate responses: "Johnny, reply to X and tell them Y"

### Search & Retrieval
**You**: "Find that email from Erik Kimel last week"  
**Johnny**: Searches, presents link or full email content

### Follow-up Tracking
**You**: "Remind me if Erik doesn't respond by Friday"  
**Johnny**: Tracks email, checks daily, alerts if no response

---

## Security & Privacy

### What's Safe:
✅ OAuth tokens stored locally on your Mac  
✅ Johnny can only access emails you authorize  
✅ Tokens can be revoked anytime in Google Account settings  
✅ All drafts visible to you before sending  

### What to Know:
⚠️ Gmail API access = full mailbox access (if you grant it)  
⚠️ Keep credentials.json and token files secure  
⚠️ Don't share OAuth client ID/secret publicly  

### Best Practices:
1. Start with read-only scope (`gmail.readonly`)
2. Add send permission only after you trust draft quality
3. Regularly review Johnny's email activity
4. Use draft mode for first 2-4 weeks minimum

---

## Cost

**Gmail API Pricing**: FREE for normal usage!
- 1 billion quota units per day (free)
- Reading email = 5 units
- Sending email = 100 units
- **Example**: 10,000 emails read + 100 sent = 50,000 + 10,000 = 60,000 units (well under limit)

**No cost concerns for Life Concierge usage.**

---

## Integration with Other Tools

### Motion API
- Johnny reads email: "Meeting request from Erik"
- Checks your Motion calendar
- Creates draft: "I'm available Tuesday at 2pm or Thursday at 10am"
- Adds tentative event to Motion calendar

### Asana
- Email says: "Here's the project update"
- Johnny extracts tasks
- Creates tasks in Asana
- Replies: "Got it, added 3 tasks to project tracker"

### Care.com (Future)
- Applicant emails resume
- Johnny logs in Care.com tracking spreadsheet
- Creates draft response with screening questions
- Schedules interview if you approve

---

## Error Handling

**Common Issues:**

**"Token expired"**
- Solution: Re-run authorization flow (browser opens again)
- Johnny can detect this and prompt you

**"Insufficient permissions"**
- Solution: Re-authorize with additional scopes
- Or: Modify OAuth consent screen scopes

**"Daily quota exceeded"**
- Unlikely (1B units/day)
- If hit: Johnny waits until tomorrow
- Or: Request quota increase (free for verified apps)

---

## Next Steps

### Immediate (Tonight/Tomorrow):
1. ✅ Create Google Cloud project
2. ✅ Enable Gmail API
3. ✅ Create OAuth credentials
4. ✅ Download credentials JSON
5. ✅ Authorize first account (kimani@kimaniclark.com)

### Short-term (This Week):
1. Johnny builds email reading script
2. Test with your inbox (read-only mode)
3. Johnny creates draft for one email
4. You review and refine

### Mid-term (Next 2 Weeks):
1. Daily email triage workflow
2. Draft quality improvement
3. Add search/retrieval commands
4. Email categorization labels

### Long-term (Month 2+):
1. Automatic responses for routine emails
2. Multi-account management
3. Receipt organization automation
4. Follow-up tracking system
5. Integration with Motion/Asana/Care.com

---

## Success Metrics

**Week 1:**
- Gmail API authorized and working
- Can read inbox via API
- Johnny creates 5 draft responses
- You review quality

**Week 2:**
- Daily email triage active
- 80% of drafts require minimal edits
- 10-15 min/day saved on email

**Month 1:**
- Fully trust Johnny's drafts
- Phase 2 activated: Auto-send routine responses
- 1-2 hours/day saved on email
- Zero missed important emails

---

## Documentation Links

- **Gmail API Docs**: https://developers.google.com/gmail/api
- **Node.js Quickstart**: https://developers.google.com/gmail/api/quickstart/nodejs
- **API Reference**: https://developers.google.com/gmail/api/reference/rest
- **OAuth 2.0 Setup**: https://developers.google.com/identity/protocols/oauth2

---

**Created**: February 5, 2026  
**Status**: Ready to implement  
**Priority**: High (core Life Concierge feature)  
**Owner**: Johnny to implement, Kimani to authorize
