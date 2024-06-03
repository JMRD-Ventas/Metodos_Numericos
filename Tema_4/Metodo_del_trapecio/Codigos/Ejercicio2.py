import math
import numpy as np

def f(x):
   """
   Función f(x) = x * cos(x)
   """
   return x * math.cos(x)

def g(x):
   """
   Función g(x) = e^cos(x)
   """
   return math.exp(math.cos(x))

def integral(f, a, b, n):
   """
   Calcula la integral definida de una función f(x) entre los límites a y b usando el método del trapecio múltiple.
   
   Argumentos:
   f -- La función a integrar.
   a -- El límite inferior de la integral.
   b -- El límite superior de la integral.
   n -- El número de trapecios a utilizar en el método.
   
   Retorna:
   La aproximación de la integral definida de f(x) entre a y b.
   """
   h = (b - a) / n  # Ancho de los trapecios
   x = np.linspace(a, b, n + 1)  # Vector de puntos en el intervalo [a, b]
   suma = np.sum(f(x[1:-1]))  # Suma de las evaluaciones de la función en los puntos interiores
   
   return (h / 2) * (f(a) + 2 * suma + f(b))  # Fórmula del trapecio múltiple

# Obtener los límites de integración y el número de trapecios del usuario
a = float(input("Dame el límite inferior: "))
b = float(input("Dame el límite superior: "))
n = int(input("Dame el número de trapecios: "))

# Calcular e imprimir las integrales
print("La integral de f(x) = ", integral(f, a, b, n))
print("La integral de g(x) = ", integral(g, a, b, n))
