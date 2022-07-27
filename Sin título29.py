# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:51:16 2022

@author: Alumno
"""

def escudos():
  var1=int(input("igrese la cantidad de escudos que desea comprar:"))
  d1= var1*1 
  return d1 
def soldado():
  var2=int(input("ingrese la cantidad de soldados que deasea comprar:"))
  d2= var2*5
  return d2
def dragon():
  var3=int(input("ingrese la cantidad de dragones que desea adquirir:"))
  d3= var3*1000
  return d3
def granada():
  var4=int(input("ingresa la cantidad de granadas que desea comprar:"))
  d4=var4*500
  return d4
def sanador():
  var5=int(input("ingrese la cantidad de sanadores que requiere:"))
  d5=var5*1
  return d5
def hechicero():
  var6=int(input("ingrese la cantidad de hechiceros que necesita:"))
  d6=var6*500
  return d6
def arcos():
  var7=int(input("infrese la cantidad de arcos y flechas requiere:"))
  d7=var7*300
  return d7

#ataque de orcos
oro=(escudos()+soldado()+granada()+arcos())
plata=(dragon()+sanador()+hechicero())

print("tu presupuesto para la batalla es:")
print("en monedad de oro: ",oro)
print("en monedas de plata: ",plata)
