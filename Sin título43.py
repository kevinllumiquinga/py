# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:54:20 2022

@author: Alumno
"""

import math
def obtenerDatos():
 print ("Ingrese el numero de datos: ")
 numeroDatos = int(input())
 datos = []
 for i in range(0, numeroDatos):
  print ("Ingrese dato ", i + 1)
  dato = float(input())
  datos.append(int(dato))
 return datos
def obtenerPromedio(datos):
 suma = 0
 for dato in datos:
  suma += dato
 return suma / len(datos)
def obtenerVarianza(datos):
 n = len(datos)
 promedio = obtenerPromedio(datos)
 varianza = 0
 for dato in datos:
  varianza += math.pow((dato - promedio), 2)
 return varianza / (n - 1)
def obtenerDesviacion(varianza, datos):
 if(varianza == 0):
  varianza = obtenerVarianza(datos)
  return math.sqrt(varianza)
 elif(varianza > 0):
  return math.sqrt(varianza)
datos = obtenerDatos()
varianza = obtenerVarianza(datos)
suma=obtenerPromedio(datos)
print("El valor de la media es: ", suma)
print ("El valor de la varianza es: ", varianza)
desviasion = obtenerDesviacion(varianza, datos)
print ("El valor de la desviacion standar es: ", desviasion)