import random
import sys
elecciones = ["piedra", "papel", "tijera"]

eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

if eleccion_usuario not in elecciones:
    print("Vuelve a jugar no escribiste bien. Por favor, elige piedra, papel o tijera.")
    sys.exit(1)
else:
    eleccion_computadora = random.choice(elecciones)
    print(f"\n La elección de la computadora es: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("\n --------Empate---------")

    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
        (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("\n ***Ganaste***")
    else:
    
        print("\n ¡¡¡¡¡¡¡¡¡¡¡Perdiste!!!!!!")

    
