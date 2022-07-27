# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 08:00:46 2022

@author: USER
"""

matrix=[[int() for i in range(4)] for j in range(4)]
for filas in range(4):
    for columnas in range(4):
        valor=int(input("ingrese el valor: "))
        matrix[filas][columnas]=valor
for i in range(4):
    print("/", end=" ")
    for j in range(4):
        print(matrix[i][j], "/", end=" ")
    print("")