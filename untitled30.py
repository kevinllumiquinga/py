# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:02:06 2022

@author: USER

"""
import random 


matrix=[[int() for i in range(4)] for j in range(4)]
for filas in range(4):
    for columnas in range(4):
        valor= random.sample(range(50,100),1 )
        matrix[filas][columnas]=valor
for i in range(4):
    print("/", end=" ")
    for j in range(4):
        print(matrix[i][j], "/", end=" ")
    print("")
