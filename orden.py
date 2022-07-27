import time
import random 
var1=int(input("ingrese el tamaño de la lista: "))

ale1= random.sample(range(50,100), var1)
vector1=ale1
vector3=[0]*var1
for i in range(var1):
    vector3[i]=vector1[i]
for i in range(var1):
    time.sleep(1)
    print("el valor en la posicion",i,vector3[i])
    
print()
time.sleep(1)
print("la lista en orden es:")
orden=ale1
orden.sort
print(orden)

