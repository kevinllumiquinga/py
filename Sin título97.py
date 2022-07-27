# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:12:32 2022

@author: Alumno
"""

var1=int(input("ingrese la presion:"))
var2=int(input("ingrese el volumen:"))
var3=int(input("ingrese la temperatura"))

form1= (var1*var2)/(0.37*(var3+460))

print("la masa es igual a:",form1)