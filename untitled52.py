# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:21:21 2022

@author: USER
"""

import random

valor=random.sample(range(50,100),1 )
primos=[]
for n in range(1,50):
    contador=0
    for i in range(1,n+1):
        if n % i ==0:
            contador+=1
    if contador ==2:
        print(primos.append(n))