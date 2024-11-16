import joblib
import numpy as np
import time
from pythonping import ping
import haversine as h
import json
import random
import webbrowser

model = joblib.load('/Users/oliver/Desktop/Github/Triangulator/disTime.joblib')
print("running")

def ping_host(address):
    q = ping(address, count=1)


hosts = [
    {
            "ip": "2.222.126.0",
            "city": "Dover",
            "coordinates": [
                51.1734,
                1.2785
            ],
            "country": "United Kingdom",
            "avgTime": 0.016706514358520507,
            "distance": 308.91593866104284
        },
        {
            "ip": "90.221.131.0",
            "city": "Brixton",
            "coordinates": [
                50.35,
                -4.03333
            ],
            "country": "United Kingdom",
            "avgTime": 0.022867441177368164,
            "distance": 379.90614367936075
        },
        {
            "ip": "51.148.134.0",
            "city": "London",
            "coordinates": [
                51.5072,
                -0.127586
            ],
            "country": "United Kingdom",
            "avgTime": 0.014091968536376953,
            "distance": 227.60839161410848
        },

]



pingResults = []
for host in hosts:
    address = host.get('ip')
    coordinates = host.get('coordinates')
    avgTime = []
    if address:
        for _ in range(5): 
            start = time.time()
            ping_host(address)
            end = time.time()
            avgTime.append(end - start)
        avg_time = sum(avgTime) / len(avgTime)
        pingResults.append({'ip': address, 'coordinates': coordinates, 'avgTime': avg_time})

# Make predictions
modelResults = []
for i in range(len(pingResults)):
    distancePredict = model.predict([[pingResults[i]['avgTime']]])

    modelResults.append({'coordinates': pingResults[i]['coordinates'], 'distance': distancePredict[0]})
    


for i in range(len(modelResults)):
    print(f"{modelResults[i]['coordinates']} : {modelResults[i]['distance']}")

    
# https://www.mapdevelopers.com/draw-circle-tool.php?circles=[[371098,50.3879546,-4.1318378,"#AAAAAA","#000000",0.4],[222928,54.9741773,-1.6150185,"#AAAAAA","#000000",0.4],[222305,51.5085078,-0.0843403,"#AAAAAA","#000000",0.4]]
# https://www.mapdevelopers.com/draw-circle-tool.php?circles=[[393.11247610677924,50.3881,-4.1324,"#AAAAAA","#000000",0.4],[311.8821298708854,56.4806,-2.9358,"#AAAAAA","#000000",0.4],[230.11380145610286,51.5074,-0.127758,"#AAAAAA","#000000",0.4]]

import urllib.parse

url = "https://www.mapdevelopers.com/draw-circle-tool.php?circles=["
circles = []

for result in modelResults:
    lat, lon = result['coordinates']
    distance = round(result['distance'] * 1000, 1)
    circle = f"[{distance},{lat},{lon},\"#AAAAAA\",\"#000000\",0.4]"
    circles.append(circle)

url += ",".join(circles)
url += "]"

encoded_url = urllib.parse.quote(url, safe=':/?=&')
print(encoded_url)
webbrowser.open(encoded_url)
