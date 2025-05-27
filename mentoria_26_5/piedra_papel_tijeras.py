
# Realizar un programa que permita jugar al piedra papel o tijera 
# utilizando el modulo random y la funcion randint

# el programa debe ejecutarse hasta que el usuario no quiera jugar mas


#  1       2        3

# 🪨      📃      ✂️


""" import random

def generar_random():
    numero_random = random.randint(1,3)
    return numero_random

def juego(usuario,random):
    if usuario == 1:
        if random == 1:
            print("🪨 vs🪨= Empate")
        elif random == 2:
            print("🪨 vs📋= Perdiste")
        else:
            print("🪨 vs✂️= Ganaste")
    if usuario == 2:
        if random == 1:
            print("📋 vs🪨= Ganaste")
        elif random == 2:
            print("📋 vs📋= Empate")
        else:
            print("📋 vs✂️= Perdiste")
    if usuario == 3:
        if random == 1:
            print("✂️ vs🪨= Perdiste")
        elif random == 2:
            print("✂️ vs📋= Ganaste")
        else:
            print("✂️ vs✂️= Empate")

print("Este es un juego de piedras papel o tijeras \n")
while True:
    usuario = int(input("Que opcion quiere jugar?\n1:Piedra\n2:Papel\n3:tijera\n\n"))
    if usuario < 1 or usuario > 3:
        print("Numero inválido, vuelve a intentarlo")
        continue
    numero_random=generar_random()
    juego(usuario,numero_random)
    opcion = input("\nQuieres seguir jugando? S/N")
    if opcion.lower() == "n":
        break

print("\nGracias por jugar") """


# utilizando el modulo random y la funcion choice

import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    print("¡Juego de Piedra, Papel o Tijera!")

    while True:
        eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower().strip()

        if eleccion_usuario == 'salir':
            print("¡Gracias por jugar!")
            break

        if eleccion_usuario not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")
            continue

        eleccion_computadora = random.choice(opciones)

        print(f"Tú elegiste: {eleccion_usuario}")
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
        (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡La computadora ganó!")


jugar_piedra_papel_tijera()