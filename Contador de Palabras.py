'''
Un programa que recibe un texto como entrada y cuenta el número de palabras, caracteres, y la frecuencia de cada palabra.
'''

import string
from collections import Counter

def analizar_texto(texto):
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    
    palabras = texto_limpio.split()
    
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    
    frecuencia_palabras = Counter(palabras)
    
    return num_palabras, num_caracteres, frecuencia_palabras

texto = input("Ingrese un texto: ")

num_palabras, num_caracteres, frecuencia_palabras = analizar_texto(texto)

print(f"\nNúmero total de palabras: {num_palabras}")
print(f"Número total de caracteres: {num_caracteres}")
print("\nFrecuencia de cada palabra:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")

analizar_texto(texto)