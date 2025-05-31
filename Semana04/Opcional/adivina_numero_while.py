"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                       Adivina el Número con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un juego simple donde el programa "piensa" un número secreto y el
usuario tiene que adivinarlo.

El programa debe:
1. Definir un número secreto (puedes "hardcodearlo", es decir, escribirlo
   directamente en el código, por ejemplo: `numero_secreto = 7`).
2. Inicializar una variable para el intento del usuario.
3. Usar un bucle `while` que continúe mientras el intento del usuario
   NO sea igual al número secreto.
4. Dentro del bucle:
    a. Solicitar al usuario que ingrese su intento (un número entero).
    b. Usar condicionales (`if-elif-else` o `if-if`) para indicar si el
       intento fue "muy alto", "muy bajo" o si adivinó correctamente.
5. Cuando el usuario adivine, imprimir un mensaje de felicitaciones
   y terminar el bucle.
(Opcional Avanzado): Contar cuántos intentos le tomó al usuario adivinar.
-------------------------------------------------------------------------------
"""

# 1. Definir el número secreto
numero_secreto = 42
# (Para hacerlo más interesante, podrías usar la biblioteca `random` para generar
# un número aleatorio, pero por ahora lo dejaremos fijo)

# 2. Inicializar variables
intento_usuario = 0 # Un valor inicial que no sea el número secreto
intentos_realizados = 0 # Opcional: contador de intentos

print("¡Bienvenido al juego 'Adivina el Número'!")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")
print("----------------------------------------------------")

# 3. Bucle `while` mientras no adivine
while intento_usuario != numero_secreto:
    # 4a. Solicitar intento al usuario
    intento_str = input("Ingresa tu intento: ")
    intento_usuario = int(intento_str)

    intentos_realizados = intentos_realizados + 1 # Opcional

    # 4b. Comparar y dar pistas
    if intento_usuario < numero_secreto:
        print("Tu intento es muy bajo. ¡Sigue intentando!")
    elif intento_usuario > numero_secreto:
        print("Tu intento es muy alto. ¡Sigue intentando!")
    else:
        # 5. Mensaje de felicitaciones al adivinar
        print(f"\n¡Felicidades! 🎉 ¡Has adivinado el número secreto: {numero_secreto}!")
        print(f"Te tomó {intentos_realizados} intento(s).") # Opcional

print("----------------------------------------------------")
print("¡Gracias por jugar!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la condición principal que controla el bucle `while` en este juego?
2. Si el número secreto fuera 50 y el usuario ingresa 50 en el primer intento,
   ¿cuántas veces se ejecutaría el cuerpo del bucle `while`? ¿Por qué?
3. ¿Qué pasaría si inicializaras `intento_usuario = numero_secreto` antes de
   que comience el bucle `while`?
4. (Referente a la parte opcional) ¿Dónde y por qué se incrementa la variable
   `intentos_realizados`?
-------------------------------------------------------------------------------
"""