#Este programa genera una serie de numeros fibonacci

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