# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:46:10 2022

@author: Alumno
"""

var1=int(input("ingrese un valor: "))
var2=int(input("ingrese el tiempo en años: "))
var3=float(input("ingrese el interes: "))
if var1>=500:
  mul=var3*0.01
  mul2=(mul*var1*12)* var2+var1
  print("total de polisa: ",mul2)