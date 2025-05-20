# Este programa ejecuta una secuencia de Collatz

pasos = int(input("Ingrese un numero para Collatz: "))
nuevo_numero = pasos
numeros = []
print("Secuencia de Collatz con el numero",pasos,"es:")
while pasos>1:
    if pasos%2==0:
        numeros.append(pasos)
        pasos //= 2
    else:
        numeros.append(pasos)
        pasos *= 3
        pasos += 1

numeros.append(1)

# Lo presento en forma de lista
print(numeros)
