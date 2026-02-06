#!/bin/bash
# Automatically sync backups to Dropbox

BACKUP_SOURCE="$HOME/.openclaw/workspace/backups"
DROPBOX_DEST="$HOME/Dropbox/OpenClaw-Backups"

echo "📤 Syncing backups to Dropbox..."

# Check if Dropbox folder exists
if [ ! -d "$HOME/Dropbox" ]; then
    echo "❌ Dropbox folder not found at $HOME/Dropbox"
    echo "   Make sure Dropbox is installed and syncing"
    exit 1
fi

# Create OpenClaw-Backups folder in Dropbox
mkdir -p "$DROPBOX_DEST/credentials"
mkdir -p "$DROPBOX_DEST/media"

# Sync encrypted credentials backups
if [ -d "$BACKUP_SOURCE/secure" ]; then
    echo "  📁 Syncing credentials backups..."
    rsync -av --progress "$BACKUP_SOURCE/secure/"*.tar.gz.enc "$DROPBOX_DEST/credentials/" 2>/dev/null
    CRED_COUNT=$(ls "$DROPBOX_DEST/credentials/"*.tar.gz.enc 2>/dev/null | wc -l)
    echo "  ✅ $CRED_COUNT credential backup(s) in Dropbox"
fi

# Sync media backups
if [ -d "$BACKUP_SOURCE/media" ]; then
    echo "  📁 Syncing media backups..."
    rsync -av --progress "$BACKUP_SOURCE/media/"*.tar.gz "$DROPBOX_DEST/media/" 2>/dev/null
    MEDIA_COUNT=$(ls "$DROPBOX_DEST/media/"*.tar.gz 2>/dev/null | wc -l)
    echo "  ✅ $MEDIA_COUNT media backup(s) in Dropbox"
fi

echo ""
echo "✅ Dropbox sync complete!"
echo "📂 Backups location: $DROPBOX_DEST"
echo ""
echo "💡 Dropbox will automatically sync to the cloud"
