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
