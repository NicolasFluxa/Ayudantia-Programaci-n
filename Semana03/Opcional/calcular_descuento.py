
"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                        Calculadora de Descuentos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Una tienda ofrece descuentos en sus productos basados en el monto total de la compra:
- Si el monto es mayor o igual a $50.000, se aplica un 15% de descuento.
- Si el monto es mayor o igual a $25.000 pero menor a $50.000, se aplica un 10% de descuento.
- Si el monto es mayor o igual a $10.000 pero menor a $25.000, se aplica un 5% de descuento.
- Si el monto es menor a $10.000, no hay descuento.

Escribe un programa que:
1. Solicite al usuario el monto total de la compra.
2. Calcule el descuento aplicable según las reglas anteriores.
3. Calcule el precio final a pagar (monto original - descuento).
4. Muestre el monto original, el porcentaje de descuento aplicado,
   el monto del descuento y el precio final a pagar.
-------------------------------------------------------------------------------
"""

# 1. Solicitar el monto total de la compra
monto_original_str = input("Ingrese el monto total de la compra: $")
monto_original = float(monto_original_str) # Convertir a flotante

# Variables para el descuento
porcentaje_descuento = 0.0
monto_descuento = 0.0

# 2. Calcular el descuento aplicable
if monto_original >= 50000:
    porcentaje_descuento = 0.15 # 15%
    print("¡Felicidades! Aplica para un 15% de descuento.")
elif monto_original >= 25000:
    porcentaje_descuento = 0.10 # 10%
    print("¡Bien! Aplica para un 10% de descuento.")
elif monto_original >= 10000:
    porcentaje_descuento = 0.05 # 5%
    print("¡Casi! Aplica para un 5% de descuento.")
else:
    porcentaje_descuento = 0.0 # 0%
    print("No aplica descuento para este monto.")

# Calcular el monto del descuento
monto_descuento = monto_original * porcentaje_descuento

# 3. Calcular el precio final
precio_final = monto_original - monto_descuento

# 4. Mostrar los resultados
print("\n--- Resumen de la Compra ---")
print(f"Monto Original : $ {monto_original:.0f}")
if porcentaje_descuento > 0:
    # Mostramos el porcentaje como entero (ej: 15% en lugar de 0.15)
    print(f"Descuento Aplicado: {porcentaje_descuento*100:.0f}%")
    print(f"Monto Descuento: $ {monto_descuento:.0f}")
else:
    print("Descuento Aplicado: Ninguno")
print("----------------------------")
print(f"Precio Final     : $ {precio_final:.0f}")
print("----------------------------")
print("¡Gracias por su compra!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. El orden de las condiciones `if` y `elif` es importante. ¿Qué pasaría si
   primero evaluaras `monto_original >= 10000` antes que `monto_original >= 50000`?
   ¿Se aplicarían correctamente los descuentos para compras mayores a $50.000? Explica.
2. ¿Cómo modificarías el programa para añadir una nueva categoría de descuento,
   por ejemplo, un 20% para compras mayores o iguales a $100.000?
3. En la línea `print(f"Descuento Aplicado: {porcentaje_descuento*100:.0f}%")`,
   ¿por qué se multiplica `porcentaje_descuento` por 100 antes de mostrarlo?
-------------------------------------------------------------------------------
"""