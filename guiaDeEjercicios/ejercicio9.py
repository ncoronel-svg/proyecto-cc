# Pedir dos números y decir cuál es mayor.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

if num1 > num2:
    print(f"{num1} es el mayor")
elif num1 < num2:
    print(f"{num2} es el mayor")
else:
    print("ambos numeros tienen el mismo valor")