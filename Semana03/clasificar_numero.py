"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                         Clasificar un Número
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla un programa que solicite al usuario ingresar un número entero
y clasifique dicho número como "Positivo", "Negativo" o "Cero".

El programa debe:
1. Pedir al usuario que ingrese un número entero.
2. Utilizar una estructura condicional `if-elif-else` para determinar
   si el número es:
    a. Mayor que cero (Positivo).
    b. Menor que cero (Negativo).
    c. Igual a cero (Cero).
3. Imprimir la clasificación correspondiente.
-------------------------------------------------------------------------------
"""

# 1. Pedir al usuario un número entero
numero_str = input("Ingresa un número entero: ")
numero = int(numero_str) # Convertir a entero

# 2. Clasificar el número usando if-elif-else
if numero > 0:
    # 3a. Imprimir si es positivo
    clasificacion = "Positivo"
elif numero < 0:
    # 3b. Imprimir si es negativo
    clasificacion = "Negativo"
else:
    # 3c. Imprimir si es cero
    clasificacion = "Cero"

# Imprimir el resultado
print(f"El número {numero} es {clasificacion}.")
print("------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la diferencia fundamental entre usar múltiples `if` separados y usar
   una estructura `if-elif-else`? ¿Cuándo elegirías una sobre la otra?
2. ¿Qué sucedería en este programa si el usuario ingresa un texto como "hola"
   en lugar de un número? (Considera la línea donde se usa `int()`).
   Aunque aún no lo hemos visto en detalle, ¿cómo crees que se podría manejar este tipo de error?
3. Escribe una condición alternativa para verificar si un número es cero sin usar `else`
   directamente para esa condición (podrías usar un `elif numero == 0:` por ejemplo).
   ¿Cambiaría el comportamiento del programa si lo haces así y ajustas el `else` final?
-------------------------------------------------------------------------------
"""