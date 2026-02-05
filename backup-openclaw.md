# OpenClaw Backup & Disaster Recovery Guide

**Created**: February 5, 2026  
**Your System**: MacBook Air (Darwin 25.2.0 arm64)

---

## What Needs to be Backed Up

### Critical Data (2.3GB total):
1. **Workspace** (`~/.openclaw/workspace/`) - 2.3GB, 750 files
   - All your documents, dashboards, memory files
   - Home Concierge Dashboard + 178MB attachments
   - Project files, credentials, service provider info
   
2. **Configuration** (`~/.openclaw/openclaw.json`) - 3KB
   - Gateway settings, API keys, integrations
   - Telegram, Twilio, Motion, Asana configs
   
3. **Credentials** (`~/.openclaw/credentials/`)
   - Stored passwords, API tokens
   
4. **Custom Skills** (`~/.openclaw/skills/`)
   - Any custom skills you've added (twilio-sms)

### Less Critical (can be recreated):
- Logs (`~/.openclaw/logs/`)
- Temporary files (`~/.openclaw/media/`)
- Browser profiles (`~/.openclaw/browser/`)

---

## Recommended Backup Strategy

### Option 1: Git + GitHub (BEST - Version Control + Cloud)

**Advantages:**
- ✅ Version history (undo mistakes)
- ✅ Cloud backup (survives computer loss)
- ✅ Private repository (secure)
- ✅ Easy to restore on new computer
- ✅ Track changes over time
- ✅ Free for private repos

**Setup:**

```bash
# 1. Initialize git in workspace
cd ~/.openclaw/workspace
git init

# 2. Create .gitignore to exclude large/temp files
cat > .gitignore << 'EOF'
# Exclude large media files
attachments/
*.mp4
*.mov
*.MP4
*.MOV

# Exclude temporary files
.DS_Store
*.tmp
*.log

# Exclude sensitive credentials (if any accidentally in workspace)
credentials.json
**/credentials.json
EOF

# 3. Make initial commit
git add .
git commit -m "Initial backup - $(date)"

# 4. Create GitHub private repo and push
# (You'll do this in GitHub web interface, then:)
git remote add origin https://github.com/YOUR_USERNAME/openclaw-workspace.git
git branch -M main
git push -u origin main
```

**Daily Backup (Automated):**
```bash
# Create a backup script
cat > ~/backup-openclaw.sh << 'EOF'
#!/bin/bash
cd ~/.openclaw/workspace
git add .
git commit -m "Auto backup - $(date '+%Y-%m-%d %H:%M')"
git push origin main
echo "✅ OpenClaw workspace backed up to GitHub"
EOF

chmod +x ~/backup-openclaw.sh

# Run it manually, or add to cron:
# (every day at 11 PM)
# 0 23 * * * /Users/kimani/backup-openclaw.sh
```

### Option 2: Cloud Storage (Dropbox/Google Drive)

**Advantages:**
- ✅ Simple, automatic sync
- ✅ No git knowledge needed
- ✅ Includes large files (videos)
- ✅ Mobile access

**Setup:**

```bash
# Move workspace to Dropbox/Google Drive
mv ~/.openclaw/workspace ~/Dropbox/OpenClaw-Backup/

# Create symlink so OpenClaw still works
ln -s ~/Dropbox/OpenClaw-Backup/workspace ~/.openclaw/workspace

# Verify it works
ls -la ~/.openclaw/workspace
```

**Backup config separately:**
```bash
# Copy config to Dropbox
cp ~/.openclaw/openclaw.json ~/Dropbox/OpenClaw-Backup/
cp -r ~/.openclaw/credentials ~/Dropbox/OpenClaw-Backup/

# Set up daily backup
cat > ~/backup-openclaw-config.sh << 'EOF'
#!/bin/bash
cp ~/.openclaw/openclaw.json ~/Dropbox/OpenClaw-Backup/openclaw-$(date +%Y%m%d).json
cp -r ~/.openclaw/credentials ~/Dropbox/OpenClaw-Backup/credentials-backup/
echo "✅ Config backed up to Dropbox"
EOF

chmod +x ~/backup-openclaw-config.sh
```

### Option 3: Time Machine + External Drive

