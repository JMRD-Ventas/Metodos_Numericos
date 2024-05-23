# Metodo de cuadratico.

## ¿Qué es?
El método de Euler es un método numérico simple y ampliamente utilizado para resolver ecuaciones diferenciales ordinarias (EDO) de forma aproximada. Se basa en la idea de utilizar una línea tangente a la curva solución en un punto dado para aproximar el valor de la solución en un punto cercano. A continuación, describiré los pasos del método de Euler:

1. Definir la ecuación diferencial y las condiciones iniciales: Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.

2. Dividir el intervalo de interés [x0, xn] en n subintervalos iguales de tamaño h = (xn - x0) / n.

3. Inicializar los valores iniciales x0 y y0.

4. Para cada subintervalo i = 0, 1, 2, ..., n-1, realizar los siguientes pasos:

a. Calcular la pendiente en el punto (xi, yi) utilizando la función f(x, y): mi = f(xi, yi).

b. Aproximar el valor de y en el siguiente punto xi+1 = xi + h mediante: yi+1 = yi + h * mi.
5. Repetir el paso 4 hasta alcanzar el valor final xn.

El método de Euler es un método de paso simple, lo que significa que solo utiliza la información del punto actual para calcular el siguiente punto en la aproximación de la solución. La precisión de este método depende del tamaño del paso h: cuanto más pequeño sea h, más precisa será la aproximación, pero también requerirá más cálculos.
    
Es importante tener en cuenta que el método de Euler es un método de aproximación y puede introducir errores acumulativos a medida que se avanza en la solución. Por lo tanto, en general, se recomienda utilizar métodos más precisos, como los métodos de Runge-Kutta, cuando se requiere una mayor precisión en la solución.

## Pseudocodigo.
    ENTRADA: f(x, y) (función que define la ecuación diferencial), x0 (valor inicial de x), y0 (valor inicial de y), xn (valor final de x), n (número de subintervalos)
    
    h = (xn - x0) / n (tamaño del paso)
    x = x0
    y = y0
    
    PARA i = 0 HASTA n-1
        pendiente = f(x, y)
        y = y + h * pendiente
        x = x + h
    FIN PARA
    
    SALIDA: y (aproximación de la solución en xn)

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

## Implementación de los codigos en Python.

### Ejercicio 1.py
#### Codigo.

#### Comprobacion.



### Ejercicio 2.py
#### Codigo.



#### Comprobacion.



### Ejercicio 3.py
#### Codigo.


    
#### Comprobacion.



### Ejercicio 4.py
#### Codigo.
   


#### Comprobacion.



### Ejercicio 5.py
#### Codigo.
   


#### Comprobacion.
