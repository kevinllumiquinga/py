# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:57:06 2022

@author: Alumno
"""

filas=int(input("introduce en nuemro de filas"))
columnas=int(input("introduce el numero de columnas"))

matriz=[]
for i in range(filas):
  matriz.append([])
  for j in range(columnas):
    valor= int(input("fila , columnas{}:". format(i+1, j+1)))
    matriz[i].append(valor)
print()
for fila in matriz:
  print("[",end=" ")
  for elemento in fila:
    print("{:8.2f}".format(elemento), end=" ")
  print("]")
print()
