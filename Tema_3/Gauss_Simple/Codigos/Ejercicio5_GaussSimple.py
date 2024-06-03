import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[1, -1, 2, -1, 3, 1], [2, 3, -1, 2, -1, 2], [3, 2, 3, -3, 2, 1], [4, -2, 1, 1, 1, -3], [1, 1, 1, 1, 1, 1], [2, -1, 1, 2, -1, 3]], dtype=float)
b = np.array([4, 1, 3, 6, 10, 5], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

