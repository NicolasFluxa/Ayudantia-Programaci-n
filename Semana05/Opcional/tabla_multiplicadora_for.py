"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                      Tabla de Multiplicar con `for`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla un programa que solicite al usuario un número entero y
luego muestre la tabla de multiplicar de ese número desde el 1 hasta el 10.

Formato de salida esperado para cada línea (ejemplo para el número 5, multiplicando por 3):
"5 x 3 = 15"
-------------------------------------------------------------------------------
"""

# Solicitar número al usuario
numero_str = input("Ingresa un número entero para ver su tabla de multiplicar: ")
numero = int(numero_str)

print(f"\n--- Tabla de Multiplicar del {numero} ---")

# Usamos un bucle for con range para iterar del 1 al 10
# range(1, 11) generará los números 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    # Imprimir la línea de la tabla con el formato especificado
    print(f"{numero} x {multiplicador} = {resultado}")

print("-----------------------------------")
print("¡Tabla generada!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En `range(1, 11)`, ¿por qué se usa `11` como segundo argumento si solo
    queremos multiplicar hasta el 10?
2.  ¿Cómo modificarías el programa para que muestre la tabla de multiplicar
    desde el 1 hasta el 12 en lugar del 10?
3.  (Desafío) ¿Podrías usar un bucle `for` anidado (un `for` dentro de otro `for`)
    para imprimir las tablas de multiplicar de todos los números del 1 al 5?
    Pista: el bucle exterior controlaría el número de la tabla (1 a 5) y el
    bucle interior el multiplicador (1 a 10).
-------------------------------------------------------------------------------
"""