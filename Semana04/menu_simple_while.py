"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                         Menú Simple con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un programa que muestre un menú simple al usuario y le permita elegir
una opción. El menú debe repetirse hasta que el usuario elija la opción de salir.

El programa debe:
1. Mostrar un menú con al menos 3 opciones, por ejemplo:
    "Menú Principal:"
    "1. Ver Saludo"
    "2. Mostrar Despedida"
    "3. Salir"
2. Usar un bucle `while` para que el menú se muestre repetidamente.
3. Solicitar al usuario que ingrese su opción.
4. Usar estructuras `if-elif-else` para procesar la opción:
    - Si elige "1", imprimir un saludo (ej: "¡Hola! Gracias por elegir esta opción.").
    - Si elige "2", imprimir una despedida (ej: "¡Adiós! Vuelve pronto.").
    - Si elige "3", terminar el bucle y el programa (ej: "Saliendo del programa...").
    - Si elige cualquier otra cosa, imprimir "Opción no válida. Intente de nuevo."
-------------------------------------------------------------------------------
"""

# Usaremos una variable para controlar el bucle del menú
opcion_elegida = ""

# 2. Bucle `while` para mostrar el menú
while opcion_elegida != "3": # Continuar mientras no se elija "3" (Salir)
    # 1. Mostrar el menú
    print("\n--- Menú Principal ---")
    print("1. Ver Saludo")
    print("2. Mostrar Despedida")
    print("3. Salir")
    print("----------------------")

    # 3. Solicitar opción al usuario
    opcion_elegida = input("Selecciona una opción (1-3): ")

    # 4. Procesar la opción
    if opcion_elegida == "1":
        print("\n¡Hola! 😊 Gracias por elegir esta opción.")
    elif opcion_elegida == "2":
        print("\n¡Adiós! 👋 Vuelve pronto.")
    elif opcion_elegida == "3":
        print("\nSaliendo del programa...")
    else:
        print("\nOpción no válida. Por favor, intente de nuevo.")

print("Programa finalizado.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la condición que mantiene el bucle `while` en ejecución? ¿Cuándo se detiene?
2. ¿Qué es un "centinela" en el contexto de los bucles? ¿Podrías identificar
   un valor que actúa como centinela en este programa?
3. Modifica el programa para añadir una cuarta opción al menú, por ejemplo,
   "4. Mostrar un chiste", e implementa su funcionalidad.
   Asegúrate de actualizar la condición del `while` si es necesario.
-------------------------------------------------------------------------------
"""