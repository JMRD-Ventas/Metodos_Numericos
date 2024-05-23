#Programa que calcula la integral x^3 donde x es 4 y 0
import numpy as np

# x= intervalo, y= resultado de la integral
x_points = np.array([2, 3, 5])
y_points = np.array([4, 20.25, 156.25])

# Matriz de Vandermonde para la interpolación cuadrática
A = np.vander(x_points, 3)
coefficients = np.linalg.solve(A, y_points)

# Polinomio cuadrático
def quadratic_polynomial(x, coeffs):
    return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

# Punto a interpolar
x_to_interpolate = 4
y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

# Visualización
x_range = np.linspace(0, 4, 400)
y_range = quadratic_polynomial(x_range, coefficients)