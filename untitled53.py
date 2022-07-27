from random import randint
n=int(input("i9ngrese el numero de filas"))

while n<4 or n>31:
    print("error, fuera de rango")
    n=int(input("i9ngrese el numero de filas"))
    
m=int(input("ingrese el numero de la columna que desea: "))
while m<4 or m>31:
    print("error, fuera de rango")
    m=int(input("ingrese el numero de la columna que desea: "))
    
l=[0]*n
for i in range(n):
    l[i]=[0]*m
for i in range(n):
    for j in range(m):
        h=randint(4,100)
        l[i][j]=h
for i in range(n):
    print("/",end="")
    for j in range(m):
        print(l[i][j],"/",end="")
print("")

f=int(input("coloque la fila que desea sumar: "))
if f>1:
    for i in range(n):
         matriz=l[i]
         print(matriz)
         print(sum(matriz))
         print(sum(matriz)/n)
         
         salir=int(input("si desea terminar el programa digite salir"))
         if salir==0:
             break
         
     
