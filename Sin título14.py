# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:46:00 2022

@author: Alumno
"""

var1=int(input("ingrese un numero: "))
if var1>=1 and var1<=100:
  for i in range(1,var1+1):
    var2=i**2
    print(i,"^2","=",var2)