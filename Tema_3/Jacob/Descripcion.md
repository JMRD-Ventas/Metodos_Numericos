# Metodo de Jacob
  ## ¿Que es?
  El método de Jacob (también conocido como el método de iteración de Jacobianos o el método de Jacobi) es 
  un algoritmo utilizado para resolver sistemas de ecuaciones lineales. Es un método iterativo que se utiliza 
  para aproximar la solución de sistemas de ecuaciones lineales, especialmente cuando estos sistemas son grandes 
  y sparse (es decir, tienen muchos ceros).
    
  El método de Jacob se basa en descomponer la matriz del sistema en una suma de una matriz diagonal y el resto 
  de la matriz. Luego, iterativamente, se resuelve un sistema de ecuaciones en el que la matriz del sistema es la 
  matriz diagonal y se actualizan las soluciones en cada iteración.
    
  El proceso se repite hasta que se alcanza una precisión deseada o se cumple algún otro criterio de convergencia. 
  Aunque el método de Jacob puede ser relativamente simple y fácil de implementar, puede converger lentamente para 
  ciertos tipos de sistemas de ecuaciones. Sin embargo, es útil como paso en métodos más avanzados como el método de 
  Gauss-Seidel o el método de relajación.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por 
  filas, lo que facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.

## Pasos
  ### 1. Preparación inicial: 
  - Antes de comenzar, necesitas tener tu sistema de ecuaciones lineales en forma matricial. Es decir, necesitas tener 
    todas las variables y constantes organizadas en una matriz.

  ### 2. Descomposición de la matriz: 
  - Divide la matriz de coeficientes en dos partes: una matriz diagonal y el resto de la matriz. La matriz diagonal son 
    los elementos de la diagonal principal de la matriz original, y el resto son los elementos que no están en la diagonal 
    principal.

  ### 3. Iniciar con una suposición inicial: 
  - Comienza con una suposición inicial para las soluciones de tus variables. Esto podría ser cualquier valor, pero es 
    común empezar con todos los valores en cero.

  ### 4. Iteración: 
  - Ahora, para cada variable en tu sistema, usa la fila correspondiente en la matriz de coeficientes y las soluciones 
    actuales de las otras variables (usando la suposición inicial para la primera iteración) para calcular una nueva 
    estimación para esa variable. Repite este proceso para cada variable.

  ### 5. Actualización de las soluciones: 
  - Después de calcular una nueva estimación para cada variable, actualiza tus soluciones actuales con estas nuevas estimaciones.

  ### 6. Comprobación de convergencia: 
  - Repite los pasos 4 y 5 hasta que tus soluciones converjan a una precisión aceptable. Esto significa que las soluciones no 
    cambian mucho entre iteraciones.

  ### 7. Verificación de la solución: 
  - Una vez que has alcanzado la convergencia, verifica tus soluciones sustituyéndolas en las ecuaciones originales para asegurarte 
  de que satisfacen todas las ecuaciones.

  ### 8. Finalización: 
  - Si tus soluciones son aceptables, entonces has resuelto tu sistema de ecuaciones utilizando el método de Jacob.

Recuerda que la velocidad de convergencia puede variar dependiendo de la naturaleza del sistema de ecuaciones, y puede que necesites ajustar la precisión o la suposición inicial para obtener resultados satisfactorios.

## Implementación de los metodos en excel
  ### Ejercicio 1
  #### Metodologia
  [![imagen-2024-05-23-091341645.png](https://i.postimg.cc/HxP4LM41/imagen-2024-05-23-091341645.png)](https://postimg.cc/ftm02Jr8)
  #### Comprobacion
  [![imagen-2024-05-23-091354523.png](https://i.postimg.cc/Rh61J0X6/imagen-2024-05-23-091354523.png)](https://postimg.cc/jnTnGRVt)
  
  ### Ejercicio 2
  #### Metodologia
  [![imagen-2024-05-23-091443345.png](https://i.postimg.cc/sfq4dpgp/imagen-2024-05-23-091443345.png)](https://postimg.cc/PNbw1vZx)
  #### Comprobacion
  [![imagen-2024-05-23-091520263.png](https://i.postimg.cc/j5CPB5Vg/imagen-2024-05-23-091520263.png)](https://postimg.cc/Fd5YLhH3)
  
  ### Ejercicio 3
  #### Metodologia 
  [![imagen-2024-05-23-091619428.png](https://i.postimg.cc/XNmgk5ZD/imagen-2024-05-23-091619428.png)](https://postimg.cc/c67YsrBQ)
  #### Comprobacion
  [![imagen-2024-05-23-091634258.png](https://i.postimg.cc/X75kHvdN/imagen-2024-05-23-091634258.png)](https://postimg.cc/MvWBXq9g)
  
  ### Ejercicio 4
  #### Metodologia
  [![imagen-2024-05-23-091956377.png](https://i.postimg.cc/v8f4CxqK/imagen-2024-05-23-091956377.png)](https://postimg.cc/pyVVFrtQ)
  #### Comprobacion
  [![imagen-2024-05-23-092009875.png](https://i.postimg.cc/9F2D2XsQ/imagen-2024-05-23-092009875.png)](https://postimg.cc/7bBHM4xF)
  
  ### Ejercicio 5
  #### Metodologia
  [![imagen-2024-05-23-092057131.png](https://i.postimg.cc/Dwj01r0S/imagen-2024-05-23-092057131.png)](https://postimg.cc/cv3dS8QW)
  #### Comprobacion
  [![imagen-2024-05-23-092109696.png](https://i.postimg.cc/vm4Bh4x3/imagen-2024-05-23-092109696.png)](https://postimg.cc/mcGB22wH)

## Implementacion y ejercicios
[Ejercicios del metodo de Jacob](https://docs.google.com/spreadsheets/d/1pCUyxeDHE9aHkJPAhAWR9iPFlqWY9MG939s1Q2w7AOs/edit?usp=sharing)
