# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:54:06 2022

@author: Alumno
"""

n=int(input("ingrese un numero: "))
if n > 0:
 for i in range(7):
   for j in range(9):
     if (i==0 or i==6) and (1 <= j <= 7):
       print("#",end="")
     elif i == 1 and j == 6:
       print("#",end=" ")
     elif i == 2 and j == 5:
       print("#",end=" ")
     elif i == 3 and j == 4:
       print("#",end=" ")
     elif i == 4 and j == 3:
       print("#",end=" ")
     elif i == 5 and j == 2:
       print("#",end=" ")
     else:
       print(" ",end="")
   print()
else:
  print("El numero es invalido")