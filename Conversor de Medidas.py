'''
Un programa que convierte entre diferentes unidades de medida, como metros a pies, kilogramos a libras o grados Celsius a Fahrenheit.
'''

def conversor_unidades():
    print("--- CONVERSOR DE UNIDADES ---\n")

    print("¿Que quiere convertir?")
    print("1. Metros a Pies \n 2. Kilogramos a Libras \n 3. Grados Celsius a Fahrenheit")
    convertir = input("")

    numero = float(input("Introduce el dato: "))

    metros_pies = (numero * 3.281)
    kilogramos_libras = (numero * 2.205)
    celsius_fahrenheir = ((numero * 9 / 5) + 32)

    if convertir == "1":
        print("Operación seleccionada -> METROS A PIES")
        print(f"La conversión de {numero} metros a pies es: {metros_pies}")
    elif convertir == "2":
        print("Operación seleccionada -> KILOGRAMOS A LIBRAS")
        print(f"La conversión de {numero} kilogramos a libras es: {kilogramos_libras}")
    elif convertir == "3":
        print("Operación seleccionada -> GRADOS CELSIUS A FAHRENHEIT")
        print(f"La conversión de {numero} grados celsius a fahrenheit es: {celsius_fahrenheir}")
    else:
        print("Introduce un número entre el 1 y el 3.")

conversor_unidades()