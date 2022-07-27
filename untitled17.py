# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:47:20 2022

@author: USER
"""

var=False
var2=False
numprimos=[]


while var==False:
    num = int(input("Ingresar numero: "))
if num<=1:
    print("Error debe ingresar un numero mayor a 1")
else:
    var=True

if num==2:
    print("El 2 es el primer numero primo")
    quit()
else:
  #determinar si el numero es primo
    for i in range(2,num):
      if (num % i) == 0:
          var2=True
          break

  #Calculo de numeros primos
  for k in range(2, num + 1):
   for j in range(2, int(k ** 0.5) + 1):
    if k%j == 0:
     break
   else:
    numprimos.append(k)

len=len(numprimos)
sumaprimos=sum(numprimos)
if len>0:
 promedioprimos="{:.2f}".format(sumaprimos/len);
      
if var2==True:
  print(num,"NO ES NUMERO PRIMO")
  print("Existen",len, "numeros primos en el rango :",numprimos)
  print("La suma de los numero primos es:",sumaprimos)
  print("La promedio de los numero primos es:",promedioprimos)

else:
  print(num,"NUMERO PRIMO")
