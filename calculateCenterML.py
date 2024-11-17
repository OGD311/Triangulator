import numpy as np
from scipy.optimize import minimize
import haversine as h

def calculate_center(modelResults, weight=1.0):
    def objective_function(point, modelResults):
        total_error = 0
        for result in modelResults:
            lat, lon = result['coordinates']
            predicted_distance = result['distance']
            actual_distance = h.haversine(point, (lat, lon))
            # Combine absolute and relative errors
            absolute_error = abs(actual_distance - predicted_distance)
            relative_error = absolute_error / predicted_distance
            total_error += weight * relative_error + (1 - weight) * absolute_error
        return total_error

    # More diverse initial guesses
    initial_guesses = [
        np.mean([result['coordinates'] for result in modelResults], axis=0),
        modelResults[0]['coordinates'],
        modelResults[-1]['coordinates'],
        [min(r['coordinates'][0] for r in modelResults),
         min(r['coordinates'][1] for r in modelResults)],
        [max(r['coordinates'][0] for r in modelResults),
         max(r['coordinates'][1] for r in modelResults)]
    ]
    
    best_result = None
    best_error = float('inf')
    
    # Try different optimization methods
    methods = ['L-BFGS-B', 'Nelder-Mead', 'Powell']
    
    for guess in initial_guesses:
        for method in methods:
            try:
                bounds = [(guess[0] - 20, guess[0] + 20),
                         (guess[1] - 20, guess[1] + 20)] if method == 'L-BFGS-B' else None
                
                result = minimize(objective_function, guess, 
                                args=(modelResults,),
                                method=method,
                                bounds=bounds,
                                options={'maxiter': 2000})
                
                if result.fun < best_error:
                    best_error = result.fun
                    best_result = result.x
            except:
                continue
            
    return best_result

def optimize_weight(modelResults, final_coordinate, max_iterations=1000):
    weights = np.concatenate([
        np.linspace(0, 1, 50),  # Linear spacing from 0 to 1
        np.logspace(-3, 3, 50)  # Log spacing for wider range
    ])
    best_error = float('inf')
    best_weight = 1.0
    
    for weight in weights:
        result = calculate_center(modelResults, weight)
        error = h.haversine(result, final_coordinate)
        
        if error < best_error:
            best_error = error
            best_weight = weight
            
        if error < 0.1:  # Stop if error is small enough
            break

        print(f"Weight: {weight:.6f}, Error: {error:.6f}")
            
    return best_weight, best_error



# Rest of your code remains the same
modelResults = [
    {'coordinates': [54.9742, -1.615], 'distance': np.float64(225.33466128529454)},
    {'coordinates': [51.5396, -3.5938], 'distance': np.float64(263.9531267398586)},
    {'coordinates': [51.5072, -0.127586], 'distance': np.float64(248.75506542611242)}
]
final_coordinate = [53.3812, -1.4788]

best_weight, final_error = optimize_weight(modelResults, final_coordinate, max_iterations=10)
final_result = calculate_center(modelResults, best_weight)

print(f"Best weight found: {best_weight}")
print(f"Final error: {final_error} km")
print(f"Final calculated point: {final_result}")
