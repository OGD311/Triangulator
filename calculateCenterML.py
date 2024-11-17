import numpy as np
from scipy.optimize import minimize
from haversine import haversine

def calculate_center_with_feedback(modelResults, final_coordinates, learning_rate=0.1, iterations=100):
    def weighted_objective_function(point, modelResults, weights):
        total_error = 0
        for result, weight in zip(modelResults, weights):
            lat, lon = result['coordinates']
            predicted_distance = result['distance']
            actual_distance = haversine(point, (lat, lon))
            lat_error = (point[0] - lat) ** 2
            lon_error = (point[1] - lon) ** 2
            total_error += weight * ((predicted_distance - actual_distance) ** 2 + lat_error + lon_error)
        return total_error

    # Initialize weights
    weights = np.ones(len(modelResults))
    initial_guess = np.mean([result['coordinates'] for result in modelResults], axis=0)

    for _ in range(iterations):
        # Optimize to find best point given current weights
        result = minimize(weighted_objective_function, initial_guess, args=(modelResults, weights), method='L-BFGS-B')
        best_point = result.x

        # Calculate feedback error
        feedback_error = np.linalg.norm(np.array(best_point) - np.array(final_coordinates))
        weights += learning_rate * feedback_error  # Adjust weights

    return best_point



# Rest of your code remains the same
modelResults = [
    {'coordinates': [54.9742, -1.615], 'distance': np.float64(225.33466128529454)},
    {'coordinates': [51.5396, -3.5938], 'distance': np.float64(263.9531267398586)},
    {'coordinates': [51.5072, -0.127586], 'distance': np.float64(248.75506542611242)}
]
final_coordinate = [53.3812, -1.4788]

best_point = calculate_center_with_feedback(modelResults, final_coordinate, )

print(best_point)
