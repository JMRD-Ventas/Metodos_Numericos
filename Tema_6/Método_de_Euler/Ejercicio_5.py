import numpy as np

def euler(f, y0, t0, t_final, n):
    """
    Resuelve una ecuación diferencial usando el método de Euler.

    Argumentos:
    f -- función que define la ecuación diferencial (dy/dt = f(t, y))
    y0 -- condición inicial para y
    t0 -- valor inicial de t
    t_final -- valor final de t
    n -- número de pasos

    Retorna:
    t -- arreglo de valores de t
    y -- arreglo de valores de y correspondientes a los valores de t
    """
    h = (t_final - t0) / n  # Tamaño del paso
    t = np.linspace(t0, t_final, n + 1)
    y = np.zeros_like(t)
    y[0] = y0

    for i in range(n):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y

# Ejemplo de uso
def ecuacion_diferencial(t, y):
    return 4 * t**3 - 6 * y  # dy/dt = 4t^3 - 6y (ecuación diferencial a resolver)

y0 = 1  # Condición inicial
t0 = 0  # Valor inicial de t
t_final = 3  # Valor final de t
n = 41  # Número de pasos

t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)

# Imprimir resultados
print("t\ty")
for t_val, y_val in zip(t, y):
    print(f"{t_val:.2f}\t{y_val:.4f}")