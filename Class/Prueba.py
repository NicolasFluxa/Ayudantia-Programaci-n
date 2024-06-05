"""
Clase de Animal y Especies Específicas:
Crea una clase Animal con atributos nombre y sonido.
Implementa un método emitir_sonido() que imprima el sonido del animal.
Crea subclases específicas como Perro y Gato que hereden de Animal.
Estas subclases deben tener un atributo adicional raza y un método mostrar_raza().
Crea instancias de Perro y Gato, muestra su información y haz que emitan su sonido.
"""


class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def emitir_sonido(self):
        print("El sonido de {} es: {}".format(self.nombre, self.sonido))


class Perro(Animal):
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza = raza

    def mostrar_raza(self):
        print("El razo de {} es: {}".format(self.nombre, self.raza))


class Gato(Animal):
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza = raza


    def mostrar_raza(self):
        print("El razo de {} es: {}".format(self.nombre, self.raza))



un_perro = Perro(nombre="Abi", sonido="guau guau", raza="Schaunser")
un_gato = Gato(nombre="lampara", sonido= "miau miau", raza="cat")

un_perro.mostrar_raza()
un_perro.emitir_sonido()

un_gato.mostrar_raza()
un_gato.emitir_sonido()