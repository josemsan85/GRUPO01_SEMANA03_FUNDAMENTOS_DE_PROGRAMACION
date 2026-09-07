# Calculadora de descuento

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_final = calcular_descuento(precio, porcentaje)
ahorro = precio - precio_final

print("Precio final:", precio_final)
print("Ahorro obtenido:", ahorro)