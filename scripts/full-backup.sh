#!/bin/bash
# Complete backup: GitHub + Encrypted Credentials + Media Files

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 OpenClaw Complete Backup System"
echo "==================================="
echo ""

# Step 1: GitHub backup
echo "1️⃣  Backing up workspace to GitHub..."
"$SCRIPT_DIR/backup-to-github.sh"
echo ""

# Step 2: Encrypted credentials backup
echo "2️⃣  Creating encrypted credentials backup..."
"$SCRIPT_DIR/backup-credentials.sh"
echo ""

# Step 3: Media files backup
echo "3️⃣  Backing up media files..."
"$SCRIPT_DIR/backup-media.sh"
echo ""

# Step 4: Sync to Dropbox
echo "4️⃣  Syncing backups to Dropbox..."
"$SCRIPT_DIR/sync-to-dropbox.sh"
echo ""

echo "✅ Complete backup finished!"
echo ""
echo "📍 Your backups are now in:"
echo "   • GitHub: workspace code (automatic)"
echo "   • Dropbox: ~/Dropbox/OpenClaw-Backups/ (encrypted + media)"
echo ""
echo "💡 Dropbox will automatically sync to the cloud"
