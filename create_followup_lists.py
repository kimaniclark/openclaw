import csv
import json

# Stage IDs from the pipeline
APPOINTMENT_SCHEDULED = "be83cc6b-5866-4559-8288-32ff4a0fdffa"
NO_SHOW = "04c5d4f6-0d5d-479a-99a4-902ed52d7139"
ATTENDED_CALL = "503ee4ec-1b53-424d-8902-604b45bb4142"
NEEDED_RESCHEDULE = "a9418160-09f9-4cee-9b72-ce1b3e60ead5"

# Full opportunity data from API
opportunities = [
    {"name": "DaJuandrick Gardner", "email": "gardnerdajuandrick@gmail.com", "phone": "+15858838353", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Brandon Gerald", "email": "bdgjeg@gmail.com", "phone": "+19014030451", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "David Pillafo", "email": "xteriorspecialistsllc@gmail.com", "phone": "+17734543914", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Chinue Lee", "email": "manajwigs@gmail.com", "phone": "+13148998399", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Wendy Steinberg", "email": "wendysteinberg710@gmail.com", "phone": "+19514508375", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Troy Tennessee", "email": "2ratedx5@gmail.com", "phone": "+15807601457", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Andre Williams", "email": "jerseystylzbarbershopandsalon@gmail.com", "phone": "+19103087517", "stageId": "a9418160-09f9-4cee-9b72-ce1b3e60ead5"},
    {"name": "Brock Crowder", "email": "eliterelocationservices1@gmail.com", "phone": "+14042590418", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Aretha Brown", "email": "arethah25@gmail.com", "phone": "+13024151063", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Randy Williams", "email": "masterfencebuilderscolo@gmail.com", "phone": "+13039527677", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Shane Johnson", "email": "bittyjohnson54@gmail.com", "phone": "+19066317712", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Brandon Reed", "email": "bran88147@gmail.com", "phone": "+19362551126", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "VICTORIA Taylo", "email": "ba345gloate3@gmail.com", "phone": "+14084218472", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Tralen James", "email": "tralen38@gmail.com", "phone": "+13802325090", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Calvin Brooks", "email": "calvinbrooks598@gmail.com", "phone": "+16824669424", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "Herbert Metoyer", "email": "director@autonomousveterans.org", "phone": "+12487945405", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "Cathy Moore", "email": "showdowntalentagency@yahoo.com", "phone": "+15622786708", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Isaac Rodriguez Jr", "email": "newera_infinitedelivereesllc@yahoo.com", "phone": "+15514037530", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "John Smith", "email": "iamcrbaby2u@gmail.com", "phone": "+13136972053", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Jesse Yeager", "email": "yeagerj206@gmail.com", "phone": "+18034464530", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "Bruce Snider", "email": "bruce.snider123@gmail.com", "phone": "+16164385718", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Dustin Hadley", "email": "dhmobile2023@gmail.com", "phone": "+13608394690", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Tong Kim", "email": "tongkim0972@gmail.com", "phone": "+823478284100", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Geraldine White", "email": "whitegeraldine737@gmail.com", "phone": "+14754340477", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "Fazal Ghafar", "email": "fazal@tops-solution.com", "phone": "+16292555993", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "PRESIDENT TILWANA S COLSON", "email": "girltastyrichcountry@gmail.com", "phone": "+17137669884", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Diana Salamone", "email": "littlebarllc@gmail.com", "phone": "+15612011228", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Marcus Roe", "email": "roetreeandlogging0605@gmail.com", "phone": "+19363979656", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Sandra Hinton-McDowell", "email": "hintonsandra569@gmail.com", "phone": "+12164248439", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Joseph Marshall", "email": "joeymarshall0402@gmail.com", "phone": "+14199558087", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Nettie Sappington", "email": "nettie@totalhomesolutions.biz", "phone": "+19728498352", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Steve Nelson", "email": "steve@ever-seal.com", "phone": "+16155573080", "stageId": "f324c891-42d7-4a60-941b-d2b56caf77c9"},
    {"name": "Maurice Hollingsworth", "email": "hollingsworthmaurice572@gmail.com", "phone": "+17164289392", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Tom Shaw", "email": "tsshawcontractingservicellc@gmail.com", "phone": "+15154502497", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Moe Vickers", "email": "moevickers1@gmail.com", "phone": "+12818819660", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Karl Nieberlein", "email": "karl74@md-weightloss.com", "phone": "+14109353435", "stageId": "f324c891-42d7-4a60-941b-d2b56caf77c9"},
    {"name": "Orielle Turner", "email": "michellehairston91@gmail.com", "phone": "+12767321141", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Corey Wright", "email": "witgads@gmail.com", "phone": "+19163080784", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Curtis Howard", "email": "curtisepc@gmail.com", "phone": "+15592837697", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Lawrence Fairbanks", "email": "pricerightsecondhandstorestore@gmail.com", "phone": "+13162889219", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Robin Tapp", "email": "quality2769@gmail.com", "phone": "+15739419655", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Lina Phung", "email": "phunglina1@icloud.com", "phone": "+16575436565", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Tony Plesh", "email": "tony@pleshelectric.com", "phone": "+19089631637", "stageId": "9ebe4980-4ee9-4932-b103-57f9c36e5a75"},
    {"name": "Roshanda Casteel", "email": "roshandacasteel3@gmail.com", "phone": "+13238049834", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Branded dropshipping", "email": "myemailisgoogle@gmail.com", "phone": "+211938294729", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Lynette Cash", "email": "lynette.cash@freshstartcolo.com", "phone": "+17192501517", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Siva Kal", "email": "siva@intellisavvy.com", "phone": "+16287772889", "stageId": "a9418160-09f9-4cee-9b72-ce1b3e60ead5"},
    {"name": "Andrew Ender", "email": "andy@reviveautocaria.com", "phone": "+13192610999", "stageId": "f324c891-42d7-4a60-941b-d2b56caf77c9"},
    {"name": "Ann Crahan", "email": "ann@sanctuairemd.com", "phone": "+19259938149", "stageId": "f324c891-42d7-4a60-941b-d2b56caf77c9"},
    {"name": "Bethany James", "email": "bethanyjames052793@gmail.com", "phone": "+19412681162", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Trudy Sobocienski", "email": "tsobocienski@gmail.com", "phone": "+19074441778", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Justin Waggoner", "email": "jutwagg13@gmail.com", "phone": "+16128015828", "stageId": "be83cc6b-5866-4559-8288-32ff4a0fdffa"},
    {"name": "Corri Fields", "email": "corri@thewin-group.com", "phone": "+13108530106", "stageId": "bc9f735c-701f-4426-bce4-df42ed5d475b"},
    {"name": "Sonny Bathija", "email": "sonnylefacce@yahoo.com", "phone": "+13058147236", "stageId": "a9418160-09f9-4cee-9b72-ce1b3e60ead5"},
    {"name": "Josue Renteria", "email": "jkbr3k@gmail.com", "phone": "+15203392385", "stageId": "04c5d4f6-0d5d-479a-99a4-902ed52d7139"},
    {"name": "Jason Alford", "email": "jason@metrocomputerllc.com", "phone": "+14808613011", "stageId": "a9418160-09f9-4cee-9b72-ce1b3e60ead5"},
    {"name": "Uriah Lofton", "email": "loftonuriah63@gmail.com", "phone": "+14343286363", "stageId": "503ee4ec-1b53-424d-8902-604b45bb4142"},
    {"name": "Ivy Henderson", "email": "dominia187poisonivy@gmail.com", "phone": "+12533310043", "stageId": "fab09a1a-9269-4f2d-96a5-022a23a372bc"},
]

# Exclusions
exclude_names = {'justin waggoner', 'branded dropshipping'}
exclude_phones = {'+823478284100'}  # Tong Kim - international

def write_csv(filename, rows, list_name):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['First Name', 'Last Name', 'Phone', 'Email', 'Stage', 'Notes'])
        
        for opp in rows:
            name = opp['name'].strip()
            
            # Skip excluded
            if name.lower() in exclude_names:
                print(f"  Skipped: {name}")
                continue
            if opp['phone'] in exclude_phones:
                print(f"  Skipped (intl): {name}")
                continue
            
            # Split name
            parts = name.split(' ', 1)
            first = parts[0]
            last = parts[1] if len(parts) > 1 else ''
            
            # Stage name for notes
            stage_names = {
                APPOINTMENT_SCHEDULED: "Appointment Scheduled",
                NO_SHOW: "No Show",
                ATTENDED_CALL: "Attended Call",
                NEEDED_RESCHEDULE: "Needed To Reschedule"
            }
            stage = stage_names.get(opp['stageId'], 'Unknown')
            
            writer.writerow([first, last, opp['phone'], opp['email'], stage, f"Stage: {stage}"])
    
    print(f"✅ {list_name}: {len(rows)} records → {filename}")

# LIST 2: Booked but never spoke (Appointment Scheduled + No Show)
list2 = [o for o in opportunities if o['stageId'] in [APPOINTMENT_SCHEDULED, NO_SHOW]]
print("\n📋 LIST 2: Booked but never spoke")
write_csv('modern-owner-booked-never-spoke.csv', list2, "Booked Never Spoke")

# LIST 3: Talked to briefly (Attended Call + Needed Reschedule)
list3 = [o for o in opportunities if o['stageId'] in [ATTENDED_CALL, NEEDED_RESCHEDULE]]
print("\n📋 LIST 3: Talked to briefly")
write_csv('modern-owner-talked-briefly.csv', list3, "Talked Briefly")

