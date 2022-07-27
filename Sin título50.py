# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:55:49 2022

@author: Alumno
"""

filas=int(input("Introdusca el numero de filas: "))
columnas=int(input("Introdusca el numero de comlumnas: "))
lista1=[ ]
for i in range(filas):
  lista1.append([])
  for j in range(columnas):
    valor=(int(input("Ingrese valores: ")))
    lista1[i].append(valor)
print(" ---- la matriz original es: ---")
for i in lista1:
  for j in i:
    print(j," ", end="")  
  print() 
print(" ---- la matriz traspuesta es: ---")
for i in range(0,columnas):
  for j in range(0,filas):
    print(lista1[j][i]," ", end="")  
  print() 