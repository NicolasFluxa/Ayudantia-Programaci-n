"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                     Búsqueda y Conteo en Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio se centra en encontrar elementos y contar sus ocurrencias
dentro de una lista.

1.  Crea una lista de nombres donde algunos nombres se repitan. Por ejemplo:
    `invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]`
2.  Imprime la lista de invitados.
3.  Pregunta al usuario qué nombre desea buscar en la lista de invitados.
4.  Utiliza el método `count()` para determinar cuántas veces aparece el
    nombre ingresado en la lista. Imprime este conteo.
5.  Si el nombre aparece al menos una vez (es decir, su conteo es > 0):
    a. Utiliza el método `index()` para encontrar el índice de la PRIMERA
       aparición del nombre en la lista. Imprime este índice.
    b. (Opcional) Explica verbalmente o con pseudocódigo cómo encontrarías
       TODOS los índices donde aparece el nombre, no solo el primero.
6.  Si el nombre no aparece en la lista, informa al usuario.
-------------------------------------------------------------------------------
"""

# 1. Crear lista de invitados con nombres repetidos
invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]

# 2. Imprimir la lista
print("Lista de invitados:", invitados)
print("-----------------------------------------")

# 3. Preguntar al usuario qué nombre buscar
nombre_a_buscar = input("Ingresa el nombre que deseas buscar en la lista: ")

# 4. Usar count() para determinar cuántas veces aparece
conteo = invitados.count(nombre_a_buscar)
print(f"El nombre '{nombre_a_buscar}' aparece {conteo} vez/veces en la lista.")
print("-----------------------------------------")

# 5. Si el nombre aparece al menos una vez
if conteo > 0:
    # 5a. Usar index() para encontrar la primera aparición
    try:
        primer_indice = invitados.index(nombre_a_buscar)
        print(f"La primera aparición de '{nombre_a_buscar}' está en el índice: {primer_indice}")
    except ValueError:
        # Esto no debería ocurrir si conteo > 0, pero es buena práctica en general.
        print(f"Hubo un error inesperado al buscar el índice de '{nombre_a_buscar}'.")

    # 5b. (Opcional) Encontrar todos los índices
    print("\nBuscando todos los índices para:", nombre_a_buscar)
    indices_encontrados = []
    for i in range(len(invitados)):
        if invitados[i] == nombre_a_buscar:
            indices_encontrados.append(i)

    if indices_encontrados:
        print(f"'{nombre_a_buscar}' se encuentra en los siguientes índices: {indices_encontrados}")
    else: # Caso poco probable si conteo > 0, pero para completar la lógica
        print(f"No se encontraron más apariciones (esto es inesperado si el conteo fue > 0).")

else:
    # 6. Si el nombre no aparece
    print(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista de invitados.")

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué hace el método `count()` de las listas? ¿Qué tipo de valor devuelve?
2.  El método `index()` devuelve el índice de la primera ocurrencia de un elemento.
    ¿Qué sucede si intentas usar `index()` para buscar un elemento que NO está
    en la lista? ¿Cómo se llama el error que se produce?
3.  En la solución opcional para encontrar todos los índices, se usó un bucle `for`
    con `range(len(invitados))`. ¿Por qué se usa `len()` aquí? ¿Qué valores toma `i`?
4.  ¿Podrías usar el método `extend()` para agregar otra lista de invitados
    a la lista `invitados` existente? Crea una pequeña lista nueva y pruébalo.
    ¿Cuál es la diferencia entre `append()` y `extend()`?
-------------------------------------------------------------------------------
"""