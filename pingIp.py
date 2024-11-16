import json
import os
import time
from pythonping import ping

# Load JSON data from file
with open('/Users/oliver/Desktop/Github/Triangulator/output_ips.json', 'r') as file:
    hosts = json.load(file)

# Function to ping a host
def ping_host(address):
    q = ping(address, count=1)


results = []
for host in hosts:
    address = host.get('ip')
    avgTime = []
    if address:
        print(f"Pinging {address}")
        for _ in range(5):  # Ping 5 times to get an average
            start = time.time()
            ping_host(address)
            end = time.time()
            avgTime.append(end - start)
        avg_time = sum(avgTime) / len(avgTime)
        results.append({'address': address, 'avgTime': avg_time})

with open('/Users/oliver/Desktop/Github/Triangulator/ping_results.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)
    