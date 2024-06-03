import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    L = np.zeros(n)
    y_interp = 0
    error_bound = 0

    for i in range(n):
        prod_num = 1
        prod_den = 1
        for j in range(n):
            if i != j:
                prod_num *= (x - x_values[j])
                prod_den *= (x_values[i] - x_values[j])
        L[i] = prod_num / prod_den
        y_interp += y_values[i] * L[i]

    # Calcular la cuota de error
    max_diff = max(abs(x - x_values[i]) for i in range(n))
    max_y_diff = max(abs(y_values[i]) for i in range(n))
    error_bound = max_y_diff * sum(abs(L[i]) for i in range(n))

    return y_interp, error_bound

# Ejemplo de uso
x_values = [10, 98, 23, 78,54]
y_values = [14, 25, 36, 20, 58]
x = 35

y_interp, error_bound = lagrange_interpolation(x_values, y_values, x)

print(f"Valor interpolado en x={x}: {y_interp}")
print(f"Cuota de error: {error_bound}")