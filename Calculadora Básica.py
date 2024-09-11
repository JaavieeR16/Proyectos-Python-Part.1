'''
Un programa que permite al usuario ingresar dos números y luego seleccionar una operación (suma, resta, multiplicación o división). 
El programa realiza la operación y muestra el resultado.
'''        

def calculadora_basica():
    print("*** CALCULADORA BÁSICA ***\n")

    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))

    print("¿Que operación quiere realizar?")
    print("1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División")
    operacion = input("")

    suma = (numero1 + numero2)
    resta = (numero1 - numero2)
    multiplicacion = (numero1 * numero2)
    division = (numero1 / numero2)

    if operacion == "1":
        print("Operación seleccionada -> SUMA")
        print(f"{numero1} + {numero2} = {suma}")
    elif operacion == "2":
        print("Operación seleccionada -> RESTA")
        print(f"{numero1} - {numero2} = {resta}")
    elif operacion == "3":
        print("Operación seleccionada -> MULTIPLICACIÓN")
        print(f"{numero1} x {numero2} = {multiplicacion}")
    elif operacion == "4":
        print("Operación seleccionada -> DIVISIÓN")
        print(f"{numero1} / {numero2} = {division}")
    else:
        print("Introduce un número entre el 1 y el 4.")

calculadora_basica()