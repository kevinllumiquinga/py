# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:17:26 2022

@author: USER
"""
var1=int(input("ingrese un numero"))
import random
lista=[]
for i in range(var1):
    var2=random.randint(0,100)
    lista.append(var2)
print(lista)