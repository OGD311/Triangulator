import json
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import joblib
import numpy as np
import matplotlib.pyplot as plt

TRAIN_SET_COUNT = 100

# Load the data
with open('/Users/oliver/Desktop/Github/Triangulator/final_data.json', 'r') as f:
    data = json.load(f)
    print(data)
    distance_data = [item['distance'] for item in data]  # Get the distance data
    time_data = [[item['avgTime']] for item in data]  # Get the time data

# Negate the distance_data to make the model negatively regress
distance_data = [-distance for distance in distance_data]

TRAIN_INPUT = time_data
TRAIN_OUTPUT = distance_data
degree = 8  # Set the degree for the polynomial

# Create and train the model
model = make_pipeline(StandardScaler(), PolynomialFeatures(degree), LinearRegression())
model.fit(TRAIN_INPUT[:TRAIN_SET_COUNT], TRAIN_OUTPUT[:TRAIN_SET_COUNT])

# Testing the model with sample inputs
X_TEST = [[0.034], [0.014091968536376953]]
outcome = model.predict(X_TEST)

# Negate the predicted outcomes
negated_outcome = -outcome

# Get model coefficients
coefficients = model.named_steps['linearregression'].coef_

# Print the negated outcome for the test set
print(negated_outcome)

# Plotting the data points and the model fit
plt.scatter(time_data, [-distance for distance in distance_data], color='blue', label='Data points')
time_range = np.linspace(min(time_data)[0], max(time_data)[0], 100).reshape(-1, 1)
predicted_distances = model.predict(time_range)

# Negate the predicted values for plotting
negated_predicted_distances = -predicted_distances

plt.plot(time_range, negated_predicted_distances, color='red', label='Model')

plt.xlabel('Time')
plt.ylabel('Distance')
plt.title('Distance vs Time with Polynomial Regression Model')
plt.legend()
plt.show()

# Save the model
model_filename = '/Users/oliver/Desktop/Github/Triangulator/disTime.joblib'
joblib.dump(model, model_filename)

print(f'Model saved to {model_filename}')
