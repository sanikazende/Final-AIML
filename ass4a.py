import math
import numpy as np
from scipy.optimize import minimize

# Math library example
radius = 5
area_circle = math.pi * radius ** 2
print("Area of the circle:", area_circle)

# Numpy library example
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix product:")
print(matrix_product)

# Scipy library example
def rosenbrock(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

initial_guess = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
result = minimize(rosenbrock, initial_guess, method='nelder-mead')
print("\nMinimized value of Rosenbrock function:", result.fun)
print("Optimal parameters:", result.x)
