# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:14:41 2022

@author: Alumno
"""

totalpasaje=1
incremento=0
pasaje= 1.5
edad= int (input("ingrese la edad"))

if edad>=18:
  print("es mayor de edad")
  incremento=pasaje*0.2 
  totalpasaje= pasaje+incremento
else:
   print("es menor de edad")
   print("incrememto: ",incremento," y pasaje total:",totalpasaje)
print("fin del progrma")