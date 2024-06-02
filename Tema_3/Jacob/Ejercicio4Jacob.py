import numpy as np

def jacobi_method(A, b, tol=1e-6, max_iter=1000):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Jacobi.
    
    Parámetros:
    A (numpy.ndarray): La matriz de coeficientes del sistema de ecuaciones.
    b (numpy.ndarray): El vector de términos independientes.
    tol (float, opcional): La tolerancia para el criterio de convergencia. Por defecto es 1e-6.
    max_iter (int, opcional): El número máximo de iteraciones. Por defecto es 1000.
    
    Devuelve:
    numpy.ndarray: La solución del sistema de ecuaciones.
    """
    n = len(b)
    x = np.zeros(n)
    
    for iter in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if j != i:
                    s -= A[i, j] * x[j]
            x_new[i] = s / A[i, i]
        
        if np.max(np.abs(x_new - x)) < tol:
            return x_new
        
        x = x_new
    
    return x

# Ejemplo de uso
A = np.array([[4, 1, 1], [1, 3, 1], [1, 1, 3]])
b = np.array([6, 4, 6])

x = jacobi_method(A, b)
print("Solución:", x)
