# Metodo de Runge-Kutta

## ¿Qué es?
El método de Runge-Kutta es un método numérico ampliamente utilizado para resolver ecuaciones diferenciales ordinarias (EDO) de manera más precisa que el método de Euler. Existen varios métodos de Runge-Kutta, siendo el más popular el método de Runge-Kutta de cuarto orden (RK4). A continuación, describiré los pasos del método RK4:

El método RK4 utiliza una combinación ponderada de cuatro pendientes (k1, k2, k3, k4) para calcular la aproximación del siguiente valor de y. Las pendientes se evalúan en diferentes puntos dentro del subintervalo [xi, xi+1], lo que permite capturar mejor el comportamiento de la solución y, por lo tanto, proporcionar una aproximación más precisa.

La principal ventaja del método de Runge-Kutta de cuarto orden es que tiene un error de truncamiento del orden de h^5, lo que significa que el error disminuye rápidamente a medida que el tamaño del paso h se reduce. Esto lo convierte en un método más preciso que el método de Euler, que tiene un error de truncamiento del orden de h^2.

Sin embargo, el método RK4 requiere más cálculos que el método de Euler, ya que implica evaluar la función f(x, y) cuatro veces en cada subintervalo. Esto puede resultar en un mayor costo computacional, pero a cambio se obtiene una mayor precisión en la solución.

Es importante mencionar que existen otros métodos de Runge-Kutta de órdenes superiores, como el RK5 (quinto orden) o el RK8 (octavo orden), que pueden proporcionar aún más precisión, pero también requieren más cálculos.

## Pasos para su solución
1. Definir la ecuación diferencial y las condiciones iniciales: Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.

2. Dividir el intervalo de interés [x0, xn] en n subintervalos iguales de tamaño h = (xn - x0) / n.

3. Inicializar los valores iniciales x0 y y0.

4. Para cada subintervalo i = 0, 1, 2, ..., n-1, realizar los siguientes pasos:
   - Calcular k1 = h * f(xi, yi)
   - Calcular k2 = h * f(xi + h/2, yi + k1/2)
   - Calcular k3 = h * f(xi + h/2, yi + k2/2)
   - Calcular k4 = h * f(xi + h, yi + k3)
   - Actualizar yi+1 = yi + (k1 + 2*k2 + 2*k3 + k4)/6
   - Actualizar xi+1 = xi + h

5. Repetir el paso 4 hasta alcanzar el valor final xn.

## Implementación de los codigos en Python

### Ejercicio 1.py
#### Codigo.
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
