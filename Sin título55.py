# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:57:48 2022

@author: Alumno
"""

lista=[]
for i in range(5):
  valor=int(input("ingresa un numero:"))
  lista.append(valor)
print("lista sin ordenar:")
print(lista)
for i in range(4):
    if lista[i]>lista[i+1]:
      a1=lista[i]
      lista[i]=lista[i+1]
      lista[i+1]=a1
print("lista del menor al mayor:")
print(lista)
