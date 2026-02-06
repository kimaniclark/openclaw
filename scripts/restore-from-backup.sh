#!/bin/bash
# Restore OpenClaw from encrypted backup

echo "🔄 OpenClaw Disaster Recovery"
echo "=============================="
echo ""

# Check if backup file provided
if [ -z "$1" ]; then
    echo "Usage: ./restore-from-backup.sh <path-to-encrypted-backup>"
    echo ""
    echo "Example:"
    echo "  ./restore-from-backup.sh ~/Dropbox/OpenClaw-Backups/credentials-backup-20260206-091500.tar.gz.enc"
    exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "📦 Backup file: $BACKUP_FILE"
echo ""
echo "Enter decryption password:"

# Create temp directory
TEMP_DIR=$(mktemp -d)

# Decrypt backup
openssl enc -aes-256-cbc -d -pbkdf2 -in "$BACKUP_FILE" -out "$TEMP_DIR/backup.tar.gz"

if [ $? -ne 0 ]; then
    echo "❌ Decryption failed - incorrect password?"
    rm -rf "$TEMP_DIR"
    exit 1
fi

# Extract files
cd "$TEMP_DIR" || exit 1
tar -xzf backup.tar.gz

echo ""
echo "✅ Backup decrypted successfully"
echo ""
echo "📁 Restoring files..."

# Restore credentials
if [ -f "credentials.json" ]; then
    mkdir -p "$HOME/.openclaw/workspace"
    cp credentials.json "$HOME/.openclaw/workspace/"
    echo "  ✅ credentials.json restored"
fi

# Restore OpenClaw config
if [ -f "openclaw-config.json" ]; then
    mkdir -p "$HOME/.openclaw"
    cp openclaw-config.json "$HOME/.openclaw/openclaw.json"
    echo "  ✅ openclaw.json restored"
fi

# Restore SSH keys
if [ -f "ssh-private-key" ]; then
    mkdir -p "$HOME/.ssh"
    cp ssh-private-key "$HOME/.ssh/id_ed25519"
    cp ssh-public-key.pub "$HOME/.ssh/id_ed25519.pub"
    chmod 600 "$HOME/.ssh/id_ed25519"
    chmod 644 "$HOME/.ssh/id_ed25519.pub"
    echo "  ✅ SSH keys restored"
fi

# Clean up
cd - > /dev/null
rm -rf "$TEMP_DIR"

echo ""
echo "✅ Restore complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Clone workspace: git clone git@github.com:kimaniclark/openclaw.git ~/.openclaw/workspace"
echo "   2. Restore media files (if needed): ./restore-media.sh <media-backup-file>"
echo "   3. Start OpenClaw: openclaw gateway start"
echo ""
