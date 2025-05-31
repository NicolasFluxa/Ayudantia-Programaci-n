"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                 Función para Análisis Simple de Lista
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea una función que reciba una lista de números y realice un análisis simple.

1.  Define una función llamada `analizar_lista_numeros(lista_de_numeros)`:
    a. Debe aceptar un parámetro: `lista_de_numeros` (se espera que sea una lista de números).
    b. Dentro de la función, primero verifica si la lista está vacía. Si lo está,
       la función debe retornar la cadena "La lista está vacía".
    c. Si la lista no está vacía:
        i.  Calcula la suma de todos los números en la lista (sin usar `sum()`).
        ii. Encuentra el número mayor en la lista (sin usar `max()`).
        iii.Retorna una cadena formateada que diga, por ejemplo:
            "Análisis: Suma = [suma_calculada], Mayor = [mayor_encontrado]".
2.  Crea dos listas de ejemplo: una con números y otra vacía.
3.  Llama a tu función `analizar_lista_numeros()` con cada una de estas listas
    e imprime el resultado que retorna la función.
-------------------------------------------------------------------------------
"""

def analizar_lista_numeros(lista_de_numeros):
    """
    Analiza una lista de números para encontrar la suma y el mayor elemento.

    Args:
        lista_de_numeros (list): Una lista de números (enteros o flotantes).

    Returns:
        str: Un mensaje con el análisis (suma y mayor) o un mensaje
             indicando que la lista está vacía.
    """
    # b. Verificar si la lista está vacía
    if not lista_de_numeros: # Una lista vacía se evalúa como False en un contexto booleano
        return "La lista está vacía y no se puede analizar."

    # c. Si la lista no está vacía:
    # i. Calcular la suma
    suma_calculada = 0
    for numero in lista_de_numeros:
        suma_calculada += numero

    # ii. Encontrar el número mayor
    mayor_encontrado = lista_de_numeros[0] # Asumimos el primero como el mayor inicialmente
    for numero in lista_de_numeros:
        if numero > mayor_encontrado:
            mayor_encontrado = numero

    # iii. Retornar el mensaje formateado
    return f"Análisis de la lista: Suma = {suma_calculada}, Número Mayor = {mayor_encontrado}"

# 2. Crear listas de ejemplo
numeros_ejemplo1 = [10, 5, 25, 8, 15, -3]
numeros_ejemplo2 = [] # Lista vacía
numeros_ejemplo3 = [100, 200, 50]

print("--- Probando la función analizar_lista_numeros ---")

# 3. Llamar a la función e imprimir resultados
resultado1 = analizar_lista_numeros(numeros_ejemplo1)
print(f"Para {numeros_ejemplo1}: {resultado1}")

resultado2 = analizar_lista_numeros(numeros_ejemplo2)
print(f"Para {numeros_ejemplo2}: {resultado2}")

resultado3 = analizar_lista_numeros(numeros_ejemplo3)
print(f"Para {numeros_ejemplo3}: {resultado3}")

print("-------------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En la función `analizar_lista_numeros`, ¿cómo se verifica si la lista
    está vacía? ¿Qué otras formas conoces para hacer esta verificación?
2.  Al buscar el número mayor, ¿por qué es importante inicializar `mayor_encontrado`
    con un elemento de la propia lista en lugar de un valor fijo como 0?
    ¿Qué problema podría surgir si lo inicializaras a 0 y todos los números
    de la lista fueran negativos?
3.  Esta función retorna una cadena de texto. ¿Podría una función retornar
    múltiples valores, por ejemplo, la suma y el mayor como números separados?
    Si es así, ¿cómo se haría y qué tipo de dato retornaría la función en ese caso?
    (Pista: Tuplas).
4.  ¿Cómo modificarías la función para que también calcule y retorne el número
    menor de la lista?
-------------------------------------------------------------------------------
"""