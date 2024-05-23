# Metodo de Gauss
  ## ¿Que es?
  El método de Gauss consiste en transformar un sistema de ecuaciones lineales en uno equivalente pero más simple, utilizando 
  operaciones elementales sobre las filas de una matriz aumentada (una matriz que incluye tanto los coeficientes de las variables 
  como los términos constantes de las ecuaciones). Las operaciones elementales sobre las filas incluyen intercambiar filas, 
  multiplicar una fila por una constante distinta de cero y sumar o restar un múltiplo de una fila a otra fila.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por filas, lo que 
  facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.

## Pasos
  ### 1. Formación de la matriz aumentada: 
  - Conviertes este sistema en una matriz. Las columnas representarán los coeficientes de las incógnitas y la última 
    columna los términos constantes. 
  ### 2. Operaciones para obtener la forma escalonada: 
  - Aplicas operaciones simples a las filas para hacer ceros debajo de los elementos principales (el primer número no nulo de 
    cada fila). El objetivo es llevar la matriz a una forma 
    escalonada. Por ejemplo, podrías restar el doble de la primera fila de la segunda fila para hacer cero el primer elemento 
    de la segunda fila. Repites este proceso para cada fila.
  ### 3. Resolución del sistema de ecuaciones: 
  - Una vez que has obtenido la forma escalonada, puedes resolver el sistema de ecuaciones resultante. Empiezas desde la última 
    ecuación y despejas la última incógnita. Luego, sustituyes este valor en la penúltima ecuación y despejas la siguiente incógnita. 
    Repites este proceso hasta haber encontrado todos los valores de las incógnitas.
  ### 4. Comprobación: 
  - Finalmente, sustituyes los valores obtenidos en las ecuaciones originales para asegurarte de que sean soluciones válidas del 
    sistema de ecuaciones.

## Implementacion y ejercicios
[Ejercicios del metodo de Gauss](https://docs.google.com/spreadsheets/d/1VNyxf74rtmIrbNZXjKSa90xqo4Xoaky72CX9Hhu8SLU/edit?usp=sharing)