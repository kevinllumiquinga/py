# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:54:30 2022

@author: Alumno
"""

def cambiar():
  num=int(input("ingrese un numero: "))
  A=num %10
  B=int((num%100)/10)
  C=int((num%1000)/100)
  D=int((num-(num%1000))/1000)

  if num > 0:
    print("El resultado es: ",str(A)+str(B)+str(C)+str(D))
  else:
    print("El numero es invalido")
invertir=cambiar()
