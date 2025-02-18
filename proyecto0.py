import re  # Importa la librería para trabajar con expresiones regulares.

# Función para leer un archivo y devolver su contenido en una lista de líneas.
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # Lee todas las líneas, elimina espacios en blanco y descarta líneas vacías.
        lineas = [line.strip() for line in archivo.readlines() if line.strip()]
    return lineas

# Conjunto de palabras reservadas del lenguaje, que no pueden ser utilizadas como nombres de variables o procedimientos.
PALABRAS_RESERVADAS = {
    "proc", "if", "else", "while", "for", "move", "jump", "put", "pick",
    "turn", "face", "not", "then", "do", "ofType", "inDir"
}

# Diccionario que almacena las expresiones regulares para verificar la sintaxis de cada comando.
REGEX_COMANDOS = {
    "variables": r"\|[a-zA-Z0-9_, ]+\|",  # Variables declaradas dentro de | ... |
    "procedimiento": r"proc [a-zA-Z_][a-zA-Z0-9_]* \[",  # Definición de procedimientos.
    "cierre_procedimiento": r"\]",  # Cierre de procedimientos con "]".
    "move": r"move: \d+ \.",  # Comando de movimiento (ej: move: 3 .)
    "jump": r"jump: \d+ \.",  # Comando de salto (ej: jump: 2 .)
    "put": r"put: \d+ ofType: #(balloons|chips) \.",  # Colocar un objeto (balloons o chips).
    "pick": r"pick: \d+ ofType: #(balloons|chips) \.",  # Recoger un objeto (balloons o chips).
    "turn": r"turn: #(left|right|around) \.",  # Girar en una dirección específica.
    "face": r"face: #(north|south|west|east) \.",  # Orientarse hacia una dirección específica.
    "if": r"if: .+ then: \[.+\]( else: \[.+\])?",  # Sentencia condicional if-then-else.
    "while": r"while: .+ do: \[.+\]",  # Bucle while con su condición y bloque de código.
}

# Función que verifica la sintaxis de una línea de código.
def verificar_sintaxis(linea):
    # Divide la línea en palabras separadas por espacios.
    tokens = re.split(r'\s+', linea)  

    # Verifica que todas las palabras reservadas estén en minúsculas.
    for token in tokens:
        if token in PALABRAS_RESERVADAS and token != token.lower():
            print(f"Error: '{token}' debe estar en minúsculas.")  # Mensaje de error si una palabra reservada está en mayúsculas.
            return False 

    # Compara la línea completa con cada patrón en REGEX_COMANDOS.
    for comando, patron in REGEX_COMANDOS.items():
        if re.fullmatch(patron, linea):  # Si la línea coincide con algún comando válido, retorna True.
            return True

    return False  # Si la línea no coincide con ningún patrón, retorna False.

# Función que analiza un archivo de código línea por línea.
def analizar_codigo(nombre_archivo):
    lineas = leer_archivo(nombre_archivo)  # Lee el archivo y obtiene las líneas.
    errores = []  # Lista para almacenar los errores encontrados.

    # Recorre cada línea del archivo y verifica su sintaxis.
    for i, linea in enumerate(lineas):
        if not verificar_sintaxis(linea):  # Si la sintaxis es incorrecta, agrega un mensaje de error.
            errores.append(f"Error en línea {i+1}: {linea}")

    # Si hay errores, los imprime en la consola.
    if errores:
        for error in errores:
            print(error)
        print("Análisis completado con errores.")
    else:
        print("El lenguaje es correcto.")  # Si no hay errores, confirma que el código es válido.

import sys  # Importa la librería para manejar argumentos desde la línea de comandos.


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analizador.py <archivo_de_codigo>")
    else:
        analizar_codigo(sys.argv[1])

