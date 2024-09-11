'''
Simula el lanzamiento de un dado de seis caras y muestra el resultado. Permite al usuario lanzar el dado tantas veces como quiera.
'''

import random

def lanzar_dado():
    return random.randint(1, 6)

def simular_lanzamiento():
    while True:
        resultado = lanzar_dado()
        print(f"El dado muestra: {resultado}")
        
        continuar = input("¿Quieres lanzar el dado nuevamente? (s/n): ").lower()
        if continuar != 's':
            print("¡Gracias por jugar!")
            break

simular_lanzamiento()
