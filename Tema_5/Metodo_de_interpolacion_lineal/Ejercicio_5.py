 def lineal_interpolation(x_values, y_values, x):
for i in range(len(x_values) - 1):
    if x_values[i] <= x <= x_values[i + 1]:
        x0, y0 = x_values[i], y_values[i]
        x1, y1 = x_values[i + 1], y_values[i + 1]
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Leer datos desde un archivo
     with open('datos.txt', 'r') as file:
         data = file.readlines()

            x_values = []
            y_values = []

    for line in data:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)

        x = 3.5  # Valor de x para interpolar

        y = lineal_interpolation(x_values, y_values, x)
        print(f"El valor interpolado en x={x} es: {y}")