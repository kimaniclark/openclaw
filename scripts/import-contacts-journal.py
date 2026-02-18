#!/usr/bin/env python3
"""Import Contacts Journal CSV into the social CRM."""

import csv
import re
import os
from pathlib import Path

CSV_PATH = "/Users/kimani/.openclaw/media/inbound/7c88c797-2775-454c-86dd-78fa4c10686f.csv"
CONTACTS_DIR = Path("/Users/kimani/.openclaw/workspace/contacts")

def sanitize_filename(name):
    """Convert name to safe filename."""
    # Remove special chars, lowercase, replace spaces with hyphens
    name = name.strip().lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    return name

def format_location(street, city, state, postal, country, street2=None, city2=None, state2=None):
    """Format address into readable location."""
    parts = []
    if city and state:
        parts.append(f"{city}, {state}")
    elif city:
        parts.append(city)
    elif state:
        parts.append(state)
    if parts:
        return parts[0]
    return ""

def format_birthday(bday):
    """Format birthday string."""
    if not bday or bday.strip() == "":
        return ""
    # Format is like "May 12, 1" - incomplete year
    return bday.replace(", 1", "").strip()

def create_contact_md(row):
    """Create markdown content for a contact."""
    name = row['Name'].strip()
    first = row['First Name'].strip()
    last = row['Last Name'].strip() if row['Last Name'] else ""
    
    phone = row['Phone'].strip() if row['Phone'] else ""
    phone2 = row['Phone2'].strip() if row['Phone2'] else ""
    email = row['Email'].strip() if row['Email'] else ""
    email2 = row['Email2'].strip() if row['Email2'] else ""
    
    company = row['Company Name'].strip() if row['Company Name'] else ""
    
    location = format_location(
        row['Street'], row['City'], row['State'], row['Postal Code'], row['Country']
    )
    
    tags = row['Tags'].strip() if row['Tags'] else ""
    notes = row['Notes'].strip() if row['Notes'] else ""
    birthday = format_birthday(row['Birthday']) if row['Birthday'] else ""
    website = row['Website'].strip() if row['Website'] else ""
    
    # Build the markdown
    lines = [f"# {name}", ""]
    
    # Basic Info
    lines.append("## Basic Info")
    lines.append(f"- **Phone:** {phone}")
    if phone2:
        lines.append(f"- **Phone2:** {phone2}")
    lines.append(f"- **Email:** {email}")
    if email2:
        lines.append(f"- **Email2:** {email2}")
    lines.append(f"- **Location:** {location}")
    lines.append(f"- **Birthday:** {birthday}")
    lines.append(f"- **Met:** ")
    lines.append("")
    
    # Relationship
    lines.append("## Relationship")
    lines.append("- **Inner Circle:** yes")
    lines.append("- **Frequency:** 9-months")
    lines.append("- **Last Contact:** ")
    lines.append("- **Next Due:** ")
    lines.append("- **Meetup Type:** ")
    lines.append("- **Preferred Days:** ")
    lines.append("- **Their Spots:** ")
    lines.append(f"- **Tags:** {tags}")
    lines.append("")
    
    # Context
    lines.append("## Context")
    if company:
        lines.append(f"{company}")
    else:
        lines.append("")
    lines.append("")
    
    # Their World
    lines.append("## Their World")
    lines.append(f"- **Business/Work:** {company}")
    lines.append("- **Interests:** ")
    lines.append("- **Family:** ")
    if website:
        lines.append(f"- **Website:** {website}")
    lines.append("")
    
    # Notes
    lines.append("## Notes")
    if notes:
        lines.append(notes)
    else:
        lines.append("")
    lines.append("")
    
    # History
    lines.append("## History")
    lines.append("- [Date] - Imported from Contacts Journal")
    lines.append("")
    
    return "\n".join(lines)

def main():
    # Ensure contacts directory exists
    CONTACTS_DIR.mkdir(parents=True, exist_ok=True)
    
    imported = 0
    skipped = 0
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Name'].strip()
            if not name:
                skipped += 1
                continue
            
            filename = sanitize_filename(name) + ".md"
            filepath = CONTACTS_DIR / filename
            
            content = create_contact_md(row)
            
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(content)
            
            imported += 1
            print(f"✓ {name}")
    
    print(f"\n✅ Imported {imported} contacts")
    if skipped:
        print(f"⚠️ Skipped {skipped} empty rows")

if __name__ == "__main__":
    main()
