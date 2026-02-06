#!/bin/bash
# Secure encrypted backup of credentials and sensitive config

WORKSPACE_DIR="$HOME/.openclaw/workspace"
BACKUP_DIR="$WORKSPACE_DIR/backups/secure"
TIMESTAMP=$(date "+%Y%m%d-%H%M%S")
BACKUP_FILE="$BACKUP_DIR/credentials-backup-$TIMESTAMP.tar.gz.enc"

# Create backup directory
mkdir -p "$BACKUP_DIR"

echo "🔐 Creating secure credentials backup..."

# Create temporary directory for backup
TEMP_DIR=$(mktemp -d)

# Copy credentials and sensitive files
cp "$WORKSPACE_DIR/credentials.json" "$TEMP_DIR/" 2>/dev/null || echo "⚠️  credentials.json not found"
cp "$HOME/.openclaw/openclaw.json" "$TEMP_DIR/openclaw-config.json" 2>/dev/null || echo "⚠️  openclaw.json not found"
cp "$HOME/.ssh/id_ed25519" "$TEMP_DIR/ssh-private-key" 2>/dev/null || echo "⚠️  SSH key not found"
cp "$HOME/.ssh/id_ed25519.pub" "$TEMP_DIR/ssh-public-key.pub" 2>/dev/null || echo "⚠️  SSH public key not found"

# Create tarball
cd "$TEMP_DIR" || exit 1
tar -czf backup.tar.gz *

# Encrypt with password
echo ""
echo "Enter encryption password (you'll need this to restore):"
openssl enc -aes-256-cbc -salt -pbkdf2 -in backup.tar.gz -out "$BACKUP_FILE"

# Clean up temp files
cd - > /dev/null
rm -rf "$TEMP_DIR"

if [ -f "$BACKUP_FILE" ]; then
    echo ""
    echo "✅ Secure backup created: $BACKUP_FILE"
    echo "📦 File size: $(du -h "$BACKUP_FILE" | cut -f1)"
    echo ""
    echo "⚠️  IMPORTANT: Save this file to Dropbox or external drive!"
    echo "⚠️  Remember your encryption password - you can't recover without it!"
else
    echo "❌ Backup failed"
    exit 1
fi
