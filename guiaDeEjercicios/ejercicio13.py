#Pedir 3 números y mostrar el mayor.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
num3 = int(input("ingrese un numero: "))

if num1 > num2 and num1 > num3:
    print(f"el numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"el numero mayor es: {num2}")
else:
    print(f"el numero mayor es: {num3}")