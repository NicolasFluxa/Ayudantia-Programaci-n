"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                      Contador con `for` y `range()`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que utilice un bucle `for` y la función `range()` para
realizar diferentes tipos de conteos:

1.  Solicita al usuario un número entero positivo (`limite`).
    Imprime los números desde 0 hasta `limite - 1`.
2.  Utilizando el mismo `limite`, imprime los números desde 1 hasta `limite`.
3.  Utilizando el mismo `limite`, imprime solo los números pares desde 0
    hasta `limite` (incluido si `limite` es par).
-------------------------------------------------------------------------------
"""

# 1. Solicitar el número límite
limite_str = input("Ingresa un número entero positivo (límite): ")
limite = int(limite_str)

if limite < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Conteo desde 0 hasta limite - 1
    print(f"\n--- Conteo 1: Números desde 0 hasta {limite - 1} ---")
    for i in range(limite): # range(limite) genera números de 0 a limite-1
        print(i)

    # Conteo desde 1 hasta limite
    print(f"\n--- Conteo 2: Números desde 1 hasta {limite} ---")
    # range(inicio, fin) genera números desde inicio hasta fin-1
    # Por eso usamos limite + 1 para incluir el 'limite'
    for i in range(1, limite + 1):
        print(i)

    # Conteo de números pares desde 0 hasta limite
    print(f"\n--- Conteo 3: Números pares desde 0 hasta {limite} ---")
    # range(inicio, fin, paso) genera números desde inicio hasta fin-1,
    # incrementando en 'paso'
    # Para incluir 'limite' si es par, vamos hasta limite + 1
    for i in range(0, limite + 1, 2):
        print(i)

    print("\n¡Conteos finalizados!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Explica las tres formas de usar `range()` que viste en este ejercicio:
    a) `range(stop)`
    b) `range(start, stop)`
    c) `range(start, stop, step)`
2.  Si quisieras imprimir los números del 10 al 1 (en orden descendente) usando
    `for` y `range()`, ¿cómo lo harías? (Pista: el `step` puede ser negativo).
3.  ¿Qué sucede si el valor de `start` es mayor que `stop` y el `step` es positivo
    en `range(start, stop, step)`?
-------------------------------------------------------------------------------
"""