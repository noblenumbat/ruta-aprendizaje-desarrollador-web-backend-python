import time
import threading

from scan_pool  import scanner_pool, guardar_hoja


print(" __________________________________")          
print("|_____________Escaner______________|")
primera_hoja = input("Inserte una hoja en el cristal y presione ENTER : ")


def escaner(cant):
    if cant == "":
        print("Escaneando ...")
        time.sleep(1)
        print("Escaneando ... ...")
        time.sleep(1)
        print("Escaneando ... ... ...")
        time.sleep(1)

        # Guarda hoja
        guardar_hoja()

        temporizador(59)

def temporizador(segundos):
    input_recibido = None

    # Función que se ejecutará en un hilo para capturar la entrada del usuario
    def obtener_input():
        nonlocal input_recibido
        input_recibido = input("\n")  # Captura la entrada del usuario

    # Crear un hilo para capturar la entrada sin bloquear el temporizador
    hilo_input = threading.Thread(target=obtener_input)
    hilo_input.daemon = True  # Permite que el hilo se cierre cuando el programa principal termine
    hilo_input.start()

    while segundos > 0:
        print(f'\rInserte otra hoja en {segundos} o presione 0 para terminar :', end='')

        if input_recibido is not None:
            if input_recibido == "0":
                print('\n')
                print('\nTrabajo de escaner terminado! 😝')
                mostrar_escaneo()
                return
            elif input_recibido == '':
                print('\nHoja insertada, continuando escaneo...')
                escaner('')  # Continúa escaneando más hojas
                return

        time.sleep(1)  # Espera 1 segundo antes de decrementar el contador
        segundos -= 1

    print('\nEl tiempo ha terminado. Ejecución del otro código...')
    mostrar_escaneo()

# Función que se ejecuta cuando el temporizador llega a 0 o se presiona '#'
def mostrar_escaneo():
    
    # aquí se retorna el diccionario que representa las hojas escaneadas
    # print(scanner_pool)
    num_lineas = len(scanner_pool[0]) # se puede obtener la longitud del sublista en el indice cero que es 3
    
    for i in range(num_lineas):
        for figure in scanner_pool:
            print(figure[i], end=' ') # Imprimir cada línea de cada figura en la misma fila
        print() # Salto de fila despues de imprimir todas las figuras de una fila

# Llamada inicial al escáner
escaner(primera_hoja)
