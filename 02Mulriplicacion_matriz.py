"""multiplica estas dos matrices
A = [[1,2,3],[4,5,6]]
B = [[-1,0],[0,1],[1,1]]
"""
import numpy as np

# Define las matrices
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, 0], [0, 1], [1, 1]])

# Multiplica las matrices
C = np.dot(A, B)

print(C)


