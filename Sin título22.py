# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:48:46 2022

@author: Alumno
"""

nombre=input("ing:")
edad=input("ing:")
cedula=input("ing:")
email=input("ing")

print(nombre)

if edad>0 or edad< 150:
     print("verdadero")
else:
     print("falso")
numeros=len(str(cedula))
if numeros>0 and numeros<11:
     print("verdadero")
else:
     print("falso")
if "@" in email:
     print("verdadero")
else:
     print("falso")