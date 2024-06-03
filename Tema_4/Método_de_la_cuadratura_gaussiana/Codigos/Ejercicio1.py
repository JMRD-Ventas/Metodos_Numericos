import math

# Definimos la función que queremos integrar
def funcion(x):
    """
    Función a integrar.
    
    Parámetros:
        x (float): Valor en el que se evalúa la función.
    
    Retorna:
        float: Valor de la función evaluada en x.
    """
    return math.exp(-x**2)

# Definimos la función que realiza la cuadratura gaussiana
def cuadratura_gaussiana(a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método de cuadratura gaussiana.
    
    Parámetros:
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de puntos de Gauss.
    
    Retorna:
        float: Aproximación de la integral definida.
    """
    # Coeficientes y nodos de los puntos de Gauss predefinidos
    coeficientes = {2: [1.0, 1.0], 
                    3: [0.5555555556, 0.8888888889, 0.5555555556], 
                    4: [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451], 
                    5: [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851], 
                    6: [0.1713244924, 0.3607615730, 0.4679139346, 0.4679139346, 0.3607615730, 0.1713244924]}
    nodos = {2: [-0.5773502692, 0.5773502692], 
             3: [0.0, -0.7745966692, 0.7745966692],
             4: [-0.3399810436, 0.3399810436, -0.8611363116, 0.8611363116], 
             5: [0.0, -0.5384693101, 0.5384693101, -0.9061798459, 0.9061798459], 
             6: [0.6612093865, -0.6612093865, -0.2386191861, 0.2386191861, -0.9324695142, 0.9324695142]}
    
    suma = 0
    # Iteramos sobre los puntos de Gauss
    for i in range(n):
        # Transformamos los nodos de Gauss al intervalo [a, b]
        xi = ((b - a) * nodos[n][i] + a + b) / 2
        # Sumamos la contribución de cada punto ponderada por su coeficiente
        suma += coeficientes[n][i] * funcion(xi)
    
    # Multiplicamos por el factor de escala y devolvemos el resultado
    return (b - a) / 2 * suma

# Definimos los límites de integración y el número de puntos de Gauss
limite_inferior = 0
limite_superior = 1
numero_puntos_gauss = 4

# Calculamos el resultado de la integral utilizando cuadratura gaussiana
resultado_integral = cuadratura_gaussiana(limite_inferior, limite_superior, numero_puntos_gauss)

# Imprimimos el resultado
print("El resultado de la integral es:", resultado_integral)
