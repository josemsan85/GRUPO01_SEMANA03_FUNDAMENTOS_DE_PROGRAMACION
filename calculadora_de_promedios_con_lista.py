# Calculadora de promedio con lista

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minimo = min(notas)
    maximo = max(notas)

    return promedio, minimo, maximo


def mostrar_resultado(nombre, notas):
    promedio, minimo, maximo = calcular_promedio(notas)

    print("Nombre:", nombre)
    print("Promedio:", promedio)
    print("Nota mínima:", minimo)
    print("Nota máxima:", maximo)


nombre = input("Ingrese el nombre del estudiante: ")

notas = []
cantidad = int(input("¿Cuántas notas va a ingresar? "))

for i in range(1, cantidad + 1):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

mostrar_resultado(nombre, notas)
