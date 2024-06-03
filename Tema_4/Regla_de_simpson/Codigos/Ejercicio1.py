import numpy as np

# Método regla de Simpson

# La regla de Simpson es una técnica de integración numérica
# que utiliza polinomios de segundo grado (parábolas) 
# para aproximar la curva.
# Divide el intervalo de integración en varios 
# subintervalos y aproxima cada uno de estos subintervalos 
# con una parábola que pasa a través de tres puntos: el punto inicial, 
# el punto medio y el punto final de cada subintervalo.

#Fórmula: 

# ((DeltaX)/3) [f(x0)+ 4 sumatoria de f(x impares)+ 2 sumatoria de f(x pares)]+f(Xn)]

# Significado de la simbología:

#    - f(x0): Funcion evaluada con intervalo a.
#    - f(Xn): Funcion evaluada con intervalo b.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n
#    - ( a ) y ( b ): Extremos del intervalo de integración.
#    - ( n ): Número de subintervalos en los que se divide el intervalo.

String = "f(x) = e^(x^2)"

# Definir integral
def f(x):
    return np.exp(x**2)
    
# Dar intervalos [a,b]
a, b = 0, 1
n = 4

# Aplicacion de la formula
def simpson(a, b, n):

#Si la función es altamente oscilatoria o carece de derivados en ciertos puntos, se puede usar la regla compuesta de Simpson dividiendo el intervalo en subintervalos pequeños y aplicando la regla de Simpson a cada uno. 
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)
    return (h / 3) * suma

resultado_simpson = simpson(a, b, n)

# Resultados

print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método regla de Simpson:", resultado_simpson)
print("Bibliográfia: https://www.youtube.com/watch?v=ypaNlJTPf9c&list=PLJPaSlai3G9YIgCJq4a3vbK6P3zWNPOWk&index=22&ab_channel=AntonioCedilloHernandez")
print("")
