# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:43:24 2022

@author: Alumno
"""

var1=(input("ingrese su nombre: "))
var2=int(input("ingrese el valor del pasaje: "))
var3=int(input("ingrese su edad: "))
if var3<=12 or var3>=65:
  por=var2*0.4
  por2=var2-por
  print("el descuento aplicado es de: ",por)
  print("el total a pagar de",var1,"es de: ",por2)
else:
  print("su pasaje no tiene descuento, debe pagar el valor de ",var2)