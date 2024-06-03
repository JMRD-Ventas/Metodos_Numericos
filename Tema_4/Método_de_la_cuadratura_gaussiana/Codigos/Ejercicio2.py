import numpy as np

def f(x):
   """
   Función a integrar: f(x) = 1 - x^2
   """
   return 1 - x**2

# Definir los límites de integración
a = 0
b = 1

# Puntos y pesos de la cuadratura gaussiana de orden 2
x = np.array([np.sqrt(1/3), -np.sqrt(1/3)])
w = np.array([1, 1])

# Cambio de variable para ajustar el intervalo de integración
u = (b - a) * x / 2 + (a + b) / 2

# Calcular la integral aproximada utilizando la cuadratura gaussiana
i = (b - a) * np.sum(w * f(u)) / 2

print(i)
