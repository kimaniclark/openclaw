import csv

input_file = 'modern-owner-cold-leads-cleaned.csv'
output_file = 'modern-owner-cold-leads-final.csv'

# Questionable entries to remove (by email)
exclude_emails = {
    'anthonyhellmaberry@hottmale.com',
    'www.fooon123690@gmail.com',
    'claudiaagudelo10@gmail.com',
}

final_rows = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    
    for row in reader:
        email = row['Email'].strip().lower()
        if email in exclude_emails:
            print(f"Removed: {row['First Name']} {row['Last Name']} ({email})")
            continue
        final_rows.append(row)

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(final_rows)

print(f"\n✅ Final list: {len(final_rows)} leads")
print(f"📁 Saved to: {output_file}")

