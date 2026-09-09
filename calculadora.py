precio      = int (input ("Coloca el precio "))
porcentaje  = float (input ("coloca el porcentaje "))
#precioFinal; 

def calcularDescuento (preci, porcentaj):
 
 if porcentaj >= 0 and porcentaj <=100:
  
  precioFinal = preci - (porcentaj/100)*preci
  print ("el descuento es " + str ((porcentaj/100)*preci) )

  return precioFinal 

 else:

  print("coloca un valor valido")


a = calcularDescuento(precio, porcentaje)

print("el precio final es " + str(a))
