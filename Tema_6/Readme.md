# Metodo de cuadratico.

## ¿Qué es?
La interpolación consiste en hallar un dato dentro de un intervalo en el que conocemos los valores en los extremos.
El problema general de la interpolación se nos presenta cuando nos dan una función de la cual solo conocemos una serie de puntos de la misma:
(xo, yo), (x1, y1),........., (xn, yn)
## Pseudocodigo.
    Funcion InterpolacionCuadratica(x0, y0, x1, y1, x2, y2, x)
    // Calcula los coeficientes del polinomio cuadrático
    a0 = y0
    a1 = (y1 - y0) / (x1 - x0)
    a2 = ((y2 - y0) / (x2 - x0) - (y1 - y0) / (x1 - x0)) / (x2 - x1)
    
    // Evalúa el polinomio en x
    y = a0 + a1 * (x - x0) + a2 * (x - x0) * (x - x1)
    
    Retornar y
    FinFuncion

    // Ejemplo de uso
    x0 = 1
    y0 = 2
    x1 = 2
    y1 = 3
    x2 = 4
    y2 = 5
    x = 3

    resultado = InterpolacionCuadratica(x0, y0, x1, y1, x2, y2, x)
    Imprimir "El valor interpolado de y en x =", x, "es", resultado


## Implementación de los codigos en Python.
### Ejercicio 1.py
#### Codigo.
    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([1986, 1994, 2001])
    y_points = np.array([4936, 5660, 6226])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 1997
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es     {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobacion.
[![imagen-2024-05-20-192826114.png](https://i.postimg.cc/FFwVVLKY/IMG-20240520-234632.png)

### Ejercicio 2.py
#### Codigo.
   
    #Programa que calcula el precio del dolar en 2016 tomando en cuenta los años 2008, 2012 y 2020
    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([2008, 2012, 2020])
    y_points = np.array([11.13, 12.96, 21.64])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 2016
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 200, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobacion.
[![imagen-2024-05-20-193210020.png](https://i.postimg.cc/1zRG30vj/IMG-20240520-234653.png)

### Ejercicio 3.py
#### Codigo.
    #Programa que calcula la integral x^3 donde x es 4 y 0
    import numpy as np

    # x= intervalo, y= resultado de la integral
    x_points = np.array([2, 3, 5])
    y_points = np.array([4, 20.25, 156.25])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 4
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
    
#### Comprobacion.
[![imagen-2024-05-20-194023521.png](https://i.postimg.cc/0Q8BxJSk/IMG-20240520-235820.png)

### Ejercicio 4.py
#### Codigo.
   
    #Programa que calcula el promedio de vida en años en México durante 1980
    import numpy as np

    # x= año, y= edad promedio
    x_points = np.array([1930, 1970, 2000])
    y_points = np.array([34, 61, 74])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 1980
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobacion.
[![imagen-2024-05-20-194230153.png](https://i.postimg.cc/Fz0dZ1PS/IMG-20240520-234709.png)

### Ejercicio 5.py
#### Codigo.
   
    #Programa que calcula el porcentaje de inflación en México en 2014
    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([2005, 2007, 2021])
    y_points = np.array([3.33, 3.6, 4.65])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 2014
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)

#### Comprobacion.
[![imagen-2024-05-20-194355297.png](https://i.postimg.cc/1RFqPY9z/IMG-20240520-234727.png)

# Metodo de Lagrange.

## ¿Qué es?
El método de interpolación de Lagrange es una técnica matemática utilizada para encontrar un polinomio que pase a través de un conjunto dado de puntos de datos. Este polinomio se denomina polinomio interpolador de Lagrange.

La idea básica del método de Lagrange es construir un polinomio de grado n-1 (donde n es el número de puntos de datos) que coincida con los valores de la función en esos puntos de datos. Matemáticamente, el polinomio interpolador de Lagrange se define como:
    
    P(x) = y₁L₁(x) + y₂L₂(x) + ... + yₙLₙ(x)
    
Donde: 

y₁, y₂, ..., yₙ son los valores de la función en los puntos de datos (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ).
L₁(x), L₂(x), ..., Lₙ(x) son los polinomios de Lagrange de grado n-1, definidos como:
    
    Lᵢ(x) = ∏(k≠i) (x - xₖ) / (xᵢ - xₖ)
    
Estos polinomios de Lagrange tienen la propiedad de que Lᵢ(xⱼ) = 1 si i = j, y Lᵢ(xⱼ) = 0 si i ≠ j.
    
Una vez construido el polinomio interpolador de Lagrange P(x), puede utilizarse para aproximar el valor de la función en cualquier punto x dentro del intervalo definido por los puntos de datos.
    
El método de interpolación de Lagrange es ampliamente utilizado en diversas áreas, como análisis numérico, cálculo computacional, procesamiento de señales, etc. Sin embargo, tiene algunas limitaciones, como el hecho de que puede presentar oscilaciones indeseables (fenómeno de Runge) cuando se interpola en un intervalo grande con puntos de datos no uniformemente distribuidos.
    
Es importante tener en cuenta que la interpolación de Lagrange solo proporciona una aproximación de la función real, y la precisión de la aproximación depende de la distribución y el número de puntos de datos disponibles.


## Pseudocodigo.
    función LagrangeInterpolation(x, y, n, x_eval):
      # x e y son los vectores de puntos de datos
      # n es el número de puntos de datos
      # x_eval es el valor de x en el que se desea evaluar el polinomio interpolador
  
      P(x) = 0  # Inicializar el polinomio interpolador
  
      para i desde 1 hasta n:
          Li(x) = 1  # Inicializar el polinomio de Lagrange para el punto i
          para j desde 1 hasta n:
              si j != i:
                  Li(x) = Li(x) * (x - x[j]) / (x[i] - x[j])
          P(x) = P(x) + y[i] * Li(x)
  
      valor_interpolado = evaluar P(x) en x_eval
  
      devolver valor_interpolado

## Implementación de los codigos en Python.
### Ejercicio 1.py
#### Codigo.
   
        import math
        def lagrange_interpolation(x, y, x_val):
            n = len(x)
            y_val = 0
            error_bound = 0
        
            for i in range(n):
                term = y[i]
                for j in range(n):
                    if i != j:
                        term = term * (x_val - x[j]) / (x[i] - x[j])
                y_val += term
        
            # Calcular la cuota de error
            min_diff = min(abs(x_val - x[i]) for i in range(n))
            max_diff = max(abs(x_val - x[i]) for i in range(n))
            max_y_diff = max(abs(y[i]) for i in range(n))
        
            for k in range(n):
                prod = 1
                for i in range(n):
                    if i != k:
                        prod *= max_diff / abs(x[k] - x[i])
                error_bound += max_y_diff * prod
        
            return y_val, error_bound
        
        # Ejemplo de uso
        x = [20, 10, 30, 45, 62]
        y = [22, 33, 14, 54, 23]
        x_val = 41
        
        y_approx, error_bound = lagrange_interpolation(x, y, x_val)
        
        print(f"Valor aproximado en x={x_val}: {y_approx}")
        print(f"Cuota de error: {error_bound}")
#### Comprobacion.
[![imagen-2024-05-20-192826114.png](https://i.postimg.cc/RZZ66vVF/imagen-2024-05-20-192826114.png)](https://postimg.cc/TpBYBMbM)

### Ejercicio 2.py
#### Codigo.
   
    import math
    
    def lagrange_interpolation(x, y, x_val):
        n = len(x)
        y_val = 0
        error_bound = 0
    
        for i in range(n):
            term = y[i]
            for j in range(n):
                if i != j:
                    term = term * (x_val - x[j]) / (x[i] - x[j])
            y_val += term
    
        # Calcular la cuota de error
        min_diff = min(abs(x_val - x[i]) for i in range(n))
        max_diff = max(abs(x_val - x[i]) for i in range(n))
        max_y_diff = max(abs(y[i]) for i in range(n))
    
        for k in range(n):
            prod = 1
            for i in range(n):
                if i != k:
                    prod *= max_diff / abs(x[k] - x[i])
            error_bound += max_y_diff * prod
    
        return y_val, error_bound
    
    # Ejemplo de uso
    x = [0, 1, 2, 3]
    y = [1, 2, 4, 8]
    x_val = 1.5
    
    y_approx, error_bound = lagrange_interpolation(x, y, x_val)
    
    print(f"Valor aproximado en x={x_val}: {y_approx}")
    print(f"Cuota de error: {error_bound}")
    
#### Comprobacion.
[![imagen-2024-05-20-193210020.png](https://i.postimg.cc/1RK3pbdN/imagen-2024-05-20-193210020.png)](https://postimg.cc/fkJssqDw)

### Ejercicio 3.py
#### Codigo.
   
    def lagrange_interpolation(x_values, y_values, x):
        n = len(x_values)
        y_interp = 0
        error_bound = 0
    
        # Calcular los coeficientes de Lagrange
        for i in range(n):
            basis = 1
            for j in range(n):
                if i != j:
                    basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
            y_interp += y_values[i] * basis
    
        # Calcular la cuota de error
        max_diff = max(abs(x - x_values[i]) for i in range(n))
        max_y_diff = max(abs(y_values[i]) for i in range(n))
        error_bound = max_y_diff * sum(abs(prod(x_values, i, x, n)) for i in range(n))
    
        return y_interp, error_bound
    
    def prod(x_values, i, x, n):
        term = 1
        for j in range(n):
            if j != i:
                term *= abs(x - x_values[j]) / abs(x_values[i] - x_values[j])
        return term
    
    # Ejemplo de uso
    x_values = [13, 46, 79, 80]
    y_values = [73, 81, 42, 20,]
    x = 10
    
    y_interp, error_bound = lagrange_interpolation(x_values, y_values, x)
    
    print(f"Valor interpolado en x={x}: {y_interp}")
    print(f"Cuota de error: {error_bound}")
    
#### Comprobacion.
[![imagen-2024-05-20-194023521.png](https://i.postimg.cc/N0bd8sRz/imagen-2024-05-20-194023521.png)](https://postimg.cc/XZGK40Hf)

### Ejercicio 4.py
#### Codigo.
   
    import numpy as np
    
    def lagrange_interpolation(x_values, y_values, x):
        n = len(x_values)
        L = np.zeros(n)
        y_interp = 0
        error_bound = 0
    
        for i in range(n):
            prod_num = 1
            prod_den = 1
            for j in range(n):
                if i != j:
                    prod_num *= (x - x_values[j])
                    prod_den *= (x_values[i] - x_values[j])
            L[i] = prod_num / prod_den
            y_interp += y_values[i] * L[i]
    
        # Calcular la cuota de error
        max_diff = max(abs(x - x_values[i]) for i in range(n))
        max_y_diff = max(abs(y_values[i]) for i in range(n))
        error_bound = max_y_diff * sum(abs(L[i]) for i in range(n))
    
        return y_interp, error_bound
    
    # Ejemplo de uso
    x_values = [12, 41, 23, 21, 63]
    y_values = [12, 23, 34, 45, 56 ]
    x = 49
    
    y_interp, error_bound = lagrange_interpolation(x_values, y_values, x)
    
    print(f"Valor interpolado en x={x}: {y_interp}")
    print(f"Cuota de error: {error_bound}")
   
#### Comprobacion.
[![imagen-2024-05-20-194230153.png](https://i.postimg.cc/V5ygsdcd/imagen-2024-05-20-194230153.png)](https://postimg.cc/T59gC216)

### Ejercicio 5.py
#### Codigo.
   
    import numpy as np
    
    def lagrange_interpolation(x_values, y_values, x):
        n = len(x_values)
        L = np.zeros(n)
        y_interp = 0
        error_bound = 0
    
        for i in range(n):
            prod_num = 1
            prod_den = 1
            for j in range(n):
                if i != j:
                    prod_num *= (x - x_values[j])
                    prod_den *= (x_values[i] - x_values[j])
            L[i] = prod_num / prod_den
            y_interp += y_values[i] * L[i]
    
        # Calcular la cuota de error
        max_diff = max(abs(x - x_values[i]) for i in range(n))
        max_y_diff = max(abs(y_values[i]) for i in range(n))
        error_bound = max_y_diff * sum(abs(L[i]) for i in range(n))
    
        return y_interp, error_bound
    
    # Ejemplo de uso
    x_values = [10, 98, 23, 78,54]
    y_values = [14, 25, 36, 20, 58]
    x = 35
    
    y_interp, error_bound = lagrange_interpolation(x_values, y_values, x)
    
    print(f"Valor interpolado en x={x}: {y_interp}")
    print(f"Cuota de error: {error_bound}")

#### Comprobacion.
[![imagen-2024-05-20-194355297.png](https://i.postimg.cc/J7yWhvLL/imagen-2024-05-20-194355297.png)](https://postimg.cc/hhqYyCvy)

# Metodo de Newton.

## ¿Qué es?

El método de interpolación de Newton es una técnica matemática utilizada para encontrar un polinomio que pase a través de un conjunto dado de puntos de datos. Este polinomio se denomina polinomio interpolador de Newton.
La idea básica del método de Newton es construir un polinomio de grado n-1 (donde n es el número de puntos de datos) que coincida con los valores de la función en esos puntos de datos. El polinomio interpolador de Newton se expresa como una suma de términos, donde cada término contiene un coeficiente y una potencia de (x - x₀), siendo x₀ el primer punto de datos.

    P(x) = a₀ + a₁(x - x₀) + a₂(x - x₀)(x - x₁) + ... + aₙ(x - x₀)(x - x₁)...(x - xₙ₋₁)    
Donde:
    P(x) es el polinomio interpolador de Newton.
    x₀, , , ...,  son los valores de la variable independiente (puntos de datos).x₁x₂xₙ
    a₀, , , ...,  son los coeficientes del polinomio interpolador.a₁a₂aₙ
    n es el número de puntos de datos (grado del polinomio es ).n-1

Los coeficientes , , , ...,  se calculan utilizando las diferencias divididas de Newton de la siguiente manera:a₀a₁a₂aₙ
  a₀ = f(x₀)
a₁ = f[x₀, x₁]
a₂ = f[x₀, x₁, x₂]
...
aₙ = f[x₀, x₁, x₂, ..., xₙ]
Donde  representa la diferencia dividida de orden  de la función  en los puntos , , ..., . Las diferencias divididas se calculan recursivamente mediante la fórmula:f[x₀, x₁, ..., xₖ]kfx₀x₁xₖ
    f[x₀, x₁, ..., xₖ] = (f[x₁, x₂, ..., xₖ] - f[x₀, x₁, ..., xₖ₋₁]) / (xₖ - x₀)
## Pseudocodigo.
     función NewtonInterpolation(x, y, x_eval):
        # x e y son los vectores de puntos de datos
        # x_eval es el valor de x en el que se desea evaluar el polinomio interpolador
        n = longitud de x
        coeff = vector de longitud n  # Coeficientes del polinomio interpolador

    # Calcular los coeficientes
    para i desde 0 hasta n-1:
        coeff[i] = y[i]  # Inicializar con los valores de y
        para j desde 0 hasta i-1:
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:
                temp_denom = denom
                para k desde 0 hasta j-1:
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:
                    coeff[i] = numer / temp_denom

    # Evaluar el polinomio en el punto x_eval
    p_val = coeff[n-1]
    para i desde n-2 hasta 0 con paso -1:
        p_val = coeff[i] + (x_eval - x[i]) * p_val

    devolver p_val

## Implementación de los codigos en Python.
### Ejercicio1.py
#### Codigo.
       from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [20, 10, 30, 45,62]  # Ejemplo con valores repetidos en x
    y = [22,33,14,54,23]
    x_val = 41
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
       

#### Comprobacion.
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/24706c86-af2c-4768-a363-f95bb1b023fd)
### Ejercicio 2.py
#### Codigo.
   
    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [0,1,2,3]  # Ejemplo con valores repetidos en x
    y = [1,2,4,8]
    x_val = 1.5
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
    
#### Comprobacion.
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/72371790-42c3-4949-95d5-56e4666f28c2)

### Ejercicio 3.py
#### Codigo.
   
    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [13,46,79,80]  # Ejemplo con valores repetidos en x
    y = [73,81,42,20]
    x_val = 25
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
    
#### Comprobacion.
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/bd2aebd1-5f19-402d-b8eb-a6a2e71e1706)

### Ejercicio 4.py
#### Codigo.
   
    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [12,41,23,21,63]  # Ejemplo con valores repetidos en x
    y = [12,23,34,45,56]
    x_val = 49
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
   
#### Comprobacion.
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/d7e25481-f890-4c87-b639-e95f1f01e3af)

### Ejercicio 5.py
#### Codigo.
   
    from math import factorial

    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [10,98,23,78,54]  # Ejemplo con valores repetidos en x
    y = [14,25,36,20,58]
    x_val = 35
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
#### Comprobacion.
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/3d4bdc6f-500d-4c2b-8e31-313eeb36bd4f)

# Metodo de la interpolación lineal

## ¿Qué es?

La interpolación lineal es un caso en donde se usa un polinomio de primer grado, es decir una función lineal o afín, para adivinar el valor de la función en un punto.


## Pseudocodigo.

    Función InterpolacionLineal(x0, y0, x1, y1, x):
        Entrada: x0, y0: coordenadas del primer punto
            x1, y1: coordenadas del segundo punto
             x: valor de x para el cual se quiere interpolar
        Salida: valor interpolado y en x

        Calcular la pendiente de la recta que pasa por los dos puntos
        pendiente = (y1 - y0) / (x1 - x0)

        Calcular el valor interpolado utilizando la ecuación de la recta
        y = y0 + pendiente * (x - x0)

        Devolver y
    Fin Función

        Programa Principal:
        Leer x0, y0, x1, y1, x

        y = InterpolacionLineal(x0, y0, x1, y1, x)

        Imprimir "El valor interpolado en x =", x, "es:", y
    Fin Programa

## Implementación de los codigos en Python.
### Ejercicio 1.py
#### Codigo.
   
    def lineal_interpolation(x_values, y_values, x):
        for i in range(len(x_values) - 1):
            if x_values[i] <= x <= x_values[i + 1]:
                x0, y0 = x_values[i], y_values[i]
                x1, y1 = x_values[i + 1], y_values[i + 1]
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]
    x = 3.5

    y = lineal_interpolation(x_values, y_values, x)
    print(f"El valor interpolado en x={x} es: {y}")

#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224700.png](https://i.postimg.cc/qRBfNB5T/Captura-de-pantalla-2024-05-20-224700.png)](https://postimg.cc/wtr4Pzzf)

### Ejercicio 2.py
#### Codigo.
   
    def lineal_interpolation(x0, y0, x1, y1, x):
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x0 = 1
    y0 = 2
    x1 = 5
    y1 = 10
    x = 3

    y = lineal_interpolation(x0, y0, x1, y1, x)
    print(f"El valor interpolado en x={x} es: {y}")
    
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224745.png](https://i.postimg.cc/yxWwTQKp/Captura-de-pantalla-2024-05-20-224745.png)](https://postimg.cc/K3SqG5Rt)

### Ejercicio 3.py
#### Codigo.
   
     import matplotlib.pyplot as plt

    def lineal_interpolation(x_values, y_values, x):
        for i in range(len(x_values) - 1):
            if x_values[i] <= x <= x_values[i + 1]:
                x0, y0 = x_values[i], y_values[i]
                x1, y1 = x_values[i + 1], y_values[i + 1]
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]
    x = 3.5

    y = lineal_interpolation(x_values, y_values, x)
    print(f"El valor interpolado en x={x} es: {y}")

    #Gráfica de los puntos y la interpolación lineal
    plt.plot(x_values, y_values, 'o')
    plt.plot([x_values[0], x_values[-1]], [lineal_interpolation(x_values, y_values, x_values[0]), lineal_interpolation(x_values, y_values, x_values[-1])], 'r--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación Lineal')
        plt.show()
    
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224835.png](https://i.postimg.cc/Qx2RpJyS/Captura-de-pantalla-2024-05-20-224835.png)](https://postimg.cc/D8cjhLFb)

### Ejercicio 4.py
#### Codigo.

     def f(x):
    return x**2

        def lineal_interpolation(x0, x1, x):
        y0 = f(x0)
        y1 = f(x1)
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

        #Ejemplo de uso
    x0 = 1
    x1 = 3
    x = 2

    y = lineal_interpolation(x0, x1, x)
    print(f"El valor interpolado en x={x} es: {y}")

   
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224911.png](https://i.postimg.cc/Xv8m6S7D/Captura-de-pantalla-2024-05-20-224911.png)](https://postimg.cc/zLy0TQhn)
### Ejercicio 5.py
#### Codigo.

     def lineal_interpolation(x_values, y_values, x):
    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            x0, y0 = x_values[i], y_values[i]
            x1, y1 = x_values[i + 1], y_values[i + 1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

        #Leer datos desde un archivo
         with open('datos.txt', 'r') as file:
             data = file.readlines()

                x_values = []
                y_values = []

        for line in data:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)

            x = 3.5  # Valor de x para interpolar

            y = lineal_interpolation(x_values, y_values, x)
            print(f"El valor interpolado en x={x} es: {y}")

#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224955.png](https://i.postimg.cc/MHcFBn0h/Captura-de-pantalla-2024-05-20-224955.png)](https://postimg.cc/hQBsWP5r)
