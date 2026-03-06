import csv
import re

# Opportunity board contacts (from API) - normalized emails
opportunity_emails = {
    "gardnerdajuandrick@gmail.com",
    "bdgjeg@gmail.com",
    "xteriorspecialistsllc@gmail.com",
    "manajwigs@gmail.com",
    "wendysteinberg710@gmail.com",
    "2ratedx5@gmail.com",
    "jerseystylzbarbershopandsalon@gmail.com",
    "eliterelocationservices1@gmail.com",
    "arethah25@gmail.com",
    "masterfencebuilderscolo@gmail.com",
    "bittyjohnson54@gmail.com",
    "bran88147@gmail.com",
    "ba345gloate3@gmail.com",
    "tralen38@gmail.com",
    "calvinbrooks598@gmail.com",
    "director@autonomousveterans.org",
    "showdowntalentagency@yahoo.com",
    "newera_infinitedelivereesllc@yahoo.com",
    "iamcrbaby2u@gmail.com",
    "yeagerj206@gmail.com",
    "bruce.snider123@gmail.com",
    "dhmobile2023@gmail.com",
    "tongkim0972@gmail.com",
    "whitegeraldine737@gmail.com",
    "fazal@tops-solution.com",
    "girltastyrichcountry@gmail.com",
    "littlebarllc@gmail.com",
    "roetreeandlogging0605@gmail.com",
    "hintonsandra569@gmail.com",
    "joeymarshall0402@gmail.com",
    "nettie@totalhomesolutions.biz",
    "steve@ever-seal.com",
    "hollingsworthmaurice572@gmail.com",
    "tsshawcontractingservicellc@gmail.com",
    "moevickers1@gmail.com",
    "karl74@md-weightloss.com",
    "michellehairston91@gmail.com",
    "witgads@gmail.com",
    "curtisepc@gmail.com",
    "pricerightsecondhandstorestore@gmail.com",
    "quality2769@gmail.com",
    "phunglina1@icloud.com",
    "tony@pleshelectric.com",
    "roshandacasteel3@gmail.com",
    "myemailisgoogle@gmail.com",
    "lynette.cash@freshstartcolo.com",
    "siva@intellisavvy.com",
    "andy@reviveautocaria.com",
    "ann@sanctuairemd.com",
    "bethanyjames052793@gmail.com",
    "tsobocienski@gmail.com",
    "jutwagg13@gmail.com",
    "corri@thewin-group.com",
    "sonnylefacce@yahoo.com",
    "jkbr3k@gmail.com",
    "jason@metrocomputerllc.com",
    "loftonuriah63@gmail.com",
    "dominia187poisonivy@gmail.com",
    # Additional variations/alternate emails from opportunities
    "fazalrabigkhan13@gmail.com",  # Fazal Ghafar alternate
    "taylovict@gmail.com",  # Victoria Taylor alternate
    "cathymitchell2024@gmail.com",  # Cathy Moore alternate
    "director@automousveterans.org",  # Herbert Metoyer
    "eliteempireautospa@gmail.com",  # Dustin Hadley
    "tgshawfixitall@gmail.com",  # Tom Shaw alternate
}

