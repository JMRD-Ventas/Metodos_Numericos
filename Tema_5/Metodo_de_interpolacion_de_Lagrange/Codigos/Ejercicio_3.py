def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    y_interp = 0
    error_bound = 0

    # Calcular los coeficientes de Lagrange
    for i in range(n):
        basis = 1
        for j in range(n):
            if i != j:
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
        y_interp += y_values[i] * basis

    # Calcular la cota de error
    max_diff = max(abs(x - x_values[i]) for i in range(n))
    max_y_diff = max(abs(y_values[i]) for i in range(n))
    error_bound = max_y_diff * sum(abs(prod(x_values, i, x, n)) for i in range(n))

    return y_interp, error_bound

def prod(x_values, i, x, n):
    term = 1
    for j in range(n):
        if j != i:
            term *= abs(x - x_values[j]) / abs(x_values[i] - x_values[j])
    return term

# Ejemplo de uso
x_values = [13, 46, 79, 80]
y_values = [73, 81, 42, 20,]
x = 10

y_interp, error_bound = lagrange_interpolation(x_values, y_values, x)

print(f"Valor interpolado en x={x}: {y_interp}")
print(f"Couta de error: {error_bound}")