def concatenacion(L1, L2):
    resultado = []
    for cadena1 in L1:
        for cadena2 in L2:
            if cadena1 not in resultado:
                resultado.append(cadena1 + cadena2)
    return resultado

def clausura_kleene(lenguaje, potencia = 2):
    cadenasActuales = [""] # Solo contiene cadenas de la última iteración
    resultado = [] # Acumula todas las cadenas generadas
    i = 0
    while i < potencia:
        cadenasNuevas = []
        for cadenaActual in cadenasActuales:
            for cadena in lenguaje:
                nuevaCadena = cadenaActual + cadena
                cadenasNuevas.append(nuevaCadena)
                if nuevaCadena not in resultado:
                    resultado.append(nuevaCadena)
        cadenasActuales = cadenasNuevas
        i += 1
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
    
