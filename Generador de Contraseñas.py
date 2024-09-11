'''
Crea un programa que genere contraseñas aleatorias basadas en los requisitos del usuario, como longitud, 
inclusión de caracteres especiales, números y letras mayúsculas.
'''

import random
import string

def generar_contraseña(longitud, incluir_especiales, incluir_numeros, incluir_mayusculas):
    caracteres = string.ascii_lowercase 

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  

    if incluir_numeros:
        caracteres += string.digits  

    if incluir_especiales:
        caracteres += string.punctuation 

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def solicitar_requisitos():
    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
    incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'

    return longitud, incluir_especiales, incluir_numeros, incluir_mayusculas

longitud, incluir_especiales, incluir_numeros, incluir_mayusculas = solicitar_requisitos()

contraseña = generar_contraseña(longitud, incluir_especiales, incluir_numeros, incluir_mayusculas)

print("Contraseña generada:", contraseña)
