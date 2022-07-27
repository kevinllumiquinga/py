# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:54:54 2022

@author: Alumno
"""

def potenciaNum():
 cont=1
 while cont != 0 :
   n=int(input("Ingrese un valor: "))
   if n > 0 :
     print("El cuadrado es: ",n*n)
   elif n == 0:
     cont = n
     print("Fin del programa")
   elif n < 0:
     print("El numero ingresado es negativo")
potenciaNum()