# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 07:52:29 2022

@author: Alumno
"""

telef=int(input("Ingrese el numero de telefono sin el 0 inicial: "))
telef1=telef/100000000
if telef1 >0 and telef1 <10:
  hora = int(input("Ingrese hora entre [0-23]: ")) 
  if hora >=0 and hora <= 23:
    min=int(input("Ingrese los minutos [0-59]: "))
    if min>= 0 and min <= 59:
      mensaje=""
      finales=telef%1000
      iniciales=telef//1000000
      horareal=hora + (min/60)
      if horareal >=0 and horareal <= 8.34:
        mensaje = "Contestar"
      else:
        if horareal <=13:
          if finales == 909:
            mensaje = "Contestar"
          else:
            mensaje = "No contestar"
        else:
          if horareal <= 19.84:
            mensaje = "Contestar"
            if iniciales == 877:
              mensaje="No contestar"
            else:
              mensaje="Contestar"
          else:
            mensaje="No contestar"
        print(mensaje)
    else:
      print("Rango de minutos no valido")
  else:
    print("Rango de hora no valido")
else:
  print("El numero de telefono debe ser de 9 digitos")
