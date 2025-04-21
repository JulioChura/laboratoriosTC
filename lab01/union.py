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