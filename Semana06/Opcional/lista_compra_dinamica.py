"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                     Lista de Compras Dinámica
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un programa que permita al usuario construir una lista de compras
de forma interactiva.

1.  Inicializa una lista vacía llamada `lista_de_compras`.
2.  Usa un bucle `while` para preguntar repetidamente al usuario qué ítem
    desea agregar a la lista.
3.  Cada ítem ingresado por el usuario debe ser añadido a `lista_de_compras`
    utilizando el método `append()`.
4.  El bucle debe continuar hasta que el usuario ingrese la palabra "fin"
    (o "listo", "salir", la que prefieras). Esta palabra no debe agregarse
    a la lista.
5.  Una vez que el usuario termine de agregar ítems, el programa debe mostrar:
    a. Un mensaje indicando "Tu lista de compras es:".
    b. Todos los ítems de la lista, uno por línea. Puedes usar un bucle `for`
       para esto.
    c. (Opcional) El número total de ítems en la lista.
-------------------------------------------------------------------------------
"""

# 1. Inicializar lista vacía
lista_de_compras = []
item_ingresado = ""

print("--- Creador de Lista de Compras ---")
print("Escribe los ítems que deseas agregar. Escribe 'fin' para terminar.")

# 2. Bucle while para agregar ítems
while item_ingresado.lower() != "fin": # .lower() para que "Fin", "FIN", "fin" funcionen
    item_ingresado = input("Agregar ítem (o 'fin' para terminar): ")

    # 3. Agregar ítem si no es la palabra para terminar
    if item_ingresado.lower() != "fin":
        lista_de_compras.append(item_ingresado)
        print(f"'{item_ingresado}' agregado a la lista.")
    else:
        print("Finalizando la adición de ítems...")

print("------------------------------------")

# 5. Mostrar la lista de compras
if len(lista_de_compras) > 0:
    # 5a. Mensaje
    print("\n🛍️ Tu lista de compras es:")
    # 5b. Ítems de la lista
    for i, item in enumerate(lista_de_compras): # enumerate da índice y valor
        print(f"{i + 1}. {item}") # i+1 para numeración natural

    # 5c. (Opcional) Número total de ítems
    print("------------------------------------")
    print(f"Total de ítems en la lista: {len(lista_de_compras)}")
else:
    print("Tu lista de compras está vacía. ¡No olvides comprar algo!")

print("------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Por qué se inicializa `lista_de_compras = []` antes del bucle?
    ¿Qué pasaría si intentaras usar `append()` en una variable que no ha sido
    inicializada como lista?
2.  En la condición `while item_ingresado.lower() != "fin":`, ¿qué función cumple
    el método `.lower()`? ¿Por qué es útil aquí?
3.  La función `enumerate()` se usó en el bucle `for` para mostrar la lista
    numerada. Investiga brevemente qué hace `enumerate()` y qué valores
    proporciona en cada iteración.
4.  ¿Cómo modificarías el programa para permitir al usuario eliminar un ítem
    de la lista después de haberla creado, antes de imprimirla finalmente?
    (Pista: podrías preguntar si desea eliminar algo y usar `remove()`).
-------------------------------------------------------------------------------
"""