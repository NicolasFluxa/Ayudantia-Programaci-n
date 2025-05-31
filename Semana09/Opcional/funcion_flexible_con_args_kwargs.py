"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
           Funciones Flexibles con `*args` y `**kwargs` (Introducción)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Python permite definir funciones que pueden aceptar un número variable de
argumentos posicionales (`*args`) y/o argumentos por palabra clave (`**kwargs`).

1.  **Uso de `*args`:**
    a. Define una función llamada `imprimir_argumentos(*args)`:
        i.  Esta función aceptará cualquier número de argumentos posicionales.
        ii. `args` será una tupla que contendrá todos los argumentos posicionales pasados.
        iii.Dentro de la función, imprime el tipo de `args` y luego itera sobre
            `args` para imprimir cada argumento recibido.
    b. Llama a `imprimir_argumentos` con diferentes cantidades de argumentos
       (ej: con 1, con 3, con una mezcla de números y strings).

2.  **Uso de `**kwargs`:**
    a. Define una función llamada `mostrar_detalles_producto(**kwargs)`:
        i.  Esta función aceptará cualquier número de argumentos por palabra clave.
        ii. `kwargs` será un diccionario que contendrá estos argumentos.
        iii.Dentro de la función, imprime el tipo de `kwargs`. Luego itera sobre
            los ítems (clave, valor) de `kwargs` e imprime cada uno.
    b. Llama a `mostrar_detalles_producto` con diferentes conjuntos de
       argumentos por palabra clave (ej: `nombre="Laptop"`, `precio=800`,
       `marca="TechCo"`).

3.  **Combinando todo (Opcional Avanzado):**
    a. Define una función `reporte_completo(titulo, *items_lista, **detalles_extra)`
    b. Imprime el título.
    c. Imprime cada ítem de `items_lista`.
    d. Imprime cada par clave-valor de `detalles_extra`.
    e. Llama a esta función con un ejemplo.
-------------------------------------------------------------------------------
"""

# 1. Uso de *args
print("--- 1. Probando *args ---")
def imprimir_argumentos(*args):
    """Imprime todos los argumentos posicionales recibidos."""
    print(f"  Tipo de 'args': {type(args)}")
    if not args:
        print("  No se recibieron argumentos posicionales.")
        return
    print("  Argumentos recibidos:")
    for i, arg_item in enumerate(args):
        print(f"    args[{i}]: {arg_item} (tipo: {type(arg_item)})")

imprimir_argumentos(10)
imprimir_argumentos("Hola", 25.5, True, [1, 2])
imprimir_argumentos() # Sin argumentos
print("-----------------------------------------")


# 2. Uso de **kwargs
print("\n--- 2. Probando **kwargs ---")
def mostrar_detalles_producto(**kwargs):
    """Muestra todos los detalles (argumentos por palabra clave) recibidos."""
    print(f"  Tipo de 'kwargs': {type(kwargs)}")
    if not kwargs:
        print("  No se recibieron detalles (argumentos por palabra clave).")
        return
    print("  Detalles del producto recibidos:")
    for clave, valor in kwargs.items():
        print(f"    {clave}: {valor}")

mostrar_detalles_producto(nombre="Teclado Mecánico", precio=75, color="Negro", stock=50)
mostrar_detalles_producto(id_producto="XYZ123", descripcion="Mouse ergonómico inalámbrico")
mostrar_detalles_producto() # Sin argumentos de palabra clave
print("-----------------------------------------")


# 3. Combinando todo (Opcional Avanzado)
print("\n--- 3. Probando una función con todo (*args y **kwargs) ---")
def reporte_completo(titulo, *items_lista, **detalles_extra):
    """Genera un reporte completo con título, lista de ítems y detalles extra."""
    print(f"\n== {titulo.upper()} ==")

    if items_lista:
        print("\n  --- Ítems Principales ---")
        for i, item in enumerate(items_lista):
            print(f"    {i+1}. {item}")
    else:
        print("\n  (No hay ítems principales en la lista)")

    if detalles_extra:
        print("\n  --- Detalles Adicionales ---")
        for clave, valor in detalles_extra.items():
            print(f"    {clave.replace('_', ' ').capitalize()}: {valor}")
    else:
        print("\n  (No hay detalles adicionales)")
    print("============================")

reporte_completo(
    "Reporte de Ventas - Mayo", # titulo (argumento posicional normal)
    "Producto A: 100 unidades", # *items_lista
    "Producto B: 150 unidades", # *items_lista
    "Producto C: 75 unidades",  # *items_lista
    responsable="Juanita Rojas", # **detalles_extra
    total_ventas=32500,          # **detalles_extra
    region="Norte"               # **detalles_extra
)

reporte_completo(
    "Notas del Estudiante",
    "Matemáticas: 6.5",
    "Lenguaje: 5.8",
    nombre_estudiante="Pedro Pascal",
    curso="3ro Medio"
)
print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Cuando una función se define con `*args`, ¿qué tipo de estructura de datos
    es `args` dentro de la función? ¿Qué contiene?
2.  Cuando una función se define con `**kwargs`, ¿qué tipo de estructura de datos
    es `kwargs` dentro de la función? ¿Qué contiene?
3.  ¿Es obligatorio usar los nombres `args` y `kwargs`? ¿O son solo una convención?
4.  Si una función se define como `def mi_funcion(a, b, *args, opcion=True, **kwargs):`,
    ¿cuál es el orden correcto en el que deben aparecer estos tipos de parámetros
    en la definición de la función?
-------------------------------------------------------------------------------
"""