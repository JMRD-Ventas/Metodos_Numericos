import matplotlib.pyplot as plt

def lineal_interpolation(x_values, y_values, x):
    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            x0, y0 = x_values[i], y_values[i]
            x1, y1 = x_values[i + 1], y_values[i + 1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

#Ejemplo de uso
  x_values = [1, 2, 3, 4, 5]
  y_values = [2, 4, 6, 8, 10]
  x = 3.5

     y = lineal_interpolation(x_values, y_values, x)
        print(f"El valor interpolado en x={x} es: {y}")

#Gráfica de los puntos y la interpolación lineal
plt.plot(x_values, y_values, 'o')
plt.plot([x_values[0], x_values[-1]], [lineal_interpolation(x_values, y_values, x_values[0]), lineal_interpolation(x_values, y_values, x_values[-1])], 'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Lineal')
    plt.show()