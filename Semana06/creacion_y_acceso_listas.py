"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                    Creación y Acceso Básico a Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te introducirá a la creación de listas y cómo acceder a
sus elementos.

1.  Crea una lista llamada `frutas_favoritas` que contenga al menos 5 nombres
    de tus frutas favoritas como cadenas de texto.
2.  Imprime la lista completa `frutas_favoritas` en la consola.
3.  Imprime la primera fruta de la lista (pista: el primer elemento tiene índice 0).
4.  Imprime la tercera fruta de la lista.
5.  Imprime la última fruta de la lista (pista: puedes usar un índice negativo).
6.  Utiliza la función `len()` para obtener e imprimir la cantidad de frutas
    en tu lista.
-------------------------------------------------------------------------------
"""

# 1. Crear una lista de frutas favoritas
frutas_favoritas = ["Manzana", "Plátano", "Frutilla", "Mango", "Cereza"]

# 2. Imprimir la lista completa
print("Mis frutas favoritas son:", frutas_favoritas)
print("-----------------------------------------")

# 3. Imprimir la primera fruta
# Los índices de las listas comienzan en 0
primera_fruta = frutas_favoritas[0]
print(f"La primera fruta de la lista es: {primera_fruta}")

# 4. Imprimir la tercera fruta
# El tercer elemento tiene índice 2
tercera_fruta = frutas_favoritas[2]
print(f"La tercera fruta de la lista es: {tercera_fruta}")

# 5. Imprimir la última fruta
# El índice -1 se refiere al último elemento, -2 al penúltimo, y así sucesivamente.
ultima_fruta = frutas_favoritas[-1]
print(f"La última fruta de la lista es: {ultima_fruta}")
print("-----------------------------------------")

# 6. Imprimir la cantidad de frutas en la lista
cantidad_frutas = len(frutas_favoritas)
print(f"Tengo {cantidad_frutas} frutas favoritas en mi lista.")

# Intento de acceso a un índice que no existe (esto generaría un error)
# print(frutas_favoritas[10]) # Descomenta esta línea para ver el error IndexError

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el índice del primer elemento en una lista de Python? ¿Y del quinto?
2.  Si una lista tiene `N` elementos, ¿cuál es el índice del último elemento
    usando numeración positiva? ¿Y usando numeración negativa?
3.  ¿Qué sucede si intentas acceder a un elemento de la lista usando un índice
    que está fuera del rango válido (por ejemplo, en una lista de 5 elementos,
    intentas acceder al índice 5 o al índice -6)?
4.  Crea una lista con diferentes tipos de datos (números, cadenas, booleanos).
    ¿Es esto posible en Python? Imprímela para verificar.
-------------------------------------------------------------------------------
"""