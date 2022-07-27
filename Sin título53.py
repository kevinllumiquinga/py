# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:57:13 2022

@author: Alumno
"""

a=[[1,2,3],
   [1,2,4]]

b=[[5,6,7],
   [3,4,6]]

def sumar_matrices(m1,m2):
  if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    m3=[]
    for i in range(len(m1)):
      m3.append([])
      for j in range(len(m1[0])):
        m3[i].append(m1[i][j]+m2[i][j])
    return m3
  else:
    return None

c=sumar_matrices(a,b)
if c==None:
  print("no se pueden sumar")
else:
  for fila in c:
    print("[",end=" ")
    for elemento in fila:
      print(elemento,end=" ")
    print("]")


  