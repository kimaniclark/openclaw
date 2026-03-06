import csv

input_file = 'modern-owner-cold-leads.csv'
output_file = 'modern-owner-cold-leads-cleaned.csv'

# Track seen phones/emails for deduplication
seen_phones = set()
seen_emails = set()
cleaned_rows = []

# Names to exclude
exclude_names = {
    'dolores hirschmann',  # Business partner from Epic Network
}

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        name = row['Full Name'].strip()
        phone = row['Phone'].strip()
        email = row['Email'].strip().lower()
        
        # Skip excluded names
        if name.lower() in exclude_names:
            print(f"Excluded (partner): {name}")
            continue
        
        # Skip duplicates by phone (use last 10 digits)
        phone_key = phone[-10:] if len(phone) >= 10 else phone
        if phone_key in seen_phones:
            print(f"Duplicate skipped: {name} ({phone})")
            continue
        
        # Skip duplicates by email
        if email in seen_emails and email:
            print(f"Duplicate skipped (email): {name} ({email})")
            continue
        
        seen_phones.add(phone_key)
        if email:
            seen_emails.add(email)
        
        cleaned_rows.append(row)

# Write cleaned output - YourAtlas-friendly format
# Most AI calling platforms want: First Name, Last Name, Phone, Email, Notes
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Common calling platform headers
    writer.writerow(['First Name', 'Last Name', 'Phone', 'Email', 'Company', 'Notes'])
    
    for row in cleaned_rows:
        full_name = row['Full Name'].strip()
        # Split name into first/last
        parts = full_name.split(' ', 1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ''
        
        # Create notes with context for the AI caller
        business = row['Business Name'].strip()
        revenue = row['Monthly Revenue'].strip()
        challenge = row['Biggest Challenge'].strip()
        
        notes_parts = []
        if business:
            notes_parts.append(f"Business: {business}")
        if revenue:
            notes_parts.append(f"Revenue: {revenue}")
        if challenge:
            notes_parts.append(f"Challenge: {challenge}")
        
        notes = " | ".join(notes_parts)
        
        writer.writerow([
            first_name,
            last_name,
            row['Phone'],
            row['Email'],
            business,
            notes
        ])

print(f"\n✅ Cleaned list: {len(cleaned_rows)} leads")
print(f"📁 Saved to: {output_file}")

