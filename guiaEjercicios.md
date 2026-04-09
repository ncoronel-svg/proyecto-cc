### GUIA DE EJERCICIOS


# ETAPA 1 Variables y tipos de datos en Python

- EXPLICACION, Primero, ejemplos claros de los tipos principales y cómo se declaran:

```python

#APARTIR DE ACA ADENTRO ARRANCA EL CODIGO DE PYTHON (```python es para que lo tome como el lenguaje eso no se incluye, no darle bola)


# Enteros (int)
edad = 25

# Flotantes (float)
altura = 1.75

# String (str)
nombre = "Nahuel"

# Booleanos (bool)
es_mayor = True

# Listas (list)
numeros = [1, 2, 3, 4]

# Tuplas (tuple) (inmutables)
coordenadas = (10, 20)

# Diccionarios (dict)
persona = {
    "nombre": "Nahuel",
    "edad": 25
}

# None (ausencia de valor)
dato = None


# IMPORTANTE

# Ver tipo de dato
print(type(nombre))  # <class 'str'> esto es lo que devuelve

# puede devolver
# str
# int
# bool
# etc... dependiendo el tipo de dato

```

* Extras importantes:

- Python es dinámico → no definís el tipo explícitamente.
Esto quiere decir que si vos definis

```python

texto = 'hola mundo'

# luego vos volves a reasignar texto

texto = 'hola'

#entonces si vos luego haces un print

print(texto) # esto devuelve:  'hola'

# entonces que quiere decir?

# ------------------------------------------------

# mediante la ejecucion del programa podes reasignar
# las variables para cuando necesites que tome otro valor,
# pero recorda estas sustituyendo un valor, esto quiere decir

# si aplicas esto, se va a perder el hola mundo en el caso del ejemplo
# y va a quedar el hola como valor


texto = 'hola mundo'

texto = 'hola'

print(texto) # devuelve: 'hola'

```


- Podés cambiar el tipo en runtime.
- Conversión de tipos:

### metodos de conversion

```python

# transforma un string numero, a numero entero

numero = int("10") # funcion int()  dentro del () se le pasa un numero en string "93"

# ejemplo de uso  int(numero en string) =  int("93")

#2do ejemplo

valor = '29'

valor_a_numero = int(valor) #podes pasarle variables que dentro tengan un valor

print(valor_a_numero) # devuelve 29

# -------------------------------------

decimal = float("3.14") #aplica la misma explicacion que para el anterior

#solo que aca pasa a ser decimal  3.14

print(decimal) # devuelve 3.14



texto = str(100) # aca aplica lo mismo pero al reves

# lo que le pases adentro lo transforma a string

print(texto) # devuelve "100"



```

### FUNCIONES DE ENTRADA

Entrada de usuario:

```python



nombre = input("Ingresá tu nombre: ") # si el usuario ingresa "juan"
edad = int(input("Ingresá tu edad: "))# si el usuario ingresa "20", luego fijate que lo trasforma con un int a numero entero y queda 20, deja de ser string


#esta es una forma de printear en una sola linea

print("Hola", nombre, "tenés", edad) # devuelve "hola juan tenes 20"


#esta es otra forma

print(f"hola {nombre} tenes {edad}")


# y sino tenes esta

print('hola')
print(nombre)
print('tenes')
print(edad)


```


# Ejercicios (Intermedio)

- Crear variables para nombre, edad y altura. Mostrar todo en una sola línea.

- Pedir al usuario dos números y mostrar la suma.

- Pedir un número como string y convertirlo a int, luego multiplicarlo por 2.

- Crear una lista con 5 números y mostrar el tipo de la lista y de un elemento.

- Crear un diccionario con datos de una persona y mostrar solo el nombre.









-------------------------------------------------------------------------



# Etapa 2 — Condicionales

# Ejemplo explicado para varias condiciones en una misma:

```python


x = 9
j = 5

# Evaluamos múltiples condiciones
if (x < 10) and ((x > 8) or (j > 9)):
    print("Se cumple la condición")
else:
    print("No se cumple")

# Explicación:
# x < 10 → True
# x > 8 → True
# j > 9 → False
# (True OR False) → True
# (True AND True) → True → entra al if


