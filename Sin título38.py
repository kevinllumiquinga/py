# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:53:12 2022

@author: Alumno
"""

acum=True
num=int(input("Ingrese un valor: "))
if num>0:
 for i in range(1, num+1):
     for j in range(1, num+1):
         print(i*j, end="\t")
     print("")
else:
  while acum== True and num < 1:
   print("El numero es invalido")
   num=int(input("Ingrese un valor: "))
   for i in range(1, num+1):
       for j in range(1, num+1):
           print(i*j, end="\t")
       print("")