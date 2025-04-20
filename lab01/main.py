from union import union
from concatenacion import concatenacion, printArray
from kleene import clausula_kleene


alfabeto = ["a", "b", "c", "d", "e"]

lenguajeA = ["ab", "bc", "ce", "ea", "bd"]
lenguajeB = ["ad", "cb", "da", "eb", "dc"]
lenguajeC = ["ac", "be", "de", "cd", "ba"]


# probar las funciones
print("Concatenacion= ", end="")
printArray(concatenacion(lenguajeA, lenguajeB))

print("Union= ", end="")
printArray(union(lenguajeA, lenguajeB))
