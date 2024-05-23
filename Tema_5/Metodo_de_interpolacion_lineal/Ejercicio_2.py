def lineal_interpolation(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

#Ejemplo de uso
x0 = 1
y0 = 2
x1 = 5
y1 = 10
x = 3

y = lineal_interpolation(x0, y0, x1, y1, x)
print(f"El valor interpolado en x={x} es: {y}")