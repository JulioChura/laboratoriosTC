def concatenacion(L1, L2):
    resultado = set()
    for cadena1 in L1:
        for cadena2 in L2:
            resultado.add(cadena1 + cadena2)
    return resultado

def printArray(arr):
    print("{ " + ", ".join(arr) + " }")
