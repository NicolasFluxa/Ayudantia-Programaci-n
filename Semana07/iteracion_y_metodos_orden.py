"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                 Iteración en Listas y Métodos de Orden
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio se enfoca en cómo recorrer listas y ordenarlas.

1.  Crea una lista de números desordenados, por ejemplo:
    `numeros = [5, 2, 9, 1, 5, 6, 3, 8]`
2.  Utiliza un bucle `for` para iterar sobre la lista `numeros` e imprimir
    cada número en una nueva línea, precedido por "Número: ".
3.  Utiliza el método `sort()` para ordenar la lista `numeros` de forma
    ascendente. Imprime la lista ordenada.
4.  Ahora, utiliza el método `reverse()` para invertir el orden de la lista
    (que ahora está ordenada). Imprime la lista invertida (quedará ordenada
    de forma descendente).
5.  Calcula la suma de todos los elementos de la lista `numeros` utilizando un
    bucle `for` y una variable acumuladora. Imprime la suma total.
    (No uses la función `sum()` incorporada para este paso, hazlo manualmente).
-------------------------------------------------------------------------------
"""

# 1. Crear una lista de números desordenados
numeros = [5, 2, 9, 1, 5, 6, 3, 8]
print("Lista original:", numeros)
print("-----------------------------------------")

# 2. Iterar e imprimir cada número
print("Iterando sobre la lista original:")
for numero in numeros:
    print(f"Número: {numero}")
print("-----------------------------------------")

# 3. Ordenar la lista con sort()
# El método sort() modifica la lista original y no devuelve nada (None).
numeros.sort()
print("Lista después de sort():", numeros)
print("-----------------------------------------")

# 4. Invertir el orden de la lista con reverse()
# El método reverse() también modifica la lista original.
numeros.reverse()
print("Lista después de reverse() (orden descendente):", numeros)
print("-----------------------------------------")

# 5. Calcular la suma de los elementos manualmente
suma_total = 0 # Variable acumuladora
for numero in numeros: # Iteramos sobre la lista (que ahora está [9, 8, 6, 5, 5, 3, 2, 1])
    suma_total = suma_total + numero # suma_total += numero

print(f"La suma de los elementos de la lista es: {suma_total}")
print("-----------------------------------------")

# Ejemplo con una lista de strings
# palabras = ["manzana", "banana", "cereza", "durazno"]
# palabras.sort()
# print("Palabras ordenadas:", palabras) # Orden alfabético
# palabras.reverse()
# print("Palabras en orden inverso:", palabras)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  El método `sort()` modifica la lista original (ordenamiento "in-place").
    ¿Qué significa esto? ¿Devuelve `sort()` algún valor?
2.  Si quisieras ordenar una lista de strings que contienen nombres, ¿cómo
    los ordenaría `sort()` por defecto?
3.  ¿Cuál es la diferencia entre `lista.reverse()` y `reversed(lista)`?
    (Pista: `reversed()` es una función incorporada que devuelve un iterador).
4.  Si tuvieras una lista de números y quisieras crear una NUEVA lista ordenada
    sin modificar la original, ¿qué función podrías usar en lugar del método `sort()`?
    (Pista: busca la función `sorted()`).
-------------------------------------------------------------------------------
"""