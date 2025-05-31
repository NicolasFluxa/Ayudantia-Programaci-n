"""
-------------------------------------------------------------------------------
                              PROYECTO 02
                Extensión: Buscar Tarea en Gestor de Tareas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio es una extensión del "Gestor de Tareas Simple".
Se te pide agregar una nueva funcionalidad: buscar tareas por una palabra clave.

1.  Define una nueva función llamada `buscar_tareas_por_palabra(tareas, palabra_clave)`:
    a.  Debe recibir la lista de `tareas` y una `palabra_clave` (string) como parámetros.
    b.  Debe crear una nueva lista (ej: `encontradas`) que contenga todas las tareas
        cuya descripción contenga la `palabra_clave` (sin importar mayúsculas/minúsculas).
    c.  Si se encuentran tareas, la función debe imprimir estas tareas encontradas
        (puedes reutilizar o adaptar parte de la lógica de `ver_tareas` para mostrarlas).
    d.  Si no se encuentra ninguna tarea que coincida, debe imprimir un mensaje indicándolo.
    e.  Esta función NO debe modificar la lista original de tareas.

2.  Modifica la función `main()` y `mostrar_menu()` del "Gestor de Tareas Simple"
    para incluir esta nueva opción (por ejemplo, "Buscar tarea").
3.  Cuando el usuario elija la opción de buscar, el programa debe solicitarle
    la palabra clave y luego llamar a la función `buscar_tareas_por_palabra()`.
-------------------------------------------------------------------------------
"""

# --- COPIA Y PEGA AQUÍ LAS FUNCIONES DEL PROYECTO_01_GESTOR_TAREAS_SIMPLE ---
# (mostrar_menu, agregar_tarea, ver_tareas, marcar_tarea_completa, eliminar_tarea)
# Y la lista_de_tareas global.
# ... (Para brevedad, no se repiten aquí, pero el estudiante debe copiarlas)

lista_de_tareas = [] # Asegúrate de tener esta línea

def mostrar_menu_extendido(): # Nombre modificado para la nueva versión
    """Muestra el menú de opciones al usuario, incluyendo buscar."""
    print("\n--- Gestor de Tareas Extendido ---")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea por palabra clave") # Nueva opción
    print("6. Salir") # Salir ahora es la opción 6
    print("----------------------------------")

# Funciones del proyecto anterior (agregar_tarea, ver_tareas_original, marcar_tarea_completa, eliminar_tarea)
# Deberían ser copiadas aquí por el estudiante.
# Ejemplo de cómo se vería ver_tareas para reutilizar:
def ver_tareas_filtradas(tareas, titulo="--- Lista de Tareas ---"):
    """Muestra una lista de tareas con su estado e índice."""
    print(f"\n{titulo}")
    if not tareas:
        print("¡No hay tareas que coincidan con los criterios!")
        return False # Indica que no se imprimieron tareas

    for indice, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        # Podríamos mostrar el índice original si la lista filtrada es temporal
        # o un nuevo índice si es una sub-selección para operar.
        # Por simplicidad, aquí mostramos con un nuevo índice.
        print(f"{indice + 1}. {tarea['descripcion']} - [{estado}]")
    print("---------------------------------")
    return True # Indica que se imprimieron tareas

# (El estudiante debe copiar las otras funciones aquí y adaptarlas si es necesario)
# Por ejemplo, la función original ver_tareas:
def ver_todas_las_tareas(tareas): # Renombrada para evitar conflicto si se copia/pega
    ver_tareas_filtradas(tareas, "--- Lista de Tareas Pendientes ---")


# 1. Nueva función para buscar tareas
def buscar_tareas_por_palabra(tareas, palabra_clave):
    """
    Busca tareas que contengan una palabra clave en su descripción.

    Args:
        tareas (list): La lista completa de tareas.
        palabra_clave (str): La palabra a buscar en las descripciones.
    """
    if not palabra_clave.strip():
        print("La palabra clave para buscar no puede estar vacía.")
        return

    encontradas = []
    palabra_clave_lower = palabra_clave.lower() # Para búsqueda case-insensitive

    for tarea in tareas:
        if palabra_clave_lower in tarea["descripcion"].lower():
            encontradas.append(tarea)

    # c. Imprimir tareas encontradas (reutilizando/adaptando ver_tareas_filtradas)
    if encontradas:
        print(f"\n--- Tareas encontradas con la palabra clave '{palabra_clave}' ---")
        ver_tareas_filtradas(encontradas, f"Resultados para '{palabra_clave}':")
    else:
        # d. Si no se encuentran tareas
        print(f"No se encontraron tareas que contengan la palabra clave '{palabra_clave}'.")


