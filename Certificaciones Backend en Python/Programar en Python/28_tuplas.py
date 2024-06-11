my_tuple = (1, 'strings', 'strings', 4.5, True) # recomendable usar parentesis

print(my_tuple[1])
print(type(my_tuple))

print(my_tuple.count('strings')) # cuenta las veces que aparece un elemento. Ejemplo 2 

print(my_tuple.index(4.5)) # devuelve el indice donde se encuentra el elemento. Ejemplo: 3

#Nota. NO se puede cambiar el elemento de una tupla.
#TypeError: 'tuple' object does not support item assignment
#my_tuple[1] = 'cadena'

for x in my_tuple:
    print(x)
