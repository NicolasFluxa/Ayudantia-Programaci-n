"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                    Modificación Básica de Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio explora cómo modificar listas existentes utilizando métodos
básicos y asignación por índice.

1.  Crea una lista llamada `tareas_pendientes` con 3 tareas (strings).
    Ej: ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]
2.  Imprime la lista inicial.
3.  Supongamos que ya completaste la segunda tarea. Modifica el segundo
    elemento de la lista para que ahora diga (por ejemplo)
    "Estudiar Python (Completado)". Imprime la lista.
4.  Agrega una nueva tarea al FINAL de la lista usando el método `append()`.
    Ej: "Comprar pan". Imprime la lista.
5.  Agrega una tarea urgente al INICIO de la lista usando el método `insert()`.
    Ej: "Pasear al perro". Imprime la lista.
6.  Elimina la última tarea de la lista usando el método `pop()` e imprime
    la tarea eliminada y la lista resultante.
7.  Supongamos que quieres eliminar "Lavar la loza" (o la primera tarea que
    pusiste) por su valor. Usa el método `remove()`. Imprime la lista.
-------------------------------------------------------------------------------
"""

# 1. Crear lista de tareas pendientes
tareas_pendientes = ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]

# 2. Imprimir lista inicial
print("Lista de tareas inicial:", tareas_pendientes)
print("-----------------------------------------")

# 3. Modificar el segundo elemento (índice 1)
tareas_pendientes[1] = "Estudiar Python (Completado)"
print("Tarea modificada:", tareas_pendientes)
print("-----------------------------------------")

# 4. Agregar una nueva tarea al final con append()
tareas_pendientes.append("Comprar pan")
print("Después de append('Comprar pan'):", tareas_pendientes)
print("-----------------------------------------")

# 5. Agregar una tarea al inicio con insert()
# insert(indice, elemento)
tareas_pendientes.insert(0, "Pasear al perro")
print("Después de insert(0, 'Pasear al perro'):", tareas_pendientes)
print("-----------------------------------------")

# 6. Eliminar la última tarea con pop()
# pop() sin argumento elimina y devuelve el último elemento.
tarea_eliminada_pop = tareas_pendientes.pop()
print(f"Tarea eliminada con pop(): '{tarea_eliminada_pop}'")
print("Lista después de pop():", tareas_pendientes)
print("-----------------------------------------")

# 7. Eliminar una tarea específica por su valor con remove()
# remove() busca y elimina la primera ocurrencia del valor especificado.
# Si el elemento no existe, genera un ValueError.
tarea_a_remover = "Lavar la loza"
if tarea_a_remover in tareas_pendientes:
    tareas_pendientes.remove(tarea_a_remover)
    print(f"Después de remove('{tarea_a_remover}'):", tareas_pendientes)
else:
    print(f"La tarea '{tarea_a_remover}' no se encontró en la lista.")
print("-----------------------------------------")

print("Lista de tareas final:", tareas_pendientes)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia entre `append()` e `insert()` al agregar elementos
    a una lista?
2.  El método `pop()` puede usarse con o sin un índice. ¿Qué hace en cada caso?
    ¿Devuelve algún valor?
3.  ¿Qué sucede si intentas usar `remove()` para eliminar un elemento que no
    existe en la lista? ¿Cómo podrías evitar un error en ese caso?
4.  Si tienes una lista `mi_lista = [10, 20, 30, 20]` y ejecutas
    `mi_lista.remove(20)`, ¿cómo quedaría `mi_lista`? ¿Por qué?
-------------------------------------------------------------------------------
"""