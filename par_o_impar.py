#Verificados de Número Par o Impar
def es_par(numero):
    es_par = numero % 2 ==0
    return es_par
def mostrar_paridad(numero):
    resultado = es_par(numero) 
    if resultado:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
numero = int(input("Escriba el numero : "))
mostrar_paridad(numero)