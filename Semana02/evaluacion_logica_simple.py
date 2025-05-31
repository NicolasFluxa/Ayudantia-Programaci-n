"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                     Evaluación Lógica Simple
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este programa explorará los operadores de comparación y lógicos.
1. Pide al usuario que ingrese dos números enteros, `a` y `b`.
2. Evalúa e imprime el resultado (True o False) de las siguientes
   comparaciones:
    a. ¿Es `a` mayor que `b`?
    b. ¿Es `a` menor o igual que `b`?
    c. ¿Son `a` y `b` iguales?
    d. ¿Son `a` y `b` diferentes?
3. Declara dos variables booleanas, `condicion1 = True` y `condicion2 = False`.
4. Evalúa e imprime el resultado de las siguientes operaciones lógicas:
    a. `condicion1 and condicion2`
    b. `condicion1 or condicion2`
    c. `not condicion1`
    d. `(a > 0) and (b > 0)` (Verifica si ambos números ingresados son positivos)
-------------------------------------------------------------------------------
"""

# 1. Pedir al usuario dos números enteros
a_str = input("Ingresa el primer número entero (a): ")
a = int(a_str)

b_str = input("Ingresa el segundo número entero (b): ")
b = int(b_str)

print(f"\nHas ingresado a = {a} y b = {b}")
print("--- Resultados de Comparaciones ---")

# 2. Evaluar e imprimir comparaciones
# a. ¿Es a mayor que b?
resultado_mayor_que = a > b
print(f"¿Es {a} > {b}?: {resultado_mayor_que}")

# b. ¿Es a menor o igual que b?
resultado_menor_igual = a <= b
print(f"¿Es {a} <= {b}?: {resultado_menor_igual}")

# c. ¿Son a y b iguales?
resultado_iguales = a == b
print(f"¿Es {a} == {b}?: {resultado_iguales}")

# d. ¿Son a y b diferentes?
resultado_diferentes = a != b
print(f"¿Es {a} != {b}?: {resultado_diferentes}")

print("\n--- Resultados de Operaciones Lógicas ---")
# 3. Declarar variables booleanas
condicion1 = True
condicion2 = False
print(f"condicion1 = {condicion1}, condicion2 = {condicion2}")

# 4. Evaluar e imprimir operaciones lógicas
# a. condicion1 and condicion2
op_and = condicion1 and condicion2
print(f"{condicion1} and {condicion2}: {op_and}")

# b. condicion1 or condicion2
op_or = condicion1 or condicion2
print(f"{condicion1} or {condicion2}: {op_or}")

# c. not condicion1
op_not = not condicion1
print(f"not {condicion1}: {op_not}")

# d. (a > 0) and (b > 0)
ambos_positivos = (a > 0) and (b > 0)
print(f"¿Son {a} y {b} ambos positivos? ({a} > 0) and ({b} > 0): {ambos_positivos}")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la diferencia entre el operador `=` (asignación) y el operador `==` (comparación)?
   Proporciona un ejemplo de cada uno.
2. Explica con tus palabras cómo funciona el operador `and`. ¿En qué caso(s)
   una expresión con `and` devuelve `True`?
3. Si `condicion1` fuera `False` y `condicion2` fuera `False`, ¿cuál sería el
   resultado de `condicion1 or condicion2`? ¿Y de `not condicion2`?
4. ¿Podrías escribir una expresión lógica que sea `True` si al menos uno de los
   números `a` o `b` es igual a cero, y `False` en caso contrario?
-------------------------------------------------------------------------------
"""