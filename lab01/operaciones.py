import random

def concatenacion(L1, L2):
    resultado = [""]
    for cadena1 in L1:
        for cadena2 in L2:
            if cadena1 not in resultado:
                resultado.append(cadena1 + cadena2)
    return resultado

def clausura_kleene(lenguaje):
    resultado = [""]
    combinaciones = [""]  #Cola de combinaciones 
    elementos = 6

    while len(resultado) < elementos:
        palabra = combinaciones.pop(0) #Se extrae y se elimina
        for simbolo in lenguaje:
            nueva = palabra + simbolo
            if nueva not in resultado:
                resultado.append(nueva)
                combinaciones.append(nueva)
                if len(resultado) == elementos:
                    break
    return resultado

def union(len1, len2):
    resultado = []
    for cadena in len1:
        if cadena not in resultado:
            resultado.append(cadena)
    for cadena in len2:
        if cadena not in resultado:
            resultado.append(cadena)
    return resultado

def printArray(arr):
    print("{ " + ", ".join(arr) + " }")
    
