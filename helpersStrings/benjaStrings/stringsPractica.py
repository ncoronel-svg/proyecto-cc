# 1. Pedir un string y mostrarlo en mayúsculas
# input: "hola"
# output: "HOLA"


def convertirMayuscula(parametro):
    return parametro.upper()
    
    
    
def eliminaEspacio(parametro_palabra):
    return parametro_palabra.strip()

#convertirMayuscula()


palabra = input("ingrese una palabra : ")
palabra_mod = convertirMayuscula(palabra)

print(palabra_mod)

palabra2 = input("ingrese una palabra con espacios: ")
palabra_mod2 = eliminaEspacio(palabra2)

print(palabra_mod2)

def reemplazarPalabra(mpalabra3):
    return palabra3.replace("mundo", "munde")

palabra3 = "hola mundo"

print(palabra3)

palabra_mod = reemplazarPalabra(palabra3)

print(palabra_mod)

def palabraCount():
    pass

palabra4 = "banana".count("a")

print(palabra4)