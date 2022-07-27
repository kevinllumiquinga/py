# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:43:46 2022

@author: Alumno
"""

nom=(input("ingrese su nombre: "))
var1=int(input("ingrese su peso (Kg): "))
var2=float(input("ingrese su altura (m): "))
cal=var1/(var2*var2)
if cal< 18.5:
  print(nom,"tiene un IMC de ",cal,"kg/m^2")
  print("observacion sobre peso: bajo")
elif cal>=18.5 and cal<=24.9:
  print(nom,"tien un INC de ",cal,"kg/m^2")
  print("observacion peso: norla")
elif cal>=25.0 and cal<=29.9:
  print(nom,"tien un INC de ",cal,"kg/m^2")
  print("observacion peso: sobrepeso")
elif cal>=30.0:
  print(nom,"tien un INC de ",cal,"kg/m^2")
  print("observacion peso: obeso")
