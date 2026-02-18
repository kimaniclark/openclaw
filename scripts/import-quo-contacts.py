#!/usr/bin/env python3
"""Import Quo/OpenPhone contacts into the broader CRM."""

import json
import re
import os
import urllib.request
from pathlib import Path

API_KEY = "iRyHq1zGyJdn9eGZIVfAGKIgSRaQuTmw"
API_URL = "https://api.openphone.com/v1/contacts"
CONTACTS_DIR = Path("/Users/kimani/.openclaw/workspace/contacts")

def sanitize_filename(name):
    """Convert name to safe filename."""
    name = name.strip().lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    return name

def fetch_all_contacts():
    """Fetch all contacts from Quo API with pagination."""
    all_contacts = []
    next_token = None
    
    while True:
        url = API_URL
        if next_token:
            url += f"?pageToken={next_token}"
        
        req = urllib.request.Request(url)
        req.add_header("Authorization", API_KEY)
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        
        all_contacts.extend(data.get("data", []))
        next_token = data.get("nextPageToken")
        
        if not next_token:
            break
    
    return all_contacts

def create_contact_md(contact):
    """Create markdown content for a Quo contact."""
    fields = contact.get("defaultFields", {})
    
    first = fields.get("firstName") or ""
    last = fields.get("lastName") or ""
    name = f"{first} {last}".strip()
    
    if not name:
        company = fields.get("company") or ""
        name = company if company else "Unknown"
    
    # Phone numbers
    phones = fields.get("phoneNumbers", [])
    phone = phones[0]["value"] if phones else ""
    phone2 = phones[1]["value"] if len(phones) > 1 else ""
    
    # Emails
    emails = fields.get("emails", [])
    email = emails[0]["value"] if emails else ""
    email2 = emails[1]["value"] if len(emails) > 1 else ""
    
    company = fields.get("company") or ""
    role = fields.get("role") or ""
    
    # Custom fields
    custom = contact.get("customFields", [])
    notes_parts = []
    for cf in custom:
        if cf.get("value"):
            notes_parts.append(f"{cf.get('name', 'Note')}: {cf.get('value')}")
    custom_notes = "\n".join(notes_parts)
    
    # Build markdown
    lines = [f"# {name}", ""]
    
    lines.append("## Basic Info")
    lines.append(f"- **Phone:** {phone}")
    if phone2:
        lines.append(f"- **Phone2:** {phone2}")
    lines.append(f"- **Email:** {email}")
    if email2:
        lines.append(f"- **Email2:** {email2}")
    lines.append("- **Location:** ")
    lines.append("- **Birthday:** ")
    lines.append("- **Met:** ")
    lines.append("")
    
    lines.append("## Relationship")
    lines.append("- **Inner Circle:** no")
    lines.append("- **Frequency:** ")
    lines.append("- **Last Contact:** ")
    lines.append("- **Next Due:** ")
    lines.append("- **Meetup Type:** ")
    lines.append("- **Preferred Days:** ")
    lines.append("- **Their Spots:** ")
    if role:
        lines.append(f"- **Tags:** {role}")
    else:
        lines.append("- **Tags:** ")
    lines.append("")
    
    lines.append("## Context")
    if role:
        lines.append(role)
    lines.append("")
    
    lines.append("## Their World")
    lines.append(f"- **Business/Work:** {company}")
    lines.append("- **Interests:** ")
    lines.append("- **Family:** ")
    lines.append("")
    
    lines.append("## Notes")
    if custom_notes:
        lines.append(custom_notes)
    lines.append("")
    
    lines.append("## History")
    lines.append("- [Date] - Imported from Quo (OpenPhone)")
    lines.append("")
    
    return name, "\n".join(lines)

def main():
    CONTACTS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Fetching contacts from Quo API...")
    contacts = fetch_all_contacts()
    print(f"Found {len(contacts)} contacts")
    
    imported = 0
    skipped = 0
    updated = 0
    
    for contact in contacts:
        name, content = create_contact_md(contact)
        
        if not name or name == "Unknown":
            skipped += 1
            continue
        
        filename = sanitize_filename(name) + ".md"
        filepath = CONTACTS_DIR / filename
        
        # Check if already exists (from CJournal import)
        if filepath.exists():
            # Don't overwrite inner circle contacts
            with open(filepath, 'r') as f:
                existing = f.read()
            if "Inner Circle:** yes" in existing:
                print(f"⏭ {name} (already in inner circle)")
                skipped += 1
                continue
            else:
                updated += 1
                print(f"↻ {name} (updated)")
        else:
            imported += 1
            print(f"✓ {name}")
        
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(content)
    
    print(f"\n✅ Imported {imported} new contacts")
    print(f"↻ Updated {updated} existing contacts")
    print(f"⏭ Skipped {skipped} (inner circle or empty)")

if __name__ == "__main__":
    main()
