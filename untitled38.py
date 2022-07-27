# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:18:04 2022

@author: USER
"""
import math 
while True:
     var1=int (input("Ingrese el valor de uno(1) si desea empezar, si desea terminar ingrewse el valor de cero(0) "))
     if var1>1:
        print("1.descomposicion de fuerzas, dado el angulo y la fuerza.")
        print("2.descomposicion de fuerzas, dado el cateto opuesto, cateto adyasente y la fuerza.")
        print("3.descomposicion de fuerzas, dado el cateto opuesto y el cateto adyasente.")
        f1=int(input("ingrese el literal que desea obtener: "))
     break
if f1==1:
    a=int(input("ingrese el angulo: "))
    a1=int(input("ingrese la fuerza: "))
    y=math.radians(a)
    sin2=math.sin(y)
    x=math.radians(a)
    sen2=math.cos(x)
         
    print("descomposicion en el eje x: ",sen2)
    print("descomposicion en el eje y: ",sin2)

   

#x=math.radians(30) 
#print("sin:30=",math.sin(x))
#x=math.radians(30) 
#print("cos:30=",math.cos(x))
#x=math.radians(30) 
#print("tan:30=",math.tan(x))