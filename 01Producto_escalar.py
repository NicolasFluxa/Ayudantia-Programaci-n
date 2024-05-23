"""Escribir un programa que almacene los vectores
(1,2,3) y (-1,0,2) en dos listas y muestre por
pantalla su producto escalar."""

vectorX = [1, 2, 3]
vectorY = [-1, 0, 2]
lista = []
for i in range(3):
    lista.append(vectorX[i]*vectorY[i])

print(lista)