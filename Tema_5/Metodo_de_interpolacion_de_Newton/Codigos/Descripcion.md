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