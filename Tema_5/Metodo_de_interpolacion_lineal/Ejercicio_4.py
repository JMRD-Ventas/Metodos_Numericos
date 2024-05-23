 def f(x):
return x**2

    def lineal_interpolation(x0, x1, x):
    y0 = f(x0)
    y1 = f(x1)
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
      x0 = 1
      x1 = 3
      x = 2

  y = lineal_interpolation(x0, x1, x)
  print(f"El valor interpolado en x={x} es: {y}")