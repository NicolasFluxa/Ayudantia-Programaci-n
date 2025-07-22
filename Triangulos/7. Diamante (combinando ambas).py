# Diamante completo
altura = 5

# Parte superior
for i in range(1, altura + 1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas + espacios)

# Parte inferior
for i in range(altura - 1, 0, -1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas + espacios)
