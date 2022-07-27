# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:51:53 2022

@author: Alumno
"""

def grados():
  resp = ((5 / 9)*(int(input("Ingrese grados Fahrenhei: ")) - 32))
  return resp
var1=grados()
print("Grados centigrados: " , var1)