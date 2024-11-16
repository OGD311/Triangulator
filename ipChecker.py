import json
import requests
import time

def check_ips(input_file, output_file):
    with open(input_file, 'r') as infile:
        ips = json.load(infile)
    
    results = []
    count = 0
    for ip in ips:
        if count == 45:
            time.sleep(60)
            count = 0
        response = requests.get(f'http://ip-api.com/json/{ip}')
        count += 1
        data = response.json()
        print(data)
        if data['status'] == 'success':
            results.append({'ip': ip, 'city': data['city'], 'coordinates': (data['lat'], data['lon']), 'country': data['country']})
        else:
            results.append({'ip': ip, 'city': 'Unknown'})
    
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    input_file = '/Users/oliver/Desktop/Github/Triangulator/input_ips.json'  # Replace with your input file path
    output_file = 'output_ips.json'  # Replace with your output file path
    check_ips(input_file, output_file)