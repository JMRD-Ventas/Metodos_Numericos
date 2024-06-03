import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 3x3:
# 2x + 3y + 6z = 7
# y + z = 2
# x + 5y + 2 = 4

A = np.array([
    [2, 3, 6, 7],
    [0, 1, 1, 2],
    [1, 5, 2, 4]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
