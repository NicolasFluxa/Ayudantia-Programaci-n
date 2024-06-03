"""
Clase de Empleado y Gerente:
Crea una clase Empleado con atributos nombre, id y salario.
Implementa un método mostrar_info() que muestre la información del empleado.
Crea una subclase Gerente que herede de Empleado y añade un atributo departamento.
Implementa un método asignar_departamento() en Gerente para cambiar el valor del departamento.
Crea una instancia de Gerente y muestra su información, incluyendo el departamento.
"""


# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, id, salario):
        self.nombre = nombre  # Atributo para el nombre del empleado
        self.id = id  # Atributo para el ID del empleado
        self.salario = salario  # Atributo para el salario del empleado

    def mostrar_info(self):
        # Imprime la información del empleado
        print(f"Empleado ID: {self.id}, Nombre: {self.nombre}, Salario: {self.salario}")


# Definición de la subclase Gerente que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, id, salario, departamento):
        super().__init__(nombre, id, salario)  # Llama al constructor de la clase padre (Empleado)
        self.departamento = departamento  # Atributo para el departamento del gerente

    def asignar_departamento(self, nuevo_departamento):
        # Método para cambiar el valor del departamento
        self.departamento = nuevo_departamento

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método mostrar_info() de la clase padre (Empleado)
        # Imprime el departamento del gerente
        print(f"Departamento: {self.departamento}")


# Crear una instancia de la clase Gerente
un_gerente = Gerente(nombre="Carlos", id=102, salario=50000, departamento="Ventas")
# Llama al método mostrar_info() para imprimir los detalles del gerente
un_gerente.mostrar_info()
