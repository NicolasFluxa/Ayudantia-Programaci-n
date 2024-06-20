"""
Clase de Palíndromos:
Crea una clase llamada Palindromo con un atributo palabra.
Implementa un método es_palindromo que verifique si la palabra es un palíndromo
 (se lee igual de izquierda a derecha que de derecha a izquierda).
Prueba con diferentes palabras.
"""


class Palindromo:
    def __init__(self, palabra):
        """
        Constructor de la clase Palindromo.
        :param palabra: Palabra a verificar si es un palíndromo.
        """
        self.palabra = palabra.lower()
        # Convertimos la palabra a minúsculas para comparar sin distinción de mayúsculas.

    def es_palindromo(self):
        """
        Verifica si la palabra es un palíndromo.
        :return: True si es palíndromo, False si no lo es.
        """
        # Eliminamos los espacios en blanco y caracteres especiales.
        palabra_limpia = ''.join(c for c in self.palabra if c.isalnum())
        return palabra_limpia == palabra_limpia[::-1]  # Comparamos la palabra con su reverso.


# Ejemplo de uso:
palabra1 = "anilina"
palabra2 = "reconocer"
palabra3 = "python"

palindromo1 = Palindromo(palabra1)
palindromo2 = Palindromo(palabra2)
palindromo3 = Palindromo(palabra3)

print(f"¿'{palabra1}' es un palíndromo? {palindromo1.es_palindromo()}")
print(f"¿'{palabra2}' es un palíndromo? {palindromo2.es_palindromo()}")
print(f"¿'{palabra3}' es un palíndromo? {palindromo3.es_palindromo()}")
