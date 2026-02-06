#!/bin/bash
# Automated GitHub backup script for OpenClaw workspace

WORKSPACE_DIR="$HOME/.openclaw/workspace"
LOG_FILE="$WORKSPACE_DIR/memory/backup-log.txt"

# Navigate to workspace
cd "$WORKSPACE_DIR" || exit 1

# Get current timestamp
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S %Z")

echo "[$TIMESTAMP] Starting automated backup..." >> "$LOG_FILE"

# Check if there are any changes
if git diff-index --quiet HEAD --; then
    echo "[$TIMESTAMP] No changes to backup" >> "$LOG_FILE"
    exit 0
fi

# Stage all changes (respecting .gitignore)
git add -A

# Commit with timestamp
git commit -m "Automated backup: $TIMESTAMP"

# Push to GitHub
if git push origin main; then
    echo "[$TIMESTAMP] ✅ Backup successful" >> "$LOG_FILE"
else
    echo "[$TIMESTAMP] ❌ Backup failed" >> "$LOG_FILE"
    exit 1
fi
