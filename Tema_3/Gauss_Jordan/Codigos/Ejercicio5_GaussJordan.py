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
# Matriz aumentada para el sistema de ecuaciones 4x4:
# 2x + 1y + 3z + w = 3
# x + 2y + 5z + w = -2
# 2x + 5y - z + w = 1
# 4x + 3y - 2z + w = 0

A = np.array([
    [2, 1, 3, 1, -3],
    [1, 2, 5, 1, -2],
    [1, 4, -3, 1, 5],
    [4, 3, -2, 1, 0]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
