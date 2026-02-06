#!/bin/bash
# Backup large media files (videos, photos, attachments)

WORKSPACE_DIR="$HOME/.openclaw/workspace"
BACKUP_DIR="$WORKSPACE_DIR/backups/media"
TIMESTAMP=$(date "+%Y%m%d-%H%M%S")

# Create backup directory
mkdir -p "$BACKUP_DIR"

echo "📸 Backing up media files..."

# Find all media directories
MEDIA_DIRS=(
    "attachments"
    "heavy-duty-videos"
    "$HOME/.openclaw/media"
)

BACKUP_FILE="$BACKUP_DIR/media-backup-$TIMESTAMP.tar.gz"

# Create tarball of all media
cd "$WORKSPACE_DIR" || exit 1

# Build list of directories that exist
EXISTING_DIRS=()
for dir in "${MEDIA_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        EXISTING_DIRS+=("$dir")
    fi
done

if [ ${#EXISTING_DIRS[@]} -eq 0 ]; then
    echo "⚠️  No media directories found to backup"
    exit 0
fi

echo "Compressing media files..."
tar -czf "$BACKUP_FILE" "${EXISTING_DIRS[@]}" 2>/dev/null

if [ -f "$BACKUP_FILE" ]; then
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo ""
    echo "✅ Media backup created: $BACKUP_FILE"
    echo "📦 File size: $SIZE"
    echo ""
    echo "📤 Next steps:"
    echo "   1. Upload to Dropbox: ~/Dropbox/OpenClaw-Backups/"
    echo "   2. Or copy to external drive"
    echo ""
    echo "💡 Tip: This file is NOT encrypted (media files aren't secret)"
else
    echo "❌ Media backup failed"
    exit 1
fi
