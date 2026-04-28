#Sistema de notas: si es mayor igual a 7 aprobado,
#  si tiene 4 entre 6 recupera, si es menor a 4 desaprobado.

nota = int(input("ingrese la nota: "))

if nota >= 7:
    print("aprobado")
if nota >= 4 and nota <= 6:
    print("debe recuperar")
if nota < 4:
    print("desaprobado")
    
