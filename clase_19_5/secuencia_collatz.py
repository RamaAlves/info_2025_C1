
# Ahora, desarrolle un programa que grafique los largos de las secuencias de Collatz de los numeros enteros positivos menores al numero ingresado con *: 
#(recuerda que si multiplicas un valor numero por un string, el string se repetira el numero veces que se multiplico)
# numero_inicio = int(input("Ingrese un número: "))  

#Grafica las secuencias de todos los numeros menores al ingresado
""" pasos = int(input("Ingrese un numero: "))
for i in range(1,pasos):
    numeros = []
    aux = i
    print("Secuencia de Collatz con el numero",i,"es:")
    while aux>1:
        if aux%2==0:
            numeros.append(aux)
            aux //= 2
        else:
            numeros.append(aux)
            aux *= 3
            aux += 1
    numeros.append(1)

    print(numeros) """


# Grafica longitudes de las secuendas de todos los numeros menores al ingresado con *
""" pasos = int(input("Ingrese un numero: "))
aux2 = pasos


for i in range(1,pasos+1):
    numeros = []
    aux = i
    print(i,":",end=" ")
    while aux>1:
        if aux%2==0:
            print("*",end=(" "))
            aux //= 2
        else:
            print("*",end=" ")
            aux *= 3
            aux += 1

    print("*")
 """

    
# solo longitud de las secuencias 
# de los numeros en la secuencia original menores al ingresado

pasos = int(input("Ingrese un numero: "))
aux2 = pasos
numeros = []
print("Secuencia de Collatz con el numero",pasos,"es:")
while aux2>1:
    if aux2%2==0:
        numeros.append(aux2)
        aux2 //= 2
    else:
        numeros.append(aux2)
        aux2 *= 3
        aux2 += 1
numeros.append(1)

# Lo presento en forma de lista
print(numeros)


for j in (numeros):
    if j < pasos:
        numeros = []
        aux = j
        print(j,":",end=" ")
        while aux>1:
            if aux%2==0:
                print("*",end=(" "))
                aux //= 2
            else:
                print("*",end=" ")
                aux *= 3
                aux += 1

        print("*")