import random
import time


def busq_ingenua(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1

mi_lista = [4,7,9,10]

# print(busq_ingenua(mi_lista,20))

def busqueda_binaria(lista,objetivo,limite_inferior=None,limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista)-1

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2 # el operador // da como resultado una división sin resto

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista,objetivo,limite_inferior,punto_medio-1)
    else:
        return busqueda_binaria(lista,objetivo,punto_medio+1,limite_superior)

if __name__=='__main__':

    # Crear una lista ordenada con 100000 números aleatorios.
    tamaño = 100000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de búsqueda ingenua.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busq_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua {fin - inicio} segundos.")

    # Medir el tiempo de búsqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria {fin - inicio} segundos.")

