# Crear un sistema que dado un número genere una sucesión de fibonacci con esa cantidad 
# de números en la serie, por ejemplo: 3 -> 0,1,1 o 5 -> 0,1,1,2,3

print("Este programa genera una serie fibonacci")
pasos = int(input("Ingrese la cantidad de pasos deseada: "))
anterior,actual=0,1

print("\nLos primeros ",pasos," numeros de la serie de fibonacci son: ")
for i in range(pasos):
    if i == pasos-1:
        print(anterior, end="\n")
    else:
        print(anterior, end=",")
    temp=anterior
    anterior=actual
    actual=temp+actual