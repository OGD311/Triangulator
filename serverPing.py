import json
import os
import time
from pythonping import ping

# Load JSON data from file
with open('servers.json', 'r') as file:
    hosts = json.load(file)

# Function to ping a host
def ping_host(url):
    ping('127.0.0.1', verbose=True)


results = []
for host in hosts:
    url = host.get('address')
    avgTime = []
    if url:
        for _ in range(5):  # Ping 5 times to get an average
            start = time.time()
            ping_host(url)
            end = time.time()
            avgTime.append(end - start)
        avg_time = sum(avgTime) / len(avgTime)
        results.append({'url': url, 'avgTime': avg_time})

with open('ping_results.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)
    