import math
var1=int(input("ingrese la base: "))
var2=int(input("ingrese el exponente: "))
if var1>0 and var2>0:
    var3=(math.pow(var1, var2))
    print(int(var3))
elif var1<0 and var2>0:
    print("error")
elif var1>0 and var2<0:
    print("error")


