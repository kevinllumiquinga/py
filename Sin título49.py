# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:55:46 2022

@author: Alumno
"""

import numpy as np

filas=int(input("Introdusca el numero de filas: "))
columnas=int(input("Introdusca el numero de comlumnas: "))
lista1=[ ]
for i in range(filas):
  lista1.append([])
  for j in range(columnas):
    valor=int(input("Dato para el vector: "))
    lista1[i].append(valor)
print("La suma total es: " ,np.sum(lista1))
print ("El promedio es: " ,np.mean(lista1))