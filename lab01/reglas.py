def mayorTresSinW(cadena):
    if len(cadena) >= 3:
        if "w" in cadena:
            # print('La cadena', cadena, 'no es válida porque contiene la letra "w"')
            return False
        else:
            return True
    else:
        return True


# alfabeto = ["x", "y", "z", "w"]
# cadenas = ["xyy", "wxy", "zxy", "zzx", "wwz"]

def contXY(cadena):
    verificaX = False
    verificaY = False
    for caracter in cadena:
        if caracter == "x":
            verificaX = True
        if caracter == "y":
            verificaY = True
    if verificaX and verificaY:
        return True
    else:
        return False

""" 
    funciones para poder mostrar en la consola los resultados
"""

# plantilla para poder mostrar cada validacion
def mostrar_validacion(lenguaje, funcion_validacion):
    for palabra in lenguaje:
        if funcion_validacion(palabra):
            print(f"La cadena '{palabra}' es VÁLIDA")
        else:
            print(f"La cadena '{palabra}' es INVÁLIDA")  

# mostrar la regla mayorTresSinW
def mostrarMayorTresSinW(lenguaje):
    mostrar_validacion(lenguaje, mayorTresSinW)

# mostrar la regla validarLenguaje
def mostrarContXY(lenguaje):
    mostrar_validacion(lenguaje, contXY)

# tiene las 2 validaciones
def validarLenguaje(lenguaje):
    for palabra in lenguaje:
        if contXY(palabra) and mayorTresSinW(palabra):
            print("La cadena " + palabra + " es VÁLIDA.")
        else:
            print("La cadena " + palabra + " es INVÁLIDA.")
