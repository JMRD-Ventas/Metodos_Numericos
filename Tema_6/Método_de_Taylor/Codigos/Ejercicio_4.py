import math

# Definir la función ln(1 + x)
def f(x):
    return math.log(1 + x)

# Derivadas de ln(1 + x) en x = 0 son (-1)^(n+1) * (n-1)! / n! = (-1)^(n+1) / n
def f_derivada_orden_n(n):
    return (-1) ** (n + 1) / n

# Función para calcular el factorial
def factorial(n):
    return math.factorial(n)

# Serie de Taylor para ln(1 + x)
def taylor_series(a, x0, n):
    suma = 0
    for i in range(1, n + 1):
        término = f_derivada_orden_n(i) * ((a - x0) ** i)
        suma += término
    return suma

# Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
a = float(input("Ingrese el valor de a: "))
x0 = 0  # para la serie de Maclaurin
n = int(input("Ingrese el número de términos (n): "))

# Calcular la aproximación usando la serie de Taylor
aproximación = taylor_series(a, x0, n)

# Imprimir el resultado
print(f"La aproximación de ln(1 + {a}) usando la serie de Taylor con {n} términos es: {aproximación}")
