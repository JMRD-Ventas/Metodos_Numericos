import math

# Definir la función sin(x)
def f(x):
    return math.sin(x)

# Derivadas de sin(x) en x = 0 alternan entre sin(x), cos(x), -sin(x), -cos(x)
def f_derivada_orden_n(x, n):
    if n % 4 == 0:
        return math.sin(x)
    elif n % 4 == 1:
        return math.cos(x)
    elif n % 4 == 2:
        return -math.sin(x)
    else:
        return -math.cos(x)

# Función para calcular el factorial
def factorial(n):
    return math.factorial(n)

# Serie de Taylor para sin(x)
def taylor_series(a, x0, n):
    suma = 0
    for i in range(n):
        término = ((-1) ** i) * ((a - x0) ** (2 * i + 1)) / factorial(2 * i + 1)
        suma += término
    return suma

# Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
a = float(input("Ingrese el valor de a: "))
x0 = 0  # para la serie de Maclaurin
n = int(input("Ingrese el número de términos (n): "))

# Calcular la aproximación usando la serie de Taylor
aproximación = taylor_series(a, x0, n)

# Imprimir el resultado
print(f"La aproximación de sin({a}) usando la serie de Taylor con {n} términos es: {aproximación}")