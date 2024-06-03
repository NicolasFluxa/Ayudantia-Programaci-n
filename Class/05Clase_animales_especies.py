"""
Clase de Animal y Especies Específicas:
Crea una clase Animal con atributos nombre y sonido.
Implementa un método emitir_sonido() que imprima el sonido del animal.
Crea subclases específicas como Perro y Gato que hereden de Animal.
Estas subclases deben tener un atributo adicional raza y un método mostrar_raza().
Crea instancias de Perro y Gato, muestra su información y haz que emitan su sonido.
"""


# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre  # Atributo para el nombre del animal
        self.sonido = sonido  # Atributo para el sonido que hace el animal

    def emitir_sonido(self):
        # Imprime el sonido del animal
        print(f"{self.nombre} dice: {self.sonido}")


# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)  # Llama al constructor de la clase padre (Animal)
        self.raza = raza  # Atributo para la raza del perro

    def mostrar_raza(self):
        # Imprime la raza del perro
        print(f"La raza del perro es: {self.raza}")


# Definición de la subclase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)  # Llama al constructor de la clase padre (Animal)
        self.raza = raza  # Atributo para la raza del gato

    def mostrar_raza(self):
        # Imprime la raza del gato
        print(f"La raza del gato es: {self.raza}")


# Crear instancias de Perro y Gato
un_perro = Perro(nombre="Firulais", sonido="guau guau", raza="Labrador")
un_gato = Gato(nombre="Misu", sonido="miau miau", raza="Siames")

# Llamar a los métodos para mostrar información
un_perro.emitir_sonido()
un_perro.mostrar_raza()

un_gato.emitir_sonido()
un_gato.mostrar_raza()
