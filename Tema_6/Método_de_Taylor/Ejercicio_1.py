import math

print("Funcion es e^x")
# Definir la función f(x) = e^x
def f(x):
    return math.exp(x)

# Derivadas de f(x) = e^x son todas e^x
def f_primera_derivada(x):
    return math.exp(x)

def f_segunda_derivada(x):
    return math.exp(x)

# Podemos generalizar para las derivadas de cualquier orden en este caso
def f_derivada_orden_n(x, n):
    return math.exp(x)

# Función para calcular el factorial
def factorial(n):
    return math.factorial(n)

# Serie de Taylor para e^x
def taylor_series(a, x0, n):
    suma = f(x0)
    for i in range(1, n + 1):
        término = f_derivada_orden_n(x0, i) * ((a - x0) ** i) / factorial(i)
        suma += término
    return suma

# Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
a = float(input("Ingrese el valor de a: "))
x0 = 0  # para la serie de Maclaurin
n = int(input("Ingrese el número de términos (n): "))

# Calcular la aproximación usando la serie de Taylor
aproximación = taylor_series(a, x0, n)

# Imprimir el resultado
print(f"La aproximación de e^{a} usando la serie de Taylor con {n} términos es: {aproximación}")