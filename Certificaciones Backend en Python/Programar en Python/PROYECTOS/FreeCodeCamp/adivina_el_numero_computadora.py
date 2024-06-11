import random

def adivina_el_numero_computadora(x):

    print("==========================")
    print(" ¡Bienvenido(a) al Juego! ")
    print("==========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # también podría ser el límite superior.
        
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
    
        if respuesta == "a":
            if prediccion == limite_inferior:
                print("🤨 No puede ser, este es el número mas bajo. Tu número debe ser mayor, Fin del Juego!")
                adivina_el_numero_computadora(x)
                #break 
            else:
                limite_superior = prediccion - 1
        elif respuesta == "b":
            if prediccion == limite_superior:
                print(" 🤨 No puede ser, este es el número mas alto. Tu número debe ser menor, Fin del Juego!")
                adivina_el_numero_computadora(x)
                #break
            else:
                limite_inferior = prediccion + 1

        elif respuesta == "c":
            print(f"🥳 ¡Esoo! La computadora adivino tu número correctamente: {prediccion}")
        else:
            print("😾 Entrada no válida. Por favor ingresa A, B o C.")

        # Si es muy bajo
        # Intervalo inicial: [1, 10]
        # Predicción: 6
        # Respuesta: "a"
        # Intervalo: [1, 5]

        # Si es muy alto
        # Intervalo inicial: [1, 10]
        # Predicción: 6
        # Respuesta: "b"
        # Intervalo: [7, 10]

adivina_el_numero_computadora(10)