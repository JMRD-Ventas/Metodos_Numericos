import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Eliminación hacia adelante
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

# Definición del sistema
A = np.array([[3, 2], [1, 2]], dtype=float)
b = np.array([1, 1], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)
