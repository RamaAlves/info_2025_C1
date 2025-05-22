# Días de la semana: Pide al usuario un número del 1 al 7. 
# Imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). 
# Si el número no está en el rango, imprime "Número inválido".
# Dificil: incorporar bucle while

""" dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
numero = int(input("Ingresa un número del 1 al 7: "))
if 1 <= numero <= 7:
print(dias_semana[numero - 1])
else:
print("Número inválido") """

""" dia = int(input("Ingrese un numero del 1 al 7 : "))

while dia < 1 or dia > 7:
    dia = int(input("Numero inválido, porfavor ingrese otro: "))

if dia == 1:
    print("\nUsted a indicado el dia domingo")
elif dia == 2:
    print("\nUsted a indicado el dia lunes")
elif dia == 3:
    print("\nUsted a indicado el dia martes")
elif dia == 4:
    print("\nUsted a indicado el dia miércoles")
elif dia == 5:
    print("\nUsted a indicado el dia jueves")
elif dia == 6:
    print("\nUsted a indicado el dia viernes")
else:
    print("\nUsted a indicado el dia Sabado")

 """

dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

while True:
    numero = int(input("Ingresa un número del 1 al 7: "))

    if 1 <= numero <= 7:
        print(dias_semana[numero - 1])
        break
    else:
        print("Número inválido. Inténtalo de nuevo.")