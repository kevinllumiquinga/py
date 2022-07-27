# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:49:57 2022

@author: Alumno
"""

import random
var1=int(input("ingrese la cantidad de las filas: "))
var2=int(input("ingrese la vantidad de las columnas: "))
if var1> 4 and var1<30 and var2>4 and var2<30:
  matrix=[[int() for i in range(var2)] for j in range(var1)]
  for filas in range(var1):
    for columnas in range(var2):
      valor= random.sample(range(50,100),1)
      matrix[filas][columnas]=valor
  for i in range(var1):
    print("/", end=" ")
    for j in range(var2):
      print(matrix[i][j],"/",end=" ")
    print("")
  x=0
  y=0
  for k in range(var1):
    print(matrix[x][y])
    x=x+1
    y=y+1