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

for palabra in cadenas:
    if contXY(palabra):
        print("La cadena " + palabra + " es VÁLIDA.")
    else:
        print("La cadena " + palabra + " es INVÁLIDA.")