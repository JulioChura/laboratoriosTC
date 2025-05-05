from operaciones import union, concatenacion, clausura_kleene, printArray
from reglas import  mostrarContXY, mostrarMayorTresSinW, validarLenguaje

alfabeto = ["x", "y", "z", "w"]

lenguajeA = ["yx", "yxy", "yxz"]
lenguajeB = ["ywx", "yzx", "yx"]

# probar las funciones
print("Concatenacion A.B = ", end="")
printArray(concatenacion(lenguajeA, lenguajeB))

print("Union A U B= ", end="")
printArray(union(lenguajeB, lenguajeA))

print("Kleene B*= ", end="")
printArray(clausura_kleene(lenguajeB, 2))

# probar las reglas
print("Probando las 2 reglas de validación")
validarLenguaje(lenguajeA)
validarLenguaje(lenguajeB)

# probar la regla de que las cadenas si son mayor o igual a 3 y contienen la w, no son válidas
print("Probando la regla: Las cadena mayor o igual a 3 y que contengan w, no son válidas")
mostrarMayorTresSinW(lenguajeA)

# probar la regla de que las cadenas deben tener tanto x como y
print("Probando la regla: Todas las cadenas que contengan tanto x como y")
mostrarContXY(lenguajeA)

