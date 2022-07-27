# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:52:12 2022

@author: Alumno
"""

def p():
  var_p = int(input("Ingrese la presion del neumatico: "))
  return var_p
def v():
  var_v = int(input("Ingrese la volumen del neumatico:  "))
  return var_v
def t():
  var_t = int(input("Ingrese la temperatura del neumatico: "))
  return var_t

print("Presion: " , p(), "PSI")
print("Volumen: " , v(), "f^3")
print("Temperatura: " , t(), "°F")

var_m =(p() * v()) / ((t() + 460) * 0.37)
c=round(var_m,5)
print("La masa de aire del neumatico es: " , c ," p ")