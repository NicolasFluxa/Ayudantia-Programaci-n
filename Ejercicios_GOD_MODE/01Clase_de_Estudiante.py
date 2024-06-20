"""
Clase de Estudiantes:
Crea una clase llamada Estudiante con los siguientes atributos:
nombre
edad
calificaciones (una lista de calificaciones)
Implementa un método promedio_calificaciones que calcule y devuelva el promedio de las calificaciones del estudiante.
Crea varios objetos de la clase Estudiante y realiza pruebas con diferentes calificaciones.
"""


class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        """
        Constructor de la clase Estudiante.
        :param nombre: Nombre del estudiante.
        :param edad: Edad del estudiante.
        :param calificaciones: Lista de calificaciones del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def promedio_calificaciones(self):
        """
        Calcula y devuelve el promedio de las calificaciones del estudiante.
        :return: Promedio de calificaciones.
        """
        if len(self.calificaciones) == 0:
            return 0  # Si no hay calificaciones, el promedio es 0.
        total_calificaciones = sum(self.calificaciones)
        promedio = total_calificaciones / len(self.calificaciones)
        return promedio


# Ejemplo de uso:
estudiante1 = Estudiante(nombre="Ana", edad=20, calificaciones=[8, 9, 7, 10, 8])
print(f"Estudiante: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad} años")
print(f"Calificaciones: {estudiante1.calificaciones}")
print(f"Promedio de calificaciones: {estudiante1.promedio_calificaciones()}")
