"""
Clase de Libros:
Crea una clase llamada Libro con los siguientes atributos:
titulo
autor
genero
Implementa un método detalles que muestre la información completa del libro.
Crea varios objetos de la clase Libro y muestra sus detalles.
"""


class Libro:
    def __init__(self, titulo, autor, genero):
        """
        Constructor de la clase Libro.
        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param genero: Género del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def detalles(self):
        """
        Muestra la información completa del libro.
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")

# Ejemplo de uso:
libro1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", genero="Realismo mágico")
libro2 = Libro(titulo="1984", autor="George Orwell", genero="Distopía")

print("Detalles del primer libro:")
libro1.detalles()

print("\nDetalles del segundo libro:")
libro2.detalles()
