import cmath 
  
a =int(input("ingrese el valor de a:"))
b =int(input("ingrese el valor de b:"))
c =int(input("ingrese el valor de c:"))
if a==0:
    print("division para cero")
elif a==b or a==c or b==c or b==a:
    print("raiz negativa")
elif a!=0:
    var1 = (b**2) - (4 * a*c) 
      
    ans1 = (-b-cmath.sqrt(var1))/(2 * a) 
    ans2 = (-b + cmath.sqrt(var1))/(2 * a) 

    if ans1==ans2:
        print("unica solucion")
        print("x=",ans1)
    elif ans1 != ans2:
        print("dos soluciones:")
        print("x1=",ans1)
        print("x2=",ans2)
        

