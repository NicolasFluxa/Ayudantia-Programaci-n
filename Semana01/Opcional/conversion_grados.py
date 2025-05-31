"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                  Conversión de Grados Celsius a Fahrenheit
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
1. Solicita al usuario que ingrese una temperatura en grados Celsius.
   Asegúrate de convertir este valor a un número decimal.
2. Aplica la fórmula de conversión: Fahrenheit = (Celsius * 9/5) + 32
3. Muestra el resultado de la temperatura en Celsius y su equivalente en Fahrenheit,
   ambos formateados a 1 decimal.
-------------------------------------------------------------------------------
"""

# Título del programa
print("Conversor de Grados Celsius a Fahrenheit")
print("----------------------------------------")

# 1. Solicitar temperatura en Celsius
celsius_str = input("Ingresa la temperatura en grados Celsius (ej: 25.5): ")
grados_celsius = float(celsius_str) # Convertir a número decimal

# 2. Aplicar la fórmula de conversión
grados_fahrenheit = (grados_celsius * 9/5) + 32

# 3. Mostrar los resultados
print("----------------------------------------")
print(f"Temperatura ingresada: {grados_celsius:.1f}°C")
print(f"Equivalente en Fahrenheit: {grados_fahrenheit:.1f}°F")
print("----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Por qué se utiliza `9/5` en la fórmula en lugar de `1.8` directamente?
   ¿Habría alguna diferencia en el resultado si usaras `1.8`? (Considera la precisión).
2. Si quisieras realizar la conversión inversa (Fahrenheit a Celsius),
   ¿cómo sería la fórmula? (Fórmula: Celsius = (Fahrenheit - 32) * 5/9)
   ¿Podrías modificar este programa para que también haga esa conversión,
   quizás preguntando al usuario qué conversión desea hacer? (Esto último es un desafío).
3. ¿Qué son los "números mágicos" en programación y por qué podría ser una buena
   idea asignar `9/5` y `32` a variables con nombres descriptivos en este programa?
-------------------------------------------------------------------------------
"""