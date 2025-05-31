"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                        Iterar sobre un String con `for`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que solicite al usuario ingresar una palabra o frase
y luego utilice un bucle `for` para realizar las siguientes acciones:

1.  Imprimir cada carácter de la palabra o frase en una línea diferente.
2.  Contar y mostrar cuántas vocales ('a', 'e', 'i', 'o', 'u',
    ignorando mayúsculas/minúsculas) hay en la palabra o frase.
3.  (Opcional) Crear una nueva cadena que sea la inversa de la cadena ingresada.
-------------------------------------------------------------------------------
"""

# Solicitar palabra o frase al usuario
texto_usuario = input("Ingresa una palabra o una frase: ")

print("\n--- 1. Imprimiendo cada carácter ---")
# 1. Imprimir cada carácter
for caracter in texto_usuario:
    print(caracter)

# 2. Contar vocales
contador_vocales = 0
vocales = "aeiouAEIOU" # Cadena con todas las vocales para facilitar la comprobación

for caracter in texto_usuario:
    if caracter in vocales: # Comprueba si el caracter está en la cadena de vocales
        contador_vocales = contador_vocales + 1

print("\n--- 2. Conteo de vocales ---")
print(f"La palabra o frase '{texto_usuario}' tiene {contador_vocales} vocal(es).")


# 3. (Opcional) Crear cadena inversa
texto_inverso = ""
# Iteramos sobre el texto original
for caracter in texto_usuario:
    # Añadimos el caracter actual al PRINCIPIO del texto_inverso
    texto_inverso = caracter + texto_inverso

print("\n--- 3. (Opcional) Cadena Inversa ---")
print(f"El texto original es: '{texto_usuario}'")
print(f"El texto invertido es: '{texto_inverso}'")


print("\n¡Proceso completado!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En el bucle `for caracter in texto_usuario:`, ¿qué representa la variable
    `caracter` en cada iteración?
2.  Para el conteo de vocales, se usó `if caracter in vocales:`.
    Explica cómo funciona el operador `in` cuando se usa con cadenas de texto.
3.  En la parte opcional de invertir la cadena, ¿por qué la línea
    `texto_inverso = caracter + texto_inverso` logra invertirla?
    ¿Qué pasaría si usaras `texto_inverso = texto_inverso + caracter`?
-------------------------------------------------------------------------------
"""