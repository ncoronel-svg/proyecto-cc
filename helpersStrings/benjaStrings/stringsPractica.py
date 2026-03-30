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

# 5. Verificar si un string termina con ".py"
# input: "script.py"
# output: True

def verificacion(palabri):
    return palabri.endswith(".py")

#palabrita = ("skibidi.py")
#print (verificacion(palabrita))

# 6. Dado un string, devolver la cantidad de palabras
# input: "hola como estas"
# output: 3

def contarSt(a):
    return a.count("") 

textito = "hola como estas"

# 7. Invertir un string
# input: "python"
# output: "nohtyp"

def invertir(a): 
    return a[::-1]

tex = "hola"
print(invertir(tex))

# 8. Verificar si un string es palíndromo
# input: "reconocer"
# output: True

def reconocer(x):
    if x == x[: :-1]:
        return True
    else: 
        return False

texto2 = "ano"
print(reconocer(texto2))

# 9. Convertir un string tipo "a,b,c,d" en lista
# input: "a,b,c,d"
# output: ["a", "b", "c", "d"]

def convLista(xx):
   return xx.split(",")

texto3 = "a,b,c,d"
print(convLista(texto3))

# 10. Unir una lista en un string separado por guiones
# input: ["python", "es", "genial"]
# output: "python-es-genial"

def unirGuiones(xxx):
    return xxx.split(",")

#print(unirGuiones(xxx))


# 11. Contar cuántas vocales tiene un string
# input: "programacion"
# output: 5

x = True
count = 0
def vocalescount(x):
        if x.count("a"):
            count = +1
        elif x.count("e"):
            count = +1
        elif x.count("i"):
            count = +1
        elif x.count("o"): 
            count = +1
        elif x.count("u"):
            count = +1
        return count


palabra24 = "ojala"

print(vocalescount(palabra24))