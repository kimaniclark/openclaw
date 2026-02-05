#!/bin/bash
# Daily OpenClaw backup script

echo "🔄 Starting OpenClaw backup..."

# 1. Git commit workspace changes (if git is set up)
if [[ -d ~/.openclaw/workspace/.git ]]; then
  cd ~/.openclaw/workspace
  if [[ -n $(git status -s) ]]; then
    git add .
    git commit -m "Auto backup - $(date '+%Y-%m-%d %H:%M')"
    git push origin main
    echo "✅ Workspace pushed to GitHub"
  else
    echo "✓ No workspace changes to commit"
  fi
else
  echo "⚠️  Git not initialized - run: cd ~/.openclaw/workspace && git init"
fi

# 2. Create dated ZIP backup
BACKUP_DIR=~/Documents/OpenClaw-Backups
mkdir -p "$BACKUP_DIR"
BACKUP_FILE="$BACKUP_DIR/openclaw-$(date +%Y%m%d-%H%M).tar.gz"

cd ~
tar -czf "$BACKUP_FILE" \
  .openclaw/workspace \
  .openclaw/openclaw.json \
  .openclaw/credentials \
  .openclaw/skills 2>/dev/null

echo "✅ Backup saved: $BACKUP_FILE"

# 3. Keep only last 7 days of backups
find "$BACKUP_DIR" -name "openclaw-*.tar.gz" -mtime +7 -delete
echo "✅ Old backups cleaned up (keeping 7 days)"

# 4. Display backup size
du -sh "$BACKUP_FILE"

echo "✅ Backup complete!"
