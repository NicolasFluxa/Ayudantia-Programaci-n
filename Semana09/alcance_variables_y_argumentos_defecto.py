"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
          Alcance de Variables y Argumentos por Defecto en Funciones
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio explora cómo funcionan las variables dentro y fuera de las
funciones (alcance) y cómo definir funciones con parámetros que tienen
valores por defecto.

1.  **Alcance de Variables:**
    a. Declara una variable global `mensaje_global = "Soy global"`.
    b. Define una función `probar_alcance()`:
        i.  Dentro de esta función, declara una variable local
            `mensaje_local = "Soy local"`.
        ii. Imprime `mensaje_local` desde dentro de la función.
        iii.Intenta imprimir `mensaje_global` desde dentro de la función.
    c. Llama a `probar_alcance()`.
    d. Después de llamar a la función, intenta imprimir `mensaje_local`
       fuera de la función. Observa y explica el error (si lo hay).
    e. Intenta imprimir `mensaje_global` fuera de la función.

2.  **Argumentos por Defecto:**
    a. Define una función `configurar_notificacion(mensaje, tipo="informativo", repetir=1)`:
        i.  `mensaje` es un parámetro obligatorio.
        ii. `tipo` debe tener un valor por defecto "informativo".
        iii.`repetir` debe tener un valor por defecto 1.
        iv. La función debe imprimir el mensaje, su tipo y cuántas veces se repetirá.
    b. Llama a `configurar_notificacion` de las siguientes maneras:
        i.  Solo con el `mensaje` obligatorio.
        ii. Con `mensaje` y `tipo`.
        iii.Con `mensaje`, `tipo` y `repetir`.
        iv. Con `mensaje` y `repetir` (usando argumento de palabra clave para `repetir`).
-------------------------------------------------------------------------------
"""

# 1. Alcance de Variables
print("--- 1. Alcance de Variables ---")
mensaje_global = "Soy global y existo fuera de cualquier función." # a. Variable global

def probar_alcance():
    """Demuestra el alcance de variables locales y globales."""
    # b.i. Variable local
    mensaje_local = "Soy local y solo existo dentro de probar_alcance()."
    # b.ii. Imprimir variable local (desde dentro)
    print(f"Dentro de la función, mensaje_local: '{mensaje_local}'")
    # b.iii. Imprimir variable global (desde dentro)
    print(f"Dentro de la función, mensaje_global: '{mensaje_global}'")

# c. Llamar a la función
probar_alcance()

# d. Intentar imprimir mensaje_local fuera de la función
print("\nIntentando acceder a mensaje_local fuera de la función:")
try:
    print(mensaje_local)
except NameError as e:
    print(f"Error: {e}. 'mensaje_local' no está definida fuera de la función.")

# e. Intentar imprimir mensaje_global fuera de la función
print(f"\nFuera de la función, mensaje_global: '{mensaje_global}'")
print("-----------------------------------------")


# 2. Argumentos por Defecto
print("\n--- 2. Argumentos por Defecto ---")
def configurar_notificacion(mensaje, tipo="informativo", repetir=1):
    """Configura y muestra una notificación con tipo y repeticiones opcionales."""
    print(f"\nNotificación:")
    print(f"  Mensaje: '{mensaje}'")
    print(f"  Tipo   : '{tipo}'")
    print(f"  Repetir: {repetir} vez/veces")

# b.i. Solo con el mensaje obligatorio
print("\nLlamada 1 (solo mensaje):")
configurar_notificacion("Actualización del sistema completada.")

# b.ii. Con mensaje y tipo
print("\nLlamada 2 (mensaje y tipo):")
configurar_notificacion("Error crítico en el servidor.", tipo="urgente")

# b.iii. Con mensaje, tipo y repetir
print("\nLlamada 3 (todos los argumentos posicionales):")
configurar_notificacion("Recordatorio: reunión a las 10 AM", tipo="recordatorio", repetir=3)

# b.iv. Con mensaje y repetir (usando argumento de palabra clave para repetir)
# Esto demuestra que podemos omitir un argumento por defecto intermedio
# si usamos argumentos por palabra clave para los que siguen.
print("\nLlamada 4 (mensaje y repetir, omitiendo tipo):")
configurar_notificacion("Oferta especial solo por hoy.", repetir=2)

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Explica con tus palabras la diferencia entre una variable local y una global.
    ¿Desde dónde se puede acceder a cada una?
2.  ¿Qué sucede si intentas modificar una variable global directamente dentro de
    una función sin usar la palabra clave `global`? (Investiga la palabra clave `global`).
3.  ¿Cuál es la ventaja de usar argumentos por defecto en una función?
4.  En la "Llamada 4" a `configurar_notificacion`, ¿por qué fue necesario usar
    `repetir=2` (argumento por palabra clave) en lugar de solo `2`?
-------------------------------------------------------------------------------
"""