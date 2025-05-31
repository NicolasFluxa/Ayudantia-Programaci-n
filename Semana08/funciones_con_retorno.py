"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                  Funciones Simples y con Parámetros
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te enseñará a definir y llamar funciones básicas, algunas de
ellas con parámetros.

1.  Define una función llamada `mostrar_saludo_simple()`:
    a. Esta función no debe recibir parámetros.
    b. Dentro de la función, simplemente imprime el mensaje "¡Hola, mundo desde una función!".
    c. Llama (ejecuta) esta función una vez.

2.  Define una función llamada `saludar_usuario(nombre_usuario)`:
    a. Esta función debe recibir un parámetro llamado `nombre_usuario`.
    b. Dentro de la función, imprime un saludo personalizado, por ejemplo:
       "¡Hola, [nombre_usuario]! Bienvenido/a."
    c. Solicita al usuario que ingrese su nombre usando `input()`.
    d. Llama a la función `saludar_usuario()` pasándole el nombre ingresado.

3.  Define una función llamada `sumar_tres_numeros(num1, num2, num3)`:
    a. Esta función debe recibir tres parámetros numéricos.
    b. Dentro de la función, calcula la suma de los tres números.
    c. Imprime el resultado de la suma desde dentro de la función.
    d. Incluye un docstring explicando brevemente qué hace la función.
    e. Llama a esta función con tres números de ejemplo (ej: 5, 10, 2).
-------------------------------------------------------------------------------
"""

# 1. Función de saludo simple
def mostrar_saludo_simple():
    """Imprime un saludo genérico."""
    print("¡Hola, mundo desde una función!")

print("--- Llamando a mostrar_saludo_simple ---")
mostrar_saludo_simple() # Llamada a la función
print("------------------------------------")

# 2. Función de saludo con parámetro
def saludar_usuario(nombre_usuario):
    """Imprime un saludo personalizado usando el nombre proporcionado."""
    print(f"¡Hola, {nombre_usuario}! Bienvenido/a.")

print("\n--- Llamando a saludar_usuario ---")
nombre_ingresado = input("Por favor, ingresa tu nombre: ")
saludar_usuario(nombre_ingresado) # Llamada con el argumento del input
saludar_usuario("Ana") # Otra llamada con un argumento directo
print("------------------------------------")

# 3. Función para sumar tres números
def sumar_tres_numeros(num1, num2, num3):
    """
    Calcula la suma de tres números y muestra el resultado.

    Args:
        num1 (int or float): El primer número.
        num2 (int or float): El segundo número.
        num3 (int or float): El tercer número.
    """
    suma = num1 + num2 + num3
    print(f"La suma de {num1} + {num2} + {num3} es: {suma}")

print("\n--- Llamando a sumar_tres_numeros ---")
sumar_tres_numeros(5, 10, 2)
sumar_tres_numeros(100, -50, 25.5)
print("------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la palabra clave utilizada en Python para definir una función?
2.  ¿Qué es un "parámetro" de una función? ¿Qué es un "argumento"?
    Usa el ejemplo de `saludar_usuario` para explicar.
3.  ¿Qué es un "docstring"? ¿Para qué sirve y cómo se define en una función?
4.  Si una función se define pero nunca se "llama", ¿se ejecutará el código
    dentro de ella? ¿Por qué?
-------------------------------------------------------------------------------
"""