# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:57:24 2022

@author: Alumno
"""

def numeroencontrar():
  import numpy
  a1=[]
  for i in  range(0,50):
    a1.append(numpy.random.randint(1,10))
  print("listas:",a1)
  cont=0
  n=int(input("ingrese el numro que busca:"))
  for i in a1:
    if i==n:
      cont+=1
  print("econtrado:",cont,"veces")
  return(cont)
  
numeroencontrar()