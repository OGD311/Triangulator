import json

# Load data from distance_output.json
with open('/Users/oliver/Desktop/Github/Triangulator/distance_output.json', 'r') as f:
    distance_data = json.load(f)

# Load data from ping_results.json
with open('/Users/oliver/Desktop/Github/Triangulator/ping_results.json', 'r') as f:
    ping_data = json.load(f)

# Create a new list to store the combined data
combined_data = []

# Assuming both JSON files have the same structure and order
for distance, ping in zip(distance_data, ping_data):
    combined_entry = {
        'distance': distance['distance'],
        'avgTime': ping['avgTime']
    }
    combined_data.append(combined_entry)

# Write the combined data to a new JSON file
with open('/Users/oliver/Desktop/Github/Triangulator/combined_output.json', 'w') as f:
    json.dump(combined_data, f, indent=4)