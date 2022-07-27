# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:44:01 2022

@author: Alumno
"""

var1=int(input("ingrese el numero de telefono:"))
var2=var1/100000000
if var2>0 and var2<10:
    var3= int(input("ingrese la hora entre[0-23]:"))
    if var3>=0 and var3<=23:
        min=int(input("ingrese los minutos[0.59]:"))
        if min>=0 and min<=59:
            men=""
            finales=var1%1000
            iniciales=var1//1000000
            horareal=var3 +(min/60)
            if horareal>=0 and horareal<=8.34:
                men="contestar"
            else:
                if horareal<=13:
                    if finales==909:
                        men="contestar"
                    else:
                        men="no contestar"
                else:
                  if horareal<= 19.89:
                       men="contestar"
                       if iniciales==877:
                           men="no contestar"
                       else:
                           men="contestar"
                  else:
                     men="contestar"
                print(men)
        else:
          print("Rango de minutos no valido")
    else: 
        print("Rango de hora no valido")
else:
    print("el numero de telefono debe ser de 9 digitos")