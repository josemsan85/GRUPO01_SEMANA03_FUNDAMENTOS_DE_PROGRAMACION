#Calculadora de Promedio con Lista
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minima = min(notas)
    maxima = max(notas)
    return promedio, minima, maxima
def mostrar_resultado(nombre, notas):
    promedio, minima, maxima =calcular_promedio(notas)
    print(f"El promedio del estudiante {nombre} fue: {promedio:.2f} ")
    print(f"La menor nota obtenida fue: {minima}")
    print(f"La mayor nota obtenida fue: {maxima}")
nombre = input("Escriba el nombre del estudiante: ")
cantidad = int(input("Introduzca la cantidad de notas a ingresar: "))
notas = []
for i in range(cantidad):
    nota = float(input("Introduzca la nota: "))
    notas.append(nota)
mostrar_resultado(nombre,notas)