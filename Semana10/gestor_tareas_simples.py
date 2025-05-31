"""
-------------------------------------------------------------------------------
                              PROYECTO 01
                         Gestor de Tareas Simple
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla una aplicación de línea de comandos para gestionar una lista de
tareas pendientes. La aplicación deberá permitir al usuario:
1.  Agregar nuevas tareas.
2.  Ver todas las tareas (mostrando su descripción y si están completadas).
3.  Marcar una tarea como completada.
4.  Eliminar una tarea.
5.  Salir de la aplicación.

Deberás estructurar tu código utilizando funciones para cada una de las
funcionalidades principales. Las tareas se almacenarán en una lista, donde
cada tarea podría ser un diccionario con su descripción y estado (completada/pendiente).
-------------------------------------------------------------------------------
"""

# Lista para almacenar las tareas. Cada tarea será un diccionario.
# Ejemplo de tarea: {"descripcion": "Hacer mercado", "completada": False}
lista_de_tareas = []

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("------------------------")

def agregar_tarea(tareas):
    """Solicita la descripción de una nueva tarea y la agrega a la lista."""
    descripcion = input("Introduce la descripción de la nueva tarea: ")
    if descripcion: # Asegurarse de que no esté vacía
        nueva_tarea = {"descripcion": descripcion, "completada": False}
        tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada con éxito.")
    else:
        print("La descripción de la tarea no puede estar vacía.")

def ver_tareas(tareas):
    """Muestra todas las tareas con su estado e índice."""
    print("\n--- Lista de Tareas Pendientes ---")
    if not tareas:
        print("¡No hay tareas en la lista! Puedes agregar algunas.")
        return

    for indice, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{indice + 1}. {tarea['descripcion']} - [{estado}]")
    print("---------------------------------")

def marcar_tarea_completa(tareas):
    """Permite al usuario marcar una tarea como completada por su número."""
    ver_tareas(tareas) # Mostrar tareas para que el usuario elija
    if not tareas:
        return

    try:
        num_tarea_str = input("Ingresa el número de la tarea a marcar como completada: ")
        num_tarea = int(num_tarea_str)
        indice_real = num_tarea - 1 # Convertir a índice de lista (base 0)

        if 0 <= indice_real < len(tareas):
            if not tareas[indice_real]["completada"]:
                tareas[indice_real]["completada"] = True
                print(f"Tarea '{tareas[indice_real]['descripcion']}' marcada como completada.")
            else:
                print(f"La tarea '{tareas[indice_real]['descripcion']}' ya estaba completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea por su número."""
    ver_tareas(tareas) # Mostrar tareas para que el usuario elija
    if not tareas:
        return

    try:
        num_tarea_str = input("Ingresa el número de la tarea a eliminar: ")
        num_tarea = int(num_tarea_str)
        indice_real = num_tarea - 1 # Convertir a índice de lista (base 0)

        if 0 <= indice_real < len(tareas):
            tarea_eliminada = tareas.pop(indice_real)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

# --- Bucle Principal de la Aplicación ---
def main():
    """Función principal que ejecuta el gestor de tareas."""
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            agregar_tarea(lista_de_tareas)
        elif opcion == "2":
            ver_tareas(lista_de_tareas)
        elif opcion == "3":
            marcar_tarea_completa(lista_de_tareas)
        elif opcion == "4":
            eliminar_tarea(lista_de_tareas)
        elif opcion == "5":
            print("Saliendo del Gestor de Tareas. ¡Hasta pronto!")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE DEL PROYECTO Y PREGUNTAS GUÍA:
## -------------------------------------------
1.  **Modularidad con Funciones:** ¿Cómo ayuda cada función a mantener el código
    organizado y legible? ¿Qué pasaría si todo este código estuviera sin funciones,
    directamente en el bucle `while`?
2.  **Manejo de Datos (Listas y Diccionarios):** ¿Por qué se eligió una lista de
    diccionarios para almacenar las tareas? ¿Qué información guarda cada diccionario?
3.  **Interacción con el Usuario:** ¿Cómo se maneja la entrada del usuario para
    seleccionar opciones del menú y para ingresar datos (descripción de tarea,
    número de tarea)?
4.  **Validación e Índices:** Al marcar o eliminar tareas, ¿por qué es importante
    convertir el número ingresado por el usuario a un índice de lista (restando 1)?
    ¿Qué tipo de errores se previenen con `try-except` y las validaciones de índice?
5.  **Reutilización:** La función `ver_tareas()` se llama desde varias partes del
    código. ¿Cuál es la ventaja de esto?
6.  **Posibles Mejoras (para pensar):**
    a. ¿Cómo podrías modificar el sistema para permitir editar la descripción de una tarea existente?
    b. ¿Cómo podrías guardar las tareas en un archivo para que persistan después
       de cerrar el programa (requiere investigar manejo de archivos)?
    c. ¿Se podrían añadir prioridades a las tareas?
-------------------------------------------------------------------------------
"""