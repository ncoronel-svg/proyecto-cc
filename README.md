🔤 Métodos de Strings en Python (con descripción)
🔹 Formato y transformación

upper()
Convierte todos los caracteres a mayúsculas.

"hola".upper()  # "HOLA"


lower()
Convierte todos los caracteres a minúsculas.

"HOLA".lower()  # "hola"


casefold()
Versión más agresiva de lower(), ideal para comparaciones entre textos.

"Straße".casefold()  # "strasse"


capitalize()
Convierte la primera letra en mayúscula y el resto en minúscula.

"hola mundo".capitalize()  # "Hola mundo"


title()
Convierte la primera letra de cada palabra en mayúscula.

"hola mundo".title()  # "Hola Mundo"


swapcase()
Invierte mayúsculas por minúsculas y viceversa.

"Hola".swapcase()  # "hOLA"

🔹 Eliminación de caracteres

strip()
Elimina espacios o caracteres al inicio y final.

"  hola  ".strip()  # "hola"


lstrip()
Elimina solo al inicio.

"  hola".lstrip()  # "hola"


rstrip()
Elimina solo al final.

"hola  ".rstrip()  # "hola"


removeprefix()
Elimina un prefijo si existe.

"test.py".removeprefix("test.")  # "py"


removesuffix()
Elimina un sufijo si existe.

"test.py".removesuffix(".py")  # "test"

🔹 Búsqueda

find()
Busca un substring y devuelve su índice o -1 si no existe.

"hola".find("o")  # 1


rfind()
Busca desde el final.

"hola hola".rfind("hola")  # 5


index()
Igual que find() pero lanza error si no encuentra.

"hola".index("o")  # 1


rindex()
Versión inversa de index().

"hola hola".rindex("hola")  # 5


count()
Cuenta cuántas veces aparece un substring.

"hola hola".count("hola")  # 2

🔹 Validación (booleanos)

startswith()
Verifica si empieza con cierto texto.

"archivo.py".startswith("archivo")  # True


endswith()
Verifica si termina con cierto texto.

"archivo.py".endswith(".py")  # True


isalpha()
True si solo contiene letras.

"hola".isalpha()  # True


isalnum()
True si contiene letras o números.

"hola123".isalnum()  # True


isdigit()
True si contiene solo dígitos.

"123".isdigit()  # True


isnumeric()
Similar a isdigit() pero más amplio (incluye caracteres numéricos especiales).

"Ⅳ".isnumeric()  # True


islower() / isupper()
Verifican si todo está en minúscula o mayúscula.

"hola".islower()  # True


isspace()
True si solo contiene espacios.

"   ".isspace()  # True

🔹 Reemplazo y modificación

replace()
Reemplaza partes del string por otro valor.

"hola mundo".replace("mundo", "Jorge")


translate()
Reemplaza caracteres usando una tabla de traducción.

tabla = str.maketrans("ae", "43")
"hola".translate(tabla)  # "hol4"

🔹 División y unión

split()
Divide el string en una lista según un separador.

"a,b,c".split(",")


rsplit()
Divide desde el final.

"a,b,c".rsplit(",", 1)  # ['a,b', 'c']


splitlines()
Divide por saltos de línea.

"a\nb".splitlines()  # ['a', 'b']


join()
Une una lista en un string.

",".join(["a", "b"])  # "a,b"

🔹 Alineación y formato

center()
Centra el texto.

"hola".center(10, "-")  # "---hola---"


ljust()
Alinea a la izquierda.

"hola".ljust(10, "-")


rjust()
Alinea a la derecha.

"hola".rjust(10, "-")


zfill()
Rellena con ceros a la izquierda.

"42".zfill(5)  # "00042"

🔹 Particionado

partition()
Divide en 3 partes: antes, separador y después.

"key=value".partition("=")
# ('key', '=', 'value')


rpartition()
Igual pero desde el final.

"a=b=c".rpartition("=")
# ('a=b', '=', 'c')

🔹 Formato de strings

format()
Permite insertar valores en un string.

"Hola {}".format("Jorge")


f-strings (moderno y recomendado)
Más limpio y rápido.

nombre = "Jorge"
f"Hola {nombre}"