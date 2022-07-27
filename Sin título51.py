# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:56:56 2022

@author: Alumno
"""

matriz0=[]

for i in range(10):
  matriz0.append([])
  for j in range(15):
    matriz0[i].append(0)
     
matriz0[4][5]=1
for fila in matriz0:
  print(fila)