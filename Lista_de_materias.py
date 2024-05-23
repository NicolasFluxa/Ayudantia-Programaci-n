"""Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en
una lista y la muestre por pantalla, ademas, debes permitir subir N datos y preguntar
 hasta que el usuario escriba salir"""


escape = False
lista = []
print('Hola bienvenido a la base de datos de materias')
while not escape:
    materia = input('¿Qué matertia te gustaria agregar?\n')
    if materia.lower() == 'salir':
        escape = True
    else:
        lista.append(materia)

print(lista)
