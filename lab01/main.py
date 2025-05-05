from operaciones import union, concatenacion, clausula_kleene, printArray
from reglas import validarLenguaje

alfabeto = ["x", "y", "z", "w"]

lenguajeA = ["xy", "yxy", "yxz"]
lenguajeB = ["ywx", "yzx", "yx"]

# probar las funciones
print("Concatenacion A.B = ", end="")
printArray(concatenacion(lenguajeA, lenguajeB))

print("Union A U B= ", end="")
printArray(union(lenguajeB, lenguajeA))

print("Kleene B*= ", end="")
printArray(clausula_kleene(lenguajeB))

# probar las reglas
print("Probando las reglas de validación")
validarLenguaje(lenguajeA)
validarLenguaje(lenguajeB)


