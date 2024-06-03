"""
Clase de Círculo:
Crea una clase llamada Circulo con un atributo radio.
Implementa métodos para calcular el área y la circunferencia del círculo.
Crea una instancia de la clase y muestra el área y la circunferencia.
"""

# Importamos el módulo math para tener acceso a funciones matemáticas
import math

# Definición de la clase Circulo
class Circulo:
    # Método constructor con un parámetro para el radio
    def __init__(self, radio):
        self.radio = radio  # Atributo para almacenar el radio del círculo

    # Método para calcular el área del círculo
    def calcular_area(self):
        # La fórmula para el área de un círculo es pi * radio^2
        return math.pi * self.radio ** 2

    # Método para calcular la circunferencia del círculo
    def calcular_circunferencia(self):
        # La fórmula para la circunferencia de un círculo es 2 * pi * radio
        return 2 * math.pi * self.radio


# Crear una instancia de la clase Circulo con un radio de 5
un_circulo = Circulo(radio=5)
# Imprimir el área del círculo, formateado a dos decimales
print(f"Área: {un_circulo.calcular_area():.2f}")
# Imprimir la circunferencia del círculo, formateado a dos decimales
print(f"Circunferencia: {un_circulo.calcular_circunferencia():.2f}")
