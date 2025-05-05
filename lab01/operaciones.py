import random

def concatenacion(L1, L2):
    resultado = [""]
    for cadena1 in L1:
        for cadena2 in L2:
            if cadena1 not in resultado:
                resultado.append(cadena1 + cadena2)
    return resultado

def clausula_kleene(lenguaje):
    resultado = [""]
    while len(resultado) < 4:
        palabra = ""
        repeticiones = random.randint(1, 3)  
        for _ in range(repeticiones):
            palabra += random.choice(lenguaje)
        if palabra not in resultado: 
            resultado.append(palabra)
    resultado.remove("")
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
    
