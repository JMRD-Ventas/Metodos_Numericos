import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, x0, y0, xn, n):
    # Inicializar variables
    x = x0
    y = y0
    h = (xn - x0) / n

    # Vectores para almacenar las soluciones
    x_sol = [x0]
    y_sol = [y0]

    # Iterar para encontrar la siguiente solución
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)

        # Calcular la siguiente solución
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x0 + i * h

        # Almacenar las soluciones
        x_sol.append(x)
        y_sol.append(y)

    return np.array(x_sol), np.array(y_sol)

# Ejemplo de uso
def f(x, y):
    # Ecuación diferencial dy/dx = f(x, y)
    return y * np.cos(x) - 2 * x * y

# Condiciones iniciales
x0 = 0
y0 = 1
xn = 10
n = 100  # Número de pasos

# Llamar a la función runge_kutta4
x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)

# Graficar las soluciones
plt.plot(x_sol, y_sol)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la ecuación diferencial por el método de Runge-Kutta')
plt.grid()
plt.show()