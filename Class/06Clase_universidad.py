"""
Supongamos que estamos desarrollando un sistema de registro de estudiantes para una universidad.
Cada estudiante tiene los siguientes atributos:

Nombre completo.
Edad.
Número de identificación estudiantil (ID).
Carrera (por ejemplo, Ingeniería Civil Informática).
El sistema debe permitir las siguientes operaciones:

Agregar un estudiante: El usuario debe ingresar los datos del estudiante (nombre, edad, ID y carrera) y agregarlo al registro.
Mostrar todos los estudiantes: Se debe mostrar una lista de todos los estudiantes registrados.
Buscar estudiante por ID: El usuario ingresa un ID y se muestra la información del estudiante correspondiente.
Eliminar estudiante por ID: El usuario ingresa un ID y se elimina al estudiante correspondiente del registro.
"""


class Estudiante:
    def __init__(self, nombre, edad, identificacion, carrera):
        # Inicialización de los atributos del estudiante
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.carrera = carrera


class RegistroEstudiantes:
    def __init__(self):
        # Inicialización de la lista de estudiantes vacía
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        # Agregar un estudiante a la lista
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        # Mostrar información de todos los estudiantes
        for estudiante in self.estudiantes:
            print(f"ID: {estudiante.identificacion} - Nombre: {estudiante.nombre}")

    def buscar_estudiante_por_id(self, identificacion):
        # Buscar un estudiante por ID
        for estudiante in self.estudiantes:
            if estudiante.identificacion == identificacion:
                return estudiante
        return None

    def eliminar_estudiante_por_id(self, identificacion):
        # Eliminar un estudiante por ID
        for estudiante in self.estudiantes:
            if estudiante.identificacion == identificacion:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante con ID {identificacion} eliminado.")
                return
        print(f"No se encontró ningún estudiante con ID {identificacion}.")


# Ejemplo de uso
registro = RegistroEstudiantes()

# Creación de estudiantes
estudiante1 = Estudiante("María González", 21, "2021001", "Ingeniería Civil Informática")
estudiante2 = Estudiante("Pedro Rodríguez", 22, "2021002", "Ingeniería Civil Informática")
estudiante3 = Estudiante("Ana López", 20, "2021003", "Ingeniería Civil Informática")
estudiante4 = Estudiante("Carlos Martínez", 23, "2021004", "Ingeniería Civil Informática")
estudiante5 = Estudiante("Laura Fernández", 19, "2021005", "Ingeniería Civil Informática")

# Agregar estudiantes al registro
registro.agregar_estudiante(estudiante1)
registro.agregar_estudiante(estudiante2)
registro.agregar_estudiante(estudiante3)
registro.agregar_estudiante(estudiante4)
registro.agregar_estudiante(estudiante5)

# Mostrar todos los estudiantes
print("Lista de estudiantes:")
registro.mostrar_estudiantes()

# Buscar estudiante por ID
id_buscado = "2021003"
estudiante_encontrado = registro.buscar_estudiante_por_id(id_buscado)
if estudiante_encontrado:
    print(f"Estudiante encontrado: {estudiante_encontrado.nombre, estudiante_encontrado.identificacion}")
else:
    print(f"No se encontró ningún estudiante con ID {id_buscado}.")

# Eliminar estudiante por ID
id_eliminar = "2021003"
registro.eliminar_estudiante_por_id(id_eliminar)

# Buscar estudiante por ID
id_buscado = "2021003"
estudiante_encontrado = registro.buscar_estudiante_por_id(id_buscado)
if estudiante_encontrado:
    print(f"Estudiante encontrado: {estudiante_encontrado.nombre, estudiante_encontrado.identificacion}")
else:
    print(f"No se encontró ningún estudiante con ID {id_buscado}.")

