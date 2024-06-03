import numpy as np
from scipy.special import roots_legendre

#Metodo  Cuadratura Gaussiana:

# La cuadratura Gaussiana es un método numérico para aproximar integrales definidas.
# La idea es utilizar pesos y nodos específicos para mejorar la precisión de la aproximación.


#Fórmula:

# ∫[a,b] f(x) dx ≈ ∑[i=1,n] w_i * f((b-a)/2 * x_i + (a+b)/2)

# Simbologia:

#    - f(x) es la función a integrar
#    - [a, b] es el intervalo de integración
#    - n es el número de nodos
#    - x_i son los nodos de integración
#    - w_i son los pesos asociados a los nodos de integración

String = "f(x) = e^(x^2)"

# Paso 2: Define la función

def f(x):
    return np.exp(x**2)

# 1.1 Determinar puntos de gauss

a, b = 0.2, 1.2
n = 2

# 1.2 Determinar los pesos y nodos

def gauss_legendre_nodes_weights(n):
    nodes, weights = roots_legendre(n)
    return nodes, weights


def cuadratura_gaussiana():
    x, w = gauss_legendre_nodes_weights(n)

    # Aplica la fórmula de Cuadratura Gaussiana
    integral = sum(w * f((b-a)/2 * x + (a+b)/2))

    # Calculo del valor [a, b]
    integral *= (b-a)/2
    return integral

resultado_cuadratura_gaussiana = cuadratura_gaussiana()

# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("Método de la Cuadratura Gaussiana:", resultado_cuadratura_gaussiana)
print("")
print("Bibliografía: https://www.youtube.com/watch?v=7fHyO8nfPIU&ab_channel=AlejandroSandovalRamos")
