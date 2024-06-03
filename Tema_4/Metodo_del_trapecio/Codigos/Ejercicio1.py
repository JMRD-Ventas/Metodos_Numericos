# Definir las funciones que se van a integrar
import math

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

def integral(f, a, b):
   """
   Calcula la integral definida de una función f(x) entre los límites a y b usando la regla del trapecio compuesta con corrección del error.
   
   Argumentos:
   f -- La función a integrar.
   a -- El límite inferior de la integral.
   b -- El límite superior de la integral.
   
   Retorna:
   La aproximación de la integral definida de f(x) entre a y b.
   """
   n = int((b - a) / 0.001 + 1)  # Número de subintervalos
   h = (b - a) / n  # Ancho de los subintervalos
   x = a  # Inicializar x en el límite inferior
   suma = 0  # Acumulador para el área de los trapecios
   
   # Iterar sobre los subintervalos
   for i in range(n):
       suma += trapecio(f, x, x + h)  # Calcular el área del trapecio y acumularla
       x += h  # Avanzar al siguiente subintervalo
   
   return suma * h  # Multiplicar la suma acumulada por el ancho de los subintervalos

def trapecio(f, a, b):
   """
   Calcula el área de un trapecio bajo la curva f(x) entre los puntos a y b, con corrección del error.
   
   Argumentos:
   f -- La función bajo la curva.
   a -- El límite inferior del trapecio.
   b -- El límite superior del trapecio.
   
   Retorna:
   El área del trapecio bajo la curva f(x) entre a y b, con corrección del error.
   """
   h = b - a  # Ancho del trapecio
   x = (a + b) / 2  # Punto medio del trapecio
   return (h / 2) * (f(a) + f(b)) - (h ** 3 / 12) * d2(f, x)  # Fórmula del trapecio con corrección del error

def d2(f, x):
   """
   Aproxima la segunda derivada de la función f(x) en el punto x usando diferencias finitas.
   
   Argumentos:
   f -- La función a derivar.
   x -- El punto en el cual se aproxima la segunda derivada.
   
   Retorna:
   La aproximación de la segunda derivada de f(x) en el punto x.
   """
   h = 0.001  # Paso para las diferencias finitas
   return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)  # Fórmula de diferencias finitas

# Obtener los límites de integración del usuario
a = float(input("Dame el límite inferior: "))
b = float(input("Dame el límite superior: "))

# Calcular e imprimir las integrales
print("La integral de f(x) = ", integral(f, a, b))
print("La integral de g(x) = ", integral(g, a, b))
