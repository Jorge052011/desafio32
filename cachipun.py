import random
import sys
elecciones = ["piedra", "papel", "tijera"]

eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

if eleccion_usuario not in elecciones:
    print("Argumento invalido. Por favor, elige piedra, papel o tijera.")
else:
    eleccion_computadora = random.choice(elecciones)
    print(f"La elección de la computadora es: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("Empate")

    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
        (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("Ganaste")
    else:
    
        print("Perdiste")
