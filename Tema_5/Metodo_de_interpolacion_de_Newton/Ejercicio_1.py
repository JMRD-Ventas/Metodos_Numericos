   from math import factorial

def newton_interpolation(x, y, x_val):
    n = len(x)
    coeff = [0] * n

# Cálculo de los coeficientes
for i in range(n):
    coeff[i] = y[i]
    for j in range(i):
        numer = coeff[i] - coeff[j]
        denom = x[i] - x[j]
        if denom != 0:  # Verificar si el denominador es distinto de cero
            temp_denom = denom
            for k in range(j):
                temp_denom -= (x[i] - x[k])
            if temp_denom != 0:  # Verificar si temp_denom no es cero
                coeff[i] = numer / temp_denom
            else:
                coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero

# Evaluación del polinomio en el punto x_val
p_val = coeff[n-1]
for i in range(n-2, -1, -1):
    p_val = coeff[i] + (x_val - x[i]) * p_val

# Cálculo de la cota de error
error_bound = 0
for i in range(n):
    term = abs(coeff[i])
    for j in range(i):
        term *= abs(x_val - x[j])
    error_bound += term

return p_val, error_bound

# Ejemplo de uso
x = [20, 10, 30, 45,62]  # Ejemplo con valores repetidos en x
y = [22,33,14,54,23]
x_val = 41

p_val, error_bound = newton_interpolation(x, y, x_val)
print(f"Valor interpolado en x={x_val}: {p_val}")
print(f"Cota de error: {error_bound}")
