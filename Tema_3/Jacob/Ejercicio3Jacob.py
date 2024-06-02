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