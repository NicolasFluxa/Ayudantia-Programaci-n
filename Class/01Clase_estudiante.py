"""
Clase de Estudiantes:
Crea una clase llamada Estudiante con los siguientes atributos:
1.-nombre
2.-edad
3.- curso
Implementa un método para mostrar la información del estudiante.
Crea una instancia de la clase y muestra los detalles del estudiante.
"""


# Definición de la clase Estudiante
class Estudiante:
    # Método constructor con parámetros para nombre, edad y curso
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre  # Atributo para el nombre del estudiante
        self.edad = edad  # Atributo para la edad del estudiante
        self.curso = curso  # Atributo para el curso del estudiante

    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        # Imprime la información del estudiante
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}")


# Crear una instancia de la clase Estudiante
un_estudiante = Estudiante(nombre="Ana", edad=18, curso="Matemáticas")
dos_estudiantes = Estudiante(nombre="camilo", edad=19, curso="Calculo I")
# Llama al método mostrar_informacion() para imprimir los detalles del estudiante
un_estudiante.mostrar_informacion()
dos_estudiantes.mostrar_informacion()
