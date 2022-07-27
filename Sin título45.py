# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:54:38 2022

@author: Alumno
"""

def ingreseDato():
  var_1=int(input("Ingrese el primer numero: "))
  var_2=int(input("Ingrese el segundo numero: "))
  if var_1==var_2:
    print("Los dos numeros son iguales")
  elif var_1 > var_2:
    print("El numero mayor es: " , var_1)
  elif var_2 > var_1:
    print("El numero mayor es: " , var_2)
ingreseDato()