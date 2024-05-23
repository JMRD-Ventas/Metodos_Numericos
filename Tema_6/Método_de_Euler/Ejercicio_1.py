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
    t -- lista de valores de t
    y -- lista de valores de y correspondientes a los valores de t
    """
    h = (t_final - t0) / n  # Tamaño del paso
    t = [t0]
    y = [y0]

    for i in range(n):
        y_nuevo = y[-1] + h * f(t[-1], y[-1])
        t_nuevo = t[-1] + h
        t.append(t_nuevo)
        y.append(y_nuevo)

    return t, y

# Ejemplo de uso
def ecuacion_diferencial(t, y):
    return y  # dy/dt = y (ecuación diferencial a resolver)

y0 = 1  # Condición inicial
t0 = 0  # Valor inicial de t
t_final = 2  # Valor final de t
n = 10  # Número de pasos

t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)

print("t\ty")
for t_val, y_val in zip(t, y):
    print(f"{t_val:.2f}\t{y_val:.4f}")