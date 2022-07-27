# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:53:36 2022

@author: USER
"""
import math
print("escoja una opcio de acuerdo a su requerimiento.")
print("1. descomposicion de fuerzas, dado el cateto opuesto, cateto adyasente y la fuerza. ")
b=int(input("ingrese el cateto opuesto: "))
b1=int(input("ingrese el cateto adyasente: "))
b3=int(input("ingrese la fuerza: "))
div=b1/b
angulo=math.atan(div)
sin3=math.sin(angulo)*b3
sen3=math.cos(angulo)*b3
print()
print("descomposicion en el eje x: ",sen3)
print("descomposicion en el eje y: ",sin3)