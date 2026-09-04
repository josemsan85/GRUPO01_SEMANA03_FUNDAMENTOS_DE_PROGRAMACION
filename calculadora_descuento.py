#Calculadora de descuento
def calcular_descuento(precio,porcentaje):
    descuento = precio * (porcentaje/100)
    precio_final = precio - descuento 
    return precio_final
precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input(" Ingrese el porcentaje de descuento establecido: "))
precio_final = calcular_descuento(precio,porcentaje)
ahorro = precio - precio_final
print(f"El precio final es: S/{precio_final:.2f}")
print(f"Usted ha ahorrado: S/{ahorro:.2f}")
