import math

def lagrange_interpolation(x, y, x_val):
    n = len(x)
    y_val = 0
    error_bound = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (x_val - x[j]) / (x[i] - x[j])
        y_val += term

    # Calcular la cota de error
    min_diff = min(abs(x_val - x[i]) for i in range(n))
    max_diff = max(abs(x_val - x[i]) for i in range(n))
    max_y_diff = max(abs(y[i]) for i in range(n))

    for k in range(n):
        prod = 1
        for i in range(n):
            if i != k:
                prod *= max_diff / abs(x[k] - x[i])
        error_bound += max_y_diff * prod

    return y_val, error_bound

# Ejemplo de uso
x = [20, 10, 30, 45, 62]
y = [22, 33, 14, 54, 23]
x_val = 41

y_approx, error_bound = lagrange_interpolation(x, y, x_val)

print(f"Valor aproximado en x={x_val}: {y_approx}")
print(f"Couta de error: {error_bound}")