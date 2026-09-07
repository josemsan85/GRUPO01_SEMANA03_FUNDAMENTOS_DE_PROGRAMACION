# Verificador de número par o impar

def es_par(numero):
    return numero % 2 == 0


def mostrar_paridad(numero):
    if es_par(numero):
        print("El número es par")
    else:
        print("El número es impar")


numero = int(input("Ingrese un número: "))

mostrar_paridad(numero)
