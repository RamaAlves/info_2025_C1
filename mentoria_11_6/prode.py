""" Realizar un prode que permita al usuario elegir cuantos goles hace cada equipo en el cada partido
y luego generar de manera aleatoria el resultado de cada partido.
Si el usuario elige el resultado correcto suma puntos (si acierta con la diferencia de gol suma mas)

Se solicita que:

- Mostrar la tabla de clasificacion de los equipos luego de finalizar el juego de los partidos
- Mostrar los puntos que saco cada jugador
- Mostrar quien es el ganador """
""" class Equipo:
    pass """
nombres_de_equipo=["Argentina", "Brasil", "Japon", "España"]

lista_de_equipos=[]
diccionario = {}

for nombre in nombres_de_equipo:
    """ lista_de_equipos.append(Equipo(nombre)) """
    diccionario[nombre]=[]

print('diccionario:',diccionario)


for key in diccionario:

    gol=int(input('ingrese el gol para '+key+':'))
    diccionario[key].append(gol)
    print(diccionario[key])

print(diccionario)
