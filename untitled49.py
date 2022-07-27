# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:41:42 2022

@author: USER
"""
notas=int(input("ingrese cuantas calificasines desea colocar"))
asignatura=int(input("ingrese las materias"))
matriz=[]
for i in range(notas):
    matriz.append([])
    for j in range(asignatura):
        valor=input("notas {},asignatturas {}: ".format(i+1, j+1))
        matriz[i].append(valor)
for fila in matriz:
    print("/",end="")
    for elemento in fila:
        print(format(elemento),end="")
    print("/")
 