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


# 2. Pedir un string y eliminar espacios al inicio y final
# input: "  python  "
# output: "python"
palabra2 = input("ingrese una palabra con espacios: ")
palabra_mod2 = eliminaEspacio(palabra2)

print(palabra_mod2)

def reemplazarPalabra(mpalabra3):
    return palabra3.replace("mundo", "munde")



# 3. Reemplazar una palabra en un string
# input: "hola mundo" → reemplazar "mundo" por "Nahuel"
# output: "hola Nahuel"
palabra3 = "hola mundo"

print(palabra3)

palabra_mod = reemplazarPalabra(palabra3)

print(palabra_mod)



# 4. Contar cuántas veces aparece una letra en un string
# input: "banana", letra: "a"
# output: 3
def palabraCount():
    pass

palabra4 = "banana".count("a")

print(palabra4)