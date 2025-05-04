from union import union
from concatenacion import concatenacion, printArray
from kleene import clausula_kleene


alfabeto = ["x", "y", "z", "w"]

lenguajeA = ["xy", "yxy", "yxz"]
lenguajeB = ["ywx", "yzx", "yx"]

# probar las funciones
print("Concatenacion= ", end="")
printArray(concatenacion(lenguajeA, lenguajeB))

print("Union= ", end="")
printArray(union(lenguajeB, lenguajeA))

print("Kleene= ", end="")
printArray(clausula_kleene(lenguajeB))
