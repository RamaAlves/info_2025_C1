# Pirámide de asteriscos: Imprime una pirámide de asteriscos de 5 filas. 
# (Usa bucles anidados, si es necesario).
# nivel 1
#*
#**
#***
#****
#*****

""" filas = 5

for i in range(1, filas + 1):
    print("*" * i)
 """

#nivel 2
#    *
#   ***
#  *****
# *******
#*********

""" filas = 5

for i in range(1, filas + 1):
    print(" " * (filas - i), end="")
    print("*" * (2 * i - 1))

 """
#queda de tarea

# nivel 3

#    * 
#   * *
#  * * *
# * * * *
#* * * * *

""" filas = 5

for i in range(1,filas+1):
    print(" " * (filas - i), end="")
    # print("* " * (i)) 
    for j in range(1, (2 * i)):
        if j%2:
            print("* ", end="")
    print()
 """

filas = int(input("Ingrese un numero: "))
for i in range(1,filas+1):
    print(" "*(filas-i),end="")
    print("* "*i)