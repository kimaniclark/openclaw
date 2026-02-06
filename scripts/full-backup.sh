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

echo "✅ Complete backup finished!"
echo ""
echo "📤 TODO: Upload these files to Dropbox or external drive:"
echo "   • backups/secure/credentials-backup-*.tar.gz.enc (ENCRYPTED - contains secrets)"
echo "   • backups/media/media-backup-*.tar.gz (large files - photos/videos)"
echo ""
echo "💡 GitHub backup is automatic (workspace code already synced)"
