'''
Un programa que permite al usuario agregar, eliminar y ver tareas en una lista. Las tareas pueden guardarse en un archivo para que persistan entre sesiones.
'''

import os

ARCHIVO_TAREAS = "tareas.txt"

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as archivo:
            tareas = archivo.read().splitlines()
    else:
        tareas = []
    return tareas

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def agregar_tarea(tareas):
    nueva_tarea = input("Escribe la nueva tarea: ")
    tareas.append(nueva_tarea)
    print(f"Tarea '{nueva_tarea}' agregada.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Elige el número de la tarea que deseas eliminar: ")) - 1
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    except (ValueError, IndexError):
        print("Entrada inválida. Intenta de nuevo.")

def ver_tareas(tareas):
    if not tareas:
        print("No tienes tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def menu():
    print("\n1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

def gestor_tareas():
    tareas = cargar_tareas()
    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

gestor_tareas()
