# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:55:04 2022

@author: Alumno
"""

cantidad=int(input("Cuantos numeros desea ingresar ? : "))
lista1 = [ ]
i = 0
while i < cantidad:
  lista=int(input("Dato para el vector: " ))
  lista1.append(lista)
  i+=1
for j in lista1:
  var1=lista1[0]-lista1[1]
  var2=lista1[1]-lista1[2]
  var3=lista1[2]-lista1[3]
  var4=lista1[3]-lista1[4]
  var5=lista1[4]-lista1[5]
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
if var1 > var2:
  print ("la diferencia mayor es: ",var1)
elif var2 > var3:
  print ("la diferencia mayor es: ",var2)
elif var3 > var4:
  print ("la diferencia mayor es: ",var3)
elif var4 > var5:
  print ("la diferencia mayor es: ",var4)