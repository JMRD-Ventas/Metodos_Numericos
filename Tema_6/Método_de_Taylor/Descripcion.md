# Metodo de Taylor

## ¿Qué es?
El método de Taylor es otro método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDO). Se basa en la expansión en series de Taylor de la solución alrededor de un punto inicial. 

El método de Taylor proporciona una aproximación polinómica de la solución en un intervalo cercano al punto inicial. La precisión de la aproximación depende del orden n de la serie de Taylor utilizada. Cuanto mayor sea n, más precisa será la aproximación, pero también requerirá más cálculos.

Una ventaja del método de Taylor es que no requiere dividir el intervalo en subintervalos, como en el método de Euler o Runge-Kutta. Sin embargo, a medida que nos alejamos del punto inicial, la precisión de la aproximación disminuye, por lo que es necesario repetir el proceso en intervalos más pequeños.

El método de Taylor es particularmente útil cuando se conocen las derivadas analíticas de la función f(x, y), ya que esto simplifica los cálculos. En caso contrario, las derivadas deben calcularse numéricamente, lo que puede introducir errores adicionales.

Es importante tener en cuenta que el método de Taylor puede ser inestable para ciertas ecuaciones diferenciales, especialmente aquellas con soluciones altamente oscilantes o con comportamientos caóticos. En esos casos, puede ser preferible utilizar otros métodos numéricos más robustos.

## Pseudocodigo
El procedimiento para aplicar el método de Taylor es el siguiente:

1. Definir la ecuación diferencial y las condiciones iniciales:
   Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.

2. Calcular las derivadas sucesivas de y con respecto a x utilizando la ecuación diferencial dada:
   y' = f(x, y)
   y'' = (∂f/∂x) + (∂f/∂y)y'
   y''' = (∂^2f/∂x^2) + 2(∂^2f/∂x∂y)y' + (∂^2f/∂y^2)y'y''
   y así sucesivamente.

3. Construir la serie de Taylor de y(x) alrededor del punto x0 hasta el orden deseado n:
   y(x) = y(x0) + y'(x0)(x - x0) + (y''(x0)/2!)(x - x0)^2 + ... + (y^(n)(x0)/n!)(x - x0)^n

4. Evaluar las derivadas y'(x0), y''(x0), ..., y^(n)(x0) utilizando las expresiones obtenidas en el paso 2 y los valores iniciales y(x0) = y0.

5. Sustituir los valores de las derivadas evaluadas en el paso 4 en la serie de Taylor del paso 3.

6. Elegir un valor para x = x1 cercano a x0 y evaluar y(x1) utilizando la serie de Taylor obtenida.

7. Repetir los pasos 4, 5 y 6 para obtener aproximaciones de y en puntos sucesivos x2, x3, ..., xn.
   

### Explicación del pseudocódigo:

1. Se toman como entrada la función f(x, y) que define la ecuación diferencial, los valores iniciales x0 y y0, el valor final xn y el número de subintervalos n.
2. Se calcula el tamaño del paso h dividiendo el intervalo [x0, xn] en n subintervalos iguales.
3. Se inicializan los valores x y y con los valores iniciales x0 y y0, respectivamente.
4. Se realiza un bucle PARA desde i = 0 hasta n-1, donde:
    - Se calcula la pendiente pendiente en el punto actual (x, y) utilizando la función f(x, y).
    - Se actualiza el valor de y sumando h * pendiente al valor anterior de y.
    - Se actualiza el valor de x sumando h al valor anterior de x.
5. Después del bucle, se devuelve el valor final de y, que es la aproximación de la solución en el punto xn.

Este pseudocódigo implementa el método de Euler de forma iterativa. En cada iteración, se calcula la pendiente en el punto actual (x, y) y se utiliza para aproximar el siguiente valor de y utilizando la fórmula y = y + h * pendiente. Luego, se avanza al siguiente punto actualizando x con x = x + h.
Es importante tener en cuenta que este pseudocódigo asume que la ecuación diferencial es de primer orden y que se conocen los valores iniciales x0 y y0. Además, el método de Euler es solo una aproximación numérica, y su precisión dependerá del tamaño del paso h y de la naturaleza de la ecuación diferencial.

## Implementación de los codigos en Python

### Ejercicio 1.py
#### Codigo
#### Comprobacion



### Ejercicio 2.py
#### Codigo
#### Comprobacion



### Ejercicio 3.py
#### Codigo    
#### Comprobacion



### Ejercicio 4.py
#### Codigo
#### Comprobacion



### Ejercicio 5.py
#### Codigo
#### Comprobacion
