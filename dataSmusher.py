import json

# Load data from output_ips.json
with open('/Users/oliver/Desktop/Github/Triangulator/output_ips.json', 'r') as file:
    output_ips = json.load(file)

# Load data from quickIps.json
with open('/Users/oliver/Desktop/Github/Triangulator/quickIPs.json', 'r') as file:
    quick_ips = json.load(file)

# Combine data where IPs match
final_data = []
for output_ip in output_ips:
    for quick_ip in quick_ips:
        if output_ip.get('ip') == quick_ip.get('address'):
            combined_data = {**output_ip, 'avgTime': quick_ip.get('avgTime')}
            final_data.append(combined_data)

# Write the combined data to final_data.json
with open('/Users/oliver/Desktop/Github/Triangulator/final_data.json', 'w') as file:
    json.dump(final_data, file, indent=4)

print("Data combined and written to final_data.json")