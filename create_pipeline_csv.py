import json
import csv
from datetime import datetime

# Read the contacts data
with open('/tmp/all_contacts.json', 'r') as f:
    data = json.load(f)

contacts = data.get('contacts', [])

# Create pipeline CSV for Closers.io/YourAtlas
output_file = 'modern-owner-complete-pipeline.csv'

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Headers for comprehensive pipeline
    writer.writerow([
        'First Name', 'Last Name', 'Phone', 'Email', 'Company', 
        'Tags', 'Source', 'Date Added', 'Last Activity', 'Status', 'Notes'
    ])
    
    for contact in contacts:
        # Basic info
        name = contact.get('name', '').strip()
        parts = name.split(' ', 1) if name else ['', '']
        first_name = parts[0] if parts else ''
        last_name = parts[1] if len(parts) > 1 else ''
        
        phone = contact.get('phone', '')
        email = contact.get('email', '')
        company = contact.get('companyName', '') or contact.get('businessName', '')
        
        # Additional data
        tags = ', '.join(contact.get('tags', []))
        source = contact.get('source', '')
        date_added = contact.get('dateAdded', '')
        last_activity = contact.get('lastActivityDate', '')
        
        # Custom fields that might be relevant
        custom_fields = contact.get('customFields', [])
        custom_data = []
        for field in custom_fields:
            if field.get('value'):
                custom_data.append(f"{field.get('name', 'Field')}: {field.get('value')}")
        
        # Create status based on available data
        status = "Lead"
        if contact.get('opportunityId'):
            status = "Opportunity"
        
        notes = f"Source: {source} | " + " | ".join(custom_data) if custom_data else f"Source: {source}"
        
        # Write row
        writer.writerow([
            first_name, last_name, phone, email, company,
            tags, source, date_added, last_activity, status, notes
        ])

print(f"✅ Complete pipeline exported: {output_file}")
print(f"📊 Total contacts: {len(contacts)}")

