# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:53:00 2022

@author: Alumno
"""

rollo_1 = 500
rollo_2 = 300
rollo_3 = 75

mts_alam = int(input("Ingrese la longitud total de alambre [m]: "))
var_1 = int(mts_alam / rollo_1)  #
var_2 = int(mts_alam % rollo_1)
var_3 = int(var_1 / rollo_2)   #
var_4 = int(mts_alam % rollo_2)
var_5 = int(var_4 / rollo_3)   #
var_6 = int(var_4 % rollo_3)   #
print(var_1 , "rollos de 500 metros, " , var_3 , "Rollos de 300 metros, " 
      , var_5 , "Rollos de 75 metros y" , " le faltan" , var_6 , "metros")