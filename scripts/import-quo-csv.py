#!/usr/bin/env python3
"""Import Quo CSV export with roles from screenshots."""

import csv
import re
from pathlib import Path

CSV_PATH = "/Users/kimani/.openclaw/media/inbound/2a0243b1-86a9-4f81-8bf6-edf34520e6ab.csv"
CONTACTS_DIR = Path("/Users/kimani/.openclaw/workspace/contacts")

# Roles observed from screenshots
ROLES = {
    "alexana larosa": "Friend",
    "andrew effross": "Barter Saves Representative",
    "barry graham": "Friend",
    "burrell": "Tailor",
    "carla": "Friend",
    "chad clark": "Kimani's Brother",
    "chris hammond": "Friend",
    "cynthia vidal": "Condo Cleaning",
    "david solomon": "Flowtract.co",
    "dr. joe kravitz's office": "Dentist at Kravitz Dentistry",
    "gwokang yang": "Friend",
    "henry vidal": "Cleaner/Cynthia's Husband/Contractor",
    "james kopcie": "Kimani's Bookeeper",
    "james meager": "Long-time Friend",
    "jason- quantum coaching": "Jason- Quantum Coaching",
    "jessica larosa": "Friend",
    "jonathan": "Car Wash at Exec Auto",
    "jorge rodriguez": "Prime Corporate Services",
    "josh marks": "Friend",
    "josh thomas": "Modeling Agency Photographer",
    "keith r.": "Costello's Hearth and Spa",
    "kevin fahey": "Kimani's Friend",
    "lu molenje": "Friend",
    "maria": "Alt Condo Assistant",
    "matt garcell": "Commercial real estate broker",
    "mitch": "Long Time Friend",
    "openphone team": "Support at OpenPhone",
    "rob": "Friend",
    "roop sood": "CEO at Fifth Weapon",
    "tony graham": "Friend",
    "victoria kulicheva": "Business partner / Friend",
    "adam schneider": "Friend",
}

def sanitize_filename(name):
    name = name.strip().lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    return name

def create_contact_md(row):
    first = row['firstName'].strip() if row['firstName'] else ""
    last = row['lastName'].strip() if row['lastName'] else ""
    company = row['company'].strip() if row['company'] else ""
    
    # Build name
    if first or last:
        name = f"{first} {last}".strip()
    elif company:
        name = company
    else:
        return None, None
    
    # Skip "Kimani" entry (that's you)
    if name.lower() == "kimani":
        return None, None
    
    phone = row['phone_number_1'].strip() if row['phone_number_1'] else ""
    phone2 = row['phone_number_2'].strip() if row['phone_number_2'] else ""
    email = row['email_1'].strip() if row['email_1'] else ""
    
    # Get role from our mapping
    role = ROLES.get(name.lower(), "")
    
    # Check if CSV has tags
    tags = row.get('custom_1_Tags', '')
    if '[\"Friend\"]' in str(tags):
        role = role or "Friend"
    
    # Get address if present
    address = row.get('custom_2_Address', '')
    
    lines = [f"# {name}", ""]
    
    lines.append("## Basic Info")
    lines.append(f"- **Phone:** {phone}")
    if phone2:
        lines.append(f"- **Phone2:** {phone2}")
    lines.append(f"- **Email:** {email}")
    lines.append(f"- **Location:** {address if address else ''}")
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
    elif company:
        lines.append(company)
    lines.append("")
    
    lines.append("## Their World")
    lines.append(f"- **Business/Work:** {company}")
    lines.append("- **Interests:** ")
    lines.append("- **Family:** ")
    lines.append("")
    
    lines.append("## Notes")
    lines.append("Contacted via assistant in the past")
    lines.append("")
    
    lines.append("## History")
    lines.append("- [Date] - Imported from Quo (OpenPhone)")
    lines.append("")
    
    return name, "\n".join(lines)

def main():
    CONTACTS_DIR.mkdir(parents=True, exist_ok=True)
    
    imported = 0
    skipped_inner = 0
    skipped_other = 0
    updated = 0
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name, content = create_contact_md(row)
            
            if not name:
                skipped_other += 1
                continue
            
            filename = sanitize_filename(name) + ".md"
            filepath = CONTACTS_DIR / filename
            
            if filepath.exists():
                with open(filepath, 'r') as ef:
                    existing = ef.read()
                if "Inner Circle:** yes" in existing:
                    print(f"⏭ {name} (inner circle - kept)")
                    skipped_inner += 1
                    continue
                else:
                    updated += 1
                    print(f"↻ {name} (updated with role)")
            else:
                imported += 1
                print(f"✓ {name}")
            
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(content)
    
    print(f"\n✅ Imported {imported} new contacts")
    print(f"↻ Updated {updated} contacts")
    print(f"⏭ Skipped {skipped_inner} inner circle")
    print(f"⏭ Skipped {skipped_other} empty/self")

if __name__ == "__main__":
    main()
