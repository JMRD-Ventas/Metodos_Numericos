from math import *

def evaluacion(x):
   """
   Evalúa la función ingresada por el usuario, reemplazando las ocurrencias de 'x' por el valor numérico dado.
   
   Argumentos:
   x -- El valor numérico a sustituir en la función.
   
   Retorna:
   El resultado de evaluar la función con el valor de x dado.
   """
   copia = funcion.copy()  # Crea una copia de la lista de la función
   for j in range(len(copia)):
       if copia[j] == "x":
           copia[j] = str(x)  # Reemplaza 'x' por el valor numérico
   return eval("".join(copia))  # Evalúa la función como una expresión

# Obtener la función y los intervalos de integración del usuario
funcion = list(input("Dame la integral/función: "))
b = float(input("Dame el intervalo superior: "))
a = float(input("Dame el intervalo inferior: "))
n = int(input("Dame el número n: "))

h = (b - a) / n  # Ancho de los trapecios
total = 0  # Acumulador para la suma de las áreas de los trapecios

# Aplicar la regla del trapecio compuesto
for i in range(1, n):
   x = a + i * h  # Calcular la coordenada x del punto intermedio
   if i % 2 == 0:
       total += 2 * evaluacion(x)  # Coeficiente 2 para trapecios pares
   else:
       total += 4 * evaluacion(x)  # Coeficiente 4 para trapecios impares

total += evaluacion(a) + evaluacion(b)  # Agregar las evaluaciones en los límites
total = total * (h / 3)  # Ajustar el resultado por el ancho de los trapecios

print(f"Resultado = {total}")
