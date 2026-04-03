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

############################################################################

######
# HACER LA GUIA DE EJERCICIOS DE guiaEjercicios.md y luego venir a ARREGLAR LOS ERRORES DE ESTOS EJERCICIOS.
######

# RECORDATORIO: por cada ejercicio, se crea un archivo:  ejercicio1.py , 
# ejercicio2.py, ejercicio3.py, ..., etc . no amontonar en un solo archivo

# CREAR UNA CARPETA GUIA y ahi dentro ir GENERANDO LOS ARCHIVOS ejercicio1.py, ejercicio2.py, ... , etc

############################################################################



# 11. Contar cuántas vocales tiene un string
# input: "programacion"
# output: 5

x = True
count = 0

############################################################################
#CORREGIR ESTE EJERCICIO, PRACTICAR OPERADORES LOGICOS Y ARITMETICOS, BUSCAR... 
# Y LUEGO APLICARLO AL EJERCICIO

# LOS IF ELSE, NO SIRVEN EN ESTE CASO, DEBE CONTAR TODAS LAS VOCALES, 
# y estas confundientdo el count() con la variable count = 0.

# USAR NOMBRES DISTINTOS, SE PODRIA USAR, RESULTADO = 0, no count = 0, cambiar el valor del parametro llamarle palabra, es mas legible

# recordar tmabien que si vos haces por ejemplos resultado +=  palabra.count('a') y replicas lo mismo solo cambiandole el valor por e i o u

# ya con eso podes sumar,

# entender el concepto de if else

# si vos entras a una condicion, el resto de condiciones no va a entrar

# HAY QUE APLICAR BUENAS PRACTICAS Y RESOLVER EL EJERCICIO CON COHERENCIA DE USO. REHACER
############################################################################

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

# 12. Eliminar todos los espacios de un string
# input: "h o l a"
# output: "hola"

############################################################################
# CON CADA METODO ESTAS SIEMPRE ELIMINANDO ESPACIOS AL FINAL Y AL INICIO, REPETIRLOS 3 VECES DE DIFERENTE FORMA NO TIENE SENTIDO
# NO CODEAR COSAS SIN SENTIDO, FIJARSE EN LA GUIA DE EJERCICIOS, EN TODO CASO ESTARIA BIEN SOLO APLICAR , STRIP(),
# Y LUEGO BUSCAR CON CHAT GPT COMO SE USA EL REPLACE EN PYTHON Y APLICARLO ACA, PEDIR QUE TE LO EXPLIQUE
############################################################################

def eliminarEspacios(palabra):
    palabra.strip()
    palabra.lstrip()
    palabra.rstrip()
    #palabra.replace(" ","")

palabra3 = "h o l a"

print(eliminarEspacios(palabra3)) # no me salio

# 13. Capitalizar la primera letra de cada palabra sin usar .title()
# input: "hola mundo"
# output: "Hola Mundo"

def capPLetra(palabra):
    return palabra.title()

palabra23 = "hola mundo"

print(capPLetra(palabra23))

# 14. Encontrar el carácter que más se repite en un string
# input: "aabbbbcc"
# output: "b"

############################################################################
#EXPLICARME CON COMENTARIOS QUE QUIERE HACER ESTE CODIGO, NO SE ENTIENDE.
############################################################################

def filtroLetras(palabra):
    palabramod3 = str.maketrans(dict.fromkeys('acAC', ''))
    palabracambiada = palabra25.translate(palabramod3)
    return palabracambiada
    

palabra25 = "aabbbbcc"

print(filtroLetras(palabra25))

# 15. Dado un string, devolver otro sin caracteres repetidos
# input: "programar"
# output: "progma" (orden original sin duplicados)



def sinRepetir(palabra):
 palabramod4 = "".join(dict.fromkeys(palabra))
 return palabramod4

palabra26 = "programar"
print(sinRepetir(palabra26))
