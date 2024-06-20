"""
Clase de Conversión de Temperatura:
Crea una clase llamada Temperatura con los siguientes métodos:
celsius_a_fahrenheit: Convierte una temperatura en grados Celsius a Fahrenheit.
fahrenheit_a_celsius: Convierte una temperatura en grados Fahrenheit a Celsius.
Realiza pruebas con diferentes temperaturas.
"""


class Temperatura:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte una temperatura en grados Celsius a Fahrenheit.
        :param celsius: Temperatura en grados Celsius.
        :return: Temperatura en grados Fahrenheit.
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte una temperatura en grados Fahrenheit a Celsius.
        :param fahrenheit: Temperatura en grados Fahrenheit.
        :return: Temperatura en grados Celsius.
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius


# Ejemplo de uso:
temperatura_actual = Temperatura()

# Conversión de 25°C a Fahrenheit:
celsius = 25
fahrenheit_resultante = temperatura_actual.celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit_resultante:.2f}°F")

# Conversión de 80°F a Celsius:
fahrenheit = 80
celsius_resultante = temperatura_actual.fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit}°F equivale a {celsius_resultante:.2f}°C")