**Advantages:**
- ✅ Backs up entire Mac (not just OpenClaw)
- ✅ Apple's built-in solution
- ✅ Easy restore process

**Setup:**
1. Connect external drive
2. System Settings → General → Time Machine
3. Add backup disk
4. Verify `~/.openclaw/` is included (not excluded)

**Restore Process:**
1. Connect Time Machine drive to new Mac
2. Migration Assistant during setup
3. Or: Browse Time Machine, restore `~/.openclaw/`

### Option 4: Manual ZIP Archive

**Quick one-time backup:**

```bash
# Create dated backup
cd ~
tar -czf "openclaw-backup-$(date +%Y%m%d).tar.gz" \
  .openclaw/workspace \
  .openclaw/openclaw.json \
  .openclaw/credentials \
  .openclaw/skills

# Move to safe location
mv openclaw-backup-*.tar.gz ~/Documents/Backups/

# Or upload to cloud
# mv openclaw-backup-*.tar.gz ~/Dropbox/
```

**Restore:**
```bash
cd ~
tar -xzf openclaw-backup-20260205.tar.gz
```

---

## Disaster Recovery: New Computer Setup

### If Your Mac Dies Tomorrow

**Step 1: Install OpenClaw on New Mac**
```bash
# Install Node.js (if not installed)
brew install node

# Install OpenClaw globally
npm install -g openclaw

# Start gateway
openclaw gateway start
```

**Step 2: Restore Your Workspace**

**From GitHub:**
```bash
cd ~/.openclaw
rm -rf workspace  # Remove empty default workspace
git clone https://github.com/YOUR_USERNAME/openclaw-workspace.git workspace
```

**From Dropbox/Google Drive:**
```bash
# Copy back from Dropbox
cp -r ~/Dropbox/OpenClaw-Backup/workspace ~/.openclaw/
```

**From Time Machine:**
```bash
# During Mac setup: Use Migration Assistant
# Or: Restore from Time Machine browser
```

**From ZIP Archive:**
```bash
cd ~
tar -xzf openclaw-backup-20260205.tar.gz
```

**Step 3: Restore Configuration**
```bash
# Copy config back
cp ~/Dropbox/OpenClaw-Backup/openclaw.json ~/.openclaw/
cp -r ~/Dropbox/OpenClaw-Backup/credentials ~/.openclaw/

# Restart gateway
openclaw gateway restart
```

**Step 4: Reconnect Telegram**
```bash
# Telegram may need re-pairing
# Check status
openclaw status

# If needed, re-pair:
openclaw telegram pair
```

**Step 5: Verify Everything Works**
```bash
# Check workspace files
ls ~/.openclaw/workspace

# Check dashboard
open ~/.openclaw/workspace/home-concierge-dashboard-full.html

# Test connection
# Send yourself a Telegram message
```

**Total Recovery Time**: 30-60 minutes

---

## My Recommendation for You

**Best Setup (Hybrid Approach):**

1. **Git + GitHub for documents** (workspace without large media files)
   - Version control for text files, code, markdown
   - Easy to track changes
   - Fast syncing

2. **Dropbox for large files** (videos, images)
   - Keep `attachments/` folder in Dropbox
   - Link from workspace

3. **Time Machine for everything else**
   - Insurance policy for entire Mac
   - Backs up OpenClaw + everything else

**Implementation:**
```bash
# 1. Move attachments to Dropbox
mkdir -p ~/Dropbox/OpenClaw-Media
mv ~/.openclaw/workspace/attachments ~/Dropbox/OpenClaw-Media/
ln -s ~/Dropbox/OpenClaw-Media/attachments ~/.openclaw/workspace/attachments

# 2. Init git for workspace
cd ~/.openclaw/workspace
git init
cat > .gitignore << 'EOF'
attachments/
*.mp4
*.MOV
.DS_Store
EOF
git add .
git commit -m "Initial backup"

# 3. Create GitHub private repo and push
# (Follow GitHub instructions)

# 4. Backup config to Dropbox
cp ~/.openclaw/openclaw.json ~/Dropbox/OpenClaw-Media/

# 5. Set up Time Machine (if not already)
# System Settings → Time Machine → Add disk
```

---

## Automated Daily Backup Script

I'll create this for you:

