# Metodo de cuadratico.

## ¿Qué es?
La interpolación consiste en hallar un dato dentro de un intervalo en el que conocemos los valores en los extremos.
El problema general de la interpolación se nos presenta cuando nos dan una función de la cual solo conocemos una serie de puntos de la misma:
(xo, yo), (x1, y1),........., (xn, yn)

# Metodo de Lagrange.

## ¿Qué es?
El método de interpolación de Lagrange es una técnica matemática utilizada para encontrar un polinomio que pase a través de un conjunto dado de puntos de datos. Este polinomio se denomina polinomio interpolador de Lagrange.

La idea básica del método de Lagrange es construir un polinomio de grado n-1 (donde n es el número de puntos de datos) que coincida con los valores de la función en esos puntos de datos. Matemáticamente, el polinomio interpolador de Lagrange se define como:
    
    P(x) = y₁L₁(x) + y₂L₂(x) + ... + yₙLₙ(x)
    
Donde: 

y₁, y₂, ..., yₙ son los valores de la función en los puntos de datos (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ).
L₁(x), L₂(x), ..., Lₙ(x) son los polinomios de Lagrange de grado n-1, definidos como:
    
    Lᵢ(x) = ∏(k≠i) (x - xₖ) / (xᵢ - xₖ)
    
Estos polinomios de Lagrange tienen la propiedad de que Lᵢ(xⱼ) = 1 si i = j, y Lᵢ(xⱼ) = 0 si i ≠ j.
    
Una vez construido el polinomio interpolador de Lagrange P(x), puede utilizarse para aproximar el valor de la función en cualquier punto x dentro del intervalo definido por los puntos de datos.
    
El método de interpolación de Lagrange es ampliamente utilizado en diversas áreas, como análisis numérico, cálculo computacional, procesamiento de señales, etc. Sin embargo, tiene algunas limitaciones, como el hecho de que puede presentar oscilaciones indeseables (fenómeno de Runge) cuando se interpola en un intervalo grande con puntos de datos no uniformemente distribuidos.
    
Es importante tener en cuenta que la interpolación de Lagrange solo proporciona una aproximación de la función real, y la precisión de la aproximación depende de la distribución y el número de puntos de datos disponibles.

    ------------

# Metodo de Newton.

## ¿Qué es?

El método de interpolación de Newton es una técnica matemática utilizada para encontrar un polinomio que pase a través de un conjunto dado de puntos de datos. Este polinomio se denomina polinomio interpolador de Newton.
La idea básica del método de Newton es construir un polinomio de grado n-1 (donde n es el número de puntos de datos) que coincida con los valores de la función en esos puntos de datos. El polinomio interpolador de Newton se expresa como una suma de términos, donde cada término contiene un coeficiente y una potencia de (x - x₀), siendo x₀ el primer punto de datos.

    P(x) = a₀ + a₁(x - x₀) + a₂(x - x₀)(x - x₁) + ... + aₙ(x - x₀)(x - x₁)...(x - xₙ₋₁)    
Donde:
    P(x) es el polinomio interpolador de Newton.
    x₀, , , ...,  son los valores de la variable independiente (puntos de datos).x₁x₂xₙ
    a₀, , , ...,  son los coeficientes del polinomio interpolador.a₁a₂aₙ
    n es el número de puntos de datos (grado del polinomio es ).n-1

Los coeficientes , , , ...,  se calculan utilizando las diferencias divididas de Newton de la siguiente manera:a₀a₁a₂aₙ
  a₀ = f(x₀)
a₁ = f[x₀, x₁]
a₂ = f[x₀, x₁, x₂]
...
aₙ = f[x₀, x₁, x₂, ..., xₙ]
Donde  representa la diferencia dividida de orden  de la función  en los puntos , , ..., . Las diferencias divididas se calculan recursivamente mediante la fórmula:f[x₀, x₁, ..., xₖ]kfx₀x₁xₖ
    f[x₀, x₁, ..., xₖ] = (f[x₁, x₂, ..., xₖ] - f[x₀, x₁, ..., xₖ₋₁]) / (xₖ - x₀)

------------

# Metodo de la interpolación lineal

## ¿Qué es?

La interpolación lineal es un caso en donde se usa un polinomio de primer grado, es decir una función lineal o afín, para adivinar el valor de la función en un punto.



