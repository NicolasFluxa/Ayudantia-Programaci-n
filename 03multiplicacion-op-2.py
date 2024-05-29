# Define las matrices
A = [[1,2,3],[4,5,6]] # Matriz A
B = [[-1,0],[0,1],[1,1]] # Matriz B

# Crea una matriz vacía para almacenar el resultado
C = [[0, 0], [0, 0]] # Matriz C que almacenará el resultado de la multiplicación de las matrices A y B

# Realiza la multiplicación de matrices
for i in range(len(A)): # Recorre cada fila de la matriz A
   for j in range(len(B[0])): # Recorre cada columna de la matriz B
       for k in range(len(B)): # Recorre cada fila de la matriz B
           C[i][j] += A[i][k] * B[k][j] # Multiplica el elemento correspondiente de la matriz A con el
           # elemento correspondiente de la matriz B y lo suma al elemento correspondiente de la matriz C

# Imprime el resultado
for r in C: # Recorre cada fila de la matriz C
   print(r) # Imprime la fila
