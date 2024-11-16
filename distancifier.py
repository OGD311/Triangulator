import joblib
import numpy as np
import time
from pythonping import ping
import haversine as h
import json
import random

model = joblib.load('/Users/oliver/Desktop/Github/Triangulator/disTime.joblib')
print("running")

def ping_host(address):
    q = ping(address, count=1)


hosts = [
    {
        "ip": "81.152.55.0",
        "city": "Plymouth",
        "coordinates": [
            50.3881,
            -4.1324
        ],
        "country": "United Kingdom",
        "avgTime": 0.03428540229797363,
        "distance": 379.3316848460527
    },
    {
        "ip": "149.255.102.0",
        "city": "Newcastle",
        "coordinates": [
            54.2218,
            -5.9362
        ],
        "country": "United Kingdom",
        "avgTime": 0.02414116859436035,
        "distance": 307.2153745690649
    },
    {
        "ip": "5.10.22.0",
        "city": "London",
        "coordinates": [
            51.5074,
            -0.127758
        ],
        "country": "United Kingdom",
        "avgTime": 0.010084199905395507,
        "distance": 227.58326183352858
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

import numpy as np
from scipy.optimize import minimize
import webbrowser

def latlon_to_cartesian(lat, lon, radius=6371):
    lat, lon = np.radians(lat), np.radians(lon)
    x = radius * np.cos(lat) * np.cos(lon)
    y = radius * np.cos(lat) * np.sin(lon)
    z = radius * np.sin(lat)
    return np.array([x, y, z])

def cartesian_to_latlon(x, y, z, radius=6371):
    lat = np.degrees(np.arcsin(z / radius))
    lon = np.degrees(np.arctan2(y, x))
    return float(lat), float(lon)

def distance_to_circle(center, circle_center, radius):
    """
    Calculate the squared distance from a point to the edge of a circle.
    """
    return (np.linalg.norm(center - circle_center) - radius)**2

def objective_function(cartesian_point, p1, r1, p2, r2, p3, r3):
    """
    Objective function to minimize: sum of squared distances to the circle edges.
    """
    return (
        distance_to_circle(cartesian_point, p1, r1) +
        distance_to_circle(cartesian_point, p2, r2) +
        distance_to_circle(cartesian_point, p3, r3)
    )

def find_overlap_center(c1, r1, c2, r2, c3, r3):
    """
    Find the approximate center of the overlapping area of three circles in latitude/longitude.
    
    c1, c2, c3: Tuples of (latitude, longitude) for the circle centers
    r1, r2, r3: Radii of the circles in kilometers
    Returns: Tuple of (latitude, longitude) for the center of overlap
    """
    # Convert circle centers to Cartesian coordinates
    p1 = latlon_to_cartesian(*c1)
    p2 = latlon_to_cartesian(*c2)
    p3 = latlon_to_cartesian(*c3)

    # Initial guess for the center (centroid of the circle centers)
    initial_guess = (p1 + p2 + p3) / 3

    # Minimize the objective function
    result = minimize(
        objective_function,
        initial_guess,
        args=(p1, r1, p2, r2, p3, r3),
        method='L-BFGS-B'
    )

    # Convert the result back to latitude and longitude
    center_cartesian = result.x
    center_latlon = cartesian_to_latlon(*center_cartesian)
    return center_latlon


circle1 = modelResults[0]['coordinates']
radius1 = modelResults[0]['distance']

circle2 = modelResults[1]['coordinates']
radius2 = modelResults[1]['distance']

circle3 = modelResults[2]['coordinates']
radius3 = modelResults[2]['distance']

center_point = find_overlap_center(circle1, radius1, circle2, radius2, circle3, radius3)
print("Approximate center of overlap:", center_point)
url = 'https://www.google.co.uk/maps/place/' + str(center_point[0]) + ',' + str(center_point[1])
print(url)
webbrowser.open(url)
