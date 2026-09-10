# Ejercicio 2: Verificador de numero par o impar
# es_par tiene return, regresa True o False
# mostrar_paridad no tiene return, solo usa es_par y muestra el mensaje

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def mostrar_paridad(numero):
    if es_par(numero):
        print(str(numero) + " es par")
    else:
        print(str(numero) + " es impar")


numero = int(input("Ingrese un numero: "))
mostrar_paridad(numero)
