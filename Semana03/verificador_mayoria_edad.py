"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                       Verificar Mayoría de Edad
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que solicite al usuario su edad y determine si es mayor
de edad o no. En Chile, se considera mayor de edad a partir de los 18 años.

El programa debe:
1. Solicitar al usuario que ingrese su edad (como un número entero).
2. Utilizar una estructura condicional `if-else` para verificar si la edad
   ingresada es mayor o igual a 18.
3. Mostrar un mensaje apropiado indicando si el usuario es "Mayor de edad"
   o "Menor de edad".
-------------------------------------------------------------------------------
"""

# 1. Solicitar la edad al usuario
edad_str = input("Por favor, ingresa tu edad: ")
edad = int(edad_str) # Convertir la entrada a un número entero

# 2. Verificar si es mayor de edad usando if-else
if edad >= 18:
    # 3. Mostrar mensaje si es mayor de edad
    print("Eres Mayor de edad. ¡Bienvenido/a!")
else:
    # 3. Mostrar mensaje si es menor de edad
    print("Eres Menor de edad.")

# Mensaje final del programa (opcional)
print("------------------------------------")
print("Gracias por usar el verificador de edad.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué operador de comparación se utiliza para verificar si la edad es "mayor o igual a" 18?
   ¿Qué pasaría si solo usaras el operador `>` (mayor que)?
2. ¿Es obligatorio que un bloque `if` tenga siempre un bloque `else` asociado?
   ¿En qué situaciones podrías usar un `if` sin un `else`?
3. Modifica el programa para que, además de indicar si es mayor o menor de edad,
   si la persona tiene exactamente 18 años, imprima un mensaje adicional como
   "¡Felicitaciones, justo en la mayoría de edad!".
-------------------------------------------------------------------------------
"""