#forma comun 

if(x < 19):
    print('es menor')
else:
    print('es mayor')

```

# Otro ejemplo con operadores:

```python

edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")
elif edad == 17:
    print("Casi mayor")
else:
    print("Menor")


```



--------------------------------------------------------------------------


* Fáciles:

1. Pedir un número y decir si es mayor a 10.
2. Pedir un número y decir si es par o impar.
3. Pedir edad y decir si es mayor de edad.
4. Pedir dos números y decir cuál es mayor.
5. Verificar si un número es igual a 0.

* Intermedios:

1. Pedir un número y decir si está entre 10 y 20.
2. Pedir usuario y contraseña y validar (valores fijos).
3. Pedir 3 números y mostrar el mayor.
4. Verificar si un número NO está entre 1 y 100.

5. Evaluar:

```python

# evaluar  que da cada caso

if (x > 5 and x < 15) or (x == 20):

## definir si da true o false dependiendo los casos de uso en x ( se puede dar explicacion)

x > 5 =

x < 15 =

x == 20

## explicar como evalua el and

* RESPONDER:


## Explicar como evalua el or

* RESPONDER:

```


# Difíciles:

1. Sistema de notas: si es mayor igual a 7 aprobado, si tiene 4 entre 6 recupera, si es menor a 4 desaprobado.

2. crear un array de Autos ponerle nombres a gusto pero que sean 6 y 2 se repitan, luego condicionar si existe algun auto que se llame igual a lo ingresado por el usuario, se necesita conseguir eso que ingresa el usuario, verificar que primero la cantidad de autos sea 6 si es igual a 6 entonces entra a las siguientes condiciones

- verifica si la palabra es igual a alguno de los 6 items que hay, verificar cada uno es decir son 6 condiciones

3. Si x es mayor a h , y , d es un numero impar , o , x es menor que d
- mostrar que se pudo entrar a la condicion con un print
- se usan condiciones multiples es la idea de la practica, se puede hacer en un solo if( aca dentro ) sino se entiende revisar los primeros ejemplos de la etapa 2 que hay se muestra un ejemplo

### sino salen seguir con otro no hay problema, no perder mucho tiempo en estos
2. Validar si un año es bisiesto (condiciones múltiples).

3. Simular login con 3 intentos (condicional + contador).



------------------------------------------------------------------------

# Etapa 3 — Bucles (for / while)

# explicacion de lista:

```python

#lista de numeros
numeros = [1, 2, 3, 4]


#recorremos la lista de numeros, y objetemos por num
for num in numeros:
    print(num)

    #primer vuelta num vale 1 y el print da 1
    #segunda vuelta num vale 2 y el print da 2
    #primer vuelta num vale 3 y el print da 3
    #primer vuelta num vale 4 y el print da 4


```


# Ejemplo diccionario:

```python


persona = {
    "nombre": "Nahuel",
    "edad": 25
}

# de esta forma se recorre un diccionario
for clave, valor in persona.items():
    print(clave, valor)
#                     clave    valor
    
    #primer vuelta :  nombre  nahuel

    #segunda vuelta:  edad      25

```


Ejemplo while:
```python


i = 0

while i < 5: # siempre que la condicion de true, el bucle continua, si da false se corta el bucle
    print(i)
    i += 1


```



# Ejercicios (Bucles)

1. Recorrer una lista de números e imprimirlos.
2. Recorrer una lista y mostrar solo los pares.
3. Recorrer un diccionario e imprimir claves.
4. Usar while para contar del 1 al 10.
5. Pedir números hasta que el usuario ingrese 0.
6. Sumar todos los números de una lista.
7. Contar cuántos números son mayores a 10 en una lista.
8. Crear una lista con inputs del usuario usando un bucle.
9. Recorrer un string y contar vocales.
10. Simular menú con while hasta que el usuario elija salir.
11. Generar tabla de multiplicar con for.
12. Buscar un número dentro de una lista.
13. Invertir una lista manualmente (sin funciones).
14. Crear un diccionario con nombres y edades y recorrerlo.
15. Bucle que valide input hasta que sea correcto.
