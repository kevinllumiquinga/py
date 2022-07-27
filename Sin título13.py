# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:45:40 2022

@author: Alumno
"""

pun1=int(input("ongrese el puntaje de la primera partida: "))
pun2=int(input("ingrese el opuntaje de la segunda partida: "))
pun3=int(input("ingrese el puntaje de la tercera partida: "))
if pun1>pun3 and pun2>pun3:
  print("el resultado obtenido es: ",pun1+pun2)
elif pun2>pun1 and pun3>pun1:
  print("el resultado obtenido es: ",pun2+pun3)
elif pun1>pun2 and pun3>pun2:
  print("el resultado obtendio es: ",pun1+pun3)