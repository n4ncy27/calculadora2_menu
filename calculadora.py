# calculadora con menu 

from math import log 

print("------------------------------------")
print("------CALCULADORA_MENU--------------")
print("------------------------------------")

# input 
bandera = false 
x = float(input ("Dame el  valor de el numero x: "))
y = float(input ("Dame el  valor de el numero y: "))

print("\n dame la opcion que deseas realizar: \n")
# se despliega el menu para seleccionar la opcion que deseas realizar:

print(" 1.sumar (el primero mas el segundo)")
print(" 2.Restar (el primero menos el segundo)")
print(" 3.multiplicar (el primero por el segundo)")
print(" 4.dividir (el primero a la potencia del segundo)")
print(" 5.potencia (el primero mas el segundo)")
print(" 6.logaritmo (el logaritmo del  primero)")

opcion = int(input("\n dame la opcion: "))

# processing
if (opcion == 1):
    z = x + y
    print (x,"+",y)
elif (opcion == 2 ):
    z = x - y
    print (x,"-",y)
elif (opcion == 3 ):
    z = x * y
    print (x,"x",y)
elif (opcion == 4 and y!=0 ):
    z = x / y
    print (x,"/",y)
elif (opcion == 4 and y==0):
    print("el denominador es igual a cero y")
    print("NO SE PUEDE REALIZAR LA DIVISION")
    bandera = True 
elif (opcion == 5):
    z = pow(x,y)
    print(x, "^", y)
elif (opcion ==6 and x > 0):
    z = log(x)
    print("logaritmo de", x)
elif(opcion == 0 and x <= 0):
    print("El valor de x es <=a cero y")
    print("NO SE PUEDE CALCULAR EL LOGARITMO.")
    bandera = True
else:
    print("Opcion no valida")

# se escribe el resultado con otra condicion 
if (opcion < 7 and bandera == false ): 
    print("Resultado =", z)

#fin

