# Divisibles por 3 y 5: Imprime los números del 1 al 30. 
# Si un número es divisible por 3, imprime "Fizz". Si es divisible por 5, imprime "Buzz". 
# Si es divisible por ambos (3 y 5), imprime "FizzBuzz". 
# Si no es divisible por ninguno, imprime el número.

for i in range (1,31):
    if i%3 == 0:
        if i%5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(f'{i}')

# Dificil: aumentar el rango del 1 al 100. si es divisible por 7 imprime "Bozz" y si es divisible por 3, 5 y 7 imprime "FizzBuzzBozz"
# puede pedirle al usuario el rango de numeros a iterar.

""" pasos = int(input("Ingrese un numero: "))

for i in range(1,pasos+1): #si el for tiene que ser del 1 al 30: (for i in range(1,31))
    if i % 5 == 0 and i % 7 == 0 and i % 3 == 0:
        print("FizzBuzzBozz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Bozz")
    else:
        print(i) """

# Si es divisible por ambos (3 y 7), imprime "FizzBozz". 
# Si es divisible por ambos (5 y 7), imprime "BuzzBozz".

""" for i in range(1,pasos+1): #si el for tiene que ser del 1 al 30: (for i in range(1,31))
    if i % 5 == 0 and i % 7 == 0 and i % 3 == 0:
        print("FizzBuzzBozz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBozz")
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzBozz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Bozz")
    else:
        print(i) """