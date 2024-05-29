# Metodo de Taylor

## ¿Qué es?
El método de Taylor es otro método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDO). Se basa en la expansión en series de Taylor de la solución alrededor de un punto inicial. 

El método de Taylor proporciona una aproximación polinómica de la solución en un intervalo cercano al punto inicial. La precisión de la aproximación depende del orden n de la serie de Taylor utilizada. Cuanto mayor sea n, más precisa será la aproximación, pero también requerirá más cálculos.

Una ventaja del método de Taylor es que no requiere dividir el intervalo en subintervalos, como en el método de Euler o Runge-Kutta. Sin embargo, a medida que nos alejamos del punto inicial, la precisión de la aproximación disminuye, por lo que es necesario repetir el proceso en intervalos más pequeños.

El método de Taylor es particularmente útil cuando se conocen las derivadas analíticas de la función f(x, y), ya que esto simplifica los cálculos. En caso contrario, las derivadas deben calcularse numéricamente, lo que puede introducir errores adicionales.

Es importante tener en cuenta que el método de Taylor puede ser inestable para ciertas ecuaciones diferenciales, especialmente aquellas con soluciones altamente oscilantes o con comportamientos caóticos. En esos casos, puede ser preferible utilizar otros métodos numéricos más robustos.

## Pasos para su solución
El procedimiento para aplicar el método de Taylor es el siguiente:
   1. Definir la ecuación diferencial y las condiciones iniciales:
      Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.
   
   2. Calcular las derivadas sucesivas de y con respecto a x utilizando la ecuación diferencial dada:
      y' = f(x, y)
      y'' = (∂f/∂x) + (∂f/∂y)y'
      y''' = (∂^2f/∂x^2) + 2(∂^2f/∂x∂y)y' + (∂^2f/∂y^2)y'y''
      y así sucesivamente.
   
   3. Construir la serie de Taylor de y(x) alrededor del punto x0 hasta el orden deseado n:
      y(x) = y(x0) + y'(x0)(x - x0) + (y''(x0)/2!)(x - x0)^2 + ... + (y^(n)(x0)/n!)(x - x0)^n
   
   4. Evaluar las derivadas y'(x0), y''(x0), ..., y^(n)(x0) utilizando las expresiones obtenidas en el paso 2 y los valores iniciales y(x0) = y0.
   
   5. Sustituir los valores de las derivadas evaluadas en el paso 4 en la serie de Taylor del paso 3.
   
   6. Elegir un valor para x = x1 cercano a x0 y evaluar y(x1) utilizando la serie de Taylor obtenida.
   
   7. Repetir los pasos 4, 5 y 6 para obtener aproximaciones de y en puntos sucesivos x2, x3, ..., xn.

## Implementación de los codigos en Python

### Ejercicio 1.py
#### Codigo
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
      
#### Comprobacion
[![imagen-2024-05-23-122006934.png](https://i.postimg.cc/KYGjM9mS/imagen-2024-05-23-122006934.png)](https://postimg.cc/FY6htVfD)


### Ejercicio 2.py
#### Codigo
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
#### Comprobacion
[![imagen-2024-05-23-122224949.png](https://i.postimg.cc/59Tg1rVt/imagen-2024-05-23-122224949.png)](https://postimg.cc/SjLCfDj0)


### Ejercicio 3.py
#### Codigo    
      import math
      
      # Definir la función cos(x)
      def f(x):
          return math.cos(x)
      
      # Derivadas de cos(x) en x = 0 alternan entre cos(x), -sin(x), -cos(x), sin(x)
      def f_derivada_orden_n(x, n):
          if n % 4 == 0:
              return math.cos(x)
          elif n % 4 == 1:
              return -math.sin(x)
          elif n % 4 == 2:
              return -math.cos(x)
          else:
              return math.sin(x)
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para cos(x)
      def taylor_series(a, x0, n):
          suma = 0
          for i in range(n):
              término = ((-1) ** i) * ((a - x0) ** (2 * i)) / factorial(2 * i)
              suma += término
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de cos({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
#### Comprobacion
[![imagen-2024-05-23-122404912.png](https://i.postimg.cc/FHQxkJ15/imagen-2024-05-23-122404912.png)](https://postimg.cc/1fJFLXpJ)


### Ejercicio 4.py
#### Codigo
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
#### Comprobacion
[![imagen-2024-05-23-122451557.png](https://i.postimg.cc/MG6bd2y9/imagen-2024-05-23-122451557.png)](https://postimg.cc/ZWQd5QsN)

### Ejercicio 5.py
#### Codigo
      import math
      
      # Definir la función f(x) = x^3 + 2x^2 + x + 1
      def f(x):
          return x**3 + 2*x**2 + x + 1
      
      # Derivadas de f(x) = x^3 + 2x^2 + x + 1
      def f_primera_derivada(x):
          return 3*x**2 + 4*x + 1
      
      def f_segunda_derivada(x):
          return 6*x + 4
      
      def f_tercera_derivada(x):
          return 6
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para f(x) = x^3 + 2x^2 + x + 1
      def taylor_series(a, x0, n):
          suma = f(x0)
          if n > 0:
              suma += f_primera_derivada(x0) * (a - x0) / factorial(1)
          if n > 1:
              suma += f_segunda_derivada(x0) * (a - x0)**2 / factorial(2)
          if n > 2:
              suma += f_tercera_derivada(x0) * (a - x0)**3 / factorial(3)
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de f({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
#### Comprobacion
[![imagen-2024-05-23-122533417.png](https://i.postimg.cc/0jwpb8sy/imagen-2024-05-23-122533417.png)](https://postimg.cc/LgmqWF5c)
