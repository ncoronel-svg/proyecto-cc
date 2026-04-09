#Pedir un número y decir si es mayor a 10.

num1 = int(input("ingrese un numero: "))

def mayordiez(a):
    if a == 10:
        print("el numero es igual a 10 .-.")
    elif a > 10:
        print("el numero es mayor a 10")
    else:
        print("el numero es menor a 10")

print(mayordiez(num1))