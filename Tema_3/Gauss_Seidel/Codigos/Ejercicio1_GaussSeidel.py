import numpy as np

def gauss_seidel(A, b, x0, tol, maxiter):
    """
    Función para resolver un sistema de ecuaciones lineales Ax = b
    utilizando el método de Gauss-Seidel.

    Argumentos:
    A -- Matriz de coeficientes del sistema
    b -- Vector de términos independientes
    x0 -- Vector inicial de aproximación
    tol -- Tolerancia para detener las iteraciones
    maxiter -- Número máximo de iteraciones

    Retorna:
    x -- Solución aproximada del sistema
    iters -- Número de iteraciones realizadas
    """
    n = len(b)  # Tamaño del sistema
    x = x0.copy()  # Inicializar vector solución

    for iter in range(maxiter):
        x_old = x.copy()  # Guardar valor anterior de x

        for i in range(n):
            sum = b[i]
            for j in range(n):
                if i != j:
                    sum -= A[i, j] * x[j]
            x[i] = sum / A[i, i]

        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_old)

        # Verificar criterio de convergencia
        if residuo < tol:
            break

    return x, iter + 1

# Ejemplo de uso
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
x0 = np.array([0, 0, 0, 0])  # Vector inicial
tol = 1e-6  # Tolerancia
maxiter = 100  # Número máximo de iteraciones

x, iters = gauss_seidel(A, b, x0, tol, maxiter)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