```bash
#!/bin/bash
# Daily OpenClaw backup script
# Save as: ~/backup-openclaw-daily.sh

echo "🔄 Starting OpenClaw backup..."

# 1. Git commit workspace changes
cd ~/.openclaw/workspace
if [[ -n $(git status -s) ]]; then
  git add .
  git commit -m "Auto backup - $(date '+%Y-%m-%d %H:%M')"
  git push origin main
  echo "✅ Workspace pushed to GitHub"
else
  echo "✓ No workspace changes to commit"
fi

# 2. Backup config to Dropbox
cp ~/.openclaw/openclaw.json ~/Dropbox/OpenClaw-Media/openclaw-latest.json
cp ~/.openclaw/openclaw.json ~/Dropbox/OpenClaw-Media/openclaw-$(date +%Y%m%d).json
echo "✅ Config backed up to Dropbox"

# 3. Verify attachments symlink is working
if [[ -L ~/.openclaw/workspace/attachments ]]; then
  echo "✅ Attachments linked to Dropbox"
else
  echo "⚠️  Warning: Attachments not linked to Dropbox"
fi

echo "✅ Backup complete!"
```

**Run it manually:**
```bash
chmod +x ~/backup-openclaw-daily.sh
~/backup-openclaw-daily.sh
```

**Or schedule with cron (every night at 11 PM):**
```bash
# Add to crontab
(crontab -l 2>/dev/null; echo "0 23 * * * /Users/kimani/backup-openclaw-daily.sh >> /Users/kimani/openclaw-backup.log 2>&1") | crontab -
```

---

## Test Your Backup

**Verify it works BEFORE disaster strikes:**

```bash
# 1. Create test restore directory
mkdir ~/openclaw-test-restore
cd ~/openclaw-test-restore

# 2. Clone from GitHub
git clone https://github.com/YOUR_USERNAME/openclaw-workspace.git

# 3. Verify files are there
ls -la openclaw-workspace/
cat openclaw-workspace/AGENTS.md

# 4. Check backup dates
ls -lh ~/Dropbox/OpenClaw-Media/

# 5. Clean up test
rm -rf ~/openclaw-test-restore
```

**Test quarterly**: Set a reminder to verify backups work.

---

## Security Notes

### What's Safe to Back Up to Cloud:
- ✅ Workspace files (mostly safe, no raw passwords)
- ✅ Configuration with API keys (encrypted at rest by Dropbox/GitHub)
- ✅ Memory files, documents, dashboards

### What to Keep More Secure:
- 🔒 `credentials.json` - Contains raw passwords
  - Option 1: Encrypt before uploading
  - Option 2: Keep local backup on encrypted drive
  - Option 3: Use password manager (1Password, LastPass) as backup

**Encrypt sensitive files:**
```bash
# Before uploading credentials to cloud
tar -czf credentials.tar.gz ~/.openclaw/credentials
openssl enc -aes-256-cbc -salt -in credentials.tar.gz -out credentials-encrypted.tar.gz.enc
# Enter password when prompted
# Upload credentials-encrypted.tar.gz.enc to Dropbox
rm credentials.tar.gz

# To restore:
openssl enc -d -aes-256-cbc -in credentials-encrypted.tar.gz.enc -out credentials.tar.gz
tar -xzf credentials.tar.gz
```

---

## Quick Reference

### Backup Checklist
- [ ] Workspace → GitHub (daily auto-commit)
- [ ] Large files → Dropbox/Drive (continuous sync)
- [ ] Config → Dropbox (weekly manual copy)
- [ ] Full Mac → Time Machine (automatic)
- [ ] Test restore (quarterly)

### Critical Files to Never Lose
1. `~/.openclaw/workspace/` - All your work
2. `~/.openclaw/openclaw.json` - Configuration
3. `~/.openclaw/credentials/` - API keys & passwords
4. `~/.openclaw/skills/twilio-sms/` - Custom skill

### Recovery Priority
**Lost computer → New Mac:**
1. Install OpenClaw (10 min)
2. Restore workspace from GitHub (5 min)
3. Restore config from Dropbox (2 min)
4. Reconnect Telegram (5 min)
5. Test everything (10 min)

**Total**: 30 minutes to fully operational

---

**Next Steps**: Choose your backup strategy and I'll help you set it up!
