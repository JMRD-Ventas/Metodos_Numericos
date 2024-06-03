import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.
    
    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    
    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    """
    n = len(b)
    x = x0.copy()
    
    for iters in range(max_iter):
        x_prev = x.copy()
        
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if i != j:
                    x[i] -= A[i, j] * x[j]
            x[i] /= A[i, i]
        
        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        
        # Verificar criterio de convergencia
        if residuo < tol:
            break
    
    return x, iters+1

# Ejemplo de uso
A = np.array([[4, 1, -1, 1],
              [1, 5, 1, 2],
              [-1, 1, 6, 1],
              [1, 2, 1, 4]])

b = np.array([5, 11, 13, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

x, iters = gauss_seidel(A, b, x0)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
