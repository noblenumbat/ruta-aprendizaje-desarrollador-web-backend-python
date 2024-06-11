# Función recursiva para Torre de Hanoi

def hanoi(discos, origen,auxiliar,destino):
    if discos == 1:
        print('Mover disco {} desde torre {} a torre {}.'.format(discos,origen,destino))
        return
    # Aquí sucede la magia de la recursión 🫣

    hanoi(discos -1, origen, destino, auxiliar)
    print('Mover disco {} desde torre {} a torre {}.'.format(discos,origen,destino))
    hanoi(discos -1, auxiliar, origen, destino)

# Controlador
discos = int(input('Número de discos a desplazar: '))

# Llamada
print(hanoi(3,'A','B','C'))
