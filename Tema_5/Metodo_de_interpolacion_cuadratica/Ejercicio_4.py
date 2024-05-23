#Programa que calcula el promedio de vida en años en México durante 1980
import numpy as np

# x= año, y= edad promedio
x_points = np.array([1930, 1970, 2000])
y_points = np.array([34, 61, 74])

# Matriz de Vandermonde para la interpolación cuadrática
A = np.vander(x_points, 3)
coefficients = np.linalg.solve(A, y_points)

# Polinomio cuadrático
def quadratic_polynomial(x, coeffs):
    return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

# Punto a interpolar
x_to_interpolate = 1980
y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

# Visualización
x_range = np.linspace(0, 4, 400)
y_range = quadratic_polynomial(x_range, coefficients)