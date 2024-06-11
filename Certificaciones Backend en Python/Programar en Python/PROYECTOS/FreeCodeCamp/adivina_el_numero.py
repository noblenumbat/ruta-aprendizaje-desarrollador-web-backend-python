import random


def adivina_el_numero(x): # x representa el límite sup del rango

    print("=========================")
    print("Bienvenido(a) al juego! ")
    print("=========================")
    print("Tu meta es averigurar el número generado por la computadora.")

    # python docs random module
    numero_aleatorio = random.randint(1, x) # número aleatorio entre 1 y x.

    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario ingresa un número
        prediccion = int(input(f"Advina un número entre 1 y {x}: ")) # f-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. ESte número es muy grande.")
    
    print(f"¡Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10)