# Ejercicio 3: Calculadora de promedio con lista
# calcular_promedio tiene return, regresa el promedio, la nota minima y la maxima
# mostrar_resultado no tiene return, solo imprime el reporte usando la otra funcion

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minimo = min(notas)
    maximo = max(notas)
    return promedio, minimo, maximo


def mostrar_resultado(nombre, notas):
    promedio, minimo, maximo = calcular_promedio(notas)
    print("Reporte de " + nombre)
    print("Promedio: " + str(promedio))
    print("Nota minima: " + str(minimo))
    print("Nota maxima: " + str(maximo))


notas = [15, 18, 12, 20, 14]
mostrar_resultado("Juan", notas)
