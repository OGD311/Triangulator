import json
import os
import time
from pythonping import ping

# Load JSON data from file
with open('/Users/oliver/Desktop/Github/Triangulator/ping_results.json', 'r') as file:
    hosts = json.load(file)

# Function to ping a host
def ping_host(address):
    q = ping(address, count=1)


results = []
for host in hosts:
   avgTime = host.get('avgTime')

   if avgTime < 2:
        results.append(host)
   
   
   
with open('/Users/oliver/Desktop/Github/Triangulator/quickIPs.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)
    