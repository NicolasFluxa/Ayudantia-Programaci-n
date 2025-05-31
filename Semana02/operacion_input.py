"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                   Operaciones Aritméticas con Input
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que realice lo siguiente:
1. Salude al usuario.
2. Solicite al usuario que ingrese un primer número entero.
3. Solicite al usuario que ingrese un segundo número entero.
4. Calcule y muestre:
    a. La suma de los dos números.
    b. La resta del primer número menos el segundo.
    c. La multiplicación de los dos números.
    d. La división del primer número entre el segundo (asegúrate de que sea división real).
5. Utiliza f-strings para mostrar los resultados de forma clara.
-------------------------------------------------------------------------------
"""

# 1. Saludar al usuario
print("¡Hola! Bienvenido/a a la calculadora básica.")
print("---------------------------------------------")

# 2. Solicitar el primer número entero
numero1_str = input("Por favor, ingresa el primer número entero: ")
numero1 = int(numero1_str) # Convertir la entrada a entero

# 3. Solicitar el segundo número entero
numero2_str = input("Ahora, ingresa el segundo número entero: ")
numero2 = int(numero2_str) # Convertir la entrada a entero

print("---------------------------------------------")
print(f"Números ingresados: {numero1} y {numero2}")
print("---------------------------------------------")

# 4. Calcular y mostrar los resultados
# a. Suma
suma = numero1 + numero2
print(f"La suma de {numero1} + {numero2} es: {suma}")

# b. Resta
resta = numero1 - numero2
print(f"La resta de {numero1} - {numero2} es: {resta}")

# c. Multiplicación
multiplicacion = numero1 * numero2
print(f"La multiplicación de {numero1} * {numero2} es: {multiplicacion}")

# d. División
# Nos aseguramos de que el divisor no sea cero antes de dividir
if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} / {numero2} es: {division:.2f}") # Mostrando con 2 decimales
else:
    print(f"No se puede dividir {numero1} entre {numero2} (división por cero).")

print("---------------------------------------------")
print("¡Cálculos completados!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué hace la función `input()` por defecto con la información que ingresa
   el usuario? ¿Por qué es necesario usar `int()` en este ejercicio?
2. ¿Qué pasaría si el usuario ingresara "hola" o "3.5" cuando se le pide un
   número entero? ¿Cómo reaccionaría el programa?
3. En la parte de la división, se incluyó una verificación `if numero2 != 0:`.
   ¿Por qué es importante esta verificación antes de intentar dividir?
   ¿Qué tipo de error se previene?
-------------------------------------------------------------------------------
"""