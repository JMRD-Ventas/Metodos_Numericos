# Método regla de Simpson

# La regla de Simpson es una técnica de integración numérica
# que utiliza polinomios de segundo grado (parábolas) 
# para aproximar la curva.
# Divide el intervalo de integración en varios 
# subintervalos y aproxima cada uno de estos subintervalos 
# con una parábola que pasa a través de tres puntos: el punto inicial, 
# el punto medio y el punto final de cada subintervalo.

#Fórmula: 

# ((DeltaX)/3) [f(a)+ 4f(m) +f(b)]

# Significado de la simbología:

#    - f(a): Funcion evaluada con intervalo a.
#    - f(b): Funcion evaluada con intervalo b.
#    - f(m): punto intermedio se calcula con: (a+b)/2.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n

# Define la función que deseas integrar.
String = "f(x) = ∫ x^3 dx  en los puntos a:0   &   b: 5"

def f(x):
    return x**3

# Define los límites del intervalo de integración.
a, b = 0, 5

# Calcula h o deltaX.
def h():
    return ((b - a) / 2) / 3

# Calcula el punto medio del intervalo f(m)
def m():
    return (b + a) / 2

# Calcula los valores de la función en los extremos y en el punto medio.
def sumaFunciones():
    return f(a) + f(m()) + f(b)

# Aplica la fórmula de Simpson.
def simpson():
    return h() * sumaFunciones()

##Margen de error

def margenError():
    error = 625/25
    return abs((error - simpson()) / error) * 100

# Calcular margen de error
mE = margenError()

# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El resultado aplicando el método del trapecio es:", simpson())
print("Bibliografía:https://es.symbolab.com/solver/step-by-step/%5Cint_%7B0%7D%5E%7B5%7D%20x%5E%7B3%7Ddx?or=input")
print("El link anterior demuestra el resultado en Symbolab para confirmar la validez del resultado")
print("El margen de error es: ", mE)
print("")
