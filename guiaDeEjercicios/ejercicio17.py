#Si x es mayor a h , y , d es un numero impar , o , x es menor que d
#- mostrar que se pudo entrar a la condicion con un print
#- se usan condiciones multiples es la idea de la practica,
#se puede hacer en un solo if( aca dentro ) sino se entiende revisar los primeros ejemplos
#de la etapa 2 que hay se muestra un ejemplo

x = int(input("ingresar un numero: "))
h = 5
y = 4
d = int(input("ingrese un numero: "))

if x > h and x > y and d % 2 != 0 and x < d:
    print("verificacion completa")