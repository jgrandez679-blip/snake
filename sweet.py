import numpy as np

A = np.array([
    [1,1,1],
    [1,3,-1],
    [0,-2,1],
])

b = np.array([120,200,-20])

solucion = np.linalg.solve(A, b)

print(solucion)
