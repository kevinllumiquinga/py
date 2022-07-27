# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:43:09 2022

@author: Alumno
"""

var1=int(input("ingrese el numero de ACL: "))

if var1>=1 and var1<=99 or var1>=1300 and var1<=1999:
  print("El dato ingresado corresponde a una ACL de tipo Estándar")
elif var1>=100 and var1<=199 or var1>=2000 and var1<=2699:
  print("El dato ingresado corresponde a una ACL de tipo Extendida en rango expandido")
else:
  print("ACL no valida")