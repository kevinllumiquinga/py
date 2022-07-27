# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:52:17 2022

@author: Alumno
"""

var_1 = int(input("Ingrese el monto: "))
def uno():
  var_mn100= ((var_1 - 1000 ) % 100 )*0.02
  return var_mn100
def dos():
  var_ms100 = (var_1 - 1000 )*0.05
  return var_ms100
def tres():
  var_ms1000 = 1000*0.08
  return var_ms1000

if var_1 < 2000 :
 pago = ( uno() + dos() + tres() )
 print("El descuento es: " , pago )
 total= var_1 - pago
 print("El valor total es: " , total)

else:
 if var_1 >= 2000:
  var_ms2000=var_1 * 0.10
  print("El descuento es: " , var_ms2000)
  total2= var_1 - var_ms2000
  print("El valor total es: " , total2)