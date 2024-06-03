import numpy as np

def jacobi(A, b, x0, tol, N):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Parámetros:
    A (numpy.ndarray): La matriz de coeficientes del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    x0 (numpy.ndarray): Una aproximación inicial de la solución.
    tol (float): La tolerancia para determinar la convergencia.
    N (int): El número máximo de iteraciones.
    
    Devuelve:
    x (numpy.ndarray): La solución aproximada.
    k (int): El número de iteraciones realizadas.
    """
    n = len(b)
    x = x0.copy()
    
    for k in range(N):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i, j] * x[j]
            x_new[i] = s / A[i, i]
        
        if np.linalg.norm(x_new - x, np.inf) < tol:
            break
        
        x = x_new
    
    return x, k + 1

# Ejemplo de uso
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
x0 = np.array([0, 0, 0, 0])  # Aproximación inicial
tol = 1e-6
N = 100

x, k = jacobi(A, b, x0, tol, N)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {k}")
