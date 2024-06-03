# Regla de Simpson.

## ¿Que es?

La regla de Simpson es un método de integración numérica que se utiliza para la aproximación numérica de integrales definidas1. El intervalo de integración [a, b] se subdivide en n subintervalos con n siendo un entero par. El ancho de cada subdivisión será: h = (b – a)/n2. La regla de Simpson se utiliza para aproximar el valor de una integral definida, y se basa en la idea de aproximar la curva de la función integrando polinomios de segundo grado2.

## Algoritmo.

1.- Dado un intervalo ([a, b]) y una función (f(x)), la regla de 1/3 de Simpson aproxima el área bajo la curva utilizando un polinomio de segundo orden (interpolante cuadrático).

2.- La fórmula es: [ \int_a^b f(x) , dx \approx \frac{h}{3} \left[ f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right] ] donde (h = \frac{b-a}{2}).

3.- Si la función es altamente oscilatoria o carece de derivados en ciertos puntos, se puede usar la regla compuesta de Simpson dividiendo el intervalo en subintervalos pequeños y aplicando la regla de Simpson a cada uno.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

### Ejercicio 2
#### Metodologia en codigo

### Ejercicio 3
#### Metodologia en codigo

### Ejercicio 4
#### Metodologia en codigo

### Ejercicio 5
#### Metodologia en codigo
