"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                   Argumentos por Palabra Clave (Keyword Arguments)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio se enfoca en cómo llamar a funciones utilizando argumentos
por palabra clave, lo que puede hacer que las llamadas a funciones con muchos
parámetros sean más claras y flexibles.

1.  Define una función llamada `crear_perfil_usuario(nombre, email, edad, pais="Chile")`:
    a. `nombre`, `email`, `edad` son parámetros posicionales.
    b. `pais` es un parámetro con un valor por defecto.
    c. La función debe imprimir los detalles del perfil del usuario.

2.  Llama a la función `crear_perfil_usuario` de las siguientes maneras:
    a. Usando solo argumentos posicionales para `nombre`, `email` y `edad`.
    b. Usando argumentos por palabra clave para todos los parámetros,
       incluido `pais`, y en un orden diferente al de la definición
       (ej: `email` primero, luego `pais`, etc.).
    c. Usando una mezcla: los primeros dos argumentos (`nombre`, `email`)
       como posicionales y los siguientes (`edad`, `pais`) como argumentos
       por palabra clave.
    d. Intenta llamar a la función proporcionando un argumento por palabra clave
       antes de un argumento posicional (ej: `crear_perfil_usuario(nombre="Ana", "ana@mail.com", edad=30)`).
       Observa y explica el error.
-------------------------------------------------------------------------------
"""

# 1. Definir la función crear_perfil_usuario
def crear_perfil_usuario(nombre, email, edad, pais="Chile"):
    """Crea e imprime un perfil de usuario con los datos proporcionados."""
    print("\n--- Perfil de Usuario ---")
    print(f"Nombre: {nombre}")
    print(f"Email : {email}")
    print(f"Edad  : {edad} años")
    print(f"País  : {pais}")
    print("-------------------------")

print("--- Llamadas a crear_perfil_usuario ---")

# 2a. Usando solo argumentos posicionales
print("\nLlamada 1 (argumentos posicionales):")
crear_perfil_usuario("Juan Pérez", "juan.perez@example.com", 28)

# 2b. Usando argumentos por palabra clave para todos, en orden diferente
print("\nLlamada 2 (argumentos por palabra clave, orden alterado):")
crear_perfil_usuario(
    email="sofia.gomez@example.com",
    pais="México",
    edad=32,
    nombre="Sofía Gómez"
)

# 2c. Mezcla de argumentos posicionales y por palabra clave
# Los argumentos posicionales deben ir ANTES que los de palabra clave.
print("\nLlamada 3 (mezcla de posicionales y por palabra clave):")
crear_perfil_usuario("Carlos Ruiz", "c.ruiz@example.net", edad=45, pais="Argentina")

# 2d. Intento de llamar con palabra clave antes de posicional (esto dará error)
print("\nLlamada 4 (intento de palabra clave antes de posicional):")
try:
    # La siguiente línea está comentada porque produce un error de sintaxis.
    # Descoméntala para ver el error directamente en la ejecución.
    # crear_perfil_usuario(nombre="Ana", "ana@mail.com", edad=30)
    print("Error: Los argumentos posicionales deben preceder a los argumentos por palabra clave.")
    print("Ejemplo de llamada INCORRECTA (no se ejecutará):")
    print("# crear_perfil_usuario(nombre=\"Ana\", \"ana@mail.com\", edad=30)")
except SyntaxError as e:
    # En la práctica, Python detecta esto como un SyntaxError antes de la ejecución.
    # El bloque try-except aquí es más para ilustrar el punto en el texto.
    print(f"Se produciría un SyntaxError: {e}")

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la principal ventaja de utilizar argumentos por palabra clave al
    llamar a una función, especialmente si tiene muchos parámetros?
2.  ¿Es obligatorio que los argumentos por palabra clave sigan el mismo orden
    que los parámetros en la definición de la función?
3.  ¿Cuál es la regla respecto al orden de los argumentos posicionales y los
    argumentos por palabra clave en una llamada a función?
4.  Si una función tiene un parámetro con valor por defecto (ej: `pais="Chile"`),
    ¿puedes aun así pasarle un valor usando un argumento por palabra clave
    (ej: `pais="Perú"`)?
-------------------------------------------------------------------------------
"""