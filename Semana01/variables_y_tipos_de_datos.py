"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                       Variables y Tipos de Datos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un programa que declare variables para almacenar los siguientes datos:
1. Tu edad (como un número entero).
2. Tu estatura en metros (como un número decimal).
3. Tu comida favorita (como texto).
4. Si te gusta programar (como un valor booleano: verdadero o falso).

Luego, imprime cada una de estas variables con un mensaje descriptivo
y también imprime el tipo de dato de cada variable usando la función `type()`.
-------------------------------------------------------------------------------
"""

# Declaración de variables
mi_edad = 25  # Tipo entero (int)
mi_estatura = 1.75  # Tipo decimal (float)
mi_comida_favorita = "Pizza"  # Tipo texto (string)
me_gusta_programar = True  # Tipo booleano (bool)

# Imprimir las variables y sus tipos
print("--- Información Personal ---")

# Edad
print("Mi edad es:", mi_edad)
print("El tipo de dato de mi_edad es:", type(mi_edad))
print("--------------------------")

# Estatura
print("Mi estatura es:", mi_estatura, "metros.")
print("El tipo de dato de mi_estatura es:", type(mi_estatura))
print("--------------------------")

# Comida Favorita
print("Mi comida favorita es:", mi_comida_favorita)
print("El tipo de dato de mi_comida_favorita es:", type(mi_comida_favorita))
print("--------------------------")

# Gusto por la programación
print("¿Me gusta programar?:", me_gusta_programar)
print("El tipo de dato de me_gusta_programar es:", type(me_gusta_programar))
print("--------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuáles son los cuatro tipos de datos básicos que utilizaste en este ejercicio?
   Describe brevemente cada uno.
2. Si intentaras sumar la variable `mi_edad` con `mi_comida_favorita`,
   ¿qué crees que pasaría? Pruébalo y explica el resultado.
3. ¿Cómo se representa un valor Falso en un tipo de dato booleano en Python?
-------------------------------------------------------------------------------
"""