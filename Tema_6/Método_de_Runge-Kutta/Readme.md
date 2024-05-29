# Metodo de Runge-Kutta

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
