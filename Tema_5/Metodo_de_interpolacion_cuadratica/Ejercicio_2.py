#Programa que calcula el precio del dolar en 2016 tomando en cuenta los años 2008, 2012 y 2020
import numpy as np

# x= año, y= población en millones
x_points = np.array([2008, 2012, 2020])
y_points = np.array([11.13, 12.96, 21.64])

# Matriz de Vandermonde para la interpolación cuadrática
A = np.vander(x_points, 3)
coefficients = np.linalg.solve(A, y_points)

# Polinomio cuadrático
def quadratic_polynomial(x, coeffs):
    return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

# Punto a interpolar
x_to_interpolate = 2016
y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

# Visualización
x_range = np.linspace(0, 200, 400)
y_range = quadratic_polynomial(x_range, coefficients)