# --- Bucle Principal de la Aplicación (Modificado) ---
def main_extendido(): # Nombre modificado para la nueva versión
    """Función principal que ejecuta el gestor de tareas extendido."""
    opcion = ""
    # El estudiante debe asegurarse que lista_de_tareas se usa consistentemente
    # (puede ser global como en el original, o pasada como argumento)

    # Cargar algunas tareas de ejemplo para probar la búsqueda rápidamente:
    if not lista_de_tareas: # Solo si está vacía para no duplicar en ejecuciones de prueba
        lista_de_tareas.append({"descripcion": "Comprar leche y pan", "completada": False})
        lista_de_tareas.append({"descripcion": "Preparar presentación de Python", "completada": False})
        lista_de_tareas.append({"descripcion": "Llamar al electricista", "completada": True})
        lista_de_tareas.append({"descripcion": "Leer capítulo 5 del libro de Python", "completada": False})


    while opcion != "6": # Salir ahora es la opción 6
        mostrar_menu_extendido()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            # agregar_tarea(lista_de_tareas) # El estudiante debe tener esta función
            print("Llamar a agregar_tarea...") # Placeholder si no se copió
        elif opcion == "2":
            # ver_todas_las_tareas(lista_de_tareas) # El estudiante debe tener esta función
            print("Llamar a ver_todas_las_tareas...") # Placeholder
        elif opcion == "3":
            # marcar_tarea_completa(lista_de_tareas) # El estudiante debe tener esta función
            print("Llamar a marcar_tarea_completa...") # Placeholder
        elif opcion == "4":
            # eliminar_tarea(lista_de_tareas) # El estudiante debe tener esta función
            print("Llamar a eliminar_tarea...") # Placeholder
        elif opcion == "5": # Nueva opción
            palabra_clave_buscar = input("Ingresa la palabra clave para buscar en las tareas: ")
            buscar_tareas_por_palabra(lista_de_tareas, palabra_clave_buscar)
        elif opcion == "6":
            print("Saliendo del Gestor de Tareas Extendido. ¡Hasta pronto!")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la aplicación extendida
if __name__ == "__main__":
    # Nota: El estudiante debe integrar las funciones del proyecto 1 aquí
    # para que esta versión extendida funcione completamente.
    # Por ahora, se ponen placeholders para las llamadas a funciones no definidas aquí.
    # Se simula la adición de algunas tareas para probar la búsqueda si se ejecuta directamente.

    # Placeholder para simular la función agregar_tarea del proyecto 1
    def agregar_tarea(tareas):
        descripcion = input("(Simulado) Introduce la descripción de la nueva tarea: ")
        if descripcion:
            tareas.append({"descripcion": descripcion, "completada": False})
            print(f"Tarea '{descripcion}' agregada.")

    # Placeholder para simular la función ver_todas_las_tareas del proyecto 1
    def ver_todas_las_tareas(tareas):
        ver_tareas_filtradas(tareas, "--- (Simulado) Lista de Tareas Pendientes ---")

    # Placeholder para simular marcar_tarea_completa
    def marcar_tarea_completa(tareas):
        print("(Simulado) Marcar tarea como completada...")
        ver_todas_las_tareas(tareas)
        # Lógica de selección y cambio de estado iría aquí

    # Placeholder para simular eliminar_tarea
    def eliminar_tarea(tareas):
        print("(Simulado) Eliminar tarea...")
        ver_todas_las_tareas(tareas)
        # Lógica de selección y pop iría aquí

    main_extendido()


"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Reutilización y Adaptación:** ¿Cómo se podría reutilizar la función
    `ver_tareas` (o una versión modificada de ella) para mostrar los resultados
    de la búsqueda sin duplicar mucho código? (La solución usa `ver_tareas_filtradas`).
2.  **Búsqueda Case-Insensitive:** En la función `buscar_tareas_por_palabra`,
    ¿cómo se logra que la búsqueda no distinga entre mayúsculas y minúsculas
    tanto en la palabra clave como en la descripción de la tarea?
3.  **Lista de Resultados:** La función de búsqueda crea una nueva lista `encontradas`.
    ¿Por qué es esto una buena práctica en lugar de, por ejemplo, modificar
    directamente la lista original o solo imprimir los hallazgos?
4.  **Integración:** ¿Qué cambios fueron necesarios en `mostrar_menu()` y en el
    bucle `while` principal de `main()` para incorporar esta nueva funcionalidad?
5.  **Pruebas:** ¿Qué casos de prueba considerarías para la función de búsqueda
    (ej: palabra clave existe, no existe, palabra clave vacía, mayúsculas/minúsculas,
    palabra clave es parte de una palabra más larga en la descripción)?
-------------------------------------------------------------------------------
"""