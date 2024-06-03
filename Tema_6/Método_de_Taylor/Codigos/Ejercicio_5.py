import math

# Definir la función f(x) = x^3 + 2x^2 + x + 1
def f(x):
    return x**3 + 2*x**2 + x + 1

# Derivadas de f(x) = x^3 + 2x^2 + x + 1
def f_primera_derivada(x):
    return 3*x**2 + 4*x + 1

def f_segunda_derivada(x):
    return 6*x + 4

def f_tercera_derivada(x):
    return 6

# Función para calcular el factorial
def factorial(n):
    return math.factorial(n)

# Serie de Taylor para f(x) = x^3 + 2x^2 + x + 1
def taylor_series(a, x0, n):
    suma = f(x0)
    if n > 0:
        suma += f_primera_derivada(x0) * (a - x0) / factorial(1)
    if n > 1:
        suma += f_segunda_derivada(x0) * (a - x0)**2 / factorial(2)
    if n > 2:
        suma += f_tercera_derivada(x0) * (a - x0)**3 / factorial(3)
    return suma

# Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
a = float(input("Ingrese el valor de a: "))
x0 = 0  # para la serie de Maclaurin
n = int(input("Ingrese el número de términos (n): "))

# Calcular la aproximación usando la serie de Taylor
aproximación = taylor_series(a, x0, n)

# Imprimir el resultado
print(f"La aproximación de f({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
