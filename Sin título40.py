# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:53:38 2022

@author: Alumno
"""

num=int(input("ingrese un valor del LIMITE: "))
if num < 10 and num > 0:
  resultado=0
  resp=1
  for i in range(1,num+1):
    resultado=resultado+(1/i)
    resp=resp+i
  print("El nunero de terminos es: " , resp)
  print("El resultado de la suma es: " , resultado)