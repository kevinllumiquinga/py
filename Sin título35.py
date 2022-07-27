# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:52:41 2022

@author: Alumno
"""

nombre = input("Ingrese su nombre: ")
pasaje = int(input("Ingrese el valor del pasaje: "))
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad <= 12 or edad >= 65:
  descuento = pasaje * 0.40
  descuento1 = pasaje - descuento
print("El descuento aplicado es de: " , descuento)
print("El total a pagar por ", nombre , "es de: " , descuento1)