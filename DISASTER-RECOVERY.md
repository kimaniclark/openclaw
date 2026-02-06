# OpenClaw Disaster Recovery Guide

## Quick Start: Restore on New MacBook

If your MacBook is lost/stolen/broken, follow these steps to restore OpenClaw completely:

### Prerequisites
1. Access to your GitHub account (https://github.com/kimaniclark)
2. Encrypted credentials backup file (from Dropbox or external drive)
3. Decryption password (you set this when creating backup)
4. Media backup file (optional - if you need attachments/videos)

---

## Step-by-Step Restoration

### 1. Install OpenClaw
```bash
npm install -g openclaw
```

### 2. Clone Workspace from GitHub
```bash
# If you have SSH keys set up:
git clone git@github.com:kimaniclark/openclaw.git ~/.openclaw/workspace

# If not (use HTTPS with Personal Access Token):
git clone https://github.com/kimaniclark/openclaw.git ~/.openclaw/workspace
```

### 3. Restore Encrypted Credentials
```bash
cd ~/.openclaw/workspace

# Run restore script with your backup file
./scripts/restore-from-backup.sh ~/Dropbox/OpenClaw-Backups/credentials-backup-YYYYMMDD-HHMMSS.tar.gz.enc

# Enter your decryption password when prompted
```

This restores:
- ✅ `credentials.json` (API keys, secrets)
- ✅ `openclaw.json` (OpenClaw configuration)
- ✅ SSH keys (for GitHub access)

### 4. Restore Media Files (Optional)
```bash
cd ~/.openclaw/workspace

# Extract media backup
tar -xzf ~/Dropbox/OpenClaw-Backups/media-backup-YYYYMMDD-HHMMSS.tar.gz
```

### 5. Start OpenClaw
```bash
openclaw gateway start
```

### 6. Verify Telegram Connection
Send a message to your Life Concierge bot on Telegram - it should respond immediately.

---

## Creating Backups

### Option 1: Full Backup (Recommended)
Creates all three backups at once:
```bash
cd ~/.openclaw/workspace
./scripts/full-backup.sh
```

This runs:
1. GitHub sync (workspace code)
2. Encrypted credentials backup
3. Media files backup

### Option 2: Individual Backups

**GitHub Backup** (automatic weekly, manual anytime):
```bash
./scripts/backup-to-github.sh
```

**Encrypted Credentials Backup**:
```bash
./scripts/backup-credentials.sh
# Enter password when prompted
# Save file to Dropbox/external drive
```

**Media Files Backup**:
```bash
./scripts/backup-media.sh
# Upload resulting file to Dropbox
```

---

## What's Backed Up Where

### GitHub (Public/Private Repo)
- ✅ All code and scripts
- ✅ Documentation (markdown files)
- ✅ Memory files (MEMORY.md, daily notes)
- ✅ Dashboards (HTML)
- ✅ Product documentation
- ❌ credentials.json (excluded for security)
- ❌ Large media files (excluded for size)

**Restored by:** `git clone`

### Encrypted Credentials Backup
- ✅ credentials.json (API keys, tokens)
- ✅ openclaw.json (OpenClaw config)
- ✅ SSH private/public keys

**Restored by:** `restore-from-backup.sh`

### Media Backup
- ✅ attachments/ (photos, videos from Home Concierge)
- ✅ heavy-duty-videos/ (fitness training videos)
- ✅ ~/.openclaw/media/ (inbound media files)

**Restored by:** Manual tar extraction

---

## Backup Schedule

### Automatic
- **Weekly GitHub backup**: Every Sunday 11 PM EST
- Runs via OpenClaw cron job

### Manual (Recommended)
- **Monthly full backup**: First of each month
- **Before major changes**: New integrations, config changes
- **After important work**: Completed projects, new dashboards

---

## Storage Recommendations

### Primary: Dropbox
Create folder: `~/Dropbox/OpenClaw-Backups/`

Structure:
```
OpenClaw-Backups/
├── credentials/
│   ├── credentials-backup-20260206-091500.tar.gz.enc
│   └── credentials-backup-20260301-120000.tar.gz.enc
└── media/
    ├── media-backup-20260206-091500.tar.gz
    └── media-backup-20260301-120000.tar.gz
```

### Secondary: External Drive
Keep a copy on external hard drive or USB stick in safe location.

### Retention Policy
- Keep last 3 monthly backups
- Keep last 6 weekly GitHub commits
- Archive older backups yearly

---

## Security Notes

### Encrypted Credentials
- **AES-256-CBC encryption** (military-grade)
- Password is NOT stored anywhere
- **Write down your password** in secure location (password manager, safe)
- Without password, backup cannot be decrypted

### What NOT to Share
- ❌ Encrypted backup files
- ❌ Decryption password
- ❌ credentials.json
- ❌ SSH private keys

### Safe to Share
- ✅ GitHub repo URL (if private repo)
- ✅ Media backup files (no sensitive data)
- ✅ Documentation files

---

## Troubleshooting

### "Decryption failed"
- Wrong password entered
- Corrupted backup file
- Try older backup file

### "SSH authentication failed"
- SSH keys not restored
- Need to add SSH key to GitHub again
- Or use HTTPS with Personal Access Token

### "Missing API keys"
You'll need to regenerate from services:
- **Twilio**: https://console.twilio.com/
- **Motion**: https://app.usemotion.com/settings/api
- **OpenAI**: https://platform.openai.com/api-keys
- **Gmail**: Re-run OAuth flow
- **Stripe**: https://dashboard.stripe.com/apikeys

---

## Test Your Backup

Run this monthly to verify backups work:

```bash
# 1. Create full backup
./scripts/full-backup.sh

# 2. Verify files exist
ls -lh backups/secure/
ls -lh backups/media/

# 3. Test decryption (without restoring)
openssl enc -aes-256-cbc -d -pbkdf2 -in backups/secure/credentials-backup-*.tar.gz.enc | tar -tzf -
```

---

## Emergency Contacts

If you can't access backups:
1. **GitHub**: https://github.com/kimaniclark/openclaw (workspace code)
2. **Telegram Bot**: @LifeConciergeBot (may still work if backend OK)
3. **Service Providers**: Regenerate API keys from their dashboards

---

**Last Updated**: February 6, 2026
