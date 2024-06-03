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
