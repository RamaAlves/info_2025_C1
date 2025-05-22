'''La secuencia de Collatz de un número entero se construye de la siguiente forma:

- si el número es par, se lo divide por dos.
- si es impar, se le multiplica tres y se le suma uno.
- la sucesión termina al llegar a uno.'''

""" Desarrolle un programa que entregue la secuencia de Collatz de un numero entero: """
""" (la secuencia debe imprimirse como un string con los numeros separados por coma) """

# Este programa ejecuta una secuencia de Collatz

pasos = int(input("Ingrese un numero para Collatz: "))

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
