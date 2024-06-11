# devices = ['Hard Disk','RAM','CPU','Motherboard','Graphic Acelerator']
# print(sorted(devices))

coffees = ['Espresso','Latte','Cappuccino','Macchiato','Americano','Decaf']

# print(coffees[::-1]) # slicing ::-1 invierte una secuencia
# # Output
# # ['Decaf', 'Americano', 'Macchiato', 'Cappuccino', 'Latte', 'Espresso']

# print(coffees[::-2]) # slicing ::-2 invierte una secuencia con un itervalo de dos
# # Output
# # ['Decaf', 'Macchiato', 'Latte']
# Custom function

# ----------------------------------------------------------------------------
# Esta función coje cada elemento y lo invierte
def reverse(str):
    return str[::-1]

# Esta otra coje la función de arriba como argumento y le pasa la variable que contiene una lista.
# Luego que le pasa la lista, map() hace su trabajo.
reversed_coffees = map(reverse, coffees)

# print(list(reversed_coffees)) # lista es una bacaneria: imprime un lista 😛
# ['osserpsE', 'ettaL', 'oniccuppaC', 'otaihccaM', 'onaciremA', 'faceD']

for x in reversed_coffees:
    print (x) # imprime cada elemento de la lista como un string