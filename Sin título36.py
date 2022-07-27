# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:52:51 2022

@author: Alumno
"""

nombre = input("Ingrese su nombre: ")
masa = float(input("Ingrese su masa corporal [Kg]: "))
estatura = float(input("Igrese su altua [m]: "))
IMC = masa/estatura **2
c = round(IMC,2)
if 18.5 > IMC:
  var_1 = ("peso bajo")
else:
  if IMC >= 18.5 and IMC <= 24.9:
    var_1 = ("peso normal")
  else:
      if IMC >= 25 and IMC <= 29.9:
       var_1 = ("tiene sobrepeso")
      else:
        if IMC >= 30:
          var_1 = ("Ust es obeso")
print(nombre,"tiene un IMC de " , c , "kg/m^2")
print("Observación sobre peso: " , var_1)