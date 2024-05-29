# Método de Euler

## ¿Qué es?
El método de Euler es un método numérico simple para aproximar soluciones de ecuaciones diferenciales ordinarias (EDOs) de primer orden. Es uno de los métodos más básicos y fundamentales para resolver EDOs numéricamente.

En esencia, el método de Euler utiliza una aproximación de la derivada utilizando el concepto de la pendiente de la recta tangente a la curva en un punto dado. La idea es avanzar un pequeño paso a lo largo de la recta tangente para obtener una aproximación del siguiente punto en la solución.

## Indice
- [Metodo de Euler](Método_de_Euler/Readme.md)
  - [Ejercicio 1.py](Método_de_Euler/Ejercicio_1.py)
  - [Ejercicio 2.py](Método_de_Euler/Ejercicio_2.py)
  - [Ejercicio 3.py](Método_de_Euler/Ejercicio_3.py)
  - [Ejercicio 4.py](Método_de_Euler/Ejercicio_4.py)
  - [Ejercicio 5.py](Método_de_Euler/Ejercicio_5.py)

------------

# Método de Runge-Kutta

## ¿Qué es?
El método de Runge-Kutta es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) de forma más precisa y eficiente que el método de Euler. Este método fue desarrollado por los matemáticos alemanes C. Runge y M.W. Kutta a principios del siglo XX.

El método de Runge-Kutta se basa en evaluar la pendiente (derivada) en varios puntos dentro de un intervalo small y combinar estas evaluaciones para obtener una mejor aproximación de la solución. Existen varios órdenes del método de Runge-Kutta, siendo el de cuarto orden (RK4) uno de los más utilizados debido a su buen equilibrio entre precisión y eficiencia computacional.

## Indice
- [Metodo Runge-Kutta](Método_de_Runge-Kutta/Readme.md)
  - [Ejercicio 1.py](Método_de_Runge-Kutta/Ejercicio_1.py)
  - [Ejercicio 2.py](Método_de_Runge-Kutta/Ejercicio_2.py)
  - [Ejercicio 3.py](Método_de_Runge-Kutta/Ejercicio_3.py)
  - [Ejercicio 4.py](Método_de_Runge-Kutta/Ejercicio_4.py)
  - [Ejercicio 5.py](Método_de_Runge-Kutta/Ejercicio_5.py)
    
------------

# Método_de_Taylor

## ¿Qué es?
El método de Taylor es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) de orden superior. Se basa en la expansión en serie de Taylor de la solución alrededor de un punto conocido.

La precisión del método depende del número de términos m retenidos en la serie de Taylor y del tamaño del paso h. Cuantos más términos se incluyan, mejor será la aproximación, pero también será más costoso computacionalmente.

Una de las principales ventajas del método de Taylor es que proporciona una solución analítica aproximada en lugar de simplemente evaluar la función en puntos discretos. Sin embargo, tiene la desventaja de requerir el cálculo de derivadas sucesivas, lo cual puede ser complicado para EDOs no lineales.

El método de Taylor es adecuado para EDOs de orden superior cuando se conocen las condiciones iniciales de todas las derivadas hasta el orden n-1. Para EDOs de primer orden, otros métodos como Euler o Runge-Kutta suelen ser más eficientes.La precisión del método depende del número de términos m retenidos en la serie de Taylor y del tamaño del paso h. Cuantos más términos se incluyan, mejor será la aproximación, pero también será más costoso computacionalmente.

Una de las principales ventajas del método de Taylor es que proporciona una solución analítica aproximada en lugar de simplemente evaluar la función en puntos discretos. Sin embargo, tiene la desventaja de requerir el cálculo de derivadas sucesivas, lo cual puede ser complicado para EDOs no lineales.

El método de Taylor es adecuado para EDOs de orden superior cuando se conocen las condiciones iniciales de todas las derivadas hasta el orden n-1. Para EDOs de primer orden, otros métodos como Euler o Runge-Kutta suelen ser más eficientes.

## Indice
- [Metodo Teylor](Método_de_Taylor/Readme.md)
  - [Ejercicio 1.py](Método_de_Taylor/Ejercicio_1.py)
  - [Ejercicio 2.py](Método_de_Taylor/Ejercicio_2.py)
  - [Ejercicio 3.py](Método_de_Taylor/Ejercicio_3.py)
  - [Ejercicio 4.py](Método_de_Taylor/Ejercicio_4.py)
  - [Ejercicio 5.py](Método_de_Taylor/Ejercicio_5.py)


