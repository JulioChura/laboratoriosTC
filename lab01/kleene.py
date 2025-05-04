import random

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

def printArray(arr):
    print("{ " + ", ".join(arr) + " }")
