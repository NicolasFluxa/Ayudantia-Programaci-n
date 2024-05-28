"""Escribir una función que reciba una muestra de números en
una lista y devuelva otra lista con sus cuadrados."""


def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """

    lista = []
    for i in sample:
        lista.append(i**2)
    return lista


print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))