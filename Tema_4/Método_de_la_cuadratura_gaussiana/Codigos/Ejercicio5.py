import numpy as np

def cuadratura_gaussiana(f, a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método de cuadratura gaussiana.

    Parámetros:
        f (función): La función a integrar.
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de puntos de Gauss.

    Retorna:
        float: Aproximación de la integral definida de f(x) desde a hasta b.
    """
    # Paso 1: Preparación
    # Calculamos los pesos y las abscisas de los puntos de Gauss
    weights, nodes = np.polynomial.legendre.leggauss(n)

    # Paso 2: Transformar el intervalo [a, b] al intervalo estándar [-1, 1]
    x_transformed = ((b - a) * nodes + (a + b)) / 2

    # Paso 3: Calcular la suma ponderada
    suma = 0
    for i in range(n):
        suma += weights[i] * f(x_transformed[i])

    # Paso 4: Devolver la aproximación de la integral
    return (b - a) / 2 * suma

# Ejemplo de uso
def funcion_ejemplo(x):
    return x**2

a = 0
b = 2
n = 3
resultado = cuadratura_gaussiana(funcion_ejemplo, a, b, n)
print("Aproximación de la integral:", resultado)
