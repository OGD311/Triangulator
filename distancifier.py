import joblib
import numpy as np
import time
from pythonping import ping
import haversine as h
import json
import random
import webbrowser
from scipy.optimize import minimize
import numpy as np
import os

model = joblib.load('/Users/oliver/Desktop/Github/Triangulator/disTime.joblib')
# print("running")

def ping_host(address):
    q = ping(address, count=1)


hosts = [
        {
        "ip": "51.89.128.110",
        "city": "Newcastle upon Tyne",
        "coordinates": [
            54.9742,
            -1.615
        ],
        "country": "United Kingdom",
        "avgTime": 0.010955476760864257,
        "distance": 177.3519567962753
    },
      {
        "ip": "51.194.79.0",
        "city": "Bridgend",
        "coordinates": [
            51.5396,
            -3.5938
        ],
        "country": "United Kingdom",
        "avgTime": 0.016228723526000976,
        "distance": 249.91227638275703
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

def calculate_center(modelResults):
    def objective_function(point, modelResults):
        total_error = 0
        for result in modelResults:
            lat, lon = result['coordinates']
            predicted_distance = result['distance']
            actual_distance = h.haversine(point, (lat, lon))
            total_error += ((predicted_distance * 0.90) - actual_distance) ** 2
        return total_error

    initial_guess = np.mean([result['coordinates'] for result in modelResults], axis=0)
    result = minimize(objective_function, initial_guess, args=(modelResults,), method='L-BFGS-B')
    return result.x



def run():

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
        if modelResults[i]['distance'] > 450:
            print(modelResults[i]['coordinates'], modelResults[i]['distance'])
            return True


    best_point = calculate_center(modelResults)
    # print(f"Best point: {best_point}")


    # # https://www.mapdevelopers.com/draw-circle-tool.php?circles=[[371098,50.3879546,-4.1318378,"#AAAAAA","#000000",0.4],[222928,54.9741773,-1.6150185,"#AAAAAA","#000000",0.4],[222305,51.5085078,-0.0843403,"#AAAAAA","#000000",0.4]]
    # # https://www.mapdevelopers.com/draw-circle-tool.php?circles=[[393.11247610677924,50.3881,-4.1324,"#AAAAAA","#000000",0.4],[311.8821298708854,56.4806,-2.9358,"#AAAAAA","#000000",0.4],[230.11380145610286,51.5074,-0.127758,"#AAAAAA","#000000",0.4]]

    # import urllib.parse

    # url = "https://www.mapdevelopers.com/draw-circle-tool.php?circles=["
    # circles = []

    # for result in modelResults:
    #     lat, lon = result['coordinates']
    #     distance = round(result['distance'] * 1000, 1)
    #     circle = f"[{distance},{lat},{lon},\"#AAAAAA\",\"#000000\",0.4]"
    #     circles.append(circle)

    # circle = f"[{1000},{best_point[0]},{best_point[1]},\"#AAAAAA\",\"#000000\",0.4]"
    # circles.append(circle)

    # url += ",".join(circles)
    # url += "]"

    # encoded_url = urllib.parse.quote(url, safe=':/?=&')
    # print(encoded_url)
    # webbrowser.open(encoded_url)

    # Am in sheffield????

    coord1 = (53.38122788610671, -1.4788009949737875) # Sheffield

    coord2 = (best_point[0], best_point[1])

    distance = h.haversine(coord1, coord2)

    if distance < 25: 
        print("You are in Sheffield")

    elif distance < 80: 
        print("Almost in Sheffield")

    else:
        print("Not in Sheffield")

    print(distance)

    return False


yes = True

while yes:
    yes = run()
    time.sleep(5)