"""
1. Crea una clase 'Auto' con atributos para marca, modelo y año.
2. Añade un método para mostrar la información del auto.
3. Crea una clase 'AutoElectrico' que herede de 'Auto' y
añade un atributo para la autonomía de la batería.
"""


# Definición de la clase Auto
class Auto:
    # Método constructor con atributos marca, modelo y año
    def __init__(self, marca, modelo, anio):
        self.marca = marca  # Atributo para la marca del auto
        self.modelo = modelo  # Atributo para el modelo del auto
        self.anio = anio  # Atributo para el año del auto

    # Método para mostrar la información del auto
    def mostrar_informacion(self):
        # Imprime la información del auto
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")


# Definición de la clase AutoElectrico que hereda de Auto
class AutoElectrico(Auto):
    # Método constructor con un atributo adicional para la autonomía de la batería
    def __init__(self, marca, modelo, anio, autonomia_bateria):
        super().__init__(marca, modelo, anio)  # Llama al constructor de la clase padre (Auto)
        self.autonomia_bateria = autonomia_bateria  # Atributo para la autonomía de la batería

    # Método para mostrar la información del auto eléctrico
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llama al método mostrar_informacion() de la clase padre (Auto)
        # Imprime la autonomía de la batería del auto eléctrico
        print(f"Autonomía de la batería: {self.autonomia_bateria} km")


# Crear una instancia de la clase AutoElectrico
un_auto_electrico = AutoElectrico(marca="Tesla", modelo="Model S", anio=2022, autonomia_bateria=400)
# Llama al método mostrar_informacion() para imprimir los detalles del auto eléctrico
un_auto_electrico.mostrar_informacion()

