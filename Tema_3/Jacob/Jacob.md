# Metodo de Jacob
  ## ¿Que es?
  El método de Jacob (también conocido como el método de iteración de Jacobianos o el método de Jacobi) es 
  un algoritmo utilizado para resolver sistemas de ecuaciones lineales. Es un método iterativo que se utiliza 
  para aproximar la solución de sistemas de ecuaciones lineales, especialmente cuando estos sistemas son grandes 
  y sparse (es decir, tienen muchos ceros).
    
  El método de Jacob se basa en descomponer la matriz del sistema en una suma de una matriz diagonal y el resto 
  de la matriz. Luego, iterativamente, se resuelve un sistema de ecuaciones en el que la matriz del sistema es la 
  matriz diagonal y se actualizan las soluciones en cada iteración.
    
  El proceso se repite hasta que se alcanza una precisión deseada o se cumple algún otro criterio de convergencia. 
  Aunque el método de Jacob puede ser relativamente simple y fácil de implementar, puede converger lentamente para 
  ciertos tipos de sistemas de ecuaciones. Sin embargo, es útil como paso en métodos más avanzados como el método de 
  Gauss-Seidel o el método de relajación.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por 
  filas, lo que facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.

## Pasos
  ### 1. Preparación inicial: 
  - Antes de comenzar, necesitas tener tu sistema de ecuaciones lineales en forma matricial. Es decir, necesitas tener 
    todas las variables y constantes organizadas en una matriz.

  ### 2. Descomposición de la matriz: 
  - Divide la matriz de coeficientes en dos partes: una matriz diagonal y el resto de la matriz. La matriz diagonal son 
    los elementos de la diagonal principal de la matriz original, y el resto son los elementos que no están en la diagonal 
    principal.

  ### 3. Iniciar con una suposición inicial: 
  - Comienza con una suposición inicial para las soluciones de tus variables. Esto podría ser cualquier valor, pero es 
    común empezar con todos los valores en cero.

  ### 4. Iteración: 
  - Ahora, para cada variable en tu sistema, usa la fila correspondiente en la matriz de coeficientes y las soluciones 
    actuales de las otras variables (usando la suposición inicial para la primera iteración) para calcular una nueva 
    estimación para esa variable. Repite este proceso para cada variable.

  ### 5. Actualización de las soluciones: 
  - Después de calcular una nueva estimación para cada variable, actualiza tus soluciones actuales con estas nuevas estimaciones.

  ### 6. Comprobación de convergencia: 
  - Repite los pasos 4 y 5 hasta que tus soluciones converjan a una precisión aceptable. Esto significa que las soluciones no 
    cambian mucho entre iteraciones.

  ### 7. Verificación de la solución: 
  - Una vez que has alcanzado la convergencia, verifica tus soluciones sustituyéndolas en las ecuaciones originales para asegurarte 
  de que satisfacen todas las ecuaciones.

  ### 8. Finalización: 
  - Si tus soluciones son aceptables, entonces has resuelto tu sistema de ecuaciones utilizando el método de Jacob.

Recuerda que la velocidad de convergencia puede variar dependiendo de la naturaleza del sistema de ecuaciones, y puede que necesites ajustar la precisión o la suposición inicial para obtener resultados satisfactorios.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

```python
import numpy as np


def jacobi(A, b, x0, tol, N):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Argumentos:
    A -- matriz de coeficientes
    b -- vector de términos independientes
    x0 -- vector inicial de aproximación
    tol -- tolerancia
    N -- número máximo de iteraciones
    """
    x = x0.copy()
    n = len(b)
    
    for i in range(N):
        x_prev = x.copy()
        for j in range(n):
            sum = b[j]
            for k in range(n):
                if k != j:
                    sum -= A[j, k] * x_prev[k]
            x[j] = sum / A[j, j]
        
        if np.linalg.norm(x - x_prev, np.inf) < tol:
            break
    
    return x


# Ejemplo de uso
A = np.array([[4, 1, -1, 1], [1, 5, 1, -1], [-1, 1, 6, 1], [1, -1, 1, 7]])
b = np.array([5, 7, 9, 11])
x0 = np.array([0, 0, 0, 0])
tol = 1e-6
N = 100


x = jacobi(A, b, x0, tol, N)
print("Solución aproximada:", x)
```

