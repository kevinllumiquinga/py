# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:14:19 2022

@author: USER
"""

nombre=input("ing:")
edad=int(input("ing:"))
cedula=input("ing:")
email=input("ing")

if "a,b" in nombre:
    print("verdadero")

if edad>0 and edad< 150:
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
