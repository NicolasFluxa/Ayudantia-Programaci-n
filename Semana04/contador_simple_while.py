"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                        Contador Simple con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que utilice un bucle `while` para contar y mostrar
los números desde 1 hasta un número ingresado por el usuario.

El programa debe:
1. Solicitar al usuario que ingrese un número entero positivo (el límite).
2. Inicializar una variable contador en 1.
3. Usar un bucle `while` que continúe mientras el contador sea menor o igual
   al número límite ingresado.
4. Dentro del bucle, imprimir el valor actual del contador.
5. Incrementar el contador en 1 en cada iteración.
-------------------------------------------------------------------------------
"""

# 1. Solicitar el número límite al usuario
limite_str = input("Ingresa un número entero positivo para contar hasta él: ")
limite = int(limite_str)

# Validar que el límite sea positivo (opcional, pero buena práctica)
if limite < 1:
    print("Por favor, ingresa un número entero positivo.")
else:
    # 2. Inicializar el contador
    contador = 1
    print(f"Contando desde 1 hasta {limite}:")

    # 3. Usar un bucle `while`
    while contador <= limite:
        # 4. Imprimir el valor actual del contador
        print(contador)
        # 5. Incrementar el contador
        contador = contador + 1 # También puede ser contador += 1

    print("¡Conteo finalizado!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué tres partes principales identificas en la estructura de este bucle `while`
   (inicialización, condición, actualización)?
2. ¿Qué pasaría si olvidaras la línea `contador = contador + 1` dentro del bucle?
   ¿Cómo se comportaría el programa? (Esto se conoce como bucle infinito).
3. Modifica el programa para que cuente hacia atrás, desde el número ingresado
   por el usuario hasta 1.
-------------------------------------------------------------------------------
"""