#### Comprobacion
[![image.png](https://i.postimg.cc/HLhfwCWY/image.png)](https://postimg.cc/4KpLGqhq)

### Ejercicio 2
#### Metodologia en codigo

```python
def sensitivity_analysis(A, b, x0, tol, max_iterations, delta):
    original_solution, _ = jacobi(A, b, x0, tol, max_iterations)
    sensitivity_results = []
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A_mod = A.copy()
            A_mod[i, j] += delta
            new_solution, _ = jacobi(A_mod, b, x0, tol, max_iterations)
            sensitivity_results.append((i, j, new_solution))
    
    for i in range(len(b)):
        b_mod = b.copy()
        b_mod[i] += delta
        new_solution, _ = jacobi(A, b_mod, x0, tol, max_iterations)
        sensitivity_results.append((i, 'b', new_solution))
    
    return original_solution, sensitivity_results


# Ejemplo
delta = 0.1
original_sol, sensitivity_results = sensitivity_analysis(A, b, x0, tol, max_iterations, delta)
print(f"Solución original: {original_sol}")
for result in sensitivity_results:
    print(f"Modificación en {result[0]}, {result[1]}: {result[2]}")

```

#### Comprobacion
[![image.png](https://i.postimg.cc/7PcpG4sm/image.png)](https://postimg.cc/grVMQCPZ)

### Ejercicio 3
#### Metodologia en codigo

```python
import numpy as np


def jacobi(A, b, x0, tol, max_iterations):
    n = len(b)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iterations


# Ejemplo
A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
b = np.array([15, 10, 10, 10])
x0 = np.zeros_like(b)
tol = 1e-10
max_iterations = 100


sol, iterations = jacobi(A, b, x0, tol, max_iterations)
print(f"Solución: {sol}")
print(f"Iteraciones: {iterations}")

```

#### Comprobacion
[![image.png](https://i.postimg.cc/v8WNBnnH/image.png)](https://postimg.cc/s1gcHvKt)

### Ejercicio 4
#### Metodologia en codigo

```python
import numpy as np


def jacobi(A, b, x0, tol, N):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Argumentos:
    A -- matriz de coeficientes
    b -- vector de términos independientes
    x0 -- vector inicial de aproximación
    tol -- tolerancia
    N -- número máximo de iteraciones
    """
    x = x0.copy()
    n = len(b)
    
    for i in range(N):
        x_prev = x.copy()
        for j in range(n):
            sum = b[j]
            for k in range(n):
                if k != j:
                    sum -= A[j, k] * x_prev[k]
            x[j] = sum / A[j, j]
        
        if np.linalg.norm(x - x_prev, np.inf) < tol:
            break
    
    return x


# Ejemplo de uso
A = np.array([[10, -1, 2], [1, 11, -1], [2, -1, 10]])
b = np.array([27, 25, 27])
x0 = np.array([0, 0, 0])
tol = 1e-6
N = 100


x = jacobi(A, b, x0, tol, N)
print(x)
```

#### Comprobacion
[![image.png](https://i.postimg.cc/rpr9H6CF/image.png)](https://postimg.cc/nsn7sPP6)

### Ejercicio 5
#### Metodologia en codigo

```python
import numpy as np
from scipy.sparse import csr_matrix


def jacobi(A, b, x0, tol, N):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Argumentos:
    A -- matriz de coeficientes (scipy.sparse.csr_matrix)
    b -- vector de términos independientes
    x0 -- vector inicial de aproximación
    tol -- tolerancia
    N -- número máximo de iteraciones
    """
    x = x0.copy()
    n = len(b)
    
    for i in range(N):
        x_prev = x.copy()
        for j in range(n):
            sum = b[j]
            for k in range(n):
                if k != j:
                    sum -= A[j, k] * x_prev[k]
            x[j] = sum / A[j, j]
        
        if np.linalg.norm(x - x_prev, np.inf) < tol:
            break
    
    return x


# Ejemplo de uso
A_data = np.array([10, 1, 2, 1, 11, 1, 2, 1, 9, 1, 2, 1, 12, 1, 2, 1, 10])
A_row = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
A_col = np.array([0, 1, 4, 0, 2, 4, 1, 2, 4, 1, 3, 4, 0, 2, 3])
A = csr_matrix((A_data, (A_row, A_col)), shape=(5, 5))


b = np.array([14, 15, 11, 16, 13])
x0 = np.array([0, 0, 0, 0, 0])
tol = 1e-6
N = 100


x = jacobi(A, b, x0, tol, N)
print(x)
```

#### Comprobacion
[![image.png](https://i.postimg.cc/NjW6mJqh/image.png)](https://postimg.cc/QFJKrqdS)

## Implementacion y ejercicios
[Ejercicios del metodo de Jacob](https://docs.google.com/spreadsheets/d/1pCUyxeDHE9aHkJPAhAWR9iPFlqWY9MG939s1Q2w7AOs/edit?usp=sharing)
