#Pedir usuario y contraseña y validar (valores fijos).

usuario = "jose"
contraseña = "Pn"

## UNICA CORRECION SEPARAR UN POCO LOS BLOQUES DE IF Y ELSE, Y TAMBIEN COMENTASR ARRIBA, EL RESTO MUY BIEN

usuario_ing = input("ingese su usuario: ")
contraseña_ing = input("ingrese su contraseña: ")

#COMENTO YO DE EJEMPLO PARA QUE SE ENTIENDA LA BUENA PRACTICA

#validacion de usuario
if usuario_ing == usuario:
    print("el usuario es correcto")
else:
    print("usuario no registrado")


#validacion de contrasenia
if contraseña_ing == contraseña:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")

#validacion de contrasenia y usuario
if contraseña_ing == contraseña and usuario_ing == usuario:
    print("sesion iniciada correctamente")

#ESTE ELIF ESTA MAL, YA VERIFICA QUE SI LA CONTRASENIA O EL USUARIO NO ES IGUAL NO VA A MANDAR EL SIGUIENTE PASO
elif contraseña_ing == contraseña and usuario_ing != usuario:
    print("el usuario no coincide")
elif contraseña != contraseña and usuario_ing == usuario:
    print("la contraseña no coicide")
    #TODO ESO ES INNECESARIO
###############################################

else:
    print("no se pudo iniciar sesion")
