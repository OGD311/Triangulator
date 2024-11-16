from random import randint
import json
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from pythonping import ping
import time

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

with open('/Users/oliver/Desktop/Github/Triangulator/combined_output.json', 'r') as f:
    data = json.load(f)
    print(data)
    distance_data = [item['distance'] for item in data]
    time_data = [[item['avgTime']] for item in data] 

TRAIN_INPUT = time_data
TRAIN_OUTPUT = distance_data

degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)

X_TEST = [[37 / 1000]]

outcome = model.predict(X_TEST)
coefficients = model.named_steps['linearregression'].coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
