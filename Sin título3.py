# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:42:13 2022

@author: Alumno
"""

var1=int(input("ingrese el numero de horas: "))
var2=int(input("ingrese la tarifa de horas: "))
var3=int(input("ingrese la tasa de impuesto: "))
pagabrutal=var1*var2
impuesto=pagabrutal*var3
paganeta= impuesto-pagabrutal
print("la paga neta del trabajador es de: ", paganeta)
