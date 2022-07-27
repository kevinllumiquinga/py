def validar(nombre,edad,cedula,email):
    print()
    if nombre==nombre:
        print("verdedero")
    else:
        print("falso")
    if edad>0 and edad< 150:
        print("verdadero")
    else:
        print("falso")
    numeros=len(str(cedula))
    if numeros>0 and numeros<11:
        print("verdadero")
    else:
        print("falso")
    if "@" in email:
        print("verdadero")
    else:
        print("falso")
        
        
nombre=input("ingrese su nombre y apellido: ")
edad=int(input("ingrese su edad: "))
cedula=input("ingrese su numero de cedula: ")
email=input("ingrese su correo electronico: ")
validar(nombre,edad,cedula,email)



