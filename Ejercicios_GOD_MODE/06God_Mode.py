"""
Ejercicio de Programación Orientada a Objetos (POO): Representación de una Casa

En este ejercicio, vamos a crear una representación básica de una casa utilizando clases en Python. La idea es modelar diferentes habitaciones de la casa y los muebles que se encuentran en cada una de ellas.

Clase Base: Habitacion
Crea una clase base llamada Habitacion con los siguientes atributos:
nombre (por ejemplo, “Dormitorio”, “Cocina”, “Sala de estar”, etc.).
muebles (una lista de muebles en la habitación).
Implementa un método mostrar_muebles que muestre los muebles presentes en la habitación.
Clases Hija: Dormitorio, Cocina, SalaDeEstar, etc.
Crea clases específicas para diferentes habitaciones (por ejemplo, Dormitorio, Cocina, etc.).
Agrega atributos adicionales específicos para cada habitación (por ejemplo, cama, mesa, sofá, etc.).
Implementa métodos específicos para cada habitación según sea necesario.
Instrucciones:

Define las clases según la jerarquía propuesta.
Crea objetos para representar una casa con al menos tres habitaciones (dormitorio, cocina, sala de estar).
Agrega algunos muebles a cada habitación.
Muestra todos los muebles presentes en la casa.

"""


class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.muebles = []

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)

    def mostrar_muebles(self):
        print(f"Muebles en la habitación {self.nombre}:")
        for mueble in self.muebles:
            print(f"  - {mueble}")

class Casa:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_todos_los_muebles(self):
        print("Muebles en toda la casa:")
        for habitacion in self.habitaciones:
            habitacion.mostrar_muebles()

# Crear una casa
mi_casa = Casa()

# Agregar habitaciones
dormitorio_principal = Habitacion(nombre="Dormitorio principal")
mi_casa.agregar_habitacion(dormitorio_principal)

cocina_principal = Habitacion(nombre="Cocina")
mi_casa.agregar_habitacion(cocina_principal)

sala_principal = Habitacion(nombre="Sala de estar")
mi_casa.agregar_habitacion(sala_principal)

# Agregar muebles a las habitaciones
dormitorio_principal.agregar_mueble("Cama")
dormitorio_principal.agregar_mueble("Armario")
dormitorio_principal.agregar_mueble("Mesita de noche")

cocina_principal.agregar_mueble("Mesa")
cocina_principal.agregar_mueble("Sillas")
cocina_principal.agregar_mueble("Fregadero")
cocina_principal.agregar_mueble("Estufa")

sala_principal.agregar_mueble("Sofá")
sala_principal.agregar_mueble("Televisor")
sala_principal.agregar_mueble("Mesa de centro")

# Mostrar todos los muebles de la casa
mi_casa.mostrar_todos_los_muebles()
