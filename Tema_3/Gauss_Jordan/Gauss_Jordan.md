# Gauss Jordan

## ¿Que es el metodo de Gauss Jordan?
  Es un algoritmo utilizado en álgebra lineal para encontrar las soluciones de un sistema de ecuaciones lineales o para encontrar la inversa de una matriz. 
  El método consiste en aplicar operaciones elementales de fila a una matriz ampliada que contiene tanto la matriz de coeficientes como el vector de términos 
  constantes en un sistema de ecuaciones lineales. Estas operaciones elementales de fila incluyen intercambio de filas, multiplicación de una fila por un escalar 
  no nulo y sumar un múltiplo de una fila a otra fila. El objetivo es llevar la matriz ampliada a una forma escalonada reducida (forma escalonada reducida por 
  filas) o a una forma diagonal si se busca la inversa de la matriz. Una vez que la matriz está en una de estas formas, se pueden identificar las soluciones del 
  sistema de ecuaciones o la inversa de la matriz directamente. El método de Gauss-Jordan es una extensión del método de eliminación de Gauss, y es especialmente 
  útil cuando se busca la inversa de una matriz o cuando se necesita resolver sistemas de ecuaciones lineales con múltiples soluciones.

## Algoritmo
 ### 1. Formar la matriz aumentada: 
 - Toma el sistema de ecuaciones lineales y escribe las coeficientes de las variables en una matriz, junto con 
  los términos constantes. Esta matriz es conocida como la matriz aumentada.

 ### 2. Convertir el primer elemento de la matriz en uno: 
 - Divide toda la primera fila de la matriz aumentada por el valor del primer elemento (el coeficiente de la 
  primera variable en la primera ecuación).

 ### 3. Hacer ceros debajo del primer elemento de la diagonal principal: 3
 - Para cada fila por debajo de la primera fila, resta múltiplos adecuados de la primera fila para hacer cero 
  el elemento que se encuentra directamente debajo 
  del primer elemento de la diagonal principal.

 ### 4. Repetir el proceso para los elementos restantes: 
 - Repite los pasos 2 y 3 para cada elemento de la diagonal principal, convirtiendo cada uno en uno y haciendo 
  ceros debajo de él.

 ### 5. Obtener la forma escalonada reducida: 
 - Continúa los pasos hasta que la matriz se convierta en una forma escalonada reducida, donde todos los elementos 
  por encima y por debajo de la diagonal principal sean cero, y cada elemento de la diagonal principal sea uno.

 ### 6. Interpretar los resultados: 
 - Una vez que tengas la forma escalonada reducida, las soluciones al sistema de ecuaciones están directamente leíbles 
  de la matriz. Si hay filas de ceros en la parte inferior de la matriz, significa que hay infinitas soluciones o que 
  el sistema es inconsistente.

 ### 7. Si es necesario, realiza operaciones adicionales: 
 - Si estás buscando la inversa de una matriz, puedes continuar el algoritmo hasta obtener una matriz identidad en el 
  lado izquierdo de la matriz aumentada.

## Implementación de los metodos en excel

### Ejercicio 1
#### Metodologia
[![imagen-2024-05-23-082336032.png](https://i.postimg.cc/VktpMfdC/imagen-2024-05-23-082336032.png)](https://postimg.cc/w16wYd5q)
#### Comprobacion
[![imagen-2024-05-23-082428875.png](https://i.postimg.cc/9ftk8LPX/imagen-2024-05-23-082428875.png)](https://postimg.cc/yJxnWXr2)


### Ejercicio 2
#### Metodologia
[![imagen-2024-05-23-082511077.png](https://i.postimg.cc/KvkHSG7H/imagen-2024-05-23-082511077.png)](https://postimg.cc/QHDbcryQ)
[![imagen-2024-05-23-082600244.png](https://i.postimg.cc/8cFtS4v6/imagen-2024-05-23-082600244.png)](https://postimg.cc/D4TqQqBv)
#### Comprobacion
![image](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/158504061/23589834-e01e-455d-93fb-742cd106d7f3)


### Ejercicio 3
#### Metodologia    
[![imagen-2024-05-23-082823677.png](https://i.postimg.cc/cHzBX3z4/imagen-2024-05-23-082823677.png)](https://postimg.cc/R6ct0W9j)
#### Comprobacion
![image](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/158504061/27620fa0-2684-4061-9743-92daf8562ff9)



### Ejercicio 4
#### Metodologia
[![imagen-2024-05-23-082920988.png](https://i.postimg.cc/RCjj0J0B/imagen-2024-05-23-082920988.png)](https://postimg.cc/CdsvP1DP)
#### Comprobacion
[![imagen-2024-05-23-082952948.png](https://i.postimg.cc/dVFp2MdN/imagen-2024-05-23-082952948.png)](https://postimg.cc/hfC2n52V)



### Ejercicio 5
#### Metodologia
[![imagen-2024-05-23-083243644.png](https://i.postimg.cc/dV0mP4Kt/imagen-2024-05-23-083243644.png)](https://postimg.cc/XpTy9KJT)
#### Comprobacion
[![imagen-2024-05-23-083312243.png](https://i.postimg.cc/rpBS4TRK/imagen-2024-05-23-083312243.png)](https://postimg.cc/f3vt46KN)

## Ejercicios en excel
[Ejercicios del metodo de Gauss Jordan](https://docs.google.com/spreadsheets/d/13LaG-yuZGNyTcdEdCONMtDpY-dnTvp2FBTZWmA-gCLY/edit?usp=sharing)


  
