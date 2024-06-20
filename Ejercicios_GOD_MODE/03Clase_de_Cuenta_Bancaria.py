"""
Clase de Cuenta Bancaria:
Crea una clase llamada CuentaBancaria con los siguientes atributos:
titular
saldo
Implementa métodos para depositar y retirar dinero de la cuenta.
Asegúrate de manejar casos en los que el saldo no sea suficiente para un retiro.
"""


class CuentaBancaria:
    def __init__(self, titular, saldo):
        """
        Constructor de la clase CuentaBancaria.
        :param titular: Nombre del titular de la cuenta.
        :param saldo: Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.
        :param cantidad: Cantidad a depositar.
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad debe ser mayor que 0.")

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.
        :param cantidad: Cantidad a retirar.
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")


# Ejemplo de uso:
cuenta1 = CuentaBancaria(titular="Juan Pérez", saldo=1000)
print(f"Titular de la cuenta: {cuenta1.titular}")
print(f"Saldo inicial: ${cuenta1.saldo}")

cuenta1.depositar(cantidad=500)
cuenta1.retirar(cantidad=200)
