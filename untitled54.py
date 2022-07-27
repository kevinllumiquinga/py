# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:08:45 2022

@author: USER
"""

import random
def mostrar_valor(valor):
    for filas in valor:
        print(filas)
filas=int(input("Ingrese el numero de filas mayor que 4 y menor que 30: "))
columnas=int(input("Ingrese el numero de columnas  mayor que 4 y menor que 30: "))
matriz=[]
primos=[]
valor=[]


while True:
    if filas<4 and filas>30 and columnas<4 and columnas>30:
        print("El numero ingresado no es valido")
        filas=int(input("Ingrese el numero de filas mayor que 4 y menor que 30: "))
        columnas=int(input("Ingrese el numero de columnas  mayor que 4 y menor que 30: "))      
    else:
        for i in range(filas):
            matriz.append([])
            for j in range(columnas):
                valor=random.randrange(1,101)
                matriz[i].append(valor)
        for i in matriz:
            print(i)
    break

filas=len(matriz)
for i in range(filas):
    suma=sum(matriz[i])
    matriz[i].append(suma)
    
print("\n")

for j in range(columnas):
    suma=sum(filas[j] for filas in matriz)
    primos.append(suma)
    
primos.append(sum(primos))
matriz.append(primos)
mostrar_valor(matriz)