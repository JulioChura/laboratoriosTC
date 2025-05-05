def mayorTresSinW(cadena):
    if len(cadena) >= 3:
        if 'w' in cadena:
            #print('La cadena', cadena, 'no es válida porque contiene la letra "w"')
            return False
        else:
            return True
    else:
        return True

alfabeto = ["x", "y", "z", "w"]
cadenas = ["xyy", "wxy", "zxy", "zzx", "wwz"]

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
    
# tiene las 2 validaciones
def validarLenguaje(array):
    for palabra in cadenas:
        if contXY(palabra) and mayorTresSinW(palabra):
            print("La cadena " + palabra + " es VÁLIDA.")
        else:
            print("La cadena " + palabra + " es INVÁLIDA.")