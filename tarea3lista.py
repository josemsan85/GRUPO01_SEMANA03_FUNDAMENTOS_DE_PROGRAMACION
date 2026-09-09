nota1 = int (input("primera nota " ))
nota2 = int (input("segunda nota " ))
nota3 = int (input("tercera nota " ))
nota4 = int (input("cuarta nota " ))

listaNotas = [] 

listaNotas.append(nota1)
listaNotas.append(nota2)
listaNotas.append(nota3)
listaNotas.append(nota4)

def mayores (notas):
   
    for i in range(0,len( notas)):
      if notas[i] <0 or notas[i] > 20  :
        # return False;
         break
     
      
         
def calcularNotas (notas):

    
    prom = "el promedio es " + str( sum(notas)/len(notas))
  
    mina = "el minimo de notas es " + str( min(notas))
    maxi = "el maximo de notas es " + str( max(notas))

    return prom, maxi, mina 

print(str( calcularNotas(listaNotas)) )
 
def reporteFormateado ( notas):

   print ("=" * 30)
   print ("REPORTE DE NOTAS")
   print ("=" * 30)

   for i in range (0, len (notas)):
      print ("Estudiante " + str ( i+1) + " : " + str (notas[i]))

    

reporteFormateado( listaNotas) 