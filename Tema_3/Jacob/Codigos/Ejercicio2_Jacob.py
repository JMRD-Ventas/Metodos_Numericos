import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    """
    Método de Jacobi para resolver el sistema de ecuaciones lineales Ax = b.
    
    Parámetros:
    A -- matriz de coeficientes (numpy array de dimensiones n x n)
    b -- vector de términos independientes (numpy array de dimensiones n)
    x0 -- vector inicial (numpy array de dimensiones n)
    tol -- tolerancia para el criterio de convergencia
    max_iter -- número máximo de iteraciones
    
    Devuelve:
    x -- vector solución (numpy array de dimensiones n)
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for iteration in range(max_iter):
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i][i]

        # Verificar la convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f'Convergencia alcanzada en {iteration + 1} iteraciones.')
            return x_new

        x = x_new.copy()

    print('Número máximo de iteraciones alcanzado.')
    return x

# Ejemplo de uso
A = np.array([[4, -1, 0, 0], 
              [-1, 4, -1, 0], 
              [0, -1, 4, -1], 
              [0, 0, -1, 3]], dtype=float)
b = np.array([15, 10, 10, 10], dtype=float)
x0 = np.zeros(len(b))

solucion = jacobi(A, b, x0)
print('Solución:', solucion)
