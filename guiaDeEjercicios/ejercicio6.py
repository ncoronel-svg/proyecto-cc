#Pedir un número y decir si es mayor a 10.

# ESTO ESTA BIEN
num1 = int(input("ingrese un numero: "))

# ESTO ESTA MAL, NO PEDIMOS FUNCIONES Y DE TODAS FORMAS PASA a COMO PARAMETRO ESTA MAL TAMBIEN, HAY QUE SER MAS
# PROLIJO USAR numero , como parametro, pensar bien los parametros a usar

# DE IGUAL FORMA REHACERLO SIN FUNCION




def mayordiez(a):

    #ESTAS CONDICIONES MUY BIEN, VERIFICA LOS 3 POSIBLES CASOS, MUY BIEN
    if a == 10:
        print("el numero es igual a 10 .-.")
    elif a > 10:
        print("el numero es mayor a 10")
    else:
        print("el numero es menor a 10")

print(mayordiez(num1))
