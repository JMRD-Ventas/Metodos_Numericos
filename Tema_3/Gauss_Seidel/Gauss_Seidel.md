# Gauss Seidel

## ¿Que es?
  El método de Gauss-Seidel es un algoritmo utilizado para resolver sistemas de ecuaciones lineales de forma iterativa. 
  Este método es una extensión del método de Jacobi y se utiliza comúnmente en álgebra lineal y en problemas de ingeniería, 
  física y matemáticas aplicadas.
  
  La idea básica detrás del método de Gauss-Seidel es resolver el sistema de ecuaciones lineales de manera iterativa, donde 
  en cada iteración se actualizan las soluciones de las ecuaciones utilizando los valores más recientes calculados en las 
  iteraciones anteriores. A diferencia del método de Jacobi, en el que se utilizan los valores de la iteración anterior para 
  actualizar todos los valores simultáneamente, en Gauss-Seidel, los valores actualizados se utilizan inmediatamente después 
  de ser calculados. Esto puede llevar a una convergencia más rápida en algunos casos.

## Pasos
  ### 1. Inicialización: 
  - Empieza con una suposición inicial de las soluciones para todas las incógnitas del sistema de ecuaciones.
  
  ### 2. Iteración:
  - Para cada ecuación en el sistema, calcula el valor de la incógnita utilizando los valores actuales de las otras incógnitas 
    (puedes empezar con la primera ecuación y luego seguir con las siguientes, o puedes cambiar el orden dependiendo de tu 
    preferencia).
  
  - Utiliza los nuevos valores calculados para actualizar las soluciones de las incógnitas.
  
  - Repite este proceso para cada ecuación en el sistema.
  
  ### 3. Criterio de parada:
  - Define un criterio de parada, como la diferencia entre los valores de las incógnitas en dos iteraciones sucesivas. Si esta
    diferencia es lo suficientemente pequeña (por debajo de un cierto umbral), detén el proceso iterativo. También puedes
    establecer un número máximo de iteraciones como criterio de parada.
  
  ### 4. Convergencia:
  - Comprueba si las soluciones convergen a una solución estable. Si no es así, es posible que necesites ajustar el sistema, cambiar
    la suposición inicial o utilizar otro método de 
    resolución.
    
  ### 5. Resultados:
  - Una vez que el criterio de parada se cumple, los valores de las incógnitas calculados en la última iteración se consideran las 
    soluciones aproximadas del sistema de ecuaciones.
  
  Este algoritmo se repite hasta que se alcanza el criterio de parada, lo que indica que las soluciones convergen a una solución estable 
  o que se ha alcanzado el número máximo de iteraciones permitidas. Es importante tener en cuenta que la convergencia del método de 
  Gauss-Seidel puede depender de varios factores, como la elección de la suposición inicial y las propiedades de la matriz de coeficientes 
  del sistema de ecuaciones lineales.

## Implementación de los metodos en excel
### Ejercicio 1
#### Metodologia en python

```python

```

#### Comprobacion
[![imagen-2024-05-23-084108570.png](https://i.postimg.cc/y8z4L3qP/imagen-2024-05-23-084108570.png)](https://postimg.cc/MvtFTTpM)

### Ejercicio 2
#### Metodologia en python

```python

```

#### Comprobacion
[![imagen-2024-05-23-084348478.png](https://i.postimg.cc/50FWPBts/imagen-2024-05-23-084348478.png)](https://postimg.cc/0Mx4jJDS)

### Ejercicio 3
#### Metodologia en python

```python

```

#### Comprobacion
[![imagen-2024-05-23-084553240.png](https://i.postimg.cc/NMRP9pFv/imagen-2024-05-23-084553240.png)](https://postimg.cc/LY6VGkjx)

### Ejercicio 4
#### Metodologia en python

```python

```

#### Comprobacion
[![imagen-2024-05-23-084833866.png](https://i.postimg.cc/BQzc32ZT/imagen-2024-05-23-084833866.png)](https://postimg.cc/6ydGL2vq)

### Ejercicio 5
#### Metodologia en python

```python

```

#### Comprobacion
[![imagen-2024-05-23-085202453.png](https://i.postimg.cc/KYf1Gy76/imagen-2024-05-23-085202453.png)](https://postimg.cc/B88SpkVp)

## Implementacion y ejercicios
[Ejercicios del metodo de Gauss - Seidel](https://docs.google.com/spreadsheets/d/126d6fVLOEG1j31MZZNvPLMYPxiLwVk9_Ih7ST6xk3Z8/edit?usp=sharing)
