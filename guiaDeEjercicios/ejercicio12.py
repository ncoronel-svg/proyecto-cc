#Pedir usuario y contraseña y validar (valores fijos).

usuario = "jose"
contraseña = "Pn"


usuario_ing = input("ingese su usuario: ")
contraseña_ing = input("ingrese su contraseña: ")

if usuario_ing == usuario:
    print("el usuario es correcto")
else:
    print("usuario no registrado")
if contraseña_ing == contraseña:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")
if contraseña_ing == contraseña and usuario_ing == usuario:
    print("sesion iniciada correctamente")
elif contraseña_ing == contraseña and usuario_ing != usuario:
    print("el usuario no coincide")
elif contraseña != contraseña and usuario_ing == usuario:
    print("la contraseña no coicide")
else:
    print("no se pudo iniciar sesion")