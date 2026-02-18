#!/usr/bin/env python3
"""Import Quo contacts from JSON files."""

import json
import re
from pathlib import Path
import glob

CONTACTS_DIR = Path("/Users/kimani/.openclaw/workspace/contacts")

def sanitize_filename(name):
    name = name.strip().lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    return name

def create_contact_md(contact):
    fields = contact.get("defaultFields", {})
    
    first = fields.get("firstName") or ""
    last = fields.get("lastName") or ""
    name = f"{first} {last}".strip()
    
    if not name:
        company = fields.get("company") or ""
        name = company if company else None
    
    if not name:
        return None, None
    
    phones = fields.get("phoneNumbers", [])
    phone = phones[0]["value"] if phones else ""
    phone2 = phones[1]["value"] if len(phones) > 1 else ""
    
    emails = fields.get("emails", [])
    email = emails[0]["value"] if emails else ""
    
    company = fields.get("company") or ""
    role = fields.get("role") or ""
    
    custom = contact.get("customFields", [])
    notes_parts = []
    for cf in custom:
        if cf.get("value"):
            notes_parts.append(f"{cf.get('name', 'Note')}: {cf.get('value')}")
    custom_notes = "\n".join(notes_parts)
    
    lines = [f"# {name}", ""]
    
    lines.append("## Basic Info")
    lines.append(f"- **Phone:** {phone}")
    if phone2:
        lines.append(f"- **Phone2:** {phone2}")
    lines.append(f"- **Email:** {email}")
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
    lines.append(f"- **Tags:** {role}")
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
    
    all_contacts = []
    for f in glob.glob("/tmp/quo_contacts_*.json"):
        try:
            with open(f) as fp:
                data = json.load(fp)
                if "data" in data:
                    all_contacts.extend(data["data"])
        except:
            pass
    
    print(f"Processing {len(all_contacts)} contacts from Quo")
    
    imported = 0
    skipped = 0
    
    for contact in all_contacts:
        name, content = create_contact_md(contact)
        
        if not name:
            skipped += 1
            continue
        
        filename = sanitize_filename(name) + ".md"
        filepath = CONTACTS_DIR / filename
        
        if filepath.exists():
            with open(filepath, 'r') as f:
                existing = f.read()
            if "Inner Circle:** yes" in existing:
                print(f"⏭ {name} (inner circle)")
                skipped += 1
                continue
        
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(content)
        
        imported += 1
        print(f"✓ {name}")
    
    print(f"\n✅ Imported {imported} contacts from Quo")
    print(f"⏭ Skipped {skipped}")

if __name__ == "__main__":
    main()
