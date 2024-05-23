import numpy as np

def calcular_pesos_y_abscisas(n):
    # Función para calcular los pesos y las abscisas de los puntos de Gauss
    # Utilizaremos la fórmula de los polinomios de Legendre para obtener estos valores
    # Aquí solo se muestra una implementación simple para n=2 y n=3, pero pueden definirse para más nodos
    if n == 2:
        return np.array([1, 1]), np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
    elif n == 3:
        return np.array([5/9, 8/9, 5/9]), np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
    else:
        raise ValueError("Número de nodos no soportado")

def cuadratura_gaussiana(f, a, b, n):
    """
    Aproxima la integral definida de la función f en el intervalo [a, b] utilizando el método de cuadratura Gaussiana.

    Parámetros:
        f: función a integrar
        a: límite inferior del intervalo de integración
        b: límite superior del intervalo de integración
        n: número de puntos de Gauss (2 o 3 para este ejemplo)

    Retorna:
        Aproximación de la integral definida de f en [a, b]
    """
    # Paso 1: Calcular los pesos y las abscisas de los puntos de Gauss
    w, x = calcular_pesos_y_abscisas(n)

    # Paso 2: Transformar el intervalo [a, b] al intervalo estándar [-1, 1]
    x_transformed = ((b - a) * x + (a + b)) / 2

    # Paso 3: Calcular la suma ponderada
    suma = 0
    for i in range(n):
        suma += w[i] * f(x_transformed[i])

    # Paso 4: Devolver la aproximación de la integral
    return (b - a) / 2 * suma

# Ejemplo de uso
def funcion_ejemplo(x):
    return np.exp(-x**2)  # Función de ejemplo, en este caso la distribución Gaussiana

a = -1
b = 1
n = 3

resultado = cuadratura_gaussiana(funcion_ejemplo, a, b, n)
print("Aproximación de la integral:", resultado)