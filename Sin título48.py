# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:55:35 2022

@author: Alumno
"""

n=int(input("Cuantos numeros desea ingresa ? : "))
numeros = [ ]

for i in range(n):
  acumulador=0
  num=int(input("Dato para el vector: " ))
  numeros.append(num)
  for j in numeros:
    acumulador=acumulador+numeros[i]
  acumuladorTot=acumulador + num

  cont=0
  cont2=1
  if numeros[0]%2 == 0:
    cont=cont+1
  elif numeros[0]%2 ==1:
    cont2=cont2+1

print("los numeros pares son: ",cont)
print("los numeros impares son: ",cont2)
print("El promedio de la matriz es: " ,(acumuladorTot/n))