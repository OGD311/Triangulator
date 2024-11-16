from random import randint
import json
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from pythonping import ping
import time
import joblib

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 8

with open('/Users/oliver/Desktop/Github/Triangulator/final_data.json', 'r') as f:
    data = json.load(f)
    print(data)
    distance_data = [item['distance'] for item in data]
    time_data = [[item['avgTime']] for item in data] 

TRAIN_INPUT = time_data
TRAIN_OUTPUT = distance_data
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(TRAIN_INPUT[:TRAIN_SET_COUNT], TRAIN_OUTPUT[:TRAIN_SET_COUNT])

X_TEST = [[0.038]]

outcome = model.predict(X_TEST)
coefficients = model.named_steps['linearregression'].coef_

print(outcome)

model_filename = '/Users/oliver/Desktop/Github/Triangulator/disTime.joblib'
joblib.dump(model, model_filename)

print(f'Model saved to {model_filename}')
