# Ejercicio 1: Calculadora de Descuento
# El programa pide el precio de un producto y el porcentaje de descuento,
# calcula el precio final con la funcion y muestra cuanto se ahorro

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_final = calcular_descuento(precio, porcentaje)
ahorro = precio - precio_final

print("Precio final: " + str(precio_final))
print("Usted se ahorro: " + str(ahorro))
