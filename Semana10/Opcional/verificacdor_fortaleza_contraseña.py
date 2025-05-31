"""
-------------------------------------------------------------------------------
                        PROYECTO OPCIONAL 01
                  Verificador de Fortaleza de Contraseña
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea una función que analice una contraseña ingresada por el usuario y
determine su fortaleza basada en algunos criterios simples:
- Longitud.
- Presencia de letras mayúsculas.
- Presencia de letras minúsculas.
- Presencia de números.
- Presencia de símbolos especiales.

La función debe retornar un mensaje indicando la fortaleza (ej: "Débil",
"Media", "Fuerte", "Muy Fuerte") y quizás algunas sugerencias.
-------------------------------------------------------------------------------
"""


def verificar_fortaleza_contrasena(contrasena):
    """
    Analiza una contraseña y devuelve un mensaje sobre su fortaleza.

    Args:
        contrasena (str): La contraseña a analizar.

    Returns:
        str: Un mensaje describiendo la fortaleza de la contraseña.
    """
    longitud = len(contrasena)
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    tiene_simbolos = False

    # Criterios y puntaje
    puntaje = 0
    sugerencias = []

    # 1. Verificar longitud
    if longitud >= 12:
        puntaje += 2
    elif longitud >= 8:
        puntaje += 1
    else:
        sugerencias.append("Hacerla más larga (mínimo 8 caracteres, idealmente 12+).")

    # Caracteres para símbolos (puedes expandir esta lista)
    simbolos_especiales = "!@#$%^&*()-_=+[]{};:,.<>/?"

    # 2-5. Verificar tipos de caracteres
    for caracter in contrasena:
        if 'a' <= caracter <= 'z':
            tiene_minusculas = True
        elif 'A' <= caracter <= 'Z':
            tiene_mayusculas = True
        elif '0' <= caracter <= '9':
            tiene_numeros = True
        elif caracter in simbolos_especiales:
            tiene_simbolos = True

    if tiene_minusculas:
        puntaje += 1
    else:
        sugerencias.append("Incluir letras minúsculas.")

    if tiene_mayusculas:
        puntaje += 1
    else:
        sugerencias.append("Incluir letras mayúsculas.")

    if tiene_numeros:
        puntaje += 1
    else:
        sugerencias.append("Incluir números.")

    if tiene_simbolos:
        puntaje += 2  # Los símbolos suelen añadir más fortaleza
    else:
        sugerencias.append("Incluir símbolos (ej: !@#$%).")

    # Determinar fortaleza basada en el puntaje
    # Puntaje máximo posible aquí: 2(long) + 1(min) + 1(may) + 1(num) + 2(sim) = 7
    fortaleza_mensaje = ""
    if puntaje >= 6:  # Requiere buena longitud y varios tipos de caracteres
        fortaleza_mensaje = "¡Muy Fuerte! 👍"
    elif puntaje >= 4:
        fortaleza_mensaje = "Fuerte. 🙂"
    elif puntaje >= 2:
        fortaleza_mensaje = "Media. 🤔"
    else:
        fortaleza_mensaje = "Débil.  보안"  # 보안 (boan) significa seguridad en coreano, un guiño a la debilidad.

    resultado_final = f"Fortaleza de la contraseña: {fortaleza_mensaje}"
    if sugerencias:
        resultado_final += "\nSugerencias para mejorar:\n"
        for sug in sugerencias:
            resultado_final += f"  - {sug}\n"

    return resultado_final.strip()


# --- Programa Principal para Probar ---
if __name__ == "__main__":
    print("--- Verificador de Fortaleza de Contraseña ---")

    contrasenas_prueba = [
        "clave123",  # Débil/Media
        "ClaveSegura",  # Media/Fuerte
        "ClaveSuperSegura123!",  # Muy Fuerte
        "abc",  # Débil
        "ABCDEFGHIJKL",  # Media (solo mayúsculas, pero larga)
        "1234567890",  # Media (solo números, pero larga)
        "aB1!cD2@",  # Fuerte
        "MiClaveSuperLargaConNumeros12345YSimbolos!@#$"  # Muy Fuerte
    ]

    for pwd in contrasenas_prueba:
        print(f"\nAnalizando contraseña: '{pwd}'")
        mensaje_fortaleza = verificar_fortaleza_contrasena(pwd)
        print(mensaje_fortaleza)
        print("--------------------")

    print("\nPrueba con una contraseña ingresada por el usuario:")
    contrasena_usuario = input("Ingresa una contraseña para verificar su fortaleza: ")
    mensaje_usuario = verificar_fortaleza_contrasena(contrasena_usuario)
    print(mensaje_usuario)

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Lógica de Puntuación:** ¿Cómo funciona el sistema de "puntaje" para determinar
    la fortaleza? ¿Consideras que los pesos asignados a cada criterio (longitud,
    tipos de caracteres) son adecuados? ¿Cómo los cambiarías?
2.  **Iteración y Verificación de Caracteres:** Explica cómo el bucle `for caracter in contrasena:`
    y las condiciones `if` internas logran identificar la presencia de minúsculas,
    mayúsculas, números y símbolos.
3.  **Manejo de Strings:** ¿Qué métodos de string se utilizan o podrían ser útiles
    aquí (ej: `islower()`, `isupper()`, `isdigit()`) en lugar de las comparaciones
    de rango como `'a' <= caracter <= 'z'`? ¿Cuáles serían las ventajas o desventajas?
4.  **Modularidad:** La lógica principal está dentro de una función. ¿Qué ventajas
    ofrece esto si quisieras usar este verificador en otro programa más grande?
5.  **Sugerencias:** ¿Cómo se generan y presentan las sugerencias al usuario?
    ¿Podrías pensar en otros criterios o sugerencias para añadir (ej: evitar
    palabras comunes, secuencias, etc.)? Esto último sería más avanzado.
-------------------------------------------------------------------------------
"""