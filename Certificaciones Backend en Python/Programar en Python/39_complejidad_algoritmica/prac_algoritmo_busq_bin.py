# Consejo: Hay que buscar la solución para el peor caso.
# Encontrar una forma de descartar, que la búsqueda sea más eficiente.

# 1. Hacer que funcione. Es lo más importante.
# 2. Lanzar el programa
# 3. Revisar de nuevo el código (para optimizar partes de código)
#------------------------------------------------------------------------------

#Algoritmo de búsqueda binaria.

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]

# 1. Tener nuestra lista ordenada para poder realizar la busqueda
lista.sort()
print(lista)

# 1. Buscar el punto medio (puntero)
# 2. Comprobar si el punto medio es el número que buscamos 
# 3. Si el valor que buscamos es mayor al puntero, inicio va a ser igual al puntero + 1
# 4. Si el valor que buscamos es menor al puntero, final va a ser igual al puntero -1 
# 5. Si inicio es mayor o igual que final entonces el valor no se encuentra en la lista


def busqueda_binaria(valor):
    inicio = 0
    final = len(lista)-1
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero 
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None

# def buscar_valor(valor):
#     res_busqueda = busqueda_binaria(valor)
#     if res_busqueda is None:
#         return f"El número {valor} no se encontró."
#     else:
#         return f"El numero {valor} se encuentra en la posición {res_busqueda}"
    
def buscar_valor():
    try:
        valor = int(input('Ingrese un número: '))
            
        res_busqueda = busqueda_binaria(valor)
        
        if res_busqueda is None:
            return f"El número {valor} no se encontró."
        else:
            return f"El numero {valor} se encuentra en la posición {res_busqueda}"
    except:
        return f"Entrada no válida:", ValueError
    
        
contador = 0

while contador >= 0:
    interruptor = input("Elija una opción\n----------------\n1. Iniciar programa \n2. Terminar programa: " )
    if interruptor == '1':
        print(buscar_valor())
    else:
        contador = -1
        print('Gracias por probar el programa!')

    
    
           



