# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:50:03 2022

@author: USER
"""

import random
while True:
    inicio=int(input("desea inicial ingrese 0 o 1, si desea terminar ingrese numeros mayores a 1: "))
    if inicio>1:
       break
    
    var1=int(input("ingrese el tamaño de su vector, recuerde que debe ser mayor que 5 y menos que 30: "))
    if var1>5 and var1<30:
        ale1= random.sample(range(1,100), var1)
        ale2= random.sample(range(1,100), var1)
        print("esta es la lisrta 1: ",ale1)
        print("esta es la lista 2: ",ale2)
        print("")
        print("1.suma")
        print("2.resta")
        print("3.multiplicacion")
        print("4.division")
        var2=int(input("ingrese el numero de la operacion que desea realizar:"))
        if var2==1:
            vector1=ale1
            vector2=ale2
            vector3=[0]*var1
            for i in range(var1):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(var1):
                "print(vector3[i])"
            print(vector3)
        elif var2==2:
            v1=ale1
            v2=ale2
            v3=[0]*var1
            for k in range(var1):
                v3[k]=v1[k]-v2[k]
            for k in range(var1):
                "print(v3[k]"
            print(v3)
        elif var2==4:
            div1=ale1
            div2=ale2
            div3=[0]*var1
            for j in range(var1):
                div3[j]=div1[j]/div2[j]
            for j in range(var1):
                "print(div3[j]"
            print(div3)
        elif var2==3:
            mul1=ale1
            mul2=ale2
            mul3=[0]*var1
            for f in range(var1):
                mul3[f]=mul1[f]*mul2[f]
            for f in range(var1):
                "print(v3[f]"
            print(mul3)
    else:
        print("fin del progamdo, datos ingresados son incorrectos")