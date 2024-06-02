import numpy as np
from typing import Callable, Optional, Tuple

def gauss_seidel(
    A: np.ndarray,
    b: np.ndarray,
    x0: np.ndarray,
    tol: float = 1e-6,
    max_iter: int = 100,
    relax: float = 1.0,
    verbose: bool = False,
    stopping_criteria: Optional[Callable[[np.ndarray, np.ndarray], bool]] = None,
) -> Tuple[np.ndarray, int, list]:
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.

    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    relax -- Factor de relajación (float)
    verbose -- Imprime información de cada iteración (bool)
    stopping_criteria -- Función personalizada para detener las iteraciones (Callable[[np.ndarray, np.ndarray], bool])

    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    residuos -- Lista de residuos en cada iteración (list)
    """
    n = len(b)
    x = x0.copy()
    residuos = []

    for iters in range(max_iter):
        x_prev = x.copy()

        for i in range(n):
            sigma = b[i]
            for j in range(n):
                if i != j:
                    sigma -= A[i, j] * x[j]
            x[i] = (1 - relax) * x_prev[i] + relax * (sigma / A[i, i])

        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        residuos.append(residuo)

        # Verificar criterio de convergencia
        if residuo < tol:
            break

        if stopping_criteria is not None and stopping_criteria(x, x_prev):
            break

        if verbose:
            print(f"Iteración {iters+1}: Residuo = {residuo:.6f}")

    if iters == max_iter - 1:
        print("Advertencia: Se alcanzó el número máximo de iteraciones.")

    return x, iters + 1, residuos


# Ejemplo de uso
A = np.array([[4, 1, -1, 1], [1, 5, 1, 2], [-1, 1, 6, 1], [1, 2, 1, 4]])
b = np.array([5, 11, 13, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

# Función de criterio de parada personalizada
def my_stopping_criteria(x: np.ndarray, x_prev: np.ndarray) -> bool:
    diff = np.abs(x - x_prev)
    return np.max(diff) < 1e-4  # Detener si la máxima diferencia es menor que 1e-4

x, iters, residuos = gauss_seidel(
    A,
    b,
    x0,
    tol=1e-8,
    max_iter=200,
    relax=1.2,
    verbose=True,
    stopping_criteria=my_stopping_criteria,
)
print(f"\nSolución aproximada: {x}")
print(f"Número de iteraciones: {iters}")