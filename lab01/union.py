def union(len1, len2):
    resultado = []
    for cadena1 in len1:
        resultado.append(cadena1)
    for cadena2 in len2:
        resultado.append(cadena2)
    return resultado

def printArray(arr):
    print("{ " + ", ".join(arr) + " }")