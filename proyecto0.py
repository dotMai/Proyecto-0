import re

def leer_archivo(nombre_archivo):
    """Lee el archivo y devuelve una lista de líneas limpias (sin espacios extra ni saltos de línea)."""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = [line.strip() for line in archivo.readlines() if line.strip()]
    return lineas

PALABRAS_RESERVADAS = {"proc", "if", "while", "for", "move", "jump", "put", "pick", "turn", "face", "not"}

COMANDOS = {
    "variables": r"\|[a-zA-Z0-9_, ]+\|",
    "procedimiento": r"proc [a-zA-Z_][a-zA-Z0-9_]* \[",
    "cierre_procedimiento": r"\]",
    "move": r"move: \d+ .",
    "jump": r"jump: \d+ .",
    "put": r"put: \d+ ofType: #(balloons|chips) .",
    "pick": r"pick: \d+ ofType: #(balloons|chips) .",
    "turn": r"turn: #(left|right|around) .",
    "face": r"face: #(north|south|west|east) .",
    "if": r"if: .+ then: \[.+\]( else: \[.+\])?",
    "while": r"while: .+ do: \[.+\]",
}

def verificar_sintaxis(linea):
    for comando, patron in COMANDOS.items():
        if re.fullmatch(patron, linea):
            return True
    return False

def analizar_codigo(nombre_archivo):
    lineas = leer_archivo(nombre_archivo)
    errores = []
    for i, linea in enumerate(lineas):
        if not verificar_sintaxis(linea):
            errores.append(f"Error en línea {i+1}: {linea}")
    
    if errores:
        for error in errores:
            print(error)
        print("Análisis completado con errores.")
    else:
        print("El lenguaje es correcto.")

        
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analizador.py <archivo_de_codigo>")
    else:
        analizar_codigo(sys.argv[1])

