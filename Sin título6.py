# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:42:57 2022

@author: Alumno
"""

num=int(input("ingrese un valor: "))
if num > 0:
 for i in range(1, num):
     for j in range(1, i + 1):
         print(j, end= " ")
     print()
 for i in range(num, 0, -1):
    for j in range(1, i + 1):
         print(j, end=" ")
    print()
else:
  print("el numero ingresado es incorrecto")
  num=int(input("ingrese un valor: "))
  for i in range(1, num):
      for j in range(1, i + 1):
          print(j, end= " ")
      print()
  for i in range(num, 0, -1):
      for j in range(1, i + 1):
          print(j, end=" ")
      print()