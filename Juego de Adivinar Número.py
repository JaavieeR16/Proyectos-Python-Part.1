'''
El programa genera un número aleatorio entre 1 y 100 y el usuario debe adivinarlo. Después de cada intento, el programa le dice al 
usuario si el número es mayor o menor que su suposición hasta que lo adivine correctamente.
'''

import random

def juego_adivinar_numero():
    numero_adivinar = random.randint(1,100)
    adivinado = False

    print("¡Bienvenido al juevo de la adivinanza de números!")
    print("He generado un número aleatorio entre el 1 y el 100.\n¡Intenta adivinarlo!")

    while not adivinado:
        try:
            suposicion = int(input("Introduce tu número: "))

            if suposicion < 1 or suposicion > 100:
                print("Recuerda que solo puedes introducir números del 1 al 100.")
            elif suposicion < numero_adivinar:
                print("El número es mayor, prueba de nuevo.")
            elif suposicion > numero_adivinar:
                print("El número es menor, prueba de nuevo.")
            else:
                print(f"Enhorabuena, Has adivinado el número correcto: {numero_adivinar}.")
                adivinado = True

        except ValueError:
            print("Por favor, introduce un número valido.")

juego_adivinar_numero()