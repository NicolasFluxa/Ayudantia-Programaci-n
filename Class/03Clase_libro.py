"""
Clase de Libro:
Crea una clase llamada Libro con los atributos titulo, autor y año.
Implementa un método para mostrar la información completa del libro.
Crea una instancia de la clase y muestra los detalles del libro.
"""


# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo  # Atributo para el título del libro
        self.autor = autor  # Atributo para el autor del libro
        self.anio = anio  # Atributo para el año de publicación del libro

    def mostrar_informacion(self):
        # Imprime la información completa del libro
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")


# Crear una instancia de la clase Libro
un_libro = Libro(titulo="El Gran Gatsby", autor="F. Scott Fitzgerald", anio=1925)
# Llama al método mostrar_informacion() para imprimir los detalles del libro
un_libro.mostrar_informacion()
