import math
import json

import haversine as h

# Example usage
# Read coordinates from ping_results.json
with open('/Users/oliver/Desktop/Github/Triangulator/servers.json', 'r') as file:
    hosts = json.load(file)

# Example coordinates
coord1 = (53.38122788610671, -1.4788009949737875)
output_data = []

for host in hosts:
    address = host.get('address')
    coord2 = host.get('coordinates')

    distance = h.haversine(coord1, coord2)
    
    # Append the result to the output data list
    output_data.append({
        "address": address,
        "distance": distance
    })

with open('/Users/oliver/Desktop/Github/Triangulator/distance_output.json', 'w') as outfile:
    json.dump(output_data, outfile, indent=4)