# Pirámide invertida centrada
altura = 5

for i in range(altura, 0, -1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas + espacios)
