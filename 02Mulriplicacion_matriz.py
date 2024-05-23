"""multiplica estas dos matrices
A = [[1,2,3],[4,5,6]]
B = [[-1,0],[0,1],[1,1]]
"""
matriz = []
A = [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1], [1, 1]]

for fila in range(2):
    matriz.append([])
    for columna in range(2):
        matriz[fila].append(columna)

print(matriz)