# Also match by phone (normalized - just digits)
opportunity_phones = {
    "15858838353", "15858830353",  # DaJuandrick Gardner
    "19014030451",  # Brandon Gerald
    "17734543914",  # David Pillado
    "13148998399",  # Chinue
    "19514508375",  # Wendy
    "15807601457",  # Troy Tennessee
    "19103087517",  # Andre Williams
    "14042590418",  # Brock Crowder
    "13024151063",  # Aretha Brown
    "13039527677", "17203930263",  # Randy/Antonio Williams
    "19066317712",  # Shane Johnson
    "19362551126",  # Brandon Reed
    "14084218472",  # Victoria Taylo
    "13802325090",  # Tralen James
    "16824669424",  # Calvin Brooks
    "12487945405",  # Herbert Metoyer
    "15622786708",  # Cathy Moore
    "15514037530",  # Isaac Rodriguez
    "13136972053",  # John Smith
    "18034464530",  # Jesse Yeager
    "16164385718",  # Bruce Snider
    "13608394690",  # Dustin Hadley
    "13478284100",  # Tong Kim
    "14754340477",  # Geraldine White
    "16152529091", "16292555993",  # Fazal Ghafar
    "17137669884",  # Tilwana Colson
    "15612011228",  # Diana Salamone
    "19363979656",  # Marcus Roe
    "12164248439",  # Sandra Hinton-McDowell
    "14199558087",  # Joseph Marshall
    "19728498352",  # Nettie Sappington
    "16155573080",  # Steve Nelson
    "17164289392",  # Maurice Hollingsworth
    "15154502497",  # Tom Shaw
    "12818819660",  # Moe Vickers
    "14109353435",  # Karl Nieberlein
    "12767321141",  # Orielle Turner
    "19163080784",  # Corey Wright
    "15592837697",  # Curtis Howard
    "13162889219",  # Lawrence Fairbanks
    "15739419655",  # Robin Tapp
    "16575436565",  # Lina Phung
    "19089631637",  # Tony Plesh
    "13238049834",  # Roshanda Casteel
    "17192501517",  # Lynette Cash
    "16287772889",  # Siva K
    "13195737620", "13192610999",  # Andrew Ender
    "19259938149",  # Ann Crahan
    "19412681162",  # Bethany James
    "19074441778",  # Trudy Sobocienski
    "16128015828",  # Justin Waggoner
    "13108530106",  # Corri Fields
    "13058147236",  # Sonny Bathija
    "15203392385",  # Josue Renteria
    "14808613011",  # Jason Alford
    "14343286363",  # Uriah Lofton
    "12533310043",  # Ivy Henderson
}

def normalize_email(email):
    return email.lower().strip() if email else ""

def normalize_phone(phone):
    # Extract just digits
    return re.sub(r'[^0-9]', '', phone) if phone else ""

# Read and filter
input_file = '/Users/kimani/.openclaw/media/inbound/5dd71657-3018-494a-b09d-24751cf9fb73.csv'
output_file = 'modern-owner-cold-leads.csv'

filtered_rows = []
header = None
excluded = []
test_entries = []  # Track test/fake entries

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for row in reader:
        if len(row) < 3:
            continue
        
        name = row[0].strip()
        phone = row[1]
        email = row[2]
        
        norm_email = normalize_email(email)
        norm_phone = normalize_phone(phone)
        
        # Skip if on opportunity board
        if norm_email in opportunity_emails or norm_phone[-10:] in {p[-10:] for p in opportunity_phones}:
            excluded.append(name)
            continue
        
        # Skip test/fake entries
        if 'test' in name.lower() or 'test@' in norm_email or 'idonthave' in norm_email or norm_email == 'bob@gmail.com':
            test_entries.append(name)
            continue
        
        # Skip Keaton (partner, not a real lead)
        if 'keaton' in name.lower():
            test_entries.append(name)
            continue
        
        filtered_rows.append(row)

# Write output CSV with columns needed for YourAtlas
# YourAtlas likely needs: Name, Phone, Email, and optionally business info
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write simplified header for calling campaign
    writer.writerow(['Full Name', 'Phone', 'Email', 'Business Name', 'Monthly Revenue', 'Biggest Challenge', 'Submission Date'])
    
    for row in filtered_rows:
        # Full Name, Phone, Email, Business Name (col 12), Revenue (col 11), Challenge (col 5), Date (col 16)
        business_name = row[12] if len(row) > 12 else row[3] if len(row) > 3 else ""
        revenue = row[11] if len(row) > 11 else ""
        challenge = row[5] if len(row) > 5 else ""
        date = row[16] if len(row) > 16 else ""
        writer.writerow([row[0], row[1], row[2], business_name, revenue, challenge, date])

print(f"Total submissions: {len(filtered_rows) + len(excluded) + len(test_entries)}")
print(f"Excluded (on opportunity board): {len(excluded)}")
print(f"Test/partner entries skipped: {len(test_entries)}")
print(f"Cold leads (no call booked): {len(filtered_rows)}")
print(f"\nOutput saved to: {output_file}")

