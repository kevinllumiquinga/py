# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:44:15 2022

@author: Alumno
"""

var1=int(input("ingrese la cantidad de fosforos: "))
caj= (var1/40)
paq= (caj/12)
print("la cantidfad de cajas es: ",caj)
print("la cantidad de pauqtes es de: ",paq)
sob=(var1%caj)
psob=(var1%paq)
print("la cantidad de cajas sobrantes es de: ",sob)
print("la cantidad de paquetes sobrantes es de: ",psob)